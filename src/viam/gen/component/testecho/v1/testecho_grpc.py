import abc
import typing
import grpclib.const
import grpclib.client
import grpclib.exceptions
if typing.TYPE_CHECKING:
    import grpclib.server
from .... import common
from .... import component

class TestEchoServiceBase(abc.ABC):

    @abc.abstractmethod
    async def Echo(self, stream: 'grpclib.server.Stream[component.testecho.v1.testecho_pb2.EchoRequest, component.testecho.v1.testecho_pb2.EchoResponse]') -> None:
        pass

    @abc.abstractmethod
    async def EchoMultiple(self, stream: 'grpclib.server.Stream[component.testecho.v1.testecho_pb2.EchoMultipleRequest, component.testecho.v1.testecho_pb2.EchoMultipleResponse]') -> None:
        pass

    @abc.abstractmethod
    async def EchoBiDi(self, stream: 'grpclib.server.Stream[component.testecho.v1.testecho_pb2.EchoBiDiRequest, component.testecho.v1.testecho_pb2.EchoBiDiResponse]') -> None:
        pass

    @abc.abstractmethod
    async def Stop(self, stream: 'grpclib.server.Stream[component.testecho.v1.testecho_pb2.StopRequest, component.testecho.v1.testecho_pb2.StopResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/viam.component.testecho.v1.TestEchoService/Echo': grpclib.const.Handler(self.Echo, grpclib.const.Cardinality.UNARY_UNARY, component.testecho.v1.testecho_pb2.EchoRequest, component.testecho.v1.testecho_pb2.EchoResponse), '/viam.component.testecho.v1.TestEchoService/EchoMultiple': grpclib.const.Handler(self.EchoMultiple, grpclib.const.Cardinality.UNARY_STREAM, component.testecho.v1.testecho_pb2.EchoMultipleRequest, component.testecho.v1.testecho_pb2.EchoMultipleResponse), '/viam.component.testecho.v1.TestEchoService/EchoBiDi': grpclib.const.Handler(self.EchoBiDi, grpclib.const.Cardinality.STREAM_STREAM, component.testecho.v1.testecho_pb2.EchoBiDiRequest, component.testecho.v1.testecho_pb2.EchoBiDiResponse), '/viam.component.testecho.v1.TestEchoService/Stop': grpclib.const.Handler(self.Stop, grpclib.const.Cardinality.UNARY_UNARY, component.testecho.v1.testecho_pb2.StopRequest, component.testecho.v1.testecho_pb2.StopResponse)}

class UnimplementedTestEchoServiceBase(TestEchoServiceBase):

    async def Echo(self, stream: 'grpclib.server.Stream[component.testecho.v1.testecho_pb2.EchoRequest, component.testecho.v1.testecho_pb2.EchoResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def EchoMultiple(self, stream: 'grpclib.server.Stream[component.testecho.v1.testecho_pb2.EchoMultipleRequest, component.testecho.v1.testecho_pb2.EchoMultipleResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def EchoBiDi(self, stream: 'grpclib.server.Stream[component.testecho.v1.testecho_pb2.EchoBiDiRequest, component.testecho.v1.testecho_pb2.EchoBiDiResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def Stop(self, stream: 'grpclib.server.Stream[component.testecho.v1.testecho_pb2.StopRequest, component.testecho.v1.testecho_pb2.StopResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

class TestEchoServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.Echo = grpclib.client.UnaryUnaryMethod(channel, '/viam.component.testecho.v1.TestEchoService/Echo', component.testecho.v1.testecho_pb2.EchoRequest, component.testecho.v1.testecho_pb2.EchoResponse)
        self.EchoMultiple = grpclib.client.UnaryStreamMethod(channel, '/viam.component.testecho.v1.TestEchoService/EchoMultiple', component.testecho.v1.testecho_pb2.EchoMultipleRequest, component.testecho.v1.testecho_pb2.EchoMultipleResponse)
        self.EchoBiDi = grpclib.client.StreamStreamMethod(channel, '/viam.component.testecho.v1.TestEchoService/EchoBiDi', component.testecho.v1.testecho_pb2.EchoBiDiRequest, component.testecho.v1.testecho_pb2.EchoBiDiResponse)
        self.Stop = grpclib.client.UnaryUnaryMethod(channel, '/viam.component.testecho.v1.TestEchoService/Stop', component.testecho.v1.testecho_pb2.StopRequest, component.testecho.v1.testecho_pb2.StopResponse)