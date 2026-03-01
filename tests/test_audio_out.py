import pytest
from grpclib.testing import ChannelFor

from viam.components.audio_out import AudioOut, AudioOutClient, AudioOutRPCService
from viam.proto.common import (
    AudioInfo,
    DoCommandRequest,
    GetGeometriesResponse,
    GetPropertiesRequest,
    GetPropertiesResponse,
)
from viam.proto.component.audioout import AudioOutServiceStub, PlayRequest
from viam.resource.manager import ResourceManager
from viam.utils import dict_to_struct, struct_to_dict

from . import expected_grpc_timeout
from .mocks.components import GEOMETRIES, MockAudioOut

# Test properties for the mock AudioIn
PROPERTIES = AudioOut.Properties(
    supported_codecs=["pcm16", "mp3"],
    sample_rate_hz=44100,
    num_channels=2,
)


@pytest.fixture(scope="function")
def audio_out() -> MockAudioOut:
    return MockAudioOut(name="audio_out", properties=PROPERTIES)


@pytest.fixture(scope="function")
def service(audio_out: MockAudioOut) -> AudioOutRPCService:
    manager = ResourceManager([audio_out])
    return AudioOutRPCService(manager)


class TestAudioOut:
    @pytest.mark.asyncio
    async def test_play(self, audio_out: MockAudioOut):
        audio_data = b"test_audio_data"
        audio_info = AudioInfo(codec="pcm16", sample_rate_hz=44100, num_channels=2)
        await audio_out.play(audio_data, audio_info)
        assert audio_out.play_called
        assert audio_out.last_audio_data == audio_data
        assert audio_out.last_audio_info == audio_info

    @pytest.mark.asyncio
    async def test_play_without_audio_info(self, audio_out: MockAudioOut):
        audio_data = b"test_audio_data"
        await audio_out.play(audio_data)
        assert audio_out.play_called
        assert audio_out.last_audio_data == audio_data
        assert audio_out.last_audio_info is None

    @pytest.mark.asyncio
    async def test_get_properties(self, audio_out: MockAudioOut):
        properties = await audio_out.get_properties()
        assert isinstance(properties, GetPropertiesResponse)
        assert properties.supported_codecs == PROPERTIES.supported_codecs
        assert properties.sample_rate_hz == PROPERTIES.sample_rate_hz
        assert properties.num_channels == PROPERTIES.num_channels

    @pytest.mark.asyncio
    async def test_do_command(self, audio_out: MockAudioOut):
        command = {"test": "command"}
        result = await audio_out.do_command(command)
        assert result == command

    @pytest.mark.asyncio
    async def test_get_geometries(self, audio_out: MockAudioOut):
        geometries = await audio_out.get_geometries()
        assert geometries == GEOMETRIES


