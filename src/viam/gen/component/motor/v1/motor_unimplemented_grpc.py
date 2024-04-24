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
from .motor_grpc import MotorServiceBase as _MotorServiceBase

class UnimplementedMotorServiceBase(_MotorServiceBase):

    async def SetPower(self, stream: 'grpclib.server.Stream[component.motor.v1.motor_pb2.SetPowerRequest, component.motor.v1.motor_pb2.SetPowerResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def GoFor(self, stream: 'grpclib.server.Stream[component.motor.v1.motor_pb2.GoForRequest, component.motor.v1.motor_pb2.GoForResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def GoTo(self, stream: 'grpclib.server.Stream[component.motor.v1.motor_pb2.GoToRequest, component.motor.v1.motor_pb2.GoToResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def ResetZeroPosition(self, stream: 'grpclib.server.Stream[component.motor.v1.motor_pb2.ResetZeroPositionRequest, component.motor.v1.motor_pb2.ResetZeroPositionResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def GetPosition(self, stream: 'grpclib.server.Stream[component.motor.v1.motor_pb2.GetPositionRequest, component.motor.v1.motor_pb2.GetPositionResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def GetProperties(self, stream: 'grpclib.server.Stream[component.motor.v1.motor_pb2.GetPropertiesRequest, component.motor.v1.motor_pb2.GetPropertiesResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def Stop(self, stream: 'grpclib.server.Stream[component.motor.v1.motor_pb2.StopRequest, component.motor.v1.motor_pb2.StopResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def IsPowered(self, stream: 'grpclib.server.Stream[component.motor.v1.motor_pb2.IsPoweredRequest, component.motor.v1.motor_pb2.IsPoweredResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def IsMoving(self, stream: 'grpclib.server.Stream[component.motor.v1.motor_pb2.IsMovingRequest, component.motor.v1.motor_pb2.IsMovingResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def DoCommand(self, stream: 'grpclib.server.Stream[common.v1.common_pb2.DoCommandRequest, common.v1.common_pb2.DoCommandResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def GetGeometries(self, stream: 'grpclib.server.Stream[common.v1.common_pb2.GetGeometriesRequest, common.v1.common_pb2.GetGeometriesResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)