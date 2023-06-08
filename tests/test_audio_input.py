import sys
from datetime import timedelta
from typing import Union

import pytest
from grpclib import GRPCError
from grpclib.testing import ChannelFor

from viam.components.audio_input import AudioInput, AudioInputClient, AudioInputRPCService
from viam.components.generic.service import GenericRPCService
from viam.resource.manager import ResourceManager
from viam.proto.common import DoCommandRequest, DoCommandResponse, GetGeometriesRequest
from viam.proto.component.audioinput import (
    AudioInputServiceStub,
    ChunksRequest,
    ChunksResponse,
    PropertiesRequest,
    PropertiesResponse,
    RecordRequest,
    SampleFormat,
)
from viam.utils import dict_to_struct, struct_to_dict

from . import loose_approx
from .mocks.components import MockAudioInput

PROPERTIES = AudioInput.Properties(
    channel_count=2,
    latency=timedelta(milliseconds=20),
    sample_rate=41400,
    sample_size=2,
    is_big_endian=sys.byteorder != "little",
    is_float=True,
    is_interleaved=True,
)


@pytest.fixture(scope="function")
def audio_input() -> MockAudioInput:
    return MockAudioInput(name="audio_input", properties=PROPERTIES)


@pytest.fixture(scope="function")
def service(audio_input: MockAudioInput) -> AudioInputRPCService:
    manager = ResourceManager([audio_input])
    return AudioInputRPCService(manager)


@pytest.fixture(scope="function")
def generic_service(audio_input: MockAudioInput) -> GenericRPCService:
    manager = ResourceManager([audio_input])
    return GenericRPCService(manager)


class TestAudioInput:
    @pytest.mark.asyncio
    async def test_stream(self, audio_input: AudioInput):
        idx = 0
        async for audio in await audio_input.stream():
            assert audio.info.channels == PROPERTIES.channel_count
            assert audio.info.sample_format == SampleFormat.SAMPLE_FORMAT_FLOAT32_INTERLEAVED
            assert audio.info.sampling_rate == PROPERTIES.sample_rate

            assert audio.chunk.data == f"{idx}".encode("utf-8")
            assert audio.chunk.length == 182

            idx += 1

    @pytest.mark.asyncio
    async def test_get_properties(self, audio_input: AudioInput):
        assert await audio_input.get_properties() == PROPERTIES

    @pytest.mark.asyncio
    async def test_do(self, audio_input: AudioInput):
        command = {"command": "args"}
        resp = await audio_input.do_command(command)
        assert resp == {"command": command}


class TestService:
    @pytest.mark.asyncio
    async def test_chunks(self, audio_input: AudioInput, service: AudioInputRPCService):
        async with ChannelFor([service]) as channel:
            client = AudioInputServiceStub(channel)
            async with client.Chunks.open() as stream:
                await stream.send_message(
                    ChunksRequest(name=audio_input.name, sample_format=SampleFormat.SAMPLE_FORMAT_FLOAT32_INTERLEAVED)
                )
                response: Union[ChunksResponse, None] = await stream.recv_message()
                assert response is not None and response.HasField("info")
                assert response.info.channels == PROPERTIES.channel_count
                assert response.info.sample_format == SampleFormat.SAMPLE_FORMAT_FLOAT32_INTERLEAVED
                assert response.info.sampling_rate == PROPERTIES.sample_rate

                idx = 0
                while True:
                    response = await stream.recv_message()
                    if response is None:
                        break
                    assert response.HasField("chunk")
                    assert response.chunk.data == f"{idx}".encode("utf-8")
                    assert response.chunk.length == 182
                    idx += 1

    @pytest.mark.asyncio
    async def test_properties(self, audio_input: MockAudioInput, service: AudioInputRPCService):
        assert audio_input.timeout is None
        async with ChannelFor([service]) as channel:
            client = AudioInputServiceStub(channel)
            response: PropertiesResponse = await client.Properties(PropertiesRequest(name=audio_input.name), timeout=1.82)
            assert AudioInput.Properties.from_proto(response) == PROPERTIES
            assert audio_input.timeout == loose_approx(1.82)

    @pytest.mark.asyncio
    async def test_record(self, service: AudioInputRPCService):
        async with ChannelFor([service]) as channel:
            client = AudioInputServiceStub(channel)
            with pytest.raises(GRPCError, match=r".*Status.UNIMPLEMENTED.*"):
                await client.Record(RecordRequest())

    @pytest.mark.asyncio
    async def test_do(self, audio_input: MockAudioInput, service: AudioInputRPCService):
        async with ChannelFor([service]) as channel:
            client = AudioInputServiceStub(channel)
            command = {"command": "args"}
            request = DoCommandRequest(name=audio_input.name, command=dict_to_struct(command))
            response: DoCommandResponse = await client.DoCommand(request)
            result = struct_to_dict(response.result)
            assert result == {"command": command}

    @pytest.mark.asyncio
    async def test_get_geometries(self, service: AudioInputRPCService):
        async with ChannelFor([service]) as channel:
            client = AudioInputServiceStub(channel)
            request = GetGeometriesRequest()
            with pytest.raises(GRPCError, match=r"Method [a-zA-Z]+ not implemented"):
                await client.GetGeometries(request)


class TestClient:
    @pytest.mark.asyncio
    async def test_stream(self, audio_input: AudioInput, service: AudioInputRPCService):
        async with ChannelFor([service]) as channel:
            client = AudioInputClient(audio_input.name, channel)

            idx = 0
            async for audio in await client.stream():
                assert audio.info.channels == PROPERTIES.channel_count
                assert audio.info.sample_format == SampleFormat.SAMPLE_FORMAT_FLOAT32_INTERLEAVED
                assert audio.info.sampling_rate == PROPERTIES.sample_rate

                assert audio.chunk.data == f"{idx}".encode("utf-8")
                assert audio.chunk.length == 182

                idx += 1

    @pytest.mark.asyncio
    async def test_get_properties(self, audio_input: MockAudioInput, service: AudioInputRPCService):
        assert audio_input.timeout is None
        async with ChannelFor([service]) as channel:
            client = AudioInputClient(audio_input.name, channel)
            assert await client.get_properties(timeout=4.4) == PROPERTIES
            assert audio_input.timeout == loose_approx(4.4)

    @pytest.mark.asyncio
    async def test_do(self, audio_input: AudioInput, service: AudioInputRPCService):
        async with ChannelFor([service]) as channel:
            client = AudioInputClient(audio_input.name, channel)
            command = {"command": "args"}
            resp = await client.do_command(command)
            assert resp == {"command": command}
