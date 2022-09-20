from grpclib.server import Stream
from viam.components.service_base import ComponentServiceBase
from viam.errors import ComponentNotFoundError
from viam.proto.component.base import (
    BaseServiceBase,
    MoveStraightRequest,
    MoveStraightResponse,
    SetPowerRequest,
    SetPowerResponse,
    SetVelocityRequest,
    SetVelocityResponse,
    SpinRequest,
    SpinResponse,
    StopRequest,
    StopResponse,
)
from viam.utils import struct_to_dict

from .base import Base


class BaseService(BaseServiceBase, ComponentServiceBase[Base]):
    """
    gRPC service for a robotic Base
    """

    RESOURCE_TYPE = Base

    async def MoveStraight(self, stream: Stream[MoveStraightRequest, MoveStraightResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        try:
            base = self.get_component(name)
        except ComponentNotFoundError as e:
            raise e.grpc_error
        await base.move_straight(distance=request.distance_mm, velocity=request.mm_per_sec, extra=struct_to_dict(request.extra))
        response = MoveStraightResponse()
        await stream.send_message(response)

    async def Spin(self, stream: Stream[SpinRequest, SpinResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        try:
            base = self.get_component(name)
        except ComponentNotFoundError as e:
            raise e.grpc_error
        await base.spin(angle=request.angle_deg, velocity=request.degs_per_sec, extra=struct_to_dict(request.extra))
        response = SpinResponse()
        await stream.send_message(response)

    async def SetPower(self, stream: Stream[SetPowerRequest, SetPowerResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        try:
            base = self.get_component(name)
        except ComponentNotFoundError as e:
            raise e.grpc_error
        await base.set_power(request.linear, request.angular, struct_to_dict(request.extra))
        response = SetPowerResponse()
        await stream.send_message(response)

    async def SetVelocity(self, stream: Stream[SetVelocityRequest, SetVelocityResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        try:
            base = self.get_component(name)
        except ComponentNotFoundError as e:
            raise e.grpc_error
        await base.set_velocity(request.linear, request.angular, struct_to_dict(request.extra))
        await stream.send_message(SetVelocityResponse())

    async def Stop(self, stream: Stream[StopRequest, StopResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        try:
            base = self.get_component(name)
        except ComponentNotFoundError as e:
            raise e.grpc_error
        await base.stop(extra=struct_to_dict(request.extra))
        response = StopResponse()
        await stream.send_message(response)
