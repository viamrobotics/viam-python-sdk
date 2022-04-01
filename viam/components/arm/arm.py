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

        Returns:

        Pose: location (comprised of `x`, `y`, and `z` representing distance in millimeters
              from the arm's base)
              and orientation (comprised of `o_x`, `o_y`, and `o_z`
              representing a vector of the point on the cartesian unit sphere at 
              which the end effector is pointing from the origin and
              `theta` representing the angle around that unit vector)
        """
        ...

    @abc.abstractmethod
    async def move_to_position(
        self,
        pose: Pose,
        world_state: Optional[WorldState] = None
    ):
        """
        Move the end of the arm to the specified `pose`.
        If obstacles are specified in `world_state`, the motion plan of the arm will avoid them.

        Args:

            pose: location (comprised of `x`, `y`, and `z` representing distance in millimeters
                  from the arm's base)
                  and orientation (comprised of `o_x`, `o_y`, and `o_z`
                  representing a vector of the point on the cartesian unit sphere at 
                  which the end effector is pointing from the origin and
                  `theta` representing the angle around that unit vector)

            world_state: list of `GeometriesInFrame`. not sure how best to describe this portion
        """
        ...

    @abc.abstractmethod
    async def move_to_joint_positions(self, positions: JointPositions):
        """
        Move each joint on the arm to the corresponding angle specified in `positions`.

        Args:

            positions: a list of floats representing joint angles in degrees, in order from
                            base to end effector.
        """
        ...

    @abc.abstractmethod
    async def get_joint_positions(self) -> JointPositions:
        """
        Get the list of the current joint angle (in degrees) for each joint on the arm.

        Returns:

            JointPositions: a list of floats representing joint angles in degrees, in order from
                            base to end effector.
        """
        ...
