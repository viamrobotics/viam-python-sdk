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

class EncoderServiceBase(abc.ABC):

    @abc.abstractmethod
    async def GetPosition(self, stream: 'grpclib.server.Stream[component.encoder.v1.encoder_pb2.GetPositionRequest, component.encoder.v1.encoder_pb2.GetPositionResponse]') -> None:
        pass

    @abc.abstractmethod
    async def ResetPosition(self, stream: 'grpclib.server.Stream[component.encoder.v1.encoder_pb2.ResetPositionRequest, component.encoder.v1.encoder_pb2.ResetPositionResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetProperties(self, stream: 'grpclib.server.Stream[component.encoder.v1.encoder_pb2.GetPropertiesRequest, component.encoder.v1.encoder_pb2.GetPropertiesResponse]') -> None:
        pass

    @abc.abstractmethod
    async def DoCommand(self, stream: 'grpclib.server.Stream[common.v1.common_pb2.DoCommandRequest, common.v1.common_pb2.DoCommandResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetGeometries(self, stream: 'grpclib.server.Stream[common.v1.common_pb2.GetGeometriesRequest, common.v1.common_pb2.GetGeometriesResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/viam.component.encoder.v1.EncoderService/GetPosition': grpclib.const.Handler(self.GetPosition, grpclib.const.Cardinality.UNARY_UNARY, component.encoder.v1.encoder_pb2.GetPositionRequest, component.encoder.v1.encoder_pb2.GetPositionResponse), '/viam.component.encoder.v1.EncoderService/ResetPosition': grpclib.const.Handler(self.ResetPosition, grpclib.const.Cardinality.UNARY_UNARY, component.encoder.v1.encoder_pb2.ResetPositionRequest, component.encoder.v1.encoder_pb2.ResetPositionResponse), '/viam.component.encoder.v1.EncoderService/GetProperties': grpclib.const.Handler(self.GetProperties, grpclib.const.Cardinality.UNARY_UNARY, component.encoder.v1.encoder_pb2.GetPropertiesRequest, component.encoder.v1.encoder_pb2.GetPropertiesResponse), '/viam.component.encoder.v1.EncoderService/DoCommand': grpclib.const.Handler(self.DoCommand, grpclib.const.Cardinality.UNARY_UNARY, common.v1.common_pb2.DoCommandRequest, common.v1.common_pb2.DoCommandResponse), '/viam.component.encoder.v1.EncoderService/GetGeometries': grpclib.const.Handler(self.GetGeometries, grpclib.const.Cardinality.UNARY_UNARY, common.v1.common_pb2.GetGeometriesRequest, common.v1.common_pb2.GetGeometriesResponse)}

class UnimplementedEncoderServiceBase(EncoderServiceBase):

    async def GetPosition(self, stream: 'grpclib.server.Stream[component.encoder.v1.encoder_pb2.GetPositionRequest, component.encoder.v1.encoder_pb2.GetPositionResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def ResetPosition(self, stream: 'grpclib.server.Stream[component.encoder.v1.encoder_pb2.ResetPositionRequest, component.encoder.v1.encoder_pb2.ResetPositionResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def GetProperties(self, stream: 'grpclib.server.Stream[component.encoder.v1.encoder_pb2.GetPropertiesRequest, component.encoder.v1.encoder_pb2.GetPropertiesResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def DoCommand(self, stream: 'grpclib.server.Stream[common.v1.common_pb2.DoCommandRequest, common.v1.common_pb2.DoCommandResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def GetGeometries(self, stream: 'grpclib.server.Stream[common.v1.common_pb2.GetGeometriesRequest, common.v1.common_pb2.GetGeometriesResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

class EncoderServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.GetPosition = grpclib.client.UnaryUnaryMethod(channel, '/viam.component.encoder.v1.EncoderService/GetPosition', component.encoder.v1.encoder_pb2.GetPositionRequest, component.encoder.v1.encoder_pb2.GetPositionResponse)
        self.ResetPosition = grpclib.client.UnaryUnaryMethod(channel, '/viam.component.encoder.v1.EncoderService/ResetPosition', component.encoder.v1.encoder_pb2.ResetPositionRequest, component.encoder.v1.encoder_pb2.ResetPositionResponse)
        self.GetProperties = grpclib.client.UnaryUnaryMethod(channel, '/viam.component.encoder.v1.EncoderService/GetProperties', component.encoder.v1.encoder_pb2.GetPropertiesRequest, component.encoder.v1.encoder_pb2.GetPropertiesResponse)
        self.DoCommand = grpclib.client.UnaryUnaryMethod(channel, '/viam.component.encoder.v1.EncoderService/DoCommand', common.v1.common_pb2.DoCommandRequest, common.v1.common_pb2.DoCommandResponse)
        self.GetGeometries = grpclib.client.UnaryUnaryMethod(channel, '/viam.component.encoder.v1.EncoderService/GetGeometries', common.v1.common_pb2.GetGeometriesRequest, common.v1.common_pb2.GetGeometriesResponse)