from typing import Any, Mapping, Optional, Sequence

from grpclib.client import Channel

from viam.proto.common import (
    DoCommandRequest,
    DoCommandResponse,
    GeoGeometry,
    Geometry,
    GeoPoint,
    Pose,
    PoseInFrame,
    ResourceName,
    Transform,
    WorldState,
)
from viam.proto.service.motion import (
    Constraints,
    GetPlanRequest,
    GetPlanResponse,
    GetPoseRequest,
    GetPoseResponse,
    ListPlanStatusesRequest,
    ListPlanStatusesResponse,
    MotionConfiguration,
    MotionServiceStub,
    MoveOnGlobeRequest,
    MoveOnGlobeResponse,
    MoveOnMapRequest,
    MoveOnMapResponse,
    MoveRequest,
    MoveResponse,
    PlanStatusWithID,
    StopPlanRequest,
    StopPlanResponse,
)
from viam.resource.rpc_client_base import ReconfigurableResourceRPCClientBase
from viam.utils import ValueTypes, dict_to_struct, struct_to_dict

from .motion import Motion


class MotionClient(Motion, ReconfigurableResourceRPCClientBase):
    """
    gRPC client for the Motion service.
    """

    client: MotionServiceStub

    def __init__(self, name: str, channel: Channel):
        self.channel = channel
        self.client = MotionServiceStub(channel)
        super().__init__(name)

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
        if extra is None:
            extra = {}
        request = MoveRequest(
            name=self.name,
            destination=destination,
            component_name=component_name,
            world_state=world_state,
            constraints=constraints,
            extra=dict_to_struct(extra),
        )
        response: MoveResponse = await self.client.Move(request, timeout=timeout)
        return response.success

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
        if extra is None:
            extra = {}
        request = MoveOnGlobeRequest(
            name=self.name,
            component_name=component_name,
            destination=destination,
            movement_sensor_name=movement_sensor_name,
            obstacles=obstacles,
            heading=heading,
            motion_configuration=configuration,
            bounding_regions=bounding_regions,
            extra=dict_to_struct(extra),
        )
        response: MoveOnGlobeResponse = await self.client.MoveOnGlobe(request, timeout=timeout)
        return response.execution_id

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
        if extra is None:
            extra = {}
        request = MoveOnMapRequest(
            name=self.name,
            destination=destination,
            component_name=component_name,
            slam_service_name=slam_service_name,
            motion_configuration=configuration,
            obstacles=obstacles,
            extra=dict_to_struct(extra),
        )
        response: MoveOnMapResponse = await self.client.MoveOnMap(request, timeout=timeout)
        return response.execution_id

    async def stop_plan(
        self,
        component_name: ResourceName,
        *,
        extra: Optional[Mapping[str, ValueTypes]] = None,
        timeout: Optional[float] = None,
    ):
        if extra is None:
            extra = {}

        request = StopPlanRequest(
            name=self.name,
            component_name=component_name,
            extra=dict_to_struct(extra),
        )
        _: StopPlanResponse = await self.client.StopPlan(request, timeout=timeout)
        return

    async def get_plan(
        self,
        component_name: ResourceName,
        last_plan_only: bool = False,
        execution_id: Optional[str] = None,
        *,
        extra: Optional[Mapping[str, ValueTypes]] = None,
        timeout: Optional[float] = None,
    ) -> GetPlanResponse:
        if extra is None:
            extra = {}

        request = GetPlanRequest(
            name=self.name,
            component_name=component_name,
            last_plan_only=last_plan_only,
            execution_id=execution_id,
            extra=dict_to_struct(extra),
        )
        response: GetPlanResponse = await self.client.GetPlan(request, timeout=timeout)
        return response

    async def list_plan_statuses(
        self,
        only_active_plans: bool = False,
        *,
        extra: Optional[Mapping[str, ValueTypes]] = None,
        timeout: Optional[float] = None,
    ) -> Sequence[PlanStatusWithID]:
        if extra is None:
            extra = {}

        request = ListPlanStatusesRequest(
            name=self.name,
            only_active_plans=only_active_plans,
            extra=dict_to_struct(extra),
        )
        response: ListPlanStatusesResponse = await self.client.ListPlanStatuses(request, timeout=timeout)
        return response.plan_statuses_with_ids

    async def get_pose(
        self,
        component_name: ResourceName,
        destination_frame: str,
        supplemental_transforms: Optional[Sequence[Transform]] = None,
        *,
        extra: Optional[Mapping[str, Any]] = None,
        timeout: Optional[float] = None,
    ) -> PoseInFrame:
        if extra is None:
            extra = {}
        request = GetPoseRequest(
            name=self.name,
            component_name=component_name,
            destination_frame=destination_frame,
            supplemental_transforms=supplemental_transforms,
            extra=dict_to_struct(extra),
        )
        response: GetPoseResponse = await self.client.GetPose(request, timeout=timeout)
        return response.pose

    async def do_command(self, command: Mapping[str, ValueTypes], *, timeout: Optional[float] = None, **__) -> Mapping[str, ValueTypes]:
        request = DoCommandRequest(name=self.name, command=dict_to_struct(command))
        response: DoCommandResponse = await self.client.DoCommand(request, timeout=timeout)
        return struct_to_dict(response.result)
