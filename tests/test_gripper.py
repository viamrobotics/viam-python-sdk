import pytest
from grpclib.testing import ChannelFor

from viam.components.generic.service import GenericService
from viam.components.gripper import Gripper, GripperClient, create_status
from viam.components.gripper.service import GripperService
from viam.components.resource_manager import ResourceManager
from viam.errors import NotSupportedError
from viam.proto.common import ActuatorStatus
from viam.proto.component.gripper import (
    GrabRequest,
    GrabResponse,
    GripperServiceStub,
    OpenRequest,
    StopRequest,
)
from viam.utils import message_to_struct

from .mocks.components import MockGripper


@pytest.fixture(scope="function")
def gripper() -> MockGripper:
    return MockGripper("gripper")


@pytest.fixture(scope="function")
def service(gripper: Gripper) -> GripperService:
    rm = ResourceManager([gripper])
    return GripperService(rm)


@pytest.fixture(scope="function")
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
    async def test_stop(self, gripper: MockGripper):
        assert gripper.is_stopped is True
        await gripper.open()
        assert gripper.is_stopped is False
        await gripper.stop()
        assert gripper.is_stopped is True

    @pytest.mark.asyncio
    async def test_is_moving(self, gripper: MockGripper):
        await gripper.open()
        assert await gripper.is_moving()
        await gripper.stop()
        assert not await gripper.is_moving()

    @pytest.mark.asyncio
    async def test_do(self, gripper: MockGripper):
        with pytest.raises(NotImplementedError):
            await gripper.do_command({"command": "args"})

    @pytest.mark.asyncio
    async def test_status(self, gripper: MockGripper):
        await gripper.open()
        status = await create_status(gripper)
        assert status.name == gripper.get_resource_name(gripper.name)
        assert status.status == message_to_struct(ActuatorStatus(is_moving=True))


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

    @pytest.mark.asyncio
    async def test_stop(self, gripper: MockGripper, service: GripperService):
        async with ChannelFor([service]) as channel:
            assert gripper.is_stopped is True

            client = GripperServiceStub(channel)
            request = OpenRequest(name=gripper.name)
            await client.Open(request)
            assert gripper.is_stopped is False

            request = StopRequest(name=gripper.name)
            await client.Stop(request)
            assert gripper.is_stopped is True


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
    async def test_stop(self, gripper: MockGripper, service: GripperService):
        async with ChannelFor([service]) as channel:
            client = GripperClient(gripper.name, channel)

            assert gripper.is_stopped is True
            await client.open()
            assert gripper.is_stopped is False
            await client.stop()
            assert gripper.is_stopped is True

    @pytest.mark.asyncio
    async def test_is_moving(self, gripper: MockGripper, service: GripperService):
        async with ChannelFor([service]) as channel:
            client = GripperClient(gripper.name, channel)
            with pytest.raises(NotSupportedError):
                await client.is_moving()

    @pytest.mark.asyncio
    async def test_do(self, gripper: MockGripper, service: GripperService, generic_service: GenericService):
        async with ChannelFor([service, generic_service]) as channel:
            client = GripperClient(gripper.name, channel)
            with pytest.raises(NotImplementedError):
                await client.do_command({"command": "args"})

    @pytest.mark.asyncio
    async def test_status(self, gripper: MockGripper, service: GripperService):
        async with ChannelFor([service]) as channel:
            client = GripperClient(gripper.name, channel)
            with pytest.raises(NotSupportedError):
                await create_status(client)
