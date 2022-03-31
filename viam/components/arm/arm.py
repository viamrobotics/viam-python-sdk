import abc
from typing import Optional

from viam.proto.api.common import Pose, WorldState
from viam.proto.api.component.arm import JointPositions

from ..component_base import ComponentBase


class Arm(ComponentBase):
    """
    Arm represents a physical robot arm that exists in three-dimensional space.

    This acts as an abstract base class for any drivers representing specific 
    arm implementations. This cannot be used on its own. If the init fucntion is
    overriden, it must call the super init function.
    """

    @abc.abstractmethod
    async def get_end_position(self) -> Pose:
        """
        Get the current position of the end of the arm expressed as
        location (`x`, `y`, `z`), and orientation (`o_x`, `o_y`, `o_z`, `theta`).

        Returns:
            Position : `Pose`

        Raises:
            grpc_error: If the component is not found in the registry   
        """
        ...

    @abc.abstractmethod
    async def move_to_position(
        self,
        pose: Pose,
        world_state: Optional[WorldState] = None
    ):
        """
        Moves the end of the arm to the given absolute position espressed
        as location (`x`, `y`, `z`), and orientation (`o_x`, `o_y`, `o_z`, `theta`).
        If obstacles are specified, the motion plan of the arm will avoid them.

        Args:
            pose : `Pose`
            obstacles : `World_State`, can be empty.

        Raises:
            grpc_error: If the component is not found in the registry
        """
        ...

    @abc.abstractmethod
    async def move_to_joint_positions(self, positions: JointPositions):
        """
        Moves every joint on the arm to specified angles which are 
        expressed in degrees.

        Args:
            positions : `JointPositions`

        Raises:
            grpc_error: If the component is not found in the registry
        """
        ...

    @abc.abstractmethod
    async def get_joint_positions(self) -> JointPositions:
        """
        Returns a list of the joint angles (in degrees) of every joint on the arm.

        Returns:
            positions : `JointPositions`

        Raises:
            grpc_error: If the component is not found in the registry
        """
        ...
