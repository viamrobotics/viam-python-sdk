from grpclib.server import Stream

from viam.proto.common import DoCommandRequest, DoCommandResponse
from viam.proto.service.discovery import (
    DiscoverResourcesRequest,
    DiscoverResourcesResponse,
    UnimplementedDiscoveryServiceBase,
)
from viam.resource.rpc_service_base import ResourceRPCServiceBase
from viam.utils import dict_to_struct, struct_to_dict

from .discovery import Discovery


class DiscoveryRPCService(UnimplementedDiscoveryServiceBase, ResourceRPCServiceBase):
    """
    gRPC service for a Discovery service
    """

    RESOURCE_TYPE = Discovery

    async def DiscoverResources(self, stream: Stream[DiscoverResourcesRequest, DiscoverResourcesResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        discovery = self.get_resource(request.name)
        extra = struct_to_dict(request.extra)
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        result = await discovery.discover_resources(
            extra=extra,
            timeout=timeout,
        )
        response = DiscoverResourcesResponse(
            discoveries=result,
        )
        await stream.send_message(response)

    async def DoCommand(self, stream: Stream[DoCommandRequest, DoCommandResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        discovery = self.get_resource(request.name)
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        result = await discovery.do_command(struct_to_dict(request.command), timeout=timeout)
        await stream.send_message(DoCommandResponse(result=dict_to_struct(result)))
