import abc
import typing
import grpclib.const
import grpclib.exceptions
if typing.TYPE_CHECKING:
    import grpclib.server
from ... import common
import google.api.annotations_pb2
import google.protobuf.duration_pb2
import google.protobuf.struct_pb2
import google.protobuf.timestamp_pb2
from ... import robot
from .robot_grpc import RobotServiceBase as _RobotServiceBase

class UnimplementedRobotServiceBase(_RobotServiceBase):

    async def GetOperations(self, stream: 'grpclib.server.Stream[robot.v1.robot_pb2.GetOperationsRequest, robot.v1.robot_pb2.GetOperationsResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def GetSessions(self, stream: 'grpclib.server.Stream[robot.v1.robot_pb2.GetSessionsRequest, robot.v1.robot_pb2.GetSessionsResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def ResourceNames(self, stream: 'grpclib.server.Stream[robot.v1.robot_pb2.ResourceNamesRequest, robot.v1.robot_pb2.ResourceNamesResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def ResourceRPCSubtypes(self, stream: 'grpclib.server.Stream[robot.v1.robot_pb2.ResourceRPCSubtypesRequest, robot.v1.robot_pb2.ResourceRPCSubtypesResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def CancelOperation(self, stream: 'grpclib.server.Stream[robot.v1.robot_pb2.CancelOperationRequest, robot.v1.robot_pb2.CancelOperationResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def BlockForOperation(self, stream: 'grpclib.server.Stream[robot.v1.robot_pb2.BlockForOperationRequest, robot.v1.robot_pb2.BlockForOperationResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def DiscoverComponents(self, stream: 'grpclib.server.Stream[robot.v1.robot_pb2.DiscoverComponentsRequest, robot.v1.robot_pb2.DiscoverComponentsResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def FrameSystemConfig(self, stream: 'grpclib.server.Stream[robot.v1.robot_pb2.FrameSystemConfigRequest, robot.v1.robot_pb2.FrameSystemConfigResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def TransformPose(self, stream: 'grpclib.server.Stream[robot.v1.robot_pb2.TransformPoseRequest, robot.v1.robot_pb2.TransformPoseResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def TransformPCD(self, stream: 'grpclib.server.Stream[robot.v1.robot_pb2.TransformPCDRequest, robot.v1.robot_pb2.TransformPCDResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def GetStatus(self, stream: 'grpclib.server.Stream[robot.v1.robot_pb2.GetStatusRequest, robot.v1.robot_pb2.GetStatusResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def StreamStatus(self, stream: 'grpclib.server.Stream[robot.v1.robot_pb2.StreamStatusRequest, robot.v1.robot_pb2.StreamStatusResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def StopAll(self, stream: 'grpclib.server.Stream[robot.v1.robot_pb2.StopAllRequest, robot.v1.robot_pb2.StopAllResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def StartSession(self, stream: 'grpclib.server.Stream[robot.v1.robot_pb2.StartSessionRequest, robot.v1.robot_pb2.StartSessionResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def SendSessionHeartbeat(self, stream: 'grpclib.server.Stream[robot.v1.robot_pb2.SendSessionHeartbeatRequest, robot.v1.robot_pb2.SendSessionHeartbeatResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def Log(self, stream: 'grpclib.server.Stream[robot.v1.robot_pb2.LogRequest, robot.v1.robot_pb2.LogResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def GetCloudMetadata(self, stream: 'grpclib.server.Stream[robot.v1.robot_pb2.GetCloudMetadataRequest, robot.v1.robot_pb2.GetCloudMetadataResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def RestartModule(self, stream: 'grpclib.server.Stream[robot.v1.robot_pb2.RestartModuleRequest, robot.v1.robot_pb2.RestartModuleResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)