import abc
from typing import Final, List, Optional

from viam.resource.types import RESOURCE_NAMESPACE_RDK, RESOURCE_TYPE_SERVICE, Subtype

from ..service_base import ServiceBase
from . import GeoObstacle, GeoPoint, Mode, Waypoint


class Navigation(ServiceBase):
    """
    Navigation represents a Navigation service.

    This acts as an abstract base class for any drivers representing specific
    arm implementations. This cannot be used on its own. If the ``__init__()`` function is
    overridden, it must call the ``super().__init__()`` function.
    """

    SUBTYPE: Final = Subtype(RESOURCE_NAMESPACE_RDK, RESOURCE_TYPE_SERVICE, "navigation")

    @abc.abstractmethod
    async def get_location(self, *, timeout: Optional[float]) -> GeoPoint:
        ...

    @abc.abstractmethod
    async def get_obstacles(self, *, timeout: Optional[float]) -> List[GeoObstacle]:
        ...

    @abc.abstractmethod
    async def get_waypoints(self, *, timeout: Optional[float]) -> List[Waypoint]:
        ...

    @abc.abstractmethod
    async def add_waypoint(self, point: GeoPoint, *, timeout: Optional[float]):
        ...

    @abc.abstractmethod
    async def remove_waypoint(self, id: str, *, timeout: Optional[float]):
        ...

    @abc.abstractmethod
    async def get_mode(self, *, timeout: Optional[float]) -> Mode.ValueType:
        ...

    @abc.abstractmethod
    async def set_mode(self, mode: Mode.ValueType, *, timeout: Optional[float]):
        ...
