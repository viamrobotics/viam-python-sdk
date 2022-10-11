import asyncio
from typing import Any, AsyncIterator, Dict, Union

from grpclib.client import Channel
import viam

from viam.components.generic.client import do_command
from viam.components.types import Audio
from viam.proto.component.audioinput import (
    AudioInputServiceStub,
    ChunksRequest,
    ChunksResponse,
    PropertiesRequest,
    PropertiesResponse,
    SampleFormat,
)

from .audio_input import AudioInput, MediaStream, MediaStreamWithPipe


class AudioInputClient(AudioInput):
    """
    gRPC client for the AudioInput component.
    """

    def __init__(self, name: str, channel: Channel):
        self.channel = channel
        self.client = AudioInputServiceStub(channel)
        super().__init__(name)

    async def stream(self) -> MediaStream[Audio]:
        media_stream = MediaStreamWithPipe()

        async def read():
            async with self.client.Chunks.open() as chunks_stream:
                await chunks_stream.send_message(
                    ChunksRequest(name=self.name, sample_format=SampleFormat.SAMPLE_FORMAT_FLOAT32_INTERLEAVED)
                )
                response: Union[ChunksResponse, None] = await chunks_stream.recv_message()
                assert response is not None and response.HasField("info")
                info = response.info

                while True:
                    response = await chunks_stream.recv_message()
                    if response is None:
                        await media_stream.close()
                        break
                    assert response.HasField("chunk")
                    audio = Audio(info=Audio.Info.from_proto(info), chunk=Audio.Chunk.from_proto(response.chunk))
                    media_stream.pipe.send(audio)

        asyncio.create_task(read(), name=f"{viam._TASK_PREFIX}-audio_input_write_stream")
        return media_stream

    async def properties(self) -> AudioInput.Properties:
        request = PropertiesRequest(name=self.name)
        response: PropertiesResponse = await self.client.Properties(request)
        return AudioInput.Properties.from_proto(response)

    async def do_command(self, command: Dict[str, Any]) -> Dict[str, Any]:
        return await do_command(self.channel, self.name, command)
