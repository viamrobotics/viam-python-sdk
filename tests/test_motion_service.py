from typing import Any, Iterable, Mapping
from unittest.mock import patch

import pytest
from google.protobuf.timestamp_pb2 import Timestamp
from grpclib.testing import ChannelFor
from pytest_mock import MockerFixture

from viam.components.arm import Arm
from viam.components.base import Base
from viam.components.gantry import Gantry
from viam.gen.service.motion.v1.motion_pb2 import (
    PLAN_STATE_FAILED,
    PLAN_STATE_IN_PROGRESS,
    PLAN_STATE_STOPPED,
    PLAN_STATE_SUCCEEDED,
    ComponentState,
    GetPlanResponse,
    ListPlanStatusesResponse,
    Plan,
    PlanStatus,
    PlanStatusWithID,
    PlanStep,
    PlanWithStatus,
)
from viam.proto.common import GeoGeometry, Geometry, GeoPoint, Pose, PoseInFrame, ResourceName, Transform, WorldState
from viam.proto.service.motion import Constraints, LinearConstraint, MotionConfiguration, ObstacleDetector
from viam.resource.manager import ResourceManager
from viam.services.motion import MotionClient
from viam.services.motion.motion import Motion
from viam.services.motion.service import MotionRPCService
from viam.utils import ValueTypes

from . import loose_approx

# from .mocks.services import MockMotion

MOVE_CONSTRAINTS = Constraints(linear_constraint=[LinearConstraint(), LinearConstraint(line_tolerance_mm=2)])
GET_POSE_RESPONSE = PoseInFrame(reference_frame="arm", pose=Pose(x=1, y=2, z=3, o_x=2, o_y=3, o_z=4, theta=20))
MOVE_ON_MAP_RESPONSE = "Move On Map Response"

GET_PLAN_RESPONSE = GetPlanResponse(
    current_plan_with_status=PlanWithStatus(
        plan=Plan(
            id="plan_id2",
            component_name=Base.get_resource_name("get_plan_base"),
            execution_id="execution_id",
            steps=[
                PlanStep(step={"get_plan_base": ComponentState(pose=Pose(x=2, y=3, z=4, o_x=3, o_y=4, o_z=5, theta=21))}),
                PlanStep(step={"get_plan_base": ComponentState(pose=Pose(x=6, y=7, z=8, o_x=9, o_y=10, o_z=11, theta=23))}),
            ],
        ),
        status=PlanStatus(state=PLAN_STATE_SUCCEEDED, timestamp=Timestamp(seconds=4)),
        status_history=[PlanStatus(state=PLAN_STATE_IN_PROGRESS, timestamp=Timestamp(seconds=3))],
    ),
    replan_history=[
        PlanWithStatus(
            plan=Plan(
                id="plan_id1",
                component_name=Base.get_resource_name("get_plan_base"),
                execution_id="execution_id",
                steps=[
                    PlanStep(step={"get_plan_base": ComponentState(pose=Pose(x=1, y=1, z=1, o_x=1, o_y=1, o_z=1, theta=20))}),
                    PlanStep(step={"get_plan_base": ComponentState(pose=Pose(x=2, y=3, z=4, o_x=3, o_y=4, o_z=5, theta=21))}),
                    PlanStep(step={"get_plan_base": ComponentState(pose=Pose(x=6, y=7, z=8, o_x=9, o_y=10, o_z=11, theta=23))}),
                ],
            ),
            status=PlanStatus(state=PLAN_STATE_FAILED, reason="failure reason", timestamp=Timestamp(seconds=2)),
            status_history=[PlanStatus(state=PLAN_STATE_IN_PROGRESS, timestamp=Timestamp(seconds=1))],
        )
    ],
)

