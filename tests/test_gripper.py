import pytest
from grpclib.testing import ChannelFor
from viam.components.gripper import Gripper, GripperClient, GripperService
from viam.components.resource_manager import ResourceManager
from viam.proto.api.component.gripper import (GrabRequest, GrabResponse,
                                              GripperServiceStub, OpenRequest)

from .mocks.components import MockGripper


@pytest.fixture(scope='function')
def gripper() -> MockGripper:
    return MockGripper('gripper')


@pytest.fixture(scope='function')
def service(gripper: Gripper) -> GripperService:
    rm = ResourceManager([gripper])
    return GripperService(rm)


class TestGripper:

    @pytest.mark.asyncio
    async def test_open(self, gripper: MockGripper):
        await gripper.open()
        assert gripper.opened is True

    @pytest.mark.asyncio
    async def test_grab(self, gripper: MockGripper):
        grabbed = await gripper.grab()
        assert gripper.opened is False
        assert isinstance(grabbed, bool)


class TestService:

    @pytest.mark.asyncio
    async def test_open(self, gripper: MockGripper, service: GripperService):
        async with ChannelFor([service]) as channel:
            client = GripperServiceStub(channel)
            request = OpenRequest(name=gripper.name)
            await client.Open(request)
            assert gripper.opened is True

    @pytest.mark.asyncio
    async def test_grab(self, gripper: MockGripper, service: GripperService):
        async with ChannelFor([service]) as channel:
            client = GripperServiceStub(channel)
            request = GrabRequest(name=gripper.name)
            response: GrabResponse = await client.Grab(request)
            assert gripper.opened is False
            assert isinstance(response.success, bool)


class TestClient:

    @pytest.mark.asyncio
    async def test_open(self, gripper: MockGripper, service: GripperService):
        async with ChannelFor([service]) as channel:
            client = GripperClient(gripper.name, channel)
            await client.open()
            assert gripper.opened is True

    @pytest.mark.asyncio
    async def test_grab(self, gripper: MockGripper, service: GripperService):
        async with ChannelFor([service]) as channel:
            client = GripperClient(gripper.name, channel)
            grabbed = await client.grab()
            assert gripper.opened is False
            assert isinstance(grabbed, bool)
