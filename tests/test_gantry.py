import pytest
from grpclib.testing import ChannelFor
from viam.components.gantry import GantryClient
from viam.components.gantry.service import GantryService
from viam.components.resource_manager import ResourceManager
from viam.proto.api.component.gantry import (GantryServiceStub,
                                             GetLengthsRequest,
                                             GetLengthsResponse,
                                             GetPositionRequest,
                                             GetPositionResponse,
                                             MoveToPositionRequest)

from .mocks.components import MockGantry


class TestGantry:

    gantry = MockGantry('gantry', [1, 2, 3], [4, 5, 6])

    @pytest.mark.asyncio
    async def test_get_position(self):
        pos = await self.gantry.get_position()
        assert pos == [1, 2, 3]

    @pytest.mark.asyncio
    async def test_move_to_position(self):
        await self.gantry.move_to_position([1, 8, 2], [])
        assert self.gantry.position == [1, 8, 2]

    @pytest.mark.asyncio
    async def test_get_lengths(self):
        lengths = await self.gantry.get_lengths()
        assert lengths == [4, 5, 6]


class TestService:

    gantry = MockGantry('gantry', [1, 2, 3], [4, 5, 6])
    manager = ResourceManager([gantry])
    service = GantryService(manager)

    @pytest.mark.asyncio
    async def test_get_position(self):
        async with ChannelFor([self.service]) as channel:
            client = GantryServiceStub(channel)
            request = GetPositionRequest(name=self.gantry.name)
            response: GetPositionResponse = await client.GetPosition(request)
            assert list(response.positions_mm) == [1, 2, 3]

    @pytest.mark.asyncio
    async def test_move_to_position(self):
        async with ChannelFor([self.service]) as channel:
            client = GantryServiceStub(channel)
            request = MoveToPositionRequest(
                name=self.gantry.name, positions_mm=[1, 8, 2])
            await client.MoveToPosition(request)
            assert self.gantry.position == [1, 8, 2]

    @pytest.mark.asyncio
    async def test_get_lengths(self):
        async with ChannelFor([self.service]) as channel:
            client = GantryServiceStub(channel)
            request = GetLengthsRequest(name=self.gantry.name)
            response: GetLengthsResponse = await client.GetLengths(request)
            assert list(response.lengths_mm) == [4, 5, 6]


class TestClient:

    gantry = MockGantry('gantry', [1, 2, 3], [4, 5, 6])
    manager = ResourceManager([gantry])
    service = GantryService(manager)

    @pytest.mark.asyncio
    async def test_get_position(self):
        async with ChannelFor([self.service]) as channel:
            client = GantryClient(self.gantry.name, channel)
            pos = await client.get_position()
            assert pos == [1, 2, 3]

    @pytest.mark.asyncio
    async def test_move_to_position(self):
        async with ChannelFor([self.service]) as channel:
            client = GantryClient(self.gantry.name, channel)
            await client.move_to_position([1, 8, 2], [])
            assert self.gantry.position == [1, 8, 2]

    @pytest.mark.asyncio
    async def test_get_lengths(self):
        async with ChannelFor([self.service]) as channel:
            client = GantryClient(self.gantry.name, channel)
            lengths = await client.get_lengths()
            assert lengths == [4, 5, 6]
