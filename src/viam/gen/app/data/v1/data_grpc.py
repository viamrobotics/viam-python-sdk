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

    @abc.abstractmethod
    async def DeleteTabularDataByFilter(self, stream: 'grpclib.server.Stream[app.data.v1.data_pb2.DeleteTabularDataByFilterRequest, app.data.v1.data_pb2.DeleteTabularDataByFilterResponse]') -> None:
        pass

    @abc.abstractmethod
    async def DeleteBinaryDataByFilter(self, stream: 'grpclib.server.Stream[app.data.v1.data_pb2.DeleteBinaryDataByFilterRequest, app.data.v1.data_pb2.DeleteBinaryDataByFilterResponse]') -> None:
        pass

    @abc.abstractmethod
    async def DeleteBinaryDataByIDs(self, stream: 'grpclib.server.Stream[app.data.v1.data_pb2.DeleteBinaryDataByIDsRequest, app.data.v1.data_pb2.DeleteBinaryDataByIDsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def AddTagsToBinaryDataByFileIDs(self, stream: 'grpclib.server.Stream[app.data.v1.data_pb2.AddTagsToBinaryDataByFileIDsRequest, app.data.v1.data_pb2.AddTagsToBinaryDataByFileIDsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def AddTagsToBinaryDataByFilter(self, stream: 'grpclib.server.Stream[app.data.v1.data_pb2.AddTagsToBinaryDataByFilterRequest, app.data.v1.data_pb2.AddTagsToBinaryDataByFilterResponse]') -> None:
        pass

    @abc.abstractmethod
    async def RemoveTagsFromBinaryDataByFileIDs(self, stream: 'grpclib.server.Stream[app.data.v1.data_pb2.RemoveTagsFromBinaryDataByFileIDsRequest, app.data.v1.data_pb2.RemoveTagsFromBinaryDataByFileIDsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def RemoveTagsFromBinaryDataByFilter(self, stream: 'grpclib.server.Stream[app.data.v1.data_pb2.RemoveTagsFromBinaryDataByFilterRequest, app.data.v1.data_pb2.RemoveTagsFromBinaryDataByFilterResponse]') -> None:
        pass

    @abc.abstractmethod
    async def TagsByFilter(self, stream: 'grpclib.server.Stream[app.data.v1.data_pb2.TagsByFilterRequest, app.data.v1.data_pb2.TagsByFilterResponse]') -> None:
        pass

    @abc.abstractmethod
    async def AddBoundingBoxToImageByID(self, stream: 'grpclib.server.Stream[app.data.v1.data_pb2.AddBoundingBoxToImageByIDRequest, app.data.v1.data_pb2.AddBoundingBoxToImageByIDResponse]') -> None:
        pass

    @abc.abstractmethod
    async def RemoveBoundingBoxFromImageByID(self, stream: 'grpclib.server.Stream[app.data.v1.data_pb2.RemoveBoundingBoxFromImageByIDRequest, app.data.v1.data_pb2.RemoveBoundingBoxFromImageByIDResponse]') -> None:
        pass

    @abc.abstractmethod
    async def BoundingBoxLabelsByFilter(self, stream: 'grpclib.server.Stream[app.data.v1.data_pb2.BoundingBoxLabelsByFilterRequest, app.data.v1.data_pb2.BoundingBoxLabelsByFilterResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/viam.app.data.v1.DataService/TabularDataByFilter': grpclib.const.Handler(self.TabularDataByFilter, grpclib.const.Cardinality.UNARY_UNARY, app.data.v1.data_pb2.TabularDataByFilterRequest, app.data.v1.data_pb2.TabularDataByFilterResponse), '/viam.app.data.v1.DataService/BinaryDataByFilter': grpclib.const.Handler(self.BinaryDataByFilter, grpclib.const.Cardinality.UNARY_UNARY, app.data.v1.data_pb2.BinaryDataByFilterRequest, app.data.v1.data_pb2.BinaryDataByFilterResponse), '/viam.app.data.v1.DataService/BinaryDataByIDs': grpclib.const.Handler(self.BinaryDataByIDs, grpclib.const.Cardinality.UNARY_UNARY, app.data.v1.data_pb2.BinaryDataByIDsRequest, app.data.v1.data_pb2.BinaryDataByIDsResponse), '/viam.app.data.v1.DataService/DeleteTabularDataByFilter': grpclib.const.Handler(self.DeleteTabularDataByFilter, grpclib.const.Cardinality.UNARY_UNARY, app.data.v1.data_pb2.DeleteTabularDataByFilterRequest, app.data.v1.data_pb2.DeleteTabularDataByFilterResponse), '/viam.app.data.v1.DataService/DeleteBinaryDataByFilter': grpclib.const.Handler(self.DeleteBinaryDataByFilter, grpclib.const.Cardinality.UNARY_UNARY, app.data.v1.data_pb2.DeleteBinaryDataByFilterRequest, app.data.v1.data_pb2.DeleteBinaryDataByFilterResponse), '/viam.app.data.v1.DataService/DeleteBinaryDataByIDs': grpclib.const.Handler(self.DeleteBinaryDataByIDs, grpclib.const.Cardinality.UNARY_UNARY, app.data.v1.data_pb2.DeleteBinaryDataByIDsRequest, app.data.v1.data_pb2.DeleteBinaryDataByIDsResponse), '/viam.app.data.v1.DataService/AddTagsToBinaryDataByFileIDs': grpclib.const.Handler(self.AddTagsToBinaryDataByFileIDs, grpclib.const.Cardinality.UNARY_UNARY, app.data.v1.data_pb2.AddTagsToBinaryDataByFileIDsRequest, app.data.v1.data_pb2.AddTagsToBinaryDataByFileIDsResponse), '/viam.app.data.v1.DataService/AddTagsToBinaryDataByFilter': grpclib.const.Handler(self.AddTagsToBinaryDataByFilter, grpclib.const.Cardinality.UNARY_UNARY, app.data.v1.data_pb2.AddTagsToBinaryDataByFilterRequest, app.data.v1.data_pb2.AddTagsToBinaryDataByFilterResponse), '/viam.app.data.v1.DataService/RemoveTagsFromBinaryDataByFileIDs': grpclib.const.Handler(self.RemoveTagsFromBinaryDataByFileIDs, grpclib.const.Cardinality.UNARY_UNARY, app.data.v1.data_pb2.RemoveTagsFromBinaryDataByFileIDsRequest, app.data.v1.data_pb2.RemoveTagsFromBinaryDataByFileIDsResponse), '/viam.app.data.v1.DataService/RemoveTagsFromBinaryDataByFilter': grpclib.const.Handler(self.RemoveTagsFromBinaryDataByFilter, grpclib.const.Cardinality.UNARY_UNARY, app.data.v1.data_pb2.RemoveTagsFromBinaryDataByFilterRequest, app.data.v1.data_pb2.RemoveTagsFromBinaryDataByFilterResponse), '/viam.app.data.v1.DataService/TagsByFilter': grpclib.const.Handler(self.TagsByFilter, grpclib.const.Cardinality.UNARY_UNARY, app.data.v1.data_pb2.TagsByFilterRequest, app.data.v1.data_pb2.TagsByFilterResponse), '/viam.app.data.v1.DataService/AddBoundingBoxToImageByID': grpclib.const.Handler(self.AddBoundingBoxToImageByID, grpclib.const.Cardinality.UNARY_UNARY, app.data.v1.data_pb2.AddBoundingBoxToImageByIDRequest, app.data.v1.data_pb2.AddBoundingBoxToImageByIDResponse), '/viam.app.data.v1.DataService/RemoveBoundingBoxFromImageByID': grpclib.const.Handler(self.RemoveBoundingBoxFromImageByID, grpclib.const.Cardinality.UNARY_UNARY, app.data.v1.data_pb2.RemoveBoundingBoxFromImageByIDRequest, app.data.v1.data_pb2.RemoveBoundingBoxFromImageByIDResponse), '/viam.app.data.v1.DataService/BoundingBoxLabelsByFilter': grpclib.const.Handler(self.BoundingBoxLabelsByFilter, grpclib.const.Cardinality.UNARY_UNARY, app.data.v1.data_pb2.BoundingBoxLabelsByFilterRequest, app.data.v1.data_pb2.BoundingBoxLabelsByFilterResponse)}

class DataServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.TabularDataByFilter = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.data.v1.DataService/TabularDataByFilter', app.data.v1.data_pb2.TabularDataByFilterRequest, app.data.v1.data_pb2.TabularDataByFilterResponse)
        self.BinaryDataByFilter = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.data.v1.DataService/BinaryDataByFilter', app.data.v1.data_pb2.BinaryDataByFilterRequest, app.data.v1.data_pb2.BinaryDataByFilterResponse)
        self.BinaryDataByIDs = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.data.v1.DataService/BinaryDataByIDs', app.data.v1.data_pb2.BinaryDataByIDsRequest, app.data.v1.data_pb2.BinaryDataByIDsResponse)
        self.DeleteTabularDataByFilter = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.data.v1.DataService/DeleteTabularDataByFilter', app.data.v1.data_pb2.DeleteTabularDataByFilterRequest, app.data.v1.data_pb2.DeleteTabularDataByFilterResponse)
        self.DeleteBinaryDataByFilter = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.data.v1.DataService/DeleteBinaryDataByFilter', app.data.v1.data_pb2.DeleteBinaryDataByFilterRequest, app.data.v1.data_pb2.DeleteBinaryDataByFilterResponse)
        self.DeleteBinaryDataByIDs = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.data.v1.DataService/DeleteBinaryDataByIDs', app.data.v1.data_pb2.DeleteBinaryDataByIDsRequest, app.data.v1.data_pb2.DeleteBinaryDataByIDsResponse)
        self.AddTagsToBinaryDataByFileIDs = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.data.v1.DataService/AddTagsToBinaryDataByFileIDs', app.data.v1.data_pb2.AddTagsToBinaryDataByFileIDsRequest, app.data.v1.data_pb2.AddTagsToBinaryDataByFileIDsResponse)
        self.AddTagsToBinaryDataByFilter = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.data.v1.DataService/AddTagsToBinaryDataByFilter', app.data.v1.data_pb2.AddTagsToBinaryDataByFilterRequest, app.data.v1.data_pb2.AddTagsToBinaryDataByFilterResponse)
        self.RemoveTagsFromBinaryDataByFileIDs = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.data.v1.DataService/RemoveTagsFromBinaryDataByFileIDs', app.data.v1.data_pb2.RemoveTagsFromBinaryDataByFileIDsRequest, app.data.v1.data_pb2.RemoveTagsFromBinaryDataByFileIDsResponse)
        self.RemoveTagsFromBinaryDataByFilter = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.data.v1.DataService/RemoveTagsFromBinaryDataByFilter', app.data.v1.data_pb2.RemoveTagsFromBinaryDataByFilterRequest, app.data.v1.data_pb2.RemoveTagsFromBinaryDataByFilterResponse)
        self.TagsByFilter = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.data.v1.DataService/TagsByFilter', app.data.v1.data_pb2.TagsByFilterRequest, app.data.v1.data_pb2.TagsByFilterResponse)
        self.AddBoundingBoxToImageByID = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.data.v1.DataService/AddBoundingBoxToImageByID', app.data.v1.data_pb2.AddBoundingBoxToImageByIDRequest, app.data.v1.data_pb2.AddBoundingBoxToImageByIDResponse)
        self.RemoveBoundingBoxFromImageByID = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.data.v1.DataService/RemoveBoundingBoxFromImageByID', app.data.v1.data_pb2.RemoveBoundingBoxFromImageByIDRequest, app.data.v1.data_pb2.RemoveBoundingBoxFromImageByIDResponse)
        self.BoundingBoxLabelsByFilter = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.data.v1.DataService/BoundingBoxLabelsByFilter', app.data.v1.data_pb2.BoundingBoxLabelsByFilterRequest, app.data.v1.data_pb2.BoundingBoxLabelsByFilterResponse)