class TestService:
    @pytest.mark.asyncio
    async def test_play(self, audio_out: MockAudioOut, service: AudioOutRPCService):
        audio_data = b"test_audio_data"
        audio_info = AudioInfo(codec="pcm16", sample_rate_hz=44100, num_channels=2)

        async with ChannelFor([service]) as channel:
            client = AudioOutServiceStub(channel)
            request = PlayRequest(
                name=audio_out.name,
                audio_data=audio_data,
                audio_info=audio_info,
                extra=dict_to_struct({}),
            )

            await client.Play(request)

            assert audio_out.play_called
            assert audio_out.last_audio_data == audio_data
            assert audio_out.last_audio_info == audio_info

    @pytest.mark.asyncio
    async def test_play_without_audio_info(self, audio_out: MockAudioOut, service: AudioOutRPCService):
        audio_data = b"test_audio_data"

        async with ChannelFor([service]) as channel:
            client = AudioOutServiceStub(channel)
            request = PlayRequest(
                name=audio_out.name,
                audio_data=audio_data,
                audio_info=None,
                extra=dict_to_struct({}),
            )

            await client.Play(request)

            assert audio_out.play_called
            assert audio_out.last_audio_data == audio_data
            assert audio_out.last_audio_info is None

    @pytest.mark.asyncio
    async def test_get_properties(self, audio_out: MockAudioOut, service: AudioOutRPCService):
        async with ChannelFor([service]) as channel:
            client = AudioOutServiceStub(channel)
            response: GetPropertiesResponse = await client.GetProperties(GetPropertiesRequest(name=audio_out.name), timeout=1.82)
            assert response.supported_codecs == PROPERTIES.supported_codecs
            assert response.sample_rate_hz == PROPERTIES.sample_rate_hz
            assert response.num_channels == PROPERTIES.num_channels
            assert audio_out.timeout == expected_grpc_timeout(1.82)

    @pytest.mark.asyncio
    async def test_do_command(self, audio_out: MockAudioOut, service: AudioOutRPCService):
        command = {"test": "command"}

        async with ChannelFor([service]) as channel:
            client = AudioOutServiceStub(channel)
            request = DoCommandRequest(name=audio_out.name, command=dict_to_struct(command))
            response = await client.DoCommand(request)

            result = struct_to_dict(response.result)
            assert result == command

    @pytest.mark.asyncio
    async def test_get_geometries(self, audio_out: MockAudioOut, service: AudioOutRPCService):
        from viam.proto.common import GetGeometriesRequest

        async with ChannelFor([service]) as channel:
            client = AudioOutServiceStub(channel)
            request = GetGeometriesRequest(name=audio_out.name, extra=dict_to_struct({}))
            response = await client.GetGeometries(request)

            assert isinstance(response, GetGeometriesResponse)
            assert [geometry for geometry in response.geometries] == GEOMETRIES


class TestClient:
    @pytest.mark.asyncio
    async def test_play(self, audio_out: MockAudioOut, service: AudioOutRPCService):
        async with ChannelFor([service]) as channel:
            client = AudioOutClient(audio_out.name, channel)
            audio_data = b"test_audio_data"
            audio_info = AudioInfo(codec="pcm16", sample_rate_hz=44100, num_channels=2)

            await client.play(audio_data, audio_info)

            assert audio_out.play_called
            assert audio_out.last_audio_data == audio_data
            assert audio_out.last_audio_info == audio_info

    @pytest.mark.asyncio
    async def test_play_without_audio_info(self, audio_out: MockAudioOut, service: AudioOutRPCService):
        async with ChannelFor([service]) as channel:
            client = AudioOutClient(audio_out.name, channel)
            audio_data = b"test_audio_data"

            await client.play(audio_data)

            assert audio_out.play_called
            assert audio_out.last_audio_data == audio_data
            assert audio_out.last_audio_info is None

    @pytest.mark.asyncio
    async def test_get_properties(self, audio_out: MockAudioOut, service: AudioOutRPCService):
        async with ChannelFor([service]) as channel:
            client = AudioOutClient(audio_out.name, channel)
            properties = await client.get_properties(timeout=4.4)
            assert isinstance(properties, GetPropertiesResponse)
            assert properties.supported_codecs == PROPERTIES.supported_codecs
            assert properties.sample_rate_hz == PROPERTIES.sample_rate_hz
            assert properties.num_channels == PROPERTIES.num_channels
            assert audio_out.timeout == expected_grpc_timeout(4.4)

    @pytest.mark.asyncio
    async def test_do_command(self, audio_out: MockAudioOut, service: AudioOutRPCService):
        async with ChannelFor([service]) as channel:
            client = AudioOutClient(audio_out.name, channel)
            command = {"command": "args"}
            resp = await client.do_command(command)
            assert resp == command

    @pytest.mark.asyncio
    async def test_get_geometries(self, audio_out: MockAudioOut, service: AudioOutRPCService):
        async with ChannelFor([service]) as channel:
            client = AudioOutClient(audio_out.name, channel)
            geometries = await client.get_geometries()
            assert geometries == GEOMETRIES
