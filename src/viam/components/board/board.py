import abc
from dataclasses import dataclass
from multiprocessing import Queue
from typing import Any, Callable, Dict, List, Optional

from viam.proto.common import BoardStatus

from ..component_base import ComponentBase


PostProcessor = Callable[[int], int]


class Board(ComponentBase):
    """
    Board represents a physical general purpose compute board that contains various
    components such as analog readers, and digital interrupts.

    This acts as an abstract base class for any drivers representing specific
    board implementations. This cannot be used on its own. If the `__init__()` function is
    overridden, it must call the `super().__init__()` function.
    """

    @dataclass
    class Attributes:
        remote: bool
        """
        Indicates whether this board is accessed over a remote connection, e.g. gRPC.
        """

    class AnalogReader(ComponentBase):
        """
        AnalogReader represents an analog pin reader that resides on a Board.
        """

        @abc.abstractmethod
        async def read(self, extra: Optional[Dict[str, Any]] = None, **kwargs) -> int:
            """
            Read the current value.

            Returns:
                int: The current value.
            """
            ...

    class DigitalInterrupt(ComponentBase):
        """
        DigitalInterrupt represents a configured interrupt on the Board that
        when interrupted, calls the added callbacks. Post processors can
        be added to modify what Value it ultimately returns.
        """

        @abc.abstractmethod
        async def value(self, extra: Optional[Dict[str, Any]] = None, **kwargs) -> int:
            """
            Get the current value of the interrupt,
            which is based on the type of interrupt.

            Returns:
                int: The current value.
            """
            ...

        @abc.abstractmethod
        async def tick(self, high: bool, nanos: int):
            """
            This method is to be called either manually if the interrupt
            is a proxy to some real hardware interrupt or for tests.

            Args:
                high (bool): If the signal of the interrupt is high.
                nanos (int): Nanoseconds from an arbitrary point in time,
                    but always increasing and always needs to be accurate.
                    Using `time.time_ns()` would be acceptable.
            """
            ...

        @abc.abstractmethod
        async def add_callback(self, queue: Queue):
            """
            Add a callback to be sent the low/high value on `tick()`.

            Args:
                queue (Queue): The receiving queue.
            """
            ...

        @abc.abstractmethod
        async def add_post_processor(self, processor: PostProcessor):
            """
            Add a post processor that should be used to modify what
            is returned by `self.value()`

            Args:
                processor (PostProcessor): The post processor to add.
            """
            ...

    class GPIOPin(ComponentBase):
        """
        Abstract representation of an individual GPIO pin on a board

        Args:
            ComponentBase (_type_): _description_
        """

        @abc.abstractmethod
        async def set(self, high: bool, extra: Optional[Dict[str, Any]] = None, **kwargs):
            """
            Set the pin to either low or high.

            Args:
                high (bool): When true, sets the pin to high. When false, sets the pin to low.
            """
            ...

        @abc.abstractmethod
        async def get(self, extra: Optional[Dict[str, Any]] = None, **kwargs) -> bool:
            """
            Get the high/low state of the pin.

            Returns:
                bool: Indicates if the state of the pin is high.
            """
            ...

        @abc.abstractmethod
        async def get_pwm(self, extra: Optional[Dict[str, Any]] = None, **kwargs) -> float:
            """
            Get the pin's given duty cycle.

            Returns:
                float: The duty cycle.
            """
            ...

        @abc.abstractmethod
        async def set_pwm(self, duty_cycle: float, extra: Optional[Dict[str, Any]] = None, **kwargs):
            """
            Set the pin to the given `duty_cycle`.

            Args:
                duty_cycle (float): The duty cycle.
            """
            ...

        @abc.abstractmethod
        async def get_pwm_frequency(self, extra: Optional[Dict[str, Any]] = None, **kwargs) -> int:
            """
            Get the PWM frequency of the pin.

            Returns:
                int: The PWM frequency.
            """
            ...

        @abc.abstractmethod
        async def set_pwm_frequency(self, frequency: int, extra: Optional[Dict[str, Any]] = None, **kwargs):
            """
            Set the pin to the given PWM `frequency` (in Hz).
            When `frequency` is 0, it will use the board's default PWM frequency.

            Args:
                frequency (int): The frequency, in Hz.
            """
            ...

    @abc.abstractmethod
    async def analog_reader_by_name(self, name: str) -> AnalogReader:
        """
        Get an AnalogReader by `name`.

        Args:
            name (str): Name of the analog reader to be retrieved.

        Returns:
            AnalogReader: The analog reader.
        """
        ...

    @abc.abstractmethod
    async def digital_interrupt_by_name(self, name: str) -> DigitalInterrupt:
        """
        Get a DigitalInterrupt by `name`.

        Args:
            name (str): Name of the digital interrupt.

        Returns:
            DigitalInterrupt: the digital interrupt.
        """
        ...

    @abc.abstractmethod
    async def gpio_pin_by_name(self, name: str) -> GPIOPin:
        """
        Get a GPIO Pin by `name`.

        Args:
            name (str): Name of the GPIO pin.

        Returns:
            GPIOPin: the pin.
        """
        ...

    @abc.abstractmethod
    async def analog_reader_names(self) -> List[str]:
        """
        Get the names of all known analog readers.

        Returns:
            List[str]: The names of the analog readers..
        """
        ...

    @abc.abstractmethod
    async def digital_interrupt_names(self) -> List[str]:
        """
        Get the names of all known digital interrupts.

        Returns:
            List[str]: The names of the digital interrupts.
        """
        ...

    @abc.abstractmethod
    async def status(self, extra: Optional[Dict[str, Any]] = None, **kwargs) -> BoardStatus:
        """
        Return the current status of the board.

        Returns:
            BoardStatus: the status.
        """
        ...

    @abc.abstractmethod
    async def model_attributes(self) -> Attributes:
        """
        Get the attributes related to the model of this board.

        Returns:
            Attributes: The attributes.
        """
        ...
