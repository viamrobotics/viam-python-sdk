from datetime import timedelta

from google.protobuf.duration_pb2 import Duration
from grpclib.server import Stream

from viam.errors import MethodNotImplementedError
from viam.proto.robot import (
    BlockForOperationRequest,
    BlockForOperationResponse,
    CancelOperationRequest,
    CancelOperationResponse,
    FrameSystemConfigRequest,
    FrameSystemConfigResponse,
    GetCloudMetadataRequest,
    GetCloudMetadataResponse,
    GetOperationsRequest,
    GetOperationsResponse,
    GetSessionsRequest,
    GetSessionsResponse,
    GetStatusRequest,
    GetStatusResponse,
    LogRequest,
    LogResponse,
    ResourceNamesRequest,
    ResourceNamesResponse,
    ResourceRPCSubtypesRequest,
    ResourceRPCSubtypesResponse,
    RestartModuleRequest,
    RestartModuleResponse,
    SendSessionHeartbeatRequest,
    SendSessionHeartbeatResponse,
    ShutdownRequest,
    ShutdownResponse,
    StartSessionRequest,
    StartSessionResponse,
    StopAllRequest,
    StopAllResponse,
    StreamStatusRequest,
    StreamStatusResponse,
    TransformPCDRequest,
    TransformPCDResponse,
    TransformPoseRequest,
    TransformPoseResponse,
    UnimplementedRobotServiceBase,
)


class MockRobot(UnimplementedRobotServiceBase):
    SESSION_ID = "sid"
    HEARTBEAT_INTERVAL = 2

    def __init__(self):
        self.heartbeat_count = 0
        super().__init__()

    async def RestartModule(self, stream: Stream[RestartModuleRequest, RestartModuleResponse]) -> None:
        return None

    async def StartSession(self, stream: Stream[StartSessionRequest, StartSessionResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        heartbeat_window = Duration()
        heartbeat_window.FromTimedelta(timedelta(seconds=self.HEARTBEAT_INTERVAL))
        response = StartSessionResponse(id=self.SESSION_ID, heartbeat_window=heartbeat_window)
        await stream.send_message(response)

    async def SendSessionHeartbeat(self, stream: Stream[SendSessionHeartbeatRequest, SendSessionHeartbeatResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.heartbeat_count += 1
        response = SendSessionHeartbeatResponse()
        await stream.send_message(response)

    async def ResourceNames(self, stream: Stream[ResourceNamesRequest, ResourceNamesResponse]) -> None:
        raise MethodNotImplementedError("ResourceNames").grpc_error

    async def GetStatus(self, stream: Stream[GetStatusRequest, GetStatusResponse]) -> None:
        raise MethodNotImplementedError("GetStatus").grpc_error

    async def StreamStatus(self, stream: Stream[StreamStatusRequest, StreamStatusResponse]) -> None:
        raise MethodNotImplementedError("StreamStatus").grpc_error

    async def GetOperations(self, stream: Stream[GetOperationsRequest, GetOperationsResponse]) -> None:
        raise MethodNotImplementedError("GetOperations").grpc_error

    async def ResourceRPCSubtypes(self, stream: Stream[ResourceRPCSubtypesRequest, ResourceRPCSubtypesResponse]) -> None:
        raise MethodNotImplementedError("ResourceRPCSubtypes").grpc_error

    async def CancelOperation(self, stream: Stream[CancelOperationRequest, CancelOperationResponse]) -> None:
        raise MethodNotImplementedError("CancelOperation").grpc_error

    async def BlockForOperation(self, stream: Stream[BlockForOperationRequest, BlockForOperationResponse]) -> None:
        raise MethodNotImplementedError("BlockForOperation").grpc_error

    async def FrameSystemConfig(self, stream: Stream[FrameSystemConfigRequest, FrameSystemConfigResponse]) -> None:
        raise MethodNotImplementedError("FrameSystemConfig").grpc_error

    async def TransformPose(self, stream: Stream[TransformPoseRequest, TransformPoseResponse]) -> None:
        raise MethodNotImplementedError("TransformPose").grpc_error

    async def StopAll(self, stream: Stream[StopAllRequest, StopAllResponse]) -> None:
        raise MethodNotImplementedError("StopAll").grpc_error

    async def GetSessions(self, stream: Stream[GetSessionsRequest, GetSessionsResponse]) -> None:
        raise MethodNotImplementedError("GetSessions").grpc_error

    async def TransformPCD(self, stream: Stream[TransformPCDRequest, TransformPCDResponse]) -> None:
        raise MethodNotImplementedError("TransformPCD").grpc_error

    async def Log(self, stream: Stream[LogRequest, LogResponse]) -> None:
        raise MethodNotImplementedError("Log").grpc_error

    async def GetCloudMetadata(self, stream: Stream[GetCloudMetadataRequest, GetCloudMetadataResponse]) -> None:
        raise MethodNotImplementedError("GetCloudMetadata").grpc_error

    async def Shutdown(self, stream: Stream[ShutdownRequest, ShutdownResponse]) -> None:
        raise MethodNotImplementedError("Shutdown").grpc_error
