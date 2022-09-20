from multiprocessing import Queue
from typing import Any, Dict, List, Optional

from grpclib.client import Channel
from viam.components.generic.client import do_command
from viam.proto.common import BoardStatus
from viam.proto.component.board import (
    BoardServiceStub,
    GetDigitalInterruptValueRequest,
    GetDigitalInterruptValueResponse,
    GetGPIORequest,
    GetGPIOResponse,
    PWMFrequencyRequest,
    PWMFrequencyResponse,
    PWMRequest,
    PWMResponse,
    ReadAnalogReaderRequest,
    ReadAnalogReaderResponse,
    SetGPIORequest,
    SetPWMFrequencyRequest,
    SetPWMRequest,
    StatusRequest,
    StatusResponse,
)
from viam.utils import dict_to_struct

from .board import Board, PostProcessor


class AnalogReaderClient(Board.AnalogReader):
    def __init__(self, name: str, board: "BoardClient"):
        self.board = board
        super().__init__(name)

    async def read(self, extra: Optional[Dict[str, Any]] = None) -> int:
        if extra is None:
            extra = {}
        request = ReadAnalogReaderRequest(board_name=self.board.name, analog_reader_name=self.name, extra=dict_to_struct(extra))
        response: ReadAnalogReaderResponse = await self.board.client.ReadAnalogReader(request)
        return response.value


class DigitalInterruptClient(Board.DigitalInterrupt):
    def __init__(self, name: str, board: "BoardClient"):
        self.board = board
        super().__init__(name)

    async def value(self, extra: Optional[Dict[str, Any]] = None) -> int:
        if extra is None:
            extra = {}
        request = GetDigitalInterruptValueRequest(board_name=self.board.name, digital_interrupt_name=self.name, extra=dict_to_struct(extra))
        response: GetDigitalInterruptValueResponse = await self.board.client.GetDigitalInterruptValue(request)
        return response.value

    async def tick(self, high: bool, nanos: int):
        raise NotImplementedError()

    async def add_callback(self, queue: Queue):
        raise NotImplementedError()

    async def add_post_processor(self, processor: PostProcessor):
        raise NotImplementedError()


class GPIOPinClient(Board.GPIOPin):
    def __init__(self, name: str, board: "BoardClient"):
        self.board = board
        super().__init__(name)

    async def get(self, extra: Optional[Dict[str, Any]] = None) -> bool:
        if extra is None:
            extra = {}
        request = GetGPIORequest(name=self.board.name, pin=self.name, extra=dict_to_struct(extra))
        response: GetGPIOResponse = await self.board.client.GetGPIO(request)
        return response.high

    async def set(self, high: bool, extra: Optional[Dict[str, Any]] = None):
        if extra is None:
            extra = {}
        request = SetGPIORequest(name=self.board.name, pin=self.name, high=high, extra=dict_to_struct(extra))
        await self.board.client.SetGPIO(request)

    async def get_pwm(self, extra: Optional[Dict[str, Any]] = None) -> float:
        if extra is None:
            extra = {}
        request = PWMRequest(name=self.board.name, pin=self.name, extra=dict_to_struct(extra))
        response: PWMResponse = await self.board.client.PWM(request)
        return response.duty_cycle_pct

    async def set_pwm(self, duty_cycle: float, extra: Optional[Dict[str, Any]] = None):
        if extra is None:
            extra = {}
        request = SetPWMRequest(name=self.board.name, pin=self.name, duty_cycle_pct=duty_cycle, extra=dict_to_struct(extra))
        await self.board.client.SetPWM(request)

    async def get_pwm_frequency(self, extra: Optional[Dict[str, Any]] = None) -> int:
        if extra is None:
            extra = {}
        request = PWMFrequencyRequest(name=self.board.name, pin=self.name, extra=dict_to_struct(extra))
        response: PWMFrequencyResponse = await self.board.client.PWMFrequency(request)
        return response.frequency_hz

    async def set_pwm_frequency(self, frequency: int, extra: Optional[Dict[str, Any]] = None):
        if extra is None:
            extra = {}
        request = SetPWMFrequencyRequest(name=self.board.name, pin=self.name, frequency_hz=frequency, extra=dict_to_struct(extra))
        await self.board.client.SetPWMFrequency(request)


class BoardClient(Board):
    """
    gRPC client for the Board component.
    """

    def __init__(self, name: str, channel: Channel):
        self.channel = channel
        self.client = BoardServiceStub(channel)
        self._analog_reader_names: Optional[List[str]] = None
        self._digital_interrupt_names: Optional[List[str]] = None
        super().__init__(name)

    async def analog_reader_by_name(self, name: str) -> Board.AnalogReader:
        return AnalogReaderClient(name, self)

    async def digital_interrupt_by_name(self, name: str) -> Board.DigitalInterrupt:
        return DigitalInterruptClient(name, self)

    async def gpio_pin_by_name(self, name: str) -> Board.GPIOPin:
        return GPIOPinClient(name, self)

    async def analog_reader_names(self) -> List[str]:
        if self._analog_reader_names is None:
            status = await self.status()
            names = [name for name in status.analogs.keys()]
            self._analog_reader_names = names
        return self._analog_reader_names

    async def digital_interrupt_names(self) -> List[str]:
        if self._digital_interrupt_names is None:
            status = await self.status()
            names = [name for name in status.digital_interrupts.keys()]
            self._digital_interrupt_names = names
        return self._digital_interrupt_names

    async def status(self, extra: Optional[Dict[str, Any]] = None) -> BoardStatus:
        if extra is None:
            extra = {}
        request = StatusRequest(name=self.name, extra=dict_to_struct(extra))
        response: StatusResponse = await self.client.Status(request)
        return response.status

    async def model_attributes(self) -> Board.Attributes:
        return Board.Attributes(remote=True)

    async def do_command(self, command: Dict[str, Any]) -> Dict[str, Any]:
        return await do_command(self.channel, self.name, command)
