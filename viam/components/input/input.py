import abc
from dataclasses import dataclass
from enum import Enum
from typing import Dict, List, Callable

from viam.components.component_base import ComponentBase


class EventType(Enum):
    """
    Represents the type of input event.
    """

    ALL_EVENTS = 'AllEvents'
    """
    Callbacks registered for this event will be called
    in ADDITION to other registered event callbacks.
    """

    CONNECT = 'Connect'
    """
    Sent at controller initialization, and on reconnects.
    """

    DISCONNECT = 'Disconnect'
    """
    If unplugged, or wireless/network times out.
    """

    BUTTON_PRESS = 'ButtonPress'
    """
    Typical key press.
    """

    BUTTON_RELEASE = 'ButtonRelease'
    """
    Key release.
    """

    BUTTON_CHANGE = 'ButtonChange'
    """
    Both up and down for convenience during registration,
    not typically emitted.
    """

    POSITION_CHANGE_ABSOLUTE = 'PositionChangeAbs'
    """
    Absolute position is reported via Value, a la joysticks.
    """

    POSITION_CHANGE_RELATIVE = 'PositionChangeRel'
    """
    Relative position is reported via Value, a la mice, or
    simulating axes with up/down buttons.
    """


class Control(Enum):
    """
    Control identifies the input (specific Axis or Button) of a controller.
    """
    # Axes
    ABSOLUTE_X = 'AbsoluteX'
    ABSOLUTE_Y = 'AbsoluteY'
    ABSOLUTE_Z = 'AbsoluteZ'
    ABSOLUTE_RX = 'AbsoluteRX'
    ABSOLUTE_RY = 'AbsoluteRY'
    ABSOLUTE_RZ = 'AbsoluteRZ'
    ABSOLUTE_HAT0_X = 'AbsoluteHat0X'
    ABSOLUTE_HAT0_Y = 'AbsoluteHat0Y'

    # Buttons
    BUTTON_SOUTH = 'ButtonSouth'
    BUTTON_EAST = 'ButtonEast'
    BUTTON_WEST = 'ButtonWest'
    BUTTON_NORTH = 'ButtonNorth'
    BUTTON_LT = 'ButtonLT'
    BUTTON_RT = 'ButtonRT'
    BUTTON_L_THUMB = 'ButtonLThumb'
    BUTTON_R_THUMB = 'ButtonRThumb'
    BUTTON_SELECT = 'ButtonSelect'
    BUTTON_START = 'ButtonStart'
    BUTTON_MENU = 'ButtonMenu'
    BUTTON_RECORD = 'ButtonRecord'
    BUTTON_E_STOP = 'ButtonEStop'


@dataclass
class Event:
    time: float  # seconds since epoch
    event: EventType
    control: Control
    value: float  # 0 or 1 for buttons, -1.0 to +1.0 for axes


ControlFunction = Callable[[Event], None]


class Controller(ComponentBase):
    """
    Controller is a logical "container" more than an actual device
    Could be a single gamepad, or a collection of digitalInterrupts
    and analogReaders, a keyboard, etc.
    """

    @abc.abstractmethod
    async def get_controls(self) -> List[Control]:
        """
        Returns a list of Controls provided by the Controller

        Returns:
            List[Control]: List of controls provided by the Controller
        """
        ...

    @abc.abstractmethod
    async def get_events(self) -> Dict[Control, Event]:
        """
        Returns the most recent Event for each input
        (which should be the current state)

        Returns:
            Dict[Control, Event]: The most recent event for each input
        """
        ...

    @abc.abstractmethod
    async def register_control_callback(
        self,
        control: Control,
        triggers: List[EventType],
        function: ControlFunction
    ):
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
