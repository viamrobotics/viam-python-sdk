from viam.proto.common import KinematicsFileFormat
from viam.resource.registry import Registry, ResourceRegistration

from .client import GripperClient
from .gripper import Gripper
from .service import GripperRPCService

__all__ = [
    "Gripper",
    "KinematicsFileFormat",
]

Registry.register_api(ResourceRegistration(Gripper, GripperRPCService, lambda name, channel: GripperClient(name, channel)))
