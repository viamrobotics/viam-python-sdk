import pytest
from grpclib.testing import ChannelFor

from viam.components.generic.service import GenericService
from viam.components.pose_tracker import PoseTrackerClient
from viam.components.pose_tracker.service import PoseTrackerService
from viam.components.resource_manager import ResourceManager
from viam.proto.common import Pose, PoseInFrame
from viam.proto.component.posetracker import (
    GetPosesRequest,
    GetPosesResponse,
    PoseTrackerServiceStub,
)

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
        received_poses = await self.mock_pose_tracker.get_poses([], timeout=1.23)
        assert received_poses["0"] == PoseInFrame(reference_frame="0", pose=Pose(x=1, y=2, z=3, o_x=2, o_y=3, o_z=4, theta=20))
        assert received_poses["1"] == PoseInFrame(reference_frame="1", pose=Pose(x=5, y=5, z=5, o_x=5, o_y=3, o_z=4, theta=30))
        assert self.mock_pose_tracker.timeout == loose_approx(1.23)

    @pytest.mark.asyncio
    async def test_do(self):
        with pytest.raises(NotImplementedError):
            await self.mock_pose_tracker.do_command({"command": "args"})


class TestService:
    name = "pose_tracker"
    pose_tracker = MockPoseTracker(name=name, poses=POSES)
    manager = ResourceManager([pose_tracker])
    service = PoseTrackerService(manager)

    @pytest.mark.asyncio
    async def test_get_poses(self):
        async with ChannelFor([self.service]) as channel:
            client = PoseTrackerServiceStub(channel)
            request = GetPosesRequest(name=self.name)
            response: GetPosesResponse = await client.GetPoses(request, timeout=2.34)
            received_poses = response.body_poses
            assert received_poses["0"] == PoseInFrame(reference_frame="0", pose=Pose(x=1, y=2, z=3, o_x=2, o_y=3, o_z=4, theta=20))
            assert received_poses["1"] == PoseInFrame(reference_frame="1", pose=Pose(x=5, y=5, z=5, o_x=5, o_y=3, o_z=4, theta=30))
            assert self.pose_tracker.timeout == loose_approx(2.34)


class TestClient:

    name = "pose_tracker"
    pose_tracker = MockPoseTracker(name=name, poses=POSES)
    manager = ResourceManager([pose_tracker])
    service = PoseTrackerService(manager)

    @pytest.mark.asyncio
    async def test_get_poses(self):
        async with ChannelFor([self.service]) as channel:
            client = PoseTrackerClient(self.name, channel)
            received_poses = await client.get_poses([], timeout=3.45)
            assert received_poses["0"] == PoseInFrame(reference_frame="0", pose=Pose(x=1, y=2, z=3, o_x=2, o_y=3, o_z=4, theta=20))
            assert received_poses["1"] == PoseInFrame(reference_frame="1", pose=Pose(x=5, y=5, z=5, o_x=5, o_y=3, o_z=4, theta=30))
            assert self.pose_tracker.timeout == loose_approx(3.45)

    @pytest.mark.asyncio
    async def test_do(self):
        async with ChannelFor([self.service, GenericService(self.manager)]) as channel:
            client = PoseTrackerClient(self.name, channel)
            with pytest.raises(NotImplementedError):
                await client.do_command({"command": "args"})
