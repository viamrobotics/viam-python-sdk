from grpclib.server import Stream
from viam.components.service_base import ComponentServiceBase
from viam.errors import ComponentNotFoundError
from viam.proto.api.component.board import (BoardServiceBase,
                                            GetDigitalInterruptValueRequest,
                                            GetDigitalInterruptValueResponse,
                                            GetGPIORequest, GetGPIOResponse,
                                            ReadAnalogReaderRequest,
                                            ReadAnalogReaderResponse,
                                            SetGPIORequest, SetGPIOResponse,
                                            SetPWMFrequencyRequest,
                                            SetPWMFrequencyResponse,
                                            SetPWMRequest, SetPWMResponse,
                                            StatusRequest, StatusResponse)

from .board import Board


class BoardService(BoardServiceBase, ComponentServiceBase[Board]):
    """
    gRPC Service for a Board
    """

    RESOURCE_TYPE = Board

    async def Status(
        self,
        stream: Stream[StatusRequest, StatusResponse]
    ) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        try:
            board = self.get_component(name)
        except ComponentNotFoundError as e:
            raise e.grpc_error()
        status = await board.status()
        response = StatusResponse(status=status)
        await stream.send_message(response)

    async def SetGPIO(
        self,
        stream: Stream[SetGPIORequest, SetGPIOResponse]
    ) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        try:
            board = self.get_component(name)
        except ComponentNotFoundError as e:
            raise e.grpc_error()
        await board.set_gpio(request.pin, request.high)
        response = SetGPIOResponse()
        await stream.send_message(response)

    async def GetGPIO(
        self,
        stream: Stream[GetGPIORequest, GetGPIOResponse]
    ) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        try:
            board = self.get_component(name)
        except ComponentNotFoundError as e:
            raise e.grpc_error()
        high = await board.get_gpio(request.pin)
        response = GetGPIOResponse(high=high)
        await stream.send_message(response)

    async def SetPWM(
        self,
        stream: Stream[SetPWMRequest, SetPWMResponse]
    ) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        try:
            board = self.get_component(name)
        except ComponentNotFoundError as e:
            raise e.grpc_error()
        await board.set_pwm(request.pin, request.duty_cycle_pct)
        response = SetPWMResponse()
        await stream.send_message(response)

    async def SetPWMFrequency(
        self,
        stream: Stream[SetPWMFrequencyRequest, SetPWMFrequencyResponse]
    ) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        try:
            board = self.get_component(name)
        except ComponentNotFoundError as e:
            raise e.grpc_error()
        await board.set_pwm_freq(request.pin, request.frequency_hz)
        response = SetPWMFrequencyResponse()
        await stream.send_message(response)

    async def ReadAnalogReader(
        self,
        stream: Stream[ReadAnalogReaderRequest, ReadAnalogReaderResponse]
    ) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.board_name
        try:
            board = self.get_component(name)
        except ComponentNotFoundError as e:
            raise e.grpc_error()
        analog_reader = await board.analog_reader_by_name(
            request.analog_reader_name)
        value = await analog_reader.read()
        response = ReadAnalogReaderResponse(value=value)
        await stream.send_message(response)

    async def GetDigitalInterruptValue(
        self,
        stream: Stream[GetDigitalInterruptValueRequest,
                       GetDigitalInterruptValueResponse]
    ) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.board_name
        try:
            board = self.get_component(name)
        except ComponentNotFoundError as e:
            raise e.grpc_error()
        interrupt = await board.digital_interrupt_by_name(
            request.digital_interrupt_name)
        value = await interrupt.value()
        response = GetDigitalInterruptValueResponse(value=value)
        await stream.send_message(response)
