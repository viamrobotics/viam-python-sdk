from grpclib.server import Stream
from viam.components.service_base import ComponentServiceBase
from viam.errors import ComponentNotFoundError
from viam.proto.api.component.motor import (
    MotorServiceBase,
    SetPowerRequest, SetPowerResponse,
    GoForRequest, GoForResponse,
    GoToRequest, GoToResponse,
    ResetZeroPositionRequest, ResetZeroPositionResponse,
    GetPositionRequest, GetPositionResponse,
    GetFeaturesRequest, GetFeaturesResponse,
    StopRequest, StopResponse,
    IsPoweredRequest, IsPoweredResponse,
)

from .motor import Motor


class MotorService(MotorServiceBase, ComponentServiceBase[Motor]):
    """
    gRPC Service for a Motor
    """

    RESOURCE_TYPE = Motor

    async def SetPower(
        self,
        stream: Stream[SetPowerRequest, SetPowerResponse]
    ) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        try:
            motor = self.get_component(name)
        except ComponentNotFoundError as e:
            raise e.grpc_error()
        await motor.set_power(request.power_pct)
        await stream.send_message(SetPowerResponse())

    async def GoFor(
        self,
        stream: Stream[GoForRequest, GoForResponse]
    ) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        try:
            motor = self.get_component(name)
        except ComponentNotFoundError as e:
            raise e.grpc_error()
        await motor.go_for(request.rpm, request.revolutions)
        await stream.send_message(GoForResponse())

    async def GoTo(
        self,
        stream: Stream[GoToRequest, GoToResponse]
    ) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        try:
            motor = self.get_component(name)
        except ComponentNotFoundError as e:
            raise e.grpc_error()
        await motor.go_to(request.rpm, request.position_revolutions)
        await stream.send_message(GoToResponse())

    async def ResetZeroPosition(
        self,
        stream: Stream[ResetZeroPositionRequest, ResetZeroPositionResponse]
    ) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        try:
            motor = self.get_component(name)
        except ComponentNotFoundError as e:
            raise e.grpc_error()
        await motor.reset_zero_position(request.offset)
        await stream.send_message(ResetZeroPositionResponse())

    async def GetPosition(
        self,
        stream: Stream[GetPositionRequest, GetPositionResponse]
    ) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        try:
            motor = self.get_component(name)
        except ComponentNotFoundError as e:
            raise e.grpc_error()
        position = await motor.get_position()
        await stream.send_message(GetPositionResponse(position=position))

    async def GetFeatures(
        self,
        stream: Stream[GetFeaturesRequest, GetFeaturesResponse]
    ) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        try:
            motor = self.get_component(name)
        except ComponentNotFoundError as e:
            raise e.grpc_error()
        features = await motor.get_features()
        response = GetFeaturesResponse(**features)
        await stream.send_message(response)

    async def Stop(
        self,
        stream: Stream[StopRequest, StopResponse]
    ) -> None:
        pass

    async def IsPowered(
        self,
        stream: Stream[IsPoweredRequest, IsPoweredResponse]
    ) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        try:
            motor = self.get_component(name)
        except ComponentNotFoundError as e:
            raise e.grpc_error()
        is_powered = await motor.is_powered()
        await stream.send_message(IsPoweredResponse(is_on=is_powered))
