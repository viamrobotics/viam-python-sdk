from viam.resource.registry import Registry, ResourceRegistration
from viam.services.discovery.service import DiscoveryRPCService

from .client import DiscoveryClient
from .discovery import Discovery

__all__ = [
    "DiscoveryClient",
    "Discovery",
]

Registry.register_api(ResourceRegistration(Discovery, DiscoveryRPCService, lambda name, channel: DiscoveryClient(name, channel)))
