from grpclib.server import Stream

from viam.errors import ResourceNotFoundError
from viam.proto.common import DoCommandRequest, DoCommandResponse
from viam.proto.component.base import (
    BaseServiceBase,
    IsMovingRequest,
    IsMovingResponse,
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
from viam.resource.rpc_service_base import ResourceRPCServiceBase
from viam.utils import dict_to_struct, struct_to_dict

from .base import Base


class BaseRPCService(BaseServiceBase, ResourceRPCServiceBase[Base]):
    """
    gRPC service for a robotic Base
    """

    RESOURCE_TYPE = Base

    async def MoveStraight(self, stream: Stream[MoveStraightRequest, MoveStraightResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        try:
            base = self.get_resource(name)
        except ResourceNotFoundError as e:
            raise e.grpc_error
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        await base.move_straight(
            distance=request.distance_mm,
            velocity=request.mm_per_sec,
            extra=struct_to_dict(request.extra),
            timeout=timeout,
            metadata=stream.metadata,
        )
        response = MoveStraightResponse()
        await stream.send_message(response)

    async def Spin(self, stream: Stream[SpinRequest, SpinResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        try:
            base = self.get_resource(name)
        except ResourceNotFoundError as e:
            raise e.grpc_error
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        await base.spin(
            angle=request.angle_deg,
            velocity=request.degs_per_sec,
            extra=struct_to_dict(request.extra),
            timeout=timeout,
            metadata=stream.metadata,
        )
        response = SpinResponse()
        await stream.send_message(response)

    async def SetPower(self, stream: Stream[SetPowerRequest, SetPowerResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        try:
            base = self.get_resource(name)
        except ResourceNotFoundError as e:
            raise e.grpc_error
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        await base.set_power(
            request.linear, request.angular, extra=struct_to_dict(request.extra), timeout=timeout, metadata=stream.metadata
        )
        response = SetPowerResponse()
        await stream.send_message(response)

    async def SetVelocity(self, stream: Stream[SetVelocityRequest, SetVelocityResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        try:
            base = self.get_resource(name)
        except ResourceNotFoundError as e:
            raise e.grpc_error
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        await base.set_velocity(
            request.linear, request.angular, extra=struct_to_dict(request.extra), timeout=timeout, metadata=stream.metadata
        )
        await stream.send_message(SetVelocityResponse())

    async def Stop(self, stream: Stream[StopRequest, StopResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        try:
            base = self.get_resource(name)
        except ResourceNotFoundError as e:
            raise e.grpc_error
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        await base.stop(extra=struct_to_dict(request.extra), timeout=timeout, metadata=stream.metadata)
        response = StopResponse()
        await stream.send_message(response)

    async def IsMoving(self, stream: Stream[IsMovingRequest, IsMovingResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        try:
            base = self.get_resource(name)
        except ResourceNotFoundError as e:
            raise e.grpc_error
        is_moving = await base.is_moving()
        response = IsMovingResponse(is_moving=is_moving)
        await stream.send_message(response)

    async def DoCommand(self, stream: Stream[DoCommandRequest, DoCommandResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        try:
            base = self.get_resource(request.name)
        except ResourceNotFoundError as e:
            raise e.grpc_error
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        result = await base.do_command(command=struct_to_dict(request.command), timeout=timeout, metadata=stream.metadata)
        response = DoCommandResponse(result=dict_to_struct(result))
        await stream.send_message(response)
