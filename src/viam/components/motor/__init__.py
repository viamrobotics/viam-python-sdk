import asyncio

from viam.proto.component.motor import Status as MotorStatus
from viam.proto.robot import Status
from viam.resource.registry import Registry, ResourceRegistration
from viam.utils import message_to_struct

from .client import MotorClient
from .motor import Motor
from .service import MotorRPCService

__all__ = [
    "Motor",
]


async def create_status(component: Motor) -> Status:
    ((is_powered, _), position, is_moving) = await asyncio.gather(
        component.is_powered(),
        component.get_position(),
        component.is_moving(),
    )
    s = MotorStatus(
        is_powered=is_powered,
        position=position,
        is_moving=is_moving,
    )
    return Status(name=Motor.get_resource_name(component.name), status=message_to_struct(s))


Registry.register_subtype(ResourceRegistration(Motor, MotorRPCService, lambda name, channel: MotorClient(name, channel), create_status))
