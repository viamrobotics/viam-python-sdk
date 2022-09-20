import abc
import typing
import grpclib.const
import grpclib.client
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
    async def GetStatus(self, stream: 'grpclib.server.Stream[robot.v1.robot_pb2.GetStatusRequest, robot.v1.robot_pb2.GetStatusResponse]') -> None:
        pass

    @abc.abstractmethod
    async def StreamStatus(self, stream: 'grpclib.server.Stream[robot.v1.robot_pb2.StreamStatusRequest, robot.v1.robot_pb2.StreamStatusResponse]') -> None:
        pass

    @abc.abstractmethod
    async def StopAll(self, stream: 'grpclib.server.Stream[robot.v1.robot_pb2.StopAllRequest, robot.v1.robot_pb2.StopAllResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/viam.robot.v1.RobotService/GetOperations': grpclib.const.Handler(self.GetOperations, grpclib.const.Cardinality.UNARY_UNARY, robot.v1.robot_pb2.GetOperationsRequest, robot.v1.robot_pb2.GetOperationsResponse), '/viam.robot.v1.RobotService/ResourceNames': grpclib.const.Handler(self.ResourceNames, grpclib.const.Cardinality.UNARY_UNARY, robot.v1.robot_pb2.ResourceNamesRequest, robot.v1.robot_pb2.ResourceNamesResponse), '/viam.robot.v1.RobotService/ResourceRPCSubtypes': grpclib.const.Handler(self.ResourceRPCSubtypes, grpclib.const.Cardinality.UNARY_UNARY, robot.v1.robot_pb2.ResourceRPCSubtypesRequest, robot.v1.robot_pb2.ResourceRPCSubtypesResponse), '/viam.robot.v1.RobotService/CancelOperation': grpclib.const.Handler(self.CancelOperation, grpclib.const.Cardinality.UNARY_UNARY, robot.v1.robot_pb2.CancelOperationRequest, robot.v1.robot_pb2.CancelOperationResponse), '/viam.robot.v1.RobotService/BlockForOperation': grpclib.const.Handler(self.BlockForOperation, grpclib.const.Cardinality.UNARY_UNARY, robot.v1.robot_pb2.BlockForOperationRequest, robot.v1.robot_pb2.BlockForOperationResponse), '/viam.robot.v1.RobotService/DiscoverComponents': grpclib.const.Handler(self.DiscoverComponents, grpclib.const.Cardinality.UNARY_UNARY, robot.v1.robot_pb2.DiscoverComponentsRequest, robot.v1.robot_pb2.DiscoverComponentsResponse), '/viam.robot.v1.RobotService/FrameSystemConfig': grpclib.const.Handler(self.FrameSystemConfig, grpclib.const.Cardinality.UNARY_UNARY, robot.v1.robot_pb2.FrameSystemConfigRequest, robot.v1.robot_pb2.FrameSystemConfigResponse), '/viam.robot.v1.RobotService/TransformPose': grpclib.const.Handler(self.TransformPose, grpclib.const.Cardinality.UNARY_UNARY, robot.v1.robot_pb2.TransformPoseRequest, robot.v1.robot_pb2.TransformPoseResponse), '/viam.robot.v1.RobotService/GetStatus': grpclib.const.Handler(self.GetStatus, grpclib.const.Cardinality.UNARY_UNARY, robot.v1.robot_pb2.GetStatusRequest, robot.v1.robot_pb2.GetStatusResponse), '/viam.robot.v1.RobotService/StreamStatus': grpclib.const.Handler(self.StreamStatus, grpclib.const.Cardinality.UNARY_STREAM, robot.v1.robot_pb2.StreamStatusRequest, robot.v1.robot_pb2.StreamStatusResponse), '/viam.robot.v1.RobotService/StopAll': grpclib.const.Handler(self.StopAll, grpclib.const.Cardinality.UNARY_UNARY, robot.v1.robot_pb2.StopAllRequest, robot.v1.robot_pb2.StopAllResponse)}

class RobotServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.GetOperations = grpclib.client.UnaryUnaryMethod(channel, '/viam.robot.v1.RobotService/GetOperations', robot.v1.robot_pb2.GetOperationsRequest, robot.v1.robot_pb2.GetOperationsResponse)
        self.ResourceNames = grpclib.client.UnaryUnaryMethod(channel, '/viam.robot.v1.RobotService/ResourceNames', robot.v1.robot_pb2.ResourceNamesRequest, robot.v1.robot_pb2.ResourceNamesResponse)
        self.ResourceRPCSubtypes = grpclib.client.UnaryUnaryMethod(channel, '/viam.robot.v1.RobotService/ResourceRPCSubtypes', robot.v1.robot_pb2.ResourceRPCSubtypesRequest, robot.v1.robot_pb2.ResourceRPCSubtypesResponse)
        self.CancelOperation = grpclib.client.UnaryUnaryMethod(channel, '/viam.robot.v1.RobotService/CancelOperation', robot.v1.robot_pb2.CancelOperationRequest, robot.v1.robot_pb2.CancelOperationResponse)
        self.BlockForOperation = grpclib.client.UnaryUnaryMethod(channel, '/viam.robot.v1.RobotService/BlockForOperation', robot.v1.robot_pb2.BlockForOperationRequest, robot.v1.robot_pb2.BlockForOperationResponse)
        self.DiscoverComponents = grpclib.client.UnaryUnaryMethod(channel, '/viam.robot.v1.RobotService/DiscoverComponents', robot.v1.robot_pb2.DiscoverComponentsRequest, robot.v1.robot_pb2.DiscoverComponentsResponse)
        self.FrameSystemConfig = grpclib.client.UnaryUnaryMethod(channel, '/viam.robot.v1.RobotService/FrameSystemConfig', robot.v1.robot_pb2.FrameSystemConfigRequest, robot.v1.robot_pb2.FrameSystemConfigResponse)
        self.TransformPose = grpclib.client.UnaryUnaryMethod(channel, '/viam.robot.v1.RobotService/TransformPose', robot.v1.robot_pb2.TransformPoseRequest, robot.v1.robot_pb2.TransformPoseResponse)
        self.GetStatus = grpclib.client.UnaryUnaryMethod(channel, '/viam.robot.v1.RobotService/GetStatus', robot.v1.robot_pb2.GetStatusRequest, robot.v1.robot_pb2.GetStatusResponse)
        self.StreamStatus = grpclib.client.UnaryStreamMethod(channel, '/viam.robot.v1.RobotService/StreamStatus', robot.v1.robot_pb2.StreamStatusRequest, robot.v1.robot_pb2.StreamStatusResponse)
        self.StopAll = grpclib.client.UnaryUnaryMethod(channel, '/viam.robot.v1.RobotService/StopAll', robot.v1.robot_pb2.StopAllRequest, robot.v1.robot_pb2.StopAllResponse)