LIST_PLAN_STATUSES_RESPONSE = ListPlanStatusesResponse(
    plan_statuses_with_ids=[
        PlanStatusWithID(
            plan_id="plan 5",
            component_name=Base.get_resource_name("list_plan_statuses_base"),
            execution_id="execution_id 3",
            status=PlanStatus(state=PLAN_STATE_IN_PROGRESS, timestamp=Timestamp(seconds=10)),
        ),
        PlanStatusWithID(
            plan_id="plan 4",
            component_name=Base.get_resource_name("list_plan_statuses_base"),
            execution_id="execution_id 2",
            status=PlanStatus(state=PLAN_STATE_SUCCEEDED, timestamp=Timestamp(seconds=9)),
        ),
        PlanStatusWithID(
            plan_id="plan 3",
            component_name=Base.get_resource_name("list_plan_statuses_base"),
            execution_id="execution_id 2",
            status=PlanStatus(state=PLAN_STATE_FAILED, reason="other failure reason", timestamp=Timestamp(seconds=8)),
        ),
        PlanStatusWithID(
            plan_id="plan 2",
            component_name=Base.get_resource_name("list_plan_statuses_base"),
            execution_id="execution_id 2",
            status=PlanStatus(state=PLAN_STATE_FAILED, reason="failure reason", timestamp=Timestamp(seconds=7)),
        ),
        PlanStatusWithID(
            plan_id="plan 1",
            component_name=Base.get_resource_name("list_plan_statuses_base"),
            execution_id="execution_id 1",
            status=PlanStatus(state=PLAN_STATE_STOPPED, timestamp=Timestamp(seconds=6)),
        ),
    ]
)

MOTION_CONFIGURATION = MotionConfiguration(
    obstacle_detectors=[
        ObstacleDetector(
            vision_service=ResourceName(namespace="rdk", type="service", subtype="vision", name="viz1"),
            camera=ResourceName(namespace="rdk", type="component", subtype="camera", name="cam1"),
        )
    ],
    position_polling_frequency_hz=144,
    obstacle_polling_frequency_hz=182,
    plan_deviation_m=41,
    linear_m_per_sec=44,
    angular_degs_per_sec=10,
)

MOTION_SERVICE_NAME = "motion1"


@pytest.fixture(scope="function")
def motion():
    class MockMotion(Motion):
        async def move(
            self,
            component_name: ResourceName,
            destination: PoseInFrame,
            world_state: WorldState | None = None,
            constraints: Constraints | None = None,
            *,
            extra: Mapping[str, Any] | None = None,
            timeout: float | None = None
        ) -> bool:
            raise NotImplementedError

        async def move_on_globe(
            self,
            component_name: ResourceName,
            destination: GeoPoint,
            movement_sensor_name: ResourceName,
            obstacles: Iterable[GeoGeometry] | None = None,
            heading: float | None = None,
            configuration: MotionConfiguration | None = None,
            *,
            bounding_regions: Iterable[GeoGeometry] | None = None,
            extra: Mapping[str, ValueTypes] | None = None,
            timeout: float | None = None
        ) -> str:
            raise NotImplementedError

        async def move_on_map(
            self,
            component_name: ResourceName,
            destination: Pose,
            slam_service_name: ResourceName,
            configuration: MotionConfiguration | None = None,
            obstacles: Iterable[Geometry] | None = None,
            *,
            extra: Mapping[str, ValueTypes] | None = None,
            timeout: float | None = None
        ) -> str:
            raise NotImplementedError

        async def stop_plan(
            self, component_name: ResourceName, *, extra: Mapping[str, ValueTypes] | None = None, timeout: float | None = None
        ):
            raise NotImplementedError

        async def get_plan(
            self,
            component_name: ResourceName,
            last_plan_only: bool = False,
            execution_id: str | None = None,
            *,
            extra: Mapping[str, ValueTypes] | None = None,
            timeout: float | None = None
        ) -> GetPlanResponse:
            raise NotImplementedError

        async def list_plan_statuses(
            self, only_active_plans: bool = False, *, extra: Mapping[str, ValueTypes] | None = None, timeout: float | None = None
        ) -> ListPlanStatusesResponse:
            raise NotImplementedError

        async def get_pose(
            self,
            component_name: ResourceName,
            destination_frame: str,
            supplemental_transforms: Iterable[Transform] | None = None,
            *,
            extra: Mapping[str, Any] | None = None,
            timeout: float | None = None
        ) -> PoseInFrame:
            raise NotImplementedError

    return MockMotion(MOTION_SERVICE_NAME)


@pytest.fixture(scope="function")
def service(motion: Motion) -> MotionRPCService:
    return MotionRPCService(ResourceManager([motion]))


