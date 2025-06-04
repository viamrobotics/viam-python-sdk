import pytest
from grpclib.testing import ChannelFor

from viam.components.generic.service import GenericRPCService
from viam.components.gripper import Gripper, GripperClient, KinematicsFileFormat
from viam.components.gripper.service import GripperRPCService
from viam.proto.common import (
    DoCommandRequest,
    DoCommandResponse,
    GetGeometriesRequest,
    GetGeometriesResponse,
    GetKinematicsRequest,
    GetKinematicsResponse,
)
from viam.proto.component.gripper import (
    GrabRequest,
    GrabResponse,
    GripperServiceStub,
    IsMovingRequest,
    IsMovingResponse,
    OpenRequest,
    StopRequest,
)
from viam.resource.manager import ResourceManager
from viam.utils import dict_to_struct, struct_to_dict

from . import loose_approx
from .mocks.components import GEOMETRIES, MockGripper


@pytest.fixture(scope="function")
def gripper() -> MockGripper:
    return MockGripper("gripper")


@pytest.fixture(scope="function")
def service(gripper: Gripper) -> GripperRPCService:
    rm = ResourceManager([gripper])
    return GripperRPCService(rm)


@pytest.fixture(scope="function")
def generic_service(gripper: Gripper) -> GenericRPCService:
    manager = ResourceManager([gripper])
    return GenericRPCService(manager)


class TestGripper:
    async def test_open(self, gripper: MockGripper):
        await gripper.open(timeout=1.82)
        assert gripper.opened is True
        assert gripper.timeout == loose_approx(1.82)

    async def test_grab(self, gripper: MockGripper):
        grabbed = await gripper.grab()
        assert gripper.opened is False
        assert isinstance(grabbed, bool)
        assert gripper.timeout is None

    async def test_stop(self, gripper: MockGripper):
        assert gripper.is_stopped is True
        await gripper.open()
        assert gripper.is_stopped is False
        await gripper.stop(timeout=7.86)
        assert gripper.is_stopped is True
        assert gripper.timeout == loose_approx(7.86)

    async def test_is_moving(self, gripper: MockGripper):
        await gripper.open()
        assert await gripper.is_moving()
        await gripper.stop()
        assert not await gripper.is_moving()

    async def test_do(self, gripper: MockGripper):
        command = {"command": "args"}
        resp = await gripper.do_command(command)
        assert resp == {"command": command}

    async def test_extra(self, gripper: MockGripper):
        assert gripper.extra is None
        extra = {"foo": "bar", "baz": [1, 2, 3]}
        await gripper.open(timeout=1.1, extra=extra)
        assert gripper.extra == extra

    async def test_get_geometries(self, gripper: MockGripper):
        geometries = await gripper.get_geometries()
        assert geometries == GEOMETRIES

    async def test_get_kinematics(self, gripper: MockGripper):
        kinematics = (KinematicsFileFormat.KINEMATICS_FILE_FORMAT_SVA, b"\x00\x01\x02")
        kd = await gripper.get_kinematics(extra={"1": "2"})
        assert kd == kinematics
        assert gripper.extra == {"1": "2"}

