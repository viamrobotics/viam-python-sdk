from grpclib.testing import ChannelFor
import pytest

from viam.components.resource_manager import ResourceManager
from viam.components.servo import ServoBase, ServoService
from viam.proto.api.component.servo import (
    ServoServiceStub,
    MoveRequest,
    GetPositionRequest, GetPositionResponse
)


class MockServo(ServoBase):

    angle: int = 0

    async def move(self, angle: int):
        self.angle = angle

    async def get_position(self) -> int:
        return self.angle


class TestServo:

    servo = MockServo(name='servo')
    pos = 42

    @pytest.mark.asyncio
    async def test_get_position(self):
        await self.servo.move(self.pos)
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

    @pytest.mark.asyncio
    async def test_get_position(self):
        async with ChannelFor([self.service]) as channel:
            client = ServoServiceStub(channel)
            request = GetPositionRequest(name=self.name)
            response: GetPositionResponse = await client.GetPosition(request)
            assert response.position_deg == self.pos