class TestMotionService:
    @pytest.mark.asyncio
    async def test_move(self, motion: Motion, service: MotionRPCService):
        with patch.object(motion, "move") as patched_method:
            patched_method.return_value = True
            async with ChannelFor([service]) as channel:
                client = MotionClient(MOTION_SERVICE_NAME, channel)
                resource_name = Arm.get_resource_name("arm")
                timeout = 2
                success = await client.move(
                    resource_name, PoseInFrame(), constraints=MOVE_CONSTRAINTS, extra={"foo": "bar"}, timeout=timeout
                )
                assert success is True
                patched_method.assert_called_once()
                assert patched_method.call_args.args[0] == resource_name
                assert patched_method.call_args.args[1] == PoseInFrame()
                assert patched_method.call_args.args[2] == WorldState()
                assert patched_method.call_args.args[3] == MOVE_CONSTRAINTS
                assert patched_method.call_args.kwargs["extra"] == {"foo": "bar"}
                assert patched_method.call_args.kwargs["timeout"] == loose_approx(timeout)

    @pytest.mark.asyncio
    async def test_get_pose(self, motion: Motion, service: MotionRPCService):
        with patch.object(motion, "get_pose") as patched_method:
            patched_method.return_value = GET_POSE_RESPONSE
            async with ChannelFor([service]) as channel:
                client = MotionClient(MOTION_SERVICE_NAME, channel)
                rn = Arm.get_resource_name("arm")
                destination_frame = "x"
                transforms = [Transform(reference_frame="y")]
                extra = {"foo": "bar"}
                pose = await client.get_pose(rn, destination_frame, transforms, extra=extra, timeout=3)
                assert pose == GET_POSE_RESPONSE
                patched_method.assert_called_once()
                assert patched_method.call_args.args[0] == rn
                assert patched_method.call_args.args[1] == destination_frame
                assert patched_method.call_args.args[2] == transforms
                assert patched_method.call_args.kwargs["extra"] == extra
                assert patched_method.call_args.kwargs["timeout"] == loose_approx(3)

    @pytest.mark.asyncio
    async def test_move_on_map(self, motion: Motion, service: MotionRPCService):
        with patch.object(motion, "move_on_map") as patched_method:
            patched_method.return_value = MOVE_ON_MAP_RESPONSE
            async with ChannelFor([service]) as channel:
                client = MotionClient(MOTION_SERVICE_NAME, channel)
                component_rn = Base.get_resource_name("move_on_globe_base")
                destination = Pose(x=1, y=2, z=3, theta=4)
                slam_rn = ResourceName(namespace="rdk", type="service", subtype="slam", name="move_on_map_slam")
                obstacles = [Geometry(center=Pose(x=9, y=8, z=7, theta=6))]
                extra = {"foo": "bar"}
                timeout = 4
                execution_id = await client.move_on_map(
                    component_rn,
                    destination,
                    slam_service_name=slam_rn,
                    configuration=MOTION_CONFIGURATION,
                    obstacles=obstacles,
                    extra=extra,
                    timeout=timeout,
                )
                assert execution_id == MOVE_ON_MAP_RESPONSE
                patched_method.assert_called_once()
                assert patched_method.call_args.args[0] == component_rn
                assert patched_method.call_args.args[1] == destination
                assert patched_method.call_args.args[2] == slam_rn
                assert patched_method.call_args.args[3] == MOTION_CONFIGURATION
                assert patched_method.call_args.args[4] == obstacles
                assert patched_method.call_args.kwargs["extra"] == extra
                assert patched_method.call_args.kwargs["timeout"] == loose_approx(timeout)

    # @pytest.mark.asyncio
    # async def test_move_on_globe(self, service: MockMotion):
    #     component_rn = Base.get_resource_name("move_on_globe_base")
    #     movement_rn = ResourceName(namespace="rdk", type="component", subtype="movement_sensor", name="move_on_globe_ms")
    #     destination = GeoPoint(latitude=123, longitude=456)
    #     obstacles = [GeoGeometry(location=GeoPoint(latitude=111, longitude=222))]
    #     bounding_regions = [GeoGeometry(location=GeoPoint(latitude=3, longitude=4))]
    #     async with ChannelFor([service]) as channel:
    #         client = MotionClient(MOTION_SERVICE_NAME, channel)
    #         execution_id = await client.move_on_globe(
    #             component_rn,
    #             destination,
    #             movement_rn,
    #             obstacles,
    #             heading=182,
    #             configuration=MOTION_CONFIGURATION,
    #         )
    #         assert service.component_name == component_rn
    #         assert service.movement_sensor == movement_rn
    #         assert service.destination == destination
    #         assert service.obstacles == obstacles
    #         assert service.heading == 182
    #         assert service.configuration == MOTION_CONFIGURATION
    #         assert service.execution_id == execution_id
    #         assert service.extra == {}
    #         assert service.timeout is None
    #         timeout = 50
    #         extra = {"max_iter": 1}
    #         execution_id = await client.move_on_globe(
    #             component_rn,
    #             destination,
    #             movement_rn,
    #             obstacles,
    #             heading=182,
    #             configuration=MOTION_CONFIGURATION,
    #             extra=extra,
    #             bounding_regions=bounding_regions,
    #             timeout=timeout,
    #         )
    #         assert service.component_name == component_rn
    #         assert service.movement_sensor == movement_rn
    #         assert service.destination == destination
    #         assert service.obstacles == obstacles
    #         assert service.heading == 182
    #         assert service.configuration == MOTION_CONFIGURATION
    #         assert service.bounding_regions == bounding_regions
    #         assert service.execution_id == execution_id
    #         assert service.extra == extra
    #         assert service.timeout == loose_approx(timeout)

    # @pytest.mark.asyncio
    # async def test_stop_plan(self, service: MockMotion):
    #     component_rn = Base.get_resource_name("stop_plan_base")
    #     async with ChannelFor([service]) as channel:
    #         client = MotionClient(MOTION_SERVICE_NAME, channel)
    #         await client.stop_plan(component_rn)
    #         assert service.component_name == component_rn
    #         assert service.extra == {}
    #         assert service.timeout is None
    #         timeout = 50
    #         extra = {"max_iter": 1}
    #         await client.stop_plan(component_rn, extra=extra, timeout=timeout)
    #         assert service.component_name == component_rn
    #         assert service.extra == extra
    #         assert service.timeout == loose_approx(timeout)

    # @pytest.mark.asyncio
    # async def test_get_plan(self, service: MockMotion):
    #     component_rn = Base.get_resource_name("get_plan_base")
    #     async with ChannelFor([service]) as channel:
    #         client = MotionClient(MOTION_SERVICE_NAME, channel)
    #         response = await client.get_plan(component_rn)
    #         assert service.component_name == component_rn
    #         assert not service.last_plan_only
    #         assert service.execution_id == ""
    #         assert service.extra == {}
    #         assert service.timeout is None
    #         assert response == GET_PLAN_RESPONSE
    #         last_plan_only = True
    #         execution_id = "execution_id"
    #         timeout = 50
    #         extra = {"some": "extra"}
    #         response = await client.get_plan(
    #             component_rn,
    #             last_plan_only=last_plan_only,
    #             execution_id=execution_id,
    #             extra=extra,
    #             timeout=timeout,
    #         )
    #         assert service.component_name == component_rn
    #         assert service.last_plan_only == last_plan_only
    #         assert service.execution_id == execution_id
    #         assert service.extra == extra
    #         assert service.timeout == loose_approx(timeout)
    #         assert response == GET_PLAN_RESPONSE

    # @pytest.mark.asyncio
    # async def test_list_plan_statuses(self, service: MockMotion):
    #     async with ChannelFor([service]) as channel:
    #         client = MotionClient(MOTION_SERVICE_NAME, channel)
    #         response = await client.list_plan_statuses()
    #         assert not service.only_active_plans
    #         assert service.extra == {}
    #         assert service.timeout is None
    #         assert response == LIST_PLAN_STATUSES_RESPONSE
    #         only_active_plans = True
    #         timeout = 50
    #         extra = {"some": "extra"}
    #         response = await client.list_plan_statuses(
    #             only_active_plans=only_active_plans,
    #             extra=extra,
    #             timeout=timeout,
    #         )
    #         assert service.only_active_plans == only_active_plans
    #         assert service.extra == extra
    #         assert service.timeout == loose_approx(timeout)
    #         assert response == LIST_PLAN_STATUSES_RESPONSE

    # @pytest.mark.asyncio
    # async def test_do(self, service: MockMotion):
    #     async with ChannelFor([service]) as channel:
    #         client = MotionClient(MOTION_SERVICE_NAME, channel)
    #         command = {"command": "args"}
    #         response = await client.do_command(command)
    #         assert response == command


