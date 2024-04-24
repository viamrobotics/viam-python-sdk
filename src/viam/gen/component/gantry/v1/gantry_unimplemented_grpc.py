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
from .gantry_grpc import GantryServiceBase as _GantryServiceBase

class UnimplementedGantryServiceBase(_GantryServiceBase):

    async def GetPosition(self, stream: 'grpclib.server.Stream[component.gantry.v1.gantry_pb2.GetPositionRequest, component.gantry.v1.gantry_pb2.GetPositionResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def MoveToPosition(self, stream: 'grpclib.server.Stream[component.gantry.v1.gantry_pb2.MoveToPositionRequest, component.gantry.v1.gantry_pb2.MoveToPositionResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def Home(self, stream: 'grpclib.server.Stream[component.gantry.v1.gantry_pb2.HomeRequest, component.gantry.v1.gantry_pb2.HomeResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def GetLengths(self, stream: 'grpclib.server.Stream[component.gantry.v1.gantry_pb2.GetLengthsRequest, component.gantry.v1.gantry_pb2.GetLengthsResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def Stop(self, stream: 'grpclib.server.Stream[component.gantry.v1.gantry_pb2.StopRequest, component.gantry.v1.gantry_pb2.StopResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def IsMoving(self, stream: 'grpclib.server.Stream[component.gantry.v1.gantry_pb2.IsMovingRequest, component.gantry.v1.gantry_pb2.IsMovingResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def DoCommand(self, stream: 'grpclib.server.Stream[common.v1.common_pb2.DoCommandRequest, common.v1.common_pb2.DoCommandResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def GetGeometries(self, stream: 'grpclib.server.Stream[common.v1.common_pb2.GetGeometriesRequest, common.v1.common_pb2.GetGeometriesResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)