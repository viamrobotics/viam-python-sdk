import abc
import typing
import grpclib.const
import grpclib.exceptions
if typing.TYPE_CHECKING:
    import grpclib.server
from .... import common
from .... import component
from .testecho_grpc import TestEchoServiceBase as _TestEchoServiceBase

class UnimplementedTestEchoServiceBase(_TestEchoServiceBase):

    async def Echo(self, stream: 'grpclib.server.Stream[component.testecho.v1.testecho_pb2.EchoRequest, component.testecho.v1.testecho_pb2.EchoResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def EchoMultiple(self, stream: 'grpclib.server.Stream[component.testecho.v1.testecho_pb2.EchoMultipleRequest, component.testecho.v1.testecho_pb2.EchoMultipleResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def EchoBiDi(self, stream: 'grpclib.server.Stream[component.testecho.v1.testecho_pb2.EchoBiDiRequest, component.testecho.v1.testecho_pb2.EchoBiDiResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def Stop(self, stream: 'grpclib.server.Stream[component.testecho.v1.testecho_pb2.StopRequest, component.testecho.v1.testecho_pb2.StopResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)