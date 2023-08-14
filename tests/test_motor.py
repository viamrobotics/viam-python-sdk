import pytest
from grpclib.testing import ChannelFor

from viam.components.generic.service import GenericRPCService
from viam.components.motor import MotorClient, MotorStatus, create_status
from viam.components.motor.service import MotorRPCService
from viam.proto.common import DoCommandRequest, DoCommandResponse, GetGeometriesRequest, GetGeometriesResponse
from viam.proto.component.motor import (
    GetPositionRequest,
    GetPositionResponse,
    GetPropertiesRequest,
    GetPropertiesResponse,
    GoForRequest,
    GoToRequest,
    IsMovingRequest,
    IsMovingResponse,
    IsPoweredRequest,
    IsPoweredResponse,
    MotorServiceStub,
    ResetZeroPositionRequest,
    SetPowerRequest,
    StopRequest,
)
from viam.resource.manager import ResourceManager
from viam.utils import dict_to_struct, message_to_struct, struct_to_dict

from . import loose_approx
from .mocks.components import GEOMETRIES, MockMotor


@pytest.fixture(scope="function")
def motor() -> MockMotor:
    return MockMotor(name="motor")


@pytest.fixture(scope="function")
def service(motor: MockMotor) -> MotorRPCService:
    manager = ResourceManager([motor])
    return MotorRPCService(manager)


@pytest.fixture(scope="function")
def generic_service(motor: MockMotor) -> GenericRPCService:
    manager = ResourceManager([motor])
    return GenericRPCService(manager)


class TestMotor:
    @pytest.mark.asyncio
    async def test_set_power(self, motor: MockMotor):
        power = 0.32
        await motor.set_power(power, timeout=1.23)
        assert motor.power == power
        assert motor.timeout == loose_approx(1.23)

    @pytest.mark.asyncio
    async def test_get_position(self, motor: MockMotor):
        pos = await motor.get_position(timeout=2.34)
        assert pos == 0
        assert motor.timeout == loose_approx(2.34)

    @pytest.mark.asyncio
    async def test_go_for(self, motor: MockMotor):
        await motor.go_for(30, 20, timeout=3.45)
        assert motor.timeout == loose_approx(3.45)
        assert await motor.get_position() == 20

        await motor.go_for(-10, 10)
        assert await motor.get_position() == 10

        await motor.go_for(10, -5)
        assert await motor.get_position() == 5

        await motor.go_for(-10, -10)
        assert await motor.get_position() == 15

    @pytest.mark.asyncio
    async def test_go_to(self, motor: MockMotor):
        await motor.go_to(30, 20, timeout=4.56)
        assert motor.timeout == loose_approx(4.56)
        assert await motor.get_position() == 20

        await motor.go_to(-10, 50)
        assert await motor.get_position() == 50

    @pytest.mark.asyncio
    async def test_reset_zero(self, motor: MockMotor):
        await motor.reset_zero_position(20, timeout=5.67)
        assert motor.offset == 20
        assert motor.timeout == loose_approx(5.67)

    @pytest.mark.asyncio
    async def test_get_properties(self, motor: MockMotor):
        properties = await motor.get_properties(timeout=6.78)
        assert properties.position_reporting is True
        assert motor.timeout == loose_approx(6.78)

    @pytest.mark.asyncio
    async def test_stop(self, motor: MockMotor):
        await motor.set_power(10)
        assert motor.powered is True
        await motor.stop(timeout=7.89)
        assert motor.powered is False
        assert motor.power == 0
        assert motor.timeout == loose_approx(7.89)

    @pytest.mark.asyncio
    async def test_is_powered(self, motor: MockMotor):
        await motor.set_power(10)
        is_powered, power_pct = await motor.is_powered(timeout=8.90)
        assert is_powered is True
        assert power_pct == 10
        assert motor.timeout == loose_approx(8.90)

        await motor.set_power(0)
        is_powered, power_pct = await motor.is_powered()
        assert is_powered is False
        assert is_powered == 0

    @pytest.mark.asyncio
    async def test_is_moving(self, motor: MockMotor):
        await motor.set_power(10)
        assert await motor.is_moving()
        await motor.set_power(0)
        assert not await motor.is_moving()

    @pytest.mark.asyncio
    async def test_do(self, motor: MockMotor):
        command = {"command": "args"}
        resp = await motor.do_command(command)
        assert resp == {"command": command}

    @pytest.mark.asyncio
    async def test_status(self, motor: MockMotor):
        await motor.set_power(10)
        status = await create_status(motor)
        assert status.name == motor.get_resource_name(motor.name)
        assert status.status == message_to_struct(MotorStatus(is_powered=True, position=0, is_moving=True))

    @pytest.mark.asyncio
    async def test_extra(self, motor: MockMotor):
        assert motor.extra is None
        extra = {"foo": "bar", "baz": [1, 2, 3]}
        await motor.is_powered(extra=extra)
        assert motor.extra == extra

    @pytest.mark.asyncio
    async def test_get_geometries(self, motor: MockMotor):
        geometries = await motor.get_geometries()
        assert geometries == GEOMETRIES


