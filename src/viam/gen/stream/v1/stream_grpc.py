import abc
import typing
import grpclib.const
import grpclib.client
import grpclib.exceptions
if typing.TYPE_CHECKING:
    import grpclib.server
from ... import stream

class StreamServiceBase(abc.ABC):

    @abc.abstractmethod
    async def ListStreams(self, stream: 'grpclib.server.Stream[stream.v1.stream_pb2.ListStreamsRequest, stream.v1.stream_pb2.ListStreamsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def AddStream(self, stream: 'grpclib.server.Stream[stream.v1.stream_pb2.AddStreamRequest, stream.v1.stream_pb2.AddStreamResponse]') -> None:
        pass

    @abc.abstractmethod
    async def RemoveStream(self, stream: 'grpclib.server.Stream[stream.v1.stream_pb2.RemoveStreamRequest, stream.v1.stream_pb2.RemoveStreamResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/proto.stream.v1.StreamService/ListStreams': grpclib.const.Handler(self.ListStreams, grpclib.const.Cardinality.UNARY_UNARY, stream.v1.stream_pb2.ListStreamsRequest, stream.v1.stream_pb2.ListStreamsResponse), '/proto.stream.v1.StreamService/AddStream': grpclib.const.Handler(self.AddStream, grpclib.const.Cardinality.UNARY_UNARY, stream.v1.stream_pb2.AddStreamRequest, stream.v1.stream_pb2.AddStreamResponse), '/proto.stream.v1.StreamService/RemoveStream': grpclib.const.Handler(self.RemoveStream, grpclib.const.Cardinality.UNARY_UNARY, stream.v1.stream_pb2.RemoveStreamRequest, stream.v1.stream_pb2.RemoveStreamResponse)}

class UnimplementedStreamServiceBase(StreamServiceBase):

    async def ListStreams(self, stream: 'grpclib.server.Stream[stream.v1.stream_pb2.ListStreamsRequest, stream.v1.stream_pb2.ListStreamsResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def AddStream(self, stream: 'grpclib.server.Stream[stream.v1.stream_pb2.AddStreamRequest, stream.v1.stream_pb2.AddStreamResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def RemoveStream(self, stream: 'grpclib.server.Stream[stream.v1.stream_pb2.RemoveStreamRequest, stream.v1.stream_pb2.RemoveStreamResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

class StreamServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.ListStreams = grpclib.client.UnaryUnaryMethod(channel, '/proto.stream.v1.StreamService/ListStreams', stream.v1.stream_pb2.ListStreamsRequest, stream.v1.stream_pb2.ListStreamsResponse)
        self.AddStream = grpclib.client.UnaryUnaryMethod(channel, '/proto.stream.v1.StreamService/AddStream', stream.v1.stream_pb2.AddStreamRequest, stream.v1.stream_pb2.AddStreamResponse)
        self.RemoveStream = grpclib.client.UnaryUnaryMethod(channel, '/proto.stream.v1.StreamService/RemoveStream', stream.v1.stream_pb2.RemoveStreamRequest, stream.v1.stream_pb2.RemoveStreamResponse)