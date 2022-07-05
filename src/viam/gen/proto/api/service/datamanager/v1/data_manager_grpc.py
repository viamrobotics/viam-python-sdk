import abc
import typing
import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server
import google.api.annotations_pb2
from ...... import proto

class DataManagerServiceBase(abc.ABC):

    @abc.abstractmethod
    async def Sync(self, stream: 'grpclib.server.Stream[proto.api.service.datamanager.v1.data_manager_pb2.SyncRequest, proto.api.service.datamanager.v1.data_manager_pb2.SyncResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/proto.api.service.datamanager.v1.DataManagerService/Sync': grpclib.const.Handler(self.Sync, grpclib.const.Cardinality.UNARY_UNARY, proto.api.service.datamanager.v1.data_manager_pb2.SyncRequest, proto.api.service.datamanager.v1.data_manager_pb2.SyncResponse)}

class DataManagerServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.Sync = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.service.datamanager.v1.DataManagerService/Sync', proto.api.service.datamanager.v1.data_manager_pb2.SyncRequest, proto.api.service.datamanager.v1.data_manager_pb2.SyncResponse)