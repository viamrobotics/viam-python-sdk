from grpclib.client import Channel
from viam.proto.api.component.servo import (GetPositionRequest,
                                            GetPositionResponse, MoveRequest,
                                            ServoServiceStub)

from .servo import ServoBase


class ServoClient(ServoBase):
    """
    gRPC client for the Servo component.
    """

    def __init__(self, name: str, channel: Channel):
        self.client = ServoServiceStub(channel)
        super().__init__(name)

    async def get_position(self) -> int:
        request = GetPositionRequest(name=self.name)
        response: GetPositionResponse = await self.client.GetPosition(request)
        return response.position_deg

    async def move(self, angle: int):
        request = MoveRequest(name=self.name, angle_deg=angle)
        await self.client.Move(request)
