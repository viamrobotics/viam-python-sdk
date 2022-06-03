import abc
import typing
import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server
import google.api.annotations_pb2
from ...... import proto

class ServoServiceBase(abc.ABC):

    @abc.abstractmethod
    async def Move(self, stream: 'grpclib.server.Stream[proto.api.component.servo.v1.servo_pb2.MoveRequest, proto.api.component.servo.v1.servo_pb2.MoveResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetPosition(self, stream: 'grpclib.server.Stream[proto.api.component.servo.v1.servo_pb2.GetPositionRequest, proto.api.component.servo.v1.servo_pb2.GetPositionResponse]') -> None:
        pass

    @abc.abstractmethod
    async def Stop(self, stream: 'grpclib.server.Stream[proto.api.component.servo.v1.servo_pb2.StopRequest, proto.api.component.servo.v1.servo_pb2.StopResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/proto.api.component.servo.v1.ServoService/Move': grpclib.const.Handler(self.Move, grpclib.const.Cardinality.UNARY_UNARY, proto.api.component.servo.v1.servo_pb2.MoveRequest, proto.api.component.servo.v1.servo_pb2.MoveResponse), '/proto.api.component.servo.v1.ServoService/GetPosition': grpclib.const.Handler(self.GetPosition, grpclib.const.Cardinality.UNARY_UNARY, proto.api.component.servo.v1.servo_pb2.GetPositionRequest, proto.api.component.servo.v1.servo_pb2.GetPositionResponse), '/proto.api.component.servo.v1.ServoService/Stop': grpclib.const.Handler(self.Stop, grpclib.const.Cardinality.UNARY_UNARY, proto.api.component.servo.v1.servo_pb2.StopRequest, proto.api.component.servo.v1.servo_pb2.StopResponse)}

class ServoServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.Move = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.component.servo.v1.ServoService/Move', proto.api.component.servo.v1.servo_pb2.MoveRequest, proto.api.component.servo.v1.servo_pb2.MoveResponse)
        self.GetPosition = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.component.servo.v1.ServoService/GetPosition', proto.api.component.servo.v1.servo_pb2.GetPositionRequest, proto.api.component.servo.v1.servo_pb2.GetPositionResponse)
        self.Stop = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.component.servo.v1.ServoService/Stop', proto.api.component.servo.v1.servo_pb2.StopRequest, proto.api.component.servo.v1.servo_pb2.StopResponse)