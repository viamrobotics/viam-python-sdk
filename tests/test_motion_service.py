import pytest
from grpclib.testing import ChannelFor

from viam.components.arm import Arm
from viam.components.gantry import Gantry
from viam.proto.common import Pose, PoseInFrame
from viam.proto.service.motion import Constraints, LinearConstraint
from viam.services.motion import MotionClient

from . import loose_approx
from .mocks.services import MockMotionService

MOVE_CONSTRAINTS = Constraints(linear_constraint=[LinearConstraint(), LinearConstraint(line_tolerance_mm=2)])
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
            client = MotionClient(MOTION_SERVICE_NAME, channel)
            assert service.timeout is None
            assert service.constraints is None
            timeout = 1.4
            success = await client.move(
                Arm.get_resource_name("arm"), PoseInFrame(), constraints=MOVE_CONSTRAINTS, extra={"foo": "bar"}, timeout=timeout
            )
            assert success == MOVE_RESPONSES["arm"]
            assert service.extra == {"foo": "bar"}
            assert service.timeout == loose_approx(timeout)
            assert service.constraints is not None
            assert service.constraints.linear_constraint == [LinearConstraint(), LinearConstraint(line_tolerance_mm=2)]
            success = await client.move(Gantry.get_resource_name("gantry"), PoseInFrame())
            assert success == MOVE_RESPONSES["gantry"]
            assert service.extra == {}
            assert service.timeout is None

    @pytest.mark.asyncio
    async def test_move_single_component(self, service: MockMotionService):
        async with ChannelFor([service]) as channel:
            client = MotionClient(MOTION_SERVICE_NAME, channel)
            success = await client.move_single_component(Arm.get_resource_name("arm"), PoseInFrame(), extra={"foo": "bar"})
            assert success == MOVE_SINGLE_COMPONENT_RESPONSES["arm"]
            assert service.extra == {"foo": "bar"}
            success = await client.move_single_component(Gantry.get_resource_name("gantry"), PoseInFrame())
            assert success == MOVE_SINGLE_COMPONENT_RESPONSES["gantry"]
            assert service.extra == {}

    @pytest.mark.asyncio
    async def test_get_pose(self, service: MockMotionService):
        async with ChannelFor([service]) as channel:
            client = MotionClient(MOTION_SERVICE_NAME, channel)
            pose = await client.get_pose(Arm.get_resource_name("arm"), "x", extra={"foo": "bar"})
            assert pose == GET_POSE_RESPONSES["arm"]
            assert service.extra == {"foo": "bar"}
            pose = await client.get_pose(Gantry.get_resource_name("gantry"), "y")
            assert pose == GET_POSE_RESPONSES["gantry"]
            assert service.extra == {}

    @pytest.mark.asyncio
    async def test_do(self, service: MockMotionService):
        async with ChannelFor([service]) as channel:
            client = MotionClient(MOTION_SERVICE_NAME, channel)
            command = {"command": "args"}
            response = await client.do_command(command)
            assert response == command
