from multiprocessing import Queue
from typing import List, Optional
from grpclib.client import Channel
from viam.proto.api.common import BoardStatus
from viam.proto.api.component.board import (BoardServiceStub,
                                            GetDigitalInterruptValueRequest,
                                            GetDigitalInterruptValueResponse,
                                            GetGPIORequest, GetGPIOResponse,
                                            ReadAnalogReaderRequest,
                                            ReadAnalogReaderResponse,
                                            SetGPIORequest,
                                            SetPWMFrequencyRequest,
                                            SetPWMRequest,
                                            StatusRequest, StatusResponse)

from .board import Board, PostProcessor


class AnalogReaderClient(Board.AnalogReader):
    def __init__(self, name: str, board: 'BoardClient'):
        self.board = board
        super().__init__(name)

    async def read(self) -> int:
        request = ReadAnalogReaderRequest(
            board_name=self.board.name,
            analog_reader_name=self.name

        )
        response: ReadAnalogReaderResponse = \
            await self.board.client.ReadAnalogReader(request)
        return response.value


class DigitalInterruptClient(Board.DigitalInterrupt):
    def __init__(self, name: str, board: 'BoardClient'):
        self.board = board
        super().__init__(name)

    async def value(self) -> int:
        request = GetDigitalInterruptValueRequest(
            board_name=self.board.name,
            digital_interrupt_name=self.name
        )
        response: GetDigitalInterruptValueResponse = \
            await self.board.client.GetDigitalInterruptValue(request)
        return response.value

    async def tick(self, high: bool, nanos: int):
        raise NotImplementedError()

    async def add_callback(self, queue: Queue):
        raise NotImplementedError()

    async def add_post_processor(self, processor: PostProcessor):
        raise NotImplementedError()


class BoardClient(Board):
    """
    gRPC client for the Board component.
    """

    def __init__(self, name: str, channel: Channel):
        self.name = name
        self.client = BoardServiceStub(channel)
        self._spi_names: Optional[List[str]] = None
        self._i2c_names: Optional[List[str]] = None
        self._analog_reader_names: Optional[List[str]] = None
        self._digital_interrupt_names: Optional[List[str]] = None

    async def analog_reader_by_name(self, name: str) -> Board.AnalogReader:
        return AnalogReaderClient(name, self)

    async def digital_interrupt_by_name(
        self,
        name: str
    ) -> Board.DigitalInterrupt:
        return DigitalInterruptClient(name, self)

    async def spi_names(self) -> List[str]:
        return self._spi_names or []

    async def i2c_names(self) -> List[str]:
        return self._i2c_names or []

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

    async def set_gpio(self, pin: str, high: bool):
        request = SetGPIORequest(name=self.name, pin=pin, high=high)
        await self.client.SetGPIO(request)

    async def get_gpio(self, pin: str) -> bool:
        request = GetGPIORequest(name=self.name, pin=pin)
        response: GetGPIOResponse = await self.client.GetGPIO(request)
        return response.high

    async def set_pwm(self, pin: str, duty_cycle: float):
        request = SetPWMRequest(name=self.name, pin=pin,
                                duty_cycle_pct=duty_cycle)
        await self.client.SetPWM(request)

    async def set_pwm_freq(self, pin: str, frequency: int):
        request = SetPWMFrequencyRequest(
            name=self.name, pin=pin, frequency_hz=frequency)
        await self.client.SetPWMFrequency(request)

    async def status(self) -> BoardStatus:
        request = StatusRequest(name=self.name)
        response: StatusResponse = await self.client.Status(request)
        return response.status

    async def model_attributes(self) -> Board.Attributes:
        return Board.Attributes(remote=True)
