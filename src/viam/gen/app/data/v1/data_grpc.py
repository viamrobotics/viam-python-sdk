import abc
import typing
import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server
import google.protobuf.any_pb2
import google.protobuf.struct_pb2
import google.protobuf.timestamp_pb2
from .... import app

class DataServiceBase(abc.ABC):

    @abc.abstractmethod
    async def TabularDataByFilter(self, stream: 'grpclib.server.Stream[app.data.v1.data_pb2.TabularDataByFilterRequest, app.data.v1.data_pb2.TabularDataByFilterResponse]') -> None:
        pass

    @abc.abstractmethod
    async def BinaryDataByFilter(self, stream: 'grpclib.server.Stream[app.data.v1.data_pb2.BinaryDataByFilterRequest, app.data.v1.data_pb2.BinaryDataByFilterResponse]') -> None:
        pass

    @abc.abstractmethod
    async def BinaryDataByIDs(self, stream: 'grpclib.server.Stream[app.data.v1.data_pb2.BinaryDataByIDsRequest, app.data.v1.data_pb2.BinaryDataByIDsResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/viam.app.data.v1.DataService/TabularDataByFilter': grpclib.const.Handler(self.TabularDataByFilter, grpclib.const.Cardinality.UNARY_UNARY, app.data.v1.data_pb2.TabularDataByFilterRequest, app.data.v1.data_pb2.TabularDataByFilterResponse), '/viam.app.data.v1.DataService/BinaryDataByFilter': grpclib.const.Handler(self.BinaryDataByFilter, grpclib.const.Cardinality.UNARY_UNARY, app.data.v1.data_pb2.BinaryDataByFilterRequest, app.data.v1.data_pb2.BinaryDataByFilterResponse), '/viam.app.data.v1.DataService/BinaryDataByIDs': grpclib.const.Handler(self.BinaryDataByIDs, grpclib.const.Cardinality.UNARY_UNARY, app.data.v1.data_pb2.BinaryDataByIDsRequest, app.data.v1.data_pb2.BinaryDataByIDsResponse)}

class DataServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.TabularDataByFilter = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.data.v1.DataService/TabularDataByFilter', app.data.v1.data_pb2.TabularDataByFilterRequest, app.data.v1.data_pb2.TabularDataByFilterResponse)
        self.BinaryDataByFilter = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.data.v1.DataService/BinaryDataByFilter', app.data.v1.data_pb2.BinaryDataByFilterRequest, app.data.v1.data_pb2.BinaryDataByFilterResponse)
        self.BinaryDataByIDs = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.data.v1.DataService/BinaryDataByIDs', app.data.v1.data_pb2.BinaryDataByIDsRequest, app.data.v1.data_pb2.BinaryDataByIDsResponse)