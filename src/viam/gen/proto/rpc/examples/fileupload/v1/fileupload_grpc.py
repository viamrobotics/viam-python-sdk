import abc
import typing
import grpclib.const
import grpclib.client
import grpclib.exceptions
if typing.TYPE_CHECKING:
    import grpclib.server
from ...... import proto

class FileUploadServiceBase(abc.ABC):

    @abc.abstractmethod
    async def UploadFile(self, stream: 'grpclib.server.Stream[proto.rpc.examples.fileupload.v1.fileupload_pb2.UploadFileRequest, proto.rpc.examples.fileupload.v1.fileupload_pb2.UploadFileResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/proto.rpc.examples.fileupload.v1.FileUploadService/UploadFile': grpclib.const.Handler(self.UploadFile, grpclib.const.Cardinality.STREAM_STREAM, proto.rpc.examples.fileupload.v1.fileupload_pb2.UploadFileRequest, proto.rpc.examples.fileupload.v1.fileupload_pb2.UploadFileResponse)}

class UnimplementedFileUploadServiceBase(FileUploadServiceBase):

    async def UploadFile(self, stream: 'grpclib.server.Stream[proto.rpc.examples.fileupload.v1.fileupload_pb2.UploadFileRequest, proto.rpc.examples.fileupload.v1.fileupload_pb2.UploadFileResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

class FileUploadServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.UploadFile = grpclib.client.StreamStreamMethod(channel, '/proto.rpc.examples.fileupload.v1.FileUploadService/UploadFile', proto.rpc.examples.fileupload.v1.fileupload_pb2.UploadFileRequest, proto.rpc.examples.fileupload.v1.fileupload_pb2.UploadFileResponse)