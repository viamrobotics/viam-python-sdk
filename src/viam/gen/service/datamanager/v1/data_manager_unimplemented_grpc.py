import abc
import typing
import grpclib.const
import grpclib.exceptions
if typing.TYPE_CHECKING:
    import grpclib.server
from .... import common
import google.api.annotations_pb2
import google.protobuf.struct_pb2
from .... import service
from .data_manager_grpc import DataManagerServiceBase as _DataManagerServiceBase

class UnimplementedDataManagerServiceBase(_DataManagerServiceBase):

    async def Sync(self, stream: 'grpclib.server.Stream[service.datamanager.v1.data_manager_pb2.SyncRequest, service.datamanager.v1.data_manager_pb2.SyncResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def DoCommand(self, stream: 'grpclib.server.Stream[common.v1.common_pb2.DoCommandRequest, common.v1.common_pb2.DoCommandResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)