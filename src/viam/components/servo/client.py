from typing import Any, Dict, Mapping, Optional

from grpclib.client import Channel

from viam.components.generic.client import do_command
from viam.proto.component.servo import (
    GetPositionRequest,
    GetPositionResponse,
    MoveRequest,
    ServoServiceStub,
    StopRequest,
)
from viam.utils import dict_to_struct

from .servo import Servo


class ServoClient(Servo):
    """
    gRPC client for the Servo component.
    """

    def __init__(self, name: str, channel: Channel):
        self.channel = channel
        self.client = ServoServiceStub(channel)
        super().__init__(name)

    async def get_position(self, *, extra: Optional[Mapping[str, Any]] = None, timeout: Optional[float] = None) -> int:
        if extra is None:
            extra = {}
        request = GetPositionRequest(name=self.name, extra=dict_to_struct(extra))
        response: GetPositionResponse = await self.client.GetPosition(request, timeout=timeout)
        return response.position_deg

    async def move(self, angle: int, *, extra: Optional[Mapping[str, Any]] = None, timeout: Optional[float] = None):
        if extra is None:
            extra = {}
        request = MoveRequest(name=self.name, angle_deg=angle, extra=dict_to_struct(extra))
        await self.client.Move(request, timeout=timeout)

    async def stop(self, *, extra: Optional[Mapping[str, Any]] = None, timeout: Optional[float] = None):
        if extra is None:
            extra = {}
        request = StopRequest(name=self.name, extra=dict_to_struct(extra))
        await self.client.Stop(request, timeout=timeout)

    async def do_command(self, command: Dict[str, Any], *, timeout: Optional[float] = None) -> Dict[str, Any]:
        return await do_command(self.channel, self.name, command, timeout=timeout)
