import pytest
from grpclib import GRPCError
from grpclib.testing import ChannelFor

from viam.components.pose_tracker import PoseTrackerClient
from viam.components.pose_tracker.service import PoseTrackerRPCService
from viam.resource.manager import ResourceManager
from viam.proto.common import DoCommandRequest, DoCommandResponse, GetGeometriesRequest, Pose, PoseInFrame
from viam.proto.component.posetracker import (
    GetPosesRequest,
    GetPosesResponse,
    PoseTrackerServiceStub,
)
from viam.utils import dict_to_struct, struct_to_dict

from . import loose_approx
from .mocks.components import MockPose, MockPoseTracker

POSES = [
    MockPose(X=1, Y=2, Z=3, o_X=2, o_Y=3, o_Z=4, theta=20),
    MockPose(X=5, Y=5, Z=5, o_X=5, o_Y=3, o_Z=4, theta=30),
]


class TestPoseTracker:
    mock_pose_tracker = MockPoseTracker(name="pt", poses=POSES)

    @pytest.mark.asyncio
    async def test_get_poses(self):
        assert self.mock_pose_tracker.extra is None
        received_poses = await self.mock_pose_tracker.get_poses([], extra={"foo": "get_poses"}, timeout=1.23)
        assert received_poses["0"] == PoseInFrame(reference_frame="0", pose=Pose(x=1, y=2, z=3, o_x=2, o_y=3, o_z=4, theta=20))
        assert received_poses["1"] == PoseInFrame(reference_frame="1", pose=Pose(x=5, y=5, z=5, o_x=5, o_y=3, o_z=4, theta=30))
        assert self.mock_pose_tracker.timeout == loose_approx(1.23)
        assert self.mock_pose_tracker.extra == {"foo": "get_poses"}

    @pytest.mark.asyncio
    async def test_do(self):
        command = {"command": "args"}
        resp = await self.mock_pose_tracker.do_command(command)
        assert resp == {"command": command}


class TestService:
    @classmethod
    def setup_class(cls):
        cls.name = "pose_tracker"
        cls.pose_tracker = MockPoseTracker(name=cls.name, poses=POSES)
        cls.manager = ResourceManager([cls.pose_tracker])
        cls.service = PoseTrackerRPCService(cls.manager)

    @pytest.mark.asyncio
    async def test_get_poses(self):
        assert self.pose_tracker.extra is None
        async with ChannelFor([self.service]) as channel:
            client = PoseTrackerServiceStub(channel)
            request = GetPosesRequest(name=self.name, extra=dict_to_struct({"foo": "get_poses"}))
            response: GetPosesResponse = await client.GetPoses(request, timeout=2.34)
            received_poses = response.body_poses
            assert received_poses["0"] == PoseInFrame(reference_frame="0", pose=Pose(x=1, y=2, z=3, o_x=2, o_y=3, o_z=4, theta=20))
            assert received_poses["1"] == PoseInFrame(reference_frame="1", pose=Pose(x=5, y=5, z=5, o_x=5, o_y=3, o_z=4, theta=30))
            assert self.pose_tracker.timeout == loose_approx(2.34)
            assert self.pose_tracker.extra == {"foo": "get_poses"}

    @pytest.mark.asyncio
    async def test_do(self):
        async with ChannelFor([self.service]) as channel:
            client = PoseTrackerServiceStub(channel)
            command = {"command": "args"}
            request = DoCommandRequest(name=self.name, command=dict_to_struct(command))
            response: DoCommandResponse = await client.DoCommand(request)
            result = struct_to_dict(response.result)
            assert result == {"command": command}

    @pytest.mark.asyncio
    async def test_get_geometries(self):
        async with ChannelFor([self.service]) as channel:
            client = PoseTrackerServiceStub(channel)
            request = GetGeometriesRequest()
            with pytest.raises(GRPCError, match=r"Method [a-zA-Z]+ not implemented"):
                await client.GetGeometries(request)


class TestClient:
    @classmethod
    def setup_class(cls):
        cls.name = "pose_tracker"
        cls.pose_tracker = MockPoseTracker(name=cls.name, poses=POSES)
        cls.manager = ResourceManager([cls.pose_tracker])
        cls.service = PoseTrackerRPCService(cls.manager)

    @pytest.mark.asyncio
    async def test_get_poses(self):
        assert self.pose_tracker.extra is None
        async with ChannelFor([self.service]) as channel:
            client = PoseTrackerClient(self.name, channel)
            received_poses = await client.get_poses([], extra={"foo": "get_poses"}, timeout=3.45)
            assert received_poses["0"] == PoseInFrame(reference_frame="0", pose=Pose(x=1, y=2, z=3, o_x=2, o_y=3, o_z=4, theta=20))
            assert received_poses["1"] == PoseInFrame(reference_frame="1", pose=Pose(x=5, y=5, z=5, o_x=5, o_y=3, o_z=4, theta=30))
            assert self.pose_tracker.timeout == loose_approx(3.45)
            assert self.pose_tracker.extra == {"foo": "get_poses"}

    @pytest.mark.asyncio
    async def test_do(self):
        async with ChannelFor([self.service]) as channel:
            client = PoseTrackerClient(self.name, channel)
            command = {"command": "args"}
            resp = await client.do_command(command)
            assert resp == {"command": command}
