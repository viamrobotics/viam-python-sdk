from datetime import timedelta
from typing import AsyncIterator, List

from grpclib import GRPCError, Status
from grpclib.server import Stream

from viam.proto.common import (
    DoCommandRequest,
    DoCommandResponse,
    GetGeometriesRequest,
    GetGeometriesResponse,
    GetKinematicsRequest,
    GetKinematicsResponse,
    GetStatusRequest,
    GetStatusResponse,
)
from viam.proto.component.arm import (
    GetEndPositionRequest,
    GetEndPositionResponse,
    GetJointPositionsRequest,
    GetJointPositionsResponse,
    IsMovingRequest,
    IsMovingResponse,
    MoveThroughJointPositionsRequest,
    MoveThroughJointPositionsResponse,
    MoveThroughJointPositionsStreamedRequest,
    MoveThroughJointPositionsStreamedResponse,
    MoveToJointPositionsRequest,
    MoveToJointPositionsResponse,
    MoveToPositionRequest,
    MoveToPositionResponse,
    StopRequest,
    StopResponse,
    UnimplementedArmServiceBase,
)
from viam.resource.rpc_service_base import ResourceRPCServiceBase
from viam.utils import dict_to_struct, struct_to_dict

from .arm import Arm


class _TrajectoryStreamValidator:
    """
    Enforces the trajectory contract across a single streamed request, one point at a time.

    The checks match what the other SDKs apply on the server side (see the C++ SDK's
    TrajectoryStreamValidator): the trajectory begins at time zero and from rest, point times
    strictly increase, and any constraints are dimensionally consistent with the positions.
    State carries across batches, so a single validator must see every point of the stream in
    order.
    """

    def __init__(self) -> None:
        self._seen_first = False
        self._last_time = timedelta()

    def check(self, point: Arm.TrajectoryPoint) -> None:
        if not self._seen_first:
            if point.time != timedelta():
                raise GRPCError(Status.INVALID_ARGUMENT, "first trajectory point must have time zero")
        elif point.time <= self._last_time:
            raise GRPCError(Status.INVALID_ARGUMENT, "trajectory point times must strictly increase")

        if not point.positions:
            raise GRPCError(Status.INVALID_ARGUMENT, "trajectory point must carry at least one position")

        constraints = point.constraints
        if constraints is not None:
            if len(constraints.velocities) != len(point.positions):
                raise GRPCError(
                    Status.INVALID_ARGUMENT,
                    "trajectory point must carry one velocity per position when constraints are present",
                )
            # The arm has to start from a standstill, so the first point may not ask for motion.
            if not self._seen_first and any(velocity != 0.0 for velocity in constraints.velocities):
                raise GRPCError(Status.INVALID_ARGUMENT, "first trajectory point must start from rest (all velocities zero)")
            if constraints.accelerations is not None and len(constraints.accelerations) != len(constraints.velocities):
                raise GRPCError(
                    Status.INVALID_ARGUMENT,
                    "trajectory point must carry one acceleration per velocity when accelerations are present",
                )

        self._seen_first = True
        self._last_time = point.time


