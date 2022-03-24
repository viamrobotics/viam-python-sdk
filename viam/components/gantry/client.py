from typing import List

from grpclib.client import Channel
from viam.proto.api.common import GeometriesInFrame, WorldState
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
        self.client = GantryServiceStub(channel)
        super().__init__(name)

    async def get_position(self) -> List[float]:
        request = GetPositionRequest(name=self.name)
        response: GetPositionResponse = await self.client.GetPosition(request)
        return list(response.positions_mm)

    async def move_to_position(
        self,
        positions: List[float],
        obstacles: List[GeometriesInFrame]
    ):
        world_state = WorldState(obstacles=obstacles)
        request = MoveToPositionRequest(
            name=self.name, positions_mm=positions, world_state=world_state)
        await self.client.MoveToPosition(request)

    async def get_lengths(self) -> List[float]:
        request = GetLengthsRequest(name=self.name)
        response: GetLengthsResponse = await self.client.GetLengths(request)
        return list(response.lengths_mm)
