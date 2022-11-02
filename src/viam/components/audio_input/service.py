import wave
from datetime import timedelta
from io import BytesIO

from google.api.httpbody_pb2 import HttpBody
from grpclib import GRPCError, Status
from grpclib.server import Stream

from viam.components.service_base import ComponentServiceBase
from viam.errors import ComponentNotFoundError, NotSupportedError
from viam.gen.component.audioinput.v1.audioinput_pb2 import SampleFormat
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

        timeout = stream.deadline.time_remaining() if stream.deadline else None
        audio_stream = await audio_input.stream(timeout=timeout)
        first_chunk = await audio_stream.__anext__()
        await stream.send_message(ChunksResponse(info=first_chunk.info))
        await stream.send_message(ChunksResponse(chunk=first_chunk.chunk))

        async for audio in audio_stream:
            await stream.send_message(ChunksResponse(chunk=audio.chunk))

    async def Properties(self, stream: Stream[PropertiesRequest, PropertiesResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        try:
            audio_input = self.get_component(request.name)
        except ComponentNotFoundError as e:
            raise e.grpc_error
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        response = (await audio_input.get_properties(timeout=timeout)).proto
        await stream.send_message(response)

    async def Record(self, stream: Stream[RecordRequest, HttpBody]) -> None:
        raise NotSupportedError("Recording audio input is not supported").grpc_error

        # TODO: Eventually implement recording
        request = await stream.recv_message()
        assert request is not None
        duration = request.duration.ToTimedelta()
        if duration.total_seconds() == 0:
            duration = timedelta(seconds=1)
        if duration.total_seconds() > 5:
            raise GRPCError(Status.INVALID_ARGUMENT, "Can only record up to 5 seconds")

        try:
            audio_input = self.get_component(request.name)
        except ComponentNotFoundError as e:
            raise e.grpc_error
        audio_stream = await audio_input.stream()
        first_chunk = await audio_stream.__anext__()
        num_chunks = int(duration.total_seconds() * float(first_chunk.info.sampling_rate / first_chunk.chunk.length))

        sample_width: int
        if first_chunk.info.sample_format == SampleFormat.SAMPLE_FORMAT_INT16_INTERLEAVED:
            sample_width = 2
        elif first_chunk.info.sample_format == SampleFormat.SAMPLE_FORMAT_FLOAT32_INTERLEAVED:
            sample_width = 4
        else:
            raise GRPCError(Status.INVALID_ARGUMENT, "Unspecified type of audio buffer")

        output = BytesIO()
        wav_file = wave.open(output, "w")
        wav_file.setnchannels(first_chunk.info.channels)
        wav_file.setframerate(first_chunk.info.sampling_rate)
        wav_file.setsampwidth(sample_width)
        try:
            wav_file.writeframes(first_chunk.chunk.data)
            for _ in range(num_chunks - 1):
                chunk = await audio_stream.__anext__()
                wav_file.writeframes(chunk.chunk.data)
        finally:
            wav_file.close()
            output.close()

        output.seek(0)
        response = HttpBody(data=output.read(), content_type="audio/wav")

        await stream.send_message(response)
