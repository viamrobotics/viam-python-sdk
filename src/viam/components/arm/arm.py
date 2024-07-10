import abc
from typing import Any, Dict, Final, Optional, Tuple

from viam.resource.types import RESOURCE_NAMESPACE_RDK, RESOURCE_TYPE_COMPONENT, Subtype

from ..component_base import ComponentBase
from . import JointPositions, KinematicsFileFormat, Pose


class Arm(ComponentBase):
    """
    Arm represents a physical robot arm that exists in three-dimensional space.

    This acts as an abstract base class for any drivers representing specific
    arm implementations. This cannot be used on its own. If the ``__init__()`` function is
    overridden, it must call the ``super().__init__()`` function.

    ::

        from viam.components.arm import Arm
        # To use move_to_position:
        from viam.proto.common import Pose
        # To use move_to_joint_positions:
        from viam.proto.component.arm import JointPositions

    For more information, see `Arm component <https://docs.viam.com/components/arm/>`_.
    """

    SUBTYPE: Final = Subtype(RESOURCE_NAMESPACE_RDK, RESOURCE_TYPE_COMPONENT, "arm")  # pyright: ignore [reportIncompatibleVariableOverride]

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

            my_arm = Arm.from_robot(robot=robot, name="my_arm")

            # Get the end position of the arm as a Pose.
            pos = await my_arm.get_end_position()

        Returns:
            Pose: A representation of the arm's current position as a 6 DOF (six degrees of freedom) pose.
            The ``Pose`` is composed of values for location and orientation with respect to the origin.
            Location is expressed as distance, which is represented by x, y, and z coordinate values.
            Orientation is expressed as an orientation vector, which is represented by o_x, o_y, o_z, and theta values.

        For more information, see `Arm component <https://docs.viam.com/components/arm/>`_.
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

            my_arm = Arm.from_robot(robot=robot, name="my_arm")

            # Create a Pose for the arm.
            examplePose = Pose(x=5, y=5, z=5, o_x=5, o_y=5, o_z=5, theta=20)

            # Move your arm to the Pose.
            await my_arm.move_to_position(pose=examplePose)

        Args:
            pose (Pose): The destination ``Pose`` for the arm. The ``Pose`` is composed of values for location and orientation
                with respect to the origin.
                Location is expressed as distance, which is represented by x, y, and z coordinate values.
                Orientation is expressed as an orientation vector, which is represented by o_x, o_y, o_z, and theta values.

        For more information, see `Arm component <https://docs.viam.com/components/arm/>`_.
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

            my_arm = Arm.from_robot(robot=robot, name="my_arm")

            # Declare a list of values with your desired rotational value for each joint on
            # the arm.
            degrees = [0.0, 45.0, 0.0, 0.0, 0.0]

            # Declare a new JointPositions with these values.
            jointPos = arm.move_to_joint_positions(
                JointPositions(values=[0.0, 45.0, 0.0, 0.0, 0.0]))

            # Move each joint of the arm to the position these values specify.
            await my_arm.move_to_joint_positions(positions=jointPos)

        Args:
            positions (JointPositions): The destination ``JointPositions`` for the arm.

        For more information, see `Arm component <https://docs.viam.com/components/arm/>`_.
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

            my_arm = Arm.from_robot(robot=robot, name="my_arm")

            # Get the current position of each joint on the arm as JointPositions.
            pos = await my_arm.get_joint_positions()

        Returns:
            JointPositions: The current ``JointPositions`` for the arm.
            ``JointPositions`` can have one attribute, ``values``, a list of joint positions with rotational values (degrees)
            and translational values (mm).

        For more information, see `Arm component <https://docs.viam.com/components/arm/>`_.
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

            my_arm = Arm.from_robot(robot=robot, name="my_arm")

            # Stop all motion of the arm. It is assumed that the arm stops immediately.
            await my_arm.stop()

        For more information, see `Arm component <https://docs.viam.com/components/arm/>`_.
        """
        ...

    @abc.abstractmethod
    async def is_moving(self) -> bool:
        """
        Get if the arm is currently moving.

        ::

            my_arm = Arm.from_robot(robot=robot, name="my_arm")

            # Stop all motion of the arm. It is assumed that the arm stops immediately.
            await my_arm.stop()

            # Print if the arm is currently moving.
            print(my_arm.is_moving())

        Returns:
            bool: Whether the arm is moving.

        For more information, see `Arm component <https://docs.viam.com/components/arm/>`_.
        """
        ...

    @abc.abstractmethod
    async def get_kinematics(
        self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None
    ) -> Tuple[KinematicsFileFormat.ValueType, bytes]:
        """
        Get the kinematics information associated with the arm.

        ::

            my_arm = Arm.from_robot(robot=robot, name="my_arm")

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

        For more information, see `Arm component <https://docs.viam.com/components/arm/>`_.
        """
        ...
