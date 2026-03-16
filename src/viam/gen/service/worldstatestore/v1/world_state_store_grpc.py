import abc
import typing
import grpclib.const
import grpclib.client
import grpclib.exceptions
if typing.TYPE_CHECKING:
    import grpclib.server
from .... import common
import google.api.annotations_pb2
import google.protobuf.field_mask_pb2
import google.protobuf.struct_pb2
from .... import service

class WorldStateStoreServiceBase(abc.ABC):

    @abc.abstractmethod
    async def ListUUIDs(self, stream: 'grpclib.server.Stream[service.worldstatestore.v1.world_state_store_pb2.ListUUIDsRequest, service.worldstatestore.v1.world_state_store_pb2.ListUUIDsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetTransform(self, stream: 'grpclib.server.Stream[service.worldstatestore.v1.world_state_store_pb2.GetTransformRequest, service.worldstatestore.v1.world_state_store_pb2.GetTransformResponse]') -> None:
        pass

    @abc.abstractmethod
    async def StreamTransformChanges(self, stream: 'grpclib.server.Stream[service.worldstatestore.v1.world_state_store_pb2.StreamTransformChangesRequest, service.worldstatestore.v1.world_state_store_pb2.StreamTransformChangesResponse]') -> None:
        pass

    @abc.abstractmethod
    async def DoCommand(self, stream: 'grpclib.server.Stream[common.v1.common_pb2.DoCommandRequest, common.v1.common_pb2.DoCommandResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/viam.service.worldstatestore.v1.WorldStateStoreService/ListUUIDs': grpclib.const.Handler(self.ListUUIDs, grpclib.const.Cardinality.UNARY_UNARY, service.worldstatestore.v1.world_state_store_pb2.ListUUIDsRequest, service.worldstatestore.v1.world_state_store_pb2.ListUUIDsResponse), '/viam.service.worldstatestore.v1.WorldStateStoreService/GetTransform': grpclib.const.Handler(self.GetTransform, grpclib.const.Cardinality.UNARY_UNARY, service.worldstatestore.v1.world_state_store_pb2.GetTransformRequest, service.worldstatestore.v1.world_state_store_pb2.GetTransformResponse), '/viam.service.worldstatestore.v1.WorldStateStoreService/StreamTransformChanges': grpclib.const.Handler(self.StreamTransformChanges, grpclib.const.Cardinality.UNARY_STREAM, service.worldstatestore.v1.world_state_store_pb2.StreamTransformChangesRequest, service.worldstatestore.v1.world_state_store_pb2.StreamTransformChangesResponse), '/viam.service.worldstatestore.v1.WorldStateStoreService/DoCommand': grpclib.const.Handler(self.DoCommand, grpclib.const.Cardinality.UNARY_UNARY, common.v1.common_pb2.DoCommandRequest, common.v1.common_pb2.DoCommandResponse)}

class UnimplementedWorldStateStoreServiceBase(WorldStateStoreServiceBase):

    async def ListUUIDs(self, stream: 'grpclib.server.Stream[service.worldstatestore.v1.world_state_store_pb2.ListUUIDsRequest, service.worldstatestore.v1.world_state_store_pb2.ListUUIDsResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def GetTransform(self, stream: 'grpclib.server.Stream[service.worldstatestore.v1.world_state_store_pb2.GetTransformRequest, service.worldstatestore.v1.world_state_store_pb2.GetTransformResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def StreamTransformChanges(self, stream: 'grpclib.server.Stream[service.worldstatestore.v1.world_state_store_pb2.StreamTransformChangesRequest, service.worldstatestore.v1.world_state_store_pb2.StreamTransformChangesResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def DoCommand(self, stream: 'grpclib.server.Stream[common.v1.common_pb2.DoCommandRequest, common.v1.common_pb2.DoCommandResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

class WorldStateStoreServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.ListUUIDs = grpclib.client.UnaryUnaryMethod(channel, '/viam.service.worldstatestore.v1.WorldStateStoreService/ListUUIDs', service.worldstatestore.v1.world_state_store_pb2.ListUUIDsRequest, service.worldstatestore.v1.world_state_store_pb2.ListUUIDsResponse)
        self.GetTransform = grpclib.client.UnaryUnaryMethod(channel, '/viam.service.worldstatestore.v1.WorldStateStoreService/GetTransform', service.worldstatestore.v1.world_state_store_pb2.GetTransformRequest, service.worldstatestore.v1.world_state_store_pb2.GetTransformResponse)
        self.StreamTransformChanges = grpclib.client.UnaryStreamMethod(channel, '/viam.service.worldstatestore.v1.WorldStateStoreService/StreamTransformChanges', service.worldstatestore.v1.world_state_store_pb2.StreamTransformChangesRequest, service.worldstatestore.v1.world_state_store_pb2.StreamTransformChangesResponse)
        self.DoCommand = grpclib.client.UnaryUnaryMethod(channel, '/viam.service.worldstatestore.v1.WorldStateStoreService/DoCommand', common.v1.common_pb2.DoCommandRequest, common.v1.common_pb2.DoCommandResponse)