# class TestClient:
#     @pytest.mark.asyncio
#     async def test_plan_and_move(self, service: MockMotion):
#         async with ChannelFor([service]) as channel:
#             client = MotionClient(MOTION_SERVICE_NAME, channel)
#             assert service.timeout is None
#             assert service.constraints is None
#             timeout = 1.4
#             success = await client.move(
#                 Arm.get_resource_name("arm"), PoseInFrame(), constraints=MOVE_CONSTRAINTS, extra={"foo": "bar"}, timeout=timeout
#             )
#             assert success == MOVE_RESPONSES["arm"]
#             assert service.extra == {"foo": "bar"}
#             assert service.timeout == loose_approx(timeout)
#             assert service.constraints is not None
#             assert service.constraints.linear_constraint == [LinearConstraint(), LinearConstraint(line_tolerance_mm=2)]
#             success = await client.move(Gantry.get_resource_name("gantry"), PoseInFrame())
#             assert success == MOVE_RESPONSES["gantry"]
#             assert service.extra == {}
#             assert service.timeout is None

#     @pytest.mark.asyncio
#     async def test_get_pose(self, service: MockMotion):
#         async with ChannelFor([service]) as channel:
#             client = MotionClient(MOTION_SERVICE_NAME, channel)
#             pose = await client.get_pose(Arm.get_resource_name("arm"), "x", extra={"foo": "bar"})
#             assert pose == GET_POSE_RESPONSES["arm"]
#             assert service.extra == {"foo": "bar"}
#             pose = await client.get_pose(Gantry.get_resource_name("gantry"), "y")
#             assert pose == GET_POSE_RESPONSES["gantry"]
#             assert service.extra == {}

