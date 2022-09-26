from grpclib.server import Stream
from viam.components.service_base import ComponentServiceBase
from viam.errors import ComponentNotFoundError
from viam.proto.component.board import (
    BoardServiceBase,
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
    SetGPIOResponse,
    SetPWMFrequencyRequest,
    SetPWMFrequencyResponse,
    SetPWMRequest,
    SetPWMResponse,
    StatusRequest,
    StatusResponse,
)
from viam.utils import struct_to_dict

from .board import Board


class BoardService(BoardServiceBase, ComponentServiceBase[Board]):
    """
    gRPC Service for a Board
    """

    RESOURCE_TYPE = Board

    async def Status(self, stream: Stream[StatusRequest, StatusResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        try:
            board = self.get_component(name)
        except ComponentNotFoundError as e:
            raise e.grpc_error
        status = await board.status(extra=struct_to_dict(request.extra))
        response = StatusResponse(status=status)
        await stream.send_message(response)

    async def SetGPIO(self, stream: Stream[SetGPIORequest, SetGPIOResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        try:
            board = self.get_component(name)
            pin = await board.gpio_pin_by_name(request.pin)
        except ComponentNotFoundError as e:
            raise e.grpc_error
        await pin.set(request.high, extra=struct_to_dict(request.extra))
        response = SetGPIOResponse()
        await stream.send_message(response)

    async def GetGPIO(self, stream: Stream[GetGPIORequest, GetGPIOResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        try:
            board = self.get_component(name)
            pin = await board.gpio_pin_by_name(request.pin)
        except ComponentNotFoundError as e:
            raise e.grpc_error
        high = await pin.get(extra=struct_to_dict(request.extra))
        response = GetGPIOResponse(high=high)
        await stream.send_message(response)

    async def PWM(self, stream: Stream[PWMRequest, PWMResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        try:
            board = self.get_component(name)
            pin = await board.gpio_pin_by_name(request.pin)
        except ComponentNotFoundError as e:
            raise e.grpc_error
        pwm = await pin.get_pwm(extra=struct_to_dict(request.extra))
        response = PWMResponse(duty_cycle_pct=pwm)
        await stream.send_message(response)

    async def SetPWM(self, stream: Stream[SetPWMRequest, SetPWMResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        try:
            board = self.get_component(name)
            pin = await board.gpio_pin_by_name(request.pin)
        except ComponentNotFoundError as e:
            raise e.grpc_error
        await pin.set_pwm(request.duty_cycle_pct, extra=struct_to_dict(request.extra))
        response = SetPWMResponse()
        await stream.send_message(response)

    async def PWMFrequency(self, stream: Stream[PWMFrequencyRequest, PWMFrequencyResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        try:
            board = self.get_component(name)
            pin = await board.gpio_pin_by_name(request.pin)
        except ComponentNotFoundError as e:
            raise e.grpc_error
        frequency = await pin.get_pwm_frequency(extra=struct_to_dict(request.extra))
        response = PWMFrequencyResponse(frequency_hz=frequency)
        await stream.send_message(response)

    async def SetPWMFrequency(self, stream: Stream[SetPWMFrequencyRequest, SetPWMFrequencyResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        try:
            board = self.get_component(name)
            pin = await board.gpio_pin_by_name(request.pin)
        except ComponentNotFoundError as e:
            raise e.grpc_error
        await pin.set_pwm_frequency(request.frequency_hz, extra=struct_to_dict(request.extra))
        response = SetPWMFrequencyResponse()
        await stream.send_message(response)

    async def ReadAnalogReader(self, stream: Stream[ReadAnalogReaderRequest, ReadAnalogReaderResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.board_name
        try:
            board = self.get_component(name)
            analog_reader = await board.analog_reader_by_name(request.analog_reader_name)
        except ComponentNotFoundError as e:
            raise e.grpc_error
        value = await analog_reader.read(extra=struct_to_dict(request.extra))
        response = ReadAnalogReaderResponse(value=value)
        await stream.send_message(response)

    async def GetDigitalInterruptValue(self, stream: Stream[GetDigitalInterruptValueRequest, GetDigitalInterruptValueResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.board_name
        try:
            board = self.get_component(name)
            interrupt = await board.digital_interrupt_by_name(request.digital_interrupt_name)
        except ComponentNotFoundError as e:
            raise e.grpc_error
        value = await interrupt.value(extra=struct_to_dict(request.extra))
        response = GetDigitalInterruptValueResponse(value=value)
        await stream.send_message(response)
