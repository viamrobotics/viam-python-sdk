import abc
from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import Callable, Dict, List, Optional

from google.protobuf.timestamp_pb2 import Timestamp
from typing_extensions import Self
from viam.components.component_base import ComponentBase
from viam.errors import NotSupportedError
from viam.proto.component.inputcontroller import Event as PBEvent


class EventType(str, Enum):
    """
    Represents the type of input event.
    """

    ALL_EVENTS = "AllEvents"
    """
    Callbacks registered for this event will be called in ADDITION to other registered event callbacks.
    """

    CONNECT = "Connect"
    """
    Sent at controller initialization, and on reconnects.
    """

    DISCONNECT = "Disconnect"
    """
    If unplugged, or wireless/network times out.
    """

    BUTTON_PRESS = "ButtonPress"
    """
    Typical key press.
    """

    BUTTON_RELEASE = "ButtonRelease"
    """
    Key release.
    """

    BUTTON_HOLD = "ButtonHold"
    """
    Key is held down. This wil likely be a repeated event.
    """

    BUTTON_CHANGE = "ButtonChange"
    """
    Both up and down for convenience during registration, not typically emitted.
    """

    POSITION_CHANGE_ABSOLUTE = "PositionChangeAbs"
    """
    Absolute position is reported via Value, a la joysticks.
    """

    POSITION_CHANGE_RELATIVE = "PositionChangeRel"
    """
    Relative position is reported via Value, a la mice, or simulating axes with up/down buttons.
    """


class Control(str, Enum):
    """
    Control identifies the input (specific Axis or Button) of a controller.
    """

    # Axes
    ABSOLUTE_X = "AbsoluteX"
    ABSOLUTE_Y = "AbsoluteY"
    ABSOLUTE_Z = "AbsoluteZ"
    ABSOLUTE_RX = "AbsoluteRX"
    ABSOLUTE_RY = "AbsoluteRY"
    ABSOLUTE_RZ = "AbsoluteRZ"
    ABSOLUTE_HAT0_X = "AbsoluteHat0X"
    ABSOLUTE_HAT0_Y = "AbsoluteHat0Y"

    # Buttons
    BUTTON_SOUTH = "ButtonSouth"
    BUTTON_EAST = "ButtonEast"
    BUTTON_WEST = "ButtonWest"
    BUTTON_NORTH = "ButtonNorth"
    BUTTON_LT = "ButtonLT"
    BUTTON_RT = "ButtonRT"
    BUTTON_LT2 = "ButtonLT2"
    BUTTON_RT2 = "ButtonRT2"
    BUTTON_L_THUMB = "ButtonLThumb"
    BUTTON_R_THUMB = "ButtonRThumb"
    BUTTON_SELECT = "ButtonSelect"
    BUTTON_START = "ButtonStart"
    BUTTON_MENU = "ButtonMenu"
    BUTTON_RECORD = "ButtonRecord"
    BUTTON_E_STOP = "ButtonEStop"


@dataclass
class Event:
    time: float
    """seconds since epoch"""

    event: EventType

    control: Control

    value: float
    """0 or 1 for buttons, -1.0 to +1.0 for axes"""

    @property
    def proto(self):
        dt = datetime.fromtimestamp(self.time)
        timestamp = Timestamp()
        timestamp.FromDatetime(dt)
        return PBEvent(time=timestamp, event=self.event.value, control=self.control.value, value=self.value)

    @classmethod
    def from_proto(cls, proto: PBEvent) -> Self:
        dt = proto.time.ToDatetime()
        return cls(dt.timestamp(), EventType(proto.event), Control(proto.control), proto.value)


ControlFunction = Callable[[Event], None]


class Controller(ComponentBase):
    """
    Controller is a logical "container" more than an actual device
    Could be a single gamepad, or a collection of digitalInterrupts
    and analogReaders, a keyboard, etc.
    """

    @abc.abstractmethod
    async def get_controls(self, **kwargs) -> List[Control]:
        """
        Returns a list of Controls provided by the Controller

        Returns:
            List[Control]: List of controls provided by the Controller
        """
        ...

    @abc.abstractmethod
    async def get_events(self, **kwargs) -> Dict[Control, Event]:
        """
        Returns the most recent Event for each input
        (which should be the current state)

        Returns:
            Dict[Control, Event]: The most recent event for each input
        """
        ...

    @abc.abstractmethod
    def register_control_callback(self, control: Control, triggers: List[EventType], function: Optional[ControlFunction], **kwargs):
        """
        Register a function that will fire on given EventTypes for a given
        Control

        Args:
            control (Control): The control to register the function for
            triggers (List[EventType]): The events that will
                trigger the function
            function (ControlFunction): The function to run on
                specific triggers
        """
        ...

    async def trigger_event(self, event: Event, **kwargs):
        """Directly send an Event (such as a button press) from external code

        Args:
            event (Event): The event to trigger
        """
        raise NotSupportedError(f"Input controller named {self.name} does not support triggering events")
