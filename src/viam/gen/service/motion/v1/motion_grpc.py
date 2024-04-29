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
import google.protobuf.timestamp_pb2
from .... import service

class MotionServiceBase(abc.ABC):

    @abc.abstractmethod
    async def Move(self, stream: 'grpclib.server.Stream[service.motion.v1.motion_pb2.MoveRequest, service.motion.v1.motion_pb2.MoveResponse]') -> None:
        pass

    @abc.abstractmethod
    async def MoveOnMap(self, stream: 'grpclib.server.Stream[service.motion.v1.motion_pb2.MoveOnMapRequest, service.motion.v1.motion_pb2.MoveOnMapResponse]') -> None:
        pass

    @abc.abstractmethod
    async def MoveOnGlobe(self, stream: 'grpclib.server.Stream[service.motion.v1.motion_pb2.MoveOnGlobeRequest, service.motion.v1.motion_pb2.MoveOnGlobeResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetPose(self, stream: 'grpclib.server.Stream[service.motion.v1.motion_pb2.GetPoseRequest, service.motion.v1.motion_pb2.GetPoseResponse]') -> None:
        pass

    @abc.abstractmethod
    async def StopPlan(self, stream: 'grpclib.server.Stream[service.motion.v1.motion_pb2.StopPlanRequest, service.motion.v1.motion_pb2.StopPlanResponse]') -> None:
        pass

    @abc.abstractmethod
    async def ListPlanStatuses(self, stream: 'grpclib.server.Stream[service.motion.v1.motion_pb2.ListPlanStatusesRequest, service.motion.v1.motion_pb2.ListPlanStatusesResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetPlan(self, stream: 'grpclib.server.Stream[service.motion.v1.motion_pb2.GetPlanRequest, service.motion.v1.motion_pb2.GetPlanResponse]') -> None:
        pass

    @abc.abstractmethod
    async def DoCommand(self, stream: 'grpclib.server.Stream[common.v1.common_pb2.DoCommandRequest, common.v1.common_pb2.DoCommandResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/viam.service.motion.v1.MotionService/Move': grpclib.const.Handler(self.Move, grpclib.const.Cardinality.UNARY_UNARY, service.motion.v1.motion_pb2.MoveRequest, service.motion.v1.motion_pb2.MoveResponse), '/viam.service.motion.v1.MotionService/MoveOnMap': grpclib.const.Handler(self.MoveOnMap, grpclib.const.Cardinality.UNARY_UNARY, service.motion.v1.motion_pb2.MoveOnMapRequest, service.motion.v1.motion_pb2.MoveOnMapResponse), '/viam.service.motion.v1.MotionService/MoveOnGlobe': grpclib.const.Handler(self.MoveOnGlobe, grpclib.const.Cardinality.UNARY_UNARY, service.motion.v1.motion_pb2.MoveOnGlobeRequest, service.motion.v1.motion_pb2.MoveOnGlobeResponse), '/viam.service.motion.v1.MotionService/GetPose': grpclib.const.Handler(self.GetPose, grpclib.const.Cardinality.UNARY_UNARY, service.motion.v1.motion_pb2.GetPoseRequest, service.motion.v1.motion_pb2.GetPoseResponse), '/viam.service.motion.v1.MotionService/StopPlan': grpclib.const.Handler(self.StopPlan, grpclib.const.Cardinality.UNARY_UNARY, service.motion.v1.motion_pb2.StopPlanRequest, service.motion.v1.motion_pb2.StopPlanResponse), '/viam.service.motion.v1.MotionService/ListPlanStatuses': grpclib.const.Handler(self.ListPlanStatuses, grpclib.const.Cardinality.UNARY_UNARY, service.motion.v1.motion_pb2.ListPlanStatusesRequest, service.motion.v1.motion_pb2.ListPlanStatusesResponse), '/viam.service.motion.v1.MotionService/GetPlan': grpclib.const.Handler(self.GetPlan, grpclib.const.Cardinality.UNARY_UNARY, service.motion.v1.motion_pb2.GetPlanRequest, service.motion.v1.motion_pb2.GetPlanResponse), '/viam.service.motion.v1.MotionService/DoCommand': grpclib.const.Handler(self.DoCommand, grpclib.const.Cardinality.UNARY_UNARY, common.v1.common_pb2.DoCommandRequest, common.v1.common_pb2.DoCommandResponse)}

class UnimplementedMotionServiceBase(MotionServiceBase):

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

class MotionServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.Move = grpclib.client.UnaryUnaryMethod(channel, '/viam.service.motion.v1.MotionService/Move', service.motion.v1.motion_pb2.MoveRequest, service.motion.v1.motion_pb2.MoveResponse)
        self.MoveOnMap = grpclib.client.UnaryUnaryMethod(channel, '/viam.service.motion.v1.MotionService/MoveOnMap', service.motion.v1.motion_pb2.MoveOnMapRequest, service.motion.v1.motion_pb2.MoveOnMapResponse)
        self.MoveOnGlobe = grpclib.client.UnaryUnaryMethod(channel, '/viam.service.motion.v1.MotionService/MoveOnGlobe', service.motion.v1.motion_pb2.MoveOnGlobeRequest, service.motion.v1.motion_pb2.MoveOnGlobeResponse)
        self.GetPose = grpclib.client.UnaryUnaryMethod(channel, '/viam.service.motion.v1.MotionService/GetPose', service.motion.v1.motion_pb2.GetPoseRequest, service.motion.v1.motion_pb2.GetPoseResponse)
        self.StopPlan = grpclib.client.UnaryUnaryMethod(channel, '/viam.service.motion.v1.MotionService/StopPlan', service.motion.v1.motion_pb2.StopPlanRequest, service.motion.v1.motion_pb2.StopPlanResponse)
        self.ListPlanStatuses = grpclib.client.UnaryUnaryMethod(channel, '/viam.service.motion.v1.MotionService/ListPlanStatuses', service.motion.v1.motion_pb2.ListPlanStatusesRequest, service.motion.v1.motion_pb2.ListPlanStatusesResponse)
        self.GetPlan = grpclib.client.UnaryUnaryMethod(channel, '/viam.service.motion.v1.MotionService/GetPlan', service.motion.v1.motion_pb2.GetPlanRequest, service.motion.v1.motion_pb2.GetPlanResponse)
        self.DoCommand = grpclib.client.UnaryUnaryMethod(channel, '/viam.service.motion.v1.MotionService/DoCommand', common.v1.common_pb2.DoCommandRequest, common.v1.common_pb2.DoCommandResponse)