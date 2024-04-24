import abc
import typing
import grpclib.const
import grpclib.exceptions
if typing.TYPE_CHECKING:
    import grpclib.server
from .... import common
import google.protobuf.struct_pb2
import google.protobuf.timestamp_pb2
from .... import app
from .cloud_slam_grpc import CloudSLAMServiceBase as _CloudSLAMServiceBase

class UnimplementedCloudSLAMServiceBase(_CloudSLAMServiceBase):

    async def StartMappingSession(self, stream: 'grpclib.server.Stream[app.cloudslam.v1.cloud_slam_pb2.StartMappingSessionRequest, app.cloudslam.v1.cloud_slam_pb2.StartMappingSessionResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def GetActiveMappingSessionsForRobot(self, stream: 'grpclib.server.Stream[app.cloudslam.v1.cloud_slam_pb2.GetActiveMappingSessionsForRobotRequest, app.cloudslam.v1.cloud_slam_pb2.GetActiveMappingSessionsForRobotResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def GetMappingSessionPointCloud(self, stream: 'grpclib.server.Stream[app.cloudslam.v1.cloud_slam_pb2.GetMappingSessionPointCloudRequest, app.cloudslam.v1.cloud_slam_pb2.GetMappingSessionPointCloudResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def ListMappingSessions(self, stream: 'grpclib.server.Stream[app.cloudslam.v1.cloud_slam_pb2.ListMappingSessionsRequest, app.cloudslam.v1.cloud_slam_pb2.ListMappingSessionsResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def StopMappingSession(self, stream: 'grpclib.server.Stream[app.cloudslam.v1.cloud_slam_pb2.StopMappingSessionRequest, app.cloudslam.v1.cloud_slam_pb2.StopMappingSessionResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def GetMappingSessionMetadataByID(self, stream: 'grpclib.server.Stream[app.cloudslam.v1.cloud_slam_pb2.GetMappingSessionMetadataByIDRequest, app.cloudslam.v1.cloud_slam_pb2.GetMappingSessionMetadataByIDResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)