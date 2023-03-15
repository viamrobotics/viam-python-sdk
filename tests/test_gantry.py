import pytest
from grpclib.testing import ChannelFor

from viam.components.gantry import GantryClient, GantryStatus, create_status
from viam.components.gantry.service import GantryService
from viam.resource.manager import ResourceManager
from viam.proto.common import DoCommandRequest, DoCommandResponse
from viam.proto.component.gantry import (
    GantryServiceStub,
    GetLengthsRequest,
    GetLengthsResponse,
    GetPositionRequest,
    GetPositionResponse,
    IsMovingRequest,
    IsMovingResponse,
    MoveToPositionRequest,
    StopRequest,
)
from viam.utils import dict_to_struct, message_to_struct, struct_to_dict

from . import loose_approx
from .mocks.components import MockGantry


class TestGantry:
    gantry = MockGantry("gantry", [1, 2, 3], [4, 5, 6])

    @pytest.mark.asyncio
    async def test_get_position(self):
        pos = await self.gantry.get_position()
        assert pos == [1, 2, 3]

    @pytest.mark.asyncio
    async def test_move_to_position(self):
        await self.gantry.move_to_position([1, 8, 2])
        assert self.gantry.position == [1, 8, 2]

    @pytest.mark.asyncio
    async def test_get_lengths(self):
        lengths = await self.gantry.get_lengths()
        assert lengths == [4, 5, 6]

    @pytest.mark.asyncio
    async def test_do(self):
        command = {"command": "args"}
        resp = await self.gantry.do_command(command)
        assert resp == {"command": command}

    @pytest.mark.asyncio
    async def test_stop(self):
        assert self.gantry.is_stopped is False
        await self.gantry.stop()
        assert self.gantry.is_stopped is True

    @pytest.mark.asyncio
    async def test_is_moving(self):
        await self.gantry.move_to_position([1, 8, 2])
        assert await self.gantry.is_moving()
        await self.gantry.stop()
        assert not await self.gantry.is_moving()

    @pytest.mark.asyncio
    async def test_status(self):
        await self.gantry.move_to_position([1, 2, 3])
        status = await create_status(self.gantry)
        assert status.name == MockGantry.get_resource_name(self.gantry.name)
        assert status.status == message_to_struct(GantryStatus(lengths_mm=[4, 5, 6], positions_mm=[1, 2, 3], is_moving=True))

    @pytest.mark.asyncio
    async def test_extra(self):
        assert self.gantry.extra is None or len(self.gantry.extra) == 0
        extra = {"foo": "bar", "baz": [1, 2, 3]}
        await self.gantry.move_to_position([1, 2, 3], extra=extra)
        assert self.gantry.extra == extra

    @pytest.mark.asyncio
    async def test_timeout(self):
        assert self.gantry.timeout is None

        await self.gantry.get_position(timeout=5.5)
        assert self.gantry.timeout == loose_approx(5.5)

        await self.gantry.move_to_position([1, 2, 3], timeout=1.82)
        assert self.gantry.timeout == loose_approx(1.82)

        await self.gantry.get_lengths(timeout=7.86)
        assert self.gantry.timeout == loose_approx(7.86)

        await self.gantry.stop(timeout=4.4)
        assert self.gantry.timeout == loose_approx(4.4)