class TestService:
    @pytest.mark.asyncio
    async def test_set_power(self, motor: MockMotor, service: MotorRPCService):
        async with ChannelFor([service]) as channel:
            client = MotorServiceStub(channel)
            request = SetPowerRequest(name=motor.name, power_pct=13)
            await client.SetPower(request, timeout=1.23)
            assert motor.power == 13
            assert motor.timeout == loose_approx(1.23)

    @pytest.mark.asyncio
    async def test_get_position(self, motor: MockMotor, service: MotorRPCService):
        async with ChannelFor([service]) as channel:
            client = MotorServiceStub(channel)
            request = GetPositionRequest(name=motor.name)
            response: GetPositionResponse = await client.GetPosition(request, timeout=2.34)
            assert response.position == 0
            assert motor.timeout == loose_approx(2.34)

    @pytest.mark.asyncio
    async def test_go_for(self, motor: MockMotor, service: MotorRPCService):
        async with ChannelFor([service]) as channel:
            client = MotorServiceStub(channel)

            request = GoForRequest(name=motor.name, rpm=30, revolutions=20)
            await client.GoFor(request, timeout=3.45)
            assert motor.position == 20
            assert motor.timeout == loose_approx(3.45)

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
    async def test_go_to(self, motor: MockMotor, service: MotorRPCService):
        async with ChannelFor([service]) as channel:
            client = MotorServiceStub(channel)

            request = GoToRequest(name=motor.name, rpm=30, position_revolutions=20)
            await client.GoTo(request, timeout=4.56)
            assert motor.position == 20
            assert motor.timeout == loose_approx(4.56)

            request = GoToRequest(name=motor.name, rpm=-10, position_revolutions=50)
            await client.GoTo(request)
            assert motor.position == 50

    @pytest.mark.asyncio
    async def test_reset_zero(self, motor: MockMotor, service: MotorRPCService):
        async with ChannelFor([service]) as channel:
            client = MotorServiceStub(channel)
            request = ResetZeroPositionRequest(name=motor.name, offset=20)
            await client.ResetZeroPosition(request, timeout=5.67)
            assert motor.offset == 20
            assert motor.timeout == loose_approx(5.67)

    @pytest.mark.asyncio
    async def test_get_properties(self, motor: MockMotor, service: MotorRPCService):
        async with ChannelFor([service]) as channel:
            client = MotorServiceStub(channel)
            request = GetPropertiesRequest(name=motor.name)
            response: GetPropertiesResponse = await client.GetProperties(request, timeout=6.78)
            assert response.position_reporting is True
            assert motor.timeout == loose_approx(6.78)

    @pytest.mark.asyncio
    async def test_stop(self, motor: MockMotor, service: MotorRPCService):
        async with ChannelFor([service]) as channel:
            client = MotorServiceStub(channel)
            request = StopRequest(name=motor.name)
            await client.Stop(request, timeout=7.89)
            assert motor.powered is False
            assert motor.power == 0
            assert motor.timeout == loose_approx(7.89)

    @pytest.mark.asyncio
    async def test_is_powered(self, motor: MockMotor, service: MotorRPCService):
        async with ChannelFor([service]) as channel:
            client = MotorServiceStub(channel)

            sp_request = SetPowerRequest(name=motor.name, power_pct=13)
            await client.SetPower(sp_request)
            request = IsPoweredRequest(name=motor.name)
            response: IsPoweredResponse = await client.IsPowered(request, timeout=8.90)
            assert response.is_on is True
            assert response.power_pct == 13
            assert motor.timeout == loose_approx(8.90)

            sp_request = SetPowerRequest(name=motor.name, power_pct=0)
            await client.SetPower(sp_request)
            request = IsPoweredRequest(name=motor.name)
            response: IsPoweredResponse = await client.IsPowered(request)
            assert response.is_on is False
            assert response.power_pct == 0

    @pytest.mark.asyncio
    async def test_is_moving(self, motor: MockMotor, service: MotorRPCService):
        async with ChannelFor([service]) as channel:
            assert motor.powered is False
            motor.powered = True
            client = MotorServiceStub(channel)
            request = IsMovingRequest(name=motor.name)
            response: IsMovingResponse = await client.IsMoving(request)
            assert response.is_moving is True

    @pytest.mark.asyncio
    async def test_extra(self, motor: MockMotor, service: MotorRPCService):
        async with ChannelFor([service]) as channel:
            client = MotorServiceStub(channel)

            assert motor.extra is None
            extra = {"foo": "bar", "baz": [1, 2, 3]}
            request = IsPoweredRequest(name=motor.name, extra=dict_to_struct(extra))
            await client.IsPowered(request)
            assert motor.extra == extra

    @pytest.mark.asyncio
    async def test_do(self, motor: MockMotor, service: MotorRPCService):
        async with ChannelFor([service]) as channel:
            client = MotorServiceStub(channel)
            command = {"command": "args"}
            request = DoCommandRequest(name=motor.name, command=dict_to_struct(command))
            response: DoCommandResponse = await client.DoCommand(request)
            result = struct_to_dict(response.result)
            assert result == {"command": command}

    @pytest.mark.asyncio
    async def test_get_geometries(self, motor: MockMotor, service: MotorRPCService):
        async with ChannelFor([service]) as channel:
            client = MotorServiceStub(channel)
            request = GetGeometriesRequest(name=motor.name)
            response: GetGeometriesResponse = await client.GetGeometries(request)
            assert [geometry for geometry in response.geometries] == GEOMETRIES


