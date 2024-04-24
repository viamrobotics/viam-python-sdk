import abc
import typing
import grpclib.const
import grpclib.exceptions
if typing.TYPE_CHECKING:
    import grpclib.server
from .... import common
import google.api.annotations_pb2
import google.protobuf.struct_pb2
from .... import component
from .servo_grpc import ServoServiceBase as _ServoServiceBase

class UnimplementedServoServiceBase(_ServoServiceBase):

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