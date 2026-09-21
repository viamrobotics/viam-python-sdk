import abc
from typing import TYPE_CHECKING, Any, Final, List, Mapping, Optional, Sequence, cast

from typing_extensions import Self

from viam.errors import ResourceNotFoundError
from viam.proto.common import PoseInFrame, ResourceName, Transform
from viam.proto.robot import FrameSystemConfig
from viam.resource.base import ResourceBase
from viam.resource.types import API, RESOURCE_NAMESPACE_RDK_INTERNAL, RESOURCE_TYPE_SERVICE

from ..service_base import ServiceBase

if TYPE_CHECKING:
    from viam.robot.client import RobotClient


class FrameSystem(ServiceBase):
    """FrameSystem gives access to the machine's frame system: the tree of reference frames viam-server builds from the frame
    configuration of every component.

    viam-server serves the frame system on the robot service itself, so there is exactly one per machine, named ``$framesystem``, and it
    is never listed in ``RobotClient.resource_names``. Get it with ``FrameSystem.from_robot(machine)`` from a client, or with
    ``FrameSystem.from_dependencies(dependencies)`` inside a modular resource constructor.

    For more information, see `Machine Management API <https://docs.viam.com/appendix/apis/robot/>`_.
    """

    API: Final = API(  # pyright: ignore [reportIncompatibleVariableOverride]
        RESOURCE_NAMESPACE_RDK_INTERNAL, RESOURCE_TYPE_SERVICE, "frame_system"
    )

    PUBLIC_NAME: Final = "$framesystem"
    """The name of the machine's frame system. The ``$`` prefix marks it as reserved, so no user configured resource can take it."""

    @classmethod
    def from_robot(cls, robot: "RobotClient", name: str = PUBLIC_NAME) -> Self:
        """Get the frame system of the provided robot.

        ::

            frame_system = FrameSystem.from_robot(robot=machine)
            gripper_pose = await frame_system.get_pose("my_gripper")

        Args:
            robot (RobotClient): The robot
            name (str): The name of the frame system. There is only one, so this defaults to ``$framesystem``.

        Returns:
            Self: The frame system
        """
        return super().from_robot(robot, name)

    @classmethod
    def from_dependencies(cls, dependencies: Mapping[ResourceName, ResourceBase]) -> Self:
        """Get the frame system from a mapping of dependencies, such as the one handed to a modular resource constructor.

        ::

            @classmethod
            def new(cls, config: ComponentConfig, dependencies: Mapping[ResourceName, ResourceBase]) -> Self:
                gizmo = cls(config.name)
                gizmo.frame_system = FrameSystem.from_dependencies(dependencies)
                return gizmo

        Args:
            dependencies (Mapping[ResourceName, ResourceBase]): The dependencies to search

        Raises:
            ResourceNotFoundError: Raised if the frame system is not among the dependencies

        Returns:
            Self: The frame system
        """
        frame_system = dependencies.get(cls.get_resource_name(cls.PUBLIC_NAME))
        if frame_system is None:
            raise ResourceNotFoundError(cls.API.resource_subtype, cls.PUBLIC_NAME)
        return cast(cls, frame_system)  # type: ignore

    @abc.abstractmethod
    async def get_frame_system_config(
        self,
        additional_transforms: Optional[Sequence[Transform]] = None,
        *,
        timeout: Optional[float] = None,
    ) -> List[FrameSystemConfig]:
        """
        Get the configuration of the machine's frame system.

        ::

            frame_system = FrameSystem.from_robot(robot=machine)

            # Get a list of each of the reference frames configured on the machine.
            config = await frame_system.get_frame_system_config()
            print(f"frame system configuration: {config}")

        Args:
            additional_transforms (Optional[List[viam.proto.common.Transform]]): Transforms used to augment the machine's frame system
                while building the configuration.

        Returns:
            List[viam.proto.robot.FrameSystemConfig]: The configuration of the machine's frame system.

        For more information, see `Machine Management API <https://docs.viam.com/appendix/apis/robot/>`_.
        """
        ...

    @abc.abstractmethod
    async def get_pose(
        self,
        component_name: str,
        destination_frame: str = "",
        supplemental_transforms: Optional[Sequence[Transform]] = None,
        *,
        extra: Optional[Mapping[str, Any]] = None,
        timeout: Optional[float] = None,
    ) -> PoseInFrame:
        """
        Get the pose of a component in the machine's frame system, expressed in a destination reference frame.

        ::

            frame_system = FrameSystem.from_robot(robot=machine)

            # Get the pose of "my_gripper" relative to the "world" reference frame.
            gripper_pose = await frame_system.get_pose("my_gripper")

            # Get the same pose relative to the origin frame of "my_arm".
            gripper_pose_in_arm = await frame_system.get_pose("my_gripper", destination_frame="my_arm")

        Args:
            component_name (str): The name of the component whose pose should be returned.
            destination_frame (str): The name of the reference frame to express the pose in. An empty string defaults to ``world``.
            supplemental_transforms (Optional[List[viam.proto.common.Transform]]): Transforms used to augment the machine's frame system
                while computing the pose.

        Returns:
            PoseInFrame: The pose of the component and the reference frame it is expressed in.

        For more information, see `Machine Management API <https://docs.viam.com/appendix/apis/robot/>`_.
        """
        ...

    @abc.abstractmethod
    async def transform_pose(
        self,
        query: PoseInFrame,
        destination: str,
        additional_transforms: Optional[Sequence[Transform]] = None,
        *,
        timeout: Optional[float] = None,
    ) -> PoseInFrame:
        """
        Transform a pose from its reference frame into a destination reference frame.

        ::

            from viam.proto.common import Pose, PoseInFrame

            frame_system = FrameSystem.from_robot(robot=machine)

            pose_in_world = PoseInFrame(reference_frame="world", pose=Pose(x=1.0, y=2.0, z=3.0, o_x=0, o_y=0, o_z=1, theta=0))

            # Express the same pose relative to the origin frame of "my_arm".
            pose_in_arm = await frame_system.transform_pose(pose_in_world, "my_arm")

        Args:
            query (viam.proto.common.PoseInFrame): The pose that should be transformed.
            destination (str): The name of the reference frame to transform the given pose to.
            additional_transforms (Optional[List[viam.proto.common.Transform]]): Transforms used to augment the machine's frame system
                while transforming the pose.

        Returns:
            PoseInFrame: The pose expressed in the destination reference frame.

        For more information, see `Machine Management API <https://docs.viam.com/appendix/apis/robot/>`_.
        """
        ...

    @abc.abstractmethod
    async def transform_pcd(
        self,
        point_cloud_pcd: bytes,
        source: str,
        destination: str,
        *,
        timeout: Optional[float] = None,
    ) -> bytes:
        """
        Transform point cloud data from its source reference frame into a destination reference frame.

        ::

            frame_system = FrameSystem.from_robot(robot=machine)

            my_camera = Camera.from_robot(robot=machine, name="my_camera")
            pcd, _ = await my_camera.get_point_cloud()

            transformed_pcd = await frame_system.transform_pcd(pcd, "my_camera", "world")

        Args:
            point_cloud_pcd (bytes): The point cloud data to transform, in PCD format.
            source (str): The name of the reference frame the point cloud data came from, i.e. the camera resource.
            destination (str): The name of the reference frame to transform the given data to, i.e. world.

        Returns:
            bytes: The point cloud data relative to the destination reference frame.

        For more information, see `Machine Management API <https://docs.viam.com/appendix/apis/robot/>`_.
        """
        ...
