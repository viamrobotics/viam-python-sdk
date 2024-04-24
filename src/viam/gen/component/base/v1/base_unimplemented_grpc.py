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
from .base_grpc import BaseServiceBase as _BaseServiceBase

class UnimplementedBaseServiceBase(_BaseServiceBase):

    async def MoveStraight(self, stream: 'grpclib.server.Stream[component.base.v1.base_pb2.MoveStraightRequest, component.base.v1.base_pb2.MoveStraightResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def Spin(self, stream: 'grpclib.server.Stream[component.base.v1.base_pb2.SpinRequest, component.base.v1.base_pb2.SpinResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def SetPower(self, stream: 'grpclib.server.Stream[component.base.v1.base_pb2.SetPowerRequest, component.base.v1.base_pb2.SetPowerResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def SetVelocity(self, stream: 'grpclib.server.Stream[component.base.v1.base_pb2.SetVelocityRequest, component.base.v1.base_pb2.SetVelocityResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def Stop(self, stream: 'grpclib.server.Stream[component.base.v1.base_pb2.StopRequest, component.base.v1.base_pb2.StopResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def IsMoving(self, stream: 'grpclib.server.Stream[component.base.v1.base_pb2.IsMovingRequest, component.base.v1.base_pb2.IsMovingResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def DoCommand(self, stream: 'grpclib.server.Stream[common.v1.common_pb2.DoCommandRequest, common.v1.common_pb2.DoCommandResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def GetGeometries(self, stream: 'grpclib.server.Stream[common.v1.common_pb2.GetGeometriesRequest, common.v1.common_pb2.GetGeometriesResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def GetProperties(self, stream: 'grpclib.server.Stream[component.base.v1.base_pb2.GetPropertiesRequest, component.base.v1.base_pb2.GetPropertiesResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)