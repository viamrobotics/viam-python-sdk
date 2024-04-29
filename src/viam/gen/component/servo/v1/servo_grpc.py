import abc
import typing
import grpclib.const
import grpclib.client
import grpclib.exceptions
if typing.TYPE_CHECKING:
    import grpclib.server
from .... import common
import google.api.annotations_pb2
import google.protobuf.struct_pb2
from .... import component

class ServoServiceBase(abc.ABC):

    @abc.abstractmethod
    async def Move(self, stream: 'grpclib.server.Stream[component.servo.v1.servo_pb2.MoveRequest, component.servo.v1.servo_pb2.MoveResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetPosition(self, stream: 'grpclib.server.Stream[component.servo.v1.servo_pb2.GetPositionRequest, component.servo.v1.servo_pb2.GetPositionResponse]') -> None:
        pass

    @abc.abstractmethod
    async def Stop(self, stream: 'grpclib.server.Stream[component.servo.v1.servo_pb2.StopRequest, component.servo.v1.servo_pb2.StopResponse]') -> None:
        pass

    @abc.abstractmethod
    async def IsMoving(self, stream: 'grpclib.server.Stream[component.servo.v1.servo_pb2.IsMovingRequest, component.servo.v1.servo_pb2.IsMovingResponse]') -> None:
        pass

    @abc.abstractmethod
    async def DoCommand(self, stream: 'grpclib.server.Stream[common.v1.common_pb2.DoCommandRequest, common.v1.common_pb2.DoCommandResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetGeometries(self, stream: 'grpclib.server.Stream[common.v1.common_pb2.GetGeometriesRequest, common.v1.common_pb2.GetGeometriesResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/viam.component.servo.v1.ServoService/Move': grpclib.const.Handler(self.Move, grpclib.const.Cardinality.UNARY_UNARY, component.servo.v1.servo_pb2.MoveRequest, component.servo.v1.servo_pb2.MoveResponse), '/viam.component.servo.v1.ServoService/GetPosition': grpclib.const.Handler(self.GetPosition, grpclib.const.Cardinality.UNARY_UNARY, component.servo.v1.servo_pb2.GetPositionRequest, component.servo.v1.servo_pb2.GetPositionResponse), '/viam.component.servo.v1.ServoService/Stop': grpclib.const.Handler(self.Stop, grpclib.const.Cardinality.UNARY_UNARY, component.servo.v1.servo_pb2.StopRequest, component.servo.v1.servo_pb2.StopResponse), '/viam.component.servo.v1.ServoService/IsMoving': grpclib.const.Handler(self.IsMoving, grpclib.const.Cardinality.UNARY_UNARY, component.servo.v1.servo_pb2.IsMovingRequest, component.servo.v1.servo_pb2.IsMovingResponse), '/viam.component.servo.v1.ServoService/DoCommand': grpclib.const.Handler(self.DoCommand, grpclib.const.Cardinality.UNARY_UNARY, common.v1.common_pb2.DoCommandRequest, common.v1.common_pb2.DoCommandResponse), '/viam.component.servo.v1.ServoService/GetGeometries': grpclib.const.Handler(self.GetGeometries, grpclib.const.Cardinality.UNARY_UNARY, common.v1.common_pb2.GetGeometriesRequest, common.v1.common_pb2.GetGeometriesResponse)}

class UnimplementedServoServiceBase(ServoServiceBase):

    async def Move(self, stream: 'grpclib.server.Stream[component.servo.v1.servo_pb2.MoveRequest, component.servo.v1.servo_pb2.MoveResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def GetPosition(self, stream: 'grpclib.server.Stream[component.servo.v1.servo_pb2.GetPositionRequest, component.servo.v1.servo_pb2.GetPositionResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def Stop(self, stream: 'grpclib.server.Stream[component.servo.v1.servo_pb2.StopRequest, component.servo.v1.servo_pb2.StopResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def IsMoving(self, stream: 'grpclib.server.Stream[component.servo.v1.servo_pb2.IsMovingRequest, component.servo.v1.servo_pb2.IsMovingResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def DoCommand(self, stream: 'grpclib.server.Stream[common.v1.common_pb2.DoCommandRequest, common.v1.common_pb2.DoCommandResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def GetGeometries(self, stream: 'grpclib.server.Stream[common.v1.common_pb2.GetGeometriesRequest, common.v1.common_pb2.GetGeometriesResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

class ServoServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.Move = grpclib.client.UnaryUnaryMethod(channel, '/viam.component.servo.v1.ServoService/Move', component.servo.v1.servo_pb2.MoveRequest, component.servo.v1.servo_pb2.MoveResponse)
        self.GetPosition = grpclib.client.UnaryUnaryMethod(channel, '/viam.component.servo.v1.ServoService/GetPosition', component.servo.v1.servo_pb2.GetPositionRequest, component.servo.v1.servo_pb2.GetPositionResponse)
        self.Stop = grpclib.client.UnaryUnaryMethod(channel, '/viam.component.servo.v1.ServoService/Stop', component.servo.v1.servo_pb2.StopRequest, component.servo.v1.servo_pb2.StopResponse)
        self.IsMoving = grpclib.client.UnaryUnaryMethod(channel, '/viam.component.servo.v1.ServoService/IsMoving', component.servo.v1.servo_pb2.IsMovingRequest, component.servo.v1.servo_pb2.IsMovingResponse)
        self.DoCommand = grpclib.client.UnaryUnaryMethod(channel, '/viam.component.servo.v1.ServoService/DoCommand', common.v1.common_pb2.DoCommandRequest, common.v1.common_pb2.DoCommandResponse)
        self.GetGeometries = grpclib.client.UnaryUnaryMethod(channel, '/viam.component.servo.v1.ServoService/GetGeometries', common.v1.common_pb2.GetGeometriesRequest, common.v1.common_pb2.GetGeometriesResponse)