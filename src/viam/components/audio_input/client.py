from typing import Any, AsyncIterator, Dict, Optional, Union

from grpclib.client import Channel

from viam.components.generic.client import do_command
from viam.media import MediaStream, MediaStreamWithIterator
from viam.media.audio import Audio
from viam.proto.component.audioinput import (
    AudioInputServiceStub,
    ChunksRequest,
    ChunksResponse,
    PropertiesRequest,
    PropertiesResponse,
    SampleFormat,
)

from .audio_input import AudioInput


class AudioInputClient(AudioInput):
    """
    gRPC client for the AudioInput component.
    """

    def __init__(self, name: str, channel: Channel):
        self.channel = channel
        self.client = AudioInputServiceStub(channel)
        super().__init__(name)

    async def stream(self, *, timeout: Optional[float] = None) -> MediaStream[Audio]:
        async def read() -> AsyncIterator[Audio]:
            async with self.client.Chunks.open(timeout=timeout) as chunks_stream:
                await chunks_stream.send_message(
                    ChunksRequest(name=self.name, sample_format=SampleFormat.SAMPLE_FORMAT_FLOAT32_INTERLEAVED), end=True
                )
                response: Union[ChunksResponse, None] = await chunks_stream.recv_message()
                assert response is not None and response.HasField("info")
                info = response.info

                while True:
                    response = await chunks_stream.recv_message()
                    if response is None:
                        break
                    assert response.HasField("chunk")
                    audio = Audio(info=info, chunk=response.chunk)
                    yield audio

        return MediaStreamWithIterator(read())

    async def get_properties(self, *, timeout: Optional[float] = None) -> AudioInput.Properties:
        request = PropertiesRequest(name=self.name)
        response: PropertiesResponse = await self.client.Properties(request, timeout=timeout)
        return AudioInput.Properties.from_proto(response)

    async def do_command(self, command: Dict[str, Any], *, timeout: Optional[float] = None) -> Dict[str, Any]:
        return await do_command(self.channel, self.name, command, timeout=timeout)
