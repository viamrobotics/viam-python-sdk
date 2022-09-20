from typing import Any, Dict, List, Optional

from grpclib.client import Channel
from viam.components.generic.client import do_command
from viam.proto.common import WorldState
from viam.proto.component.gantry import (
    GantryServiceStub,
    GetLengthsRequest,
    GetLengthsResponse,
    GetPositionRequest,
    GetPositionResponse,
    MoveToPositionRequest,
    StopRequest,
)
from viam.utils import dict_to_struct

from .gantry import Gantry


class GantryClient(Gantry):
    """
    gRPC client for the Gantry component.
    """

    def __init__(self, name: str, channel: Channel):
        self.channel = channel
        self.client = GantryServiceStub(channel)
        super().__init__(name)

    async def get_position(self, extra: Optional[Dict[str, Any]] = None) -> List[float]:
        if extra is None:
            extra = {}
        request = GetPositionRequest(name=self.name, extra=dict_to_struct(extra))
        response: GetPositionResponse = await self.client.GetPosition(request)
        return list(response.positions_mm)

    async def move_to_position(
        self,
        positions: List[float],
        world_state: Optional[WorldState] = None,
        extra: Optional[Dict[str, Any]] = None,
    ):
        if extra is None:
            extra = {}
        request = MoveToPositionRequest(name=self.name, positions_mm=positions, world_state=world_state, extra=dict_to_struct(extra))
        await self.client.MoveToPosition(request)

    async def get_lengths(self, extra: Optional[Dict[str, Any]] = None) -> List[float]:
        if extra is None:
            extra = {}
        request = GetLengthsRequest(name=self.name, extra=dict_to_struct(extra))
        response: GetLengthsResponse = await self.client.GetLengths(request)
        return list(response.lengths_mm)

    async def stop(self, extra: Optional[Dict[str, Any]] = None):
        if extra is None:
            extra = {}
        request = StopRequest(name=self.name, extra=dict_to_struct(extra))
        await self.client.Stop(request)

    async def do_command(self, command: Dict[str, Any]) -> Dict[str, Any]:
        return await do_command(self.channel, self.name, command)
