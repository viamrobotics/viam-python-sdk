from grpclib.server import Stream

from viam.proto.common import DoCommandRequest, DoCommandResponse
from viam.proto.service.motion import (
    GetPlanRequest,
    GetPlanResponse,
    GetPoseRequest,
    GetPoseResponse,
    ListPlanStatusesRequest,
    ListPlanStatusesResponse,
    MoveOnGlobeRequest,
    MoveOnGlobeResponse,
    MoveOnMapRequest,
    MoveOnMapResponse,
    MoveRequest,
    MoveResponse,
    StopPlanRequest,
    StopPlanResponse,
    UnimplementedMotionServiceBase,
)
from viam.resource.rpc_service_base import ResourceRPCServiceBase
from viam.utils import dict_to_struct, struct_to_dict

from .motion import Motion


class MotionRPCService(UnimplementedMotionServiceBase, ResourceRPCServiceBase[Motion]):
    RESOURCE_TYPE = Motion

    async def Move(self, stream: Stream[MoveRequest, MoveResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        service = self.get_resource(request.name)
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        result = await service.move(
            request.component_name,
            request.destination,
            request.world_state,
            request.constraints,
            extra=struct_to_dict(request.extra),
            timeout=timeout,
        )
        response = MoveResponse(success=result)
        await stream.send_message(response)

    async def MoveOnMap(self, stream: Stream[MoveOnMapRequest, MoveOnMapResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        service = self.get_resource(request.name)
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        result = await service.move_on_map(
            request.component_name,
            request.destination,
            request.slam_service_name,
            request.motion_configuration,
            request.obstacles,
            extra=struct_to_dict(request.extra),
            timeout=timeout,
        )
        response = MoveOnMapResponse(execution_id=result)
        await stream.send_message(response)

    async def MoveOnGlobe(self, stream: Stream[MoveOnGlobeRequest, MoveOnGlobeResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        service = self.get_resource(request.name)
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        result = await service.move_on_globe(
            request.component_name,
            request.destination,
            request.movement_sensor_name,
            request.obstacles,
            request.heading,
            request.motion_configuration,
            bounding_regions=request.bounding_regions,
            extra=struct_to_dict(request.extra),
            timeout=timeout,
        )
        response = MoveOnGlobeResponse(execution_id=result)
        await stream.send_message(response)

    async def GetPose(self, stream: Stream[GetPoseRequest, GetPoseResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        service = self.get_resource(request.name)
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        result = await service.get_pose(
            request.component_name,
            request.destination_frame,
            request.supplemental_transforms,
            extra=struct_to_dict(request.extra),
            timeout=timeout,
        )
        response = GetPoseResponse(pose=result)
        await stream.send_message(response)

    async def StopPlan(self, stream: Stream[StopPlanRequest, StopPlanResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        service = self.get_resource(request.name)
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        await service.stop_plan(request.component_name, extra=struct_to_dict(request.extra), timeout=timeout)
        response = StopPlanResponse()
        await stream.send_message(response)

    async def ListPlanStatuses(self, stream: Stream[ListPlanStatusesRequest, ListPlanStatusesResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        service = self.get_resource(request.name)
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        result = await service.list_plan_statuses(request.only_active_plans, extra=struct_to_dict(request.extra), timeout=timeout)
        response = ListPlanStatusesResponse(plan_statuses_with_ids=result)
        await stream.send_message(response)

    async def GetPlan(self, stream: Stream[GetPlanRequest, GetPlanResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        service = self.get_resource(request.name)
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        result = await service.get_plan(
            request.component_name, request.last_plan_only, request.execution_id, extra=struct_to_dict(request.extra), timeout=timeout
        )
        await stream.send_message(result)

    async def DoCommand(self, stream: Stream[DoCommandRequest, DoCommandResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        service = self.get_resource(request.name)
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        result = await service.do_command(struct_to_dict(request.command), timeout=timeout, metadata=stream.metadata)
        response = DoCommandResponse(result=dict_to_struct(result))
        await stream.send_message(response)
