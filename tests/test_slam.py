import pytest

from grpclib.testing import ChannelFor

from viam.proto.common import DoCommandRequest, DoCommandResponse, Pose
from viam.proto.service.slam import GetInternalStateRequest, GetPointCloudMapRequest, GetPositionRequest, SLAMServiceStub
from viam.resource.manager import ResourceManager
from viam.services.slam import SLAMServiceClient
from viam.services.slam.service import SLAMService
from viam.utils import dict_to_struct, struct_to_dict

from .mocks.services import MockSLAM

INTERNAL_STATE_CHUNKS = [bytes(5), bytes(2)]
POINT_CLOUD_CHUNKS = [bytes(3), bytes(2)]
POSITION = Pose(x=1, y=2, z=3, o_x=2, o_y=3, o_z=4, theta=20)


class TestSLAM:
    name = "slam"
    slam = MockSLAM(name="slam")

    @pytest.mark.asyncio
    async def test_get_internal_state_chunks(self):
        chunks = await self.slam.get_internal_state(self.name)
        assert chunks == INTERNAL_STATE_CHUNKS

    @pytest.mark.asyncio
    async def test_get_point_cloud_map(self):
        chunks = await self.slam.get_point_cloud_map(self.name)
        assert chunks == POINT_CLOUD_CHUNKS

    @pytest.mark.asyncio
    async def test_get_position(self):
        pos = await self.slam.get_position(self.name)
        assert pos == POSITION

    @pytest.mark.asyncio
    async def test_do(self):
        command = {"command": "args"}
        resp = await self.slam.do_command(command)
        assert resp == {"command": command}


class TestServer:
    @classmethod
    def setup_class(cls):
        cls.name = "slam"
        cls.slam = MockSLAM(name=cls.name)
        cls.manager = ResourceManager([cls.slam])
        cls.service = SLAMService(cls.manager)

    @pytest.mark.asyncio
    async def test_get_internal_state(self):
        async with ChannelFor([self.service]) as channel:
            client = SLAMServiceStub(channel)
            request = GetInternalStateRequest(name=self.name)
            await client.GetInternalState(request)
            assert self.slam.internal_state_chunks == INTERNAL_STATE_CHUNKS

    @pytest.mark.asyncio
    async def test_get_point_cloud_map(self):
        async with ChannelFor([self.service]) as channel:
            client = SLAMServiceStub(channel)
            request = GetPointCloudMapRequest(name=self.name)
            await client.GetPointCloudMap(request)
            assert self.slam.point_cloud_pcd_chunks == POINT_CLOUD_CHUNKS

    @pytest.mark.asyncio
    async def test_get_position(self):
        async with ChannelFor([self.service]) as channel:
            client = SLAMServiceStub(channel)
            request = GetPositionRequest(name=self.name)
            await client.GetPosition(request)
            assert self.slam.position == POSITION

    @pytest.mark.asyncio
    async def test_do(self):
        async with ChannelFor([self.service]) as channel:
            client = SLAMServiceStub(channel)
            command = {"command": "args"}
            request = DoCommandRequest(name=self.name, command=dict_to_struct(command))
            response: DoCommandResponse = await client.DoCommand(request)
            result = struct_to_dict(response.result)
            assert result == {"command": command}


class TestClient:
    @classmethod
    def setup_class(cls):
        cls.name = "slam"
        cls.slam = MockSLAM(name=cls.name)
        cls.manager = ResourceManager([cls.slam])
        cls.service = SLAMService(cls.manager)

    @pytest.mark.asyncio
    async def test_get_internal_state(self):
        async with ChannelFor([self.service]) as channel:
            client = SLAMServiceClient(self.name, channel)
            response = await client.get_internal_state(self.name)
            assert len(response) == len(INTERNAL_STATE_CHUNKS)
            for i, chunk in enumerate(response):
                assert chunk.internal_state_chunk == INTERNAL_STATE_CHUNKS[i]

    @pytest.mark.asyncio
    async def test_get_point_cloud_map(self):
        async with ChannelFor([self.service]) as channel:
            client = SLAMServiceClient(self.name, channel)
            response = await client.get_point_cloud_map(self.name)
            assert len(response) == len(POINT_CLOUD_CHUNKS)
            for i, chunk in enumerate(response):
                assert chunk.point_cloud_pcd_chunk == POINT_CLOUD_CHUNKS[i]

    @pytest.mark.asyncio
    async def test_get_position(self):
        async with ChannelFor([self.service]) as channel:
            client = SLAMServiceClient(self.name, channel)
            response = await client.get_position(self.name)
            assert response == POSITION

    @pytest.mark.asyncio
    async def test_do(self):
        async with ChannelFor([self.service]) as channel:
            client = SLAMServiceClient(self.name, channel)
            command = {"command": "args"}
            response = await client.do_command(command)
            assert response == {"command": command}
