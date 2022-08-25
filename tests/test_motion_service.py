import pytest
from grpclib.testing import ChannelFor

from viam.components.arm import Arm
from viam.components.gantry import Gantry
from viam.proto.api.common import Pose, PoseInFrame
from viam.services.motion import MotionServiceClient

from .mocks.services import MockMotionService

MOVE_RESPONSES = {"arm": False, "gantry": True}
MOVE_SINGLE_COMPONENT_RESPONSES = {"arm": True, "gantry": False}
GET_POSE_RESPONSES = {
    "arm": PoseInFrame(reference_frame="arm", pose=Pose(x=1, y=2, z=3, o_x=2, o_y=3, o_z=4, theta=20)),
    "gantry": PoseInFrame(reference_frame="gantry", pose=Pose(x=2, y=3, z=4, o_x=3, o_y=4, o_z=5, theta=21)),
}

MOTION_SERVICE_NAME = "motion1"


@pytest.fixture(scope="function")
def service() -> MockMotionService:
    return MockMotionService(
        move_responses=MOVE_RESPONSES,
        move_single_component_responses=MOVE_SINGLE_COMPONENT_RESPONSES,
        get_pose_responses=GET_POSE_RESPONSES,
    )


class TestClient:
    @pytest.mark.asyncio
    async def test_plan_and_move(self, service: MockMotionService):
        async with ChannelFor([service]) as channel:
            client = MotionServiceClient(channel)
            success = await client.move(MOTION_SERVICE_NAME, Arm.get_resource_name("arm"), PoseInFrame())
            assert success == MOVE_RESPONSES["arm"]
            success = await client.move(MOTION_SERVICE_NAME, Gantry.get_resource_name("gantry"), PoseInFrame())
            assert success == MOVE_RESPONSES["gantry"]

    @pytest.mark.asyncio
    async def test_move_single_component(self, service: MockMotionService):
        async with ChannelFor([service]) as channel:
            client = MotionServiceClient(channel)
            success = await client.move_single_component(MOTION_SERVICE_NAME, Arm.get_resource_name("arm"), PoseInFrame())
            assert success == MOVE_SINGLE_COMPONENT_RESPONSES["arm"]
            success = await client.move_single_component(MOTION_SERVICE_NAME, Gantry.get_resource_name("gantry"), PoseInFrame())
            assert success == MOVE_SINGLE_COMPONENT_RESPONSES["gantry"]

    @pytest.mark.asyncio
    async def test_get_pose(self, service: MockMotionService):
        async with ChannelFor([service]) as channel:
            client = MotionServiceClient(channel)
            pose = await client.get_pose(MOTION_SERVICE_NAME, Arm.get_resource_name("arm"), "x")
            assert pose == GET_POSE_RESPONSES["arm"]
            pose = await client.get_pose(MOTION_SERVICE_NAME, Gantry.get_resource_name("gantry"), "y")
            assert pose == GET_POSE_RESPONSES["gantry"]
