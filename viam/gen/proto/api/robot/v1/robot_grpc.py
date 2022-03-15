import abc
import typing
import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server
import google.protobuf.struct_pb2
import google.api.annotations_pb2
from ..... import proto
from ..... import proto

class RobotServiceBase(abc.ABC):

    @abc.abstractmethod
    async def Config(self, stream: 'grpclib.server.Stream[proto.api.robot.v1.robot_pb2.ConfigRequest, proto.api.robot.v1.robot_pb2.ConfigResponse]') -> None:
        pass

    @abc.abstractmethod
    async def DoAction(self, stream: 'grpclib.server.Stream[proto.api.robot.v1.robot_pb2.DoActionRequest, proto.api.robot.v1.robot_pb2.DoActionResponse]') -> None:
        pass

    @abc.abstractmethod
    async def ExecuteFunction(self, stream: 'grpclib.server.Stream[proto.api.robot.v1.robot_pb2.ExecuteFunctionRequest, proto.api.robot.v1.robot_pb2.ExecuteFunctionResponse]') -> None:
        pass

    @abc.abstractmethod
    async def ExecuteSource(self, stream: 'grpclib.server.Stream[proto.api.robot.v1.robot_pb2.ExecuteSourceRequest, proto.api.robot.v1.robot_pb2.ExecuteSourceResponse]') -> None:
        pass

    @abc.abstractmethod
    async def ResourceRunCommand(self, stream: 'grpclib.server.Stream[proto.api.robot.v1.robot_pb2.ResourceRunCommandRequest, proto.api.robot.v1.robot_pb2.ResourceRunCommandResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/proto.api.robot.v1.RobotService/Config': grpclib.const.Handler(self.Config, grpclib.const.Cardinality.UNARY_UNARY, proto.api.robot.v1.robot_pb2.ConfigRequest, proto.api.robot.v1.robot_pb2.ConfigResponse), '/proto.api.robot.v1.RobotService/DoAction': grpclib.const.Handler(self.DoAction, grpclib.const.Cardinality.UNARY_UNARY, proto.api.robot.v1.robot_pb2.DoActionRequest, proto.api.robot.v1.robot_pb2.DoActionResponse), '/proto.api.robot.v1.RobotService/ExecuteFunction': grpclib.const.Handler(self.ExecuteFunction, grpclib.const.Cardinality.UNARY_UNARY, proto.api.robot.v1.robot_pb2.ExecuteFunctionRequest, proto.api.robot.v1.robot_pb2.ExecuteFunctionResponse), '/proto.api.robot.v1.RobotService/ExecuteSource': grpclib.const.Handler(self.ExecuteSource, grpclib.const.Cardinality.UNARY_UNARY, proto.api.robot.v1.robot_pb2.ExecuteSourceRequest, proto.api.robot.v1.robot_pb2.ExecuteSourceResponse), '/proto.api.robot.v1.RobotService/ResourceRunCommand': grpclib.const.Handler(self.ResourceRunCommand, grpclib.const.Cardinality.UNARY_UNARY, proto.api.robot.v1.robot_pb2.ResourceRunCommandRequest, proto.api.robot.v1.robot_pb2.ResourceRunCommandResponse)}

class RobotServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.Config = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.robot.v1.RobotService/Config', proto.api.robot.v1.robot_pb2.ConfigRequest, proto.api.robot.v1.robot_pb2.ConfigResponse)
        self.DoAction = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.robot.v1.RobotService/DoAction', proto.api.robot.v1.robot_pb2.DoActionRequest, proto.api.robot.v1.robot_pb2.DoActionResponse)
        self.ExecuteFunction = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.robot.v1.RobotService/ExecuteFunction', proto.api.robot.v1.robot_pb2.ExecuteFunctionRequest, proto.api.robot.v1.robot_pb2.ExecuteFunctionResponse)
        self.ExecuteSource = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.robot.v1.RobotService/ExecuteSource', proto.api.robot.v1.robot_pb2.ExecuteSourceRequest, proto.api.robot.v1.robot_pb2.ExecuteSourceResponse)
        self.ResourceRunCommand = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.robot.v1.RobotService/ResourceRunCommand', proto.api.robot.v1.robot_pb2.ResourceRunCommandRequest, proto.api.robot.v1.robot_pb2.ResourceRunCommandResponse)