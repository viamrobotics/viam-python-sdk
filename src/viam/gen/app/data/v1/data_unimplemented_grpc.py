import abc
import typing
import grpclib.const
import grpclib.exceptions
if typing.TYPE_CHECKING:
    import grpclib.server
import google.protobuf.any_pb2
import google.protobuf.struct_pb2
import google.protobuf.timestamp_pb2
from .... import app
from .data_grpc import DataServiceBase as _DataServiceBase

class UnimplementedDataServiceBase(_DataServiceBase):

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