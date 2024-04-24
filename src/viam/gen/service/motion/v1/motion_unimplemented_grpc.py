import abc
import typing
import grpclib.const
import grpclib.exceptions
if typing.TYPE_CHECKING:
    import grpclib.server
from .... import common
import google.api.annotations_pb2
import google.protobuf.struct_pb2
import google.protobuf.timestamp_pb2
from .... import service
from .motion_grpc import MotionServiceBase as _MotionServiceBase

class UnimplementedMotionServiceBase(_MotionServiceBase):

    async def Move(self, stream: 'grpclib.server.Stream[service.motion.v1.motion_pb2.MoveRequest, service.motion.v1.motion_pb2.MoveResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def MoveOnMap(self, stream: 'grpclib.server.Stream[service.motion.v1.motion_pb2.MoveOnMapRequest, service.motion.v1.motion_pb2.MoveOnMapResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def MoveOnGlobe(self, stream: 'grpclib.server.Stream[service.motion.v1.motion_pb2.MoveOnGlobeRequest, service.motion.v1.motion_pb2.MoveOnGlobeResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def GetPose(self, stream: 'grpclib.server.Stream[service.motion.v1.motion_pb2.GetPoseRequest, service.motion.v1.motion_pb2.GetPoseResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def StopPlan(self, stream: 'grpclib.server.Stream[service.motion.v1.motion_pb2.StopPlanRequest, service.motion.v1.motion_pb2.StopPlanResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def ListPlanStatuses(self, stream: 'grpclib.server.Stream[service.motion.v1.motion_pb2.ListPlanStatusesRequest, service.motion.v1.motion_pb2.ListPlanStatusesResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def GetPlan(self, stream: 'grpclib.server.Stream[service.motion.v1.motion_pb2.GetPlanRequest, service.motion.v1.motion_pb2.GetPlanResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def DoCommand(self, stream: 'grpclib.server.Stream[common.v1.common_pb2.DoCommandRequest, common.v1.common_pb2.DoCommandResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)