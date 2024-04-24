import abc
import typing
import grpclib.const
import grpclib.exceptions
if typing.TYPE_CHECKING:
    import grpclib.server
from ... import stream
from .stream_grpc import StreamServiceBase as _StreamServiceBase

class UnimplementedStreamServiceBase(_StreamServiceBase):

    async def ListStreams(self, stream: 'grpclib.server.Stream[stream.v1.stream_pb2.ListStreamsRequest, stream.v1.stream_pb2.ListStreamsResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def AddStream(self, stream: 'grpclib.server.Stream[stream.v1.stream_pb2.AddStreamRequest, stream.v1.stream_pb2.AddStreamResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def RemoveStream(self, stream: 'grpclib.server.Stream[stream.v1.stream_pb2.RemoveStreamRequest, stream.v1.stream_pb2.RemoveStreamResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)