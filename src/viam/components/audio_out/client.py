from typing import Any, Dict, List, Mapping, Optional

from grpclib.client import Channel

from viam.proto.common import DoCommandRequest, DoCommandResponse, Geometry, GetPropertiesRequest, GetPropertiesResponse
from viam.proto.component.audioout import AudioOutServiceStub, PlayRequest
from viam.resource.rpc_client_base import ReconfigurableResourceRPCClientBase
from viam.utils import ValueTypes, dict_to_struct, get_geometries, struct_to_dict

from .audio_out import AudioInfo, AudioOut


class AudioOutClient(AudioOut, ReconfigurableResourceRPCClientBase):
    """gRPC client for AudioOut component."""

    def __init__(self, name: str, channel: Channel) -> None:
        self.channel = channel
        self.client = AudioOutServiceStub(channel)
        super().__init__(name)

    async def play(
        self,
        data: bytes,
        info: Optional[AudioInfo] = None,
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ) -> None:
        if extra is None:
            extra = {}

        md = kwargs.get("metadata", self.Metadata()).proto
        request = PlayRequest(
            name=self.name,
            audio_data=data,
            audio_info=info,
            extra=dict_to_struct(extra),
        )
        await self.client.Play(request, timeout=timeout, metadata=md)

    async def get_properties(
        self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs
    ) -> AudioOut.Properties:
        if extra is None:
            extra = {}

        md = kwargs.get("metadata", self.Metadata()).proto
        request = GetPropertiesRequest(name=self.name, extra=dict_to_struct(extra))
        response: GetPropertiesResponse = await self.client.GetProperties(request, timeout=timeout, metadata=md)
        return response

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

    async def get_geometries(self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs) -> List[Geometry]:
        md = kwargs.get("metadata", self.Metadata())
        return await get_geometries(self.client, self.name, extra, timeout, md)
