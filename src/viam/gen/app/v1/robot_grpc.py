import abc
import typing
import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server
from ... import app
import google.protobuf.duration_pb2
import google.protobuf.struct_pb2
from ... import tagger

class RobotServiceBase(abc.ABC):

    @abc.abstractmethod
    async def Config(self, stream: 'grpclib.server.Stream[app.v1.robot_pb2.ConfigRequest, app.v1.robot_pb2.ConfigResponse]') -> None:
        pass

    @abc.abstractmethod
    async def Certificate(self, stream: 'grpclib.server.Stream[app.v1.robot_pb2.CertificateRequest, app.v1.robot_pb2.CertificateResponse]') -> None:
        pass

    @abc.abstractmethod
    async def Log(self, stream: 'grpclib.server.Stream[app.v1.robot_pb2.LogRequest, app.v1.robot_pb2.LogResponse]') -> None:
        pass

    @abc.abstractmethod
    async def NeedsRestart(self, stream: 'grpclib.server.Stream[app.v1.robot_pb2.NeedsRestartRequest, app.v1.robot_pb2.NeedsRestartResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/viam.app.v1.RobotService/Config': grpclib.const.Handler(self.Config, grpclib.const.Cardinality.UNARY_UNARY, app.v1.robot_pb2.ConfigRequest, app.v1.robot_pb2.ConfigResponse), '/viam.app.v1.RobotService/Certificate': grpclib.const.Handler(self.Certificate, grpclib.const.Cardinality.UNARY_UNARY, app.v1.robot_pb2.CertificateRequest, app.v1.robot_pb2.CertificateResponse), '/viam.app.v1.RobotService/Log': grpclib.const.Handler(self.Log, grpclib.const.Cardinality.UNARY_UNARY, app.v1.robot_pb2.LogRequest, app.v1.robot_pb2.LogResponse), '/viam.app.v1.RobotService/NeedsRestart': grpclib.const.Handler(self.NeedsRestart, grpclib.const.Cardinality.UNARY_UNARY, app.v1.robot_pb2.NeedsRestartRequest, app.v1.robot_pb2.NeedsRestartResponse)}

class RobotServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.Config = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.v1.RobotService/Config', app.v1.robot_pb2.ConfigRequest, app.v1.robot_pb2.ConfigResponse)
        self.Certificate = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.v1.RobotService/Certificate', app.v1.robot_pb2.CertificateRequest, app.v1.robot_pb2.CertificateResponse)
        self.Log = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.v1.RobotService/Log', app.v1.robot_pb2.LogRequest, app.v1.robot_pb2.LogResponse)
        self.NeedsRestart = grpclib.client.UnaryUnaryMethod(channel, '/viam.app.v1.RobotService/NeedsRestart', app.v1.robot_pb2.NeedsRestartRequest, app.v1.robot_pb2.NeedsRestartResponse)