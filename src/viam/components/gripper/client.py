from typing import Any, Dict

from grpclib.client import Channel
from viam.components.generic.client import do_command
from viam.proto.component.gripper import GrabRequest, GrabResponse, GripperServiceStub, OpenRequest, StopRequest

from .gripper import Gripper


class GripperClient(Gripper):
    """
    gRPC client for the Gripper component
    """

    def __init__(self, name: str, channel: Channel):
        self.channel = channel
        self.client = GripperServiceStub(channel)
        super().__init__(name)

    async def open(self):
        request = OpenRequest(name=self.name)
        await self.client.Open(request)

    async def grab(self) -> bool:
        request = GrabRequest(name=self.name)
        response: GrabResponse = await self.client.Grab(request)
        return response.success

    async def stop(self):
        request = StopRequest(name=self.name)
        await self.client.Stop(request)

    async def do_command(self, command: Dict[str, Any]) -> Dict[str, Any]:
        return await do_command(self.channel, self.name, command)
