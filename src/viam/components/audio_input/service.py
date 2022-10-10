from google.api.httpbody_pb2 import HttpBody
from grpclib.server import Stream

from viam.components.service_base import ComponentServiceBase
from viam.errors import ComponentNotFoundError
from viam.proto.component.audioinput import (
    AudioInputServiceBase,
    ChunksRequest,
    ChunksResponse,
    PropertiesRequest,
    PropertiesResponse,
    RecordRequest,
)

from .audio_input import AudioInput


class AudioInputService(AudioInputServiceBase, ComponentServiceBase[AudioInput]):
    """
    gRPC Service for a generic AudioInput
    """

    RESOURCE_TYPE = AudioInput

    async def Chunks(self, stream: Stream[ChunksRequest, ChunksResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        try:
            audio_input = self.get_component(request.name)
        except ComponentNotFoundError as e:
            raise e.grpc_error

        audio_stream = await audio_input.stream()
        first_chunk = await anext(audio_stream)
        await stream.send_message(ChunksResponse(info=first_chunk.info.proto))
        await stream.send_message(ChunksResponse(chunk=first_chunk.chunk.proto))

        async for audio in audio_stream:
            await stream.send_message(ChunksResponse(chunk=audio.chunk.proto))

    async def Properties(self, stream: Stream[PropertiesRequest, PropertiesResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        try:
            audio_input = self.get_component(request.name)
        except ComponentNotFoundError as e:
            raise e.grpc_error
        response = (await audio_input.properties()).proto
        await stream.send_message(response)

    async def Record(self, stream: Stream[RecordRequest, HttpBody]) -> None:
        # TODO: Implement this function
        request = await stream.recv_message()
        assert request is not None
        try:
            audio_input = self.get_component(request.name)
        except ComponentNotFoundError as e:
            raise e.grpc_error
        response = HttpBody()
        await stream.send_message(response)
