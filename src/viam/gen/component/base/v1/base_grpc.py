import abc
import typing
import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server
from .... import common
import google.api.annotations_pb2
import google.protobuf.struct_pb2
from .... import component

class BaseServiceBase(abc.ABC):

    @abc.abstractmethod
    async def MoveStraight(self, stream: 'grpclib.server.Stream[component.base.v1.base_pb2.MoveStraightRequest, component.base.v1.base_pb2.MoveStraightResponse]') -> None:
        pass

    @abc.abstractmethod
    async def Spin(self, stream: 'grpclib.server.Stream[component.base.v1.base_pb2.SpinRequest, component.base.v1.base_pb2.SpinResponse]') -> None:
        pass

    @abc.abstractmethod
    async def SetPower(self, stream: 'grpclib.server.Stream[component.base.v1.base_pb2.SetPowerRequest, component.base.v1.base_pb2.SetPowerResponse]') -> None:
        pass

    @abc.abstractmethod
    async def SetVelocity(self, stream: 'grpclib.server.Stream[component.base.v1.base_pb2.SetVelocityRequest, component.base.v1.base_pb2.SetVelocityResponse]') -> None:
        pass

    @abc.abstractmethod
    async def Stop(self, stream: 'grpclib.server.Stream[component.base.v1.base_pb2.StopRequest, component.base.v1.base_pb2.StopResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/viam.component.base.v1.BaseService/MoveStraight': grpclib.const.Handler(self.MoveStraight, grpclib.const.Cardinality.UNARY_UNARY, component.base.v1.base_pb2.MoveStraightRequest, component.base.v1.base_pb2.MoveStraightResponse), '/viam.component.base.v1.BaseService/Spin': grpclib.const.Handler(self.Spin, grpclib.const.Cardinality.UNARY_UNARY, component.base.v1.base_pb2.SpinRequest, component.base.v1.base_pb2.SpinResponse), '/viam.component.base.v1.BaseService/SetPower': grpclib.const.Handler(self.SetPower, grpclib.const.Cardinality.UNARY_UNARY, component.base.v1.base_pb2.SetPowerRequest, component.base.v1.base_pb2.SetPowerResponse), '/viam.component.base.v1.BaseService/SetVelocity': grpclib.const.Handler(self.SetVelocity, grpclib.const.Cardinality.UNARY_UNARY, component.base.v1.base_pb2.SetVelocityRequest, component.base.v1.base_pb2.SetVelocityResponse), '/viam.component.base.v1.BaseService/Stop': grpclib.const.Handler(self.Stop, grpclib.const.Cardinality.UNARY_UNARY, component.base.v1.base_pb2.StopRequest, component.base.v1.base_pb2.StopResponse)}

class BaseServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.MoveStraight = grpclib.client.UnaryUnaryMethod(channel, '/viam.component.base.v1.BaseService/MoveStraight', component.base.v1.base_pb2.MoveStraightRequest, component.base.v1.base_pb2.MoveStraightResponse)
        self.Spin = grpclib.client.UnaryUnaryMethod(channel, '/viam.component.base.v1.BaseService/Spin', component.base.v1.base_pb2.SpinRequest, component.base.v1.base_pb2.SpinResponse)
        self.SetPower = grpclib.client.UnaryUnaryMethod(channel, '/viam.component.base.v1.BaseService/SetPower', component.base.v1.base_pb2.SetPowerRequest, component.base.v1.base_pb2.SetPowerResponse)
        self.SetVelocity = grpclib.client.UnaryUnaryMethod(channel, '/viam.component.base.v1.BaseService/SetVelocity', component.base.v1.base_pb2.SetVelocityRequest, component.base.v1.base_pb2.SetVelocityResponse)
        self.Stop = grpclib.client.UnaryUnaryMethod(channel, '/viam.component.base.v1.BaseService/Stop', component.base.v1.base_pb2.StopRequest, component.base.v1.base_pb2.StopResponse)