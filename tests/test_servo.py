import pytest
from grpclib.testing import ChannelFor
from viam.components.resource_manager import ResourceManager
from viam.components.servo import ServoClient
from viam.components.servo.service import ServoService
from viam.proto.api.component.servo import (GetPositionRequest,
                                            GetPositionResponse, MoveRequest,
                                            ServoServiceStub)

from .mocks.components import MockServo


class TestServo:

    servo = MockServo(name='servo')
    pos = 42

    @pytest.mark.asyncio
    async def test_move(self):
        await self.servo.move(self.pos)
        assert self.servo.angle == self.pos

    @pytest.mark.asyncio
    async def test_get_position(self):
        new_pos = await self.servo.get_position()
        assert new_pos == self.pos


class TestService:

    name = 'servo'
    servo = MockServo(name=name)
    manager = ResourceManager([servo])
    service = ServoService(manager)
    pos = 42

    @pytest.mark.asyncio
    async def test_move(self):
        async with ChannelFor([self.service]) as channel:
            client = ServoServiceStub(channel)
            request = MoveRequest(name=self.name, angle_deg=self.pos)
            await client.Move(request)
            assert self.servo.angle == self.pos

    @pytest.mark.asyncio
    async def test_get_position(self):
        async with ChannelFor([self.service]) as channel:
            client = ServoServiceStub(channel)
            request = GetPositionRequest(name=self.name)
            response: GetPositionResponse = await client.GetPosition(request)
            assert response.position_deg == self.pos


class TestClient:

    name = 'servo'
    servo = MockServo(name=name)
    manager = ResourceManager([servo])
    service = ServoService(manager)
    pos = 42

    @pytest.mark.asyncio
    async def test_move(self):
        async with ChannelFor([self.service]) as channel:
            client = ServoClient(self.servo.name, channel)
            await client.move(self.pos)
            assert self.servo.angle == self.pos

    @pytest.mark.asyncio
    async def test_get_position(self):
        async with ChannelFor([self.service]) as channel:
            client = ServoClient(self.servo.name, channel)
            new_pos = await client.get_position()
            assert new_pos == self.pos
