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
    async def Spin(self, stream: 'grpclib.server.Stream[proto.api.component.base.v1.base_pb2.SpinRequest, proto.api.component.base.v1.base_pb2.SpinResponse]') -> None:
        pass

    @abc.abstractmethod
    async def SetPower(self, stream: 'grpclib.server.Stream[proto.api.component.base.v1.base_pb2.SetPowerRequest, proto.api.component.base.v1.base_pb2.SetPowerResponse]') -> None:
        pass

    @abc.abstractmethod
    async def SetVelocity(self, stream: 'grpclib.server.Stream[proto.api.component.base.v1.base_pb2.SetVelocityRequest, proto.api.component.base.v1.base_pb2.SetVelocityResponse]') -> None:
        pass

    @abc.abstractmethod
    async def Stop(self, stream: 'grpclib.server.Stream[proto.api.component.base.v1.base_pb2.StopRequest, proto.api.component.base.v1.base_pb2.StopResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/proto.api.component.base.v1.BaseService/MoveStraight': grpclib.const.Handler(self.MoveStraight, grpclib.const.Cardinality.UNARY_UNARY, proto.api.component.base.v1.base_pb2.MoveStraightRequest, proto.api.component.base.v1.base_pb2.MoveStraightResponse), '/proto.api.component.base.v1.BaseService/Spin': grpclib.const.Handler(self.Spin, grpclib.const.Cardinality.UNARY_UNARY, proto.api.component.base.v1.base_pb2.SpinRequest, proto.api.component.base.v1.base_pb2.SpinResponse), '/proto.api.component.base.v1.BaseService/SetPower': grpclib.const.Handler(self.SetPower, grpclib.const.Cardinality.UNARY_UNARY, proto.api.component.base.v1.base_pb2.SetPowerRequest, proto.api.component.base.v1.base_pb2.SetPowerResponse), '/proto.api.component.base.v1.BaseService/SetVelocity': grpclib.const.Handler(self.SetVelocity, grpclib.const.Cardinality.UNARY_UNARY, proto.api.component.base.v1.base_pb2.SetVelocityRequest, proto.api.component.base.v1.base_pb2.SetVelocityResponse), '/proto.api.component.base.v1.BaseService/Stop': grpclib.const.Handler(self.Stop, grpclib.const.Cardinality.UNARY_UNARY, proto.api.component.base.v1.base_pb2.StopRequest, proto.api.component.base.v1.base_pb2.StopResponse)}

class BaseServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.MoveStraight = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.component.base.v1.BaseService/MoveStraight', proto.api.component.base.v1.base_pb2.MoveStraightRequest, proto.api.component.base.v1.base_pb2.MoveStraightResponse)
        self.Spin = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.component.base.v1.BaseService/Spin', proto.api.component.base.v1.base_pb2.SpinRequest, proto.api.component.base.v1.base_pb2.SpinResponse)
        self.SetPower = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.component.base.v1.BaseService/SetPower', proto.api.component.base.v1.base_pb2.SetPowerRequest, proto.api.component.base.v1.base_pb2.SetPowerResponse)
        self.SetVelocity = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.component.base.v1.BaseService/SetVelocity', proto.api.component.base.v1.base_pb2.SetVelocityRequest, proto.api.component.base.v1.base_pb2.SetVelocityResponse)
        self.Stop = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.component.base.v1.BaseService/Stop', proto.api.component.base.v1.base_pb2.StopRequest, proto.api.component.base.v1.base_pb2.StopResponse)