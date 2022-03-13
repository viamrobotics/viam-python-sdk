import abc
from dataclasses import dataclass
from multiprocessing import Queue
from typing import Callable, List

from viam.proto.api.common import BoardStatus

from ..component_base import ComponentBase


PostProcessor = Callable[[int], int]


class Board(ComponentBase):
    """
    A Board represents a physical general purpose board that contains various
    components such as analog readers, and digital interrupts.

    If you override the init function,
    you must call the super init function.
    """

    @dataclass
    class Attributes:
        remote: bool
        """
        If this board is accessed over a remote connection, e.g. gRPC
        """

    class AnalogReader(ComponentBase):
        """
        An AnalogReader represents an analog pin reader
        that resides on a board.
        """
        @abc.abstractmethod
        async def read(self) -> int:
            """
            Read the current value

            Returns:
                int: The current value
            """
            ...

    class DigitalInterrupt(ComponentBase):
        """
        A DigitalInterrupt represents a configured interrupt on the board that,
        when interrupted, calls the added callbacks. Post processors can also
        be added to modify what Value ultimately returns.
        """

        @abc.abstractmethod
        async def value(self) -> int:
            """
            Get the current value of the interrupt,
            which is based on the type of interrupt

            Returns:
                int: The current value
            """
            ...

        @abc.abstractmethod
        async def tick(self, high: bool, nanos: int):
            """
            This method is to be called either manually if the interrupt
            is a proxy to some real hardware interrupt or for tests.

            Args:
                high (bool): _description_
                nanos (int): Nanoseconds from an arbitrary point in time,
                    but always increasing and always needs to be accurate.
                    Using `time.time_ns()` would be acceptable
            """
            ...

        @abc.abstractmethod
        async def add_callback(self, queue: Queue):
            """
            Add a callback to be sent a low/high value on tick.

            Args:
                queue (Queue): The receiving queue
            """
            ...

        @abc.abstractmethod
        async def add_post_processor(self, processor: PostProcessor):
            """
            Add a post processor that should be used to modify what
            is returned by `self.value()`

            Args:
                processor (PostProcessor): The post processor to add
            """
            ...

    # AnalogReaderByName returns an analog reader by name.
    @abc.abstractmethod
    async def analog_reader_by_name(self, name: str) -> AnalogReader:
        """
        Get an AnalogReader by name

        Args:
            name (str): Name of the analog reader

        Returns:
            AnalogReader: the analog reader
        """
        ...

        # DigitalInterruptByName returns a digital interrupt by name.
    @abc.abstractmethod
    async def digital_interrupt_by_name(self, name: str) -> DigitalInterrupt:
        """
        Get a DigitalInterrupt by name

        Args:
            name (str): Name of the digital interrupt

        Returns:
            DigitalInterrupt: the digital interrupt
        """
        ...

    @abc.abstractmethod
    async def spi_names(self) -> List[str]:
        """
        Get the names of all known SPI busses.

        Returns:
            List[str]: The names of the SPI busses
        """

    @abc.abstractmethod
    async def i2c_names(self) -> List[str]:
        """
        Get the names of all known I2C busses.

        Returns:
            List[str]: The names of the I2C busses
        """
        ...

    @abc.abstractmethod
    async def analog_reader_names(self) -> List[str]:
        """
        Get the names of all known analog readers

        Returns:
            List[str]: The names of the analog readers
        """
        ...

    @abc.abstractmethod
    async def digital_interrupt_names(self) -> List[str]:
        """
        Get the names of all known digital interrupts

        Returns:
            List[str]: The names of the digital interrupts
        """

    @abc.abstractmethod
    async def set_gpio(self, pin: str, high: bool):
        """
        Set the given pin to either low or high

        Args:
            pin (str): The pin identifier
            high (bool): Whether the pin should be set to high
        """
        ...

    @abc.abstractmethod
    async def get_gpio(self, pin: str) -> bool:
        """
        Get the hihg/low state of the given pin

        Args:
            pin (str): The pin identifier

        Returns:
            bool: Whether the pin is in the high state
        """
        ...

    @abc.abstractmethod
    async def set_pwm(self, pin: str, duty_cycle: float):
        """
        Set the given pin to the given duty cycle

        Args:
            pin (str): The pin
            duty_cycle (float): The duty cycle as a percent
        """
        ...

    @abc.abstractmethod
    async def set_pwm_freq(self, pin: str, frequency: int):
        """
        Set the given pin to the given PWM frequency.
        A frequency of 0 (zero) will use the board's default PWM frequency

        Args:
            pin (str): The pin
            frequency (int): The PWM frequency in Hz
        """
        ...

    @abc.abstractmethod
    async def status(self) -> BoardStatus:
        """
        Return the current status of the board.

        Returns:
            BoardStatus: the status
        """

    # ModelAttributes returns attributes related to the model of this board.
    @abc.abstractmethod
    async def model_attributes(self) -> Attributes:
        """
        Get the attributes related to the model of this board

        Returns:
            Attributes: The attributes
        """
        ...