#     @pytest.mark.asyncio
#     async def test_move_on_map(self, service: MockMotion):
#         component_rn = Base.get_resource_name("move_on_globe_base")
#         slam_rn = ResourceName(namespace="rdk", type="service", subtype="slam", name="move_on_map_slam")
#         async with ChannelFor([service]) as channel:
#             client = MotionClient(MOTION_SERVICE_NAME, channel)
#             execution_id = await client.move_on_map(
#                 component_rn,
#                 Pose(),
#                 slam_service_name=slam_rn,
#                 configuration=MOTION_CONFIGURATION,
#             )
#             assert service.component_name == component_rn
#             assert service.slam_service == slam_rn
#             assert service.execution_id == execution_id
#             assert service.extra == {}
#             assert service.timeout is None
#             timeout = 50
#             extra = {"max_iter": 1}
#             execution_id = await client.move_on_map(
#                 component_rn,
#                 Pose(),
#                 slam_service_name=slam_rn,
#                 configuration=MOTION_CONFIGURATION,
#                 extra=extra,
#                 timeout=timeout,
#             )
#             assert service.component_name == component_rn
#             assert service.slam_service == slam_rn
#             assert service.execution_id == execution_id
#             assert service.extra == extra
#             assert service.timeout == loose_approx(timeout)

