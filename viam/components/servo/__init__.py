from viam.proto.api.component.servo import Status as ServoStatus
from viam.proto.api.service.status import Status
from viam.registry import ComponentRegistration, Registry
from viam.utils import message_to_struct

from .client import ServoClient
from .servo import Servo

from.service import ServoService

__all__ = [
    'Servo',
    'ServoClient',
]


async def create_status(component: Servo) -> Status:
    s = ServoStatus(
        position_deg=await component.get_position()
    )
    return Status(
        name=Servo.get_resource_name(component.name),
        status=message_to_struct(s)
    )

Registry.register(
    ComponentRegistration(
        Servo,
        'servo',
        ServoService,
        lambda name, channel: ServoClient(name, channel),
        create_status
    )
)
