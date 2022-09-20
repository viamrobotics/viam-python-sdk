import abc
import typing
import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server
import google.api.annotations_pb2
from .... import service

class DataManagerServiceBase(abc.ABC):

    @abc.abstractmethod
    async def Sync(self, stream: 'grpclib.server.Stream[service.datamanager.v1.data_manager_pb2.SyncRequest, service.datamanager.v1.data_manager_pb2.SyncResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/viam.service.datamanager.v1.DataManagerService/Sync': grpclib.const.Handler(self.Sync, grpclib.const.Cardinality.UNARY_UNARY, service.datamanager.v1.data_manager_pb2.SyncRequest, service.datamanager.v1.data_manager_pb2.SyncResponse)}

class DataManagerServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.Sync = grpclib.client.UnaryUnaryMethod(channel, '/viam.service.datamanager.v1.DataManagerService/Sync', service.datamanager.v1.data_manager_pb2.SyncRequest, service.datamanager.v1.data_manager_pb2.SyncResponse)