from viam.resource.registry import Registry, ResourceRegistration

from .client import ServoClient
from .service import ServoRPCService
from .servo import Servo

__all__ = [
    "Servo",
]

Registry.register_api(ResourceRegistration(Servo, ServoRPCService, lambda name, channel: ServoClient(name, channel)))
