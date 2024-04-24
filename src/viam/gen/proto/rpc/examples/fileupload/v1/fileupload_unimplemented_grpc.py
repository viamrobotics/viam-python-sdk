import abc
import typing
import grpclib.const
import grpclib.exceptions
if typing.TYPE_CHECKING:
    import grpclib.server
from ...... import proto
from .fileupload_grpc import FileUploadServiceBase as _FileUploadServiceBase

class UnimplementedFileUploadServiceBase(_FileUploadServiceBase):

    async def UploadFile(self, stream: 'grpclib.server.Stream[proto.rpc.examples.fileupload.v1.fileupload_pb2.UploadFileRequest, proto.rpc.examples.fileupload.v1.fileupload_pb2.UploadFileResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)