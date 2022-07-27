from typing import Any, Dict, List, Optional

from google.protobuf.struct_pb2 import Struct
from grpclib.client import Channel
from viam.components.generic.client import do_command
from viam.proto.api.common import WorldState
from viam.proto.api.component.gantry import (GantryServiceStub,
                                             GetLengthsRequest,
                                             GetLengthsResponse,
                                             GetPositionRequest,
                                             GetPositionResponse,
                                             MoveToPositionRequest,
                                             StopRequest)

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
        struct = None
        if extra:
            struct = Struct()
            struct.update(extra)
        request = GetPositionRequest(name=self.name, extra=struct)
        response: GetPositionResponse = await self.client.GetPosition(request)
        return list(response.positions_mm)

    async def move_to_position(
        self,
        positions: List[float],
        world_state: Optional[WorldState] = None,
        extra: Optional[Dict[str, Any]] = None,
    ):
        struct = None
        if extra:
            struct = Struct()
            struct.update(extra)
        request = MoveToPositionRequest(name=self.name, positions_mm=positions, world_state=world_state, extra=struct)
        await self.client.MoveToPosition(request)

    async def get_lengths(self, extra: Optional[Dict[str, Any]] = None) -> List[float]:
        struct = None
        if extra:
            struct = Struct()
            struct.update(extra)
        request = GetLengthsRequest(name=self.name, extra=struct)
        response: GetLengthsResponse = await self.client.GetLengths(request)
        return list(response.lengths_mm)

    async def stop(self, extra: Optional[Dict[str, Any]] = None):
        struct = None
        if extra:
            struct = Struct()
            struct.update(extra)
        request = StopRequest(name=self.name, extra=struct)
        await self.client.Stop(request)

    async def do(self, command: Dict[str, Any]) -> Dict[str, Any]:
        return await do_command(self.channel, self.name, command)
