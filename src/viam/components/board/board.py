import abc
from datetime import timedelta
from typing import Any, Dict, Final, List, Optional

from viam.proto.component.board import PowerMode, StreamTicksResponse
from viam.resource.types import RESOURCE_NAMESPACE_RDK, RESOURCE_TYPE_COMPONENT, Subtype
from viam.streams import Stream

from ..component_base import ComponentBase

Tick = StreamTicksResponse
TickStream = Stream[Tick]


class Board(ComponentBase):
    """
    Board represents a physical general purpose compute board that contains various
    components such as analog readers, and digital interrupts.

    This acts as an abstract base class for any drivers representing specific
    board implementations. This cannot be used on its own. If the ``__init__()`` function is
    overridden, it must call the ``super().__init__()`` function.

    ::

        from viam.components.board import Board
    """

    SUBTYPE: Final = Subtype(  # pyright: ignore [reportIncompatibleVariableOverride]
        RESOURCE_NAMESPACE_RDK, RESOURCE_TYPE_COMPONENT, "board"
    )

    class AnalogReader:
        """
        AnalogReader represents an analog pin reader that resides on a Board.
        """

        name: str
        """The name of the analog reader"""

        def __init__(self, name: str):
            self.name = name

        @abc.abstractmethod
        async def read(self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs) -> int:
            """
            Read the current value.

            ::

                my_board = Board.from_robot(robot=robot, name="my_board")

                # Get the GPIOPin with pin number 15.
                pin = await my_board.gpio_pin_by_name(name="15")

                # Get if it is true or false that the pin is set to high.
                duty_cycle = await pin.get_pwm()

                # Get the AnalogReader "my_example_analog_reader".
                reader = await my_board.analog_reader_by_name(
                    name="my_example_analog_reader")

                # Get the value of the digital signal "my_example_analog_reader" has most
                # recently measured.
                reading = reader.read()

            Returns:
                int: The current value.
            """
            ...

    class DigitalInterrupt:
        """
        DigitalInterrupt represents a configured interrupt on the Board that
        when interrupted, calls the added callbacks. Post processors can
        be added to modify what Value it ultimately returns.
        """

        name: str
        """The name of the digital interrupt"""

        def __init__(self, name: str):
            self.name = name

        @abc.abstractmethod
        async def value(self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs) -> int:
            """
            Get the current value of the interrupt,
            which is based on the type of interrupt.

            ::

                my_board = Board.from_robot(robot=robot, name="my_board")

                # Get the DigitalInterrupt "my_example_digital_interrupt".
                interrupt = await my_board.digital_interrupt_by_name(
                    name="my_example_digital_interrupt")

                # Get the amount of times this DigitalInterrupt has been interrupted with a
                # tick.
                count = await interrupt.value()

            Returns:
                int: The current value.
            """
            ...

    class GPIOPin:
        """
        Abstract representation of an individual GPIO pin on a board
        """

        name: str
        """The name of the GPIO pin"""

        def __init__(self, name: str):
            self.name = name

        @abc.abstractmethod
        async def set(self, high: bool, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs):
            """
            Set the pin to either low or high.

            ::

                my_board = Board.from_robot(robot=robot, name="my_board")

                # Get the GPIOPin with pin number 15.
                pin = await my_board.gpio_pin_by_name(name="15")

                # Set the pin to high.
                await pin.set(high="true")

            Args:
                high (bool): When true, sets the pin to high. When false, sets the pin to low.
            """
            ...

        @abc.abstractmethod
        async def get(self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs) -> bool:
            """
            Get the high/low state of the pin.

            ::

                my_board = Board.from_robot(robot=robot, name="my_board")

                # Get the GPIOPin with pin number 15.
                pin = await my_board.gpio_pin_by_name(name="15")

                # Get if it is true or false that the state of the pin is high.
                high = await pin.get()

            Returns:
                bool: Indicates if the state of the pin is high.
            """
            ...

        @abc.abstractmethod
        async def get_pwm(self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs) -> float:
            """
            Get the pin's given duty cycle.

            ::

                my_board = Board.from_robot(robot=robot, name="my_board")

                # Get the GPIOPin with pin number 15.
                pin = await my_board.gpio_pin_by_name(name="15")

                # Get if it is true or false that the state of the pin is high.
                duty_cycle = await pin.get_pwm()

            Returns:
                float: The duty cycle.
            """
            ...

        @abc.abstractmethod
        async def set_pwm(self, duty_cycle: float, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs):
            """
            Set the pin to the given ``duty_cycle``.

            ::

                my_board = Board.from_robot(robot=robot, name="my_board")

                # Get the GPIOPin with pin number 15.
                pin = await my_board.gpio_pin_by_name(name="15")

                # Set the duty cycle to .6, meaning that this pin will be in the high state for
                # 60% of the duration of the PWM interval period.
                await pin.set_pwm(cycle=.6)

            Args:
                duty_cycle (float): The duty cycle.
            """
            ...

        @abc.abstractmethod
        async def get_pwm_frequency(self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs) -> int:
            """
            Get the PWM frequency of the pin.

            ::

                my_board = Board.from_robot(robot=robot, name="my_board")

                # Get the GPIOPin with pin number 15.
                pin = await my_board.gpio_pin_by_name(name="15")

                # Get the PWM frequency of this pin.
                freq = await pin.get_pwm_frequency()

            Returns:
                int: The PWM frequency.
            """
            ...

        @abc.abstractmethod
        async def set_pwm_frequency(
            self,
            frequency: int,
            *,
            extra: Optional[Dict[str, Any]] = None,
            timeout: Optional[float] = None,
            **kwargs,
        ):
            """
            Set the pin to the given PWM ``frequency`` (in Hz).
            When ``frequency`` is 0, it will use the board's default PWM frequency.

            ::

                my_board = Board.from_robot(robot=robot, name="my_board")

                # Get the GPIOPin with pin number 15.
                pin = await my_board.gpio_pin_by_name(name="15")

                # Set the PWM frequency of this pin to 1600 Hz.
                high = await pin.set_pwm_frequency(frequency=1600)

            Args:
                frequency (int): The frequency, in Hz.
            """
            ...

    @abc.abstractmethod
    async def analog_reader_by_name(self, name: str) -> AnalogReader:
        """
        Get an AnalogReader by ``name``.

        ::

            my_board = Board.from_robot(robot=robot, name="my_board")

            # Get the AnalogReader "my_example_analog_reader".
            reader = await my_board.analog_reader_by_name(name="my_example_analog_reader")

        Args:
            name (str): Name of the analog reader to be retrieved.

        Returns:
            AnalogReader: The analog reader.
        """
        ...

    @abc.abstractmethod
    async def digital_interrupt_by_name(self, name: str) -> DigitalInterrupt:
        """
        Get a DigitalInterrupt by ``name``.

        ::

            my_board = Board.from_robot(robot=robot, name="my_board")

            # Get the DigitalInterrupt "my_example_digital_interrupt".
            interrupt = await my_board.digital_interrupt_by_name(
                name="my_example_digital_interrupt")

        Args:
            name (str): Name of the digital interrupt.

        Returns:
            DigitalInterrupt: The digital interrupt.
        """
        ...

    @abc.abstractmethod
    async def gpio_pin_by_name(self, name: str) -> GPIOPin:
        """
        Get a GPIO Pin by ``name``.

        ::

            my_board = Board.from_robot(robot=robot, name="my_board")

            # Get the GPIOPin with pin number 15.
            pin = await my_board.gpio_pin_by_name(name="15")

        Args:
            name (str): Name of the GPIO pin.

        Returns:
            GPIOPin: The pin.
        """
        ...

    @abc.abstractmethod
    async def analog_reader_names(self) -> List[str]:
        """
        Get the names of all known analog readers.

        ::

            my_board = Board.from_robot(robot=robot, name="my_board")

            # Get the name of every AnalogReader configured on the board.
            names = await my_board.analog_reader_names()

        Returns:
            List[str]: The list of names of all known analog readers.
        """
        ...

    @abc.abstractmethod
    async def digital_interrupt_names(self) -> List[str]:
        """
        Get the names of all known digital interrupts.

        ::

            my_board = Board.from_robot(robot=robot, name="my_board")

            # Get the name of every DigitalInterrupt configured on the board.
            names = await my_board.digital_interrupt_names()

        Returns:
            List[str]: The names of the digital interrupts.
        """
        ...

    @abc.abstractmethod
    async def set_power_mode(
        self, mode: PowerMode.ValueType, duration: Optional[timedelta] = None, *, timeout: Optional[float] = None, **kwargs
    ):
        """
        Set the board to the indicated power mode.

        ::

            my_board = Board.from_robot(robot=robot, name="my_board")

            # Set the power mode of the board to OFFLINE_DEEP.
            status = await my_board.set_power_mode(mode=PowerMode.POWER_MODE_OFFLINE_DEEP)

        Args:
            mode (PowerMode): The desired power mode.
            duration (Optional[timedelta]): Requested duration to stay in power mode.
        """
        ...

    @abc.abstractmethod
    async def write_analog(self, pin: str, value: int, *, timeout: Optional[float] = None, **kwargs):
        """
        Write an analog value to a pin on the board.

        ::

            my_board = Board.from_robot(robot=robot, name="my_board")

            # Set pin 11 to value 48.
            await my_board.write_analog(pin="11", value=48)

        Args:
            pin (str): The name of the pin.
            value (int): The value to write.
        """
        ...

    @abc.abstractmethod
    async def stream_ticks(self, interrupts: List[DigitalInterrupt], *, timeout: Optional[float] = None, **kwargs) -> TickStream:
        """
        Stream digital interrupt ticks.

        ::


            my_board = Board.from_robot(robot=robot, name="my_board")
            di8 = await my_board.digital_interrupt_by_name(name="8"))
            di11 = await my_board.digital_interrupt_by_name(name="11"))

            Stream ticks from pins 8 and 11.
            ticks = my_board.stream_ticks([di8, di11])

        Args:
            interrupts (List[DigitalInterrupt]) : list of digital interrupts to recieve ticks from.

        Returns:
            TickStream: stream of ticks.
        """
        ...
