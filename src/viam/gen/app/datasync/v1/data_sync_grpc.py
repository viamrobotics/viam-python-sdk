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
    async def Upload(self, stream: 'grpclib.server.Stream[app.datasync.v1.data_sync_pb2.UploadRequest, app.datasync.v1.data_sync_pb2.UploadResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/viam.app.datasync.v1.DataSyncService/Upload': grpclib.const.Handler(self.Upload, grpclib.const.Cardinality.STREAM_STREAM, app.datasync.v1.data_sync_pb2.UploadRequest, app.datasync.v1.data_sync_pb2.UploadResponse)}

class DataSyncServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.Upload = grpclib.client.StreamStreamMethod(channel, '/viam.app.datasync.v1.DataSyncService/Upload', app.datasync.v1.data_sync_pb2.UploadRequest, app.datasync.v1.data_sync_pb2.UploadResponse)