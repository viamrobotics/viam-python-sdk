from viam.components.gantry.gantry import Gantry
from viam.registry import ComponentRegistration, Registry
from viam.proto.common import ActuatorStatus
from viam.proto.robot import Status
from viam.utils import message_to_struct

from .client import GripperClient
from .gripper import Gripper
from .service import GripperService

__all__ = [
    "Gripper",
]


async def create_status(component: Gripper) -> Status:
    s = ActuatorStatus(is_moving=await component.is_moving())
    return Status(name=Gripper.get_resource_name(component.name), status=message_to_struct(s))


Registry.register(
    ComponentRegistration(Gripper, "gripper", GripperService, lambda name, channel: GripperClient(name, channel), create_status)
)
