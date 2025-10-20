import pytest
from grpclib.testing import ChannelFor

from viam.components.audio_out import AudioOutClient, AudioOutRPCService
from viam.proto.common import (
    GetGeometriesResponse,
      AudioInfo,
      GetPropertiesRequest,
      GetPropertiesResponse,
      DoCommandRequest,
)
from viam.resource.manager import ResourceManager
from viam.utils import dict_to_struct, struct_to_dict
from viam.proto.component.audioout import PlayRequest, AudioOutServiceStub

from .mocks.components import MockAudioOut


@pytest.fixture(scope="function")
def audio_out() -> MockAudioOut:
    return MockAudioOut(name="audio_out")


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
    async def test_get_properties(self, audio_out: MockAudioOut):
        properties = await audio_out.get_properties()
        assert isinstance(properties, GetPropertiesResponse)
        assert audio_out.get_properties_called

    @pytest.mark.asyncio
    async def test_do_command(self, audio_out: MockAudioOut):
        command = {"test": "command"}
        result = await audio_out.do_command(command)
        assert result == command


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
    async def test_get_properties(self, audio_out: MockAudioOut, service: AudioOutRPCService):
        async with ChannelFor([service]) as channel:
            client = AudioOutServiceStub(channel)
            request = GetPropertiesRequest(name=audio_out.name, extra=dict_to_struct({}))
            response = await client.GetProperties(request)

            assert isinstance(response, GetPropertiesResponse)
            assert audio_out.get_properties_called

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
            assert len(response.geometries) == 0  # MockAudioOut returns empty list


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
    async def test_get_properties(self, audio_out: MockAudioOut,service: AudioOutRPCService):
        async with ChannelFor([service]) as channel:
            client = AudioOutClient(audio_out.name, channel)
            properties = await client.get_properties()
            assert isinstance(properties, GetPropertiesResponse)
            assert audio_out.get_properties_called

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
            assert len(geometries) == 0
