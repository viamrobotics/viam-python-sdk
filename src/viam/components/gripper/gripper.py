import abc
from dataclasses import dataclass
from typing import Any, Dict, Final, List, Optional

from viam.components import KinematicsReturn
from viam.components.component_base import ComponentBase
from viam.errors import MethodNotImplementedError
from viam.proto.common import KinematicModel
from viam.resource.types import API, RESOURCE_NAMESPACE_RDK, RESOURCE_TYPE_COMPONENT


class Gripper(ComponentBase):
    """
    Gripper represents a physical robotic gripper.

    This acts as an abstract base class for any drivers representing specific
    gripper implementations. This cannot be used on its own. If the ``__init__()`` function is
    overridden, it must call the ``super().__init__()`` function.

    ::

        from viam.components.gripper import Gripper

    For more information, see `Gripper component <https://docs.viam.com/reference/apis/components/gripper/>`_.
    """

    API: Final = API(  # pyright: ignore [reportIncompatibleVariableOverride]
        RESOURCE_NAMESPACE_RDK, RESOURCE_TYPE_COMPONENT, "gripper"
    )

    @dataclass
    class HoldingStatus:
        """
        HoldingStatus represents whether the gripper is currently holding onto an object. The
        additional ``meta`` attribute contains other optional contextual information (i.e. confidence
        interval, pressure, etc.)
        """

        is_holding_something: bool
        meta: Optional[Dict[str, Any]] = None

    @abc.abstractmethod
    async def open(
        self,
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ):
        """
        Open the gripper.

        ::

            my_gripper = Gripper.from_robot(robot=machine, name="my_gripper")

            # Open the gripper.
            await my_gripper.open()

        For more information, see `Gripper component <https://docs.viam.com/reference/apis/components/gripper/#open>`_.
        """
        ...

    @abc.abstractmethod
    async def grab(
        self,
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ) -> bool:
        """
        Instruct the gripper to grab.

        ::

            my_gripper = Gripper.from_robot(robot=machine, name="my_gripper")

            # Grab with the gripper.
            grabbed = await my_gripper.grab()

        Returns:
            bool: Indicates if the gripper grabbed something.

        For more information, see `Gripper component <https://docs.viam.com/reference/apis/components/gripper/#grab>`_.
        """
        ...

    @abc.abstractmethod
    async def is_holding_something(
        self,
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ) -> HoldingStatus:
        """
        Get information about whether the gripper is currently holding onto an object.

        ::

            my_gripper = Gripper.from_robot(robot=machine, name="my_gripper")

            # Grab with the gripper.
            holding_status = await my_gripper.is_holding_something()
            # get the boolean result
            is_holding_something = holding_status.is_holding_something

        Returns:
            HoldingStatus: see documentation on `HoldingStatus` for more information

        For more information, see `Gripper component <https://docs.viam.com/reference/apis/components/gripper/#grab>`_.

        """

    @abc.abstractmethod
    async def stop(
        self,
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ):
        """
        Stop the gripper. It is assumed the gripper stops immediately.

        ::

            my_gripper = Gripper.from_robot(robot=machine, name="my_gripper")

            # Stop the gripper.
            await my_gripper.stop()

        For more information, see `Gripper component <https://docs.viam.com/reference/apis/components/gripper/#stop>`_.
        """
        ...

    @abc.abstractmethod
    async def is_moving(self) -> bool:
        """
        Get if the gripper is currently moving.

        ::

            my_gripper = Gripper.from_robot(robot=machine, name="my_gripper")

            # Check whether the gripper is currently moving.
            moving = await my_gripper.is_moving()
            print('Moving:', moving)

        Returns:
            bool: Whether the gripper is moving.

        For more information, see `Gripper component <https://docs.viam.com/reference/apis/components/gripper/#ismoving>`_.
        """
        ...

    async def get_kinematics(
        self,
        *,
        include_collision_meshes: bool = False,
        include_visual_meshes: bool = False,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ) -> KinematicsReturn:
        """
        Get the kinematics information associated with the gripper.

        .. deprecated:: 0.86.0
            Use ``get_kinematic_model``, which returns the typed model. A new gripper implements that method and leaves this one alone.

        ::

            my_gripper = Gripper.from_robot(robot=machine, name="my_gripper")

            # Get the kinematics information associated with the gripper.
            kinematics = await my_gripper.get_kinematics()

            # Get the format of the kinematics file.
            k_file = kinematics[0]

            # Get the byte contents of the file.
            k_bytes = kinematics[1]

        Args:
            include_collision_meshes (bool): Include collision mesh bytes in the response. Otherwise meshes carry only their path.
            include_visual_meshes (bool): Include visual mesh bytes in the response.

        Returns:
            Tuple[KinematicsFileFormat.ValueType, bytes]: A tuple containing two values; the first [0] value represents the format of the
            file, either in URDF format (``KinematicsFileFormat.KINEMATICS_FILE_FORMAT_URDF``) or
            Viam's kinematic parameter format (spatial vector algebra) (``KinematicsFileFormat.KINEMATICS_FILE_FORMAT_SVA``),
            and the second [1] value represents the byte contents of the file.
            If available, a third [2] value provides meshes keyed by URDF filepath.
            If available, a fourth [3] value provides the structured ``KinematicModel`` (links, joints, output frames, and properties).

        For more information, see `Gripper component <https://docs.viam.com/reference/apis/components/gripper/#getkinematics>`_.
        """
        raise MethodNotImplementedError("get_kinematics")

    async def get_kinematic_model(
        self,
        *,
        include_collision_meshes: bool = False,
        include_visual_meshes: bool = False,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ) -> KinematicModel:
        """
        Get the kinematic model of the gripper: its links, joints with their limits, output frames and properties.
        Lengths are in millimeters and angles in degrees.

        ::

            my_gripper = Gripper.from_robot(robot=machine, name="my_gripper")

            model = await my_gripper.get_kinematic_model()

            for joint in model.joints:
                print(joint.id, joint.limits.min, joint.limits.max, joint.limits.max_velocity)

        A module implements this by returning the model it holds, which ``viam.kinematics.read_kinematic_model_file`` reads from a
        kinematic model file. It may ignore the two flags and return every mesh, since the server drops the bytes a request did not
        ask for and fills the deprecated file fields for a client that predates the model.

        Args:
            include_collision_meshes (bool): Include collision mesh bytes. Otherwise a collision mesh carries only its path and
                content type.
            include_visual_meshes (bool): Include visual mesh bytes. Otherwise a visual mesh carries only its path and content type.
                With neither flag set a server sends every mesh whole, as it did before the flags existed, so set one to leave the
                other out.

        Raises:
            NotSupportedError: If the gripper is served by a machine that predates the model and sent only the kinematics file, which
                ``get_kinematics`` still returns.

        Returns:
            KinematicModel: The kinematic model of the gripper.
        """
        raise MethodNotImplementedError("get_kinematic_model")

    @abc.abstractmethod
    async def get_current_inputs(
        self,
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ) -> List[float]:
        """
        Get the current input values of the gripper.

        ::

            my_gripper = Gripper.from_robot(robot=machine, name="my_gripper")

            # Get the current input values of the gripper.
            inputs = await my_gripper.get_current_inputs()

        Returns:
            List[float]: The current input values of the gripper.

        For more information, see `Gripper component <https://docs.viam.com/reference/apis/components/gripper/>`_.
        """
        ...

    @abc.abstractmethod
    async def go_to_inputs(
        self,
        values: List[float],
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ):
        """
        Move the gripper to the specified input values.

        ::

            my_gripper = Gripper.from_robot(robot=machine, name="my_gripper")

            # Move the gripper to specific input values.
            await my_gripper.go_to_inputs([0.5, 0.8])

        Args:
            values (List[float]): The input values to move the gripper to.

        For more information, see `Gripper component <https://docs.viam.com/reference/apis/components/gripper/>`_.
        """
        ...