class TestService:
    @classmethod
    def setup_class(cls):
        cls.gantry = MockGantry("gantry", [1, 2, 3], [4, 5, 6])
        cls.manager = ResourceManager([cls.gantry])
        cls.service = GantryService(cls.manager)

    @pytest.mark.asyncio
    async def test_get_position(self):
        async with ChannelFor([self.service]) as channel:
            client = GantryServiceStub(channel)
            request = GetPositionRequest(name=self.gantry.name)
            response: GetPositionResponse = await client.GetPosition(request, timeout=9.87)
            assert list(response.positions_mm) == [1, 2, 3]
            assert self.gantry.timeout == loose_approx(9.87)

    @pytest.mark.asyncio
    async def test_move_to_position(self):
        async with ChannelFor([self.service]) as channel:
            client = GantryServiceStub(channel)
            request = MoveToPositionRequest(name=self.gantry.name, positions_mm=[1, 8, 2])
            await client.MoveToPosition(request, timeout=18.2)
            assert self.gantry.position == [1, 8, 2]
            assert self.gantry.timeout == loose_approx(18.2)

    @pytest.mark.asyncio
    async def test_get_lengths(self):
        async with ChannelFor([self.service]) as channel:
            client = GantryServiceStub(channel)
            request = GetLengthsRequest(name=self.gantry.name)
            response: GetLengthsResponse = await client.GetLengths(request, timeout=3.3)
            assert list(response.lengths_mm) == [4, 5, 6]
            assert self.gantry.timeout == loose_approx(3.3)

    @pytest.mark.asyncio
    async def test_stop(self):
        async with ChannelFor([self.service]) as channel:
            assert self.gantry.is_stopped is False
            client = GantryServiceStub(channel)
            request = StopRequest(name=self.gantry.name)
            await client.Stop(request, timeout=1.1)
            assert self.gantry.is_stopped is True
            assert self.gantry.timeout == loose_approx(1.1)

    @pytest.mark.asyncio
    async def test_is_moving(self):
        async with ChannelFor([self.service]) as channel:
            assert self.gantry.is_stopped is True
            self.gantry.is_stopped = False
            client = GantryServiceStub(channel)
            request = IsMovingRequest(name=self.gantry.name)
            response: IsMovingResponse = await client.IsMoving(request)
            assert response.is_moving is True

    @pytest.mark.asyncio
    async def test_extra(self):
        async with ChannelFor([self.service]) as channel:
            assert self.gantry.extra is None or len(self.gantry.extra) == 0
            client = GantryServiceStub(channel)
            extra = {"foo": "bar", "baz": [1, 2, 3]}
            request = StopRequest(name=self.gantry.name, extra=dict_to_struct(extra))
            await client.Stop(request)
            assert self.gantry.extra == extra

    @pytest.mark.asyncio
    async def test_do(self):
        async with ChannelFor([self.service]) as channel:
            client = GantryServiceStub(channel)
            command = {"command": "args"}
            request = DoCommandRequest(name=self.gantry.name, command=dict_to_struct(command))
            response: DoCommandResponse = await client.DoCommand(request)
            result = struct_to_dict(response.result)
            assert result == {"command": command}


class TestClient:
    @classmethod
    def setup_class(cls):
        cls.gantry = MockGantry("gantry", [1, 2, 3], [4, 5, 6])
        cls.manager = ResourceManager([cls.gantry])
        cls.service = GantryService(cls.manager)

    @pytest.mark.asyncio
    async def test_get_position(self):
        async with ChannelFor([self.service]) as channel:
            client = GantryClient(self.gantry.name, channel)
            pos = await client.get_position(timeout=1.82)
            assert pos == [1, 2, 3]
            assert self.gantry.timeout == loose_approx(1.82)

    @pytest.mark.asyncio
    async def test_move_to_position(self):
        async with ChannelFor([self.service]) as channel:
            client = GantryClient(self.gantry.name, channel)
            await client.move_to_position([1, 8, 2], timeout=4.4)
            assert self.gantry.position == [1, 8, 2]
            assert self.gantry.timeout == loose_approx(4.4)

    @pytest.mark.asyncio
    async def test_get_lengths(self):
        async with ChannelFor([self.service]) as channel:
            client = GantryClient(self.gantry.name, channel)
            lengths = await client.get_lengths(timeout=5.5)
            assert lengths == [4, 5, 6]
            assert self.gantry.timeout == loose_approx(5.5)

    @pytest.mark.asyncio
    async def test_do(self):
        async with ChannelFor([self.service]) as channel:
            client = GantryClient(self.gantry.name, channel)
            command = {"command": "args"}
            resp = await client.do_command(command)
            assert resp == {"command": command}

    @pytest.mark.asyncio
    async def test_stop(self):
        async with ChannelFor([self.service]) as channel:
            assert self.gantry.is_stopped is False
            client = GantryClient(self.gantry.name, channel)
            await client.stop(timeout=None)
            assert self.gantry.is_stopped is True
            assert self.gantry.timeout is None

    @pytest.mark.asyncio
    async def test_is_moving(self):
        async with ChannelFor([self.service]) as channel:
            assert self.gantry.is_stopped is True
            self.gantry.is_stopped = False
            client = GantryClient(self.gantry.name, channel)
            assert await client.is_moving() is True

    @pytest.mark.asyncio
    async def test_extra(self):
        async with ChannelFor([self.service]) as channel:
            assert self.gantry.extra is None or len(self.gantry.extra) == 0
            client = GantryClient(self.gantry.name, channel)
            extra = {"foo": "bar", "baz": [1, 2, 3]}
            await client.move_to_position([1, 2, 3], extra=extra)
            assert self.gantry.extra == extra
