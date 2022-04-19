import abc
import typing
import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server
import google.protobuf.struct_pb2
import google.protobuf.timestamp_pb2
import google.api.annotations_pb2
from ..... import proto
from ..... import proto

class RobotServiceBase(abc.ABC):

    @abc.abstractmethod
    async def ResourceRunCommand(self, stream: 'grpclib.server.Stream[proto.api.robot.v1.robot_pb2.ResourceRunCommandRequest, proto.api.robot.v1.robot_pb2.ResourceRunCommandResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetOperations(self, stream: 'grpclib.server.Stream[proto.api.robot.v1.robot_pb2.GetOperationsRequest, proto.api.robot.v1.robot_pb2.GetOperationsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def CancelOperation(self, stream: 'grpclib.server.Stream[proto.api.robot.v1.robot_pb2.CancelOperationRequest, proto.api.robot.v1.robot_pb2.CancelOperationResponse]') -> None:
        pass

    @abc.abstractmethod
    async def BlockForOperation(self, stream: 'grpclib.server.Stream[proto.api.robot.v1.robot_pb2.BlockForOperationRequest, proto.api.robot.v1.robot_pb2.BlockForOperationResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/proto.api.robot.v1.RobotService/ResourceRunCommand': grpclib.const.Handler(self.ResourceRunCommand, grpclib.const.Cardinality.UNARY_UNARY, proto.api.robot.v1.robot_pb2.ResourceRunCommandRequest, proto.api.robot.v1.robot_pb2.ResourceRunCommandResponse), '/proto.api.robot.v1.RobotService/GetOperations': grpclib.const.Handler(self.GetOperations, grpclib.const.Cardinality.UNARY_UNARY, proto.api.robot.v1.robot_pb2.GetOperationsRequest, proto.api.robot.v1.robot_pb2.GetOperationsResponse), '/proto.api.robot.v1.RobotService/CancelOperation': grpclib.const.Handler(self.CancelOperation, grpclib.const.Cardinality.UNARY_UNARY, proto.api.robot.v1.robot_pb2.CancelOperationRequest, proto.api.robot.v1.robot_pb2.CancelOperationResponse), '/proto.api.robot.v1.RobotService/BlockForOperation': grpclib.const.Handler(self.BlockForOperation, grpclib.const.Cardinality.UNARY_UNARY, proto.api.robot.v1.robot_pb2.BlockForOperationRequest, proto.api.robot.v1.robot_pb2.BlockForOperationResponse)}

class RobotServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.ResourceRunCommand = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.robot.v1.RobotService/ResourceRunCommand', proto.api.robot.v1.robot_pb2.ResourceRunCommandRequest, proto.api.robot.v1.robot_pb2.ResourceRunCommandResponse)
        self.GetOperations = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.robot.v1.RobotService/GetOperations', proto.api.robot.v1.robot_pb2.GetOperationsRequest, proto.api.robot.v1.robot_pb2.GetOperationsResponse)
        self.CancelOperation = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.robot.v1.RobotService/CancelOperation', proto.api.robot.v1.robot_pb2.CancelOperationRequest, proto.api.robot.v1.robot_pb2.CancelOperationResponse)
        self.BlockForOperation = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.robot.v1.RobotService/BlockForOperation', proto.api.robot.v1.robot_pb2.BlockForOperationRequest, proto.api.robot.v1.robot_pb2.BlockForOperationResponse)