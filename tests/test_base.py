from random import randint, random

import pytest
from grpclib.testing import ChannelFor
from viam.components.base import BaseClient, Vector3
from viam.components.base.service import BaseService
from viam.components.generic.service import GenericService
from viam.components.resource_manager import ResourceManager
from viam.proto.api.component.base import (BaseServiceStub, MoveArcRequest,
                                           MoveStraightRequest,
                                           SetPowerRequest, SetPowerResponse,
                                           SpinRequest, StopRequest)

from .mocks.components import MockBase


@pytest.fixture(scope='function')
def base() -> MockBase:
    return MockBase(name='base')


@pytest.fixture(scope='function')
def service(base: MockBase) -> BaseService:
    manager = ResourceManager([base])
    return BaseService(manager)


@pytest.fixture(scope='function')
def generic_service(base: MockBase) -> GenericService:
    manager = ResourceManager([base])
    return GenericService(manager)


class TestBase:

    @pytest.mark.asyncio
    async def test_move_straight(self, base: MockBase):
        distances = [randint(-50, 50) for _ in range(4)]
        velocities = [random()+1 for _ in range(4)]

        for (i, (d, v)) in enumerate(zip(distances, velocities)):
            await base.move_straight(d, v)
            assert base.position == sum(distances[:i+1])

    @pytest.mark.asyncio
    async def test_move_arc(self, base: MockBase):
        distances = [randint(-50, 50) for _ in range(8)]
        velocities = [random()+1 for _ in range(8)]
        angles = [randint(-180, 180) for _ in range(8)]

        for (i, (d, v, a)) in enumerate(zip(distances, velocities, angles)):
            await base.move_arc(d, v, a)
            assert base.position == sum(distances[:i+1])
            assert base.angle == sum(angles[:i+1])

    @pytest.mark.asyncio
    async def test_spin(self, base: MockBase):
        angles = [randint(-180, 180) for _ in range(4)]
        velocities = [random()+1 for _ in range(4)]

        for (i, (a, v)) in enumerate(zip(angles, velocities)):
            await base.spin(a, v)
            assert base.angle == sum(angles[:i+1])

    @pytest.mark.asyncio
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

        await base.move_arc(1, 1, 1)
        assert base.stopped is False
        await base.move_arc(0, 0, 0)
        assert base.stopped is True

        await base.spin(1, 1)
        assert base.stopped is False
        await base.spin(0, 0)
        assert base.stopped is True

    @pytest.mark.asyncio
    async def test_set_power(self, base: MockBase):
        assert base.linear == Vector3(x=0, y=0, z=0)
        assert base.angular == Vector3(x=0, y=0, z=0)

        await base.set_power(Vector3(x=1, y=2, z=3), Vector3(x=4, y=5, z=6))

        assert base.linear == Vector3(x=1, y=2, z=3)
        assert base.angular == Vector3(x=4, y=5, z=6)

    @pytest.mark.asyncio
    async def test_do(self, base: MockBase):
        with pytest.raises(NotImplementedError):
            await base.do({'command': 'args'})


class TestService:

    @pytest.mark.asyncio
    async def test_move_straight(self, base: MockBase, service: BaseService):
        distances = [randint(-50, 50) for _ in range(4)]
        velocities = [random()+1 for _ in range(4)]

        async with ChannelFor([service]) as channel:
            client = BaseServiceStub(channel)
            for (i, (d, v)) in enumerate(zip(distances, velocities)):
                request = MoveStraightRequest(
                    name=base.name,
                    distance_mm=d,
                    mm_per_sec=v,
                )
                await client.MoveStraight(request)
                assert base.position == sum(distances[:i+1])

    @pytest.mark.asyncio
    async def test_move_arc(self, base: MockBase, service: BaseService):
        distances = [randint(-50, 50) for _ in range(8)]
        velocities = [random()+1 for _ in range(8)]
        angles = [randint(-180, 180) for _ in range(8)]

        async with ChannelFor([service]) as channel:
            client = BaseServiceStub(channel)
            for (i, (d, v, a)) in enumerate(
                    zip(distances, velocities, angles)):
                request = MoveArcRequest(
                    name=base.name,
                    distance_mm=d,
                    mm_per_sec=v,
                    angle_deg=a,
                )
                await client.MoveArc(request)
                assert base.position == sum(distances[:i+1])
                assert base.angle == sum(angles[:i+1])

    @pytest.mark.asyncio
    async def test_spin(self, base: MockBase, service: BaseService):
        angles = [randint(-180, 180) for _ in range(4)]
        velocities = [random()+1 for _ in range(4)]

        async with ChannelFor([service]) as channel:
            client = BaseServiceStub(channel)
            for (i, (a, v)) in enumerate(zip(angles, velocities)):
                request = SpinRequest(
                    name=base.name,
                    angle_deg=a,
                    degs_per_sec=v,
                )
                await client.Spin(request)
                assert base.angle == sum(angles[:i+1])

    @pytest.mark.asyncio
    async def test_set_power(self, base: MockBase, service: BaseService):
        async with ChannelFor([service]) as channel:
            client = BaseServiceStub(channel)
            assert base.linear == Vector3(x=0, y=0, z=0)
            assert base.angular == Vector3(x=0, y=0, z=0)

            request = SetPowerRequest(name=base.name, linear=Vector3(x=1, y=2, z=3), angular=Vector3(x=4, y=5, z=6))
            await client.SetPower(request)

            assert base.linear == Vector3(x=1, y=2, z=3)
            assert base.angular == Vector3(x=4, y=5, z=6)

    @pytest.mark.asyncio
    async def test_stop(self, base: MockBase, service: BaseService):
        async with ChannelFor([service]) as channel:
            client = BaseServiceStub(channel)

            assert base.stopped is True

            request = MoveStraightRequest(
                name=base.name,
                distance_mm=1,
                mm_per_sec=1,
            )
            await client.MoveStraight(request)
            assert base.stopped is False
            await client.Stop(StopRequest(name=base.name))
            assert base.stopped is True

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

            request = MoveArcRequest(
                name=base.name,
                distance_mm=1,
                mm_per_sec=1,
                angle_deg=1,
            )
            await client.MoveArc(request)
            assert base.stopped is False
            request = MoveArcRequest(
                name=base.name,
                distance_mm=0,
                mm_per_sec=0,
                angle_deg=0,
            )
            await client.MoveArc(request)
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


