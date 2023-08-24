from viam.proto.common import ActuatorStatus, Vector3
from viam.proto.robot import Status
from viam.resource.registry import Registry, ResourceRegistration
from viam.utils import message_to_struct

from .base import Base
from .client import BaseClient
from .service import BaseRPCService

__all__ = [
    "Base",
    "Vector3",
]


async def create_status(component: Base) -> Status:
    s = ActuatorStatus(is_moving=await component.is_moving())
    return Status(name=Base.get_resource_name(component.name), status=message_to_struct(s))


Registry.register_subtype(ResourceRegistration(Base, BaseRPCService, lambda name, channel: BaseClient(name, channel), create_status))
