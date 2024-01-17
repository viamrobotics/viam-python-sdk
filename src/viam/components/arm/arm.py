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
        Get the current position of the end of the arm expressed as a Pose.

        Returns:
            Pose: The location and orientation of the arm described as a Pose.
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

        Args:
            pose (Pose): The destination Pose for the arm.
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

        Args:
            positions (JointPositions): The destination ``JointPositions`` for the arm.
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

        Returns:
            JointPositions: The current JointPositions for the arm.
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
        """
        ...

    @abc.abstractmethod
    async def is_moving(self) -> bool:
        """
        Get if the arm is currently moving.

        Returns:
            bool: Whether the arm is moving.
        """
        ...

    @abc.abstractmethod
    async def get_kinematics(
        self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None
    ) -> Tuple[KinematicsFileFormat.ValueType, bytes]:
        """
        Get the kinematics information associated with the arm.

        Returns:
            Tuple[KinematicsFileFormat.ValueType, bytes]:
                - KinematicsFileFormat.ValueType:
                  The format of the file, either in URDF format or Viam's kinematic parameter format (spatial vector algebra).

                - bytes: The byte contents of the file.
        """
        ...
