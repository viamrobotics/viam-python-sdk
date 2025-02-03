from viam.proto.common import Vector3
from viam.resource.registry import Registry, ResourceRegistration

from .base import Base
from .client import BaseClient
from .service import BaseRPCService

__all__ = [
    "Base",
    "Vector3",
]

Registry.register_api(ResourceRegistration(Base, BaseRPCService, lambda name, channel: BaseClient(name, channel)))
