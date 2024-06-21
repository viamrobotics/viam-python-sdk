import abc
import sys
from datetime import timedelta
from typing import Any, Dict, Final, List, Optional

from viam.proto.component.board import PowerMode, ReadAnalogReaderResponse, StreamTicksResponse
from viam.resource.types import RESOURCE_NAMESPACE_RDK, RESOURCE_TYPE_COMPONENT, Subtype
from viam.streams import Stream

from ..component_base import ComponentBase

if sys.version_info >= (3, 10):
    from typing import TypeAlias
else:
    from typing_extensions import TypeAlias

Tick = StreamTicksResponse
TickStream = Stream[Tick]


class Board(ComponentBase):
    """
    Board represents a physical general purpose compute board that contains various
    components such as analog readers/writers, and digital interrupts.

    This acts as an abstract base class for any drivers representing specific
    board implementations. This cannot be used on its own. If the ``__init__()`` function is
    overridden, it must call the ``super().__init__()`` function.

    ::

        from viam.components.board import Board

    For more information, see `Board component <https://docs.viam.com/components/board/>`_.
    """

    SUBTYPE: Final = Subtype(  # pyright: ignore [reportIncompatibleVariableOverride]
        RESOURCE_NAMESPACE_RDK, RESOURCE_TYPE_COMPONENT, "board"
    )

    class Analog:
        """
        Analog represents an analog pin reader or writer that resides on a Board.
        """

        name: str
        """The name of the analog pin"""

        Value: "TypeAlias" = ReadAnalogReaderResponse
        """
        Value contains the result of reading an analog reader. It contains the raw data read,
        the reader's minimum and maximum possible values, and its step size (the minimum possible
        change between values it can read).

        For more information, see `analogs <https://docs.viam.com/components/board/#analogs>`_.
        """

        def __init__(self, name: str):
            self.name = name

        @abc.abstractmethod
        async def read(self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs) -> Value:
            """
            Read the current value from the reader.

            ::

                my_board = Board.from_robot(robot=robot, name="my_board")

                # Get the Analog "my_example_analog_reader".
                reader = await my_board.analog_reader_by_name(
                    name="my_example_analog_reader")

                # Get the value of the digital signal "my_example_analog_reader" has most
                # recently measured.
                reading = await reader.read()

            Returns:
                Value: The current value, including the min, max, and step_size of the reader.

            For more information, see `Board component Analog API <https://docs.viam.com/components/board/#analog-api>`_.
            """
            ...

        @abc.abstractmethod
        async def write(self, value: int, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs):
            """
            Write a value to the Analog writer.

            ::

                my_board = Board.from_robot(robot=robot, name="my_board")

                # Get the Analog "my_example_analog_writer".
                writer = await my_board.analog_by_name(
                    name="my_example_analog_writer")

                await writer.write(42)

            Args:
                value (int): Value to write to the analog writer.

            For more information, see `Board component Analog API <https://docs.viam.com/components/board/#analog-api>`_.
            """
            ...

    class DigitalInterrupt:
        """
        DigitalInterrupt represents a configured interrupt on the Board that
        when interrupted, calls the added callbacks. Post processors can
        be added to modify what Value it ultimately returns.

        For more information, see `digital_interrupts <https://docs.viam.com/components/board/#digital_interrupts>`_.
        """

        name: str
        """The name of the digital interrupt."""

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

            For more information, see
            `Board component DigitalInterrupt API <https://docs.viam.com/components/board/#digitalinterrupt-api>`_.
            """
            ...

    class GPIOPin:
        """
        Abstract representation of an individual GPIO pin on a board.
        """

        name: str
        """The name of the GPIO pin."""

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

            For more information, see `GPIOPin API <https://docs.viam.com/components/board/#gpiopin-api>`_.
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

            For more information, see `GPIOPin API <https://docs.viam.com/components/board/#gpiopin-api>`_.
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

            For more information, see `GPIOPin API <https://docs.viam.com/components/board/#gpiopin-api>`_.
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

            For more information, see `GPIOPin API <https://docs.viam.com/components/board/#gpiopin-api>`_.
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

            For more information, see `GPIOPin API <https://docs.viam.com/components/board/#gpiopin-api>`_.
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

            For more information, see `GPIOPin API <https://docs.viam.com/components/board/#gpiopin-api>`_.
            """
            ...

    @abc.abstractmethod
    async def analog_by_name(self, name: str) -> Analog:
        """
        Get an Analog (reader or writer) by ``name``.

        ::

            my_board = Board.from_robot(robot=robot, name="my_board")

            # Get the Analog "my_example_analog_reader".
            reader = await my_board.analog_by_name(name="my_example_analog_reader")

        Args:
            name (str): Name of the analog reader to be retrieved.

        Returns:
            Analog: The analog reader or writer.

        For more information, see `Board component <https://docs.viam.com/components/board/>`_.
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

        For more information, see `Board component <https://docs.viam.com/components/board/>`_.
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

        For more information, see `Board component <https://docs.viam.com/components/board/>`_.
        """
        ...

    @abc.abstractmethod
    async def analog_names(self) -> List[str]:
        """
        Get the names of all known analog readers and/or writers.

        ::

            my_board = Board.from_robot(robot=robot, name="my_board")

            # Get the name of every Analog configured on the board.
            names = await my_board.analog_names()

        Returns:
            List[str]: The list of names of all known analog readers/writers.

        For more information, see `Board component <https://docs.viam.com/components/board/>`_.
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

        For more information, see `Board component <https://docs.viam.com/components/board/>`_.
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

        For more information, see `Board component <https://docs.viam.com/components/board/>`_.
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

            # Iterate over stream of ticks from pins 8 and 11.
            async for tick in my_board.stream_ticks([di8, di11]):
                print(f"Pin {tick.pin_name} changed to {'high' if tick.high else 'low'} at {tick.time}")


        Args:
            interrupts (List[DigitalInterrupt]) : list of digital interrupts to receive ticks from.

        Returns:
            TickStream: stream of ticks.

        For more information, see `Board component <https://docs.viam.com/components/board/>`_.
        """
        ...
