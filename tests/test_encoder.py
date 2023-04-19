import pytest
from grpclib.testing import ChannelFor

from viam.components.encoder import EncoderClient
from viam.components.encoder.service import EncoderService
from viam.components.generic.service import GenericService
from viam.proto.common import DoCommandRequest, DoCommandResponse
from viam.proto.component.encoder import (
    EncoderServiceStub,
    GetPositionRequest,
    GetPositionResponse,
    GetPropertiesRequest,
    GetPropertiesResponse,
    PositionType,
    ResetPositionRequest,
)
from viam.resource.manager import ResourceManager
from viam.utils import dict_to_struct, struct_to_dict

from . import loose_approx
from .mocks.components import MockEncoder


@pytest.fixture(scope="function")
def encoder() -> MockEncoder:
    return MockEncoder(name="encoder")


@pytest.fixture(scope="function")
def service(encoder: MockEncoder) -> EncoderService:
    manager = ResourceManager([encoder])
    return EncoderService(manager)


@pytest.fixture(scope="function")
def generic_service(encoder: MockEncoder) -> GenericService:
    manager = ResourceManager([encoder])
    return GenericService(manager)


class TestEncoder:
    @pytest.mark.asyncio
    async def test_get_position(self, encoder: MockEncoder):
        pos, pos_type = await encoder.get_position(timeout=2.34)
        assert pos == 0
        assert pos_type == PositionType.POSITION_TYPE_TICKS_COUNT
        assert encoder.timeout == loose_approx(2.34)

    @pytest.mark.asyncio
    async def test_reset_position(self, encoder: MockEncoder):
        await encoder.reset_position(timeout=5.67)
        assert encoder.position == 0
        assert encoder.timeout == loose_approx(5.67)

    @pytest.mark.asyncio
    async def test_get_properties(self, encoder: MockEncoder):
        properties = await encoder.get_properties(timeout=6.78)
        assert properties.ticks_count_supported is True
        assert properties.angle_degrees_supported is False
        assert encoder.timeout == loose_approx(6.78)

    @pytest.mark.asyncio
    async def test_do(self, encoder: MockEncoder):
        command = {"command": "args"}
        resp = await encoder.do_command(command)
        assert resp == {"command": command}


class TestService:
    @pytest.mark.asyncio
    async def test_get_position(self, encoder: MockEncoder, service: EncoderService):
        async with ChannelFor([service]) as channel:
            client = EncoderServiceStub(channel)
            request = GetPositionRequest(name=encoder.name)
            response: GetPositionResponse = await client.GetPosition(request, timeout=2.34)
            assert response.value == 0
            assert response.position_type == PositionType.POSITION_TYPE_TICKS_COUNT
            assert encoder.timeout == loose_approx(2.34)

    @pytest.mark.asyncio
    async def test_reset_position(self, encoder: MockEncoder, service: EncoderService):
        async with ChannelFor([service]) as channel:
            client = EncoderServiceStub(channel)
            request = ResetPositionRequest(name=encoder.name)
            await client.ResetPosition(request, timeout=5.67)
            assert encoder.position == 0
            assert encoder.timeout == loose_approx(5.67)

    @pytest.mark.asyncio
    async def test_get_properties(self, encoder: MockEncoder, service: EncoderService):
        async with ChannelFor([service]) as channel:
            client = EncoderServiceStub(channel)
            request = GetPropertiesRequest(name=encoder.name)
            response: GetPropertiesResponse = await client.GetProperties(request, timeout=6.78)
            assert response.ticks_count_supported is True
            assert response.angle_degrees_supported is False
            assert encoder.timeout == loose_approx(6.78)

    @pytest.mark.asyncio
    async def test_do(self, encoder: MockEncoder, service: EncoderService):
        async with ChannelFor([service]) as channel:
            client = EncoderServiceStub(channel)
            command = {"command": "args"}
            request = DoCommandRequest(name=encoder.name, command=dict_to_struct(command))
            response: DoCommandResponse = await client.DoCommand(request)
            result = struct_to_dict(response.result)
            assert result == {"command": command}


class TestClient:
    @pytest.mark.asyncio
    async def test_get_position(self, encoder: MockEncoder, service: EncoderService):
        async with ChannelFor([service]) as channel:
            client = EncoderClient(encoder.name, channel)
            position, pos_type = await client.get_position(timeout=2.34)
            assert position == 0
            assert pos_type == PositionType.POSITION_TYPE_TICKS_COUNT
            assert encoder.timeout == loose_approx(2.34)

    @pytest.mark.asyncio
    async def test_reset_position(self, encoder: MockEncoder, service: EncoderService):
        async with ChannelFor([service]) as channel:
            client = EncoderClient(encoder.name, channel)
            await client.reset_position(timeout=5.67)
            assert encoder.timeout == loose_approx(5.67)
            assert encoder.position == 0

    @pytest.mark.asyncio
    async def test_get_properties(self, encoder: MockEncoder, service: EncoderService):
        async with ChannelFor([service]) as channel:
            client = EncoderClient(encoder.name, channel)
            properties = await client.get_properties(timeout=6.78)
            assert properties.ticks_count_supported is True
            assert properties.angle_degrees_supported is False
            assert encoder.timeout == loose_approx(6.78)

    @pytest.mark.asyncio
    async def test_do(self, encoder: MockEncoder, service: EncoderService):
        async with ChannelFor([service]) as channel:
            client = EncoderClient(encoder.name, channel)
            command = {"command": "args"}
            resp = await client.do_command(command)
            assert resp == {"command": command}
