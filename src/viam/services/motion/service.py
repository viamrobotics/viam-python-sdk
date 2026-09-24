from typing import AsyncIterator, List

from grpclib import GRPCError, Status
from grpclib.server import Stream

from viam.proto.common import DoCommandRequest, DoCommandResponse, GetStatusRequest, GetStatusResponse
from viam.proto.component.arm import JointPositions
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
    TempStreamArmJointPositionsRequest,
    TempStreamArmJointPositionsResponse,
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

    async def TempStreamArmJointPositions(
        self,
        stream: Stream[TempStreamArmJointPositionsRequest, TempStreamArmJointPositionsResponse],
    ) -> None:
        # The stream opens with exactly one Init, which names the motion service and the arm to
        # stream to, and carries the sticky extra arguments and session options.
        first_request = await stream.recv_message()
        if first_request is None:
            raise GRPCError(Status.INVALID_ARGUMENT, "stream closed before init message")
        if not first_request.HasField("init"):
            raise GRPCError(Status.INVALID_ARGUMENT, "first message must be init")

        service = self.get_resource(first_request.name)
        component_name = first_request.init.component_name
        options = Motion.StreamOptions.from_proto(first_request.init.options) if first_request.init.HasField("options") else None
        extra = struct_to_dict(first_request.init.extra)
        timeout = stream.deadline.time_remaining() if stream.deadline else None

        # Turn the rest of the request stream into the async iterator of target batches the
        # implementation consumes. A second Init, or any message that is not a batch of targets, is
        # a protocol violation that ends the stream with an error.
        async def target_batches() -> AsyncIterator[List[JointPositions]]:
            while True:
                request = await stream.recv_message()
                if request is None:
                    return
                message = request.WhichOneof("message")
                if message == "init":
                    raise GRPCError(Status.INVALID_ARGUMENT, "init may only appear as the first message")
                if message != "targets":
                    raise GRPCError(Status.INVALID_ARGUMENT, "expected a batch of targets")
                positions = list(request.targets.positions)
                if positions:
                    yield positions

        async for _ in service.temp_stream_arm_joint_positions(  # pyright: ignore [reportGeneralTypeIssues]
            component_name,
            target_batches(),
            options,
            extra=extra,
            timeout=timeout,
            metadata=stream.metadata,
        ):
            await stream.send_message(TempStreamArmJointPositionsResponse())

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

    async def GetStatus(self, stream: Stream[GetStatusRequest, GetStatusResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        service = self.get_resource(request.name)
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        result = await service.get_status(timeout=timeout, metadata=stream.metadata)
        response = GetStatusResponse(result=dict_to_struct(result))
        await stream.send_message(response)
