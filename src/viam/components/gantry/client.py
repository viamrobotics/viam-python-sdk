from typing import Any, Dict, List, Mapping, Optional

from grpclib.client import Channel

from viam.proto.common import DoCommandRequest, DoCommandResponse, WorldState
from viam.proto.component.gantry import (
    GantryServiceStub,
    GetLengthsRequest,
    GetLengthsResponse,
    GetPositionRequest,
    GetPositionResponse,
    IsMovingRequest,
    IsMovingResponse,
    MoveToPositionRequest,
    StopRequest,
)
from viam.resource.rpc_client_base import ReconfigurableResourceRPCClientBase
from viam.utils import ValueTypes, dict_to_struct, struct_to_dict

from .gantry import Gantry


class GantryClient(Gantry, ReconfigurableResourceRPCClientBase):
    """
    gRPC client for the Gantry component.
    """

    def __init__(self, name: str, channel: Channel):
        self.channel = channel
        self.client = GantryServiceStub(channel)
        super().__init__(name)

    async def get_position(self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None) -> List[float]:
        if extra is None:
            extra = {}
        request = GetPositionRequest(name=self.name, extra=dict_to_struct(extra))
        response: GetPositionResponse = await self.client.GetPosition(request, timeout=timeout)
        return list(response.positions_mm)

    async def move_to_position(
        self,
        positions: List[float],
        world_state: Optional[WorldState] = None,
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
    ):
        if extra is None:
            extra = {}
        request = MoveToPositionRequest(name=self.name, positions_mm=positions, extra=dict_to_struct(extra))
        await self.client.MoveToPosition(request, timeout=timeout)

    async def get_lengths(self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None) -> List[float]:
        if extra is None:
            extra = {}
        request = GetLengthsRequest(name=self.name, extra=dict_to_struct(extra))
        response: GetLengthsResponse = await self.client.GetLengths(request, timeout=timeout)
        return list(response.lengths_mm)

    async def stop(self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None):
        if extra is None:
            extra = {}
        request = StopRequest(name=self.name, extra=dict_to_struct(extra))
        await self.client.Stop(request, timeout=timeout)

    async def is_moving(self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None) -> bool:
        if extra is None:
            extra = {}
        request = IsMovingRequest(name=self.name)
        response: IsMovingResponse = await self.client.IsMoving(request, timeout=timeout)
        return response.is_moving

    async def do_command(self, command: Mapping[str, ValueTypes], *, timeout: Optional[float] = None) -> Mapping[str, ValueTypes]:
        request = DoCommandRequest(name=self.name, command=dict_to_struct(command))
        response: DoCommandResponse = await self.client.DoCommand(request, timeout=timeout)
        return struct_to_dict(response.result)
