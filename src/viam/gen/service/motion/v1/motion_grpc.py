import abc
import typing
import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server
from .... import common
import google.api.annotations_pb2
import google.protobuf.struct_pb2
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
    async def DoCommand(self, stream: 'grpclib.server.Stream[common.v1.common_pb2.DoCommandRequest, common.v1.common_pb2.DoCommandResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/viam.service.motion.v1.MotionService/Move': grpclib.const.Handler(self.Move, grpclib.const.Cardinality.UNARY_UNARY, service.motion.v1.motion_pb2.MoveRequest, service.motion.v1.motion_pb2.MoveResponse), '/viam.service.motion.v1.MotionService/MoveOnMap': grpclib.const.Handler(self.MoveOnMap, grpclib.const.Cardinality.UNARY_UNARY, service.motion.v1.motion_pb2.MoveOnMapRequest, service.motion.v1.motion_pb2.MoveOnMapResponse), '/viam.service.motion.v1.MotionService/MoveOnGlobe': grpclib.const.Handler(self.MoveOnGlobe, grpclib.const.Cardinality.UNARY_UNARY, service.motion.v1.motion_pb2.MoveOnGlobeRequest, service.motion.v1.motion_pb2.MoveOnGlobeResponse), '/viam.service.motion.v1.MotionService/GetPose': grpclib.const.Handler(self.GetPose, grpclib.const.Cardinality.UNARY_UNARY, service.motion.v1.motion_pb2.GetPoseRequest, service.motion.v1.motion_pb2.GetPoseResponse), '/viam.service.motion.v1.MotionService/DoCommand': grpclib.const.Handler(self.DoCommand, grpclib.const.Cardinality.UNARY_UNARY, common.v1.common_pb2.DoCommandRequest, common.v1.common_pb2.DoCommandResponse)}

class MotionServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.Move = grpclib.client.UnaryUnaryMethod(channel, '/viam.service.motion.v1.MotionService/Move', service.motion.v1.motion_pb2.MoveRequest, service.motion.v1.motion_pb2.MoveResponse)
        self.MoveOnMap = grpclib.client.UnaryUnaryMethod(channel, '/viam.service.motion.v1.MotionService/MoveOnMap', service.motion.v1.motion_pb2.MoveOnMapRequest, service.motion.v1.motion_pb2.MoveOnMapResponse)
        self.MoveOnGlobe = grpclib.client.UnaryUnaryMethod(channel, '/viam.service.motion.v1.MotionService/MoveOnGlobe', service.motion.v1.motion_pb2.MoveOnGlobeRequest, service.motion.v1.motion_pb2.MoveOnGlobeResponse)
        self.GetPose = grpclib.client.UnaryUnaryMethod(channel, '/viam.service.motion.v1.MotionService/GetPose', service.motion.v1.motion_pb2.GetPoseRequest, service.motion.v1.motion_pb2.GetPoseResponse)
        self.DoCommand = grpclib.client.UnaryUnaryMethod(channel, '/viam.service.motion.v1.MotionService/DoCommand', common.v1.common_pb2.DoCommandRequest, common.v1.common_pb2.DoCommandResponse)