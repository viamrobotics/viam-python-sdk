from grpclib.server import Stream
from viam.components.service_base import ComponentServiceBase
from viam.errors import ComponentNotFoundError
from viam.proto.api.component.servo import (
    ServoServiceBase,
    MoveRequest, MoveResponse,
    GetPositionRequest, GetPositionResponse
)

from .servo import ServoBase


class ServoService(ServoServiceBase, ComponentServiceBase[ServoBase]):
    """
    gRPC Service for a Servo
    """

    RESOURCE_TYPE = ServoBase

    async def Move(
        self,
        stream: Stream[MoveRequest, MoveResponse]
    ) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        try:
            servo = self.get_component(name)
        except ComponentNotFoundError as e:
            raise e.grpc_error()
        await servo.move(request.angle_deg)
        await stream.send_message(MoveResponse())

    async def GetPosition(
        self,
        stream: Stream[GetPositionRequest, GetPositionResponse]
    ) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        try:
            servo = self.get_component(name)
        except ComponentNotFoundError as e:
            raise e.grpc_error()
        position = await servo.get_position()
        resp = GetPositionResponse(position_deg=position)
        await stream.send_message(resp)
