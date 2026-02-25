from random import randint, random

import pytest
from grpclib.testing import ChannelFor

from viam.components.base import BaseClient, Vector3
from viam.components.base.service import BaseRPCService
from viam.components.generic.service import GenericRPCService
from viam.proto.common import DoCommandRequest, DoCommandResponse, GetGeometriesRequest, GetGeometriesResponse
from viam.proto.component.base import (
    BaseServiceStub,
    IsMovingRequest,
    IsMovingResponse,
    MoveStraightRequest,
    SetPowerRequest,
    SetVelocityRequest,
    SpinRequest,
    StopRequest,
)
from viam.resource.manager import ResourceManager
from viam.utils import dict_to_struct, struct_to_dict

from . import expected_grpc_timeout
from .mocks.components import GEOMETRIES, MockBase


@pytest.fixture(scope="function")
def base() -> MockBase:
    return MockBase(name="base")


@pytest.fixture(scope="function")
def service(base: MockBase) -> BaseRPCService:
    manager = ResourceManager([base])
    return BaseRPCService(manager)


@pytest.fixture(scope="function")
def generic_service(base: MockBase) -> GenericRPCService:
    manager = ResourceManager([base])
    return GenericRPCService(manager)


class TestBase:
    async def test_move_straight(self, base: MockBase):
        distances = [randint(-50, 50) for _ in range(4)]
        velocities = [random() + 1 for _ in range(4)]

        for i, (d, v) in enumerate(zip(distances, velocities)):
            await base.move_straight(d, v)
            assert base.position == sum(distances[: i + 1])

    async def test_spin(self, base: MockBase):
        angles = [randint(-180, 180) for _ in range(4)]
        velocities = [random() + 1 for _ in range(4)]

        for i, (a, v) in enumerate(zip(angles, velocities)):
            await base.spin(a, v)
            assert base.angle == sum(angles[: i + 1])

    async def test_stop(self, base: MockBase):
        assert base.stopped is True

        await base.move_straight(1, 1)
        assert base.stopped is False
        await base.stop()
        assert base.stopped is True

        await base.move_straight(1, 1)
        assert base.stopped is False
        await base.move_straight(0, 0)
        assert base.stopped is True

        await base.spin(1, 1)
        assert base.stopped is False
        await base.spin(0, 0)
        assert base.stopped is True

    async def test_set_power(self, base: MockBase):
        assert base.linear_pwr == Vector3(x=0, y=0, z=0)
        assert base.angular_pwr == Vector3(x=0, y=0, z=0)

        await base.set_power(Vector3(x=1, y=2, z=3), Vector3(x=4, y=5, z=6))

        assert base.linear_pwr == Vector3(x=1, y=2, z=3)
        assert base.angular_pwr == Vector3(x=4, y=5, z=6)

    async def test_velocity(self, base: MockBase):
        assert base.linear_vel == Vector3(x=0, y=0, z=0)
        assert base.angular_vel == Vector3(x=0, y=0, z=0)

        await base.set_velocity(Vector3(x=1, y=2, z=3), Vector3(x=4, y=5, z=6))

        assert base.linear_vel == Vector3(x=1, y=2, z=3)
        assert base.angular_vel == Vector3(x=4, y=5, z=6)

    async def test_is_moving(self, base: MockBase):
        await base.move_straight(1, 1)
        assert await base.is_moving()
        await base.stop()
        assert base.stopped is True
        assert not await base.is_moving()

    async def test_get_properties(self, base: MockBase):
        properties = await base.get_properties()
        assert properties.width_meters == 1.0
        assert properties.turning_radius_meters == 2.0
        assert properties.wheel_circumference_meters == 3.0

    async def test_do(self, base: MockBase):
        command = {"command": "args"}
        resp = await base.do_command(command)
        assert resp == {"command": command}

    async def test_extra(self, base: MockBase):
        assert base.extra is None
        extra = {"foo": "bar", "baz": [1, 2, 3]}
        await base.move_straight(1, 1, extra=extra)
        assert base.extra == extra

    async def test_get_geometries(self, base: MockBase):
        geometries = await base.get_geometries()
        assert geometries == GEOMETRIES


