import abc
import typing
import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server
import google.protobuf.timestamp_pb2
from .... import app

class DataServiceBase(abc.ABC):

    @abc.abstractmethod
    async def Query(self, stream: 'grpclib.server.Stream[app.data.v1.data_pb2.QueryRequest, app.data.v1.data_pb2.QueryResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/viam.app.data.v1.DataService/Query': grpclib.const.Handler(self.Query, grpclib.const.Cardinality.UNARY_UNARY, app.data.v1.data_pb2.QueryRequest, app.data.v1.data_pb2.QueryResponse)}

class DataServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.Query = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.data.v1.DataService/Query', app.data.v1.data_pb2.QueryRequest, app.data.v1.data_pb2.QueryResponse)