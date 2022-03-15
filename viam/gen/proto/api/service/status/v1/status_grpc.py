import abc
import typing
import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server
import google.protobuf.struct_pb2
import google.protobuf.duration_pb2
import google.api.annotations_pb2
from ...... import proto
from ...... import proto

class StatusServiceBase(abc.ABC):

    @abc.abstractmethod
    async def GetStatus(self, stream: 'grpclib.server.Stream[proto.api.service.status.v1.status_pb2.GetStatusRequest, proto.api.service.status.v1.status_pb2.GetStatusResponse]') -> None:
        pass

    @abc.abstractmethod
    async def StreamStatus(self, stream: 'grpclib.server.Stream[proto.api.service.status.v1.status_pb2.StreamStatusRequest, proto.api.service.status.v1.status_pb2.StreamStatusResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/proto.api.service.status.v1.StatusService/GetStatus': grpclib.const.Handler(self.GetStatus, grpclib.const.Cardinality.UNARY_UNARY, proto.api.service.status.v1.status_pb2.GetStatusRequest, proto.api.service.status.v1.status_pb2.GetStatusResponse), '/proto.api.service.status.v1.StatusService/StreamStatus': grpclib.const.Handler(self.StreamStatus, grpclib.const.Cardinality.UNARY_STREAM, proto.api.service.status.v1.status_pb2.StreamStatusRequest, proto.api.service.status.v1.status_pb2.StreamStatusResponse)}

class StatusServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.GetStatus = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.service.status.v1.StatusService/GetStatus', proto.api.service.status.v1.status_pb2.GetStatusRequest, proto.api.service.status.v1.status_pb2.GetStatusResponse)
        self.StreamStatus = grpclib.client.UnaryStreamMethod(channel, '/proto.api.service.status.v1.StatusService/StreamStatus', proto.api.service.status.v1.status_pb2.StreamStatusRequest, proto.api.service.status.v1.status_pb2.StreamStatusResponse)