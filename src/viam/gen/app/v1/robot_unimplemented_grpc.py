import abc
import typing
import grpclib.const
import grpclib.exceptions
if typing.TYPE_CHECKING:
    import grpclib.server
from ... import common
import google.protobuf.duration_pb2
import google.protobuf.struct_pb2
from ... import tagger
from ... import app
from .robot_grpc import RobotServiceBase as _RobotServiceBase

class UnimplementedRobotServiceBase(_RobotServiceBase):

    async def Config(self, stream: 'grpclib.server.Stream[app.v1.robot_pb2.ConfigRequest, app.v1.robot_pb2.ConfigResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def Certificate(self, stream: 'grpclib.server.Stream[app.v1.robot_pb2.CertificateRequest, app.v1.robot_pb2.CertificateResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def Log(self, stream: 'grpclib.server.Stream[app.v1.robot_pb2.LogRequest, app.v1.robot_pb2.LogResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def NeedsRestart(self, stream: 'grpclib.server.Stream[app.v1.robot_pb2.NeedsRestartRequest, app.v1.robot_pb2.NeedsRestartResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)