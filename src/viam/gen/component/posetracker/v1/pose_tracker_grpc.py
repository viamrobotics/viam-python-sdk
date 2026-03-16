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
from .... import component

class PoseTrackerServiceBase(abc.ABC):

    @abc.abstractmethod
    async def GetPoses(self, stream: 'grpclib.server.Stream[component.posetracker.v1.pose_tracker_pb2.GetPosesRequest, component.posetracker.v1.pose_tracker_pb2.GetPosesResponse]') -> None:
        pass

    @abc.abstractmethod
    async def DoCommand(self, stream: 'grpclib.server.Stream[common.v1.common_pb2.DoCommandRequest, common.v1.common_pb2.DoCommandResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetGeometries(self, stream: 'grpclib.server.Stream[common.v1.common_pb2.GetGeometriesRequest, common.v1.common_pb2.GetGeometriesResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/viam.component.posetracker.v1.PoseTrackerService/GetPoses': grpclib.const.Handler(self.GetPoses, grpclib.const.Cardinality.UNARY_UNARY, component.posetracker.v1.pose_tracker_pb2.GetPosesRequest, component.posetracker.v1.pose_tracker_pb2.GetPosesResponse), '/viam.component.posetracker.v1.PoseTrackerService/DoCommand': grpclib.const.Handler(self.DoCommand, grpclib.const.Cardinality.UNARY_UNARY, common.v1.common_pb2.DoCommandRequest, common.v1.common_pb2.DoCommandResponse), '/viam.component.posetracker.v1.PoseTrackerService/GetGeometries': grpclib.const.Handler(self.GetGeometries, grpclib.const.Cardinality.UNARY_UNARY, common.v1.common_pb2.GetGeometriesRequest, common.v1.common_pb2.GetGeometriesResponse)}

class UnimplementedPoseTrackerServiceBase(PoseTrackerServiceBase):

    async def GetPoses(self, stream: 'grpclib.server.Stream[component.posetracker.v1.pose_tracker_pb2.GetPosesRequest, component.posetracker.v1.pose_tracker_pb2.GetPosesResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def DoCommand(self, stream: 'grpclib.server.Stream[common.v1.common_pb2.DoCommandRequest, common.v1.common_pb2.DoCommandResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def GetGeometries(self, stream: 'grpclib.server.Stream[common.v1.common_pb2.GetGeometriesRequest, common.v1.common_pb2.GetGeometriesResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

class PoseTrackerServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.GetPoses = grpclib.client.UnaryUnaryMethod(channel, '/viam.component.posetracker.v1.PoseTrackerService/GetPoses', component.posetracker.v1.pose_tracker_pb2.GetPosesRequest, component.posetracker.v1.pose_tracker_pb2.GetPosesResponse)
        self.DoCommand = grpclib.client.UnaryUnaryMethod(channel, '/viam.component.posetracker.v1.PoseTrackerService/DoCommand', common.v1.common_pb2.DoCommandRequest, common.v1.common_pb2.DoCommandResponse)
        self.GetGeometries = grpclib.client.UnaryUnaryMethod(channel, '/viam.component.posetracker.v1.PoseTrackerService/GetGeometries', common.v1.common_pb2.GetGeometriesRequest, common.v1.common_pb2.GetGeometriesResponse)