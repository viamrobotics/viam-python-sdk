import pytest
from grpclib.testing import ChannelFor

from viam.components.arm import Arm
from viam.components.gantry import Gantry
from viam.proto.common import GeoObstacle, GeoPoint, Pose, PoseInFrame, ResourceName
from viam.proto.service.motion import Constraints, LinearConstraint, MotionConfiguration
from viam.services.motion import MotionClient

from . import loose_approx
from .mocks.services import MockMotion

MOVE_CONSTRAINTS = Constraints(linear_constraint=[LinearConstraint(), LinearConstraint(line_tolerance_mm=2)])
MOVE_RESPONSES = {"arm": False, "gantry": True}
GET_POSE_RESPONSES = {
    "arm": PoseInFrame(reference_frame="arm", pose=Pose(x=1, y=2, z=3, o_x=2, o_y=3, o_z=4, theta=20)),
    "gantry": PoseInFrame(reference_frame="gantry", pose=Pose(x=2, y=3, z=4, o_x=3, o_y=4, o_z=5, theta=21)),
}
MOTION_CONFIGURATION = MotionConfiguration(
    vision_services=[ResourceName(namespace="rdk", type="service", subtype="vision", name="viz1")],
    position_polling_frequency_hz=144,
    obstacle_polling_frequency_hz=182,
    plan_deviation_m=41,
    linear_m_per_sec=44,
    angular_degs_per_sec=10,
)

MOTION_SERVICE_NAME = "motion1"


@pytest.fixture(scope="function")
def service() -> MockMotion:
    return MockMotion(
        move_responses=MOVE_RESPONSES,
        get_pose_responses=GET_POSE_RESPONSES,
    )


class TestClient:
    @pytest.mark.asyncio
    async def test_plan_and_move(self, service: MockMotion):
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
    async def test_get_pose(self, service: MockMotion):
        async with ChannelFor([service]) as channel:
            client = MotionClient(MOTION_SERVICE_NAME, channel)
            pose = await client.get_pose(Arm.get_resource_name("arm"), "x", extra={"foo": "bar"})
            assert pose == GET_POSE_RESPONSES["arm"]
            assert service.extra == {"foo": "bar"}
            pose = await client.get_pose(Gantry.get_resource_name("gantry"), "y")
            assert pose == GET_POSE_RESPONSES["gantry"]
            assert service.extra == {}

    @pytest.mark.asyncio
    async def test_move_on_map(self, service: MockMotion):
        component_rn = Arm.get_resource_name("move_on_map_arm")
        slam_rn = ResourceName(namespace="rdk", type="service", subtype="slam", name="move_on_map_slam")
        async with ChannelFor([service]) as channel:
            client = MotionClient(MOTION_SERVICE_NAME, channel)
            success = await client.move_on_map(component_rn, Pose(), slam_service_name=slam_rn)
            assert service.component_name == component_rn
            assert service.slam_service == slam_rn
            assert success

    @pytest.mark.asyncio
    async def test_move_on_globe(self, service: MockMotion):
        component_rn = Arm.get_resource_name("move_on_globe_arm")
        movement_rn = ResourceName(namespace="rdk", type="component", subtype="movement_sensor", name="move_on_globe_ms")
        destination = GeoPoint(latitude=123, longitude=456)
        obstacles = [GeoObstacle(location=GeoPoint(latitude=111, longitude=222))]
        async with ChannelFor([service]) as channel:
            client = MotionClient(MOTION_SERVICE_NAME, channel)
            success = await client.move_on_globe(
                component_rn,
                destination,
                movement_rn,
                obstacles,
                heading=182,
                configuration=MOTION_CONFIGURATION,
            )
            assert service.component_name == component_rn
            assert service.movement_sensor == movement_rn
            assert service.destination == destination
            assert service.obstacles == obstacles
            assert service.heading == 182
            assert service.configuration == MOTION_CONFIGURATION
            assert success

    @pytest.mark.asyncio
    async def test_do(self, service: MockMotion):
        async with ChannelFor([service]) as channel:
            client = MotionClient(MOTION_SERVICE_NAME, channel)
            command = {"command": "args"}
            response = await client.do_command(command)
            assert response == command
