from typing import Any, Dict, List, Mapping, Optional, Tuple

from grpclib.client import Channel

from viam.proto.common import DoCommandRequest, DoCommandResponse, Geometry
from viam.proto.component.encoder import (
    EncoderServiceStub,
    GetPositionRequest,
    GetPositionResponse,
    GetPropertiesRequest,
    GetPropertiesResponse,
    PositionType,
    ResetPositionRequest,
)
from viam.resource.rpc_client_base import ReconfigurableResourceRPCClientBase
from viam.utils import ValueTypes, dict_to_struct, get_geometries, struct_to_dict

from .encoder import Encoder


class EncoderClient(Encoder, ReconfigurableResourceRPCClientBase):
    """
    gRPC client for the Encoder component.
    """

    def __init__(self, name: str, channel: Channel):
        self.channel = channel
        self.client = EncoderServiceStub(channel)
        super().__init__(name)

    async def reset_position(
        self,
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
        **__,
    ):
        if extra is None:
            extra = {}
        request = ResetPositionRequest(name=self.name, extra=dict_to_struct(extra))
        await self.client.ResetPosition(request, timeout=timeout)

    async def get_position(
        self,
        position_type: Optional[PositionType.ValueType] = None,
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
        **__,
    ) -> Tuple[float, PositionType.ValueType]:
        if extra is None:
            extra = {}
        request = GetPositionRequest(name=self.name, position_type=position_type, extra=dict_to_struct(extra))
        response: GetPositionResponse = await self.client.GetPosition(request, timeout=timeout)
        return response.value, response.position_type

    async def get_properties(
        self,
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
        **__,
    ) -> Encoder.Properties:
        if extra is None:
            extra = {}
        request = GetPropertiesRequest(name=self.name, extra=dict_to_struct(extra))
        response: GetPropertiesResponse = await self.client.GetProperties(request, timeout=timeout)
        return Encoder.Properties(
            ticks_count_supported=response.ticks_count_supported, angle_degrees_supported=response.angle_degrees_supported
        )

    async def do_command(
        self,
        command: Mapping[str, ValueTypes],
        *,
        timeout: Optional[float] = None,
        **__,
    ) -> Mapping[str, ValueTypes]:
        request = DoCommandRequest(name=self.name, command=dict_to_struct(command))
        response: DoCommandResponse = await self.client.DoCommand(request, timeout=timeout)
        return struct_to_dict(response.result)

    async def get_geometries(self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None) -> List[Geometry]:
        return await get_geometries(self.client, self.name, extra, timeout)
