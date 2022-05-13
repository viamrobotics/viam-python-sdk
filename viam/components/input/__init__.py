from viam.registry import ComponentRegistration, Registry

from .client import ControllerClient
from .input import Control, ControlFunction, Controller, Event, EventType
from .service import InputControllerService

__all__ = [
    'Controller',
    'Control',
    'ControlFunction',
    'Event',
    'EventType',
    'ControllerClient',
]

Registry.register(
    ComponentRegistration(
        Controller,
        'input_controller',
        InputControllerService,
        lambda name, channel: ControllerClient(name, channel),
    )
)
