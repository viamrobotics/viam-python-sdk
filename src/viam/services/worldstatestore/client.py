from typing import Any, AsyncGenerator, List, Mapping, Optional

from grpclib.client import Channel

from viam.proto.common import DoCommandRequest, DoCommandResponse, Transform
from viam.proto.service.worldstatestore import (
    GetTransformRequest,
    GetTransformResponse,
    ListUUIDsRequest,
    ListUUIDsResponse,
    StreamTransformChangesRequest,
    StreamTransformChangesResponse,
    WorldStateStoreServiceStub,
)
from viam.resource.rpc_client_base import ReconfigurableResourceRPCClientBase
from viam.utils import ValueTypes, dict_to_struct, struct_to_dict

from .worldstatestore import WorldStateStore


class WorldStateStoreClient(WorldStateStore, ReconfigurableResourceRPCClientBase):
    """
    gRPC client for the WorldStateStore service.
    """

    client: WorldStateStoreServiceStub

    def __init__(self, name: str, channel: Channel):
        self.channel = channel
        self.client = WorldStateStoreServiceStub(channel)
        super().__init__(name)

    async def list_uuids(
        self,
        *,
        extra: Optional[Mapping[str, Any]] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ) -> List[bytes]:
        md = kwargs.get("metadata", self.Metadata()).proto
        request = ListUUIDsRequest(
            name=self.name,
            extra=dict_to_struct(extra),
        )
        response: ListUUIDsResponse = await self.client.ListUUIDs(request, timeout=timeout, metadata=md)
        return list(response.uuids)

    async def get_transform(
        self,
        uuid: bytes,
        *,
        extra: Optional[Mapping[str, Any]] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ) -> "Transform":
        md = kwargs.get("metadata", self.Metadata()).proto
        request = GetTransformRequest(
            name=self.name,
            uuid=uuid,
            extra=dict_to_struct(extra),
        )
        response: GetTransformResponse = await self.client.GetTransform(request, timeout=timeout, metadata=md)
        return response.transform

    async def stream_transform_changes(
        self,
        *,
        extra: Optional[Mapping[str, Any]] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ) -> AsyncGenerator[StreamTransformChangesResponse, None]:
        md = kwargs.get("metadata", self.Metadata()).proto
        request = StreamTransformChangesRequest(
            name=self.name,
            extra=dict_to_struct(extra),
        )
        responses = await self.client.StreamTransformChanges(request, timeout=timeout, metadata=md)
        for response in responses:
            yield response

    async def do_command(
        self,
        command: Mapping[str, ValueTypes],
        *,
        timeout: Optional[float] = None,
        **kwargs,
    ) -> Mapping[str, ValueTypes]:
        md = kwargs.get("metadata", self.Metadata()).proto
        request = DoCommandRequest(
            name=self.name,
            command=dict_to_struct(command),
        )
        response: DoCommandResponse = await self.client.DoCommand(request, timeout=timeout, metadata=md)
        return struct_to_dict(response.result)
