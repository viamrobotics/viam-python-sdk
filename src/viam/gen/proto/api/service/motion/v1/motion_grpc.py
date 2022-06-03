import abc
import typing
import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server
import google.api.annotations_pb2
from ...... import proto
from ...... import proto

class MotionServiceBase(abc.ABC):

    @abc.abstractmethod
    async def Move(self, stream: 'grpclib.server.Stream[proto.api.service.motion.v1.motion_pb2.MoveRequest, proto.api.service.motion.v1.motion_pb2.MoveResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetPose(self, stream: 'grpclib.server.Stream[proto.api.service.motion.v1.motion_pb2.GetPoseRequest, proto.api.service.motion.v1.motion_pb2.GetPoseResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/proto.api.service.motion.v1.MotionService/Move': grpclib.const.Handler(self.Move, grpclib.const.Cardinality.UNARY_UNARY, proto.api.service.motion.v1.motion_pb2.MoveRequest, proto.api.service.motion.v1.motion_pb2.MoveResponse), '/proto.api.service.motion.v1.MotionService/GetPose': grpclib.const.Handler(self.GetPose, grpclib.const.Cardinality.UNARY_UNARY, proto.api.service.motion.v1.motion_pb2.GetPoseRequest, proto.api.service.motion.v1.motion_pb2.GetPoseResponse)}

class MotionServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.Move = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.service.motion.v1.MotionService/Move', proto.api.service.motion.v1.motion_pb2.MoveRequest, proto.api.service.motion.v1.motion_pb2.MoveResponse)
        self.GetPose = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.service.motion.v1.MotionService/GetPose', proto.api.service.motion.v1.motion_pb2.GetPoseRequest, proto.api.service.motion.v1.motion_pb2.GetPoseResponse)