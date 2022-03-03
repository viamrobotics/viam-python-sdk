from grpclib.testing import ChannelFor
import pytest

from viam.components.resource_manager import ResourceManager
from viam.components.motor import MotorService, MotorClient
from viam.proto.api.component.motor import (
    MotorServiceStub,
    SetPowerRequest,
    GoForRequest,
    GoToRequest,
    ResetZeroPositionRequest,
    GetPositionRequest, GetPositionResponse,
    GetFeaturesRequest, GetFeaturesResponse,
    IsPoweredRequest, IsPoweredResponse,
)

from .mocks.components import MockMotor


@pytest.fixture(scope='function')
def motor() -> MockMotor:
    return MockMotor(name='motor')


@pytest.fixture(scope='function')
def service(motor: MockMotor) -> MotorService:
    manager = ResourceManager([motor])
    return MotorService(manager)


class TestMotor:

    @pytest.mark.asyncio
    async def test_set_power(self, motor: MockMotor):
        power = 0.32
        await motor.set_power(power)
        assert motor.power == power

    @pytest.mark.asyncio
    async def test_get_position(self, motor: MockMotor):
        pos = await motor.get_position()
        assert pos == 0

    @pytest.mark.asyncio
    async def test_go_for(self, motor: MockMotor):
        await motor.go_for(30, 20)
        assert await motor.get_position() == 20

        await motor.go_for(-10, 10)
        assert await motor.get_position() == 10

        await motor.go_for(10, -5)
        assert await motor.get_position() == 5

        await motor.go_for(-10, -10)
        assert await motor.get_position() == 15

    @pytest.mark.asyncio
    async def test_go_to(self, motor: MockMotor):
        await motor.go_to(30, 20)
        assert await motor.get_position() == 20

        await motor.go_to(-10, 50)
        assert await motor.get_position() == 50

    @pytest.mark.asyncio
    async def test_reset_zero(self, motor: MockMotor):
        await motor.reset_zero_position(20)
        assert motor.offset == 20

    @pytest.mark.asyncio
    async def test_get_features(self, motor: MockMotor):
        features = await motor.get_features()
        assert features['position_reporting'] is True

    @pytest.mark.asyncio
    async def test_is_powered(self, motor: MockMotor):
        await motor.set_power(10)
        is_powered = await motor.is_powered()
        assert is_powered is True

        await motor.set_power(0)
        is_powered = await motor.is_powered()
        assert is_powered is False


