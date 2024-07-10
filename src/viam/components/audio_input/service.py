import wave
from datetime import timedelta
from io import BytesIO

from google.api.httpbody_pb2 import HttpBody  # type: ignore
from grpclib import GRPCError, Status
from grpclib.server import Stream

from viam.errors import NotSupportedError
from viam.proto.common import DoCommandRequest, DoCommandResponse, GetGeometriesRequest, GetGeometriesResponse
from viam.proto.component.audioinput import (
    AudioInputServiceBase,
    ChunksRequest,
    ChunksResponse,
    PropertiesRequest,
    PropertiesResponse,
    RecordRequest,
    SampleFormat,
)
from viam.resource.rpc_service_base import ResourceRPCServiceBase
from viam.utils import dict_to_struct, struct_to_dict

from .audio_input import AudioInput


class AudioInputRPCService(AudioInputServiceBase, ResourceRPCServiceBase[AudioInput]):
    """
    gRPC Service for a generic AudioInput
    """

    RESOURCE_TYPE = AudioInput

    async def Chunks(self, stream: Stream[ChunksRequest, ChunksResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        audio_input = self.get_resource(request.name)
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        audio_stream = await audio_input.stream(timeout=timeout, metadata=stream.metadata)
        first_chunk = await audio_stream.__anext__()
        await stream.send_message(ChunksResponse(info=first_chunk.info))
        await stream.send_message(ChunksResponse(chunk=first_chunk.chunk))

        async for audio in audio_stream:
            await stream.send_message(ChunksResponse(chunk=audio.chunk))

    async def Properties(self, stream: Stream[PropertiesRequest, PropertiesResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        audio_input = self.get_resource(request.name)
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        response = (await audio_input.get_properties(timeout=timeout, metadata=stream.metadata)).proto
        await stream.send_message(response)

    async def Record(self, stream: Stream[RecordRequest, HttpBody]) -> None:  # pyright: ignore [reportInvalidTypeForm]
        raise NotSupportedError("Recording audio input is not supported").grpc_error

        # TODO: Eventually implement recording
        request = await stream.recv_message()
        assert request is not None
        duration = request.duration.ToTimedelta()
        if duration.total_seconds() == 0:
            duration = timedelta(seconds=1)
        if duration.total_seconds() > 5:
            raise GRPCError(Status.INVALID_ARGUMENT, "Can only record up to 5 seconds")

        audio_input = self.get_resource(request.name)
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

    async def DoCommand(self, stream: Stream[DoCommandRequest, DoCommandResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        audio_input = self.get_resource(request.name)
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        result = await audio_input.do_command(command=struct_to_dict(request.command), timeout=timeout, metadata=stream.metadata)
        response = DoCommandResponse(result=dict_to_struct(result))
        await stream.send_message(response)

    async def GetGeometries(self, stream: Stream[GetGeometriesRequest, GetGeometriesResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        audio_input = self.get_resource(request.name)
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        geometries = await audio_input.get_geometries(extra=struct_to_dict(request.extra), timeout=timeout)
        response = GetGeometriesResponse(geometries=geometries)
        await stream.send_message(response)
