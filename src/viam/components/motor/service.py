from grpclib.server import Stream

from viam.proto.common import DoCommandRequest, DoCommandResponse, GetGeometriesRequest, GetGeometriesResponse
from viam.proto.component.motor import (
    GetPositionRequest,
    GetPositionResponse,
    GetPropertiesRequest,
    GetPropertiesResponse,
    GoForRequest,
    GoForResponse,
    GoToRequest,
    GoToResponse,
    IsMovingRequest,
    IsMovingResponse,
    IsPoweredRequest,
    IsPoweredResponse,
    ResetZeroPositionRequest,
    ResetZeroPositionResponse,
    SetPowerRequest,
    SetPowerResponse,
    SetRPMRequest,
    SetRPMResponse,
    StopRequest,
    StopResponse,
    UnimplementedMotorServiceBase,
)
from viam.resource.rpc_service_base import ResourceRPCServiceBase
from viam.utils import dict_to_struct, struct_to_dict

from .motor import Motor


class MotorRPCService(UnimplementedMotorServiceBase, ResourceRPCServiceBase[Motor]):
    """
    gRPC Service for a Motor
    """

    RESOURCE_TYPE = Motor

    async def SetPower(self, stream: Stream[SetPowerRequest, SetPowerResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        motor = self.get_resource(name)
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        await motor.set_power(request.power_pct, extra=struct_to_dict(request.extra), timeout=timeout, metadata=stream.metadata)
        await stream.send_message(SetPowerResponse())

    async def GoFor(self, stream: Stream[GoForRequest, GoForResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        motor = self.get_resource(name)
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        await motor.go_for(request.rpm, request.revolutions, extra=struct_to_dict(request.extra), timeout=timeout, metadata=stream.metadata)
        await stream.send_message(GoForResponse())

    async def GoTo(self, stream: Stream[GoToRequest, GoToResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        motor = self.get_resource(name)
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        await motor.go_to(
            request.rpm, request.position_revolutions, extra=struct_to_dict(request.extra), timeout=timeout, metadata=stream.metadata
        )
        await stream.send_message(GoToResponse())

    async def SetRPM(self, stream: Stream[SetRPMRequest, SetRPMResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        motor = self.get_resource(name)
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        await motor.set_rpm(request.rpm, extra=struct_to_dict(request.extra), timeout=timeout, metadata=stream.metadata)
        await stream.send_message(SetRPMResponse())

    async def ResetZeroPosition(self, stream: Stream[ResetZeroPositionRequest, ResetZeroPositionResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        motor = self.get_resource(name)
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        await motor.reset_zero_position(request.offset, extra=struct_to_dict(request.extra), timeout=timeout, metadata=stream.metadata)
        await stream.send_message(ResetZeroPositionResponse())

    async def GetPosition(self, stream: Stream[GetPositionRequest, GetPositionResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        motor = self.get_resource(name)
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        position = await motor.get_position(extra=struct_to_dict(request.extra), timeout=timeout, metadata=stream.metadata)
        await stream.send_message(GetPositionResponse(position=position))

    async def GetProperties(self, stream: Stream[GetPropertiesRequest, GetPropertiesResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        motor = self.get_resource(name)
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        properties = await motor.get_properties(extra=struct_to_dict(request.extra), timeout=timeout, metadata=stream.metadata)
        response = GetPropertiesResponse(**properties.__dict__)
        await stream.send_message(response)

    async def Stop(self, stream: Stream[StopRequest, StopResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        motor = self.get_resource(name)
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        await motor.stop(extra=struct_to_dict(request.extra), timeout=timeout, metadata=stream.metadata)
        response = StopResponse()
        await stream.send_message(response)

    async def IsPowered(self, stream: Stream[IsPoweredRequest, IsPoweredResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        motor = self.get_resource(name)
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        is_powered, power_pct = await motor.is_powered(extra=struct_to_dict(request.extra), timeout=timeout, metadata=stream.metadata)
        await stream.send_message(IsPoweredResponse(is_on=is_powered, power_pct=power_pct))

    async def IsMoving(self, stream: Stream[IsMovingRequest, IsMovingResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        motor = self.get_resource(name)
        is_moving = await motor.is_moving()
        response = IsMovingResponse(is_moving=is_moving)
        await stream.send_message(response)

    async def DoCommand(self, stream: Stream[DoCommandRequest, DoCommandResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        motor = self.get_resource(request.name)
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        result = await motor.do_command(command=struct_to_dict(request.command), timeout=timeout, metadata=stream.metadata)
        response = DoCommandResponse(result=dict_to_struct(result))
        await stream.send_message(response)

    async def GetGeometries(self, stream: Stream[GetGeometriesRequest, GetGeometriesResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        motor = self.get_resource(request.name)
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        geometries = await motor.get_geometries(extra=struct_to_dict(request.extra), timeout=timeout)
        response = GetGeometriesResponse(geometries=geometries)
        await stream.send_message(response)
