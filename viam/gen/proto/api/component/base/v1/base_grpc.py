import abc
import typing
import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server
import google.api.annotations_pb2
from ...... import proto

class BaseServiceBase(abc.ABC):

    @abc.abstractmethod
    async def MoveStraight(self, stream: 'grpclib.server.Stream[proto.api.component.base.v1.base_pb2.MoveStraightRequest, proto.api.component.base.v1.base_pb2.MoveStraightResponse]') -> None:
        pass

    @abc.abstractmethod
    async def MoveArc(self, stream: 'grpclib.server.Stream[proto.api.component.base.v1.base_pb2.MoveArcRequest, proto.api.component.base.v1.base_pb2.MoveArcResponse]') -> None:
        pass

    @abc.abstractmethod
    async def Spin(self, stream: 'grpclib.server.Stream[proto.api.component.base.v1.base_pb2.SpinRequest, proto.api.component.base.v1.base_pb2.SpinResponse]') -> None:
        pass

    @abc.abstractmethod
    async def Stop(self, stream: 'grpclib.server.Stream[proto.api.component.base.v1.base_pb2.StopRequest, proto.api.component.base.v1.base_pb2.StopResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/proto.api.component.base.v1.BaseService/MoveStraight': grpclib.const.Handler(self.MoveStraight, grpclib.const.Cardinality.UNARY_UNARY, proto.api.component.base.v1.base_pb2.MoveStraightRequest, proto.api.component.base.v1.base_pb2.MoveStraightResponse), '/proto.api.component.base.v1.BaseService/MoveArc': grpclib.const.Handler(self.MoveArc, grpclib.const.Cardinality.UNARY_UNARY, proto.api.component.base.v1.base_pb2.MoveArcRequest, proto.api.component.base.v1.base_pb2.MoveArcResponse), '/proto.api.component.base.v1.BaseService/Spin': grpclib.const.Handler(self.Spin, grpclib.const.Cardinality.UNARY_UNARY, proto.api.component.base.v1.base_pb2.SpinRequest, proto.api.component.base.v1.base_pb2.SpinResponse), '/proto.api.component.base.v1.BaseService/Stop': grpclib.const.Handler(self.Stop, grpclib.const.Cardinality.UNARY_UNARY, proto.api.component.base.v1.base_pb2.StopRequest, proto.api.component.base.v1.base_pb2.StopResponse)}

class BaseServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.MoveStraight = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.component.base.v1.BaseService/MoveStraight', proto.api.component.base.v1.base_pb2.MoveStraightRequest, proto.api.component.base.v1.base_pb2.MoveStraightResponse)
        self.MoveArc = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.component.base.v1.BaseService/MoveArc', proto.api.component.base.v1.base_pb2.MoveArcRequest, proto.api.component.base.v1.base_pb2.MoveArcResponse)
        self.Spin = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.component.base.v1.BaseService/Spin', proto.api.component.base.v1.base_pb2.SpinRequest, proto.api.component.base.v1.base_pb2.SpinResponse)
        self.Stop = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.component.base.v1.BaseService/Stop', proto.api.component.base.v1.base_pb2.StopRequest, proto.api.component.base.v1.base_pb2.StopResponse)