class TestService:
    async def test_move_straight(self, base: MockBase, service: BaseRPCService):
        distances = [randint(-50, 50) for _ in range(4)]
        velocities = [random() + 1 for _ in range(4)]

        async with ChannelFor([service]) as channel:
            client = BaseServiceStub(channel)
            for i, (d, v) in enumerate(zip(distances, velocities)):
                request = MoveStraightRequest(
                    name=base.name,
                    distance_mm=d,
                    mm_per_sec=v,
                )
                await client.MoveStraight(request)
                assert base.position == sum(distances[: i + 1])

    async def test_spin(self, base: MockBase, service: BaseRPCService):
        angles = [randint(-180, 180) for _ in range(4)]
        velocities = [random() + 1 for _ in range(4)]

        async with ChannelFor([service]) as channel:
            client = BaseServiceStub(channel)
            for i, (a, v) in enumerate(zip(angles, velocities)):
                request = SpinRequest(
                    name=base.name,
                    angle_deg=a,
                    degs_per_sec=v,
                )
                await client.Spin(request)
                assert base.angle == sum(angles[: i + 1])

    async def test_set_power(self, base: MockBase, service: BaseRPCService):
        async with ChannelFor([service]) as channel:
            client = BaseServiceStub(channel)
            assert base.linear_pwr == Vector3(x=0, y=0, z=0)
            assert base.angular_pwr == Vector3(x=0, y=0, z=0)

            request = SetPowerRequest(name=base.name, linear=Vector3(x=1, y=2, z=3), angular=Vector3(x=4, y=5, z=6))
            await client.SetPower(request)

            assert base.linear_pwr == Vector3(x=1, y=2, z=3)
            assert base.angular_pwr == Vector3(x=4, y=5, z=6)

    async def test_set_velocity(self, base: MockBase, service: BaseRPCService):
        async with ChannelFor([service]) as channel:
            client = BaseServiceStub(channel)
            assert base.linear_vel == Vector3(x=0, y=0, z=0)
            assert base.angular_vel == Vector3(x=0, y=0, z=0)

            request = SetVelocityRequest(name=base.name, linear=Vector3(x=1, y=2, z=3), angular=Vector3(x=4, y=5, z=6))
            await client.SetVelocity(request)

            assert base.linear_vel == Vector3(x=1, y=2, z=3)
            assert base.angular_vel == Vector3(x=4, y=5, z=6)

    async def test_stop(self, base: MockBase, service: BaseRPCService):
        async with ChannelFor([service]) as channel:
            client = BaseServiceStub(channel)

            assert base.stopped is True
            assert base.timeout is None

            request = MoveStraightRequest(
                name=base.name,
                distance_mm=1,
                mm_per_sec=1,
            )
            await client.MoveStraight(request)
            assert base.stopped is False
            await client.Stop(StopRequest(name=base.name), timeout=1.82)
            assert base.stopped is True
            assert base.timeout == expected_grpc_timeout(1.82)

            request = MoveStraightRequest(
                name=base.name,
                distance_mm=1,
                mm_per_sec=1,
            )
            await client.MoveStraight(request)
            assert base.stopped is False
            request = MoveStraightRequest(
                name=base.name,
                distance_mm=0,
                mm_per_sec=0,
            )
            await client.MoveStraight(request)
            assert base.stopped is True

            request = SpinRequest(
                name=base.name,
                angle_deg=1,
                degs_per_sec=1,
            )
            await client.Spin(request)
            assert base.stopped is False
            request = SpinRequest(
                name=base.name,
                angle_deg=0,
                degs_per_sec=0,
            )
            await client.Spin(request)
            assert base.stopped is True

    async def test_is_moving(self, base: MockBase, service: BaseRPCService):
        async with ChannelFor([service]) as channel:
            assert base.stopped is True
            base.stopped = False
            client = BaseServiceStub(channel)
            request = IsMovingRequest(name=base.name)
            response: IsMovingResponse = await client.IsMoving(request)
            assert response.is_moving is True

    async def test_extra(self, base: MockBase, service: BaseRPCService):
        async with ChannelFor([service]) as channel:
            assert base.extra is None
            client = BaseServiceStub(channel)
            extra = {"foo": "bar", "baz": [1, 2, 3]}
            request = MoveStraightRequest(name=base.name, distance_mm=1, mm_per_sec=1, extra=dict_to_struct(extra))
            await client.MoveStraight(request)
            assert base.extra == extra

    async def test_do(self, base: MockBase, service: BaseRPCService):
        async with ChannelFor([service]) as channel:
            client = BaseServiceStub(channel)
            command = {"command": "args"}
            request = DoCommandRequest(name=base.name, command=dict_to_struct(command))
            response: DoCommandResponse = await client.DoCommand(request)
            result = struct_to_dict(response.result)
            assert result == {"command": command}

    async def test_get_geometries(self, base: MockBase, service: BaseRPCService):
        async with ChannelFor([service]) as channel:
            client = BaseServiceStub(channel)
            request = GetGeometriesRequest(name=base.name)
            response: GetGeometriesResponse = await client.GetGeometries(request)
            assert [geometry for geometry in response.geometries] == GEOMETRIES


