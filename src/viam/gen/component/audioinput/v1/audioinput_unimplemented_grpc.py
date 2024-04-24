import abc
import typing
import grpclib.const
import grpclib.exceptions
if typing.TYPE_CHECKING:
    import grpclib.server
from .... import common
import google.api.annotations_pb2
import google.api.httpbody_pb2
import google.protobuf.duration_pb2
from .... import component
from .audioinput_grpc import AudioInputServiceBase as _AudioInputServiceBase

class UnimplementedAudioInputServiceBase(_AudioInputServiceBase):

    async def Chunks(self, stream: 'grpclib.server.Stream[component.audioinput.v1.audioinput_pb2.ChunksRequest, component.audioinput.v1.audioinput_pb2.ChunksResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def Properties(self, stream: 'grpclib.server.Stream[component.audioinput.v1.audioinput_pb2.PropertiesRequest, component.audioinput.v1.audioinput_pb2.PropertiesResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def Record(self, stream: 'grpclib.server.Stream[component.audioinput.v1.audioinput_pb2.RecordRequest, google.api.httpbody_pb2.HttpBody]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def DoCommand(self, stream: 'grpclib.server.Stream[common.v1.common_pb2.DoCommandRequest, common.v1.common_pb2.DoCommandResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def GetGeometries(self, stream: 'grpclib.server.Stream[common.v1.common_pb2.GetGeometriesRequest, common.v1.common_pb2.GetGeometriesResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)