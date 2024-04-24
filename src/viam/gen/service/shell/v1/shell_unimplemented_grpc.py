import abc
import typing
import grpclib.const
import grpclib.exceptions
if typing.TYPE_CHECKING:
    import grpclib.server
from .... import common
import google.api.annotations_pb2
import google.protobuf.struct_pb2
from .... import service
from .shell_grpc import ShellServiceBase as _ShellServiceBase

class UnimplementedShellServiceBase(_ShellServiceBase):

    async def Shell(self, stream: 'grpclib.server.Stream[service.shell.v1.shell_pb2.ShellRequest, service.shell.v1.shell_pb2.ShellResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def DoCommand(self, stream: 'grpclib.server.Stream[common.v1.common_pb2.DoCommandRequest, common.v1.common_pb2.DoCommandResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)