class TestService:
    async def test_open(self, gripper: MockGripper, service: GripperRPCService):
        async with ChannelFor([service]) as channel:
            client = GripperServiceStub(channel)
            request = OpenRequest(name=gripper.name)
            await client.Open(request, timeout=1.23)
            assert gripper.opened is True
            assert gripper.timeout == loose_approx(1.23)

    async def test_grab(self, gripper: MockGripper, service: GripperRPCService):
        async with ChannelFor([service]) as channel:
            client = GripperServiceStub(channel)
            request = GrabRequest(name=gripper.name)
            response: GrabResponse = await client.Grab(request, timeout=4.56)
            assert gripper.opened is False
            assert isinstance(response.success, bool)
            assert gripper.timeout == loose_approx(4.56)

    async def test_stop(self, gripper: MockGripper, service: GripperRPCService):
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

    async def test_is_moving(self, gripper: MockGripper, service: GripperRPCService):
        async with ChannelFor([service]) as channel:
            assert gripper.is_stopped is True
            gripper.is_stopped = False
            client = GripperServiceStub(channel)
            request = IsMovingRequest(name=gripper.name)
            response: IsMovingResponse = await client.IsMoving(request)
            assert response.is_moving is True

    async def test_extra(self, gripper: MockGripper, service: GripperRPCService):
        async with ChannelFor([service]) as channel:
            assert gripper.extra is None
            client = GripperServiceStub(channel)
            extra = {"foo": "bar", "baz": [1, 2, 3]}
            request = OpenRequest(name=gripper.name, extra=dict_to_struct(extra))
            await client.Open(request)
            assert gripper.extra == extra

    async def test_do(self, gripper: MockGripper, service: GripperRPCService):
        async with ChannelFor([service]) as channel:
            client = GripperServiceStub(channel)
            command = {"command": "args"}
            request = DoCommandRequest(name=gripper.name, command=dict_to_struct(command))
            response: DoCommandResponse = await client.DoCommand(request)
            result = struct_to_dict(response.result)
            assert result == {"command": command}

    async def test_get_geometries(self, gripper: MockGripper, service: GripperRPCService):
        async with ChannelFor([service]) as channel:
            client = GripperServiceStub(channel)
            request = GetGeometriesRequest(name=gripper.name)
            response: GetGeometriesResponse = await client.GetGeometries(request)
            assert [geometry for geometry in response.geometries] == GEOMETRIES

    async def test_get_kinematics(self, gripper: MockGripper, service: GripperRPCService):
        async with ChannelFor([service]) as channel:
            client = GripperServiceStub(channel)
            kinematics = (KinematicsFileFormat.KINEMATICS_FILE_FORMAT_SVA, b"\x00\x01\x02")
            request = GetKinematicsRequest(name=gripper.name)
            response: GetKinematicsResponse = await client.GetKinematics(request)
            assert (response.format, response.kinematics_data) == kinematics

class TestClient:
    async def test_open(self, gripper: MockGripper, service: GripperRPCService):
        async with ChannelFor([service]) as channel:
            client = GripperClient(gripper.name, channel)
            await client.open(timeout=1.23)
            assert gripper.opened is True
            assert gripper.timeout == loose_approx(1.23)

    async def test_grab(self, gripper: MockGripper, service: GripperRPCService):
        async with ChannelFor([service]) as channel:
            client = GripperClient(gripper.name, channel)
            grabbed = await client.grab(timeout=2.34)
            assert gripper.opened is False
            assert isinstance(grabbed, bool)
            assert gripper.timeout == loose_approx(2.34)

    async def test_stop(self, gripper: MockGripper, service: GripperRPCService):
        async with ChannelFor([service]) as channel:
            client = GripperClient(gripper.name, channel)

            assert gripper.is_stopped is True
            await client.open()
            assert gripper.is_stopped is False
            await client.stop(timeout=3.45)
            assert gripper.is_stopped is True
            assert gripper.timeout == loose_approx(3.45)

    async def test_is_moving(self, gripper: MockGripper, service: GripperRPCService):
        async with ChannelFor([service]) as channel:
            assert gripper.is_stopped is True
            gripper.is_stopped = False
            client = GripperClient(gripper.name, channel)
            assert await client.is_moving() is True

    async def test_do(self, gripper: MockGripper, service: GripperRPCService):
        async with ChannelFor([service]) as channel:
            client = GripperClient(gripper.name, channel)
            command = {"command": "args"}
            resp = await client.do_command(command)
            assert resp == {"command": command}

    async def test_extra(self, gripper: MockGripper, service: GripperRPCService):
        async with ChannelFor([service]) as channel:
            assert gripper.extra is None
            client = GripperClient(gripper.name, channel)
            extra = {"foo": "bar", "baz": [1, 2, 3]}
            await client.open(timeout=1.1, extra=extra)
            assert gripper.extra == extra

    async def test_get_geometries(self, gripper: MockGripper, service: GripperRPCService):
        async with ChannelFor([service]) as channel:
            client = GripperClient(gripper.name, channel)
            geometries = await client.get_geometries()
            assert geometries == GEOMETRIES

    async def test_get_kinematics(self, gripper: MockGripper, service: GripperRPCService):
        async with ChannelFor([service]) as channel:
            client = GripperClient(gripper.name, channel)
            kinematics = (KinematicsFileFormat.KINEMATICS_FILE_FORMAT_SVA, b"\x00\x01\x02")
            kd = await client.get_kinematics(extra={"1": "2"})
            assert kd == kinematics
            assert gripper.extra == {"1": "2"}
