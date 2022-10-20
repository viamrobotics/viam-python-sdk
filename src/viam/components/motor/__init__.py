import asyncio
from viam.proto.component.motor import Status as MotorStatus
from viam.proto.robot import Status
from viam.registry import ComponentRegistration, Registry
from viam.utils import message_to_struct

from .client import MotorClient
from .motor import Motor
from .service import MotorService

__all__ = [
    "Motor",
]


async def create_status(component: Motor) -> Status:
    ((is_powered, _), position, properties, is_moving) = await asyncio.gather(
        component.is_powered(),
        component.get_position(),
        component.get_properties(),
        component.is_moving(),
    )
    s = MotorStatus(
        is_powered=is_powered,
        position=position,
        position_reporting=properties.position_reporting,
        is_moving=is_moving,
    )
    return Status(name=Motor.get_resource_name(component.name), status=message_to_struct(s))


Registry.register(ComponentRegistration(Motor, "motor", MotorService, lambda name, channel: MotorClient(name, channel), create_status))
