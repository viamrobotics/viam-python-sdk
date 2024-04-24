import abc
import typing
import grpclib.const
import grpclib.exceptions
if typing.TYPE_CHECKING:
    import grpclib.server
from .... import common
import google.api.annotations_pb2
import google.protobuf.struct_pb2
from .... import service
from .slam_grpc import SLAMServiceBase as _SLAMServiceBase

class UnimplementedSLAMServiceBase(_SLAMServiceBase):

    async def GetPosition(self, stream: 'grpclib.server.Stream[service.slam.v1.slam_pb2.GetPositionRequest, service.slam.v1.slam_pb2.GetPositionResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def GetPointCloudMap(self, stream: 'grpclib.server.Stream[service.slam.v1.slam_pb2.GetPointCloudMapRequest, service.slam.v1.slam_pb2.GetPointCloudMapResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def GetInternalState(self, stream: 'grpclib.server.Stream[service.slam.v1.slam_pb2.GetInternalStateRequest, service.slam.v1.slam_pb2.GetInternalStateResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def GetProperties(self, stream: 'grpclib.server.Stream[service.slam.v1.slam_pb2.GetPropertiesRequest, service.slam.v1.slam_pb2.GetPropertiesResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def DoCommand(self, stream: 'grpclib.server.Stream[common.v1.common_pb2.DoCommandRequest, common.v1.common_pb2.DoCommandResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)