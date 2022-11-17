from grpclib.server import Stream

from viam.components.service_base import ComponentServiceBase
from viam.errors import ComponentNotFoundError
from viam.proto.component.servo import (
    GetPositionRequest,
    GetPositionResponse,
    MoveRequest,
    MoveResponse,
    ServoServiceBase,
    StopRequest,
    StopResponse,
)
from viam.utils import struct_to_dict

from .servo import Servo


class ServoService(ServoServiceBase, ComponentServiceBase[Servo]):
    """
    gRPC Service for a Servo
    """

    RESOURCE_TYPE = Servo

    async def Move(self, stream: Stream[MoveRequest, MoveResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        try:
            servo = self.get_component(name)
        except ComponentNotFoundError as e:
            raise e.grpc_error
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        await servo.move(request.angle_deg, extra=struct_to_dict(request.extra), timeout=timeout)
        await stream.send_message(MoveResponse())

    async def GetPosition(self, stream: Stream[GetPositionRequest, GetPositionResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        try:
            servo = self.get_component(name)
        except ComponentNotFoundError as e:
            raise e.grpc_error
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        position = await servo.get_position(extra=struct_to_dict(request.extra), timeout=timeout)
        resp = GetPositionResponse(position_deg=position)
        await stream.send_message(resp)

    async def Stop(self, stream: Stream[StopRequest, StopResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        try:
            servo = self.get_component(name)
        except ComponentNotFoundError as e:
            raise e.grpc_error
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        await servo.stop(extra=struct_to_dict(request.extra), timeout=timeout)
        await stream.send_message(StopResponse())
