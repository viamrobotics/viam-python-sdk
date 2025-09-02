from grpclib.server import Stream

from viam.proto.common import DoCommandRequest, DoCommandResponse
from viam.proto.service.worldstatestore import (
    GetTransformRequest,
    GetTransformResponse,
    ListUUIDsRequest,
    ListUUIDsResponse,
    StreamTransformChangesRequest,
    StreamTransformChangesResponse,
    UnimplementedWorldStateStoreServiceBase,
)
from viam.resource.rpc_service_base import ResourceRPCServiceBase
from viam.utils import dict_to_struct, struct_to_dict

from .worldstatestore import WorldStateStore


class WorldStateStoreService(UnimplementedWorldStateStoreServiceBase, ResourceRPCServiceBase[WorldStateStore]):
    RESOURCE_TYPE = WorldStateStore

    async def ListUUIDs(self, stream: Stream[ListUUIDsRequest, ListUUIDsResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        service = self.get_resource(request.name)
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        uuids = await service.list_uuids(extra=struct_to_dict(request.extra), timeout=timeout)
        await stream.send_message(ListUUIDsResponse(uuids=uuids))

    async def GetTransform(self, stream: Stream[GetTransformRequest, GetTransformResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        service = self.get_resource(request.name)
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        transform = await service.get_transform(uuid=request.uuid, extra=struct_to_dict(request.extra), timeout=timeout)
        await stream.send_message(GetTransformResponse(transform=transform))

    async def StreamTransformChanges(
        self,
        stream: Stream[StreamTransformChangesRequest, StreamTransformChangesResponse],
    ) -> None:
        request = await stream.recv_message()
        assert request is not None
        service = self.get_resource(request.name)
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        async for change in service.stream_transform_changes(extra=struct_to_dict(request.extra), timeout=timeout):
            await stream.send_message(change)

    async def DoCommand(self, stream: Stream[DoCommandRequest, DoCommandResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        worldstatestore = self.get_resource(request.name)
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        result = await worldstatestore.do_command(struct_to_dict(request.command), timeout=timeout)
        await stream.send_message(DoCommandResponse(result=dict_to_struct(result)))