class ArmRPCService(UnimplementedArmServiceBase, ResourceRPCServiceBase[Arm]):
    """
    gRPC Service for an Arm
    """

    RESOURCE_TYPE = Arm

    async def GetEndPosition(self, stream: Stream[GetEndPositionRequest, GetEndPositionResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        arm = self.get_resource(name)
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        position = await arm.get_end_position(extra=struct_to_dict(request.extra), timeout=timeout, metadata=stream.metadata)
        response = GetEndPositionResponse(pose=position)
        await stream.send_message(response)

    async def MoveToPosition(self, stream: Stream[MoveToPositionRequest, MoveToPositionResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        arm = self.get_resource(name)
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        await arm.move_to_position(request.to, extra=struct_to_dict(request.extra), timeout=timeout, metadata=stream.metadata)
        response = MoveToPositionResponse()
        await stream.send_message(response)

    async def GetJointPositions(self, stream: Stream[GetJointPositionsRequest, GetJointPositionsResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        arm = self.get_resource(name)
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        positions = await arm.get_joint_positions(extra=struct_to_dict(request.extra), timeout=timeout, metadata=stream.metadata)
        response = GetJointPositionsResponse(positions=positions)
        await stream.send_message(response)

    async def MoveToJointPositions(self, stream: Stream[MoveToJointPositionsRequest, MoveToJointPositionsResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        arm = self.get_resource(name)
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        await arm.move_to_joint_positions(request.positions, extra=struct_to_dict(request.extra), timeout=timeout, metadata=stream.metadata)
        response = MoveToJointPositionsResponse()
        await stream.send_message(response)

    async def MoveThroughJointPositions(
        self,
        stream: Stream[MoveThroughJointPositionsRequest, MoveThroughJointPositionsResponse],
    ) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        arm = self.get_resource(name)
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        await arm.move_through_joint_positions(
            list(request.positions),
            extra=struct_to_dict(request.extra),
            timeout=timeout,
            metadata=stream.metadata,
        )
        response = MoveThroughJointPositionsResponse()
        await stream.send_message(response)

    async def MoveThroughJointPositionsStreamed(
        self,
        stream: Stream[MoveThroughJointPositionsStreamedRequest, MoveThroughJointPositionsStreamedResponse],
    ) -> None:
        # The stream opens with exactly one Init, which names the arm and carries the sticky extra
        # arguments. The name sits at the top level of the request rather than inside Init because
        # that is where the RDK server reads it.
        first_request = await stream.recv_message()
        if first_request is None:
            raise GRPCError(Status.INVALID_ARGUMENT, "stream closed before init message")
        if not first_request.HasField("init"):
            raise GRPCError(Status.INVALID_ARGUMENT, "first message must be init")

        name = first_request.name
        arm = self.get_resource(name)
        extra = struct_to_dict(first_request.init.extra)
        timeout = stream.deadline.time_remaining() if stream.deadline else None

        # Turn the rest of the request stream into the async iterator of point-lists the driver
        # consumes, validating each point as it arrives. Validation lives here on the server so
        # that every arm implementation gets the same contract enforcement without having to
        # repeat it. An empty batch is a wire no-op and is skipped; a second Init, or any message
        # that is not a batch, is a protocol violation that ends the stream with an error.
        validator = _TrajectoryStreamValidator()

        async def batches() -> AsyncIterator[List[Arm.TrajectoryPoint]]:
            while True:
                request = await stream.recv_message()
                if request is None:
                    return
                message = request.WhichOneof("message")
                if message == "init":
                    raise GRPCError(Status.INVALID_ARGUMENT, "init may only appear as the first message")
                if message != "batch":
                    raise GRPCError(Status.INVALID_ARGUMENT, "expected a trajectory batch")
                points = [Arm.TrajectoryPoint.from_proto(point_proto) for point_proto in request.batch.points]
                for point in points:
                    validator.check(point)
                if points:
                    yield points

        async for update in arm.move_through_joint_positions_streamed(  # pyright: ignore [reportGeneralTypeIssues]
            batches(),
            extra=extra,
            timeout=timeout,
            metadata=stream.metadata,
        ):
            await stream.send_message(update.to_proto())

    async def Stop(self, stream: Stream[StopRequest, StopResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        arm = self.get_resource(name)
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        await arm.stop(extra=struct_to_dict(request.extra), timeout=timeout, metadata=stream.metadata)
        response = StopResponse()
        await stream.send_message(response)

    async def IsMoving(self, stream: Stream[IsMovingRequest, IsMovingResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        arm = self.get_resource(name)
        is_moving = await arm.is_moving()
        response = IsMovingResponse(is_moving=is_moving)
        await stream.send_message(response)

    async def DoCommand(self, stream: Stream[DoCommandRequest, DoCommandResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        arm = self.get_resource(request.name)
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        result = await arm.do_command(command=struct_to_dict(request.command), timeout=timeout, metadata=stream.metadata)
        response = DoCommandResponse(result=dict_to_struct(result))
        await stream.send_message(response)

    async def GetStatus(self, stream: Stream[GetStatusRequest, GetStatusResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        arm = self.get_resource(request.name)
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        result = await arm.get_status(timeout=timeout, metadata=stream.metadata)
        response = GetStatusResponse(result=dict_to_struct(result))
        await stream.send_message(response)

    async def GetKinematics(self, stream: Stream[GetKinematicsRequest, GetKinematicsResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        arm = self.get_resource(request.name)
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        kinematics = await arm.get_kinematics(extra=struct_to_dict(request.extra), timeout=timeout, metadata=stream.metadata)
        if len(kinematics) == 2:
            format, kinematics_data = kinematics
            meshes = {}
        else:
            format, kinematics_data, meshes = kinematics
        response = GetKinematicsResponse(format=format, kinematics_data=kinematics_data, meshes_by_urdf_filepath=meshes)
        await stream.send_message(response)

    async def GetGeometries(self, stream: Stream[GetGeometriesRequest, GetGeometriesResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        arm = self.get_resource(request.name)
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        geometries = await arm.get_geometries(extra=struct_to_dict(request.extra), timeout=timeout)
        response = GetGeometriesResponse(geometries=geometries)
        await stream.send_message(response)
