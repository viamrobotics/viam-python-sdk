from typing import AsyncIterator, List

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
        # The first message on the request stream is the Init.
        first_request = await stream.recv_message()
        assert first_request is not None
        assert first_request.HasField("init"), "First message must contain init"

        name = first_request.name
        arm = self.get_resource(name)
        extra = struct_to_dict(first_request.init.extra)
        timeout = stream.deadline.time_remaining() if stream.deadline else None

        # Surface subsequent TrajectoryBatch messages as an async iterator of lists of
        # TrajectoryPoint values -- one yielded list per wire TrajectoryBatch -- which
        # is what driver code consumes. Empty batches and non-Batch messages are
        # filtered out by the dispatcher and never surface to the driver.
        async def batch_iterator() -> AsyncIterator[List[Arm.TrajectoryPoint]]:
            while True:
                request = await stream.recv_message()
                if request is None:
                    break
                if request.HasField("batch") and request.batch.points:
                    yield [Arm.TrajectoryPoint.from_proto(point_proto) for point_proto in request.batch.points]

        async for response in arm.move_through_joint_positions_streamed(  # pyright: ignore [reportGeneralTypeIssues]
            batch_iterator(),
            extra=extra,
            timeout=timeout,
            metadata=stream.metadata,
        ):
            await stream.send_message(response.to_proto())

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