class TestService:

    @pytest.mark.asyncio
    async def test_set_power(self, motor: MockMotor, service: MotorService):
        async with ChannelFor([service]) as channel:
            client = MotorServiceStub(channel)
            request = SetPowerRequest(name=motor.name, power_pct=13)
            await client.SetPower(request)
            assert motor.power == 13

    @pytest.mark.asyncio
    async def test_get_position(self, motor: MockMotor, service: MotorService):
        async with ChannelFor([service]) as channel:
            client = MotorServiceStub(channel)
            request = GetPositionRequest(name=motor.name)
            response: GetPositionResponse = await client.GetPosition(request)
            assert response.position == 0

    @pytest.mark.asyncio
    async def test_go_for(self, motor: MockMotor, service: MotorService):
        async with ChannelFor([service]) as channel:
            client = MotorServiceStub(channel)

            request = GoForRequest(name=motor.name, rpm=30, revolutions=20)
            await client.GoFor(request)
            assert motor.position == 20

            request = GoForRequest(name=motor.name, rpm=-10, revolutions=10)
            await client.GoFor(request)
            assert motor.position == 10

            request = GoForRequest(name=motor.name, rpm=10, revolutions=-5)
            await client.GoFor(request)
            assert motor.position == 5

            request = GoForRequest(name=motor.name, rpm=-10, revolutions=-10)
            await client.GoFor(request)
            assert motor.position == 15

    @pytest.mark.asyncio
    async def test_go_to(self, motor: MockMotor, service: MotorService):
        async with ChannelFor([service]) as channel:
            client = MotorServiceStub(channel)

            request = GoToRequest(
                name=motor.name,
                rpm=30,
                position_revolutions=20
            )
            await client.GoTo(request)
            assert motor.position == 20

            request = GoToRequest(
                name=motor.name,
                rpm=-10,
                position_revolutions=50
            )
            await client.GoTo(request)
            assert motor.position == 50

    @pytest.mark.asyncio
    async def test_reset_zero(self, motor: MockMotor, service: MotorService):
        async with ChannelFor([service]) as channel:
            client = MotorServiceStub(channel)
            request = ResetZeroPositionRequest(name=motor.name, offset=20)
            await client.ResetZeroPosition(request)
            assert motor.offset == 20

    @pytest.mark.asyncio
    async def test_get_features(self, motor: MockMotor, service: MotorService):
        async with ChannelFor([service]) as channel:
            client = MotorServiceStub(channel)
            request = GetFeaturesRequest(name=motor.name)
            response: GetFeaturesResponse = await client.GetFeatures(request)
            assert response.position_reporting is True

    @pytest.mark.asyncio
    async def test_is_powered(self, motor: MockMotor, service: MotorService):
        async with ChannelFor([service]) as channel:
            client = MotorServiceStub(channel)

            sp_request = SetPowerRequest(name=motor.name, power_pct=13)
            await client.SetPower(sp_request)
            request = IsPoweredRequest(name=motor.name)
            response: IsPoweredResponse = await client.IsPowered(request)
            assert response.is_on is True

            sp_request = SetPowerRequest(name=motor.name, power_pct=0)
            await client.SetPower(sp_request)
            request = IsPoweredRequest(name=motor.name)
            response: IsPoweredResponse = await client.IsPowered(request)
            assert response.is_on is False


class TestClient:

    @pytest.mark.asyncio
    async def test_set_power(self, motor: MockMotor, service: MotorService):
        async with ChannelFor([service]) as channel:
            client = MotorClient(motor.name, channel)
            await client.set_power(13)
            assert motor.power == 13

    @pytest.mark.asyncio
    async def test_get_position(self, motor: MockMotor, service: MotorService):
        async with ChannelFor([service]) as channel:
            client = MotorClient(motor.name, channel)
            position = await client.get_position()
            assert position == 0

    @pytest.mark.asyncio
    async def test_go_for(self, motor: MockMotor, service: MotorService):
        async with ChannelFor([service]) as channel:
            client = MotorClient(motor.name, channel)

            await client.go_for(30, 20)
            assert motor.position == 20

            await client.go_for(-10, 10)
            assert motor.position == 10

            await client.go_for(10, -5)
            assert motor.position == 5

            await client.go_for(-10, -10)
            assert motor.position == 15

    @pytest.mark.asyncio
    async def test_go_to(self, motor: MockMotor, service: MotorService):
        async with ChannelFor([service]) as channel:
            client = MotorClient(motor.name, channel)

            await client.go_to(30, 20)
            assert motor.position == 20

            await client.go_to(-10, 50)
            assert motor.position == 50

    @pytest.mark.asyncio
    async def test_reset_zero(self, motor: MockMotor, service: MotorService):
        async with ChannelFor([service]) as channel:
            client = MotorClient(motor.name, channel)
            await client.reset_zero_position(20)
            assert motor.offset == 20

    @pytest.mark.asyncio
    async def test_get_features(self, motor: MockMotor, service: MotorService):
        async with ChannelFor([service]) as channel:
            client = MotorClient(motor.name, channel)
            features = await client.get_features()
            assert features['position_reporting'] is True

    @pytest.mark.asyncio
    async def test_is_powered(self, motor: MockMotor, service: MotorService):
        async with ChannelFor([service]) as channel:
            client = MotorClient(motor.name, channel)

            await client.set_power(13)
            is_on = await client.is_powered()
            assert is_on is True

            await client.set_power(0)
            is_on = await client.is_powered()
            assert is_on is False
