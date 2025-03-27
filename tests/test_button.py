import pytest
from grpclib.testing import ChannelFor

from viam.components.button import ButtonClient
from viam.components.button.service import ButtonRPCService
from viam.gen.component.button.v1.button_pb2 import (
    PushRequest
)
from viam.proto.common import (
    DoCommandRequest,
    DoCommandResponse,
)
from viam.proto.component.button import ButtonServiceStub
from viam.resource.manager import ResourceManager
from viam.utils import dict_to_struct, struct_to_dict

from . import loose_approx
from .mocks.components import MockButton

EXTRA_PARAMS = {"foo": "bar", "baz": [1, 2, 3]}


@pytest.fixture(scope="function")
def button() -> MockButton:
    return MockButton(name="button")


class TestButton:
    async def test_push(self, button):
        await button.push(timeout=1.23, extra=EXTRA_PARAMS)
        assert button.pushed is True
        assert button.timeout == loose_approx(1.23)
        assert button.extra == EXTRA_PARAMS

    async def test_do(self, button):
        command = {"command": "args"}
        resp = await button.do_command(command)
        assert resp == {"command": command}


@pytest.fixture(scope="function")
def manager(button) -> ResourceManager:
    return ResourceManager([button])


@pytest.fixture(scope="function")
def service(manager) -> ButtonRPCService:
    return ButtonRPCService(manager)


class TestService:
    async def test_push(self, button, service):
        async with ChannelFor([service]) as channel:
            client = ButtonServiceStub(channel)
            request = PushRequest(name=button.name, extra=dict_to_struct(EXTRA_PARAMS))
            assert button.extra is None
            await client.Push(request, timeout=1.23)
            assert button.pushed is True
            assert button.extra == EXTRA_PARAMS
            assert button.timeout == loose_approx(1.23)

    async def test_do(self, button: MockButton, service: ButtonRPCService):
        async with ChannelFor([service]) as channel:
            client = ButtonServiceStub(channel)
            command = {"command": "args"}
            request = DoCommandRequest(name=button.name, command=dict_to_struct(command))
            response: DoCommandResponse = await client.DoCommand(request)
            result = struct_to_dict(response.result)
            assert result == {"command": command}


class TestClient:
    async def test_push(self, button, service):
        async with ChannelFor([service]) as channel:
            client = ButtonClient(button.name, channel)
            assert button.extra is None
            await client.push(timeout=3.45, extra=EXTRA_PARAMS)
            assert button.pushed is True
            assert button.extra == EXTRA_PARAMS
            assert button.timeout == loose_approx(3.45)

    async def test_do(self, button, manager, service):
        async with ChannelFor([service]) as channel:
            client = ButtonClient(button.name, channel)
            command = {"command": "args"}
            resp = await client.do_command(command)
            assert resp == {"command": command}
