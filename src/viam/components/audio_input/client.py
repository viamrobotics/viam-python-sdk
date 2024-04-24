from typing import Any, AsyncIterator, Dict, List, Mapping, Optional, Union

from grpclib.client import Channel

from viam.media.audio import Audio
from viam.proto.common import DoCommandRequest, DoCommandResponse, Geometry
from viam.proto.component.audioinput import (
    AudioInputServiceStub,
    ChunksRequest,
    ChunksResponse,
    PropertiesRequest,
    PropertiesResponse,
    SampleFormat,
)
from viam.resource.rpc_client_base import ReconfigurableResourceRPCClientBase
from viam.streams import Stream, StreamWithIterator
from viam.utils import ValueTypes, dict_to_struct, get_geometries, struct_to_dict

from .audio_input import AudioInput


class AudioInputClient(AudioInput, ReconfigurableResourceRPCClientBase):
    """
    gRPC client for the AudioInput component.
    """

    def __init__(self, name: str, channel: Channel):
        self.channel = channel
        self.client = AudioInputServiceStub(channel)
        super().__init__(name)

    async def stream(self, *, timeout: Optional[float] = None, **__) -> Stream[Audio]:
        async def read() -> AsyncIterator[Audio]:
            async with self.client.Chunks.open(timeout=timeout) as chunks_stream:
                await chunks_stream.send_message(
                    ChunksRequest(name=self.name, sample_format=SampleFormat.SAMPLE_FORMAT_FLOAT32_INTERLEAVED), end=True
                )
                response: Union[ChunksResponse, None] = await chunks_stream.recv_message()
                if not response:
                    await chunks_stream.recv_trailing_metadata()  # causes us to throw appropriate gRPC error.
                    raise TypeError("Response cannot be empty")  # we should never get here, but for typechecking
                assert response.HasField("info")
                info = response.info

                while True:
                    response = await chunks_stream.recv_message()
                    if response is None:
                        break
                    assert response.HasField("chunk")
                    audio = Audio(info=info, chunk=response.chunk)
                    yield audio

        return StreamWithIterator(read())

    async def get_properties(self, *, timeout: Optional[float] = None, **__) -> AudioInput.Properties:
        request = PropertiesRequest(name=self.name)
        response: PropertiesResponse = await self.client.Properties(request, timeout=timeout)
        return AudioInput.Properties.from_proto(response)

    async def do_command(self, command: Mapping[str, ValueTypes], *, timeout: Optional[float] = None, **__) -> Mapping[str, ValueTypes]:
        request = DoCommandRequest(name=self.name, command=dict_to_struct(command))
        response: DoCommandResponse = await self.client.DoCommand(request, timeout=timeout)
        return struct_to_dict(response.result)

    async def get_geometries(self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None) -> List[Geometry]:
        return await get_geometries(self.client, self.name, extra, timeout)
