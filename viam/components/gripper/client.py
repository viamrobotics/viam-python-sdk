from grpclib.client import Channel
from viam.proto.api.component.gripper import (GrabRequest, GrabResponse,
                                              GripperServiceStub, OpenRequest)

from .gripper import Gripper


class GripperClient(Gripper):
    """
    gRPC client for the Gripper component
    """

    def __init__(self, name: str, channel: Channel):
        self.client = GripperServiceStub(channel)
        super().__init__(name)

    async def open(self):
        request = OpenRequest(name=self.name)
        await self.client.Open(request)

    async def grab(self) -> bool:
        request = GrabRequest(name=self.name)
        response: GrabResponse = await self.client.Grab(request)
        return response.success
