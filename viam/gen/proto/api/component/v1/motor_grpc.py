import abc
import typing
import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server
import google.protobuf.struct_pb2
import google.api.annotations_pb2
from ..... import proto

class MotorServiceBase(abc.ABC):

    @abc.abstractmethod
    async def SetPower(self, stream: 'grpclib.server.Stream[proto.api.component.v1.motor_pb2.MotorServiceSetPowerRequest, proto.api.component.v1.motor_pb2.MotorServiceSetPowerResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GoFor(self, stream: 'grpclib.server.Stream[proto.api.component.v1.motor_pb2.MotorServiceGoForRequest, proto.api.component.v1.motor_pb2.MotorServiceGoForResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GoTo(self, stream: 'grpclib.server.Stream[proto.api.component.v1.motor_pb2.MotorServiceGoToRequest, proto.api.component.v1.motor_pb2.MotorServiceGoToResponse]') -> None:
        pass

    @abc.abstractmethod
    async def ResetZeroPosition(self, stream: 'grpclib.server.Stream[proto.api.component.v1.motor_pb2.MotorServiceResetZeroPositionRequest, proto.api.component.v1.motor_pb2.MotorServiceResetZeroPositionResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetPosition(self, stream: 'grpclib.server.Stream[proto.api.component.v1.motor_pb2.MotorServiceGetPositionRequest, proto.api.component.v1.motor_pb2.MotorServiceGetPositionResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetFeatures(self, stream: 'grpclib.server.Stream[proto.api.component.v1.motor_pb2.MotorServiceGetFeaturesRequest, proto.api.component.v1.motor_pb2.MotorServiceGetFeaturesResponse]') -> None:
        pass

    @abc.abstractmethod
    async def Stop(self, stream: 'grpclib.server.Stream[proto.api.component.v1.motor_pb2.MotorServiceStopRequest, proto.api.component.v1.motor_pb2.MotorServiceStopResponse]') -> None:
        pass

    @abc.abstractmethod
    async def IsPowered(self, stream: 'grpclib.server.Stream[proto.api.component.v1.motor_pb2.MotorServiceIsPoweredRequest, proto.api.component.v1.motor_pb2.MotorServiceIsPoweredResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/proto.api.component.v1.MotorService/SetPower': grpclib.const.Handler(self.SetPower, grpclib.const.Cardinality.UNARY_UNARY, proto.api.component.v1.motor_pb2.MotorServiceSetPowerRequest, proto.api.component.v1.motor_pb2.MotorServiceSetPowerResponse), '/proto.api.component.v1.MotorService/GoFor': grpclib.const.Handler(self.GoFor, grpclib.const.Cardinality.UNARY_UNARY, proto.api.component.v1.motor_pb2.MotorServiceGoForRequest, proto.api.component.v1.motor_pb2.MotorServiceGoForResponse), '/proto.api.component.v1.MotorService/GoTo': grpclib.const.Handler(self.GoTo, grpclib.const.Cardinality.UNARY_UNARY, proto.api.component.v1.motor_pb2.MotorServiceGoToRequest, proto.api.component.v1.motor_pb2.MotorServiceGoToResponse), '/proto.api.component.v1.MotorService/ResetZeroPosition': grpclib.const.Handler(self.ResetZeroPosition, grpclib.const.Cardinality.UNARY_UNARY, proto.api.component.v1.motor_pb2.MotorServiceResetZeroPositionRequest, proto.api.component.v1.motor_pb2.MotorServiceResetZeroPositionResponse), '/proto.api.component.v1.MotorService/GetPosition': grpclib.const.Handler(self.GetPosition, grpclib.const.Cardinality.UNARY_UNARY, proto.api.component.v1.motor_pb2.MotorServiceGetPositionRequest, proto.api.component.v1.motor_pb2.MotorServiceGetPositionResponse), '/proto.api.component.v1.MotorService/GetFeatures': grpclib.const.Handler(self.GetFeatures, grpclib.const.Cardinality.UNARY_UNARY, proto.api.component.v1.motor_pb2.MotorServiceGetFeaturesRequest, proto.api.component.v1.motor_pb2.MotorServiceGetFeaturesResponse), '/proto.api.component.v1.MotorService/Stop': grpclib.const.Handler(self.Stop, grpclib.const.Cardinality.UNARY_UNARY, proto.api.component.v1.motor_pb2.MotorServiceStopRequest, proto.api.component.v1.motor_pb2.MotorServiceStopResponse), '/proto.api.component.v1.MotorService/IsPowered': grpclib.const.Handler(self.IsPowered, grpclib.const.Cardinality.UNARY_UNARY, proto.api.component.v1.motor_pb2.MotorServiceIsPoweredRequest, proto.api.component.v1.motor_pb2.MotorServiceIsPoweredResponse)}

class MotorServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.SetPower = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.component.v1.MotorService/SetPower', proto.api.component.v1.motor_pb2.MotorServiceSetPowerRequest, proto.api.component.v1.motor_pb2.MotorServiceSetPowerResponse)
        self.GoFor = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.component.v1.MotorService/GoFor', proto.api.component.v1.motor_pb2.MotorServiceGoForRequest, proto.api.component.v1.motor_pb2.MotorServiceGoForResponse)
        self.GoTo = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.component.v1.MotorService/GoTo', proto.api.component.v1.motor_pb2.MotorServiceGoToRequest, proto.api.component.v1.motor_pb2.MotorServiceGoToResponse)
        self.ResetZeroPosition = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.component.v1.MotorService/ResetZeroPosition', proto.api.component.v1.motor_pb2.MotorServiceResetZeroPositionRequest, proto.api.component.v1.motor_pb2.MotorServiceResetZeroPositionResponse)
        self.GetPosition = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.component.v1.MotorService/GetPosition', proto.api.component.v1.motor_pb2.MotorServiceGetPositionRequest, proto.api.component.v1.motor_pb2.MotorServiceGetPositionResponse)
        self.GetFeatures = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.component.v1.MotorService/GetFeatures', proto.api.component.v1.motor_pb2.MotorServiceGetFeaturesRequest, proto.api.component.v1.motor_pb2.MotorServiceGetFeaturesResponse)
        self.Stop = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.component.v1.MotorService/Stop', proto.api.component.v1.motor_pb2.MotorServiceStopRequest, proto.api.component.v1.motor_pb2.MotorServiceStopResponse)
        self.IsPowered = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.component.v1.MotorService/IsPowered', proto.api.component.v1.motor_pb2.MotorServiceIsPoweredRequest, proto.api.component.v1.motor_pb2.MotorServiceIsPoweredResponse)