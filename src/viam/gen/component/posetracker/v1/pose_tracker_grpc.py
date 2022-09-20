import abc
import typing
import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server
from .... import common
import google.api.annotations_pb2
from .... import component

class PoseTrackerServiceBase(abc.ABC):

    @abc.abstractmethod
    async def GetPoses(self, stream: 'grpclib.server.Stream[component.posetracker.v1.pose_tracker_pb2.GetPosesRequest, component.posetracker.v1.pose_tracker_pb2.GetPosesResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/viam.component.posetracker.v1.PoseTrackerService/GetPoses': grpclib.const.Handler(self.GetPoses, grpclib.const.Cardinality.UNARY_UNARY, component.posetracker.v1.pose_tracker_pb2.GetPosesRequest, component.posetracker.v1.pose_tracker_pb2.GetPosesResponse)}

class PoseTrackerServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.GetPoses = grpclib.client.UnaryUnaryMethod(channel, '/viam.component.posetracker.v1.PoseTrackerService/GetPoses', component.posetracker.v1.pose_tracker_pb2.GetPosesRequest, component.posetracker.v1.pose_tracker_pb2.GetPosesResponse)