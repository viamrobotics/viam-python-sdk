import pytest
from grpclib.testing import ChannelFor
from viam.components.generic.service import GenericService
from viam.components.motor import MotorClient, MotorStatus, create_status
from viam.components.motor.service import MotorService
from viam.components.resource_manager import ResourceManager
from viam.errors import NotSupportedError
from viam.proto.api.component.motor import (
    GetFeaturesRequest,
    GetFeaturesResponse,
    GetPositionRequest,
    GetPositionResponse,
    GoForRequest,
    GoToRequest,
    IsPoweredRequest,
    IsPoweredResponse,
    MotorServiceStub,
    ResetZeroPositionRequest,
    SetPowerRequest,
    StopRequest,
)
from viam.utils import dict_to_struct, message_to_struct

from .mocks.components import MockMotor


@pytest.fixture(scope="function")
def motor() -> MockMotor:
    return MockMotor(name="motor")


@pytest.fixture(scope="function")
def service(motor: MockMotor) -> MotorService:
    manager = ResourceManager([motor])
    return MotorService(manager)


@pytest.fixture(scope="function")
def generic_service(motor: MockMotor) -> GenericService:
    manager = ResourceManager([motor])
    return GenericService(manager)


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
        assert features.position_reporting is True

    @pytest.mark.asyncio
    async def test_stop(self, motor: MockMotor):
        await motor.set_power(10)
        assert motor.powered is True
        await motor.stop()
        assert motor.powered is False
        assert motor.power == 0

    @pytest.mark.asyncio
    async def test_is_powered(self, motor: MockMotor):
        await motor.set_power(10)
        is_powered = await motor.is_powered()
        assert is_powered is True

        await motor.set_power(0)
        is_powered = await motor.is_powered()
        assert is_powered is False

    @pytest.mark.asyncio
    async def test_is_moving(self, motor: MockMotor):
        await motor.set_power(10)
        assert await motor.is_moving()
        await motor.set_power(0)
        assert not await motor.is_moving()

    @pytest.mark.asyncio
    async def test_do(self, motor: MockMotor):
        with pytest.raises(NotImplementedError):
            await motor.do({"command": "args"})

    @pytest.mark.asyncio
    async def test_status(self, motor: MockMotor):
        await motor.set_power(10)
        status = await create_status(motor)
        assert status.name == motor.get_resource_name(motor.name)
        assert status.status == message_to_struct(MotorStatus(is_powered=True, position=0, position_reporting=True, is_moving=True))

    @pytest.mark.asyncio
    async def test_extra(self, motor: MockMotor):
        assert motor.extra is None
        extra = {"foo": "bar", "baz": [1, 2, 3]}
        await motor.is_powered(extra=extra)
        assert motor.extra == extra


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

            request = GoToRequest(name=motor.name, rpm=30, position_revolutions=20)
            await client.GoTo(request)
            assert motor.position == 20

            request = GoToRequest(name=motor.name, rpm=-10, position_revolutions=50)
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
    async def test_stop(self, motor: MockMotor, service: MotorService):
        async with ChannelFor([service]) as channel:
            client = MotorServiceStub(channel)
            request = StopRequest(name=motor.name)
            await client.Stop(request)
            assert motor.powered is False
            assert motor.power == 0

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

    @pytest.mark.asyncio
    async def test_extra(self, motor: MockMotor, service: MotorService):
        async with ChannelFor([service]) as channel:
            client = MotorServiceStub(channel)

            assert motor.extra is None
            extra = {"foo": "bar", "baz": [1, 2, 3]}
            request = IsPoweredRequest(name=motor.name, extra=dict_to_struct(extra))
            await client.IsPowered(request)
            assert motor.extra == extra


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
            assert features.position_reporting is True

    @pytest.mark.asyncio
    async def test_stop(self, motor: MockMotor, service: MotorService):
        async with ChannelFor([service]) as channel:
            client = MotorClient(motor.name, channel)
            await client.stop()
            assert motor.powered is False
            assert motor.power == 0

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

    @pytest.mark.asyncio
    async def test_is_moving(self, motor: MockMotor, service: MotorService):
        async with ChannelFor([service]) as channel:
            client = MotorClient(motor.name, channel)
            with pytest.raises(NotSupportedError):
                await client.is_moving()

    @pytest.mark.asyncio
    async def test_do(self, motor: MockMotor, service: MotorService, generic_service: GenericService):
        async with ChannelFor([service, generic_service]) as channel:
            client = MotorClient(motor.name, channel)
            with pytest.raises(NotImplementedError):
                await client.do({"command": "args"})

    @pytest.mark.asyncio
    async def test_status(self, motor: MockMotor, service: MotorService):
        async with ChannelFor([service]) as channel:
            client = MotorClient(motor.name, channel)
            with pytest.raises(NotSupportedError):
                await create_status(client)

    @pytest.mark.asyncio
    async def test_extra(self, motor: MockMotor, service: MotorService):
        async with ChannelFor([service]) as channel:
            client = MotorClient(motor.name, channel)

            assert motor.extra is None
            extra = {"foo": "bar", "baz": [1, 2, 3]}
            await client.is_powered(extra=extra)
            assert motor.extra == extra
