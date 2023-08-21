from typing import Any, Final, List, Mapping, Optional, Sequence

from grpclib.client import Channel

from viam.proto.common import (
    DoCommandRequest,
    DoCommandResponse,
    GeoObstacle,
    GeoPoint,
    Pose,
    PoseInFrame,
    ResourceName,
    Transform,
    WorldState,
)
from viam.proto.service.motion import (
    Constraints,
    GetPoseRequest,
    GetPoseResponse,
    MotionConfiguration,
    MotionServiceStub,
    MoveOnGlobeRequest,
    MoveOnGlobeResponse,
    MoveOnMapRequest,
    MoveOnMapResponse,
    MoveRequest,
    MoveResponse,
)
from viam.resource.rpc_client_base import ReconfigurableResourceRPCClientBase
from viam.resource.types import RESOURCE_NAMESPACE_RDK, RESOURCE_TYPE_SERVICE, Subtype
from viam.services.service_client_base import ServiceClientBase
from viam.utils import ValueTypes, dict_to_struct, struct_to_dict


class MotionClient(ServiceClientBase, ReconfigurableResourceRPCClientBase):
    """Motion is a Viam service that coordinates motion planning across all of the components in a given robot.

    The motion planning service calculates a valid path that avoids self collision by default. If additional constraints are supplied in the
    ``world_state`` message, the motion planning service will also account for those.
    """

    SUBTYPE: Final = Subtype(RESOURCE_NAMESPACE_RDK, RESOURCE_TYPE_SERVICE, "motion")
    client: MotionServiceStub

    def __init__(self, name: str, channel: Channel):
        super().__init__(name, channel)
        self.client = MotionServiceStub(channel)

    async def move(
        self,
        component_name: ResourceName,
        destination: PoseInFrame,
        world_state: Optional[WorldState] = None,
        constraints: Optional[Constraints] = None,
        *,
        extra: Optional[Mapping[str, Any]] = None,
        timeout: Optional[float] = None,
    ) -> bool:
        """Plan and execute a movement to move the component specified to its goal destination.

        Note: Frames designated with respect to components can also be used as the ``component_name`` when calling for a move. This
        technique allows for planning and moving the frame itself to the ``destination``. To do so, simply create a resource name with
        originating ReferenceFrame's name. Then pass in the resource name into ``component_name``. Ex::

            resource_name = Arm.get_resource_name("externalFrame")
            success = await MotionServiceClient.move(resource_name, ...)

        Args:
            component_name (viam.proto.common.ResourceName): Name of a component on a given robot.
            destination (viam.proto.common.PoseInFrame): The destination to move to, expressed as a ``Pose`` and the frame in which it was
                observed.
            world_state (viam.proto.common.WorldState): When supplied, the motion service will create a plan that obeys any contraints
                expressed in the WorldState message.
            constraints (viam.proto.service.motion.Constraints): When supplied, the motion service will create a plan that obeys any
                specified constraints

        Returns:
            bool: Whether the move was successful
        """
        if extra is None:
            extra = {}
        request = MoveRequest(
            name=self.name,
            destination=destination,
            component_name=component_name,
            world_state=world_state,
            constraints=constraints,
            extra=dict_to_struct(extra),
        )
        response: MoveResponse = await self.client.Move(request, timeout=timeout)
        return response.success

    async def move_on_globe(
        self,
        component_name: ResourceName,
        destination: GeoPoint,
        movement_sensor_name: ResourceName,
        obstacles: Optional[Sequence[GeoObstacle]] = None,
        heading: Optional[float] = None,
        configuration: Optional[MotionConfiguration] = None,
        *,
        extra: Optional[Mapping[str, ValueTypes]] = None,
        timeout: Optional[float] = None,
    ) -> bool:
        """Move a component to a specific latitude and longitude, using a ``MovementSensor`` to check the location.

        Args:
            component_name (ResourceName): The component to move
            destination (GeoPoint): The destination point
            movement_sensor_name (ResourceName): The ``MovementSensor`` which will be used to check robot location
            obstacles (Optional[Sequence[GeoObstacle]], optional): Obstacles to be considered for motion planning. Defaults to None.
            heading (Optional[float], optional): Compass heading to achieve at the destination, in degrees [0-360). Defaults to None.
            linear_meters_per_sec (Optional[float], optional): Linear velocity to target when moving. Defaults to None.
            angular_deg_per_sec (Optional[float], optional): Angular velocity to target when turning. Defaults to None.

        Returns:
            bool: Whether the request was successful
        """
        if extra is None:
            extra = {}
        request = MoveOnGlobeRequest(
            name=self.name,
            component_name=component_name,
            destination=destination,
            movement_sensor_name=movement_sensor_name,
            obstacles=obstacles,
            heading=heading,
            motion_configuration=configuration,
            extra=dict_to_struct(extra),
        )
        response: MoveOnGlobeResponse = await self.client.MoveOnGlobe(request, timeout=timeout)
        return response.success

    async def move_on_map(
        self,
        component_name: ResourceName,
        destination: Pose,
        slam_service_name: ResourceName,
        *,
        extra: Optional[Mapping[str, ValueTypes]] = None,
        timeout: Optional[float] = None,
    ) -> bool:
        """Move a component to a specific pose, using a ``SlamService`` for the SLAM map

        Args:
            component_name (ResourceName): The component to move
            destination (Pose): The destination, which can be any pose with respect to the SLAM map's origin
            slam_service_name (ResourceName): The slam service from which the SLAM map is requested

        Returns:
            bool: Whether the request was successful
        """
        if extra is None:
            extra = {}
        request = MoveOnMapRequest(
            name=self.name,
            destination=destination,
            component_name=component_name,
            slam_service_name=slam_service_name,
            extra=dict_to_struct(extra),
        )
        response: MoveOnMapResponse = await self.client.MoveOnMap(request, timeout=timeout)
        return response.success

    async def get_pose(
        self,
        component_name: ResourceName,
        destination_frame: str,
        supplemental_transforms: Optional[List[Transform]] = None,
        *,
        extra: Optional[Mapping[str, Any]] = None,
        timeout: Optional[float] = None,
    ) -> PoseInFrame:
        """
        Get the Pose and observer frame for any given component on a robot. A ``component_name`` can be created like this::

            component_name = Arm.get_resource_name("arm")

        Note that the example uses the ``Arm`` class, but any component class that inherits from ``ComponentBase`` will work
        (``Base``, ``Gripper``, etc).


        Args:
            component_name (viam.proto.common.ResourceName): Name of a component on a robot.
            destination_frame (str): Name of the desired reference frame.
            supplemental_transforms (Optional[List[viam.proto.common.Transform]]): Transforms used to augment the robot's frame while
                calculating pose.

        Returns:
            ``Pose`` (PoseInFrame): Pose of the given component and the frame in which it was observed.
        """
        if extra is None:
            extra = {}
        request = GetPoseRequest(
            name=self.name,
            component_name=component_name,
            destination_frame=destination_frame,
            supplemental_transforms=supplemental_transforms,
            extra=dict_to_struct(extra),
        )
        response: GetPoseResponse = await self.client.GetPose(request, timeout=timeout)
        return response.pose

    async def do_command(self, command: Mapping[str, ValueTypes], *, timeout: Optional[float] = None) -> Mapping[str, ValueTypes]:
        """Send/receive arbitrary commands

        Args:
            command (Dict[str, ValueTypes]): The command to execute

        Returns:
            Dict[str, ValueTypes]: Result of the executed command
        """
        request = DoCommandRequest(name=self.name, command=dict_to_struct(command))
        response: DoCommandResponse = await self.client.DoCommand(request, timeout=timeout)
        return struct_to_dict(response.result)
