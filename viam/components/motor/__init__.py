from viam.proto.api.component.motor import Status as MotorStatus
from viam.proto.api.service.status import Status
from viam.registry import ComponentRegistration, Registry
from viam.utils import message_to_struct

from .client import MotorClient
from .motor import Motor
from .service import MotorService

__all__ = [
    'Motor',
    'MotorClient',
]


async def create_status(component: Motor) -> Status:
    s = MotorStatus(
        is_on=await component.is_powered(),
        position=await component.get_position(),
        position_reporting=(await component.get_features()).position_reporting
    )
    return Status(
        name=Motor.get_resource_name(component.name),
        status=message_to_struct(s)
    )

Registry.register(
    ComponentRegistration(
        Motor,
        'motor',
        MotorService,
        lambda name, channel: MotorClient(name, channel),
        create_status
    )
)
