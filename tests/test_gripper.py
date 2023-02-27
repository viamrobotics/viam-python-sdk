import pytest
from grpclib.testing import ChannelFor

from viam.components.generic.service import GenericService
from viam.components.gripper import Gripper, GripperClient, create_status
from viam.components.gripper.service import GripperService
from viam.components.resource_manager import ResourceManager
from viam.proto.common import ActuatorStatus, DoCommandRequest, DoCommandResponse
from viam.proto.component.gripper import (
    GrabRequest,
    GrabResponse,
    GripperServiceStub,
    IsMovingRequest,
    IsMovingResponse,
    OpenRequest,
    StopRequest,
)
from viam.utils import dict_to_struct, struct_to_dict, message_to_struct

from . import loose_approx
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
        await gripper.open(timeout=1.82)
        assert gripper.opened is True
        assert gripper.timeout == loose_approx(1.82)

    @pytest.mark.asyncio
    async def test_grab(self, gripper: MockGripper):
        grabbed = await gripper.grab()
        assert gripper.opened is False
        assert isinstance(grabbed, bool)
        assert gripper.timeout is None

    @pytest.mark.asyncio
    async def test_stop(self, gripper: MockGripper):
        assert gripper.is_stopped is True
        await gripper.open()
        assert gripper.is_stopped is False
        await gripper.stop(timeout=7.86)
        assert gripper.is_stopped is True
        assert gripper.timeout == loose_approx(7.86)

    @pytest.mark.asyncio
    async def test_is_moving(self, gripper: MockGripper):
        await gripper.open()
        assert await gripper.is_moving()
        await gripper.stop()
        assert not await gripper.is_moving()

    @pytest.mark.asyncio
    async def test_do(self, gripper: MockGripper):
        resp = await gripper.do_command({"command": "args"})
        assert resp == {"hello": "world"}

    @pytest.mark.asyncio
    async def test_status(self, gripper: MockGripper):
        await gripper.open()
        status = await create_status(gripper)
        assert status.name == gripper.get_resource_name(gripper.name)
        assert status.status == message_to_struct(ActuatorStatus(is_moving=True))

    @pytest.mark.asyncio
    async def test_extra(self, gripper: MockGripper):
        assert gripper.extra is None
        extra = {"foo": "bar", "baz": [1, 2, 3]}
        await gripper.open(timeout=1.1, extra=extra)
        assert gripper.extra == extra


class TestService:
    @pytest.mark.asyncio
    async def test_open(self, gripper: MockGripper, service: GripperService):
        async with ChannelFor([service]) as channel:
            client = GripperServiceStub(channel)
            request = OpenRequest(name=gripper.name)
            await client.Open(request, timeout=1.23)
            assert gripper.opened is True
            assert gripper.timeout == loose_approx(1.23)

    @pytest.mark.asyncio
    async def test_grab(self, gripper: MockGripper, service: GripperService):
        async with ChannelFor([service]) as channel:
            client = GripperServiceStub(channel)
            request = GrabRequest(name=gripper.name)
            response: GrabResponse = await client.Grab(request, timeout=4.56)
            assert gripper.opened is False
            assert isinstance(response.success, bool)
            assert gripper.timeout == loose_approx(4.56)

    @pytest.mark.asyncio
    async def test_stop(self, gripper: MockGripper, service: GripperService):
        async with ChannelFor([service]) as channel:
            assert gripper.is_stopped is True

            client = GripperServiceStub(channel)
            request = OpenRequest(name=gripper.name)
            await client.Open(request)
            assert gripper.is_stopped is False

            request = StopRequest(name=gripper.name)
            await client.Stop(request, timeout=7.89)
            assert gripper.is_stopped is True
            assert gripper.timeout == loose_approx(7.89)

    @pytest.mark.asyncio
    async def test_is_moving(self, gripper: MockGripper, service: GripperService):
        async with ChannelFor([service]) as channel:
            assert gripper.is_stopped is True
            gripper.is_stopped = False
            client = GripperServiceStub(channel)
            request = IsMovingRequest(name=gripper.name)
            response: IsMovingResponse = await client.IsMoving(request)
            assert response.is_moving is True

    @pytest.mark.asyncio
    async def test_extra(self, gripper: MockGripper, service: GripperService):
        async with ChannelFor([service]) as channel:
            assert gripper.extra is None
            client = GripperServiceStub(channel)
            extra = {"foo": "bar", "baz": [1, 2, 3]}
            request = OpenRequest(name=gripper.name, extra=dict_to_struct(extra))
            await client.Open(request)
            assert gripper.extra == extra


class TestClient:
    @pytest.mark.asyncio
    async def test_open(self, gripper: MockGripper, service: GripperService):
        async with ChannelFor([service]) as channel:
            client = GripperClient(gripper.name, channel)
            await client.open(timeout=1.23)
            assert gripper.opened is True
            assert gripper.timeout == loose_approx(1.23)

    @pytest.mark.asyncio
    async def test_grab(self, gripper: MockGripper, service: GripperService):
        async with ChannelFor([service]) as channel:
            client = GripperClient(gripper.name, channel)
            grabbed = await client.grab(timeout=2.34)
            assert gripper.opened is False
            assert isinstance(grabbed, bool)
            assert gripper.timeout == loose_approx(2.34)

    @pytest.mark.asyncio
    async def test_stop(self, gripper: MockGripper, service: GripperService):
        async with ChannelFor([service]) as channel:
            client = GripperClient(gripper.name, channel)

            assert gripper.is_stopped is True
            await client.open()
            assert gripper.is_stopped is False
            await client.stop(timeout=3.45)
            assert gripper.is_stopped is True
            assert gripper.timeout == loose_approx(3.45)

    @pytest.mark.asyncio
    async def test_is_moving(self, gripper: MockGripper, service: GripperService):
        async with ChannelFor([service]) as channel:
            assert gripper.is_stopped is True
            gripper.is_stopped = False
            client = GripperClient(gripper.name, channel)
            assert await client.is_moving() is True

    @pytest.mark.asyncio
    async def test_do(self, gripper: MockGripper, service: GripperService):
        async with ChannelFor([service]) as channel:
            client = GripperClient(gripper.name, channel)
            resp = await client.do_command({"command": "args"})
            assert resp == {"hello": "world"}

    @pytest.mark.asyncio
    async def test_extra(self, gripper: MockGripper, service: GripperService):
        async with ChannelFor([service]) as channel:
            assert gripper.extra is None
            client = GripperClient(gripper.name, channel)
            extra = {"foo": "bar", "baz": [1, 2, 3]}
            await client.open(timeout=1.1, extra=extra)
            assert gripper.extra == extra
