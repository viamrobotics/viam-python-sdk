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
    IsMovingRequest,
    IsMovingResponse,
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
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        await motor.set_power(request.power_pct, extra=struct_to_dict(request.extra), timeout=timeout)
        await stream.send_message(SetPowerResponse())

    async def GoFor(self, stream: Stream[GoForRequest, GoForResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        try:
            motor = self.get_component(name)
        except ComponentNotFoundError as e:
            raise e.grpc_error
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        await motor.go_for(request.rpm, request.revolutions, extra=struct_to_dict(request.extra), timeout=timeout)
        await stream.send_message(GoForResponse())

    async def GoTo(self, stream: Stream[GoToRequest, GoToResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        try:
            motor = self.get_component(name)
        except ComponentNotFoundError as e:
            raise e.grpc_error
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        await motor.go_to(request.rpm, request.position_revolutions, extra=struct_to_dict(request.extra), timeout=timeout)
        await stream.send_message(GoToResponse())

    async def ResetZeroPosition(self, stream: Stream[ResetZeroPositionRequest, ResetZeroPositionResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        try:
            motor = self.get_component(name)
        except ComponentNotFoundError as e:
            raise e.grpc_error
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        await motor.reset_zero_position(request.offset, extra=struct_to_dict(request.extra), timeout=timeout)
        await stream.send_message(ResetZeroPositionResponse())

    async def GetPosition(self, stream: Stream[GetPositionRequest, GetPositionResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        try:
            motor = self.get_component(name)
        except ComponentNotFoundError as e:
            raise e.grpc_error
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        position = await motor.get_position(extra=struct_to_dict(request.extra), timeout=timeout)
        await stream.send_message(GetPositionResponse(position=position))

    async def GetProperties(self, stream: Stream[GetPropertiesRequest, GetPropertiesResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        try:
            motor = self.get_component(name)
        except ComponentNotFoundError as e:
            raise e.grpc_error
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        properties = await motor.get_properties(extra=struct_to_dict(request.extra), timeout=timeout)
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
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        await motor.stop(extra=struct_to_dict(request.extra), timeout=timeout)
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
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        is_powered, power_pct = await motor.is_powered(extra=struct_to_dict(request.extra), timeout=timeout)
        await stream.send_message(IsPoweredResponse(is_on=is_powered, power_pct=power_pct))

    async def IsMoving(self, stream: Stream[IsMovingRequest, IsMovingResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        try:
            motor = self.get_component(name)
        except ComponentNotFoundError as e:
            raise e.grpc_error
        await motor.is_moving()
        response = IsMovingResponse()
        await stream.send_message(response)
