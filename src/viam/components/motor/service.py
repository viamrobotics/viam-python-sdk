from grpclib.server import Stream
from viam.components.service_base import ComponentServiceBase
from viam.errors import ComponentNotFoundError
from viam.proto.component.motor import (
    GetPropertiesRequest,
    GetPropertiesResponse,
    GetPositionRequest,
    GetPositionResponse,
    GoForRequest,
    GoForResponse,
    GoToRequest,
    GoToResponse,
    IsPoweredRequest,
    IsPoweredResponse,
    MotorServiceBase,
    ResetZeroPositionRequest,
    ResetZeroPositionResponse,
    SetPowerRequest,
    SetPowerResponse,
    StopRequest,
    StopResponse,
)
from viam.utils import struct_to_dict

from .motor import Motor


class MotorService(MotorServiceBase, ComponentServiceBase[Motor]):
    """
    gRPC Service for a Motor
    """

    RESOURCE_TYPE = Motor

    async def SetPower(self, stream: Stream[SetPowerRequest, SetPowerResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        try:
            motor = self.get_component(name)
        except ComponentNotFoundError as e:
            raise e.grpc_error
        await motor.set_power(request.power_pct, struct_to_dict(request.extra))
        await stream.send_message(SetPowerResponse())

    async def GoFor(self, stream: Stream[GoForRequest, GoForResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        try:
            motor = self.get_component(name)
        except ComponentNotFoundError as e:
            raise e.grpc_error
        await motor.go_for(request.rpm, request.revolutions, struct_to_dict(request.extra))
        await stream.send_message(GoForResponse())

    async def GoTo(self, stream: Stream[GoToRequest, GoToResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        try:
            motor = self.get_component(name)
        except ComponentNotFoundError as e:
            raise e.grpc_error
        await motor.go_to(request.rpm, request.position_revolutions, struct_to_dict(request.extra))
        await stream.send_message(GoToResponse())

    async def ResetZeroPosition(self, stream: Stream[ResetZeroPositionRequest, ResetZeroPositionResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        try:
            motor = self.get_component(name)
        except ComponentNotFoundError as e:
            raise e.grpc_error
        await motor.reset_zero_position(request.offset, struct_to_dict(request.extra))
        await stream.send_message(ResetZeroPositionResponse())

    async def GetPosition(self, stream: Stream[GetPositionRequest, GetPositionResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        try:
            motor = self.get_component(name)
        except ComponentNotFoundError as e:
            raise e.grpc_error
        position = await motor.get_position(struct_to_dict(request.extra))
        await stream.send_message(GetPositionResponse(position=position))

    async def GetProperties(self, stream: Stream[GetPropertiesRequest, GetPropertiesResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        try:
            motor = self.get_component(name)
        except ComponentNotFoundError as e:
            raise e.grpc_error
        properties = await motor.get_properties(struct_to_dict(request.extra))
        response = GetPropertiesResponse(**properties.__dict__)
        await stream.send_message(response)

    async def Stop(self, stream: Stream[StopRequest, StopResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        try:
            motor = self.get_component(name)
        except ComponentNotFoundError as e:
            raise e.grpc_error
        await motor.stop(struct_to_dict(request.extra))
        response = StopResponse()
        await stream.send_message(response)

    async def IsPowered(self, stream: Stream[IsPoweredRequest, IsPoweredResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        try:
            motor = self.get_component(name)
        except ComponentNotFoundError as e:
            raise e.grpc_error
        is_powered = await motor.is_powered(struct_to_dict(request.extra))
        await stream.send_message(IsPoweredResponse(is_on=is_powered))
