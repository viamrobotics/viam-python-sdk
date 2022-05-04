from typing import Any, Dict, List, Optional

from grpclib.client import Channel
from viam.components.generic.client import do_command
from viam.proto.api.common import WorldState
from viam.proto.api.component.gantry import (GantryServiceStub,
                                             GetLengthsRequest,
                                             GetLengthsResponse,
                                             GetPositionRequest,
                                             GetPositionResponse,
                                             MoveToPositionRequest)

from .gantry import Gantry


class GantryClient(Gantry):
    """
    gRPC client for the Gantry component.
    """

    def __init__(self, name: str, channel: Channel):
        self.channel = channel
        self.client = GantryServiceStub(channel)
        super().__init__(name)

    async def get_position(self) -> List[float]:
        request = GetPositionRequest(name=self.name)
        response: GetPositionResponse = await self.client.GetPosition(request)
        return list(response.positions_mm)

    async def move_to_position(
        self,
        positions: List[float],
        world_state: Optional[WorldState] = None
    ):
        request = MoveToPositionRequest(
            name=self.name, positions_mm=positions, world_state=world_state)
        await self.client.MoveToPosition(request)

    async def get_lengths(self) -> List[float]:
        request = GetLengthsRequest(name=self.name)
        response: GetLengthsResponse = await self.client.GetLengths(request)
        return list(response.lengths_mm)

    async def do(self, command: Dict[str, Any]) -> Dict[str, Any]:
        return await do_command(self.channel, self.name, command)
