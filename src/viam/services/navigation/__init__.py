from viam.proto.common import GeoObstacle, GeoPoint
from viam.proto.service.navigation import MapType, Mode, Path, Waypoint
from viam.resource.registry import Registry, ResourceRegistration

from .client import NavigationClient
from .navigation import Navigation
from .service import NavigationRPCService

__all__ = ["GeoPoint", "GeoObstacle", "NavigationClient", "Navigation", "Waypoint", "Mode", "Path", "MapType"]

Registry.register_subtype(ResourceRegistration(Navigation, NavigationRPCService, lambda name, channel: NavigationClient(name, channel)))
