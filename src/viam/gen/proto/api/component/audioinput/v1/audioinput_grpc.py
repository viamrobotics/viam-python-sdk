import abc
import typing
import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server
import google.api.annotations_pb2
import google.api.httpbody_pb2
import google.protobuf.duration_pb2
from ...... import proto

class AudioInputServiceBase(abc.ABC):

    @abc.abstractmethod
    async def Chunks(self, stream: 'grpclib.server.Stream[proto.api.component.audioinput.v1.audioinput_pb2.ChunksRequest, proto.api.component.audioinput.v1.audioinput_pb2.ChunksResponse]') -> None:
        pass

    @abc.abstractmethod
    async def Properties(self, stream: 'grpclib.server.Stream[proto.api.component.audioinput.v1.audioinput_pb2.PropertiesRequest, proto.api.component.audioinput.v1.audioinput_pb2.PropertiesResponse]') -> None:
        pass

    @abc.abstractmethod
    async def Record(self, stream: 'grpclib.server.Stream[proto.api.component.audioinput.v1.audioinput_pb2.RecordRequest, google.api.httpbody_pb2.HttpBody]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/proto.api.component.audioinput.v1.AudioInputService/Chunks': grpclib.const.Handler(self.Chunks, grpclib.const.Cardinality.UNARY_STREAM, proto.api.component.audioinput.v1.audioinput_pb2.ChunksRequest, proto.api.component.audioinput.v1.audioinput_pb2.ChunksResponse), '/proto.api.component.audioinput.v1.AudioInputService/Properties': grpclib.const.Handler(self.Properties, grpclib.const.Cardinality.UNARY_UNARY, proto.api.component.audioinput.v1.audioinput_pb2.PropertiesRequest, proto.api.component.audioinput.v1.audioinput_pb2.PropertiesResponse), '/proto.api.component.audioinput.v1.AudioInputService/Record': grpclib.const.Handler(self.Record, grpclib.const.Cardinality.UNARY_UNARY, proto.api.component.audioinput.v1.audioinput_pb2.RecordRequest, google.api.httpbody_pb2.HttpBody)}

class AudioInputServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.Chunks = grpclib.client.UnaryStreamMethod(channel, '/proto.api.component.audioinput.v1.AudioInputService/Chunks', proto.api.component.audioinput.v1.audioinput_pb2.ChunksRequest, proto.api.component.audioinput.v1.audioinput_pb2.ChunksResponse)
        self.Properties = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.component.audioinput.v1.AudioInputService/Properties', proto.api.component.audioinput.v1.audioinput_pb2.PropertiesRequest, proto.api.component.audioinput.v1.audioinput_pb2.PropertiesResponse)
        self.Record = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.component.audioinput.v1.AudioInputService/Record', proto.api.component.audioinput.v1.audioinput_pb2.RecordRequest, google.api.httpbody_pb2.HttpBody)