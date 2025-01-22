import pytest
from grpclib.testing import ChannelFor

from viam.proto.app.robot import ComponentConfig
from viam.proto.common import (
    DoCommandRequest,
    DoCommandResponse,
)
from viam.proto.service.discovery import (
    DiscoverResourcesRequest,
    DiscoverResourcesResponse,
    DiscoveryServiceStub,
)
from viam.resource.manager import ResourceManager
from viam.services.discovery import DiscoveryClient
from viam.services.discovery.service import DiscoveryRPCService
from viam.utils import dict_to_struct, struct_to_dict

from .mocks.services import MockDiscovery

DISCOVERIES = [ComponentConfig()]


DISCOVERY_SERVICE_NAME = "discovery1"


@pytest.fixture(scope="function")
def discovery() -> MockDiscovery:
    return MockDiscovery(
        DISCOVERY_SERVICE_NAME,
    )


@pytest.fixture(scope="function")
def service(discovery: MockDiscovery) -> DiscoveryRPCService:
    rm = ResourceManager([discovery])
    return DiscoveryRPCService(rm)


class TestDiscovery:
    async def test_discover_resources(self, discovery: MockDiscovery):
        extra = {"foo": "discovery"}
        response = await discovery.discover_resources(extra=extra)
        assert discovery.extra == extra
        assert response == DISCOVERIES

    async def test_do(self, discovery: MockDiscovery):
        command = {"command": "args"}
        response = await discovery.do_command(command)
        assert response["cmd"] == command


class TestService:
    async def test_discover_resources(self, discovery: MockDiscovery, service: DiscoveryRPCService):
        async with ChannelFor([service]) as channel:
            client = DiscoveryServiceStub(channel)
            extra = {"cmd": "discovery"}
            request = DiscoverResourcesRequest(name=discovery.name, extra=dict_to_struct(extra))
            response: DiscoverResourcesResponse = await client.DiscoverResources(request)
            assert discovery.extra == extra
            assert response.discoveries == DISCOVERIES

    async def test_do(self, discovery: MockDiscovery, service: DiscoveryRPCService):
        async with ChannelFor([service]) as channel:
            client = DiscoveryServiceStub(channel)
            command = {"command": "args"}
            request = DoCommandRequest(name=discovery.name, command=dict_to_struct(command))
            response: DoCommandResponse = await client.DoCommand(request)
            assert struct_to_dict(response.result)["cmd"] == command


class TestClient:
    async def test_discover_resources(self, discovery: MockDiscovery, service: DiscoveryRPCService):
        async with ChannelFor([service]) as channel:
            client = DiscoveryClient(DISCOVERY_SERVICE_NAME, channel)
            extra = {"foo": "discovery"}
            response = await client.discover_resources(name=DISCOVERY_SERVICE_NAME, extra=extra)
            assert response == DISCOVERIES
            assert discovery.extra == extra

    async def test_do(self, service: DiscoveryRPCService):
        async with ChannelFor([service]) as channel:
            client = DiscoveryClient(DISCOVERY_SERVICE_NAME, channel)
            command = {"command": "args"}
            response = await client.do_command(command)
            assert response["cmd"] == command
