import abc
from typing import Any, Dict, Final, List, Optional

from viam.components import KinematicsReturn
from viam.components.component_base import ComponentBase
from viam.errors import MethodNotImplementedError
from viam.proto.common import KinematicModel
from viam.resource.types import API, RESOURCE_NAMESPACE_RDK, RESOURCE_TYPE_COMPONENT


class Gantry(ComponentBase):
    """
    Gantry represents a physical Gantry and can be used for controlling gantries of N axes.

    This acts as an abstract base class for any drivers representing specific
    gantry implementations. This cannot be used on its own. If the ``__init__()`` function is
    overridden, it must call the ``super().__init__()`` function.

    ::

        from viam.components.gantry import Gantry

    For more information, see `Gantry component <https://docs.viam.com/reference/apis/components/gantry/>`_.
    """

    API: Final = API(  # pyright: ignore [reportIncompatibleVariableOverride]
        RESOURCE_NAMESPACE_RDK, RESOURCE_TYPE_COMPONENT, "gantry"
    )

    @abc.abstractmethod
    async def get_position(self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs) -> List[float]:
        """
        Get the positions of the axes of the gantry in millimeters.

        ::

            my_gantry = Gantry.from_robot(robot=machine, name="my_gantry")

            # Get the current positions of the axes of the gantry in millimeters.
            positions = await my_gantry.get_position()

        Returns:
            List[float]: A list of the position of the axes of the gantry in millimeters.

        For more information, see `Gantry component <https://docs.viam.com/reference/apis/components/gantry/#getposition>`_.
        """
        ...

    @abc.abstractmethod
    async def move_to_position(
        self,
        positions: List[float],
        speeds: List[float],
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ):
        """
        Move the axes of the gantry to the desired positions (mm) at the requested speeds (mm/sec).

        ::

            my_gantry = Gantry.from_robot(robot=machine, name="my_gantry")

            # Create a list of positions for the axes of the gantry to move to. Assume in
            # this example that the gantry is multi-axis, with 3 axes.
            examplePositions = [1, 2, 3]

            exampleSpeeds = [3, 9, 12]

            # Move the axes of the gantry to the positions specified.
            await my_gantry.move_to_position(
                positions=examplePositions, speeds=exampleSpeeds)

        Args:
            positions (List[float]): A list of positions for the axes of the gantry to move to, in millimeters.
            speeds (List[float]): A list of speeds in millimeters per second for the gantry to move at respective to each axis.

        For more information, see `Gantry component <https://docs.viam.com/reference/apis/components/gantry/#movetoposition>`_.
        """
        ...

    @abc.abstractmethod
    async def home(self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs) -> bool:
        """
        Run the homing sequence of the gantry to re-calibrate the axes with respect to the limit switches.

        ::

            my_gantry = Gantry.from_robot(robot=machine, name="my_gantry")

            await my_gantry.home()

        Returns:
            bool: Whether the gantry has run the homing sequence successfully.

        For more information, see `Gantry component <https://docs.viam.com/reference/apis/components/gantry/#home>`_.
        """

    @abc.abstractmethod
    async def get_lengths(self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs) -> List[float]:
        """
        Get the lengths of the axes of the gantry in millimeters.

        ::

            my_gantry = Gantry.from_robot(robot=machine, name="my_gantry")

            # Get the lengths of the axes of the gantry in millimeters.
            lengths_mm = await my_gantry.get_lengths()

        Returns:
            List[float]: A list of the lengths of the axes of the gantry in millimeters.

        For more information, see `Gantry component <https://docs.viam.com/reference/apis/components/gantry/#getlengths>`_.
        """
        ...

    @abc.abstractmethod
    async def stop(self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs):
        """
        Stop all motion of the gantry. It is assumed that the gantry stops immediately.

        ::

            my_gantry = Gantry.from_robot(robot=machine, name="my_gantry")

            # Stop all motion of the gantry. It is assumed that the gantry stops
            # immediately.
            await my_gantry.stop()

        For more information, see `Gantry component <https://docs.viam.com/reference/apis/components/gantry/#stop>`_.
        """
        ...

    @abc.abstractmethod
    async def is_moving(self) -> bool:
        """
        Get if the gantry is currently moving.

        ::

            my_gantry = Gantry.from_robot(robot=machine, name="my_gantry")

            # Stop all motion of the gantry. It is assumed that the
            # gantry stops immediately.
            await my_gantry.stop()

            # Print if the gantry is currently moving.
            print(await my_gantry.is_moving())

        Returns:
            bool: Whether the gantry is moving.

        For more information, see `Gantry component <https://docs.viam.com/reference/apis/components/gantry/#ismoving>`_.
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
        Get the kinematics information associated with the gantry.

        .. deprecated:: 0.86.0
            Use ``get_kinematic_model``, which returns the typed model. A new gantry implements that method and leaves this one alone.

        ::

            my_gantry = Gantry.from_robot(robot=machine, name="my_gantry")

            # Get the kinematics information associated with the gantry.
            kinematics = await my_gantry.get_kinematics()

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

        For more information, see `Arm component <https://docs.viam.com/reference/apis/components/arm/#getkinematics>`_.
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
        Get the kinematic model of the gantry: its links, joints with their limits, output frames and properties.
        Lengths are in millimeters and angles in degrees.

        ::

            my_gantry = Gantry.from_robot(robot=machine, name="my_gantry")

            model = await my_gantry.get_kinematic_model()

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
            NotSupportedError: If the gantry is served by a machine that predates the model and sent only the kinematics file, which
                ``get_kinematics`` still returns.

        Returns:
            KinematicModel: The kinematic model of the gantry.
        """
        raise MethodNotImplementedError("get_kinematic_model")
