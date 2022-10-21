import asyncio
from viam.proto.component.servo import Status as ServoStatus
from viam.proto.robot import Status
from viam.registry import ComponentRegistration, Registry
from viam.utils import message_to_struct

from .client import ServoClient
from .servo import Servo

from .service import ServoService

__all__ = [
    "Servo",
]


async def create_status(component: Servo) -> Status:
    (position_deg, is_moving) = await asyncio.gather(component.get_position(), component.is_moving())
    s = ServoStatus(position_deg=position_deg, is_moving=is_moving)
    return Status(name=Servo.get_resource_name(component.name), status=message_to_struct(s))


Registry.register(ComponentRegistration(Servo, "servo", ServoService, lambda name, channel: ServoClient(name, channel), create_status))
