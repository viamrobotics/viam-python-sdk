from datetime import timedelta
from typing import Any, Dict, List, Mapping, Optional

from google.protobuf.duration_pb2 import Duration
from grpclib.client import Channel

from viam.proto.common import BoardStatus, DoCommandRequest, DoCommandResponse, Geometry
from viam.proto.component.board import (
    BoardServiceStub,
    GetDigitalInterruptValueRequest,
    GetDigitalInterruptValueResponse,
    GetGPIORequest,
    GetGPIOResponse,
    PowerMode,
    PWMFrequencyRequest,
    PWMFrequencyResponse,
    PWMRequest,
    PWMResponse,
    ReadAnalogReaderRequest,
    ReadAnalogReaderResponse,
    SetGPIORequest,
    SetPowerModeRequest,
    SetPWMFrequencyRequest,
    SetPWMRequest,
    StatusRequest,
    StatusResponse,
    WriteAnalogRequest,
)
from viam.resource.rpc_client_base import ReconfigurableResourceRPCClientBase
from viam.utils import ValueTypes, dict_to_struct, get_geometries, struct_to_dict

from . import Board


class AnalogReaderClient(Board.AnalogReader):
    def __init__(self, name: str, board: "BoardClient"):
        self.board = board
        super().__init__(name)

    async def read(
        self,
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
        **__,
    ) -> int:
        if extra is None:
            extra = {}
        request = ReadAnalogReaderRequest(board_name=self.board.name, analog_reader_name=self.name, extra=dict_to_struct(extra))
        response: ReadAnalogReaderResponse = await self.board.client.ReadAnalogReader(request, timeout=timeout)
        return response.value


class DigitalInterruptClient(Board.DigitalInterrupt):
    def __init__(self, name: str, board: "BoardClient"):
        self.board = board
        super().__init__(name)

    async def value(
        self,
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
        **__,
    ) -> int:
        if extra is None:
            extra = {}
        request = GetDigitalInterruptValueRequest(board_name=self.board.name, digital_interrupt_name=self.name, extra=dict_to_struct(extra))
        response: GetDigitalInterruptValueResponse = await self.board.client.GetDigitalInterruptValue(request, timeout=timeout)
        return response.value


class GPIOPinClient(Board.GPIOPin):
    def __init__(self, name: str, board: "BoardClient"):
        self.board = board
        super().__init__(name)

    async def get(
        self,
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
        **__,
    ) -> bool:
        if extra is None:
            extra = {}
        request = GetGPIORequest(name=self.board.name, pin=self.name, extra=dict_to_struct(extra))
        response: GetGPIOResponse = await self.board.client.GetGPIO(request, timeout=timeout)
        return response.high

    async def set(
        self,
        high: bool,
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
        **__,
    ):
        if extra is None:
            extra = {}
        request = SetGPIORequest(name=self.board.name, pin=self.name, high=high, extra=dict_to_struct(extra))
        await self.board.client.SetGPIO(request, timeout=timeout)

    async def get_pwm(
        self,
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
        **__,
    ) -> float:
        if extra is None:
            extra = {}
        request = PWMRequest(name=self.board.name, pin=self.name, extra=dict_to_struct(extra))
        response: PWMResponse = await self.board.client.PWM(request, timeout=timeout)
        return response.duty_cycle_pct

    async def set_pwm(
        self,
        duty_cycle: float,
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
        **__,
    ):
        if extra is None:
            extra = {}
        request = SetPWMRequest(name=self.board.name, pin=self.name, duty_cycle_pct=duty_cycle, extra=dict_to_struct(extra))
        await self.board.client.SetPWM(request, timeout=timeout)

    async def get_pwm_frequency(
        self,
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
        **__,
    ) -> int:
        if extra is None:
            extra = {}
        request = PWMFrequencyRequest(name=self.board.name, pin=self.name, extra=dict_to_struct(extra))
        response: PWMFrequencyResponse = await self.board.client.PWMFrequency(request, timeout=timeout)
        return response.frequency_hz

    async def set_pwm_frequency(
        self,
        frequency: int,
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
        **__,
    ):
        if extra is None:
            extra = {}
        request = SetPWMFrequencyRequest(name=self.board.name, pin=self.name, frequency_hz=frequency, extra=dict_to_struct(extra))
        await self.board.client.SetPWMFrequency(request, timeout=timeout)


class BoardClient(Board, ReconfigurableResourceRPCClientBase):
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

    async def status(
        self,
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
        **__,
    ) -> BoardStatus:
        if extra is None:
            extra = {}
        request = StatusRequest(name=self.name, extra=dict_to_struct(extra))
        response: StatusResponse = await self.client.Status(request, timeout=timeout)
        return response.status

    async def do_command(
        self,
        command: Mapping[str, ValueTypes],
        *,
        timeout: Optional[float] = None,
        **__,
    ) -> Mapping[str, ValueTypes]:
        request = DoCommandRequest(name=self.name, command=dict_to_struct(command))
        response: DoCommandResponse = await self.client.DoCommand(request, timeout=timeout)
        return struct_to_dict(response.result)

    async def set_power_mode(
        self,
        mode: PowerMode.ValueType,
        duration: Optional[timedelta] = None,
        *,
        timeout: Optional[float] = None,
        **__,
    ):
        duration_pb: Optional[Duration] = None
        if duration is not None:
            duration_pb = [(d, d.FromTimedelta(duration)) for d in [Duration()]][0][0]
        request = SetPowerModeRequest(name=self.name, power_mode=mode, duration=duration_pb)
        await self.client.SetPowerMode(request, timeout=timeout)

    async def get_geometries(self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None) -> List[Geometry]:
        return await get_geometries(self.client, self.name, extra, timeout)

    async def write_analog(
        self,
        pin: str,
        value: int,
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
        **__,
    ):
        if extra is None:
            extra = {}
        request = WriteAnalogRequest(name=self.name, pin=pin, value=value, extra=dict_to_struct(extra))
        await self.client.WriteAnalog(request, timeout=timeout)
