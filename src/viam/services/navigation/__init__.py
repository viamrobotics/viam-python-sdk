from viam.proto.common import Pose
from viam.resource.registry import Registry, ResourceRegistration

from .client import NavigationClient
from .navigation import Navigation
from .service import NavigationRPCService

__all__ = [
    "Pose",
    "NavigationClient",
    "Navigation",
]

Registry.register_subtype(ResourceRegistration(Navigation, NavigationRPCService, lambda name, channel: NavigationClient(name, channel)))
