import abc
from typing import List

from viam.proto.api.common import GeometriesInFrame

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
        obstacles: List[GeometriesInFrame]
    ):
        """
        Move the gantry to a new poition

        Args:
            positions (List[float]): List of positions for the axes to move to,
                in millimeters
            obstacles (List[GeometriesInFrame]): The geometries of any
                obstacles
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