class TestClient:
    async def test_move_straight(self, base: MockBase, service: BaseRPCService):
        distances = [randint(-50, 50) for _ in range(4)]
        velocities = [random() + 1 for _ in range(4)]

        async with ChannelFor([service]) as channel:
            client = BaseClient(base.name, channel)
            for i, (d, v) in enumerate(zip(distances, velocities)):
                await client.move_straight(d, v)
                assert base.position == sum(distances[: i + 1])

    async def test_spin(self, base: MockBase, service: BaseRPCService):
        angles = [randint(-180, 180) for _ in range(4)]
        velocities = [random() + 1 for _ in range(4)]

        async with ChannelFor([service]) as channel:
            client = BaseClient(base.name, channel)
            for i, (a, v) in enumerate(zip(angles, velocities)):
                await client.spin(a, v)
                assert base.angle == sum(angles[: i + 1])

    async def test_set_power(self, base: MockBase, service: BaseRPCService):
        async with ChannelFor([service]) as channel:
            client = BaseClient(base.name, channel)
            assert base.linear_pwr == Vector3(x=0, y=0, z=0)
            assert base.angular_pwr == Vector3(x=0, y=0, z=0)

            await client.set_power(Vector3(x=1, y=2, z=3), Vector3(x=4, y=5, z=6))

            assert base.linear_pwr == Vector3(x=1, y=2, z=3)
            assert base.angular_pwr == Vector3(x=4, y=5, z=6)

    async def test_set_velocity(self, base: MockBase, service: BaseRPCService):
        async with ChannelFor([service]) as channel:
            client = BaseClient(base.name, channel)
            assert base.linear_vel == Vector3(x=0, y=0, z=0)
            assert base.angular_vel == Vector3(x=0, y=0, z=0)

            await client.set_velocity(Vector3(x=1, y=2, z=3), Vector3(x=4, y=5, z=6))

            assert base.linear_vel == Vector3(x=1, y=2, z=3)
            assert base.angular_vel == Vector3(x=4, y=5, z=6)

    async def test_stop(self, base: MockBase, service: BaseRPCService):
        assert base.timeout is None
        async with ChannelFor([service]) as channel:
            client = BaseClient(base.name, channel)

            assert base.stopped is True

            await client.move_straight(1, 1)
            assert base.stopped is False
            await client.stop(timeout=4.4)
            assert base.stopped is True
            assert base.timeout == expected_grpc_timeout(4.4)

            await client.move_straight(1, 1)
            assert base.stopped is False
            await client.move_straight(0, 0)
            assert base.stopped is True

            await client.spin(1, 1)
            assert base.stopped is False
            await client.spin(0, 0)
            assert base.stopped is True

    async def test_is_moving(self, base: MockBase, service: BaseRPCService):
        async with ChannelFor([service]) as channel:
            assert base.stopped is True
            base.stopped = False
            client = BaseClient(base.name, channel)
            assert await client.is_moving() is True

    async def test_do(self, base: MockBase, service: BaseRPCService):
        async with ChannelFor([service]) as channel:
            client = BaseClient(base.name, channel)
            command = {"command": "args"}
            resp = await client.do_command(command)
            assert resp == {"command": command}

    async def test_extra(self, base: MockBase, service: BaseRPCService):
        async with ChannelFor([service]) as channel:
            assert base.extra is None
            client = BaseClient(base.name, channel)
            extra = {"foo": "bar", "baz": [1, 2, 3]}
            await client.move_straight(1, 1, extra=extra)
            assert base.extra == extra

    async def test_get_geometries(self, base: MockBase, service: BaseRPCService):
        async with ChannelFor([service]) as channel:
            client = BaseClient(base.name, channel)
            geometries = await client.get_geometries()
            assert geometries == GEOMETRIES
