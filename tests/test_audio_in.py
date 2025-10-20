import pytest
from grpclib.testing import ChannelFor

from viam.components.audio_in import AudioIn, AudioInClient, AudioInRPCService, AudioResponse
from viam.components.generic.service import GenericRPCService
from viam.proto.common import (
    DoCommandRequest,
    DoCommandResponse,
    GetGeometriesRequest,
    GetGeometriesResponse,
    GetPropertiesRequest,
    GetPropertiesResponse,
)
from viam.proto.component.audioin import (
    AudioInServiceStub,
    GetAudioRequest
)
from viam.resource.manager import ResourceManager
from viam.utils import dict_to_struct, struct_to_dict

from . import loose_approx
from .mocks.components import GEOMETRIES, MockAudioIn

# Test properties for the mock AudioIn
PROPERTIES = AudioIn.Properties(
    supported_codecs=["pcm16", "mp3"],
    sample_rate_hz=44100,
    num_channels=2,
)


@pytest.fixture(scope="function")
def audio_in() -> MockAudioIn:
    return MockAudioIn(name="audio_in", properties=PROPERTIES)


@pytest.fixture(scope="function")
def service(audio_in: MockAudioIn) -> AudioInRPCService:
    manager = ResourceManager([audio_in])
    return AudioInRPCService(manager)


@pytest.fixture(scope="function")
def generic_service(audio_in: MockAudioIn) -> GenericRPCService:
    manager = ResourceManager([audio_in])
    return GenericRPCService(manager)


class TestAudioIn:
    async def test_get_audio(self, audio_in: AudioIn):
        previous_timestamp = 1000000000  # 1 second in nanoseconds
        codec = "pcm16"
        duration_seconds = 2.0

        stream = await audio_in.get_audio(codec, duration_seconds, previous_timestamp)

        chunk_count = 0
        async for response in stream:
            assert response.audio.audio_data is not None
            assert response.audio.audio_info.codec == codec
            assert response.audio.audio_info.sample_rate_hz == PROPERTIES.sample_rate_hz
            assert response.audio.audio_info.num_channels == PROPERTIES.num_channels
            assert response.audio.sequence == chunk_count
            assert response.audio.start_timestamp_nanoseconds >= previous_timestamp
            assert response.audio.end_timestamp_nanoseconds > response.audio.start_timestamp_nanoseconds
            chunk_count += 1

        assert chunk_count == 2  # Should have received 2 chunks from mock

    async def test_get_properties(self, audio_in: AudioIn):
        properties = await audio_in.get_properties()
        assert properties.supported_codecs == PROPERTIES.supported_codecs
        assert properties.sample_rate_hz == PROPERTIES.sample_rate_hz
        assert properties.num_channels == PROPERTIES.num_channels

    async def test_do_command(self, audio_in: AudioIn):
        command = {"command": "args"}
        resp = await audio_in.do_command(command)
        assert resp == {"command": command}

            #


class TestService:
    async def test_get_audio(self, audio_in: AudioIn, service: AudioInRPCService):
        async with ChannelFor([service]) as channel:
            client = AudioInServiceStub(channel)
            previous_timestamp = 1000000000
            codec = "pcm16"
            duration_seconds = 2.0

            request = GetAudioRequest(
                name=audio_in.name,
                codec=codec,
                duration_seconds=duration_seconds,
                previous_timestamp_nanoseconds=previous_timestamp
            )

            async with client.GetAudio.open() as stream:
                await stream.send_message(request)

                chunk_count = 0
                async for response in stream:
                    assert isinstance(response, AudioResponse)
                    assert response.audio.audio_data is not None
                    assert response.audio.audio_info.codec == codec
                    assert response.audio.audio_info.sample_rate_hz == PROPERTIES.sample_rate_hz
                    assert response.audio.audio_info.num_channels == PROPERTIES.num_channels
                    assert response.audio.sequence == chunk_count
                    chunk_count += 1

                assert chunk_count > 0

    async def test_get_properties(self, audio_in: MockAudioIn, service: AudioInRPCService):
        assert audio_in.timeout is None
        async with ChannelFor([service]) as channel:
            client = AudioInServiceStub(channel)
            response: GetPropertiesResponse = await client.GetProperties(
                GetPropertiesRequest(name=audio_in.name), timeout=1.82
            )
            assert response.supported_codecs == PROPERTIES.supported_codecs
            assert response.sample_rate_hz == PROPERTIES.sample_rate_hz
            assert response.num_channels == PROPERTIES.num_channels
            assert audio_in.timeout == loose_approx(1.82)

    async def test_do_command(self, audio_in: MockAudioIn, service: AudioInRPCService):
        async with ChannelFor([service]) as channel:
            client = AudioInServiceStub(channel)
            command = {"command": "args"}
            request = DoCommandRequest(name=audio_in.name, command=dict_to_struct(command))
            response: DoCommandResponse = await client.DoCommand(request)
            result = struct_to_dict(response.result)
            assert result == {"command": command}

    async def test_get_geometries(self, audio_in: MockAudioIn, service: AudioInRPCService):
        async with ChannelFor([service]) as channel:
            client = AudioInServiceStub(channel)
            request = GetGeometriesRequest(name=audio_in.name)
            response: GetGeometriesResponse = await client.GetGeometries(request)
            assert [geometry for geometry in response.geometries] == GEOMETRIES


class TestClient:
    async def test_get_audio(self, audio_in: AudioIn, service: AudioInRPCService):
        async with ChannelFor([service]) as channel:
            client = AudioInClient(audio_in.name, channel)

            previous_timestamp = 1000000000
            codec = "pcm16"
            duration_seconds = 2.0

            stream = await client.get_audio(codec, duration_seconds, previous_timestamp)

            chunk_count = 0
            async for resp in stream:
                assert resp.audio.audio_data is not None
                assert resp.audio.audio_info.codec == codec
                assert resp.audio.audio_info.sample_rate_hz == PROPERTIES.sample_rate_hz
                assert resp.audio.audio_info.num_channels == PROPERTIES.num_channels
                assert resp.audio.sequence == chunk_count
                chunk_count += 1

            assert chunk_count > 0

    async def test_get_properties(self, audio_in: MockAudioIn, service: AudioInRPCService):
        assert audio_in.timeout is None
        async with ChannelFor([service]) as channel:
            client = AudioInClient(audio_in.name, channel)
            properties = await client.get_properties(timeout=4.4)
            assert properties.supported_codecs == PROPERTIES.supported_codecs
            assert properties.sample_rate_hz == PROPERTIES.sample_rate_hz
            assert properties.num_channels == PROPERTIES.num_channels
            assert audio_in.timeout == loose_approx(4.4)

    async def test_do_command(self, audio_in: AudioIn, service: AudioInRPCService):
        async with ChannelFor([service]) as channel:
            client = AudioInClient(audio_in.name, channel)
            command = {"command": "args"}
            resp = await client.do_command(command)
            assert resp == {"command": command}