class TestClient:
    @pytest.mark.asyncio
    async def test_set_power(self, motor: MockMotor, service: MotorRPCService):
        async with ChannelFor([service]) as channel:
            client = MotorClient(motor.name, channel)
            await client.set_power(13, timeout=1.23)
            assert motor.power == 13
            assert motor.timeout == loose_approx(1.23)

    @pytest.mark.asyncio
    async def test_get_position(self, motor: MockMotor, service: MotorRPCService):
        async with ChannelFor([service]) as channel:
            client = MotorClient(motor.name, channel)
            position = await client.get_position(timeout=2.34)
            assert position == 0
            assert motor.timeout == loose_approx(2.34)

    @pytest.mark.asyncio
    async def test_go_for(self, motor: MockMotor, service: MotorRPCService):
        async with ChannelFor([service]) as channel:
            client = MotorClient(motor.name, channel)

            await client.go_for(30, 20, timeout=3.45)
            assert motor.position == 20
            assert motor.timeout == loose_approx(3.45)

            await client.go_for(-10, 10)
            assert motor.position == 10

            await client.go_for(10, -5)
            assert motor.position == 5

            await client.go_for(-10, -10)
            assert motor.position == 15

    @pytest.mark.asyncio
    async def test_go_to(self, motor: MockMotor, service: MotorRPCService):
        async with ChannelFor([service]) as channel:
            client = MotorClient(motor.name, channel)

            await client.go_to(30, 20, timeout=4.56)
            assert motor.position == 20
            assert motor.timeout == loose_approx(4.56)

            await client.go_to(-10, 50)
            assert motor.position == 50

    @pytest.mark.asyncio
    async def test_reset_zero(self, motor: MockMotor, service: MotorRPCService):
        async with ChannelFor([service]) as channel:
            client = MotorClient(motor.name, channel)
            await client.reset_zero_position(20, timeout=5.67)
            assert motor.timeout == loose_approx(5.67)
            assert motor.offset == 20

    @pytest.mark.asyncio
    async def test_get_properties(self, motor: MockMotor, service: MotorRPCService):
        async with ChannelFor([service]) as channel:
            client = MotorClient(motor.name, channel)
            properties = await client.get_properties(timeout=6.78)
            assert properties.position_reporting is True
            assert motor.timeout == loose_approx(6.78)

    @pytest.mark.asyncio
    async def test_stop(self, motor: MockMotor, service: MotorRPCService):
        async with ChannelFor([service]) as channel:
            client = MotorClient(motor.name, channel)
            await client.stop(timeout=7.89)
            assert motor.powered is False
            assert motor.power == 0
            assert motor.timeout == loose_approx(7.89)

    @pytest.mark.asyncio
    async def test_is_powered(self, motor: MockMotor, service: MotorRPCService):
        async with ChannelFor([service]) as channel:
            client = MotorClient(motor.name, channel)

            await client.set_power(13)
            is_on, power_pct = await client.is_powered(timeout=8.90)
            assert is_on is True
            assert power_pct == 13
            assert motor.timeout == loose_approx(8.90)

            await client.set_power(0)
            is_on, power_pct = await client.is_powered()
            assert is_on is False
            assert power_pct == 0

    @pytest.mark.asyncio
    async def test_is_moving(self, motor: MockMotor, service: MotorRPCService):
        async with ChannelFor([service]) as channel:
            client = MotorClient(motor.name, channel)
            assert motor.powered is False
            motor.powered = True
            assert await client.is_moving() is True

    @pytest.mark.asyncio
    async def test_do(self, motor: MockMotor, service: MotorRPCService):
        async with ChannelFor([service]) as channel:
            client = MotorClient(motor.name, channel)
            command = {"command": "args"}
            resp = await client.do_command(command)
            assert resp == {"command": command}

    @pytest.mark.asyncio
    async def test_extra(self, motor: MockMotor, service: MotorRPCService):
        async with ChannelFor([service]) as channel:
            client = MotorClient(motor.name, channel)

            assert motor.extra is None
            extra = {"foo": "bar", "baz": [1, 2, 3]}
            await client.is_powered(extra=extra)
            assert motor.extra == extra

    @pytest.mark.asyncio
    async def test_get_geometries(self, motor: MockMotor, service: MotorRPCService):
        async with ChannelFor([service]) as channel:
            client = MotorClient(motor.name, channel)
            geometries = await client.get_geometries()
            assert geometries == GEOMETRIES
