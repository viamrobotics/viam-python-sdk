from grpclib.server import Stream

from viam.errors import MethodNotImplementedError
from viam.proto.common import DoCommandRequest, DoCommandResponse
from viam.proto.service.navigation import (
    NavigationServiceBase,
)
from viam.resource.rpc_service_base import ResourceRPCServiceBase
from viam.utils import dict_to_struct, struct_to_dict

from .navigation import Navigation


class NavigationRPCService(NavigationServiceBase, ResourceRPCServiceBase):
    """
    gRPC Service for a Navigation service
    """

    RESOURCE_TYPE = Navigation

    async def GetInternalState(self, stream: Stream[GetInternalStateRequest, GetInternalStateResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        navigation = self.get_resource(name)
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        chunks = await navigation.get_internal_state(timeout=timeout)
        for chunk in chunks:
            response = GetInternalStateResponse(internal_state_chunk=chunk)
            await stream.send_message(response)

    async def GetPointCloudMap(self, stream: Stream[GetPointCloudMapRequest, GetPointCloudMapResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        navigation = self.get_resource(name)
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        chunks = await navigation.get_point_cloud_map(timeout=timeout)
        for chunk in chunks:
            response = GetPointCloudMapResponse(point_cloud_pcd_chunk=chunk)
            await stream.send_message(response)

    async def GetPosition(self, stream: Stream[GetPositionRequest, GetPositionResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        navigation = self.get_resource(name)
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        position = await navigation.get_position(timeout=timeout)
        response = GetPositionResponse(pose=position)
        await stream.send_message(response)

    async def GetLatestMapInfo(self, stream: Stream[GetLatestMapInfoRequest, GetLatestMapInfoResponse]) -> None:
        raise MethodNotImplementedError("GetLatestMapInfo").grpc_error

    async def DoCommand(self, stream: Stream[DoCommandRequest, DoCommandResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        navigation = self.get_resource(request.name)
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        result = await navigation.do_command(command=struct_to_dict(request.command), timeout=timeout, metadata=stream.metadata)
        response = DoCommandResponse(result=dict_to_struct(result))
        await stream.send_message(response)
