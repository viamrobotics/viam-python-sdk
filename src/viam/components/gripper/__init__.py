from viam.resource.registry import Registry, ResourceRegistration

from .client import GripperClient
from .gripper import Gripper
from .service import GripperRPCService

__all__ = [
    "Gripper",
]

Registry.register_api(ResourceRegistration(Gripper, GripperRPCService, lambda name, channel: GripperClient(name, channel)))
