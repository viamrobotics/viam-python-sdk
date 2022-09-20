import abc
import typing
import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server
import google.api.annotations_pb2
import google.api.httpbody_pb2
import google.protobuf.duration_pb2
from .... import component

class AudioInputServiceBase(abc.ABC):

    @abc.abstractmethod
    async def Chunks(self, stream: 'grpclib.server.Stream[component.audioinput.v1.audioinput_pb2.ChunksRequest, component.audioinput.v1.audioinput_pb2.ChunksResponse]') -> None:
        pass

    @abc.abstractmethod
    async def Properties(self, stream: 'grpclib.server.Stream[component.audioinput.v1.audioinput_pb2.PropertiesRequest, component.audioinput.v1.audioinput_pb2.PropertiesResponse]') -> None:
        pass

    @abc.abstractmethod
    async def Record(self, stream: 'grpclib.server.Stream[component.audioinput.v1.audioinput_pb2.RecordRequest, google.api.httpbody_pb2.HttpBody]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/viam.component.audioinput.v1.AudioInputService/Chunks': grpclib.const.Handler(self.Chunks, grpclib.const.Cardinality.UNARY_STREAM, component.audioinput.v1.audioinput_pb2.ChunksRequest, component.audioinput.v1.audioinput_pb2.ChunksResponse), '/viam.component.audioinput.v1.AudioInputService/Properties': grpclib.const.Handler(self.Properties, grpclib.const.Cardinality.UNARY_UNARY, component.audioinput.v1.audioinput_pb2.PropertiesRequest, component.audioinput.v1.audioinput_pb2.PropertiesResponse), '/viam.component.audioinput.v1.AudioInputService/Record': grpclib.const.Handler(self.Record, grpclib.const.Cardinality.UNARY_UNARY, component.audioinput.v1.audioinput_pb2.RecordRequest, google.api.httpbody_pb2.HttpBody)}

class AudioInputServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.Chunks = grpclib.client.UnaryStreamMethod(channel, '/viam.component.audioinput.v1.AudioInputService/Chunks', component.audioinput.v1.audioinput_pb2.ChunksRequest, component.audioinput.v1.audioinput_pb2.ChunksResponse)
        self.Properties = grpclib.client.UnaryUnaryMethod(channel, '/viam.component.audioinput.v1.AudioInputService/Properties', component.audioinput.v1.audioinput_pb2.PropertiesRequest, component.audioinput.v1.audioinput_pb2.PropertiesResponse)
        self.Record = grpclib.client.UnaryUnaryMethod(channel, '/viam.component.audioinput.v1.AudioInputService/Record', component.audioinput.v1.audioinput_pb2.RecordRequest, google.api.httpbody_pb2.HttpBody)