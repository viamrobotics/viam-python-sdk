import abc
import typing
import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server
import google.api.annotations_pb2
from ..... import proto

class ForceMatrixServiceBase(abc.ABC):

    @abc.abstractmethod
    async def ReadMatrix(self, stream: 'grpclib.server.Stream[proto.api.component.v1.forcematrix_pb2.ForceMatrixServiceReadMatrixRequest, proto.api.component.v1.forcematrix_pb2.ForceMatrixServiceReadMatrixResponse]') -> None:
        pass

    @abc.abstractmethod
    async def DetectSlip(self, stream: 'grpclib.server.Stream[proto.api.component.v1.forcematrix_pb2.ForceMatrixServiceDetectSlipRequest, proto.api.component.v1.forcematrix_pb2.ForceMatrixServiceDetectSlipResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/proto.api.component.v1.ForceMatrixService/ReadMatrix': grpclib.const.Handler(self.ReadMatrix, grpclib.const.Cardinality.UNARY_UNARY, proto.api.component.v1.forcematrix_pb2.ForceMatrixServiceReadMatrixRequest, proto.api.component.v1.forcematrix_pb2.ForceMatrixServiceReadMatrixResponse), '/proto.api.component.v1.ForceMatrixService/DetectSlip': grpclib.const.Handler(self.DetectSlip, grpclib.const.Cardinality.UNARY_UNARY, proto.api.component.v1.forcematrix_pb2.ForceMatrixServiceDetectSlipRequest, proto.api.component.v1.forcematrix_pb2.ForceMatrixServiceDetectSlipResponse)}

class ForceMatrixServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.ReadMatrix = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.component.v1.ForceMatrixService/ReadMatrix', proto.api.component.v1.forcematrix_pb2.ForceMatrixServiceReadMatrixRequest, proto.api.component.v1.forcematrix_pb2.ForceMatrixServiceReadMatrixResponse)
        self.DetectSlip = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.component.v1.ForceMatrixService/DetectSlip', proto.api.component.v1.forcematrix_pb2.ForceMatrixServiceDetectSlipRequest, proto.api.component.v1.forcematrix_pb2.ForceMatrixServiceDetectSlipResponse)