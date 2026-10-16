from viam.proto.service.navigation import (
    GetCostmapResponse,
    GoalState,
    GoalStatus,
    Location,
    MapType,
    NavError,
    NavErrorCode,
    NavMode,
    Plan,
    Position,
    Progress,
    Properties,
    Route,
    RouteProgress,
    Status,
    Velocity,
    Waypoint,
    Zone,
)
from viam.resource.registry import Registry, ResourceRegistration

from .client import NavigationClient
from .navigation import Navigation
from .service import NavigationRPCService

__all__ = [
    "GetCostmapResponse",
    "GoalState",
    "GoalStatus",
    "Location",
    "MapType",
    "NavError",
    "NavErrorCode",
    "NavMode",
    "Navigation",
    "NavigationClient",
    "Plan",
    "Position",
    "Progress",
    "Properties",
    "Route",
    "RouteProgress",
    "Status",
    "Velocity",
    "Waypoint",
    "Zone",
]

Registry.register_api(ResourceRegistration(Navigation, NavigationRPCService, lambda name, channel: NavigationClient(name, channel)))
