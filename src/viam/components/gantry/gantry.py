import abc
from typing import Any, Dict, Final, List, Optional

from viam.resource.types import RESOURCE_NAMESPACE_RDK, RESOURCE_TYPE_COMPONENT, Subtype

from ..component_base import ComponentBase


class Gantry(ComponentBase):
    """
    Gantry represents a physical Gantry and can be used for controlling gantries of N axes.

    This acts as an abstract base class for any drivers representing specific
    gantry implementations. This cannot be used on its own. If the ``__init__()`` function is
    overridden, it must call the ``super().__init__()`` function.
    """

    SUBTYPE: Final = Subtype(  # pyright: ignore [reportIncompatibleVariableOverride]
        RESOURCE_NAMESPACE_RDK, RESOURCE_TYPE_COMPONENT, "gantry"
    )

    @abc.abstractmethod
    async def get_position(self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs) -> List[float]:
        """
        Get the position in millimeters.

        Returns:
            List[float]: The position of the axes.
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
        Move the gantry to a new position at the requested speeds.

        Args:
            positions (List[float]): List of positions for the axes to move to,
                in millimeters.
        """
        ...

    @abc.abstractmethod
    async def home(self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs) -> bool:
        """
        Home the gantry to find it's starting and ending positions

        Returns:
            bool : whether the gantry has run the homing sequence successfully
        """

    @abc.abstractmethod
    async def get_lengths(self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs) -> List[float]:
        """
        Get the lengths of the axes of the gantry in millimeters.

        Returns:
            List[float]: The lengths of the axes.
        """
        ...

    @abc.abstractmethod
    async def stop(self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs):
        """
        Stop all motion of the gantry. It is assumed that the gantry stops immediately.
        """
        ...

    @abc.abstractmethod
    async def is_moving(self) -> bool:
        """
        Get if the gantry is currently moving.

        Returns:
            bool: Whether the gantry is moving.
        """
        ...
