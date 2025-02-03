from viam.resource.registry import Registry, ResourceRegistration

from .client import ControllerClient
from .input import Control, ControlFunction, Controller, Event, EventType
from .service import InputControllerRPCService

__all__ = [
    "Controller",
    "Control",
    "ControlFunction",
    "Event",
    "EventType",
]

Registry.register_api(ResourceRegistration(Controller, InputControllerRPCService, lambda name, channel: ControllerClient(name, channel)))