class TestClient:

    @pytest.mark.asyncio
    async def test_move_straight(self, base: MockBase, service: BaseService):
        distances = [randint(-50, 50) for _ in range(4)]
        velocities = [random()+1 for _ in range(4)]

        async with ChannelFor([service]) as channel:
            client = BaseClient(base.name, channel)
            for (i, (d, v)) in enumerate(zip(distances, velocities)):
                await client.move_straight(d, v)
                assert base.position == sum(distances[:i+1])

    @pytest.mark.asyncio
    async def test_move_arc(self, base: MockBase, service: BaseService):
        distances = [randint(-50, 50) for _ in range(8)]
        velocities = [random()+1 for _ in range(8)]
        angles = [randint(-180, 180) for _ in range(8)]

        async with ChannelFor([service]) as channel:
            client = BaseClient(base.name, channel)
            for (i, (d, v, a)) in enumerate(
                    zip(distances, velocities, angles)):
                await client.move_arc(d, v, a)
                assert base.position == sum(distances[:i+1])
                assert base.angle == sum(angles[:i+1])

    @pytest.mark.asyncio
    async def test_spin(self, base: MockBase, service: BaseService):
        angles = [randint(-180, 180) for _ in range(4)]
        velocities = [random()+1 for _ in range(4)]

        async with ChannelFor([service]) as channel:
            client = BaseClient(base.name, channel)
            for (i, (a, v)) in enumerate(zip(angles, velocities)):
                await client.spin(a, v)
                assert base.angle == sum(angles[:i+1])

    @pytest.mark.asyncio
    async def test_stop(self, base: MockBase, service: BaseService):
        async with ChannelFor([service]) as channel:
            client = BaseClient(base.name, channel)

            assert base.stopped is True

            await client.move_straight(1, 1)
            assert base.stopped is False
            await client.stop()
            assert base.stopped is True

            await client.move_straight(1, 1)
            assert base.stopped is False
            await client.move_straight(0, 0)
            assert base.stopped is True

            await client.move_arc(1, 1, 1)
            assert base.stopped is False
            await client.move_arc(0, 0, 0)
            assert base.stopped is True

            await client.spin(1, 1)
            assert base.stopped is False
            await client.spin(0, 0)
            assert base.stopped is True

    @pytest.mark.asyncio
    async def test_set_power(self, base: MockBase, service: BaseService):
        async with ChannelFor([service]) as channel:
            client = BaseClient(base.name, channel)
            assert base.linear == Vector3(x=0, y=0, z=0)
            assert base.angular == Vector3(x=0, y=0, z=0)

            await client.set_power(Vector3(x=1, y=2, z=3), Vector3(x=4, y=5, z=6))

            assert base.linear == Vector3(x=1, y=2, z=3)
            assert base.angular == Vector3(x=4, y=5, z=6)

    @pytest.mark.asyncio
    async def test_do(self, base: MockBase, service: BaseService, generic_service: GenericService):
        async with ChannelFor([service, generic_service]) as channel:
            client = BaseClient(base.name, channel)
            with pytest.raises(NotImplementedError):
                await client.do({'command': 'args'})
