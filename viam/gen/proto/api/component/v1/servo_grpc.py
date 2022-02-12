import abc
import typing
import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server
import google.api.annotations_pb2
from ..... import proto

class ServoServiceBase(abc.ABC):

    @abc.abstractmethod
    async def Move(self, stream: 'grpclib.server.Stream[proto.api.component.v1.servo_pb2.ServoServiceMoveRequest, proto.api.component.v1.servo_pb2.ServoServiceMoveResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetPosition(self, stream: 'grpclib.server.Stream[proto.api.component.v1.servo_pb2.ServoServiceGetPositionRequest, proto.api.component.v1.servo_pb2.ServoServiceGetPositionResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/proto.api.component.v1.ServoService/Move': grpclib.const.Handler(self.Move, grpclib.const.Cardinality.UNARY_UNARY, proto.api.component.v1.servo_pb2.ServoServiceMoveRequest, proto.api.component.v1.servo_pb2.ServoServiceMoveResponse), '/proto.api.component.v1.ServoService/GetPosition': grpclib.const.Handler(self.GetPosition, grpclib.const.Cardinality.UNARY_UNARY, proto.api.component.v1.servo_pb2.ServoServiceGetPositionRequest, proto.api.component.v1.servo_pb2.ServoServiceGetPositionResponse)}

class ServoServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.Move = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.component.v1.ServoService/Move', proto.api.component.v1.servo_pb2.ServoServiceMoveRequest, proto.api.component.v1.servo_pb2.ServoServiceMoveResponse)
        self.GetPosition = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.component.v1.ServoService/GetPosition', proto.api.component.v1.servo_pb2.ServoServiceGetPositionRequest, proto.api.component.v1.servo_pb2.ServoServiceGetPositionResponse)