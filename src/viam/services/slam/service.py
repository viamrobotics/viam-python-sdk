from grpclib.server import Stream

from viam.proto.common import DoCommandRequest, DoCommandResponse
from viam.proto.service.slam import (
    GetInternalStateRequest,
    GetInternalStateResponse,
    GetLatestMapInfoRequest,
    GetLatestMapInfoResponse,
    GetPointCloudMapRequest,
    GetPointCloudMapResponse,
    GetPositionRequest,
    GetPositionResponse,
    SLAMServiceBase,
)
from viam.resource.rpc_service_base import ResourceRPCServiceBase
from viam.utils import datetime_to_timestamp, dict_to_struct, struct_to_dict

from .slam import SLAM


class SLAMRPCService(SLAMServiceBase, ResourceRPCServiceBase):
    """
    gRPC Service for a SLAM service
    """

    RESOURCE_TYPE = SLAM

    async def GetInternalState(self, stream: Stream[GetInternalStateRequest, GetInternalStateResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        slam = self.get_resource(name)
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        chunks = await slam.get_internal_state(timeout=timeout)
        for chunk in chunks:
            response = GetInternalStateResponse(internal_state_chunk=chunk)
            await stream.send_message(response)

    async def GetPointCloudMap(self, stream: Stream[GetPointCloudMapRequest, GetPointCloudMapResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        slam = self.get_resource(name)
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        chunks = await slam.get_point_cloud_map(timeout=timeout)
        for chunk in chunks:
            response = GetPointCloudMapResponse(point_cloud_pcd_chunk=chunk)
            await stream.send_message(response)

    async def GetPosition(self, stream: Stream[GetPositionRequest, GetPositionResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        slam = self.get_resource(name)
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        position = await slam.get_position(timeout=timeout)
        response = GetPositionResponse(pose=position)
        await stream.send_message(response)

    async def GetLatestMapInfo(self, stream: Stream[GetLatestMapInfoRequest, GetLatestMapInfoResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        slam = self.get_resource(request.name)
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        time = await slam.get_latest_map_info(timeout=timeout)
        response = GetLatestMapInfoResponse(last_map_update=datetime_to_timestamp(time))
        await stream.send_message(response)

    async def DoCommand(self, stream: Stream[DoCommandRequest, DoCommandResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        slam = self.get_resource(request.name)
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        result = await slam.do_command(command=struct_to_dict(request.command), timeout=timeout, metadata=stream.metadata)
        response = DoCommandResponse(result=dict_to_struct(result))
        await stream.send_message(response)
