import abc
from typing import List, Optional

from viam.proto.api.common import WorldState

from ..component_base import ComponentBase


class Gantry(ComponentBase):
    """
    Abstract representation of a physical Gantry,
    used for controlling gantries of N axes.

    If you override the init function,
    you must call the super init function.
    """

    @abc.abstractmethod
    async def get_position(self) -> List[float]:
        """
        Get the position in millimeters

        Returns:
            List[float]: the position of the axes
        """
        ...

    @abc.abstractmethod
    async def move_to_position(
        self,
        positions: List[float],
        world_state: Optional[WorldState] = None
    ):
        """
        Move the gantry to a new poition

        Args:
            positions (List[float]): List of positions for the axes to move to,
                in millimeters
            world_state (Optional[WorldState]): Object describing
                obstacles and transforms
        """
        ...

    @abc.abstractmethod
    async def get_lengths(self) -> List[float]:
        """
        Get the lengths of the axes of the gantry in millimeters

        Returns:
            List[float]: The lengths of the axes
        """
        ...
