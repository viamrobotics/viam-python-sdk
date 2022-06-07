import abc
import typing
import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server
import google.api.annotations_pb2
import google.protobuf.struct_pb2
from ...... import proto
from ...... import proto

class PoseTrackerServiceBase(abc.ABC):

    @abc.abstractmethod
    async def GetPoses(self, stream: 'grpclib.server.Stream[proto.api.component.posetracker.v1.pose_tracker_pb2.GetPosesRequest, proto.api.component.posetracker.v1.pose_tracker_pb2.GetPosesResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/proto.api.component.posetracker.v1.PoseTrackerService/GetPoses': grpclib.const.Handler(self.GetPoses, grpclib.const.Cardinality.UNARY_UNARY, proto.api.component.posetracker.v1.pose_tracker_pb2.GetPosesRequest, proto.api.component.posetracker.v1.pose_tracker_pb2.GetPosesResponse)}

class PoseTrackerServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.GetPoses = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.component.posetracker.v1.PoseTrackerService/GetPoses', proto.api.component.posetracker.v1.pose_tracker_pb2.GetPosesRequest, proto.api.component.posetracker.v1.pose_tracker_pb2.GetPosesResponse)