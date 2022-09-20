from typing import Any, Dict

from grpclib.client import Channel
from viam.components.generic.client import do_command
from viam.proto.component.servo import GetPositionRequest, GetPositionResponse, MoveRequest, ServoServiceStub, StopRequest

from .servo import Servo


class ServoClient(Servo):
    """
    gRPC client for the Servo component.
    """

    def __init__(self, name: str, channel: Channel):
        self.channel = channel
        self.client = ServoServiceStub(channel)
        super().__init__(name)

    async def get_position(self) -> int:
        request = GetPositionRequest(name=self.name)
        response: GetPositionResponse = await self.client.GetPosition(request)
        return response.position_deg

    async def move(self, angle: int):
        request = MoveRequest(name=self.name, angle_deg=angle)
        await self.client.Move(request)

    async def stop(self):
        request = StopRequest(name=self.name)
        await self.client.Stop(request)

    async def do_command(self, command: Dict[str, Any]) -> Dict[str, Any]:
        return await do_command(self.channel, self.name, command)
