import abc
from dataclasses import dataclass
from typing import Any, Dict, Final, List, Mapping, Optional

from viam.components import KinematicsReturn
from viam.components.component_base import ComponentBase
from viam.resource.types import API, RESOURCE_NAMESPACE_RDK, RESOURCE_TYPE_COMPONENT

from . import JointPositions, Mesh, MoveOptions, Pose


class Arm(ComponentBase):
    """
    Arm represents a physical robot arm that exists in three-dimensional space.

    This acts as an abstract base class for any drivers representing specific
    arm implementations. This cannot be used on its own. If the ``__init__()`` function is
    overridden, it must call the ``super().__init__()`` function.

    ::

        from viam.components.arm import Arm
        # To use move_to_position:
        from viam.components.arm import Pose
        # To use move_to_joint_positions and move_through_joint_positions:
        from viam.components.arm import JointPositions
        # To use move_through_joint_positions:
        from viam.components.arm import MoveOptions
        # To use get_3d_models:
        from viam.components.arm import Mesh

    For more information, see `Arm component <https://docs.viam.com/dev/reference/apis/components/arm/>`_.
    """

    @dataclass
    class Properties:
        support_manual_mode: bool = False
        support_cartesian_commands: bool = False

    API: Final = API(RESOURCE_NAMESPACE_RDK, RESOURCE_TYPE_COMPONENT, "arm")  # pyright: ignore [reportIncompatibleVariableOverride]

    @abc.abstractmethod
    async def get_end_position(
        self,
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ) -> Pose:
        """
        Get the current position of the end of the arm expressed as a ``Pose``.

        ::

            my_arm = Arm.from_robot(robot=machine, name="my_arm")

            # Get the end position of the arm as a Pose.
            pos = await my_arm.get_end_position()

        Returns:
            Pose: A representation of the arm's current position as a 6 DOF (six degrees of freedom) pose.
            The ``Pose`` is composed of values for location and orientation with respect to the origin.
            Location is expressed as distance, which is represented by x, y, and z coordinate values.
            Orientation is expressed as an orientation vector, which is represented by o_x, o_y, o_z, and theta values.

        For more information, see `Arm component <https://docs.viam.com/dev/reference/apis/components/arm/#getendposition>`_.
        """
        ...

    @abc.abstractmethod
    async def move_to_position(
        self,
        pose: Pose,
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ):
        """
        Move the end of the arm to the Pose specified in ``pose``.

        ::

            my_arm = Arm.from_robot(robot=machine, name="my_arm")

            # Create a Pose for the arm.
            examplePose = Pose(x=5, y=5, z=5, o_x=5, o_y=5, o_z=5, theta=20)

            # Move your arm to the Pose.
            await my_arm.move_to_position(pose=examplePose)

        Args:
            pose (Pose): The destination ``Pose`` for the arm. The ``Pose`` is composed of values for location and orientation
                with respect to the origin.
                Location is expressed as distance, which is represented by x, y, and z coordinate values.
                Orientation is expressed as an orientation vector, which is represented by o_x, o_y, o_z, and theta values.

        For more information, see `Arm component <https://docs.viam.com/dev/reference/apis/components/arm/#movetoposition>`_.
        """
        ...

    @abc.abstractmethod
    async def move_to_joint_positions(
        self,
        positions: JointPositions,
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ):
        """
        Move each joint on the arm to the corresponding angle specified in ``positions``.

        ::

            my_arm = Arm.from_robot(robot=machine, name="my_arm")

            # Declare a list of values with your desired rotational value for each joint on
            # the arm. This example is for a 5dof arm.
            degrees = [0.0, 45.0, 0.0, 0.0, 0.0]

            # Declare a new JointPositions with these values.
            jointPos = JointPositions(values=degrees)

            # Move each joint of the arm to the position these values specify.
            await my_arm.move_to_joint_positions(positions=jointPos)

        Args:
            positions (JointPositions): The destination ``JointPositions`` for the arm.

        For more information, see `Arm component <https://docs.viam.com/dev/reference/apis/components/arm/#movetojointpositions>`_.
        """
        ...

    @abc.abstractmethod
    async def move_through_joint_positions(
        self,
        positions: List[JointPositions],
        options: Optional[MoveOptions] = None,
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ):
        """
        Move the arm through the given joint positions in the order they are specified,
        obeying the velocity and acceleration limits in ``options``.

        ::

            my_arm = Arm.from_robot(robot=machine, name="my_arm")

            # Move through two waypoints, capping joint speed and acceleration.
            await my_arm.move_through_joint_positions(
                positions=[
                    JointPositions(values=[0, 45, 0, 0, 0, 0]),
                    JointPositions(values=[0, 0, 0, 0, 0, 0]),
                ],
                options=MoveOptions(max_vel_degs_per_sec=15.0, max_acc_degs_per_sec2=30.0),
            )

        Args:
            positions (List[JointPositions]): The waypoints to move through, in order.
            options (Optional[MoveOptions]): Optional kinematic ceilings obeyed at every
                point along the trajectory. ``None`` means no limits are requested.

        Note:
            Unlike the Go SDK, this method does not validate the requested positions
            against the arm's joint limits before sending them, because the Python SDK
            cannot yet parse a kinematics model. Implementations are responsible for
            their own limit checking.

            Every scalar field on ``MoveOptions`` (``max_vel_degs_per_sec``,
            ``max_acc_degs_per_sec2``, ``max_tcp_speed``) also has explicit presence: an
            unset field reads back as ``0.0``, indistinguishable from an explicitly-set
            zero. Implementations must check ``options.HasField("max_vel_degs_per_sec")``
            (and likewise for the other scalar fields) before applying it as a ceiling —
            reading an unset field's ``0.0`` directly would misread "no limit requested"
            as "do not move". Per the proto definition, ``max_vel_degs_per_sec`` is
            ignored whenever ``max_vel_degs_per_sec_joints`` is set, and likewise
            ``max_acc_degs_per_sec2`` is ignored whenever ``max_acc_degs_per_sec2_joints``
            is set; implementations should honor only the per-joint limit in that case,
            not both.

            An empty ``positions`` list is passed through to the implementation
            unchanged; implementations must handle it, typically as a no-op.

        For more information, see `Arm component <https://docs.viam.com/dev/reference/apis/components/arm/#movethroughjointpositions>`_.
        """
        ...

    @abc.abstractmethod
    async def get_joint_positions(
        self,
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ) -> JointPositions:
        """
        Get the JointPositions representing the current position of the arm.

        ::

            my_arm = Arm.from_robot(robot=machine, name="my_arm")

            # Get the current position of each joint on the arm as JointPositions.
            pos = await my_arm.get_joint_positions()

        Returns:
            JointPositions: The current ``JointPositions`` for the arm.
            ``JointPositions`` can have one attribute, ``values``, a list of joint positions with rotational values (degrees)
            and translational values (mm).

        For more information, see `Arm component <https://docs.viam.com/dev/reference/apis/components/arm/#getjointpositions>`_.
        """
        ...

    @abc.abstractmethod
    async def stop(
        self,
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ):
        """
        Stop all motion of the arm. It is assumed that the arm stops immediately.

        ::

            my_arm = Arm.from_robot(robot=machine, name="my_arm")

            # Stop all motion of the arm. It is assumed that the arm stops immediately.
            await my_arm.stop()

        For more information, see `Arm component <https://docs.viam.com/dev/reference/apis/components/arm/#stop>`_.
        """
        ...

    @abc.abstractmethod
    async def is_moving(self) -> bool:
        """
        Get if the arm is currently moving.

        ::

            my_arm = Arm.from_robot(robot=machine, name="my_arm")

            # Stop all motion of the arm. It is assumed that the arm stops immediately.
            await my_arm.stop()

            # Print if the arm is currently moving.
            print(await my_arm.is_moving())

        Returns:
            bool: Whether the arm is moving.

        For more information, see `Arm component <https://docs.viam.com/dev/reference/apis/components/arm/#ismoving>`_.
        """
        ...

    @abc.abstractmethod
    async def get_kinematics(
        self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs
    ) -> KinematicsReturn:
        """
        Get the kinematics information associated with the arm.

        ::

            my_arm = Arm.from_robot(robot=machine, name="my_arm")

            # Get the kinematics information associated with the arm.
            kinematics = await my_arm.get_kinematics()

            # Get the format of the kinematics file.
            k_file = kinematics[0]

            # Get the byte contents of the file.
            k_bytes = kinematics[1]

        Returns:
            Tuple[KinematicsFileFormat.ValueType, bytes]: A tuple containing two values; the first [0] value represents the format of the
            file, either in URDF format (``KinematicsFileFormat.KINEMATICS_FILE_FORMAT_URDF``) or
            Viam's kinematic parameter format (spatial vector algebra) (``KinematicsFileFormat.KINEMATICS_FILE_FORMAT_SVA``),
            and the second [1] value represents the byte contents of the file.
            If available, a third [2] value provides meshes keyed by URDF filepath.
            See ``get_3d_models`` for meshes keyed by model name instead.

        For more information, see `Arm component <https://docs.viam.com/dev/reference/apis/components/arm/#getkinematics>`_.
        """
        ...

    @abc.abstractmethod
    async def get_3d_models(
        self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs
    ) -> Mapping[str, Mesh]:
        """
        Get the 3D models associated with the arm, keyed by name.

        ::

            my_arm = Arm.from_robot(robot=machine, name="my_arm")

            # Get the arm's 3D models.
            models = await my_arm.get_3d_models()

            for name, mesh in models.items():
                print(name, mesh.content_type, len(mesh.mesh))

        Returns:
            Mapping[str, Mesh]: The arm's 3D models keyed by name. Each ``Mesh`` carries a
            ``content_type`` (for example ``"ply"``) and the raw ``mesh`` bytes in that format.
            This is distinct from ``get_kinematics``'s third return value, which keys meshes
            by URDF filepath rather than by model name.

        Note:
            Implementations with no models must return an empty mapping, not ``None``.

        For more information, see `Arm component <https://docs.viam.com/dev/reference/apis/components/arm/#get3dmodels>`_.
        """
        ...

    @abc.abstractmethod
    async def set_manual_mode(
        self,
        manual_mode: bool,
        enabled_for: int = 0,
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ):
        """
        Enter or exit manual mode for an arm that supports it.

        ::

            my_arm = Arm.from_robot(robot=machine, name="my_arm")

            # Enter manual mode for at most 30 seconds.
            await my_arm.set_manual_mode(manual_mode=True, enabled_for=30)

            # Exit manual mode.
            await my_arm.set_manual_mode(manual_mode=False)

        Args:
            manual_mode (bool): Whether to enter (``True``) or exit (``False``) manual mode.
            enabled_for (int): How long to stay in manual mode, in seconds. ``0`` means no time limit.

        For more information, see `Arm component <https://docs.viam.com/dev/reference/apis/components/arm/#setmanualmode>`_.
        """
        ...

    @abc.abstractmethod
    async def get_manual_mode(
        self,
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ) -> bool:
        """
        Get whether the arm is currently in manual mode.

        ::

            my_arm = Arm.from_robot(robot=machine, name="my_arm")

            # Print whether the arm is currently in manual mode.
            print(await my_arm.get_manual_mode())

        Returns:
            bool: Whether the arm is in manual mode.

        For more information, see `Arm component <https://docs.viam.com/dev/reference/apis/components/arm/#getmanualmode>`_.
        """
        ...

    @abc.abstractmethod
    async def get_properties(
        self,
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ) -> Properties:
        """
        Get a mapping of each optional feature to whether it is supported by this arm.

        ::

            my_arm = Arm.from_robot(robot=machine, name="my_arm")

            # Get the properties of the arm.
            properties = await my_arm.get_properties()

        Returns:
            Properties: The arm's properties; whether it supports software-enabled manual mode
            and whether it supports direct cartesian commands (``move_to_position``).

        For more information, see `Arm component <https://docs.viam.com/dev/reference/apis/components/arm/#getproperties>`_.
        """
        ...
