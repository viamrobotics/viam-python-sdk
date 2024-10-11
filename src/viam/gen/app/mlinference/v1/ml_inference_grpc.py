import abc
import typing
import grpclib.const
import grpclib.client
import grpclib.exceptions
if typing.TYPE_CHECKING:
    import grpclib.server
from .... import app

class MLInferenceServiceBase(abc.ABC):

    @abc.abstractmethod
    async def GetInference(self, stream: 'grpclib.server.Stream[app.mlinference.v1.ml_inference_pb2.GetInferenceRequest, app.mlinference.v1.ml_inference_pb2.GetInferenceResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/viam.app.mlinference.v1.MLInferenceService/GetInference': grpclib.const.Handler(self.GetInference, grpclib.const.Cardinality.UNARY_UNARY, app.mlinference.v1.ml_inference_pb2.GetInferenceRequest, app.mlinference.v1.ml_inference_pb2.GetInferenceResponse)}

class UnimplementedMLInferenceServiceBase(MLInferenceServiceBase):

    async def GetInference(self, stream: 'grpclib.server.Stream[app.mlinference.v1.ml_inference_pb2.GetInferenceRequest, app.mlinference.v1.ml_inference_pb2.GetInferenceResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

class MLInferenceServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.GetInference = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.mlinference.v1.MLInferenceService/GetInference', app.mlinference.v1.ml_inference_pb2.GetInferenceRequest, app.mlinference.v1.ml_inference_pb2.GetInferenceResponse)