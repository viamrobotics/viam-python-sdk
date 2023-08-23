from viam.proto.common import ActuatorStatus
from viam.proto.robot import Status
from viam.resource.registry import Registry, ResourceRegistration
from viam.utils import message_to_struct

from .client import GripperClient
from .gripper import Gripper
from .service import GripperRPCService

__all__ = [
    "Gripper",
]


async def create_status(component: Gripper) -> Status:
    s = ActuatorStatus(is_moving=await component.is_moving())
    return Status(name=Gripper.get_resource_name(component.name), status=message_to_struct(s))


Registry.register_subtype(
    ResourceRegistration(Gripper, GripperRPCService, lambda name, channel: GripperClient(name, channel), create_status)
)
