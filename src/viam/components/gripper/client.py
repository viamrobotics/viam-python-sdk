from typing import Any, Dict, Optional

from grpclib.client import Channel

from viam.components.generic.client import do_command
from viam.proto.component.gripper import (
    GrabRequest,
    GrabResponse,
    GripperServiceStub,
    OpenRequest,
    StopRequest,
)
from viam.utils import dict_to_struct

from .gripper import Gripper


class GripperClient(Gripper):
    """
    gRPC client for the Gripper component
    """

    def __init__(self, name: str, channel: Channel):
        self.channel = channel
        self.client = GripperServiceStub(channel)
        super().__init__(name)

    async def open(self, *, timeout: Optional[float] = None, extra: Optional[Dict[str, Any]] = None):
        request = OpenRequest(name=self.name, extra=dict_to_struct(extra))
        await self.client.Open(request, timeout=timeout)

    async def grab(self, *, timeout: Optional[float] = None, extra: Optional[Dict[str, Any]] = None) -> bool:
        request = GrabRequest(name=self.name, extra=dict_to_struct(extra))
        response: GrabResponse = await self.client.Grab(request, timeout=timeout)
        return response.success

    async def stop(self, *, timeout: Optional[float] = None, extra: Optional[Dict[str, Any]] = None):
        request = StopRequest(name=self.name, extra=dict_to_struct(extra))
        await self.client.Stop(request, timeout=timeout)

    async def do_command(self, command: Dict[str, Any], *, timeout: Optional[float] = None) -> Dict[str, Any]:
        return await do_command(self.channel, self.name, command, timeout=timeout)
