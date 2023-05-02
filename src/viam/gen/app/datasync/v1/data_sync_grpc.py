import abc
import typing
import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server
import google.protobuf.any_pb2
import google.protobuf.struct_pb2
import google.protobuf.timestamp_pb2
from .... import tagger
from .... import app

class DataSyncServiceBase(abc.ABC):

    @abc.abstractmethod
    async def DataCaptureUpload(self, stream: 'grpclib.server.Stream[app.datasync.v1.data_sync_pb2.DataCaptureUploadRequest, app.datasync.v1.data_sync_pb2.DataCaptureUploadResponse]') -> None:
        pass

    @abc.abstractmethod
    async def FileUpload(self, stream: 'grpclib.server.Stream[app.datasync.v1.data_sync_pb2.FileUploadRequest, app.datasync.v1.data_sync_pb2.FileUploadResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/viam.app.datasync.v1.DataSyncService/DataCaptureUpload': grpclib.const.Handler(self.DataCaptureUpload, grpclib.const.Cardinality.UNARY_UNARY, app.datasync.v1.data_sync_pb2.DataCaptureUploadRequest, app.datasync.v1.data_sync_pb2.DataCaptureUploadResponse), '/viam.app.datasync.v1.DataSyncService/FileUpload': grpclib.const.Handler(self.FileUpload, grpclib.const.Cardinality.STREAM_UNARY, app.datasync.v1.data_sync_pb2.FileUploadRequest, app.datasync.v1.data_sync_pb2.FileUploadResponse)}

class DataSyncServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.DataCaptureUpload = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.datasync.v1.DataSyncService/DataCaptureUpload', app.datasync.v1.data_sync_pb2.DataCaptureUploadRequest, app.datasync.v1.data_sync_pb2.DataCaptureUploadResponse)
        self.FileUpload = grpclib.client.StreamUnaryMethod(channel, '/viam.app.datasync.v1.DataSyncService/FileUpload', app.datasync.v1.data_sync_pb2.FileUploadRequest, app.datasync.v1.data_sync_pb2.FileUploadResponse)