from random import randint, random
from grpclib.testing import ChannelFor
import pytest

from viam.components.resource_manager import ResourceManager
from viam.components.base import BaseClient, BaseService
from viam.proto.api.component.base import (
    BaseServiceStub,
    MoveStraightRequest,
    MoveArcRequest,
    SpinRequest,
    StopRequest
)

from .mocks.components import MockBase


@pytest.fixture(scope='function')
def base() -> MockBase:
    return MockBase(name='base')


@pytest.fixture(scope='function')
def service(base: MockBase) -> BaseService:
    manager = ResourceManager([base])
    return BaseService(manager)


class TestBase:

    @pytest.mark.asyncio
    async def test_move_straight(self, base: MockBase):
        distances = [randint(-50, 50) for _ in range(4)]
        velocities = [random()+1 for _ in range(4)]

        for (i, (d, v)) in enumerate(zip(distances, velocities)):
            await base.move_straight(d, v, False)
            assert base.position == sum(distances[:i+1])

    @pytest.mark.asyncio
    async def test_move_arc(self, base: MockBase):
        distances = [randint(-50, 50) for _ in range(8)]
        velocities = [random()+1 for _ in range(8)]
        angles = [randint(-180, 180) for _ in range(8)]

        for (i, (d, v, a)) in enumerate(zip(distances, velocities, angles)):
            await base.move_arc(d, v, a, False)
            assert base.position == sum(distances[:i+1])
            assert base.angle == sum(angles[:i+1])

    @pytest.mark.asyncio
    async def test_spin(self, base: MockBase):
        angles = [randint(-180, 180) for _ in range(4)]
        velocities = [random()+1 for _ in range(4)]

        for (i, (a, v)) in enumerate(zip(angles, velocities)):
            await base.spin(a, v, False)
            assert base.angle == sum(angles[:i+1])

    @pytest.mark.asyncio
    async def test_stop(self, base: MockBase):
        assert base.stopped is True

        await base.move_straight(1, 1, False)
        assert base.stopped is False
        await base.stop()
        assert base.stopped is True

        await base.move_straight(1, 1, False)
        assert base.stopped is False
        await base.move_straight(0, 0, False)
        assert base.stopped is True

        await base.move_arc(1, 1, 1, False)
        assert base.stopped is False
        await base.move_arc(0, 0, 0, False)
        assert base.stopped is True

        await base.spin(1, 1, False)
        assert base.stopped is False
        await base.spin(0, 0, False)
        assert base.stopped is True


class TestService:

    @pytest.fixture(scope='function')
    def service(self, base: MockBase) -> BaseService:
        manager = ResourceManager([base])
        return BaseService(manager)

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
                    block=False
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
                    block=False
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
                    block=False
                )
                await client.Spin(request)
                assert base.angle == sum(angles[:i+1])

    @pytest.mark.asyncio
    async def test_stop(self, base: MockBase, service: BaseService):
        async with ChannelFor([service]) as channel:
            client = BaseServiceStub(channel)

            assert base.stopped is True

            request = MoveStraightRequest(
                name=base.name,
                distance_mm=1,
                mm_per_sec=1,
                block=False
            )
            await client.MoveStraight(request)
            assert base.stopped is False
            await client.Stop(StopRequest(name=base.name))
            assert base.stopped is True

            request = MoveStraightRequest(
                name=base.name,
                distance_mm=1,
                mm_per_sec=1,
                block=False
            )
            await client.MoveStraight(request)
            assert base.stopped is False
            request = MoveStraightRequest(
                name=base.name,
                distance_mm=0,
                mm_per_sec=0,
                block=False
            )
            await client.MoveStraight(request)
            assert base.stopped is True

            request = MoveArcRequest(
                name=base.name,
                distance_mm=1,
                mm_per_sec=1,
                angle_deg=1,
                block=False
            )
            await client.MoveArc(request)
            assert base.stopped is False
            request = MoveArcRequest(
                name=base.name,
                distance_mm=0,
                mm_per_sec=0,
                angle_deg=0,
                block=False
            )
            await client.MoveArc(request)
            assert base.stopped is True

            request = SpinRequest(
                name=base.name,
                angle_deg=1,
                degs_per_sec=1,
                block=False
            )
            await client.Spin(request)
            assert base.stopped is False
            request = SpinRequest(
                name=base.name,
                angle_deg=0,
                degs_per_sec=0,
                block=False
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
                await client.move_straight(d, v, False)
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
                await client.move_arc(d, v, a, False)
                assert base.position == sum(distances[:i+1])
                assert base.angle == sum(angles[:i+1])

    @pytest.mark.asyncio
    async def test_spin(self, base: MockBase, service: BaseService):
        angles = [randint(-180, 180) for _ in range(4)]
        velocities = [random()+1 for _ in range(4)]

        async with ChannelFor([service]) as channel:
            client = BaseClient(base.name, channel)
            for (i, (a, v)) in enumerate(zip(angles, velocities)):
                await client.spin(a, v, False)
                assert base.angle == sum(angles[:i+1])

    @pytest.mark.asyncio
    async def test_stop(self, base: MockBase, service: BaseService):
        async with ChannelFor([service]) as channel:
            client = BaseClient(base.name, channel)

            assert base.stopped is True

            await client.move_straight(1, 1, False)
            assert base.stopped is False
            await client.stop()
            assert base.stopped is True

            await client.move_straight(1, 1, False)
            assert base.stopped is False
            await client.move_straight(0, 0, False)
            assert base.stopped is True

            await client.move_arc(1, 1, 1, False)
            assert base.stopped is False
            await client.move_arc(0, 0, 0, False)
            assert base.stopped is True

            await client.spin(1, 1, False)
            assert base.stopped is False
            await client.spin(0, 0, False)
            assert base.stopped is True
