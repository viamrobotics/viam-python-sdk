from typing import cast
from unittest.mock import AsyncMock

import pytest
from grpclib.testing import ChannelFor

from viam.components.switch import Switch, SwitchClient
from viam.components.switch.service import SwitchRPCService
from viam.gen.component.switch.v1.switch_pb2 import (
    GetNumberOfPositionsRequest,
    GetPositionRequest,
    SetPositionRequest,
)
from viam.proto.common import (
    DoCommandRequest,
)
from viam.proto.component.switch import SwitchServiceStub
from viam.resource.manager import ResourceManager
from viam.resource.rpc_client_base import ResourceRPCClientBase
from viam.utils import dict_to_struct

from . import loose_approx
from .mocks import create_mock_subclass

DEFAULT_POSITION = 0
DEFAULT_NUMBER_OF_POSITIONS = 3
DEFAULT_LABELS = ["a", "b", "c"]
DEFAULT_EXTRA = {"foo": "bar", "baz": [1, 2, 3]}
EXTRA_PARAMS_STRUCT = dict_to_struct(DEFAULT_EXTRA)
DEFAULT_TIMEOUT = 1.82
DEFAULT_TIMEOUT_APPROX = loose_approx(DEFAULT_TIMEOUT)
DEFAULT_METADATA = ResourceRPCClientBase.Metadata()
DEFAULT_METADATA.enable_debug_logging


@pytest.fixture(scope="function")
def switch() -> Switch:
    _Switch = create_mock_subclass(Switch)
    return _Switch(name="switch")


@pytest.fixture(scope="function")
def manager(switch) -> ResourceManager:
    return ResourceManager([switch])


@pytest.fixture(scope="function")
def service(manager) -> SwitchRPCService:
    return SwitchRPCService(manager)


class TestService:
    pos = 2

    async def test_set_position(self, switch: Switch, service: SwitchRPCService):
        async with ChannelFor([service]) as channel:
            client = SwitchServiceStub(channel)
            request = SetPositionRequest(name=switch.name, position=self.pos, extra=dict_to_struct(DEFAULT_EXTRA))
            await client.SetPosition(request, timeout=DEFAULT_TIMEOUT, metadata=DEFAULT_METADATA.proto)
            cast(AsyncMock, switch.set_position).assert_called_once_with(
                position=self.pos, timeout=DEFAULT_TIMEOUT_APPROX, extra=DEFAULT_EXTRA, metadata=DEFAULT_METADATA.metadata
            )

    async def test_get_position(self, switch: Switch, service: SwitchRPCService):
        async with ChannelFor([service]) as channel:
            client = SwitchServiceStub(channel)
            request = GetPositionRequest(name=switch.name, extra=dict_to_struct(DEFAULT_EXTRA))
            await client.GetPosition(request, timeout=DEFAULT_TIMEOUT, metadata=DEFAULT_METADATA.proto)
            cast(AsyncMock, switch.get_position).assert_called_once_with(
                timeout=DEFAULT_TIMEOUT_APPROX, extra=DEFAULT_EXTRA, metadata=DEFAULT_METADATA.metadata
            )

    async def test_get_number_of_positions(self, switch: Switch, service: SwitchRPCService):
        async with ChannelFor([service]) as channel:
            cast(AsyncMock, switch.get_number_of_positions).return_value = (DEFAULT_NUMBER_OF_POSITIONS, DEFAULT_LABELS)
            client = SwitchServiceStub(channel)
            request = GetNumberOfPositionsRequest(name=switch.name, extra=dict_to_struct(DEFAULT_EXTRA))
            await client.GetNumberOfPositions(request, timeout=DEFAULT_TIMEOUT, metadata=DEFAULT_METADATA.proto)
            cast(AsyncMock, switch.get_number_of_positions).assert_called_once_with(
                timeout=DEFAULT_TIMEOUT_APPROX, extra=DEFAULT_EXTRA, metadata=DEFAULT_METADATA.metadata
            )

    async def test_do(self, switch: Switch, service: SwitchRPCService):
        async with ChannelFor([service]) as channel:
            command = {"command": "args"}
            request = DoCommandRequest(name=switch.name, command=dict_to_struct(command))
            client = SwitchServiceStub(channel)
            await client.DoCommand(request, timeout=DEFAULT_TIMEOUT, metadata=DEFAULT_METADATA.proto)
            cast(AsyncMock, switch.do_command).assert_called_once_with(
                command=command, timeout=DEFAULT_TIMEOUT_APPROX, metadata=DEFAULT_METADATA.metadata
            )


class TestClient:
    pos = 2

    async def test_set_position(self, switch: Switch, service: SwitchRPCService):
        async with ChannelFor([service]) as channel:
            client = SwitchClient(switch.name, channel)
            await client.set_position(position=self.pos, timeout=DEFAULT_TIMEOUT, extra=DEFAULT_EXTRA, metadata=DEFAULT_METADATA)
            cast(AsyncMock, switch.set_position).assert_called_once_with(
                position=self.pos, timeout=DEFAULT_TIMEOUT_APPROX, extra=DEFAULT_EXTRA, metadata=DEFAULT_METADATA.metadata
            )

    async def test_get_position(self, switch: Switch, service: SwitchRPCService):
        async with ChannelFor([service]) as channel:
            client = SwitchClient(switch.name, channel)
            await client.get_position(timeout=DEFAULT_TIMEOUT, extra=DEFAULT_EXTRA)
            cast(AsyncMock, switch.get_position).assert_called_once_with(
                timeout=DEFAULT_TIMEOUT_APPROX, extra=DEFAULT_EXTRA, metadata=DEFAULT_METADATA.metadata
            )

    async def test_get_number_of_positions(self, switch: Switch, service: SwitchRPCService):
        async with ChannelFor([service]) as channel:
            cast(AsyncMock, switch.get_number_of_positions).return_value = (DEFAULT_NUMBER_OF_POSITIONS, DEFAULT_LABELS)
            client = SwitchClient(switch.name, channel)
            await client.get_number_of_positions(timeout=DEFAULT_TIMEOUT, extra=DEFAULT_EXTRA)
            cast(AsyncMock, switch.get_number_of_positions).assert_called_once_with(
                timeout=DEFAULT_TIMEOUT_APPROX, extra=DEFAULT_EXTRA, metadata=DEFAULT_METADATA.metadata
            )

    async def test_do(self, switch: Switch, service: SwitchRPCService):
        async with ChannelFor([service]) as channel:
            client = SwitchClient(switch.name, channel)
            command = {"command": "args"}
            await client.do_command(command, timeout=DEFAULT_TIMEOUT, metadata=DEFAULT_METADATA)
            cast(AsyncMock, switch.do_command).assert_called_once_with(
                command=command, timeout=DEFAULT_TIMEOUT_APPROX, metadata=DEFAULT_METADATA.metadata
            )
