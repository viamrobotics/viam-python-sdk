import abc
import typing
import grpclib.const
import grpclib.client
import grpclib.exceptions
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
    async def TabularDataBySQL(self, stream: 'grpclib.server.Stream[app.data.v1.data_pb2.TabularDataBySQLRequest, app.data.v1.data_pb2.TabularDataBySQLResponse]') -> None:
        pass

    @abc.abstractmethod
    async def TabularDataByMQL(self, stream: 'grpclib.server.Stream[app.data.v1.data_pb2.TabularDataByMQLRequest, app.data.v1.data_pb2.TabularDataByMQLResponse]') -> None:
        pass

    @abc.abstractmethod
    async def BinaryDataByFilter(self, stream: 'grpclib.server.Stream[app.data.v1.data_pb2.BinaryDataByFilterRequest, app.data.v1.data_pb2.BinaryDataByFilterResponse]') -> None:
        pass

    @abc.abstractmethod
    async def BinaryDataByIDs(self, stream: 'grpclib.server.Stream[app.data.v1.data_pb2.BinaryDataByIDsRequest, app.data.v1.data_pb2.BinaryDataByIDsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def DeleteTabularData(self, stream: 'grpclib.server.Stream[app.data.v1.data_pb2.DeleteTabularDataRequest, app.data.v1.data_pb2.DeleteTabularDataResponse]') -> None:
        pass

    @abc.abstractmethod
    async def DeleteBinaryDataByFilter(self, stream: 'grpclib.server.Stream[app.data.v1.data_pb2.DeleteBinaryDataByFilterRequest, app.data.v1.data_pb2.DeleteBinaryDataByFilterResponse]') -> None:
        pass

    @abc.abstractmethod
    async def DeleteBinaryDataByIDs(self, stream: 'grpclib.server.Stream[app.data.v1.data_pb2.DeleteBinaryDataByIDsRequest, app.data.v1.data_pb2.DeleteBinaryDataByIDsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def AddTagsToBinaryDataByIDs(self, stream: 'grpclib.server.Stream[app.data.v1.data_pb2.AddTagsToBinaryDataByIDsRequest, app.data.v1.data_pb2.AddTagsToBinaryDataByIDsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def AddTagsToBinaryDataByFilter(self, stream: 'grpclib.server.Stream[app.data.v1.data_pb2.AddTagsToBinaryDataByFilterRequest, app.data.v1.data_pb2.AddTagsToBinaryDataByFilterResponse]') -> None:
        pass

    @abc.abstractmethod
    async def RemoveTagsFromBinaryDataByIDs(self, stream: 'grpclib.server.Stream[app.data.v1.data_pb2.RemoveTagsFromBinaryDataByIDsRequest, app.data.v1.data_pb2.RemoveTagsFromBinaryDataByIDsResponse]') -> None:
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

    @abc.abstractmethod
    async def GetDatabaseConnection(self, stream: 'grpclib.server.Stream[app.data.v1.data_pb2.GetDatabaseConnectionRequest, app.data.v1.data_pb2.GetDatabaseConnectionResponse]') -> None:
        pass

    @abc.abstractmethod
    async def ConfigureDatabaseUser(self, stream: 'grpclib.server.Stream[app.data.v1.data_pb2.ConfigureDatabaseUserRequest, app.data.v1.data_pb2.ConfigureDatabaseUserResponse]') -> None:
        pass

    @abc.abstractmethod
    async def AddBinaryDataToDatasetByIDs(self, stream: 'grpclib.server.Stream[app.data.v1.data_pb2.AddBinaryDataToDatasetByIDsRequest, app.data.v1.data_pb2.AddBinaryDataToDatasetByIDsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def RemoveBinaryDataFromDatasetByIDs(self, stream: 'grpclib.server.Stream[app.data.v1.data_pb2.RemoveBinaryDataFromDatasetByIDsRequest, app.data.v1.data_pb2.RemoveBinaryDataFromDatasetByIDsResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/viam.app.data.v1.DataService/TabularDataByFilter': grpclib.const.Handler(self.TabularDataByFilter, grpclib.const.Cardinality.UNARY_UNARY, app.data.v1.data_pb2.TabularDataByFilterRequest, app.data.v1.data_pb2.TabularDataByFilterResponse), '/viam.app.data.v1.DataService/TabularDataBySQL': grpclib.const.Handler(self.TabularDataBySQL, grpclib.const.Cardinality.UNARY_UNARY, app.data.v1.data_pb2.TabularDataBySQLRequest, app.data.v1.data_pb2.TabularDataBySQLResponse), '/viam.app.data.v1.DataService/TabularDataByMQL': grpclib.const.Handler(self.TabularDataByMQL, grpclib.const.Cardinality.UNARY_UNARY, app.data.v1.data_pb2.TabularDataByMQLRequest, app.data.v1.data_pb2.TabularDataByMQLResponse), '/viam.app.data.v1.DataService/BinaryDataByFilter': grpclib.const.Handler(self.BinaryDataByFilter, grpclib.const.Cardinality.UNARY_UNARY, app.data.v1.data_pb2.BinaryDataByFilterRequest, app.data.v1.data_pb2.BinaryDataByFilterResponse), '/viam.app.data.v1.DataService/BinaryDataByIDs': grpclib.const.Handler(self.BinaryDataByIDs, grpclib.const.Cardinality.UNARY_UNARY, app.data.v1.data_pb2.BinaryDataByIDsRequest, app.data.v1.data_pb2.BinaryDataByIDsResponse), '/viam.app.data.v1.DataService/DeleteTabularData': grpclib.const.Handler(self.DeleteTabularData, grpclib.const.Cardinality.UNARY_UNARY, app.data.v1.data_pb2.DeleteTabularDataRequest, app.data.v1.data_pb2.DeleteTabularDataResponse), '/viam.app.data.v1.DataService/DeleteBinaryDataByFilter': grpclib.const.Handler(self.DeleteBinaryDataByFilter, grpclib.const.Cardinality.UNARY_UNARY, app.data.v1.data_pb2.DeleteBinaryDataByFilterRequest, app.data.v1.data_pb2.DeleteBinaryDataByFilterResponse), '/viam.app.data.v1.DataService/DeleteBinaryDataByIDs': grpclib.const.Handler(self.DeleteBinaryDataByIDs, grpclib.const.Cardinality.UNARY_UNARY, app.data.v1.data_pb2.DeleteBinaryDataByIDsRequest, app.data.v1.data_pb2.DeleteBinaryDataByIDsResponse), '/viam.app.data.v1.DataService/AddTagsToBinaryDataByIDs': grpclib.const.Handler(self.AddTagsToBinaryDataByIDs, grpclib.const.Cardinality.UNARY_UNARY, app.data.v1.data_pb2.AddTagsToBinaryDataByIDsRequest, app.data.v1.data_pb2.AddTagsToBinaryDataByIDsResponse), '/viam.app.data.v1.DataService/AddTagsToBinaryDataByFilter': grpclib.const.Handler(self.AddTagsToBinaryDataByFilter, grpclib.const.Cardinality.UNARY_UNARY, app.data.v1.data_pb2.AddTagsToBinaryDataByFilterRequest, app.data.v1.data_pb2.AddTagsToBinaryDataByFilterResponse), '/viam.app.data.v1.DataService/RemoveTagsFromBinaryDataByIDs': grpclib.const.Handler(self.RemoveTagsFromBinaryDataByIDs, grpclib.const.Cardinality.UNARY_UNARY, app.data.v1.data_pb2.RemoveTagsFromBinaryDataByIDsRequest, app.data.v1.data_pb2.RemoveTagsFromBinaryDataByIDsResponse), '/viam.app.data.v1.DataService/RemoveTagsFromBinaryDataByFilter': grpclib.const.Handler(self.RemoveTagsFromBinaryDataByFilter, grpclib.const.Cardinality.UNARY_UNARY, app.data.v1.data_pb2.RemoveTagsFromBinaryDataByFilterRequest, app.data.v1.data_pb2.RemoveTagsFromBinaryDataByFilterResponse), '/viam.app.data.v1.DataService/TagsByFilter': grpclib.const.Handler(self.TagsByFilter, grpclib.const.Cardinality.UNARY_UNARY, app.data.v1.data_pb2.TagsByFilterRequest, app.data.v1.data_pb2.TagsByFilterResponse), '/viam.app.data.v1.DataService/AddBoundingBoxToImageByID': grpclib.const.Handler(self.AddBoundingBoxToImageByID, grpclib.const.Cardinality.UNARY_UNARY, app.data.v1.data_pb2.AddBoundingBoxToImageByIDRequest, app.data.v1.data_pb2.AddBoundingBoxToImageByIDResponse), '/viam.app.data.v1.DataService/RemoveBoundingBoxFromImageByID': grpclib.const.Handler(self.RemoveBoundingBoxFromImageByID, grpclib.const.Cardinality.UNARY_UNARY, app.data.v1.data_pb2.RemoveBoundingBoxFromImageByIDRequest, app.data.v1.data_pb2.RemoveBoundingBoxFromImageByIDResponse), '/viam.app.data.v1.DataService/BoundingBoxLabelsByFilter': grpclib.const.Handler(self.BoundingBoxLabelsByFilter, grpclib.const.Cardinality.UNARY_UNARY, app.data.v1.data_pb2.BoundingBoxLabelsByFilterRequest, app.data.v1.data_pb2.BoundingBoxLabelsByFilterResponse), '/viam.app.data.v1.DataService/GetDatabaseConnection': grpclib.const.Handler(self.GetDatabaseConnection, grpclib.const.Cardinality.UNARY_UNARY, app.data.v1.data_pb2.GetDatabaseConnectionRequest, app.data.v1.data_pb2.GetDatabaseConnectionResponse), '/viam.app.data.v1.DataService/ConfigureDatabaseUser': grpclib.const.Handler(self.ConfigureDatabaseUser, grpclib.const.Cardinality.UNARY_UNARY, app.data.v1.data_pb2.ConfigureDatabaseUserRequest, app.data.v1.data_pb2.ConfigureDatabaseUserResponse), '/viam.app.data.v1.DataService/AddBinaryDataToDatasetByIDs': grpclib.const.Handler(self.AddBinaryDataToDatasetByIDs, grpclib.const.Cardinality.UNARY_UNARY, app.data.v1.data_pb2.AddBinaryDataToDatasetByIDsRequest, app.data.v1.data_pb2.AddBinaryDataToDatasetByIDsResponse), '/viam.app.data.v1.DataService/RemoveBinaryDataFromDatasetByIDs': grpclib.const.Handler(self.RemoveBinaryDataFromDatasetByIDs, grpclib.const.Cardinality.UNARY_UNARY, app.data.v1.data_pb2.RemoveBinaryDataFromDatasetByIDsRequest, app.data.v1.data_pb2.RemoveBinaryDataFromDatasetByIDsResponse)}

class UnimplementedDataServiceBase(DataServiceBase):

    async def TabularDataByFilter(self, stream: 'grpclib.server.Stream[app.data.v1.data_pb2.TabularDataByFilterRequest, app.data.v1.data_pb2.TabularDataByFilterResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def TabularDataBySQL(self, stream: 'grpclib.server.Stream[app.data.v1.data_pb2.TabularDataBySQLRequest, app.data.v1.data_pb2.TabularDataBySQLResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def TabularDataByMQL(self, stream: 'grpclib.server.Stream[app.data.v1.data_pb2.TabularDataByMQLRequest, app.data.v1.data_pb2.TabularDataByMQLResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def BinaryDataByFilter(self, stream: 'grpclib.server.Stream[app.data.v1.data_pb2.BinaryDataByFilterRequest, app.data.v1.data_pb2.BinaryDataByFilterResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def BinaryDataByIDs(self, stream: 'grpclib.server.Stream[app.data.v1.data_pb2.BinaryDataByIDsRequest, app.data.v1.data_pb2.BinaryDataByIDsResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def DeleteTabularData(self, stream: 'grpclib.server.Stream[app.data.v1.data_pb2.DeleteTabularDataRequest, app.data.v1.data_pb2.DeleteTabularDataResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def DeleteBinaryDataByFilter(self, stream: 'grpclib.server.Stream[app.data.v1.data_pb2.DeleteBinaryDataByFilterRequest, app.data.v1.data_pb2.DeleteBinaryDataByFilterResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def DeleteBinaryDataByIDs(self, stream: 'grpclib.server.Stream[app.data.v1.data_pb2.DeleteBinaryDataByIDsRequest, app.data.v1.data_pb2.DeleteBinaryDataByIDsResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def AddTagsToBinaryDataByIDs(self, stream: 'grpclib.server.Stream[app.data.v1.data_pb2.AddTagsToBinaryDataByIDsRequest, app.data.v1.data_pb2.AddTagsToBinaryDataByIDsResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def AddTagsToBinaryDataByFilter(self, stream: 'grpclib.server.Stream[app.data.v1.data_pb2.AddTagsToBinaryDataByFilterRequest, app.data.v1.data_pb2.AddTagsToBinaryDataByFilterResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def RemoveTagsFromBinaryDataByIDs(self, stream: 'grpclib.server.Stream[app.data.v1.data_pb2.RemoveTagsFromBinaryDataByIDsRequest, app.data.v1.data_pb2.RemoveTagsFromBinaryDataByIDsResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def RemoveTagsFromBinaryDataByFilter(self, stream: 'grpclib.server.Stream[app.data.v1.data_pb2.RemoveTagsFromBinaryDataByFilterRequest, app.data.v1.data_pb2.RemoveTagsFromBinaryDataByFilterResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def TagsByFilter(self, stream: 'grpclib.server.Stream[app.data.v1.data_pb2.TagsByFilterRequest, app.data.v1.data_pb2.TagsByFilterResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def AddBoundingBoxToImageByID(self, stream: 'grpclib.server.Stream[app.data.v1.data_pb2.AddBoundingBoxToImageByIDRequest, app.data.v1.data_pb2.AddBoundingBoxToImageByIDResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def RemoveBoundingBoxFromImageByID(self, stream: 'grpclib.server.Stream[app.data.v1.data_pb2.RemoveBoundingBoxFromImageByIDRequest, app.data.v1.data_pb2.RemoveBoundingBoxFromImageByIDResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def BoundingBoxLabelsByFilter(self, stream: 'grpclib.server.Stream[app.data.v1.data_pb2.BoundingBoxLabelsByFilterRequest, app.data.v1.data_pb2.BoundingBoxLabelsByFilterResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def GetDatabaseConnection(self, stream: 'grpclib.server.Stream[app.data.v1.data_pb2.GetDatabaseConnectionRequest, app.data.v1.data_pb2.GetDatabaseConnectionResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def ConfigureDatabaseUser(self, stream: 'grpclib.server.Stream[app.data.v1.data_pb2.ConfigureDatabaseUserRequest, app.data.v1.data_pb2.ConfigureDatabaseUserResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def AddBinaryDataToDatasetByIDs(self, stream: 'grpclib.server.Stream[app.data.v1.data_pb2.AddBinaryDataToDatasetByIDsRequest, app.data.v1.data_pb2.AddBinaryDataToDatasetByIDsResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def RemoveBinaryDataFromDatasetByIDs(self, stream: 'grpclib.server.Stream[app.data.v1.data_pb2.RemoveBinaryDataFromDatasetByIDsRequest, app.data.v1.data_pb2.RemoveBinaryDataFromDatasetByIDsResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

class DataServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.TabularDataByFilter = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.data.v1.DataService/TabularDataByFilter', app.data.v1.data_pb2.TabularDataByFilterRequest, app.data.v1.data_pb2.TabularDataByFilterResponse)
        self.TabularDataBySQL = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.data.v1.DataService/TabularDataBySQL', app.data.v1.data_pb2.TabularDataBySQLRequest, app.data.v1.data_pb2.TabularDataBySQLResponse)
        self.TabularDataByMQL = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.data.v1.DataService/TabularDataByMQL', app.data.v1.data_pb2.TabularDataByMQLRequest, app.data.v1.data_pb2.TabularDataByMQLResponse)
        self.BinaryDataByFilter = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.data.v1.DataService/BinaryDataByFilter', app.data.v1.data_pb2.BinaryDataByFilterRequest, app.data.v1.data_pb2.BinaryDataByFilterResponse)
        self.BinaryDataByIDs = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.data.v1.DataService/BinaryDataByIDs', app.data.v1.data_pb2.BinaryDataByIDsRequest, app.data.v1.data_pb2.BinaryDataByIDsResponse)
        self.DeleteTabularData = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.data.v1.DataService/DeleteTabularData', app.data.v1.data_pb2.DeleteTabularDataRequest, app.data.v1.data_pb2.DeleteTabularDataResponse)
        self.DeleteBinaryDataByFilter = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.data.v1.DataService/DeleteBinaryDataByFilter', app.data.v1.data_pb2.DeleteBinaryDataByFilterRequest, app.data.v1.data_pb2.DeleteBinaryDataByFilterResponse)
        self.DeleteBinaryDataByIDs = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.data.v1.DataService/DeleteBinaryDataByIDs', app.data.v1.data_pb2.DeleteBinaryDataByIDsRequest, app.data.v1.data_pb2.DeleteBinaryDataByIDsResponse)
        self.AddTagsToBinaryDataByIDs = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.data.v1.DataService/AddTagsToBinaryDataByIDs', app.data.v1.data_pb2.AddTagsToBinaryDataByIDsRequest, app.data.v1.data_pb2.AddTagsToBinaryDataByIDsResponse)
        self.AddTagsToBinaryDataByFilter = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.data.v1.DataService/AddTagsToBinaryDataByFilter', app.data.v1.data_pb2.AddTagsToBinaryDataByFilterRequest, app.data.v1.data_pb2.AddTagsToBinaryDataByFilterResponse)
        self.RemoveTagsFromBinaryDataByIDs = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.data.v1.DataService/RemoveTagsFromBinaryDataByIDs', app.data.v1.data_pb2.RemoveTagsFromBinaryDataByIDsRequest, app.data.v1.data_pb2.RemoveTagsFromBinaryDataByIDsResponse)
        self.RemoveTagsFromBinaryDataByFilter = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.data.v1.DataService/RemoveTagsFromBinaryDataByFilter', app.data.v1.data_pb2.RemoveTagsFromBinaryDataByFilterRequest, app.data.v1.data_pb2.RemoveTagsFromBinaryDataByFilterResponse)
        self.TagsByFilter = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.data.v1.DataService/TagsByFilter', app.data.v1.data_pb2.TagsByFilterRequest, app.data.v1.data_pb2.TagsByFilterResponse)
        self.AddBoundingBoxToImageByID = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.data.v1.DataService/AddBoundingBoxToImageByID', app.data.v1.data_pb2.AddBoundingBoxToImageByIDRequest, app.data.v1.data_pb2.AddBoundingBoxToImageByIDResponse)
        self.RemoveBoundingBoxFromImageByID = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.data.v1.DataService/RemoveBoundingBoxFromImageByID', app.data.v1.data_pb2.RemoveBoundingBoxFromImageByIDRequest, app.data.v1.data_pb2.RemoveBoundingBoxFromImageByIDResponse)
        self.BoundingBoxLabelsByFilter = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.data.v1.DataService/BoundingBoxLabelsByFilter', app.data.v1.data_pb2.BoundingBoxLabelsByFilterRequest, app.data.v1.data_pb2.BoundingBoxLabelsByFilterResponse)
        self.GetDatabaseConnection = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.data.v1.DataService/GetDatabaseConnection', app.data.v1.data_pb2.GetDatabaseConnectionRequest, app.data.v1.data_pb2.GetDatabaseConnectionResponse)
        self.ConfigureDatabaseUser = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.data.v1.DataService/ConfigureDatabaseUser', app.data.v1.data_pb2.ConfigureDatabaseUserRequest, app.data.v1.data_pb2.ConfigureDatabaseUserResponse)
        self.AddBinaryDataToDatasetByIDs = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.data.v1.DataService/AddBinaryDataToDatasetByIDs', app.data.v1.data_pb2.AddBinaryDataToDatasetByIDsRequest, app.data.v1.data_pb2.AddBinaryDataToDatasetByIDsResponse)
        self.RemoveBinaryDataFromDatasetByIDs = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.data.v1.DataService/RemoveBinaryDataFromDatasetByIDs', app.data.v1.data_pb2.RemoveBinaryDataFromDatasetByIDsRequest, app.data.v1.data_pb2.RemoveBinaryDataFromDatasetByIDsResponse)