#     @pytest.mark.asyncio
#     async def test_move_on_globe(self, service: MockMotion):
#         component_rn = Base.get_resource_name("move_on_globe_base")
#         movement_rn = ResourceName(namespace="rdk", type="component", subtype="movement_sensor", name="move_on_globe_ms")
#         destination = GeoPoint(latitude=123, longitude=456)
#         obstacles = [GeoGeometry(location=GeoPoint(latitude=111, longitude=222))]
#         bounding_regions = [GeoGeometry(location=GeoPoint(latitude=3, longitude=4))]
#         async with ChannelFor([service]) as channel:
#             client = MotionClient(MOTION_SERVICE_NAME, channel)
#             execution_id = await client.move_on_globe(
#                 component_rn,
#                 destination,
#                 movement_rn,
#                 obstacles,
#                 heading=182,
#                 configuration=MOTION_CONFIGURATION,
#             )
#             assert service.component_name == component_rn
#             assert service.movement_sensor == movement_rn
#             assert service.destination == destination
#             assert service.obstacles == obstacles
#             assert service.heading == 182
#             assert service.configuration == MOTION_CONFIGURATION
#             assert service.execution_id == execution_id
#             assert service.extra == {}
#             assert service.timeout is None
#             timeout = 50
#             extra = {"max_iter": 1}
#             execution_id = await client.move_on_globe(
#                 component_rn,
#                 destination,
#                 movement_rn,
#                 obstacles,
#                 heading=182,
#                 configuration=MOTION_CONFIGURATION,
#                 extra=extra,
#                 bounding_regions=bounding_regions,
#                 timeout=timeout,
#             )
#             assert service.component_name == component_rn
#             assert service.movement_sensor == movement_rn
#             assert service.destination == destination
#             assert service.obstacles == obstacles
#             assert service.heading == 182
#             assert service.configuration == MOTION_CONFIGURATION
#             assert service.bounding_regions == bounding_regions
#             assert service.execution_id == execution_id
#             assert service.extra == extra
#             assert service.timeout == loose_approx(timeout)

#     @pytest.mark.asyncio
#     async def test_stop_plan(self, service: MockMotion):
#         component_rn = Base.get_resource_name("stop_plan_base")
#         async with ChannelFor([service]) as channel:
#             client = MotionClient(MOTION_SERVICE_NAME, channel)
#             await client.stop_plan(component_rn)
#             assert service.component_name == component_rn
#             assert service.extra == {}
#             assert service.timeout is None
#             timeout = 50
#             extra = {"max_iter": 1}
#             await client.stop_plan(component_rn, extra=extra, timeout=timeout)
#             assert service.component_name == component_rn
#             assert service.extra == extra
#             assert service.timeout == loose_approx(timeout)

#     @pytest.mark.asyncio
#     async def test_get_plan(self, service: MockMotion):
#         component_rn = Base.get_resource_name("get_plan_base")
#         async with ChannelFor([service]) as channel:
#             client = MotionClient(MOTION_SERVICE_NAME, channel)
#             response = await client.get_plan(component_rn)
#             assert service.component_name == component_rn
#             assert not service.last_plan_only
#             assert service.execution_id == ""
#             assert service.extra == {}
#             assert service.timeout is None
#             assert response == GET_PLAN_RESPONSE
#             last_plan_only = True
#             execution_id = "execution_id"
#             timeout = 50
#             extra = {"some": "extra"}
#             response = await client.get_plan(
#                 component_rn,
#                 last_plan_only=last_plan_only,
#                 execution_id=execution_id,
#                 extra=extra,
#                 timeout=timeout,
#             )
#             assert service.component_name == component_rn
#             assert service.last_plan_only == last_plan_only
#             assert service.execution_id == execution_id
#             assert service.extra == extra
#             assert service.timeout == loose_approx(timeout)
#             assert response == GET_PLAN_RESPONSE

#     @pytest.mark.asyncio
#     async def test_list_plan_statuses(self, service: MockMotion):
#         async with ChannelFor([service]) as channel:
#             client = MotionClient(MOTION_SERVICE_NAME, channel)
#             response = await client.list_plan_statuses()
#             assert not service.only_active_plans
#             assert service.extra == {}
#             assert service.timeout is None
#             assert response == LIST_PLAN_STATUSES_RESPONSE
#             only_active_plans = True
#             timeout = 50
#             extra = {"some": "extra"}
#             response = await client.list_plan_statuses(
#                 only_active_plans=only_active_plans,
#                 extra=extra,
#                 timeout=timeout,
#             )
#             assert service.only_active_plans == only_active_plans
#             assert service.extra == extra
#             assert service.timeout == loose_approx(timeout)
#             assert response == LIST_PLAN_STATUSES_RESPONSE

#     @pytest.mark.asyncio
#     async def test_do(self, service: MockMotion):
#         async with ChannelFor([service]) as channel:
#             client = MotionClient(MOTION_SERVICE_NAME, channel)
#             command = {"command": "args"}
#             response = await client.do_command(command)
#             assert response == command
