import abc
import typing
import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server
import google.api.annotations_pb2
import google.protobuf.struct_pb2
from ...... import proto

class MotorServiceBase(abc.ABC):

    @abc.abstractmethod
    async def SetPower(self, stream: 'grpclib.server.Stream[proto.api.component.motor.v1.motor_pb2.SetPowerRequest, proto.api.component.motor.v1.motor_pb2.SetPowerResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GoFor(self, stream: 'grpclib.server.Stream[proto.api.component.motor.v1.motor_pb2.GoForRequest, proto.api.component.motor.v1.motor_pb2.GoForResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GoTo(self, stream: 'grpclib.server.Stream[proto.api.component.motor.v1.motor_pb2.GoToRequest, proto.api.component.motor.v1.motor_pb2.GoToResponse]') -> None:
        pass

    @abc.abstractmethod
    async def ResetZeroPosition(self, stream: 'grpclib.server.Stream[proto.api.component.motor.v1.motor_pb2.ResetZeroPositionRequest, proto.api.component.motor.v1.motor_pb2.ResetZeroPositionResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetPosition(self, stream: 'grpclib.server.Stream[proto.api.component.motor.v1.motor_pb2.GetPositionRequest, proto.api.component.motor.v1.motor_pb2.GetPositionResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetFeatures(self, stream: 'grpclib.server.Stream[proto.api.component.motor.v1.motor_pb2.GetFeaturesRequest, proto.api.component.motor.v1.motor_pb2.GetFeaturesResponse]') -> None:
        pass

    @abc.abstractmethod
    async def Stop(self, stream: 'grpclib.server.Stream[proto.api.component.motor.v1.motor_pb2.StopRequest, proto.api.component.motor.v1.motor_pb2.StopResponse]') -> None:
        pass

    @abc.abstractmethod
    async def IsPowered(self, stream: 'grpclib.server.Stream[proto.api.component.motor.v1.motor_pb2.IsPoweredRequest, proto.api.component.motor.v1.motor_pb2.IsPoweredResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/proto.api.component.motor.v1.MotorService/SetPower': grpclib.const.Handler(self.SetPower, grpclib.const.Cardinality.UNARY_UNARY, proto.api.component.motor.v1.motor_pb2.SetPowerRequest, proto.api.component.motor.v1.motor_pb2.SetPowerResponse), '/proto.api.component.motor.v1.MotorService/GoFor': grpclib.const.Handler(self.GoFor, grpclib.const.Cardinality.UNARY_UNARY, proto.api.component.motor.v1.motor_pb2.GoForRequest, proto.api.component.motor.v1.motor_pb2.GoForResponse), '/proto.api.component.motor.v1.MotorService/GoTo': grpclib.const.Handler(self.GoTo, grpclib.const.Cardinality.UNARY_UNARY, proto.api.component.motor.v1.motor_pb2.GoToRequest, proto.api.component.motor.v1.motor_pb2.GoToResponse), '/proto.api.component.motor.v1.MotorService/ResetZeroPosition': grpclib.const.Handler(self.ResetZeroPosition, grpclib.const.Cardinality.UNARY_UNARY, proto.api.component.motor.v1.motor_pb2.ResetZeroPositionRequest, proto.api.component.motor.v1.motor_pb2.ResetZeroPositionResponse), '/proto.api.component.motor.v1.MotorService/GetPosition': grpclib.const.Handler(self.GetPosition, grpclib.const.Cardinality.UNARY_UNARY, proto.api.component.motor.v1.motor_pb2.GetPositionRequest, proto.api.component.motor.v1.motor_pb2.GetPositionResponse), '/proto.api.component.motor.v1.MotorService/GetFeatures': grpclib.const.Handler(self.GetFeatures, grpclib.const.Cardinality.UNARY_UNARY, proto.api.component.motor.v1.motor_pb2.GetFeaturesRequest, proto.api.component.motor.v1.motor_pb2.GetFeaturesResponse), '/proto.api.component.motor.v1.MotorService/Stop': grpclib.const.Handler(self.Stop, grpclib.const.Cardinality.UNARY_UNARY, proto.api.component.motor.v1.motor_pb2.StopRequest, proto.api.component.motor.v1.motor_pb2.StopResponse), '/proto.api.component.motor.v1.MotorService/IsPowered': grpclib.const.Handler(self.IsPowered, grpclib.const.Cardinality.UNARY_UNARY, proto.api.component.motor.v1.motor_pb2.IsPoweredRequest, proto.api.component.motor.v1.motor_pb2.IsPoweredResponse)}

class MotorServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.SetPower = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.component.motor.v1.MotorService/SetPower', proto.api.component.motor.v1.motor_pb2.SetPowerRequest, proto.api.component.motor.v1.motor_pb2.SetPowerResponse)
        self.GoFor = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.component.motor.v1.MotorService/GoFor', proto.api.component.motor.v1.motor_pb2.GoForRequest, proto.api.component.motor.v1.motor_pb2.GoForResponse)
        self.GoTo = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.component.motor.v1.MotorService/GoTo', proto.api.component.motor.v1.motor_pb2.GoToRequest, proto.api.component.motor.v1.motor_pb2.GoToResponse)
        self.ResetZeroPosition = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.component.motor.v1.MotorService/ResetZeroPosition', proto.api.component.motor.v1.motor_pb2.ResetZeroPositionRequest, proto.api.component.motor.v1.motor_pb2.ResetZeroPositionResponse)
        self.GetPosition = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.component.motor.v1.MotorService/GetPosition', proto.api.component.motor.v1.motor_pb2.GetPositionRequest, proto.api.component.motor.v1.motor_pb2.GetPositionResponse)
        self.GetFeatures = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.component.motor.v1.MotorService/GetFeatures', proto.api.component.motor.v1.motor_pb2.GetFeaturesRequest, proto.api.component.motor.v1.motor_pb2.GetFeaturesResponse)
        self.Stop = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.component.motor.v1.MotorService/Stop', proto.api.component.motor.v1.motor_pb2.StopRequest, proto.api.component.motor.v1.motor_pb2.StopResponse)
        self.IsPowered = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.component.motor.v1.MotorService/IsPowered', proto.api.component.motor.v1.motor_pb2.IsPoweredRequest, proto.api.component.motor.v1.motor_pb2.IsPoweredResponse)