import abc
from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import Any, Callable, Dict, Final, List, Optional

from google.protobuf.timestamp_pb2 import Timestamp
from typing_extensions import Self

from viam.components.component_base import ComponentBase
from viam.errors import NotSupportedError
from viam.proto.component.inputcontroller import Event as PBEvent
from viam.resource.types import RESOURCE_NAMESPACE_RDK, RESOURCE_TYPE_COMPONENT, Subtype


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

    # Pedals
    ABSOLUTE_PEDAL_ACCELERATOR = "AbsolutePedalAccelerator"
    ABSOLUTE_PEDAL_BRAKE = "AbsolutePedalBrake"
    ABSOLUTE_PEDAL_CLUTCH = "AbsolutePedalClutch"


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

    ::

        from viam.components.input import Control, Controller, EventType

    For more information, see `Input Controller component <https://docs.viam.com/components/input-controller/>`_.
    """

    SUBTYPE: Final = Subtype(  # pyright: ignore [reportIncompatibleVariableOverride]
        RESOURCE_NAMESPACE_RDK, RESOURCE_TYPE_COMPONENT, "input_controller"
    )

    @abc.abstractmethod
    async def get_controls(self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs) -> List[Control]:
        """
        Returns a list of Controls provided by the Controller

        ::

            # Get the controller from the machine.
            my_controller = Controller.from_robot(
                robot=myRobotWithController, name="my_controller")

            # Get the list of Controls provided by the controller.
            controls = await my_controller.get_controls()

            # Print the list of Controls provided by the controller.
            print(f"Controls: {controls}")

        Returns:
            List[Control]: List of controls provided by the Controller

        For more information, see `Input Controller component <https://docs.viam.com/components/input-controller/>`_.
        """
        ...

    @abc.abstractmethod
    async def get_events(
        self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs
    ) -> Dict[Control, Event]:
        """
        Returns the most recent Event for each input
        (which should be the current state)

        ::

            # Get the controller from the machine.
            my_controller = Controller.from_robot(
                robot=myRobotWithController, name="my_controller")

            # Get the most recent Event for each Control.
            recent_events = await my_controller.get_events()

            # Print out the most recent Event for each Control.
            print(f"Recent Events: {recent_events}")

        Returns:
            Dict[Control, Event]: The most recent event for each input

        For more information, see `Input Controller component <https://docs.viam.com/components/input-controller/>`_.
        """
        ...

    @abc.abstractmethod
    def register_control_callback(
        self,
        control: Control,
        triggers: List[EventType],
        function: Optional[ControlFunction],
        *,
        extra: Optional[Dict[str, Any]] = None,
        **kwargs,
    ):
        """
        Register a function that will fire on given EventTypes for a given
        Control

        ::

            # Define a function to handle pressing the Start Menu Button "BUTTON_START" on
            # your controller, printing out the start time.
            def print_start_time(event):
                print(f"Start Menu Button was pressed at this time: {event.time}")


            # Define a function that handles the controller.
            async def handle_controller(controller):
                # Get the list of Controls on the controller.
                controls = await controller.get_controls()

                # If the "BUTTON_START" Control is found, register the function
                # print_start_time to fire when "BUTTON_START" has the event "ButtonPress"
                # occur.
                if Control.BUTTON_START in controls:
                    controller.register_control_callback(
                        Control.BUTTON_START, [EventType.BUTTON_PRESS], print_start_time)
                else:
                    print("Oops! Couldn't find the start button control! Is your "
                        "controller connected?")
                    exit()

                while True:
                    await asyncio.sleep(1.0)


            async def main():
                # ... < INSERT CONNECTION CODE FROM MACHINE'S CODE SAMPLE TAB >

                # Get your controller from the machine.
                my_controller = Controller.from_robot(
                    robot=myRobotWithController, name="my_controller")

                # Run the handleController function.
                await handleController(my_controller)

                # ... < INSERT ANY OTHER CODE FOR MAIN FUNCTION >

        Args:
            control (Control): The control to register the function for
            triggers (List[EventType]): The events that will
                trigger the function
            function (ControlFunction): The function to run on
                specific triggers

        For more information, see `Input Controller component <https://docs.viam.com/components/input-controller/>`_.
        """
        ...

    async def trigger_event(
        self,
        event: Event,
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ) -> None:  # Explicitly return None for typechecking, as this is technically a NoReturn default implementation
        """Directly send an Event (such as a button press) from external code

        ::

            # Define a "Button is Pressed" event for the control BUTTON_START.
            button_is_pressed_event = Event(
                time(), EventType.BUTTON_PRESS, Control.BUTTON_START, 1.0)

            # Trigger the event on your controller. Set this trigger to timeout if it has
            # not completed in 7 seconds.
            await myController.trigger_event(event=my_event, timeout=7.0)

        Args:
            event (Event): The event to trigger

        For more information, see `Input Controller component <https://docs.viam.com/components/input-controller/>`_.
        """
        raise NotSupportedError(f"Input controller named {self.name} does not support triggering events")
