import abc
import typing
import grpclib.const
import grpclib.client
import grpclib.exceptions
if typing.TYPE_CHECKING:
    import grpclib.server
import google.api.annotations_pb2
import google.protobuf.struct_pb2
from .... import service

class MLModelServiceBase(abc.ABC):

    @abc.abstractmethod
    async def Infer(self, stream: 'grpclib.server.Stream[service.mlmodel.v1.mlmodel_pb2.InferRequest, service.mlmodel.v1.mlmodel_pb2.InferResponse]') -> None:
        pass

    @abc.abstractmethod
    async def Metadata(self, stream: 'grpclib.server.Stream[service.mlmodel.v1.mlmodel_pb2.MetadataRequest, service.mlmodel.v1.mlmodel_pb2.MetadataResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/viam.service.mlmodel.v1.MLModelService/Infer': grpclib.const.Handler(self.Infer, grpclib.const.Cardinality.UNARY_UNARY, service.mlmodel.v1.mlmodel_pb2.InferRequest, service.mlmodel.v1.mlmodel_pb2.InferResponse), '/viam.service.mlmodel.v1.MLModelService/Metadata': grpclib.const.Handler(self.Metadata, grpclib.const.Cardinality.UNARY_UNARY, service.mlmodel.v1.mlmodel_pb2.MetadataRequest, service.mlmodel.v1.mlmodel_pb2.MetadataResponse)}

class UnimplementedMLModelServiceBase(MLModelServiceBase):

    async def Infer(self, stream: 'grpclib.server.Stream[service.mlmodel.v1.mlmodel_pb2.InferRequest, service.mlmodel.v1.mlmodel_pb2.InferResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def Metadata(self, stream: 'grpclib.server.Stream[service.mlmodel.v1.mlmodel_pb2.MetadataRequest, service.mlmodel.v1.mlmodel_pb2.MetadataResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

class MLModelServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.Infer = grpclib.client.UnaryUnaryMethod(channel, '/viam.service.mlmodel.v1.MLModelService/Infer', service.mlmodel.v1.mlmodel_pb2.InferRequest, service.mlmodel.v1.mlmodel_pb2.InferResponse)
        self.Metadata = grpclib.client.UnaryUnaryMethod(channel, '/viam.service.mlmodel.v1.MLModelService/Metadata', service.mlmodel.v1.mlmodel_pb2.MetadataRequest, service.mlmodel.v1.mlmodel_pb2.MetadataResponse)