from viam.proto.component.inputcontroller import Status as InputStatus
from viam.proto.robot import Status
from viam.registry import ComponentRegistration, Registry
from viam.utils import message_to_struct

from .client import ControllerClient
from .input import Control, ControlFunction, Controller, Event, EventType
from .service import InputControllerService

__all__ = [
    "Controller",
    "Control",
    "ControlFunction",
    "Event",
    "EventType",
]


async def create_status(component: Controller) -> Status:
    return Status(
        name=Controller.get_resource_name(component.name),
        status=message_to_struct(InputStatus(events=[event.proto for event in (await component.get_events()).values()])),
    )


Registry.register(
    ComponentRegistration(
        Controller, "input_controller", InputControllerService, lambda name, channel: ControllerClient(name, channel), create_status
    )
)
