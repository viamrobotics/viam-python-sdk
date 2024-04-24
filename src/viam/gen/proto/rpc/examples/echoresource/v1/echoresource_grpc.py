import abc
import typing
import grpclib.const
import grpclib.client
import grpclib.exceptions
if typing.TYPE_CHECKING:
    import grpclib.server
from ...... import proto

class EchoResourceServiceBase(abc.ABC):

    @abc.abstractmethod
    async def EchoResource(self, stream: 'grpclib.server.Stream[proto.rpc.examples.echoresource.v1.echoresource_pb2.EchoResourceRequest, proto.rpc.examples.echoresource.v1.echoresource_pb2.EchoResourceResponse]') -> None:
        pass

    @abc.abstractmethod
    async def EchoResourceMultiple(self, stream: 'grpclib.server.Stream[proto.rpc.examples.echoresource.v1.echoresource_pb2.EchoResourceMultipleRequest, proto.rpc.examples.echoresource.v1.echoresource_pb2.EchoResourceMultipleResponse]') -> None:
        pass

    @abc.abstractmethod
    async def EchoResourceBiDi(self, stream: 'grpclib.server.Stream[proto.rpc.examples.echoresource.v1.echoresource_pb2.EchoResourceBiDiRequest, proto.rpc.examples.echoresource.v1.echoresource_pb2.EchoResourceBiDiResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/proto.rpc.examples.echoresource.v1.EchoResourceService/EchoResource': grpclib.const.Handler(self.EchoResource, grpclib.const.Cardinality.UNARY_UNARY, proto.rpc.examples.echoresource.v1.echoresource_pb2.EchoResourceRequest, proto.rpc.examples.echoresource.v1.echoresource_pb2.EchoResourceResponse), '/proto.rpc.examples.echoresource.v1.EchoResourceService/EchoResourceMultiple': grpclib.const.Handler(self.EchoResourceMultiple, grpclib.const.Cardinality.UNARY_STREAM, proto.rpc.examples.echoresource.v1.echoresource_pb2.EchoResourceMultipleRequest, proto.rpc.examples.echoresource.v1.echoresource_pb2.EchoResourceMultipleResponse), '/proto.rpc.examples.echoresource.v1.EchoResourceService/EchoResourceBiDi': grpclib.const.Handler(self.EchoResourceBiDi, grpclib.const.Cardinality.STREAM_STREAM, proto.rpc.examples.echoresource.v1.echoresource_pb2.EchoResourceBiDiRequest, proto.rpc.examples.echoresource.v1.echoresource_pb2.EchoResourceBiDiResponse)}

class UnimplementedEchoResourceServiceBase(EchoResourceServiceBase):

    async def EchoResource(self, stream: 'grpclib.server.Stream[proto.rpc.examples.echoresource.v1.echoresource_pb2.EchoResourceRequest, proto.rpc.examples.echoresource.v1.echoresource_pb2.EchoResourceResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def EchoResourceMultiple(self, stream: 'grpclib.server.Stream[proto.rpc.examples.echoresource.v1.echoresource_pb2.EchoResourceMultipleRequest, proto.rpc.examples.echoresource.v1.echoresource_pb2.EchoResourceMultipleResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def EchoResourceBiDi(self, stream: 'grpclib.server.Stream[proto.rpc.examples.echoresource.v1.echoresource_pb2.EchoResourceBiDiRequest, proto.rpc.examples.echoresource.v1.echoresource_pb2.EchoResourceBiDiResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

class EchoResourceServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.EchoResource = grpclib.client.UnaryUnaryMethod(channel, '/proto.rpc.examples.echoresource.v1.EchoResourceService/EchoResource', proto.rpc.examples.echoresource.v1.echoresource_pb2.EchoResourceRequest, proto.rpc.examples.echoresource.v1.echoresource_pb2.EchoResourceResponse)
        self.EchoResourceMultiple = grpclib.client.UnaryStreamMethod(channel, '/proto.rpc.examples.echoresource.v1.EchoResourceService/EchoResourceMultiple', proto.rpc.examples.echoresource.v1.echoresource_pb2.EchoResourceMultipleRequest, proto.rpc.examples.echoresource.v1.echoresource_pb2.EchoResourceMultipleResponse)
        self.EchoResourceBiDi = grpclib.client.StreamStreamMethod(channel, '/proto.rpc.examples.echoresource.v1.EchoResourceService/EchoResourceBiDi', proto.rpc.examples.echoresource.v1.echoresource_pb2.EchoResourceBiDiRequest, proto.rpc.examples.echoresource.v1.echoresource_pb2.EchoResourceBiDiResponse)