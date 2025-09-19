from typing import Any, Mapping, Optional, Sequence, Union

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

    def _convert_obstacle_detector_to_request_format(self, od: MotionServiceStub.ObstacleDetector) -> MotionServiceStub.ObstacleDetector:
        new_od = MotionServiceStub.ObstacleDetector()
        if od.vision_service:
            new_od.vision_service = od.vision_service
        elif od.vision_service_deprecated:
            new_od.vision_service = od.vision_service_deprecated.name
            new_od.vision_service_deprecated = od.vision_service_deprecated

        if od.camera:
            new_od.camera = od.camera
        elif od.camera_deprecated:
            new_od.camera = od.camera_deprecated.name
            new_od.camera_deprecated = od.camera_deprecated
        return new_od

    def _convert_motion_configuration_to_request_format(self, config: MotionConfiguration) -> MotionConfiguration:
        new_config = MotionConfiguration()
        new_config.obstacle_detectors.extend([self._convert_obstacle_detector_to_request_format(od) for od in config.obstacle_detectors])

        if config.HasField("position_polling_frequency_hz"):
            new_config.position_polling_frequency_hz = config.position_polling_frequency_hz
        if config.HasField("linear_velocity_m_per_sec"):
            new_config.linear_velocity_m_per_sec = config.linear_velocity_m_per_sec
        if config.HasField("linear_acceleration_m_per_sec_sq"):
            new_config.linear_acceleration_m_per_sec_sq = config.linear_acceleration_m_per_sec_sq
        if config.HasField("angular_velocity_rad_per_sec"):
            new_config.angular_velocity_rad_per_sec = config.angular_velocity_rad_per_sec
        if config.HasField("angular_acceleration_rad_per_sec_sq"):
            new_config.angular_acceleration_rad_per_sec_sq = config.angular_acceleration_rad_per_sec_sq
        if config.HasField("reconfigure_enabled"):
            new_config.reconfigure_enabled = config.reconfigure_enabled
        return new_config

    async def move(
        self,
        component_name: Union[ResourceName, str],
        destination: PoseInFrame,
        world_state: Optional[WorldState] = None,
        constraints: Optional[Constraints] = None,
        *,
        extra: Optional[Mapping[str, Any]] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ) -> bool:
        md = kwargs.get("metadata", self.Metadata()).proto
        component_name_str = component_name.name if isinstance(component_name, ResourceName) else component_name
        component_name_deprecated = component_name if isinstance(component_name, ResourceName) else None
        request = MoveRequest(
            name=self.name,
            destination=destination,
            component_name=component_name_str,
            component_name_deprecated=component_name_deprecated,
            world_state=world_state,
            constraints=constraints,
            extra=dict_to_struct(extra),
        )
        response: MoveResponse = await self.client.Move(request, timeout=timeout, metadata=md)
        return response.success

    async def move_on_globe(
        self,
        component_name: Union[ResourceName, str],
        destination: GeoPoint,
        movement_sensor_name: Union[ResourceName, str],
        obstacles: Optional[Sequence[GeoGeometry]] = None,
        heading: Optional[float] = None,
        configuration: Optional[MotionConfiguration] = None,
        *,
        bounding_regions: Optional[Sequence[GeoGeometry]] = None,
        extra: Optional[Mapping[str, ValueTypes]] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ) -> str:
        md = kwargs.get("metadata", self.Metadata()).proto
        component_name_str = component_name.name if isinstance(component_name, ResourceName) else component_name
        component_name_deprecated = component_name if isinstance(component_name, ResourceName) else None
        movement_sensor_name_str = movement_sensor_name.name if isinstance(movement_sensor_name, ResourceName) else movement_sensor_name
        movement_sensor_name_deprecated = movement_sensor_name if isinstance(movement_sensor_name, ResourceName) else None

        request_configuration = None
        if configuration is not None:
            request_configuration = self._convert_motion_configuration_to_request_format(configuration)

        request = MoveOnGlobeRequest(
            name=self.name,
            component_name=component_name_str,
            component_name_deprecated=component_name_deprecated,
            destination=destination,
            movement_sensor_name=movement_sensor_name_str,
            movement_sensor_name_deprecated=movement_sensor_name_deprecated,
            obstacles=obstacles,
            heading=heading,
            motion_configuration=request_configuration,
            bounding_regions=bounding_regions,
            extra=dict_to_struct(extra),
        )
        response: MoveOnGlobeResponse = await self.client.MoveOnGlobe(request, timeout=timeout, metadata=md)
        return response.execution_id

    async def move_on_map(
        self,
        component_name: Union[ResourceName, str],
        destination: Pose,
        slam_service_name: Union[ResourceName, str],
        configuration: Optional[MotionConfiguration] = None,
        obstacles: Optional[Sequence[Geometry]] = None,
        *,
        extra: Optional[Mapping[str, ValueTypes]] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ) -> str:
        md = kwargs.get("metadata", self.Metadata()).proto
        component_name_str = component_name.name if isinstance(component_name, ResourceName) else component_name
        component_name_deprecated = component_name if isinstance(component_name, ResourceName) else None
        slam_service_name_str = slam_service_name.name if isinstance(slam_service_name, ResourceName) else slam_service_name
        slam_service_name_deprecated = slam_service_name if isinstance(slam_service_name, ResourceName) else None

        request_configuration = None
        if configuration is not None:
            request_configuration = self._convert_motion_configuration_to_request_format(configuration)

        request = MoveOnMapRequest(
            name=self.name,
            destination=destination,
            component_name=component_name_str,
            component_name_deprecated=component_name_deprecated,
            slam_service_name=slam_service_name_str,
            slam_service_name_deprecated=slam_service_name_deprecated,
            motion_configuration=request_configuration,
            obstacles=obstacles,
            extra=dict_to_struct(extra),
        )
        response: MoveOnMapResponse = await self.client.MoveOnMap(request, timeout=timeout, metadata=md)
        return response.execution_id

    async def stop_plan(
        self,
        component_name: Union[ResourceName, str],
        *,
        extra: Optional[Mapping[str, ValueTypes]] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ):
        md = kwargs.get("metadata", self.Metadata()).proto
        component_name_str = component_name.name if isinstance(component_name, ResourceName) else component_name
        component_name_deprecated = component_name if isinstance(component_name, ResourceName) else None

        request = StopPlanRequest(
            name=self.name,
            component_name=component_name_str,
            component_name_deprecated=component_name_deprecated,
            extra=dict_to_struct(extra),
        )
        _: StopPlanResponse = await self.client.StopPlan(request, timeout=timeout, metadata=md)
        return

    async def get_plan(
        self,
        component_name: Union[ResourceName, str],
        last_plan_only: bool = False,
        execution_id: Optional[str] = None,
        *,
        extra: Optional[Mapping[str, ValueTypes]] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ) -> GetPlanResponse:
        md = kwargs.get("metadata", self.Metadata()).proto
        component_name_str = component_name.name if isinstance(component_name, ResourceName) else component_name
        component_name_deprecated = component_name if isinstance(component_name, ResourceName) else None

        request = GetPlanRequest(
            name=self.name,
            component_name=component_name_str,
            component_name_deprecated=component_name_deprecated,
            last_plan_only=last_plan_only,
            execution_id=execution_id,
            extra=dict_to_struct(extra),
        )
        response: GetPlanResponse = await self.client.GetPlan(request, timeout=timeout, metadata=md)
        return response

    async def list_plan_statuses(
        self,
        only_active_plans: bool = False,
        *,
        extra: Optional[Mapping[str, ValueTypes]] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ) -> Sequence[PlanStatusWithID]:
        md = kwargs.get("metadata", self.Metadata()).proto

        request = ListPlanStatusesRequest(
            name=self.name,
            only_active_plans=only_active_plans,
            extra=dict_to_struct(extra),
        )
        response: ListPlanStatusesResponse = await self.client.ListPlanStatuses(request, timeout=timeout, metadata=md)
        return response.plan_statuses_with_ids

    async def get_pose(
        self,
        component_name: Union[ResourceName, str],
        destination_frame: str,
        supplemental_transforms: Optional[Sequence[Transform]] = None,
        *,
        extra: Optional[Mapping[str, Any]] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ) -> PoseInFrame:
        md = kwargs.get("metadata", self.Metadata()).proto
        component_name_str = component_name.name if isinstance(component_name, ResourceName) else component_name
        component_name_deprecated = component_name if isinstance(component_name, ResourceName) else None
        request = GetPoseRequest(
            name=self.name,
            component_name=component_name_str,
            component_name_deprecated=component_name_deprecated,
            destination_frame=destination_frame,
            supplemental_transforms=supplemental_transforms,
            extra=dict_to_struct(extra),
        )
        response: GetPoseResponse = await self.client.GetPose(request, timeout=timeout, metadata=md)
        return response.pose

    async def do_command(self, command: Mapping[str, ValueTypes], *, timeout: Optional[float] = None, **kwargs) -> Mapping[str, ValueTypes]:
        md = kwargs.get("metadata", self.Metadata()).proto
        request = DoCommandRequest(name=self.name, command=dict_to_struct(command))
        response: DoCommandResponse = await self.client.DoCommand(request, timeout=timeout, metadata=md)
        return struct_to_dict(response.result)
