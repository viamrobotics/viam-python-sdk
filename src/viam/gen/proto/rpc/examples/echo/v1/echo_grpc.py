import abc
import typing
import grpclib.const
import grpclib.client
import grpclib.exceptions
if typing.TYPE_CHECKING:
    import grpclib.server
import google.api.annotations_pb2
from ...... import proto

class EchoServiceBase(abc.ABC):

    @abc.abstractmethod
    async def Echo(self, stream: 'grpclib.server.Stream[proto.rpc.examples.echo.v1.echo_pb2.EchoRequest, proto.rpc.examples.echo.v1.echo_pb2.EchoResponse]') -> None:
        pass

    @abc.abstractmethod
    async def EchoMultiple(self, stream: 'grpclib.server.Stream[proto.rpc.examples.echo.v1.echo_pb2.EchoMultipleRequest, proto.rpc.examples.echo.v1.echo_pb2.EchoMultipleResponse]') -> None:
        pass

    @abc.abstractmethod
    async def EchoBiDi(self, stream: 'grpclib.server.Stream[proto.rpc.examples.echo.v1.echo_pb2.EchoBiDiRequest, proto.rpc.examples.echo.v1.echo_pb2.EchoBiDiResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/proto.rpc.examples.echo.v1.EchoService/Echo': grpclib.const.Handler(self.Echo, grpclib.const.Cardinality.UNARY_UNARY, proto.rpc.examples.echo.v1.echo_pb2.EchoRequest, proto.rpc.examples.echo.v1.echo_pb2.EchoResponse), '/proto.rpc.examples.echo.v1.EchoService/EchoMultiple': grpclib.const.Handler(self.EchoMultiple, grpclib.const.Cardinality.UNARY_STREAM, proto.rpc.examples.echo.v1.echo_pb2.EchoMultipleRequest, proto.rpc.examples.echo.v1.echo_pb2.EchoMultipleResponse), '/proto.rpc.examples.echo.v1.EchoService/EchoBiDi': grpclib.const.Handler(self.EchoBiDi, grpclib.const.Cardinality.STREAM_STREAM, proto.rpc.examples.echo.v1.echo_pb2.EchoBiDiRequest, proto.rpc.examples.echo.v1.echo_pb2.EchoBiDiResponse)}

class UnimplementedEchoServiceBase(EchoServiceBase):

    async def Echo(self, stream: 'grpclib.server.Stream[proto.rpc.examples.echo.v1.echo_pb2.EchoRequest, proto.rpc.examples.echo.v1.echo_pb2.EchoResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def EchoMultiple(self, stream: 'grpclib.server.Stream[proto.rpc.examples.echo.v1.echo_pb2.EchoMultipleRequest, proto.rpc.examples.echo.v1.echo_pb2.EchoMultipleResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def EchoBiDi(self, stream: 'grpclib.server.Stream[proto.rpc.examples.echo.v1.echo_pb2.EchoBiDiRequest, proto.rpc.examples.echo.v1.echo_pb2.EchoBiDiResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

class EchoServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.Echo = grpclib.client.UnaryUnaryMethod(channel, '/proto.rpc.examples.echo.v1.EchoService/Echo', proto.rpc.examples.echo.v1.echo_pb2.EchoRequest, proto.rpc.examples.echo.v1.echo_pb2.EchoResponse)
        self.EchoMultiple = grpclib.client.UnaryStreamMethod(channel, '/proto.rpc.examples.echo.v1.EchoService/EchoMultiple', proto.rpc.examples.echo.v1.echo_pb2.EchoMultipleRequest, proto.rpc.examples.echo.v1.echo_pb2.EchoMultipleResponse)
        self.EchoBiDi = grpclib.client.StreamStreamMethod(channel, '/proto.rpc.examples.echo.v1.EchoService/EchoBiDi', proto.rpc.examples.echo.v1.echo_pb2.EchoBiDiRequest, proto.rpc.examples.echo.v1.echo_pb2.EchoBiDiResponse)