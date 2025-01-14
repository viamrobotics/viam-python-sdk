from viam.resource.registry import Registry, ResourceRegistration

from .client import GantryClient
from .gantry import Gantry
from .service import GantryRPCService

__all__ = [
    "Gantry",
]

Registry.register_api(ResourceRegistration(Gantry, GantryRPCService, lambda name, channel: GantryClient(name, channel)))
