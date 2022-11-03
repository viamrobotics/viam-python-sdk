import pytest
from grpclib.testing import ChannelFor

from viam.components.generic.service import GenericService
from viam.components.resource_manager import ResourceManager
from viam.components.servo import ServoClient, ServoStatus, create_status
from viam.components.servo.service import ServoService
from viam.errors import NotSupportedError
from viam.proto.component.servo import (
    GetPositionRequest,
    GetPositionResponse,
    MoveRequest,
    ServoServiceStub,
    StopRequest,
)
from viam.utils import message_to_struct

from . import loose_approx
from .mocks.components import MockServo


class TestServo:

    servo = MockServo(name="servo")
    pos = 42

    @pytest.mark.asyncio
    async def test_move(self):
        await self.servo.move(self.pos, timeout=1.23)
        assert self.servo.angle == self.pos
        assert self.servo.timeout == loose_approx(1.23)

    @pytest.mark.asyncio
    async def test_get_position(self):
        new_pos = await self.servo.get_position(timeout=2.34)
        assert new_pos == self.pos
        assert self.servo.timeout == loose_approx(2.34)

    @pytest.mark.asyncio
    async def test_stop(self):
        assert self.servo.is_stopped is False
        await self.servo.stop(timeout=3.45)
        assert self.servo.is_stopped is True
        assert self.servo.timeout == loose_approx(3.45)

    @pytest.mark.asyncio
    async def test_is_moving(self):
        await self.servo.move(self.pos)
        assert await self.servo.is_moving()
        await self.servo.stop()
        assert not await self.servo.is_moving()

    @pytest.mark.asyncio
    async def test_do(self):
        with pytest.raises(NotImplementedError):
            await self.servo.do_command({"command": "args"})

    @pytest.mark.asyncio
    async def test_status(self):
        await self.servo.move(self.pos)
        status = await create_status(self.servo)
        assert status.name == self.servo.get_resource_name(self.servo.name)
        assert status.status == message_to_struct(ServoStatus(position_deg=self.pos, is_moving=True))


class TestService:

    name = "servo"
    servo = MockServo(name=name)
    manager = ResourceManager([servo])
    service = ServoService(manager)
    pos = 42

    @pytest.mark.asyncio
    async def test_move(self):
        async with ChannelFor([self.service]) as channel:
            client = ServoServiceStub(channel)
            request = MoveRequest(name=self.name, angle_deg=self.pos)
            await client.Move(request, timeout=1.23)
            assert self.servo.angle == self.pos
            assert self.servo.timeout == loose_approx(1.23)

    @pytest.mark.asyncio
    async def test_get_position(self):
        async with ChannelFor([self.service]) as channel:
            client = ServoServiceStub(channel)
            request = GetPositionRequest(name=self.name)
            response: GetPositionResponse = await client.GetPosition(request, timeout=2.34)
            assert response.position_deg == self.pos
            assert self.servo.timeout == loose_approx(2.34)

    @pytest.mark.asyncio
    async def test_stop(self):
        async with ChannelFor([self.service]) as channel:
            assert self.servo.is_stopped is False
            client = ServoServiceStub(channel)
            request = StopRequest(name=self.name)
            await client.Stop(request, timeout=3.45)
            assert self.servo.is_stopped is True
            assert self.servo.timeout == loose_approx(3.45)


class TestClient:

    name = "servo"
    servo = MockServo(name=name)
    manager = ResourceManager([servo])
    service = ServoService(manager)
    pos = 42

    @pytest.mark.asyncio
    async def test_move(self):
        async with ChannelFor([self.service]) as channel:
            client = ServoClient(self.servo.name, channel)
            await client.move(self.pos, timeout=1.23)
            assert self.servo.angle == self.pos
            assert self.servo.timeout == loose_approx(1.23)

    @pytest.mark.asyncio
    async def test_get_position(self):
        async with ChannelFor([self.service]) as channel:
            client = ServoClient(self.servo.name, channel)
            new_pos = await client.get_position(timeout=2.34)
            assert new_pos == self.pos
            assert self.servo.timeout == loose_approx(2.34)

    @pytest.mark.asyncio
    async def test_stop(self):
        async with ChannelFor([self.service]) as channel:
            assert self.servo.is_stopped is False
            client = ServoClient(self.name, channel)
            await client.stop(timeout=3.45)
            assert self.servo.is_stopped is True
            assert self.servo.timeout == loose_approx(3.45)

    @pytest.mark.asyncio
    async def test_is_moving(self):
        async with ChannelFor([self.service]) as channel:
            client = ServoClient(self.name, channel)
            with pytest.raises(NotSupportedError):
                await client.is_moving()

    @pytest.mark.asyncio
    async def test_do(self):
        async with ChannelFor([self.service, GenericService(self.manager)]) as channel:
            client = ServoClient(self.name, channel)
            with pytest.raises(NotImplementedError):
                await client.do_command({"command": "args"})

    @pytest.mark.asyncio
    async def test_status(self):
        async with ChannelFor([self.service]) as channel:
            client = ServoClient(self.name, channel)
            with pytest.raises(NotSupportedError):
                await create_status(client)
