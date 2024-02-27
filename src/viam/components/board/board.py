import abc
from datetime import timedelta
from typing import Any, Dict, Final, List, Optional

from viam.proto.common import BoardStatus
from viam.proto.component.board import PowerMode
from viam.resource.types import RESOURCE_NAMESPACE_RDK, RESOURCE_TYPE_COMPONENT, Subtype

from ..component_base import ComponentBase


class Board(ComponentBase):
    """
    Board represents a physical general purpose compute board that contains various
    components such as analog readers, and digital interrupts.

    This acts as an abstract base class for any drivers representing specific
    board implementations. This cannot be used on its own. If the ``__init__()`` function is
    overridden, it must call the ``super().__init__()`` function.
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

            Args:
                high (bool): When true, sets the pin to high. When false, sets the pin to low.
            """
            ...

        @abc.abstractmethod
        async def get(self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs) -> bool:
            """
            Get the high/low state of the pin.

            Returns:
                bool: Indicates if the state of the pin is high.
            """
            ...

        @abc.abstractmethod
        async def get_pwm(self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs) -> float:
            """
            Get the pin's given duty cycle.

            Returns:
                float: The duty cycle.
            """
            ...

        @abc.abstractmethod
        async def set_pwm(self, duty_cycle: float, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs):
            """
            Set the pin to the given ``duty_cycle``.

            Args:
                duty_cycle (float): The duty cycle.
            """
            ...

        @abc.abstractmethod
        async def get_pwm_frequency(self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs) -> int:
            """
            Get the PWM frequency of the pin.

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

            Args:
                frequency (int): The frequency, in Hz.
            """
            ...

    @abc.abstractmethod
    async def analog_reader_by_name(self, name: str) -> AnalogReader:
        """
        Get an AnalogReader by ``name``.

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

        Args:
            name (str): Name of the digital interrupt.

        Returns:
            DigitalInterrupt: the digital interrupt.
        """
        ...

    @abc.abstractmethod
    async def gpio_pin_by_name(self, name: str) -> GPIOPin:
        """
        Get a GPIO Pin by ``name``.

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
    async def status(self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs) -> BoardStatus:
        """
        Return the current status of the board.

        Returns:
            viam.proto.common.BoardStatus: the status.
        """
        ...

    @abc.abstractmethod
    async def set_power_mode(
        self, mode: PowerMode.ValueType, duration: Optional[timedelta] = None, *, timeout: Optional[float] = None, **kwargs
    ):
        """
        Set the board to the indicated power mode.

        Args:
            mode: the desired power mode
        """
        ...

    @abc.abstractmethod
    async def write_analog(self, pin: str, value: int, *, timeout: Optional[float] = None, **kwargs):
        """
        Write an analog value to a pin on the board.

        Args:
            pin (str): name of the pin.
            value (int): value to write.
        """
        ...
