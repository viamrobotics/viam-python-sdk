import abc
import typing
import grpclib.const
import grpclib.client
import grpclib.exceptions
if typing.TYPE_CHECKING:
    import grpclib.server
from .... import common
import google.api.annotations_pb2
import google.protobuf.struct_pb2
from .... import service

class DataManagerServiceBase(abc.ABC):

    @abc.abstractmethod
    async def Sync(self, stream: 'grpclib.server.Stream[service.datamanager.v1.data_manager_pb2.SyncRequest, service.datamanager.v1.data_manager_pb2.SyncResponse]') -> None:
        pass

    @abc.abstractmethod
    async def DoCommand(self, stream: 'grpclib.server.Stream[common.v1.common_pb2.DoCommandRequest, common.v1.common_pb2.DoCommandResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/viam.service.datamanager.v1.DataManagerService/Sync': grpclib.const.Handler(self.Sync, grpclib.const.Cardinality.UNARY_UNARY, service.datamanager.v1.data_manager_pb2.SyncRequest, service.datamanager.v1.data_manager_pb2.SyncResponse), '/viam.service.datamanager.v1.DataManagerService/DoCommand': grpclib.const.Handler(self.DoCommand, grpclib.const.Cardinality.UNARY_UNARY, common.v1.common_pb2.DoCommandRequest, common.v1.common_pb2.DoCommandResponse)}

class UnimplementedDataManagerServiceBase(DataManagerServiceBase):

    async def Sync(self, stream: 'grpclib.server.Stream[service.datamanager.v1.data_manager_pb2.SyncRequest, service.datamanager.v1.data_manager_pb2.SyncResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def DoCommand(self, stream: 'grpclib.server.Stream[common.v1.common_pb2.DoCommandRequest, common.v1.common_pb2.DoCommandResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

class DataManagerServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.Sync = grpclib.client.UnaryUnaryMethod(channel, '/viam.service.datamanager.v1.DataManagerService/Sync', service.datamanager.v1.data_manager_pb2.SyncRequest, service.datamanager.v1.data_manager_pb2.SyncResponse)
        self.DoCommand = grpclib.client.UnaryUnaryMethod(channel, '/viam.service.datamanager.v1.DataManagerService/DoCommand', common.v1.common_pb2.DoCommandRequest, common.v1.common_pb2.DoCommandResponse)