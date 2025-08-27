from typing import Any, Mapping, Optional, Sequence
from unittest.mock import patch

import pytest
from google.protobuf.timestamp_pb2 import Timestamp
from grpclib.testing import ChannelFor

from viam.components.arm import Arm
from viam.components.base import Base
from viam.gen.service.motion.v1.motion_pb2 import (
    PLAN_STATE_FAILED,
    PLAN_STATE_IN_PROGRESS,
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
from viam.proto.service.motion import Constraints, LinearConstraint, MotionConfiguration, PseudolinearConstraint
from viam.resource.manager import ResourceManager
from viam.services.motion import MotionClient
from viam.services.motion.motion import Motion
from viam.services.motion.service import MotionRPCService
from viam.utils import ValueTypes

from . import loose_approx

MOTION_SERVICE_NAME = "motion1"


@pytest.fixture(scope="function")
def motion():
    class MockMotion(Motion):
        async def move(
            self,
            component_name: ResourceName,
            destination: PoseInFrame,
            world_state: Optional[WorldState] = None,
            constraints: Optional[Constraints] = None,
            *,
            extra: Optional[Mapping[str, Any]] = None,
            timeout: Optional[float] = None,
        ) -> bool:
            raise NotImplementedError

        async def move_on_globe(
            self,
            component_name: ResourceName,
            destination: GeoPoint,
            movement_sensor_name: ResourceName,
            obstacles: Optional[Sequence[GeoGeometry]] = None,
            heading: Optional[float] = None,
            configuration: Optional[MotionConfiguration] = None,
            *,
            bounding_regions: Optional[Sequence[GeoGeometry]] = None,
            extra: Optional[Mapping[str, ValueTypes]] = None,
            timeout: Optional[float] = None,
        ) -> str:
            raise NotImplementedError

        async def move_on_map(
            self,
            component_name: ResourceName,
            destination: Pose,
            slam_service_name: ResourceName,
            configuration: Optional[MotionConfiguration] = None,
            obstacles: Optional[Sequence[Geometry]] = None,
            *,
            extra: Optional[Mapping[str, ValueTypes]] = None,
            timeout: Optional[float] = None,
        ) -> str:
            raise NotImplementedError

        async def stop_plan(
            self, component_name: ResourceName, *, extra: Optional[Mapping[str, ValueTypes]] = None, timeout: Optional[float] = None
        ):
            raise NotImplementedError

        async def get_plan(
            self,
            component_name: ResourceName,
            last_plan_only: bool = False,
            execution_id: Optional[str] = None,
            *,
            extra: Optional[Mapping[str, ValueTypes]] = None,
            timeout: Optional[float] = None,
        ) -> GetPlanResponse:
            raise NotImplementedError

        async def list_plan_statuses(
            self, only_active_plans: bool = False, *, extra: Optional[Mapping[str, ValueTypes]] = None, timeout: Optional[float] = None
        ) -> ListPlanStatusesResponse:
            raise NotImplementedError

        async def get_pose(
            self,
            component_name: ResourceName,
            destination_frame: str,
            supplemental_transforms: Optional[Sequence[Transform]] = None,
            *,
            extra: Optional[Mapping[str, Any]] = None,
            timeout: Optional[float] = None,
        ) -> PoseInFrame:
            raise NotImplementedError

    return MockMotion(MOTION_SERVICE_NAME)


@pytest.fixture(scope="function")
def service(motion: Motion) -> MotionRPCService:
    return MotionRPCService(ResourceManager([motion]))


class TestMotionService:
    async def test_move(self, motion: Motion, service: MotionRPCService):
        with patch.object(motion, "move") as patched_method:
            patched_method.return_value = True
            async with ChannelFor([service]) as channel:
                client = MotionClient(MOTION_SERVICE_NAME, channel)
                resource_name = Arm.get_resource_name("arm")
                destination = PoseInFrame(reference_frame="refframe")
                world_state = WorldState(transforms=[Transform(reference_frame="ws_tfrm_rf")])
                constraints = Constraints(
                    linear_constraint=[LinearConstraint(), LinearConstraint(line_tolerance_mm=2)],
                    pseudolinear_constraint=[PseudolinearConstraint(line_tolerance_factor=1.0, orientation_tolerance_factor=0.5)],
                )
                extra = {"foo": "bar"}
                timeout = 2
                success = await client.move(
                    resource_name,
                    destination,
                    world_state,
                    constraints,
                    extra=extra,
                    timeout=timeout,
                )
                assert success is True
                patched_method.assert_called_once()
                assert patched_method.call_args.args[0] == resource_name
                assert patched_method.call_args.args[1] == destination
                assert patched_method.call_args.args[2] == world_state
                assert patched_method.call_args.args[3] == constraints
                assert patched_method.call_args.kwargs["extra"] == extra
                assert patched_method.call_args.kwargs["timeout"] == loose_approx(timeout)

    async def test_get_pose(self, motion: Motion, service: MotionRPCService):
        with patch.object(motion, "get_pose") as patched_method:
            response = PoseInFrame(reference_frame="arm", pose=Pose(x=1, y=2, z=3, o_x=2, o_y=3, o_z=4, theta=20))
            patched_method.return_value = response
            async with ChannelFor([service]) as channel:
                client = MotionClient(MOTION_SERVICE_NAME, channel)
                rn = Arm.get_resource_name("arm")
                destination_frame = "x"
                transforms = [Transform(reference_frame="y")]
                extra = {"foo": "bar"}
                timeout = 4
                pose = await client.get_pose(rn, destination_frame, transforms, extra=extra, timeout=timeout)
                assert pose == response
                patched_method.assert_called_once()
                assert patched_method.call_args.args[0] == rn
                assert patched_method.call_args.args[1] == destination_frame
                assert patched_method.call_args.args[2] == transforms
                assert patched_method.call_args.kwargs["extra"] == extra
                assert patched_method.call_args.kwargs["timeout"] == loose_approx(timeout)

    async def test_move_on_map(self, motion: Motion, service: MotionRPCService):
        with patch.object(motion, "move_on_map") as patched_method:
            resopnse = "Move On Map Response"
            patched_method.return_value = resopnse
            async with ChannelFor([service]) as channel:
                client = MotionClient(MOTION_SERVICE_NAME, channel)
                component_rn = Base.get_resource_name("move_on_globe_base")
                destination = Pose(x=1, y=2, z=3, theta=4)
                slam_rn = ResourceName(namespace="rdk", type="service", subtype="slam", name="move_on_map_slam")
                configuration = MotionConfiguration(position_polling_frequency_hz=4.44)
                obstacles = [Geometry(center=Pose(x=9, y=8, z=7, theta=6))]
                extra = {"foo": "bar"}
                timeout = 4
                execution_id = await client.move_on_map(
                    component_rn,
                    destination,
                    slam_service_name=slam_rn,
                    configuration=configuration,
                    obstacles=obstacles,
                    extra=extra,
                    timeout=timeout,
                )
                assert execution_id == resopnse
                patched_method.assert_called_once()
                assert patched_method.call_args.args[0] == component_rn
                assert patched_method.call_args.args[1] == destination
                assert patched_method.call_args.args[2] == slam_rn
                assert patched_method.call_args.args[3] == configuration
                assert patched_method.call_args.args[4] == obstacles
                assert patched_method.call_args.kwargs["extra"] == extra
                assert patched_method.call_args.kwargs["timeout"] == loose_approx(timeout)

    async def test_move_on_globe(self, motion: Motion, service: MotionRPCService):
        with patch.object(motion, "move_on_globe") as patched_method:
            response = "Move On Globe Response"
            patched_method.return_value = response
            async with ChannelFor([service]) as channel:
                client = MotionClient(MOTION_SERVICE_NAME, channel)
                component_rn = Base.get_resource_name("move_on_globe_base")
                destination = GeoPoint(latitude=123, longitude=456)
                movement_rn = ResourceName(namespace="rdk", type="component", subtype="movement_sensor", name="move_on_globe_ms")
                obstacles = [GeoGeometry(location=GeoPoint(latitude=44, longitude=786))]
                heading = 5.55
                configuration = MotionConfiguration(position_polling_frequency_hz=4.44)
                bounding_regions = [GeoGeometry(location=GeoPoint(latitude=182, longitude=41))]
                extra = {"foo": "bar"}
                timeout = 3
                execution_id = await client.move_on_globe(
                    component_rn,
                    destination,
                    movement_rn,
                    obstacles,
                    heading,
                    configuration,
                    bounding_regions=bounding_regions,
                    extra=extra,
                    timeout=timeout,
                )
                assert execution_id == response
                patched_method.assert_called_once()
                assert patched_method.call_args.args[0] == component_rn
                assert patched_method.call_args.args[1] == destination
                assert patched_method.call_args.args[2] == movement_rn
                assert patched_method.call_args.args[3] == obstacles
                assert patched_method.call_args.args[4] == heading
                assert patched_method.call_args.args[5] == configuration
                assert patched_method.call_args.kwargs["bounding_regions"] == bounding_regions
                assert patched_method.call_args.kwargs["extra"] == extra
                assert patched_method.call_args.kwargs["timeout"] == loose_approx(timeout)

    async def test_stop_plan(self, motion: Motion, service: MotionRPCService):
        with patch.object(motion, "stop_plan") as patched_method:
            async with ChannelFor([service]) as channel:
                client = MotionClient(MOTION_SERVICE_NAME, channel)
                component_rn = Base.get_resource_name("stop_plan_base")
                extra = {"foo": "bar"}
                timeout = 4
                await client.stop_plan(component_rn, extra=extra, timeout=timeout)
                patched_method.assert_called_once()
                assert patched_method.call_args.args[0] == component_rn
                assert patched_method.call_args.kwargs["extra"] == extra
                assert patched_method.call_args.kwargs["timeout"] == loose_approx(timeout)

    async def test_get_plan(self, motion: Motion, service: MotionRPCService):
        with patch.object(motion, "get_plan") as patched_method:
            response = GetPlanResponse(
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
            patched_method.return_value = response
            async with ChannelFor([service]) as channel:
                client = MotionClient(MOTION_SERVICE_NAME, channel)
                component_rn = Base.get_resource_name("get_plan_base")
                last_plan_only = True
                execution_id = "ex_id"
                extra = {"foo": "bar"}
                timeout = 4

                plan = await client.get_plan(component_rn, last_plan_only, execution_id, extra=extra, timeout=timeout)
                assert plan == response
                patched_method.assert_called_once()
                assert patched_method.call_args.args[0] == component_rn
                assert patched_method.call_args.args[1] == last_plan_only
                assert patched_method.call_args.args[2] == execution_id
                assert patched_method.call_args.kwargs["extra"] == extra
                assert patched_method.call_args.kwargs["timeout"] == loose_approx(timeout)

    async def test_list_plan_statuses(self, motion: Motion, service: MotionRPCService):
        with patch.object(motion, "list_plan_statuses") as patched_method:
            response = [PlanStatusWithID(plan_id="lpsr_pswid")]
            patched_method.return_value = response
            async with ChannelFor([service]) as channel:
                client = MotionClient(MOTION_SERVICE_NAME, channel)

                only_active_plans = True
                extra = {"foo": "bar"}
                timeout = 5

                plan_statuses = await client.list_plan_statuses(only_active_plans, extra=extra, timeout=timeout)

                assert plan_statuses == response
                patched_method.assert_called_once()
                assert patched_method.call_args.args[0] == only_active_plans
                assert patched_method.call_args.kwargs["extra"] == extra
                assert patched_method.call_args.kwargs["timeout"] == loose_approx(timeout)

    async def test_do(self, motion: Motion, service: MotionRPCService):
        with patch.object(motion, "do_command") as patched_method:
            response = {"do": "command"}
            patched_method.return_value = response
            async with ChannelFor([service]) as channel:
                client = MotionClient(MOTION_SERVICE_NAME, channel)
                command = {"command": "args"}
                timeout = 5
                dc_response = await client.do_command(command, timeout=timeout)
                assert dc_response == response
                patched_method.assert_called_once()
                assert patched_method.call_args.args[0] == command
                assert patched_method.call_args.kwargs["timeout"] == loose_approx(timeout)
