import abc
import typing
import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server
import google.api.annotations_pb2
from ...... import proto

class MotionServiceBase(abc.ABC):

    @abc.abstractmethod
    async def PlanAndMove(self, stream: 'grpclib.server.Stream[proto.api.service.motion.v1.motion_pb2.PlanAndMoveRequest, proto.api.service.motion.v1.motion_pb2.PlanAndMoveResponse]') -> None:
        pass

    @abc.abstractmethod
    async def MoveSingleComponent(self, stream: 'grpclib.server.Stream[proto.api.service.motion.v1.motion_pb2.MoveSingleComponentRequest, proto.api.service.motion.v1.motion_pb2.MoveSingleComponentResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetPose(self, stream: 'grpclib.server.Stream[proto.api.service.motion.v1.motion_pb2.GetPoseRequest, proto.api.service.motion.v1.motion_pb2.GetPoseResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/proto.api.service.motion.v1.MotionService/PlanAndMove': grpclib.const.Handler(self.PlanAndMove, grpclib.const.Cardinality.UNARY_UNARY, proto.api.service.motion.v1.motion_pb2.PlanAndMoveRequest, proto.api.service.motion.v1.motion_pb2.PlanAndMoveResponse), '/proto.api.service.motion.v1.MotionService/MoveSingleComponent': grpclib.const.Handler(self.MoveSingleComponent, grpclib.const.Cardinality.UNARY_UNARY, proto.api.service.motion.v1.motion_pb2.MoveSingleComponentRequest, proto.api.service.motion.v1.motion_pb2.MoveSingleComponentResponse), '/proto.api.service.motion.v1.MotionService/GetPose': grpclib.const.Handler(self.GetPose, grpclib.const.Cardinality.UNARY_UNARY, proto.api.service.motion.v1.motion_pb2.GetPoseRequest, proto.api.service.motion.v1.motion_pb2.GetPoseResponse)}

class MotionServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.PlanAndMove = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.service.motion.v1.MotionService/PlanAndMove', proto.api.service.motion.v1.motion_pb2.PlanAndMoveRequest, proto.api.service.motion.v1.motion_pb2.PlanAndMoveResponse)
        self.MoveSingleComponent = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.service.motion.v1.MotionService/MoveSingleComponent', proto.api.service.motion.v1.motion_pb2.MoveSingleComponentRequest, proto.api.service.motion.v1.motion_pb2.MoveSingleComponentResponse)
        self.GetPose = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.service.motion.v1.MotionService/GetPose', proto.api.service.motion.v1.motion_pb2.GetPoseRequest, proto.api.service.motion.v1.motion_pb2.GetPoseResponse)