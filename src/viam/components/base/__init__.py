from viam.resource.registry import ResourceRegistration, Registry
from viam.proto.common import ActuatorStatus
from viam.proto.robot import Status
from viam.utils import message_to_struct

from .base import Base, Vector3
from .client import BaseClient
from .service import BaseService

__all__ = ["Base", "Vector3"]


async def create_status(component: Base) -> Status:
    s = ActuatorStatus(is_moving=await component.is_moving())
    return Status(name=Base.get_resource_name(component.name), status=message_to_struct(s))


Registry.register_subtype(ResourceRegistration(Base, BaseService, lambda name, channel: BaseClient(name, channel), create_status))
