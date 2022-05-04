import pytest
from grpclib.testing import ChannelFor
from viam.components.generic.service import GenericService
from viam.components.gripper import Gripper, GripperClient
from viam.components.gripper.service import GripperService
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


@pytest.fixture(scope='function')
def generic_service(gripper: Gripper) -> GenericService:
    manager = ResourceManager([gripper])
    return GenericService(manager)


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

    @pytest.mark.asyncio
    async def test_do(self, gripper: MockGripper):
        with pytest.raises(NotImplementedError):
            await gripper.do({'command': 'args'})


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

    @pytest.mark.asyncio
    async def test_do(self, gripper: MockGripper, service: GripperService, generic_service: GenericService):
        async with ChannelFor([service, generic_service]) as channel:
            client = GripperClient(gripper.name, channel)
            with pytest.raises(NotImplementedError):
                await client.do({'command': 'args'})
