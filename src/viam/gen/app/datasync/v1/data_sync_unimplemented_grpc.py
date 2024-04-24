import abc
import typing
import grpclib.const
import grpclib.exceptions
if typing.TYPE_CHECKING:
    import grpclib.server
import google.api.annotations_pb2
import google.protobuf.any_pb2
import google.protobuf.struct_pb2
import google.protobuf.timestamp_pb2
from .... import app
from .data_sync_grpc import DataSyncServiceBase as _DataSyncServiceBase

class UnimplementedDataSyncServiceBase(_DataSyncServiceBase):

    async def DataCaptureUpload(self, stream: 'grpclib.server.Stream[app.datasync.v1.data_sync_pb2.DataCaptureUploadRequest, app.datasync.v1.data_sync_pb2.DataCaptureUploadResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def FileUpload(self, stream: 'grpclib.server.Stream[app.datasync.v1.data_sync_pb2.FileUploadRequest, app.datasync.v1.data_sync_pb2.FileUploadResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def StreamingDataCaptureUpload(self, stream: 'grpclib.server.Stream[app.datasync.v1.data_sync_pb2.StreamingDataCaptureUploadRequest, app.datasync.v1.data_sync_pb2.StreamingDataCaptureUploadResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)