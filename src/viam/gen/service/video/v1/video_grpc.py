import abc
import typing
import grpclib.const
import grpclib.client
import grpclib.exceptions
if typing.TYPE_CHECKING:
    import grpclib.server
from .... import common
import google.api.annotations_pb2
import google.protobuf.struct_pb2
import google.protobuf.timestamp_pb2
from .... import service

class VideoServiceBase(abc.ABC):

    @abc.abstractmethod
    async def GetVideo(self, stream: 'grpclib.server.Stream[service.video.v1.video_pb2.GetVideoRequest, service.video.v1.video_pb2.GetVideoResponse]') -> None:
        pass

    @abc.abstractmethod
    async def DoCommand(self, stream: 'grpclib.server.Stream[common.v1.common_pb2.DoCommandRequest, common.v1.common_pb2.DoCommandResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/viam.service.video.v1.VideoService/GetVideo': grpclib.const.Handler(self.GetVideo, grpclib.const.Cardinality.UNARY_STREAM, service.video.v1.video_pb2.GetVideoRequest, service.video.v1.video_pb2.GetVideoResponse), '/viam.service.video.v1.VideoService/DoCommand': grpclib.const.Handler(self.DoCommand, grpclib.const.Cardinality.UNARY_UNARY, common.v1.common_pb2.DoCommandRequest, common.v1.common_pb2.DoCommandResponse)}

class UnimplementedVideoServiceBase(VideoServiceBase):

    async def GetVideo(self, stream: 'grpclib.server.Stream[service.video.v1.video_pb2.GetVideoRequest, service.video.v1.video_pb2.GetVideoResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def DoCommand(self, stream: 'grpclib.server.Stream[common.v1.common_pb2.DoCommandRequest, common.v1.common_pb2.DoCommandResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

class VideoServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.GetVideo = grpclib.client.UnaryStreamMethod(channel, '/viam.service.video.v1.VideoService/GetVideo', service.video.v1.video_pb2.GetVideoRequest, service.video.v1.video_pb2.GetVideoResponse)
        self.DoCommand = grpclib.client.UnaryUnaryMethod(channel, '/viam.service.video.v1.VideoService/DoCommand', common.v1.common_pb2.DoCommandRequest, common.v1.common_pb2.DoCommandResponse)