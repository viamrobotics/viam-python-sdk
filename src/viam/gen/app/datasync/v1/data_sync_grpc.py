import abc
import typing
import grpclib.const
import grpclib.client
import grpclib.exceptions
if typing.TYPE_CHECKING:
    import grpclib.server
import google.api.annotations_pb2
import google.protobuf.any_pb2
import google.protobuf.struct_pb2
import google.protobuf.timestamp_pb2
from .... import app

class DataSyncServiceBase(abc.ABC):

    @abc.abstractmethod
    async def DataCaptureUpload(self, stream: 'grpclib.server.Stream[app.datasync.v1.data_sync_pb2.DataCaptureUploadRequest, app.datasync.v1.data_sync_pb2.DataCaptureUploadResponse]') -> None:
        pass

    @abc.abstractmethod
    async def FileUpload(self, stream: 'grpclib.server.Stream[app.datasync.v1.data_sync_pb2.FileUploadRequest, app.datasync.v1.data_sync_pb2.FileUploadResponse]') -> None:
        pass

    @abc.abstractmethod
    async def StreamingDataCaptureUpload(self, stream: 'grpclib.server.Stream[app.datasync.v1.data_sync_pb2.StreamingDataCaptureUploadRequest, app.datasync.v1.data_sync_pb2.StreamingDataCaptureUploadResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/viam.app.datasync.v1.DataSyncService/DataCaptureUpload': grpclib.const.Handler(self.DataCaptureUpload, grpclib.const.Cardinality.UNARY_UNARY, app.datasync.v1.data_sync_pb2.DataCaptureUploadRequest, app.datasync.v1.data_sync_pb2.DataCaptureUploadResponse), '/viam.app.datasync.v1.DataSyncService/FileUpload': grpclib.const.Handler(self.FileUpload, grpclib.const.Cardinality.STREAM_UNARY, app.datasync.v1.data_sync_pb2.FileUploadRequest, app.datasync.v1.data_sync_pb2.FileUploadResponse), '/viam.app.datasync.v1.DataSyncService/StreamingDataCaptureUpload': grpclib.const.Handler(self.StreamingDataCaptureUpload, grpclib.const.Cardinality.STREAM_UNARY, app.datasync.v1.data_sync_pb2.StreamingDataCaptureUploadRequest, app.datasync.v1.data_sync_pb2.StreamingDataCaptureUploadResponse)}

class UnimplementedDataSyncServiceBase(DataSyncServiceBase):

    async def DataCaptureUpload(self, stream: 'grpclib.server.Stream[app.datasync.v1.data_sync_pb2.DataCaptureUploadRequest, app.datasync.v1.data_sync_pb2.DataCaptureUploadResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def FileUpload(self, stream: 'grpclib.server.Stream[app.datasync.v1.data_sync_pb2.FileUploadRequest, app.datasync.v1.data_sync_pb2.FileUploadResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def StreamingDataCaptureUpload(self, stream: 'grpclib.server.Stream[app.datasync.v1.data_sync_pb2.StreamingDataCaptureUploadRequest, app.datasync.v1.data_sync_pb2.StreamingDataCaptureUploadResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

class DataSyncServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.DataCaptureUpload = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.datasync.v1.DataSyncService/DataCaptureUpload', app.datasync.v1.data_sync_pb2.DataCaptureUploadRequest, app.datasync.v1.data_sync_pb2.DataCaptureUploadResponse)
        self.FileUpload = grpclib.client.StreamUnaryMethod(channel, '/viam.app.datasync.v1.DataSyncService/FileUpload', app.datasync.v1.data_sync_pb2.FileUploadRequest, app.datasync.v1.data_sync_pb2.FileUploadResponse)
        self.StreamingDataCaptureUpload = grpclib.client.StreamUnaryMethod(channel, '/viam.app.datasync.v1.DataSyncService/StreamingDataCaptureUpload', app.datasync.v1.data_sync_pb2.StreamingDataCaptureUploadRequest, app.datasync.v1.data_sync_pb2.StreamingDataCaptureUploadResponse)