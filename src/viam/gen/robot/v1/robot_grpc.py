import abc
import typing
import grpclib.const
import grpclib.client
import grpclib.exceptions
if typing.TYPE_CHECKING:
    import grpclib.server
from ... import common
import google.api.annotations_pb2
import google.protobuf.duration_pb2
import google.protobuf.struct_pb2
import google.protobuf.timestamp_pb2
from ... import robot

class RobotServiceBase(abc.ABC):

    @abc.abstractmethod
    async def GetOperations(self, stream: 'grpclib.server.Stream[robot.v1.robot_pb2.GetOperationsRequest, robot.v1.robot_pb2.GetOperationsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetSessions(self, stream: 'grpclib.server.Stream[robot.v1.robot_pb2.GetSessionsRequest, robot.v1.robot_pb2.GetSessionsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def ResourceNames(self, stream: 'grpclib.server.Stream[robot.v1.robot_pb2.ResourceNamesRequest, robot.v1.robot_pb2.ResourceNamesResponse]') -> None:
        pass

    @abc.abstractmethod
    async def ResourceRPCSubtypes(self, stream: 'grpclib.server.Stream[robot.v1.robot_pb2.ResourceRPCSubtypesRequest, robot.v1.robot_pb2.ResourceRPCSubtypesResponse]') -> None:
        pass

    @abc.abstractmethod
    async def CancelOperation(self, stream: 'grpclib.server.Stream[robot.v1.robot_pb2.CancelOperationRequest, robot.v1.robot_pb2.CancelOperationResponse]') -> None:
        pass

    @abc.abstractmethod
    async def BlockForOperation(self, stream: 'grpclib.server.Stream[robot.v1.robot_pb2.BlockForOperationRequest, robot.v1.robot_pb2.BlockForOperationResponse]') -> None:
        pass

    @abc.abstractmethod
    async def DiscoverComponents(self, stream: 'grpclib.server.Stream[robot.v1.robot_pb2.DiscoverComponentsRequest, robot.v1.robot_pb2.DiscoverComponentsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def FrameSystemConfig(self, stream: 'grpclib.server.Stream[robot.v1.robot_pb2.FrameSystemConfigRequest, robot.v1.robot_pb2.FrameSystemConfigResponse]') -> None:
        pass

    @abc.abstractmethod
    async def TransformPose(self, stream: 'grpclib.server.Stream[robot.v1.robot_pb2.TransformPoseRequest, robot.v1.robot_pb2.TransformPoseResponse]') -> None:
        pass

    @abc.abstractmethod
    async def TransformPCD(self, stream: 'grpclib.server.Stream[robot.v1.robot_pb2.TransformPCDRequest, robot.v1.robot_pb2.TransformPCDResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetStatus(self, stream: 'grpclib.server.Stream[robot.v1.robot_pb2.GetStatusRequest, robot.v1.robot_pb2.GetStatusResponse]') -> None:
        pass

    @abc.abstractmethod
    async def StreamStatus(self, stream: 'grpclib.server.Stream[robot.v1.robot_pb2.StreamStatusRequest, robot.v1.robot_pb2.StreamStatusResponse]') -> None:
        pass

    @abc.abstractmethod
    async def StopAll(self, stream: 'grpclib.server.Stream[robot.v1.robot_pb2.StopAllRequest, robot.v1.robot_pb2.StopAllResponse]') -> None:
        pass

    @abc.abstractmethod
    async def StartSession(self, stream: 'grpclib.server.Stream[robot.v1.robot_pb2.StartSessionRequest, robot.v1.robot_pb2.StartSessionResponse]') -> None:
        pass

    @abc.abstractmethod
    async def SendSessionHeartbeat(self, stream: 'grpclib.server.Stream[robot.v1.robot_pb2.SendSessionHeartbeatRequest, robot.v1.robot_pb2.SendSessionHeartbeatResponse]') -> None:
        pass

    @abc.abstractmethod
    async def Log(self, stream: 'grpclib.server.Stream[robot.v1.robot_pb2.LogRequest, robot.v1.robot_pb2.LogResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetCloudMetadata(self, stream: 'grpclib.server.Stream[robot.v1.robot_pb2.GetCloudMetadataRequest, robot.v1.robot_pb2.GetCloudMetadataResponse]') -> None:
        pass

    @abc.abstractmethod
    async def RestartModule(self, stream: 'grpclib.server.Stream[robot.v1.robot_pb2.RestartModuleRequest, robot.v1.robot_pb2.RestartModuleResponse]') -> None:
        pass

    @abc.abstractmethod
    async def Shutdown(self, stream: 'grpclib.server.Stream[robot.v1.robot_pb2.ShutdownRequest, robot.v1.robot_pb2.ShutdownResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetMachineStatus(self, stream: 'grpclib.server.Stream[robot.v1.robot_pb2.GetMachineStatusRequest, robot.v1.robot_pb2.GetMachineStatusResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetVersion(self, stream: 'grpclib.server.Stream[robot.v1.robot_pb2.GetVersionRequest, robot.v1.robot_pb2.GetVersionResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/viam.robot.v1.RobotService/GetOperations': grpclib.const.Handler(self.GetOperations, grpclib.const.Cardinality.UNARY_UNARY, robot.v1.robot_pb2.GetOperationsRequest, robot.v1.robot_pb2.GetOperationsResponse), '/viam.robot.v1.RobotService/GetSessions': grpclib.const.Handler(self.GetSessions, grpclib.const.Cardinality.UNARY_UNARY, robot.v1.robot_pb2.GetSessionsRequest, robot.v1.robot_pb2.GetSessionsResponse), '/viam.robot.v1.RobotService/ResourceNames': grpclib.const.Handler(self.ResourceNames, grpclib.const.Cardinality.UNARY_UNARY, robot.v1.robot_pb2.ResourceNamesRequest, robot.v1.robot_pb2.ResourceNamesResponse), '/viam.robot.v1.RobotService/ResourceRPCSubtypes': grpclib.const.Handler(self.ResourceRPCSubtypes, grpclib.const.Cardinality.UNARY_UNARY, robot.v1.robot_pb2.ResourceRPCSubtypesRequest, robot.v1.robot_pb2.ResourceRPCSubtypesResponse), '/viam.robot.v1.RobotService/CancelOperation': grpclib.const.Handler(self.CancelOperation, grpclib.const.Cardinality.UNARY_UNARY, robot.v1.robot_pb2.CancelOperationRequest, robot.v1.robot_pb2.CancelOperationResponse), '/viam.robot.v1.RobotService/BlockForOperation': grpclib.const.Handler(self.BlockForOperation, grpclib.const.Cardinality.UNARY_UNARY, robot.v1.robot_pb2.BlockForOperationRequest, robot.v1.robot_pb2.BlockForOperationResponse), '/viam.robot.v1.RobotService/DiscoverComponents': grpclib.const.Handler(self.DiscoverComponents, grpclib.const.Cardinality.UNARY_UNARY, robot.v1.robot_pb2.DiscoverComponentsRequest, robot.v1.robot_pb2.DiscoverComponentsResponse), '/viam.robot.v1.RobotService/FrameSystemConfig': grpclib.const.Handler(self.FrameSystemConfig, grpclib.const.Cardinality.UNARY_UNARY, robot.v1.robot_pb2.FrameSystemConfigRequest, robot.v1.robot_pb2.FrameSystemConfigResponse), '/viam.robot.v1.RobotService/TransformPose': grpclib.const.Handler(self.TransformPose, grpclib.const.Cardinality.UNARY_UNARY, robot.v1.robot_pb2.TransformPoseRequest, robot.v1.robot_pb2.TransformPoseResponse), '/viam.robot.v1.RobotService/TransformPCD': grpclib.const.Handler(self.TransformPCD, grpclib.const.Cardinality.UNARY_UNARY, robot.v1.robot_pb2.TransformPCDRequest, robot.v1.robot_pb2.TransformPCDResponse), '/viam.robot.v1.RobotService/GetStatus': grpclib.const.Handler(self.GetStatus, grpclib.const.Cardinality.UNARY_UNARY, robot.v1.robot_pb2.GetStatusRequest, robot.v1.robot_pb2.GetStatusResponse), '/viam.robot.v1.RobotService/StreamStatus': grpclib.const.Handler(self.StreamStatus, grpclib.const.Cardinality.UNARY_STREAM, robot.v1.robot_pb2.StreamStatusRequest, robot.v1.robot_pb2.StreamStatusResponse), '/viam.robot.v1.RobotService/StopAll': grpclib.const.Handler(self.StopAll, grpclib.const.Cardinality.UNARY_UNARY, robot.v1.robot_pb2.StopAllRequest, robot.v1.robot_pb2.StopAllResponse), '/viam.robot.v1.RobotService/StartSession': grpclib.const.Handler(self.StartSession, grpclib.const.Cardinality.UNARY_UNARY, robot.v1.robot_pb2.StartSessionRequest, robot.v1.robot_pb2.StartSessionResponse), '/viam.robot.v1.RobotService/SendSessionHeartbeat': grpclib.const.Handler(self.SendSessionHeartbeat, grpclib.const.Cardinality.UNARY_UNARY, robot.v1.robot_pb2.SendSessionHeartbeatRequest, robot.v1.robot_pb2.SendSessionHeartbeatResponse), '/viam.robot.v1.RobotService/Log': grpclib.const.Handler(self.Log, grpclib.const.Cardinality.UNARY_UNARY, robot.v1.robot_pb2.LogRequest, robot.v1.robot_pb2.LogResponse), '/viam.robot.v1.RobotService/GetCloudMetadata': grpclib.const.Handler(self.GetCloudMetadata, grpclib.const.Cardinality.UNARY_UNARY, robot.v1.robot_pb2.GetCloudMetadataRequest, robot.v1.robot_pb2.GetCloudMetadataResponse), '/viam.robot.v1.RobotService/RestartModule': grpclib.const.Handler(self.RestartModule, grpclib.const.Cardinality.UNARY_UNARY, robot.v1.robot_pb2.RestartModuleRequest, robot.v1.robot_pb2.RestartModuleResponse), '/viam.robot.v1.RobotService/Shutdown': grpclib.const.Handler(self.Shutdown, grpclib.const.Cardinality.UNARY_UNARY, robot.v1.robot_pb2.ShutdownRequest, robot.v1.robot_pb2.ShutdownResponse), '/viam.robot.v1.RobotService/GetMachineStatus': grpclib.const.Handler(self.GetMachineStatus, grpclib.const.Cardinality.UNARY_UNARY, robot.v1.robot_pb2.GetMachineStatusRequest, robot.v1.robot_pb2.GetMachineStatusResponse), '/viam.robot.v1.RobotService/GetVersion': grpclib.const.Handler(self.GetVersion, grpclib.const.Cardinality.UNARY_UNARY, robot.v1.robot_pb2.GetVersionRequest, robot.v1.robot_pb2.GetVersionResponse)}

class UnimplementedRobotServiceBase(RobotServiceBase):

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

    async def Shutdown(self, stream: 'grpclib.server.Stream[robot.v1.robot_pb2.ShutdownRequest, robot.v1.robot_pb2.ShutdownResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def GetMachineStatus(self, stream: 'grpclib.server.Stream[robot.v1.robot_pb2.GetMachineStatusRequest, robot.v1.robot_pb2.GetMachineStatusResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def GetVersion(self, stream: 'grpclib.server.Stream[robot.v1.robot_pb2.GetVersionRequest, robot.v1.robot_pb2.GetVersionResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

class RobotServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.GetOperations = grpclib.client.UnaryUnaryMethod(channel, '/viam.robot.v1.RobotService/GetOperations', robot.v1.robot_pb2.GetOperationsRequest, robot.v1.robot_pb2.GetOperationsResponse)
        self.GetSessions = grpclib.client.UnaryUnaryMethod(channel, '/viam.robot.v1.RobotService/GetSessions', robot.v1.robot_pb2.GetSessionsRequest, robot.v1.robot_pb2.GetSessionsResponse)
        self.ResourceNames = grpclib.client.UnaryUnaryMethod(channel, '/viam.robot.v1.RobotService/ResourceNames', robot.v1.robot_pb2.ResourceNamesRequest, robot.v1.robot_pb2.ResourceNamesResponse)
        self.ResourceRPCSubtypes = grpclib.client.UnaryUnaryMethod(channel, '/viam.robot.v1.RobotService/ResourceRPCSubtypes', robot.v1.robot_pb2.ResourceRPCSubtypesRequest, robot.v1.robot_pb2.ResourceRPCSubtypesResponse)
        self.CancelOperation = grpclib.client.UnaryUnaryMethod(channel, '/viam.robot.v1.RobotService/CancelOperation', robot.v1.robot_pb2.CancelOperationRequest, robot.v1.robot_pb2.CancelOperationResponse)
        self.BlockForOperation = grpclib.client.UnaryUnaryMethod(channel, '/viam.robot.v1.RobotService/BlockForOperation', robot.v1.robot_pb2.BlockForOperationRequest, robot.v1.robot_pb2.BlockForOperationResponse)
        self.DiscoverComponents = grpclib.client.UnaryUnaryMethod(channel, '/viam.robot.v1.RobotService/DiscoverComponents', robot.v1.robot_pb2.DiscoverComponentsRequest, robot.v1.robot_pb2.DiscoverComponentsResponse)
        self.FrameSystemConfig = grpclib.client.UnaryUnaryMethod(channel, '/viam.robot.v1.RobotService/FrameSystemConfig', robot.v1.robot_pb2.FrameSystemConfigRequest, robot.v1.robot_pb2.FrameSystemConfigResponse)
        self.TransformPose = grpclib.client.UnaryUnaryMethod(channel, '/viam.robot.v1.RobotService/TransformPose', robot.v1.robot_pb2.TransformPoseRequest, robot.v1.robot_pb2.TransformPoseResponse)
        self.TransformPCD = grpclib.client.UnaryUnaryMethod(channel, '/viam.robot.v1.RobotService/TransformPCD', robot.v1.robot_pb2.TransformPCDRequest, robot.v1.robot_pb2.TransformPCDResponse)
        self.GetStatus = grpclib.client.UnaryUnaryMethod(channel, '/viam.robot.v1.RobotService/GetStatus', robot.v1.robot_pb2.GetStatusRequest, robot.v1.robot_pb2.GetStatusResponse)
        self.StreamStatus = grpclib.client.UnaryStreamMethod(channel, '/viam.robot.v1.RobotService/StreamStatus', robot.v1.robot_pb2.StreamStatusRequest, robot.v1.robot_pb2.StreamStatusResponse)
        self.StopAll = grpclib.client.UnaryUnaryMethod(channel, '/viam.robot.v1.RobotService/StopAll', robot.v1.robot_pb2.StopAllRequest, robot.v1.robot_pb2.StopAllResponse)
        self.StartSession = grpclib.client.UnaryUnaryMethod(channel, '/viam.robot.v1.RobotService/StartSession', robot.v1.robot_pb2.StartSessionRequest, robot.v1.robot_pb2.StartSessionResponse)
        self.SendSessionHeartbeat = grpclib.client.UnaryUnaryMethod(channel, '/viam.robot.v1.RobotService/SendSessionHeartbeat', robot.v1.robot_pb2.SendSessionHeartbeatRequest, robot.v1.robot_pb2.SendSessionHeartbeatResponse)
        self.Log = grpclib.client.UnaryUnaryMethod(channel, '/viam.robot.v1.RobotService/Log', robot.v1.robot_pb2.LogRequest, robot.v1.robot_pb2.LogResponse)
        self.GetCloudMetadata = grpclib.client.UnaryUnaryMethod(channel, '/viam.robot.v1.RobotService/GetCloudMetadata', robot.v1.robot_pb2.GetCloudMetadataRequest, robot.v1.robot_pb2.GetCloudMetadataResponse)
        self.RestartModule = grpclib.client.UnaryUnaryMethod(channel, '/viam.robot.v1.RobotService/RestartModule', robot.v1.robot_pb2.RestartModuleRequest, robot.v1.robot_pb2.RestartModuleResponse)
        self.Shutdown = grpclib.client.UnaryUnaryMethod(channel, '/viam.robot.v1.RobotService/Shutdown', robot.v1.robot_pb2.ShutdownRequest, robot.v1.robot_pb2.ShutdownResponse)
        self.GetMachineStatus = grpclib.client.UnaryUnaryMethod(channel, '/viam.robot.v1.RobotService/GetMachineStatus', robot.v1.robot_pb2.GetMachineStatusRequest, robot.v1.robot_pb2.GetMachineStatusResponse)
        self.GetVersion = grpclib.client.UnaryUnaryMethod(channel, '/viam.robot.v1.RobotService/GetVersion', robot.v1.robot_pb2.GetVersionRequest, robot.v1.robot_pb2.GetVersionResponse)