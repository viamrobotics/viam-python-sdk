from grpclib.server import Stream

from viam.proto.common import DoCommandRequest, DoCommandResponse, GetGeometriesRequest, GetGeometriesResponse
from viam.proto.component.servo import (
    GetPositionRequest,
    GetPositionResponse,
    IsMovingRequest,
    IsMovingResponse,
    MoveRequest,
    MoveResponse,
    ServoServiceBase,
    StopRequest,
    StopResponse,
)
from viam.resource.rpc_service_base import ResourceRPCServiceBase
from viam.utils import dict_to_struct, struct_to_dict

from .servo import Servo


class ServoRPCService(ServoServiceBase, ResourceRPCServiceBase[Servo]):
    """
    gRPC Service for a Servo
    """

    RESOURCE_TYPE = Servo

    async def Move(self, stream: Stream[MoveRequest, MoveResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        servo = self.get_resource(name)
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        await servo.move(request.angle_deg, extra=struct_to_dict(request.extra), timeout=timeout, metadata=stream.metadata)
        await stream.send_message(MoveResponse())

    async def GetPosition(self, stream: Stream[GetPositionRequest, GetPositionResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        servo = self.get_resource(name)
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        position = await servo.get_position(extra=struct_to_dict(request.extra), timeout=timeout, metadata=stream.metadata)
        resp = GetPositionResponse(position_deg=position)
        await stream.send_message(resp)

    async def Stop(self, stream: Stream[StopRequest, StopResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        servo = self.get_resource(name)
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        await servo.stop(extra=struct_to_dict(request.extra), timeout=timeout, metadata=stream.metadata)
        await stream.send_message(StopResponse())

    async def IsMoving(self, stream: Stream[IsMovingRequest, IsMovingResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        servo = self.get_resource(name)
        is_moving = await servo.is_moving()
        await stream.send_message(IsMovingResponse(is_moving=is_moving))

    async def DoCommand(self, stream: Stream[DoCommandRequest, DoCommandResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        servo = self.get_resource(request.name)
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        result = await servo.do_command(command=struct_to_dict(request.command), timeout=timeout, metadata=stream.metadata)
        response = DoCommandResponse(result=dict_to_struct(result))
        await stream.send_message(response)

    async def GetGeometries(self, stream: Stream[GetGeometriesRequest, GetGeometriesResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        servo = self.get_resource(request.name)
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        geometries = await servo.get_geometries(extra=struct_to_dict(request.extra), timeout=timeout)
        response = GetGeometriesResponse(geometries=geometries)
        await stream.send_message(response)
