import pytest
from grpclib.testing import ChannelFor

from viam.components.switch.service import SwitchRPCService
from viam.components.switch import SwitchClient
from viam.proto.common import (
    DoCommandRequest,
    DoCommandResponse,
)
from viam.gen.component.switch.v1.switch_pb2 import (
    GetPositionRequest,
    GetPositionResponse,
    SetPositionRequest,
    GetNumberOfPositionsRequest,
    GetNumberOfPositionsResponse,
)
from viam.proto.component.switch import SwitchServiceStub
from viam.resource.manager import ResourceManager
from viam.utils import dict_to_struct, struct_to_dict

from . import loose_approx
from .mocks.components import MockSwitch

DEFAULT_POSITION = 0
DEFAULT_NUMBER_OF_POSITIONS = 0
EXTRA_PARAMS = {"foo": "bar", "baz": [1, 2, 3]}


@pytest.fixture(scope="function")
def switch() -> MockSwitch:
    return MockSwitch(name="sensor", number_of_positions=DEFAULT_NUMBER_OF_POSITIONS, position=DEFAULT_POSITION)


class TestSwitch:
    pos = 2

    async def test_set_position(self, switch):
        await switch.set_position(self.pos, timeout=1.23, extra=EXTRA_PARAMS)
        assert switch.position == self.pos
        assert switch.timeout == loose_approx(1.23)
        assert switch.extra == EXTRA_PARAMS

    async def test_get_position(self, switch):
        assert switch.extra is None
        position = await switch.get_position(timeout=2.34, extra=EXTRA_PARAMS)
        assert position == DEFAULT_NUMBER_OF_POSITIONS
        assert switch.extra == EXTRA_PARAMS
        assert switch.timeout == loose_approx(2.34)

    async def test_get_number_of_positions(self, switch):
        number_of_positions = await switch.get_number_of_positions(timeout=3.45, extra=EXTRA_PARAMS)
        assert number_of_positions == DEFAULT_NUMBER_OF_POSITIONS
        assert switch.extra == EXTRA_PARAMS
        assert switch.timeout == loose_approx(3.45)

    async def test_do(self, switch):
        command = {"command": "args"}
        resp = await switch.do_command(command)
        assert resp == {"command": command}


@pytest.fixture(scope="function")
def manager(switch) -> ResourceManager:
    return ResourceManager([switch])


@pytest.fixture(scope="function")
def service(manager) -> SwitchRPCService:
    return SwitchRPCService(manager)


class TestService:
    pos = 2

    async def test_set_position(self, switch, service):
        async with ChannelFor([service]) as channel:
            client = SwitchServiceStub(channel)
            request = SetPositionRequest(name=switch.name, position=self.pos, extra=dict_to_struct(EXTRA_PARAMS))
            assert switch.extra is None
            await client.SetPosition(request, timeout=1.23)
            assert switch.position == self.pos
            assert switch.extra == EXTRA_PARAMS
            assert switch.timeout == loose_approx(1.23)

    async def test_get_position(self, switch, service):
        async with ChannelFor([service]) as channel:
            client = SwitchServiceStub(channel)
            request = GetPositionRequest(name=switch.name, extra=dict_to_struct(EXTRA_PARAMS))
            assert switch.extra is None
            result: GetPositionResponse = await client.GetPosition(request, timeout=2.34)
            assert result.position == DEFAULT_POSITION
            assert switch.extra == EXTRA_PARAMS
            assert switch.timeout == loose_approx(2.34)

    async def test_get_number_of_positions(self, switch, service):
        async with ChannelFor([service]) as channel:
            client = SwitchServiceStub(channel)
            request = GetNumberOfPositionsRequest(name=switch.name, extra=dict_to_struct(EXTRA_PARAMS))
            assert switch.extra is None
            result: GetNumberOfPositionsResponse = await client.GetNumberOfPositions(request, timeout=4.56)
            assert result.number_of_positions == DEFAULT_NUMBER_OF_POSITIONS
            assert switch.extra == EXTRA_PARAMS
            assert switch.timeout == loose_approx(4.56)

    async def test_do(self, switch: MockSwitch, service: SwitchRPCService):
        async with ChannelFor([service]) as channel:
            client = SwitchServiceStub(channel)
            command = {"command": "args"}
            request = DoCommandRequest(name=switch.name, command=dict_to_struct(command))
            response: DoCommandResponse = await client.DoCommand(request)
            result = struct_to_dict(response.result)
            assert result == {"command": command}


class TestClient:
    pos = 2

    async def test_set_position(self, switch, service):
        async with ChannelFor([service]) as channel:
            client = SwitchClient(switch.name, channel)
            assert switch.extra is None
            await client.set_position(position=self.pos, timeout=3.45, extra=EXTRA_PARAMS)
            assert switch.position == self.pos
            assert switch.extra == EXTRA_PARAMS
            assert switch.timeout == loose_approx(3.45)

    async def test_get_position(self, switch, service):
        async with ChannelFor([service]) as channel:
            client = SwitchClient(switch.name, channel)
            assert switch.extra is None
            value_position = await client.get_position(timeout=3.45, extra=EXTRA_PARAMS)
            assert DEFAULT_POSITION == value_position
            assert switch.extra == EXTRA_PARAMS
            assert switch.timeout == loose_approx(3.45)

    async def test_get_number_of_positions(self, switch, service):
        async with ChannelFor([service]) as channel:
            client = SwitchClient(switch.name, channel)
            assert switch.extra is None
            value_number_of_positions = await client.get_number_of_positions(timeout=3.45, extra=EXTRA_PARAMS)
            assert DEFAULT_NUMBER_OF_POSITIONS == value_number_of_positions
            assert switch.extra == EXTRA_PARAMS
            assert switch.timeout == loose_approx(3.45)

    async def test_do(self, switch, manager, service):
        async with ChannelFor([service]) as channel:
            client = SwitchClient(switch.name, channel)
            command = {"command": "args"}
            resp = await client.do_command(command)
            assert resp == {"command": command}
