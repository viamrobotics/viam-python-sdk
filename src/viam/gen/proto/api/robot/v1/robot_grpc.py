import abc
import typing
import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server
import google.api.annotations_pb2
import google.protobuf.duration_pb2
import google.protobuf.struct_pb2
import google.protobuf.timestamp_pb2
from ..... import proto

class RobotServiceBase(abc.ABC):

    @abc.abstractmethod
    async def GetOperations(self, stream: 'grpclib.server.Stream[proto.api.robot.v1.robot_pb2.GetOperationsRequest, proto.api.robot.v1.robot_pb2.GetOperationsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def ResourceNames(self, stream: 'grpclib.server.Stream[proto.api.robot.v1.robot_pb2.ResourceNamesRequest, proto.api.robot.v1.robot_pb2.ResourceNamesResponse]') -> None:
        pass

    @abc.abstractmethod
    async def ResourceRPCSubtypes(self, stream: 'grpclib.server.Stream[proto.api.robot.v1.robot_pb2.ResourceRPCSubtypesRequest, proto.api.robot.v1.robot_pb2.ResourceRPCSubtypesResponse]') -> None:
        pass

    @abc.abstractmethod
    async def CancelOperation(self, stream: 'grpclib.server.Stream[proto.api.robot.v1.robot_pb2.CancelOperationRequest, proto.api.robot.v1.robot_pb2.CancelOperationResponse]') -> None:
        pass

    @abc.abstractmethod
    async def BlockForOperation(self, stream: 'grpclib.server.Stream[proto.api.robot.v1.robot_pb2.BlockForOperationRequest, proto.api.robot.v1.robot_pb2.BlockForOperationResponse]') -> None:
        pass

    @abc.abstractmethod
    async def DiscoverComponents(self, stream: 'grpclib.server.Stream[proto.api.robot.v1.robot_pb2.DiscoverComponentsRequest, proto.api.robot.v1.robot_pb2.DiscoverComponentsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def FrameSystemConfig(self, stream: 'grpclib.server.Stream[proto.api.robot.v1.robot_pb2.FrameSystemConfigRequest, proto.api.robot.v1.robot_pb2.FrameSystemConfigResponse]') -> None:
        pass

    @abc.abstractmethod
    async def TransformPose(self, stream: 'grpclib.server.Stream[proto.api.robot.v1.robot_pb2.TransformPoseRequest, proto.api.robot.v1.robot_pb2.TransformPoseResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetStatus(self, stream: 'grpclib.server.Stream[proto.api.robot.v1.robot_pb2.GetStatusRequest, proto.api.robot.v1.robot_pb2.GetStatusResponse]') -> None:
        pass

    @abc.abstractmethod
    async def StreamStatus(self, stream: 'grpclib.server.Stream[proto.api.robot.v1.robot_pb2.StreamStatusRequest, proto.api.robot.v1.robot_pb2.StreamStatusResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/proto.api.robot.v1.RobotService/GetOperations': grpclib.const.Handler(self.GetOperations, grpclib.const.Cardinality.UNARY_UNARY, proto.api.robot.v1.robot_pb2.GetOperationsRequest, proto.api.robot.v1.robot_pb2.GetOperationsResponse), '/proto.api.robot.v1.RobotService/ResourceNames': grpclib.const.Handler(self.ResourceNames, grpclib.const.Cardinality.UNARY_UNARY, proto.api.robot.v1.robot_pb2.ResourceNamesRequest, proto.api.robot.v1.robot_pb2.ResourceNamesResponse), '/proto.api.robot.v1.RobotService/ResourceRPCSubtypes': grpclib.const.Handler(self.ResourceRPCSubtypes, grpclib.const.Cardinality.UNARY_UNARY, proto.api.robot.v1.robot_pb2.ResourceRPCSubtypesRequest, proto.api.robot.v1.robot_pb2.ResourceRPCSubtypesResponse), '/proto.api.robot.v1.RobotService/CancelOperation': grpclib.const.Handler(self.CancelOperation, grpclib.const.Cardinality.UNARY_UNARY, proto.api.robot.v1.robot_pb2.CancelOperationRequest, proto.api.robot.v1.robot_pb2.CancelOperationResponse), '/proto.api.robot.v1.RobotService/BlockForOperation': grpclib.const.Handler(self.BlockForOperation, grpclib.const.Cardinality.UNARY_UNARY, proto.api.robot.v1.robot_pb2.BlockForOperationRequest, proto.api.robot.v1.robot_pb2.BlockForOperationResponse), '/proto.api.robot.v1.RobotService/DiscoverComponents': grpclib.const.Handler(self.DiscoverComponents, grpclib.const.Cardinality.UNARY_UNARY, proto.api.robot.v1.robot_pb2.DiscoverComponentsRequest, proto.api.robot.v1.robot_pb2.DiscoverComponentsResponse), '/proto.api.robot.v1.RobotService/FrameSystemConfig': grpclib.const.Handler(self.FrameSystemConfig, grpclib.const.Cardinality.UNARY_UNARY, proto.api.robot.v1.robot_pb2.FrameSystemConfigRequest, proto.api.robot.v1.robot_pb2.FrameSystemConfigResponse), '/proto.api.robot.v1.RobotService/TransformPose': grpclib.const.Handler(self.TransformPose, grpclib.const.Cardinality.UNARY_UNARY, proto.api.robot.v1.robot_pb2.TransformPoseRequest, proto.api.robot.v1.robot_pb2.TransformPoseResponse), '/proto.api.robot.v1.RobotService/GetStatus': grpclib.const.Handler(self.GetStatus, grpclib.const.Cardinality.UNARY_UNARY, proto.api.robot.v1.robot_pb2.GetStatusRequest, proto.api.robot.v1.robot_pb2.GetStatusResponse), '/proto.api.robot.v1.RobotService/StreamStatus': grpclib.const.Handler(self.StreamStatus, grpclib.const.Cardinality.UNARY_STREAM, proto.api.robot.v1.robot_pb2.StreamStatusRequest, proto.api.robot.v1.robot_pb2.StreamStatusResponse)}

class RobotServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.GetOperations = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.robot.v1.RobotService/GetOperations', proto.api.robot.v1.robot_pb2.GetOperationsRequest, proto.api.robot.v1.robot_pb2.GetOperationsResponse)
        self.ResourceNames = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.robot.v1.RobotService/ResourceNames', proto.api.robot.v1.robot_pb2.ResourceNamesRequest, proto.api.robot.v1.robot_pb2.ResourceNamesResponse)
        self.ResourceRPCSubtypes = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.robot.v1.RobotService/ResourceRPCSubtypes', proto.api.robot.v1.robot_pb2.ResourceRPCSubtypesRequest, proto.api.robot.v1.robot_pb2.ResourceRPCSubtypesResponse)
        self.CancelOperation = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.robot.v1.RobotService/CancelOperation', proto.api.robot.v1.robot_pb2.CancelOperationRequest, proto.api.robot.v1.robot_pb2.CancelOperationResponse)
        self.BlockForOperation = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.robot.v1.RobotService/BlockForOperation', proto.api.robot.v1.robot_pb2.BlockForOperationRequest, proto.api.robot.v1.robot_pb2.BlockForOperationResponse)
        self.DiscoverComponents = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.robot.v1.RobotService/DiscoverComponents', proto.api.robot.v1.robot_pb2.DiscoverComponentsRequest, proto.api.robot.v1.robot_pb2.DiscoverComponentsResponse)
        self.FrameSystemConfig = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.robot.v1.RobotService/FrameSystemConfig', proto.api.robot.v1.robot_pb2.FrameSystemConfigRequest, proto.api.robot.v1.robot_pb2.FrameSystemConfigResponse)
        self.TransformPose = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.robot.v1.RobotService/TransformPose', proto.api.robot.v1.robot_pb2.TransformPoseRequest, proto.api.robot.v1.robot_pb2.TransformPoseResponse)
        self.GetStatus = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.robot.v1.RobotService/GetStatus', proto.api.robot.v1.robot_pb2.GetStatusRequest, proto.api.robot.v1.robot_pb2.GetStatusResponse)
        self.StreamStatus = grpclib.client.UnaryStreamMethod(channel, '/proto.api.robot.v1.RobotService/StreamStatus', proto.api.robot.v1.robot_pb2.StreamStatusRequest, proto.api.robot.v1.robot_pb2.StreamStatusResponse)