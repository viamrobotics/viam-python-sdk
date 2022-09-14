import abc
from typing import Any, Dict, Optional

from viam.errors import NotSupportedError
from viam.proto.common import Pose, WorldState
from viam.proto.component.arm import JointPositions

from ..component_base import ComponentBase


class Arm(ComponentBase):
    """
    Arm represents a physical robot arm that exists in three-dimensional space.

    This acts as an abstract base class for any drivers representing specific
    arm implementations. This cannot be used on its own. If the `__init__()` function is
    overridden, it must call the `super().__init__()` function.
    """

    @abc.abstractmethod
    async def get_end_position(self, extra: Optional[Dict[str, Any]] = None, **kwargs) -> Pose:
        """
        Get the current position of the end of the arm expressed as a Pose.

        Returns: The location and orientation of the arm described as a Pose.
        """
        ...

    @abc.abstractmethod
    async def move_to_position(
        self, pose: Pose, world_state: Optional[WorldState] = None, extra: Optional[Dict[str, Any]] = None, **kwargs
    ):
        """
        Move the end of the arm to the Pose specified in `pose`.
        When obstacles are specified in `world_state`, the motion plan of the arm will avoid them.

        Args:

            pose (Pose): The destination Pose for the arm.

            world_state (WorldState): The obstacles for the arm to avoid on its way to `pose`.
        """
        ...

    @abc.abstractmethod
    async def move_to_joint_positions(self, positions: JointPositions, extra: Optional[Dict[str, Any]] = None, **kwargs):
        """
        Move each joint on the arm to the corresponding angle specified in `positions`.

        Args:

            positions (JointPositions): The destination `JointPositions` for the arm.
        """
        ...

    @abc.abstractmethod
    async def get_joint_positions(self, extra: Optional[Dict[str, Any]] = None, **kwargs) -> JointPositions:
        """
        Get the JointPositions representing the current position of the arm.

        Returns:
            JointPositions: The current JointPositions for the arm.
        """
        ...

    @abc.abstractmethod
    async def stop(self, extra: Optional[Dict[str, Any]] = None, **kwargs):
        """
        Stop all motion of the arm. It is assumed that the arm stops immediately.
        """
        ...

    async def is_moving(self) -> bool:
        """
        Get if the arm is currently moving.

        Returns:
            bool: Whether the arm is moving.
        """
        raise NotSupportedError(f"Arm named {self.name} does not support returning whether it is moving")
