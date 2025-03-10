from typing import Any, Mapping, Optional

from grpclib.client import Channel

from viam.gen.component.switch.v1.switch_pb2 import (
    GetNumberOfPositionsRequest,
    GetNumberOfPositionsResponse,
    GetPositionRequest,
    GetPositionResponse,
    SetPositionRequest,
)
from viam.proto.common import (
    DoCommandRequest,
    DoCommandResponse,
)
from viam.proto.component.switch import SwitchServiceStub
from viam.resource.rpc_client_base import ReconfigurableResourceRPCClientBase
from viam.utils import (
    ValueTypes,
    dict_to_struct,
    struct_to_dict,
)

from .switch import Switch


class SwitchClient(Switch, ReconfigurableResourceRPCClientBase):
    """
    gRPC client for Switch component
    """

    def __init__(self, name: str, channel: Channel):
        self.channel = channel
        self.client = SwitchServiceStub(channel)
        super().__init__(name)

    async def get_position(
        self,
        *,
        extra: Optional[Mapping[str, Any]] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ) -> int:
        md = kwargs.get("metadata", self.Metadata()).proto
        request = GetPositionRequest(name=self.name, extra=dict_to_struct(extra))
        response: GetPositionResponse = await self.client.GetPosition(request, timeout=timeout, metadata=md)
        return response.position

    async def set_position(
        self,
        position: int,
        *,
        extra: Optional[Mapping[str, Any]] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ) -> None:
        md = kwargs.get("metadata", self.Metadata()).proto
        request = SetPositionRequest(name=self.name, position=position, extra=dict_to_struct(extra))
        await self.client.SetPosition(request, timeout=timeout, metadata=md)

    async def get_number_of_positions(
        self,
        *,
        extra: Optional[Mapping[str, Any]] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ) -> int:
        md = kwargs.get("metadata", self.Metadata()).proto
        request = GetNumberOfPositionsRequest(name=self.name, extra=dict_to_struct(extra))
        response: GetNumberOfPositionsResponse = await self.client.GetNumberOfPositions(request, timeout=timeout, metadata=md)
        return response.number_of_positions

    async def do_command(
        self,
        command: Mapping[str, ValueTypes],
        *,
        timeout: Optional[float] = None,
        **kwargs,
    ) -> Mapping[str, ValueTypes]:
        md = kwargs.get("metadata", self.Metadata()).proto
        request = DoCommandRequest(name=self.name, command=dict_to_struct(command))
        response: DoCommandResponse = await self.client.DoCommand(request, timeout=timeout, metadata=md)
        return struct_to_dict(response.result)
