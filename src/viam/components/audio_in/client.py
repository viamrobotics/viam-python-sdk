import uuid
from typing import Any, Dict, List, Mapping, Optional

from grpclib.client import Channel
from grpclib.client import Stream as ClientStream

from viam.proto.common import DoCommandRequest, DoCommandResponse, Geometry, GetPropertiesRequest
from viam.proto.component.audioin import AudioInServiceStub, GetAudioRequest, GetAudioResponse
from viam.resource.rpc_client_base import ReconfigurableResourceRPCClientBase
from viam.streams import StreamWithIterator
from viam.utils import ValueTypes, dict_to_struct, get_geometries, struct_to_dict

from .audio_in import AudioIn


class AudioInClient(AudioIn, ReconfigurableResourceRPCClientBase):
    def __init__(self, name: str, channel: Channel) -> None:
        self.channel = channel
        self.client = AudioInServiceStub(channel)
        super().__init__(name)

    async def get_audio(
        self,
        codec: str,
        duration_seconds: float,
        previous_timestamp_ns: int,
        *,
        extra: Optional[Dict[str, Any]] = None,
        **kwargs,
    ):
        request = GetAudioRequest(
            name=self.name,
            codec=codec,
            duration_seconds=duration_seconds,
            previous_timestamp_nanoseconds=previous_timestamp_ns,
            request_id=str(uuid.uuid4()),
            extra=dict_to_struct(extra),
        )

        async def read():
            md = kwargs.get("metadata", self.Metadata()).proto
            audio_stream: ClientStream[GetAudioRequest, GetAudioResponse]
            async with self.client.GetAudio.open(metadata=md) as audio_stream:
                try:
                    await audio_stream.send_message(request, end=True)
                    async for response in audio_stream:
                        yield response
                except Exception as e:
                    raise (e)

        return StreamWithIterator(read())

    async def get_properties(
        self,
        *,
        timeout: Optional[float] = None,
        **kwargs,
    ) -> AudioIn.Properties:
        md = kwargs.get("metadata", self.Metadata()).proto
        return await self.client.GetProperties(GetPropertiesRequest(name=self.name), timeout=timeout, metadata=md)

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
