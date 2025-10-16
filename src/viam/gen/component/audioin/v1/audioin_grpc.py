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
from .... import component

class AudioInServiceBase(abc.ABC):

    @abc.abstractmethod
    async def GetAudio(self, stream: 'grpclib.server.Stream[component.audioin.v1.audioin_pb2.GetAudioRequest, component.audioin.v1.audioin_pb2.GetAudioResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetProperties(self, stream: 'grpclib.server.Stream[common.v1.common_pb2.GetPropertiesRequest, common.v1.common_pb2.GetPropertiesResponse]') -> None:
        pass

    @abc.abstractmethod
    async def DoCommand(self, stream: 'grpclib.server.Stream[common.v1.common_pb2.DoCommandRequest, common.v1.common_pb2.DoCommandResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetGeometries(self, stream: 'grpclib.server.Stream[common.v1.common_pb2.GetGeometriesRequest, common.v1.common_pb2.GetGeometriesResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/viam.component.audioin.v1.AudioInService/GetAudio': grpclib.const.Handler(self.GetAudio, grpclib.const.Cardinality.UNARY_STREAM, component.audioin.v1.audioin_pb2.GetAudioRequest, component.audioin.v1.audioin_pb2.GetAudioResponse), '/viam.component.audioin.v1.AudioInService/GetProperties': grpclib.const.Handler(self.GetProperties, grpclib.const.Cardinality.UNARY_UNARY, common.v1.common_pb2.GetPropertiesRequest, common.v1.common_pb2.GetPropertiesResponse), '/viam.component.audioin.v1.AudioInService/DoCommand': grpclib.const.Handler(self.DoCommand, grpclib.const.Cardinality.UNARY_UNARY, common.v1.common_pb2.DoCommandRequest, common.v1.common_pb2.DoCommandResponse), '/viam.component.audioin.v1.AudioInService/GetGeometries': grpclib.const.Handler(self.GetGeometries, grpclib.const.Cardinality.UNARY_UNARY, common.v1.common_pb2.GetGeometriesRequest, common.v1.common_pb2.GetGeometriesResponse)}

class UnimplementedAudioInServiceBase(AudioInServiceBase):

    async def GetAudio(self, stream: 'grpclib.server.Stream[component.audioin.v1.audioin_pb2.GetAudioRequest, component.audioin.v1.audioin_pb2.GetAudioResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def GetProperties(self, stream: 'grpclib.server.Stream[common.v1.common_pb2.GetPropertiesRequest, common.v1.common_pb2.GetPropertiesResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def DoCommand(self, stream: 'grpclib.server.Stream[common.v1.common_pb2.DoCommandRequest, common.v1.common_pb2.DoCommandResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def GetGeometries(self, stream: 'grpclib.server.Stream[common.v1.common_pb2.GetGeometriesRequest, common.v1.common_pb2.GetGeometriesResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

class AudioInServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.GetAudio = grpclib.client.UnaryStreamMethod(channel, '/viam.component.audioin.v1.AudioInService/GetAudio', component.audioin.v1.audioin_pb2.GetAudioRequest, component.audioin.v1.audioin_pb2.GetAudioResponse)
        self.GetProperties = grpclib.client.UnaryUnaryMethod(channel, '/viam.component.audioin.v1.AudioInService/GetProperties', common.v1.common_pb2.GetPropertiesRequest, common.v1.common_pb2.GetPropertiesResponse)
        self.DoCommand = grpclib.client.UnaryUnaryMethod(channel, '/viam.component.audioin.v1.AudioInService/DoCommand', common.v1.common_pb2.DoCommandRequest, common.v1.common_pb2.DoCommandResponse)
        self.GetGeometries = grpclib.client.UnaryUnaryMethod(channel, '/viam.component.audioin.v1.AudioInService/GetGeometries', common.v1.common_pb2.GetGeometriesRequest, common.v1.common_pb2.GetGeometriesResponse)