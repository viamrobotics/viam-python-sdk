import abc
import typing
import grpclib.const
import grpclib.exceptions
if typing.TYPE_CHECKING:
    import grpclib.server
import google.api.annotations_pb2
import google.protobuf.struct_pb2
from .... import service
from .mlmodel_grpc import MLModelServiceBase as _MLModelServiceBase

class UnimplementedMLModelServiceBase(_MLModelServiceBase):

    async def Infer(self, stream: 'grpclib.server.Stream[service.mlmodel.v1.mlmodel_pb2.InferRequest, service.mlmodel.v1.mlmodel_pb2.InferResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def Metadata(self, stream: 'grpclib.server.Stream[service.mlmodel.v1.mlmodel_pb2.MetadataRequest, service.mlmodel.v1.mlmodel_pb2.MetadataResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)