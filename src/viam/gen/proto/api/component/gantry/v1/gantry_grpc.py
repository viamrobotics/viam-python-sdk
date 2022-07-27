import abc
import typing
import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server
import google.api.annotations_pb2
import google.protobuf.struct_pb2
from ...... import proto

class GantryServiceBase(abc.ABC):

    @abc.abstractmethod
    async def GetPosition(self, stream: 'grpclib.server.Stream[proto.api.component.gantry.v1.gantry_pb2.GetPositionRequest, proto.api.component.gantry.v1.gantry_pb2.GetPositionResponse]') -> None:
        pass

    @abc.abstractmethod
    async def MoveToPosition(self, stream: 'grpclib.server.Stream[proto.api.component.gantry.v1.gantry_pb2.MoveToPositionRequest, proto.api.component.gantry.v1.gantry_pb2.MoveToPositionResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetLengths(self, stream: 'grpclib.server.Stream[proto.api.component.gantry.v1.gantry_pb2.GetLengthsRequest, proto.api.component.gantry.v1.gantry_pb2.GetLengthsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def Stop(self, stream: 'grpclib.server.Stream[proto.api.component.gantry.v1.gantry_pb2.StopRequest, proto.api.component.gantry.v1.gantry_pb2.StopResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/proto.api.component.gantry.v1.GantryService/GetPosition': grpclib.const.Handler(self.GetPosition, grpclib.const.Cardinality.UNARY_UNARY, proto.api.component.gantry.v1.gantry_pb2.GetPositionRequest, proto.api.component.gantry.v1.gantry_pb2.GetPositionResponse), '/proto.api.component.gantry.v1.GantryService/MoveToPosition': grpclib.const.Handler(self.MoveToPosition, grpclib.const.Cardinality.UNARY_UNARY, proto.api.component.gantry.v1.gantry_pb2.MoveToPositionRequest, proto.api.component.gantry.v1.gantry_pb2.MoveToPositionResponse), '/proto.api.component.gantry.v1.GantryService/GetLengths': grpclib.const.Handler(self.GetLengths, grpclib.const.Cardinality.UNARY_UNARY, proto.api.component.gantry.v1.gantry_pb2.GetLengthsRequest, proto.api.component.gantry.v1.gantry_pb2.GetLengthsResponse), '/proto.api.component.gantry.v1.GantryService/Stop': grpclib.const.Handler(self.Stop, grpclib.const.Cardinality.UNARY_UNARY, proto.api.component.gantry.v1.gantry_pb2.StopRequest, proto.api.component.gantry.v1.gantry_pb2.StopResponse)}

class GantryServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.GetPosition = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.component.gantry.v1.GantryService/GetPosition', proto.api.component.gantry.v1.gantry_pb2.GetPositionRequest, proto.api.component.gantry.v1.gantry_pb2.GetPositionResponse)
        self.MoveToPosition = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.component.gantry.v1.GantryService/MoveToPosition', proto.api.component.gantry.v1.gantry_pb2.MoveToPositionRequest, proto.api.component.gantry.v1.gantry_pb2.MoveToPositionResponse)
        self.GetLengths = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.component.gantry.v1.GantryService/GetLengths', proto.api.component.gantry.v1.gantry_pb2.GetLengthsRequest, proto.api.component.gantry.v1.gantry_pb2.GetLengthsResponse)
        self.Stop = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.component.gantry.v1.GantryService/Stop', proto.api.component.gantry.v1.gantry_pb2.StopRequest, proto.api.component.gantry.v1.gantry_pb2.StopResponse)