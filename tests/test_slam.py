import pytest
from grpclib.testing import ChannelFor

from viam.proto.common import Pose
from viam.services.slam import SLAMServiceClient

from . import loose_approx
from .mocks.services import MockSLAMService

INTERNAL_STATE_CHUNKS = [bytes(5), bytes(2)]
POINT_CLOUD_CHUNKS = [bytes(3), bytes(2)]
POSITION = Pose(
    x=1,
    y=2,
    z=3,
    o_x=2,
    o_y=3,
    o_z=4,
    theta=20,
)

SLAM_SERVICE_NAME = "slam1"


@pytest.fixture(scope="function")
def service() -> MockSLAMService:
    return MockSLAMService(
        name=SLAM_SERVICE_NAME,
        internal_state_chunks=INTERNAL_STATE_CHUNKS,
        point_cloud_pcd_chunks=POINT_CLOUD_CHUNKS,
        position=POSITION,
    )


class TestClient:
    @pytest.mark.asyncio
    async def test_get_position(self, service: MockSLAMService):
        async with ChannelFor([service]) as channel:
            client = SLAMServiceClient(SLAM_SERVICE_NAME, channel)
            assert service.timeout is None
            timeout = 1.1
            response = await client.get_position(SLAM_SERVICE_NAME, timeout=timeout)
            assert response == POSITION
            assert service.timeout == loose_approx(timeout)

    @pytest.mark.asyncio
    async def test_get_internal_state(self, service: MockSLAMService):
        async with ChannelFor([service]) as channel:
            client = SLAMServiceClient(SLAM_SERVICE_NAME, channel)
            response = await client.get_internal_state(SLAM_SERVICE_NAME)
            assert len(response) == len(INTERNAL_STATE_CHUNKS)
            for i, chunk in enumerate(response):
                assert chunk.internal_state_chunk == INTERNAL_STATE_CHUNKS[i]

    @pytest.mark.asyncio
    async def test_get_point_cloud_map(self, service: MockSLAMService):
        async with ChannelFor([service]) as channel:
            client = SLAMServiceClient(SLAM_SERVICE_NAME, channel)
            response = await client.get_point_cloud_map(SLAM_SERVICE_NAME)
            assert len(response) == len(POINT_CLOUD_CHUNKS)
            for i, chunk in enumerate(response):
                assert chunk.point_cloud_pcd_chunk == POINT_CLOUD_CHUNKS[i]

    @pytest.mark.asyncio
    async def test_do(self, service: MockSLAMService):
        async with ChannelFor([service]) as channel:
            client = SLAMServiceClient(SLAM_SERVICE_NAME, channel)
            command = {"command": "args"}
            response = await client.do_command(command)
            assert response == command
