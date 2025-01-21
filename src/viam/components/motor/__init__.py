from viam.resource.registry import Registry, ResourceRegistration

from .client import MotorClient
from .motor import Motor
from .service import MotorRPCService

__all__ = [
    "Motor",
]

Registry.register_api(ResourceRegistration(Motor, MotorRPCService, lambda name, channel: MotorClient(name, channel)))
