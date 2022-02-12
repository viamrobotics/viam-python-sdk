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
    async def Go(self, stream: 'grpclib.server.Stream[proto.api.component.v1.motor_pb2.MotorServiceGoRequest, proto.api.component.v1.motor_pb2.MotorServiceGoResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GoFor(self, stream: 'grpclib.server.Stream[proto.api.component.v1.motor_pb2.MotorServiceGoForRequest, proto.api.component.v1.motor_pb2.MotorServiceGoForResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GoTo(self, stream: 'grpclib.server.Stream[proto.api.component.v1.motor_pb2.MotorServiceGoToRequest, proto.api.component.v1.motor_pb2.MotorServiceGoToResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GoTillStop(self, stream: 'grpclib.server.Stream[proto.api.component.v1.motor_pb2.MotorServiceGoTillStopRequest, proto.api.component.v1.motor_pb2.MotorServiceGoTillStopResponse]') -> None:
        pass

    @abc.abstractmethod
    async def ResetZeroPosition(self, stream: 'grpclib.server.Stream[proto.api.component.v1.motor_pb2.MotorServiceResetZeroPositionRequest, proto.api.component.v1.motor_pb2.MotorServiceResetZeroPositionResponse]') -> None:
        pass

    @abc.abstractmethod
    async def Position(self, stream: 'grpclib.server.Stream[proto.api.component.v1.motor_pb2.MotorServicePositionRequest, proto.api.component.v1.motor_pb2.MotorServicePositionResponse]') -> None:
        pass

    @abc.abstractmethod
    async def PositionSupported(self, stream: 'grpclib.server.Stream[proto.api.component.v1.motor_pb2.MotorServicePositionSupportedRequest, proto.api.component.v1.motor_pb2.MotorServicePositionSupportedResponse]') -> None:
        pass

    @abc.abstractmethod
    async def Stop(self, stream: 'grpclib.server.Stream[proto.api.component.v1.motor_pb2.MotorServiceStopRequest, proto.api.component.v1.motor_pb2.MotorServiceStopResponse]') -> None:
        pass

    @abc.abstractmethod
    async def IsOn(self, stream: 'grpclib.server.Stream[proto.api.component.v1.motor_pb2.MotorServiceIsOnRequest, proto.api.component.v1.motor_pb2.MotorServiceIsOnResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/proto.api.component.v1.MotorService/SetPower': grpclib.const.Handler(self.SetPower, grpclib.const.Cardinality.UNARY_UNARY, proto.api.component.v1.motor_pb2.MotorServiceSetPowerRequest, proto.api.component.v1.motor_pb2.MotorServiceSetPowerResponse), '/proto.api.component.v1.MotorService/Go': grpclib.const.Handler(self.Go, grpclib.const.Cardinality.UNARY_UNARY, proto.api.component.v1.motor_pb2.MotorServiceGoRequest, proto.api.component.v1.motor_pb2.MotorServiceGoResponse), '/proto.api.component.v1.MotorService/GoFor': grpclib.const.Handler(self.GoFor, grpclib.const.Cardinality.UNARY_UNARY, proto.api.component.v1.motor_pb2.MotorServiceGoForRequest, proto.api.component.v1.motor_pb2.MotorServiceGoForResponse), '/proto.api.component.v1.MotorService/GoTo': grpclib.const.Handler(self.GoTo, grpclib.const.Cardinality.UNARY_UNARY, proto.api.component.v1.motor_pb2.MotorServiceGoToRequest, proto.api.component.v1.motor_pb2.MotorServiceGoToResponse), '/proto.api.component.v1.MotorService/GoTillStop': grpclib.const.Handler(self.GoTillStop, grpclib.const.Cardinality.UNARY_UNARY, proto.api.component.v1.motor_pb2.MotorServiceGoTillStopRequest, proto.api.component.v1.motor_pb2.MotorServiceGoTillStopResponse), '/proto.api.component.v1.MotorService/ResetZeroPosition': grpclib.const.Handler(self.ResetZeroPosition, grpclib.const.Cardinality.UNARY_UNARY, proto.api.component.v1.motor_pb2.MotorServiceResetZeroPositionRequest, proto.api.component.v1.motor_pb2.MotorServiceResetZeroPositionResponse), '/proto.api.component.v1.MotorService/Position': grpclib.const.Handler(self.Position, grpclib.const.Cardinality.UNARY_UNARY, proto.api.component.v1.motor_pb2.MotorServicePositionRequest, proto.api.component.v1.motor_pb2.MotorServicePositionResponse), '/proto.api.component.v1.MotorService/PositionSupported': grpclib.const.Handler(self.PositionSupported, grpclib.const.Cardinality.UNARY_UNARY, proto.api.component.v1.motor_pb2.MotorServicePositionSupportedRequest, proto.api.component.v1.motor_pb2.MotorServicePositionSupportedResponse), '/proto.api.component.v1.MotorService/Stop': grpclib.const.Handler(self.Stop, grpclib.const.Cardinality.UNARY_UNARY, proto.api.component.v1.motor_pb2.MotorServiceStopRequest, proto.api.component.v1.motor_pb2.MotorServiceStopResponse), '/proto.api.component.v1.MotorService/IsOn': grpclib.const.Handler(self.IsOn, grpclib.const.Cardinality.UNARY_UNARY, proto.api.component.v1.motor_pb2.MotorServiceIsOnRequest, proto.api.component.v1.motor_pb2.MotorServiceIsOnResponse)}

class MotorServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.SetPower = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.component.v1.MotorService/SetPower', proto.api.component.v1.motor_pb2.MotorServiceSetPowerRequest, proto.api.component.v1.motor_pb2.MotorServiceSetPowerResponse)
        self.Go = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.component.v1.MotorService/Go', proto.api.component.v1.motor_pb2.MotorServiceGoRequest, proto.api.component.v1.motor_pb2.MotorServiceGoResponse)
        self.GoFor = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.component.v1.MotorService/GoFor', proto.api.component.v1.motor_pb2.MotorServiceGoForRequest, proto.api.component.v1.motor_pb2.MotorServiceGoForResponse)
        self.GoTo = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.component.v1.MotorService/GoTo', proto.api.component.v1.motor_pb2.MotorServiceGoToRequest, proto.api.component.v1.motor_pb2.MotorServiceGoToResponse)
        self.GoTillStop = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.component.v1.MotorService/GoTillStop', proto.api.component.v1.motor_pb2.MotorServiceGoTillStopRequest, proto.api.component.v1.motor_pb2.MotorServiceGoTillStopResponse)
        self.ResetZeroPosition = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.component.v1.MotorService/ResetZeroPosition', proto.api.component.v1.motor_pb2.MotorServiceResetZeroPositionRequest, proto.api.component.v1.motor_pb2.MotorServiceResetZeroPositionResponse)
        self.Position = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.component.v1.MotorService/Position', proto.api.component.v1.motor_pb2.MotorServicePositionRequest, proto.api.component.v1.motor_pb2.MotorServicePositionResponse)
        self.PositionSupported = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.component.v1.MotorService/PositionSupported', proto.api.component.v1.motor_pb2.MotorServicePositionSupportedRequest, proto.api.component.v1.motor_pb2.MotorServicePositionSupportedResponse)
        self.Stop = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.component.v1.MotorService/Stop', proto.api.component.v1.motor_pb2.MotorServiceStopRequest, proto.api.component.v1.motor_pb2.MotorServiceStopResponse)
        self.IsOn = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.component.v1.MotorService/IsOn', proto.api.component.v1.motor_pb2.MotorServiceIsOnRequest, proto.api.component.v1.motor_pb2.MotorServiceIsOnResponse)