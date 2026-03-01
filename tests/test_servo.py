from grpclib.testing import ChannelFor

from viam.components.servo import ServoClient
from viam.components.servo.service import ServoRPCService
from viam.proto.common import DoCommandRequest, DoCommandResponse, GetGeometriesRequest, GetGeometriesResponse
from viam.proto.component.servo import (
    GetPositionRequest,
    GetPositionResponse,
    IsMovingRequest,
    IsMovingResponse,
    MoveRequest,
    ServoServiceStub,
    StopRequest,
)
from viam.resource.manager import ResourceManager
from viam.utils import dict_to_struct, struct_to_dict

from . import expected_grpc_timeout
from .mocks.components import GEOMETRIES, MockServo


class TestServo:
    servo = MockServo(name="servo")
    pos = 42

    async def test_move(self):
        await self.servo.move(self.pos, timeout=1.23, extra={"foo": "move"})
        assert self.servo.angle == self.pos
        assert self.servo.timeout == expected_grpc_timeout(1.23)
        assert self.servo.extra == {"foo": "move"}

    async def test_get_position(self):
        new_pos = await self.servo.get_position(timeout=2.34, extra={"foo": "get_position"})
        assert new_pos == self.pos
        assert self.servo.timeout == expected_grpc_timeout(2.34)
        assert self.servo.extra == {"foo": "get_position"}

    async def test_stop(self):
        assert self.servo.is_stopped is False
        await self.servo.stop(timeout=3.45, extra={"foo": "stop"})
        assert self.servo.is_stopped is True
        assert self.servo.timeout == expected_grpc_timeout(3.45)
        assert self.servo.extra == {"foo": "stop"}

    async def test_is_moving(self):
        await self.servo.move(self.pos)
        assert await self.servo.is_moving()
        await self.servo.stop()
        assert not await self.servo.is_moving()

    async def test_do(self):
        command = {"command": "args"}
        resp = await self.servo.do_command(command)
        assert resp == {"command": command}

    async def test_get_geometries(self):
        geometries = await self.servo.get_geometries()
        assert geometries == GEOMETRIES


class TestService:
    @classmethod
    def setup_class(cls):
        cls.name = "servo"
        cls.servo = MockServo(name=cls.name)
        cls.manager = ResourceManager([cls.servo])
        cls.service = ServoRPCService(cls.manager)
        cls.pos = 42

    async def test_move(self):
        async with ChannelFor([self.service]) as channel:
            client = ServoServiceStub(channel)
            request = MoveRequest(name=self.name, angle_deg=self.pos, extra=dict_to_struct({"foo": "move"}))
            await client.Move(request, timeout=1.23)
            assert self.servo.angle == self.pos
            assert self.servo.timeout == expected_grpc_timeout(1.23)
            assert self.servo.extra == {"foo": "move"}

    async def test_get_position(self):
        async with ChannelFor([self.service]) as channel:
            client = ServoServiceStub(channel)
            request = GetPositionRequest(name=self.name, extra=dict_to_struct({"foo": "get_position"}))
            response: GetPositionResponse = await client.GetPosition(request, timeout=2.34)
            assert response.position_deg == self.pos
            assert self.servo.timeout == expected_grpc_timeout(2.34)
            assert self.servo.extra == {"foo": "get_position"}

    async def test_stop(self):
        async with ChannelFor([self.service]) as channel:
            assert self.servo.is_stopped is False
            client = ServoServiceStub(channel)
            request = StopRequest(name=self.name, extra=dict_to_struct({"foo": "stop"}))
            await client.Stop(request, timeout=3.45)
            assert self.servo.is_stopped is True
            assert self.servo.timeout == expected_grpc_timeout(3.45)
            assert self.servo.extra == {"foo": "stop"}

    async def test_is_moving(self):
        async with ChannelFor([self.service]) as channel:
            assert self.servo.is_stopped is True
            self.servo.is_stopped = False
            client = ServoServiceStub(channel)
            request = IsMovingRequest(name=self.servo.name)
            response: IsMovingResponse = await client.IsMoving(request)
            assert response.is_moving is True

    async def test_do(self):
        async with ChannelFor([self.service]) as channel:
            client = ServoServiceStub(channel)
            command = {"command": "args"}
            request = DoCommandRequest(name=self.name, command=dict_to_struct(command))
            response: DoCommandResponse = await client.DoCommand(request)
            result = struct_to_dict(response.result)
            assert result == {"command": command}

    async def test_get_geometries(self):
        async with ChannelFor([self.service]) as channel:
            client = ServoServiceStub(channel)
            request = GetGeometriesRequest(name=self.servo.name)
            response: GetGeometriesResponse = await client.GetGeometries(request)
            assert [geometry for geometry in response.geometries] == GEOMETRIES


class TestClient:
    @classmethod
    def setup_class(cls):
        cls.name = "servo"
        cls.servo = MockServo(name=cls.name)
        cls.manager = ResourceManager([cls.servo])
        cls.service = ServoRPCService(cls.manager)
        cls.pos = 42

    async def test_move(self):
        async with ChannelFor([self.service]) as channel:
            client = ServoClient(self.servo.name, channel)
            await client.move(self.pos, timeout=1.23, extra={"foo": "move"})
            assert self.servo.angle == self.pos
            assert self.servo.timeout == expected_grpc_timeout(1.23)
            assert self.servo.extra == {"foo": "move"}

    async def test_get_position(self):
        async with ChannelFor([self.service]) as channel:
            client = ServoClient(self.servo.name, channel)
            new_pos = await client.get_position(timeout=2.34, extra={"foo": "get_position"})
            assert new_pos == self.pos
            assert self.servo.timeout == expected_grpc_timeout(2.34)
            assert self.servo.extra == {"foo": "get_position"}

    async def test_stop(self):
        async with ChannelFor([self.service]) as channel:
            assert self.servo.is_stopped is False
            client = ServoClient(self.name, channel)
            await client.stop(timeout=3.45, extra={"foo": "stop"})
            assert self.servo.is_stopped is True
            assert self.servo.timeout == expected_grpc_timeout(3.45)
            assert self.servo.extra == {"foo": "stop"}

    async def test_is_moving(self):
        async with ChannelFor([self.service]) as channel:
            client = ServoClient(self.name, channel)
            assert self.servo.is_stopped is True
            self.servo.is_stopped = False
            assert await client.is_moving() is True

    async def test_do(self):
        async with ChannelFor([self.service]) as channel:
            client = ServoClient(self.name, channel)
            command = {"command": "args"}
            resp = await client.do_command(command)
            assert resp == {"command": command}

    async def test_get_geometries(self):
        async with ChannelFor([self.service]) as channel:
            client = ServoClient(self.name, channel)
            geometries = await client.get_geometries()
            assert geometries == GEOMETRIES
