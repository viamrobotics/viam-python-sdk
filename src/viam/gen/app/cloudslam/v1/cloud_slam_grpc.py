import abc
import typing
import grpclib.const
import grpclib.client
import grpclib.exceptions
if typing.TYPE_CHECKING:
    import grpclib.server
from .... import common
import google.protobuf.struct_pb2
import google.protobuf.timestamp_pb2
from .... import app

class CloudSLAMServiceBase(abc.ABC):

    @abc.abstractmethod
    async def StartMappingSession(self, stream: 'grpclib.server.Stream[app.cloudslam.v1.cloud_slam_pb2.StartMappingSessionRequest, app.cloudslam.v1.cloud_slam_pb2.StartMappingSessionResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetActiveMappingSessionsForRobot(self, stream: 'grpclib.server.Stream[app.cloudslam.v1.cloud_slam_pb2.GetActiveMappingSessionsForRobotRequest, app.cloudslam.v1.cloud_slam_pb2.GetActiveMappingSessionsForRobotResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetMappingSessionPointCloud(self, stream: 'grpclib.server.Stream[app.cloudslam.v1.cloud_slam_pb2.GetMappingSessionPointCloudRequest, app.cloudslam.v1.cloud_slam_pb2.GetMappingSessionPointCloudResponse]') -> None:
        pass

    @abc.abstractmethod
    async def ListMappingSessions(self, stream: 'grpclib.server.Stream[app.cloudslam.v1.cloud_slam_pb2.ListMappingSessionsRequest, app.cloudslam.v1.cloud_slam_pb2.ListMappingSessionsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def StopMappingSession(self, stream: 'grpclib.server.Stream[app.cloudslam.v1.cloud_slam_pb2.StopMappingSessionRequest, app.cloudslam.v1.cloud_slam_pb2.StopMappingSessionResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetMappingSessionMetadataByID(self, stream: 'grpclib.server.Stream[app.cloudslam.v1.cloud_slam_pb2.GetMappingSessionMetadataByIDRequest, app.cloudslam.v1.cloud_slam_pb2.GetMappingSessionMetadataByIDResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/viam.app.cloudslam.v1.CloudSLAMService/StartMappingSession': grpclib.const.Handler(self.StartMappingSession, grpclib.const.Cardinality.UNARY_UNARY, app.cloudslam.v1.cloud_slam_pb2.StartMappingSessionRequest, app.cloudslam.v1.cloud_slam_pb2.StartMappingSessionResponse), '/viam.app.cloudslam.v1.CloudSLAMService/GetActiveMappingSessionsForRobot': grpclib.const.Handler(self.GetActiveMappingSessionsForRobot, grpclib.const.Cardinality.UNARY_UNARY, app.cloudslam.v1.cloud_slam_pb2.GetActiveMappingSessionsForRobotRequest, app.cloudslam.v1.cloud_slam_pb2.GetActiveMappingSessionsForRobotResponse), '/viam.app.cloudslam.v1.CloudSLAMService/GetMappingSessionPointCloud': grpclib.const.Handler(self.GetMappingSessionPointCloud, grpclib.const.Cardinality.UNARY_UNARY, app.cloudslam.v1.cloud_slam_pb2.GetMappingSessionPointCloudRequest, app.cloudslam.v1.cloud_slam_pb2.GetMappingSessionPointCloudResponse), '/viam.app.cloudslam.v1.CloudSLAMService/ListMappingSessions': grpclib.const.Handler(self.ListMappingSessions, grpclib.const.Cardinality.UNARY_UNARY, app.cloudslam.v1.cloud_slam_pb2.ListMappingSessionsRequest, app.cloudslam.v1.cloud_slam_pb2.ListMappingSessionsResponse), '/viam.app.cloudslam.v1.CloudSLAMService/StopMappingSession': grpclib.const.Handler(self.StopMappingSession, grpclib.const.Cardinality.UNARY_UNARY, app.cloudslam.v1.cloud_slam_pb2.StopMappingSessionRequest, app.cloudslam.v1.cloud_slam_pb2.StopMappingSessionResponse), '/viam.app.cloudslam.v1.CloudSLAMService/GetMappingSessionMetadataByID': grpclib.const.Handler(self.GetMappingSessionMetadataByID, grpclib.const.Cardinality.UNARY_UNARY, app.cloudslam.v1.cloud_slam_pb2.GetMappingSessionMetadataByIDRequest, app.cloudslam.v1.cloud_slam_pb2.GetMappingSessionMetadataByIDResponse)}

class UnimplementedCloudSLAMServiceBase(CloudSLAMServiceBase):

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

class CloudSLAMServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.StartMappingSession = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.cloudslam.v1.CloudSLAMService/StartMappingSession', app.cloudslam.v1.cloud_slam_pb2.StartMappingSessionRequest, app.cloudslam.v1.cloud_slam_pb2.StartMappingSessionResponse)
        self.GetActiveMappingSessionsForRobot = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.cloudslam.v1.CloudSLAMService/GetActiveMappingSessionsForRobot', app.cloudslam.v1.cloud_slam_pb2.GetActiveMappingSessionsForRobotRequest, app.cloudslam.v1.cloud_slam_pb2.GetActiveMappingSessionsForRobotResponse)
        self.GetMappingSessionPointCloud = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.cloudslam.v1.CloudSLAMService/GetMappingSessionPointCloud', app.cloudslam.v1.cloud_slam_pb2.GetMappingSessionPointCloudRequest, app.cloudslam.v1.cloud_slam_pb2.GetMappingSessionPointCloudResponse)
        self.ListMappingSessions = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.cloudslam.v1.CloudSLAMService/ListMappingSessions', app.cloudslam.v1.cloud_slam_pb2.ListMappingSessionsRequest, app.cloudslam.v1.cloud_slam_pb2.ListMappingSessionsResponse)
        self.StopMappingSession = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.cloudslam.v1.CloudSLAMService/StopMappingSession', app.cloudslam.v1.cloud_slam_pb2.StopMappingSessionRequest, app.cloudslam.v1.cloud_slam_pb2.StopMappingSessionResponse)
        self.GetMappingSessionMetadataByID = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.cloudslam.v1.CloudSLAMService/GetMappingSessionMetadataByID', app.cloudslam.v1.cloud_slam_pb2.GetMappingSessionMetadataByIDRequest, app.cloudslam.v1.cloud_slam_pb2.GetMappingSessionMetadataByIDResponse)