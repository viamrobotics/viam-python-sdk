from grpclib.server import Stream

from viam.proto.common import DoCommandRequest, DoCommandResponse, GetGeometriesRequest, GetGeometriesResponse
from viam.proto.component.posetracker import GetPosesRequest, GetPosesResponse, PoseTrackerServiceBase
from viam.resource.rpc_service_base import ResourceRPCServiceBase
from viam.utils import dict_to_struct, struct_to_dict

from .pose_tracker import PoseTracker


class PoseTrackerRPCService(PoseTrackerServiceBase, ResourceRPCServiceBase[PoseTracker]):
    """
    gRPC service for a pose tracker
    """

    RESOURCE_TYPE = PoseTracker

    async def GetPoses(self, stream: Stream[GetPosesRequest, GetPosesResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        pose_tracker = self.get_resource(name)
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        poses = await pose_tracker.get_poses(
            list(request.body_names), extra=struct_to_dict(request.extra), timeout=timeout, metadata=stream.metadata
        )
        await stream.send_message(GetPosesResponse(body_poses=poses))

    async def DoCommand(self, stream: Stream[DoCommandRequest, DoCommandResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        pose_tracker = self.get_resource(request.name)
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        result = await pose_tracker.do_command(command=struct_to_dict(request.command), timeout=timeout, metadata=stream.metadata)
        response = DoCommandResponse(result=dict_to_struct(result))
        await stream.send_message(response)

    async def GetGeometries(self, stream: Stream[GetGeometriesRequest, GetGeometriesResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        pose_tracker = self.get_resource(request.name)
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        geometries = await pose_tracker.get_geometries(extra=struct_to_dict(request.extra), timeout=timeout)
        response = GetGeometriesResponse(geometries=geometries)
        await stream.send_message(response)
