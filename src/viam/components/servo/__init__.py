import asyncio

from viam.proto.component.servo import Status as ServoStatus
from viam.proto.robot import Status
from viam.resource.registry import Registry, ResourceRegistration
from viam.utils import message_to_struct

from .client import ServoClient
from .service import ServoRPCService
from .servo import Servo

__all__ = [
    "Servo",
]


async def create_status(component: Servo) -> Status:
    (position_deg, is_moving) = await asyncio.gather(component.get_position(), component.is_moving())
    s = ServoStatus(position_deg=position_deg, is_moving=is_moving)
    return Status(name=Servo.get_resource_name(component.name), status=message_to_struct(s))


Registry.register_subtype(ResourceRegistration(Servo, ServoRPCService, lambda name, channel: ServoClient(name, channel), create_status))
