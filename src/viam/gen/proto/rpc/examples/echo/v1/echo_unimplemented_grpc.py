import abc
import typing
import grpclib.const
import grpclib.exceptions
if typing.TYPE_CHECKING:
    import grpclib.server
import google.api.annotations_pb2
from ...... import proto
from .echo_grpc import EchoServiceBase as _EchoServiceBase

class UnimplementedEchoServiceBase(_EchoServiceBase):

    async def Echo(self, stream: 'grpclib.server.Stream[proto.rpc.examples.echo.v1.echo_pb2.EchoRequest, proto.rpc.examples.echo.v1.echo_pb2.EchoResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def EchoMultiple(self, stream: 'grpclib.server.Stream[proto.rpc.examples.echo.v1.echo_pb2.EchoMultipleRequest, proto.rpc.examples.echo.v1.echo_pb2.EchoMultipleResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def EchoBiDi(self, stream: 'grpclib.server.Stream[proto.rpc.examples.echo.v1.echo_pb2.EchoBiDiRequest, proto.rpc.examples.echo.v1.echo_pb2.EchoBiDiResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)