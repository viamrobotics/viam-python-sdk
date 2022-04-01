import abc
from typing import Optional

from viam.proto.api.common import Pose, WorldState
from viam.proto.api.component.arm import JointPositions

from ..component_base import ComponentBase


class Arm(ComponentBase):
    """
    Arm represents a physical robot arm that exists in three-dimensional space.

    This acts as an abstract base class for any drivers representing specific 
    arm implementations. This cannot be used on its own. If the `__init__()` function is
    overriden, it must call the `super().__init__()` function.
    """

    @abc.abstractmethod
    async def get_end_position(self) -> Pose:
        """
        Get the current position of the end of the arm expressed as a `Pose`.

        Returns: the location and orientation of the arm described as a `Pose`.
        """
        ...

    @abc.abstractmethod
    async def move_to_position(
        self,
        pose: Pose,
        world_state: Optional[WorldState] = None
    ):
        """
        Move the end of the arm to the `Pose` specified in `pose`.
        If obstacles are specified in `world_state`, the motion plan of the arm will avoid them.

        Args:

            pose (`Pose`): the destination `Pose` for the arm.

            world_state (`WorldState`): the obstacles for the arm to avoid on its way to `pose`.
        """
        ...

    @abc.abstractmethod
    async def move_to_joint_positions(self, positions: JointPositions):
        """
        Move each joint on the arm to the corresponding angle specified in `positions`.

        Args:

            positions (`JointPositions`): the destination `JointPositions` for the arm.
        """
        ...

    @abc.abstractmethod
    async def get_joint_positions(self) -> JointPositions:
        """
        Get the list of the current joint angle (in degrees) for each joint on the arm.

        Returns:

            `JointPositions`: the current `JointPositions` for the arm.
        """
        ...
