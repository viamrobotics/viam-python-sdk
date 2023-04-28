from grpclib.server import Stream

from viam.errors import ResourceNotFoundError
from viam.gen.service.slam.v1.slam_grpc import SLAMServiceBase
from viam.proto.common import DoCommandRequest, DoCommandResponse
from viam.proto.service.slam import (
    GetInternalStateRequest,
    GetInternalStateResponse,
    GetPointCloudMapRequest,
    GetPointCloudMapResponse,
    GetPositionRequest,
    GetPositionResponse,
)
from viam.resource.rpc_service_base import ResourceRPCServiceBase
from viam.services.slam.slam import SLAM
from viam.utils import dict_to_struct, struct_to_dict


class SLAMServiceRPCService(SLAMServiceBase, ResourceRPCServiceBase[SLAM]):
    """
    gRPC Service for a SLAM service
    """

    RESOURCE_TYPE = SLAM

    async def GetInternalState(self, stream: Stream[GetInternalStateRequest, GetInternalStateResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        try:
            slam = self.get_resource(name)
        except ResourceNotFoundError as e:
            raise e.grpc_error
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        chunks = await slam.get_internal_state(timeout=timeout)
        for chunk in chunks:
            response = GetInternalStateResponse(internal_state_chunk=chunk)
            await stream.send_message(response)

    async def GetPointCloudMap(self, stream: Stream[GetPointCloudMapRequest, GetPointCloudMapResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        try:
            slam = self.get_resource(name)
        except ResourceNotFoundError as e:
            raise e.grpc_error
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        chunks = await slam.get_point_cloud_map(timeout=timeout)
        for chunk in chunks:
            response = GetPointCloudMapResponse(point_cloud_pcd_chunk=chunk)
            await stream.send_message(response)

    async def GetPosition(self, stream: Stream[GetPositionRequest, GetPositionResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        try:
            slam = self.get_resource(name)
        except ResourceNotFoundError as e:
            raise e.grpc_error
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        position = await slam.get_position(timeout=timeout)
        response = GetPositionResponse(pose=position)
        await stream.send_message(response)

    async def DoCommand(self, stream: Stream[DoCommandRequest, DoCommandResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        try:
            arm = self.get_resource(request.name)
        except ResourceNotFoundError as e:
            raise e.grpc_error
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        result = await arm.do_command(command=struct_to_dict(request.command), timeout=timeout, metadata=stream.metadata)
        response = DoCommandResponse(result=dict_to_struct(result))
        await stream.send_message(response)
