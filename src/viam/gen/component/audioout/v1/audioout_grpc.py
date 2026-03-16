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

class AudioOutServiceBase(abc.ABC):

    @abc.abstractmethod
    async def Play(self, stream: 'grpclib.server.Stream[component.audioout.v1.audioout_pb2.PlayRequest, component.audioout.v1.audioout_pb2.PlayResponse]') -> None:
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
        return {'/viam.component.audioout.v1.AudioOutService/Play': grpclib.const.Handler(self.Play, grpclib.const.Cardinality.UNARY_UNARY, component.audioout.v1.audioout_pb2.PlayRequest, component.audioout.v1.audioout_pb2.PlayResponse), '/viam.component.audioout.v1.AudioOutService/GetProperties': grpclib.const.Handler(self.GetProperties, grpclib.const.Cardinality.UNARY_UNARY, common.v1.common_pb2.GetPropertiesRequest, common.v1.common_pb2.GetPropertiesResponse), '/viam.component.audioout.v1.AudioOutService/DoCommand': grpclib.const.Handler(self.DoCommand, grpclib.const.Cardinality.UNARY_UNARY, common.v1.common_pb2.DoCommandRequest, common.v1.common_pb2.DoCommandResponse), '/viam.component.audioout.v1.AudioOutService/GetGeometries': grpclib.const.Handler(self.GetGeometries, grpclib.const.Cardinality.UNARY_UNARY, common.v1.common_pb2.GetGeometriesRequest, common.v1.common_pb2.GetGeometriesResponse)}

class UnimplementedAudioOutServiceBase(AudioOutServiceBase):

    async def Play(self, stream: 'grpclib.server.Stream[component.audioout.v1.audioout_pb2.PlayRequest, component.audioout.v1.audioout_pb2.PlayResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def GetProperties(self, stream: 'grpclib.server.Stream[common.v1.common_pb2.GetPropertiesRequest, common.v1.common_pb2.GetPropertiesResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def DoCommand(self, stream: 'grpclib.server.Stream[common.v1.common_pb2.DoCommandRequest, common.v1.common_pb2.DoCommandResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def GetGeometries(self, stream: 'grpclib.server.Stream[common.v1.common_pb2.GetGeometriesRequest, common.v1.common_pb2.GetGeometriesResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

class AudioOutServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.Play = grpclib.client.UnaryUnaryMethod(channel, '/viam.component.audioout.v1.AudioOutService/Play', component.audioout.v1.audioout_pb2.PlayRequest, component.audioout.v1.audioout_pb2.PlayResponse)
        self.GetProperties = grpclib.client.UnaryUnaryMethod(channel, '/viam.component.audioout.v1.AudioOutService/GetProperties', common.v1.common_pb2.GetPropertiesRequest, common.v1.common_pb2.GetPropertiesResponse)
        self.DoCommand = grpclib.client.UnaryUnaryMethod(channel, '/viam.component.audioout.v1.AudioOutService/DoCommand', common.v1.common_pb2.DoCommandRequest, common.v1.common_pb2.DoCommandResponse)
        self.GetGeometries = grpclib.client.UnaryUnaryMethod(channel, '/viam.component.audioout.v1.AudioOutService/GetGeometries', common.v1.common_pb2.GetGeometriesRequest, common.v1.common_pb2.GetGeometriesResponse)