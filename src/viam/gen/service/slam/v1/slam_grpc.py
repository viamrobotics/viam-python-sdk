import abc
import typing
import grpclib.const
import grpclib.client
import grpclib.exceptions
if typing.TYPE_CHECKING:
    import grpclib.server
from .... import common
import google.api.annotations_pb2
from .... import service

class SLAMServiceBase(abc.ABC):

    @abc.abstractmethod
    async def GetPosition(self, stream: 'grpclib.server.Stream[service.slam.v1.slam_pb2.GetPositionRequest, service.slam.v1.slam_pb2.GetPositionResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetPointCloudMap(self, stream: 'grpclib.server.Stream[service.slam.v1.slam_pb2.GetPointCloudMapRequest, service.slam.v1.slam_pb2.GetPointCloudMapResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetInternalState(self, stream: 'grpclib.server.Stream[service.slam.v1.slam_pb2.GetInternalStateRequest, service.slam.v1.slam_pb2.GetInternalStateResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetProperties(self, stream: 'grpclib.server.Stream[service.slam.v1.slam_pb2.GetPropertiesRequest, service.slam.v1.slam_pb2.GetPropertiesResponse]') -> None:
        pass

    @abc.abstractmethod
    async def DoCommand(self, stream: 'grpclib.server.Stream[common.v1.common_pb2.DoCommandRequest, common.v1.common_pb2.DoCommandResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/viam.service.slam.v1.SLAMService/GetPosition': grpclib.const.Handler(self.GetPosition, grpclib.const.Cardinality.UNARY_UNARY, service.slam.v1.slam_pb2.GetPositionRequest, service.slam.v1.slam_pb2.GetPositionResponse), '/viam.service.slam.v1.SLAMService/GetPointCloudMap': grpclib.const.Handler(self.GetPointCloudMap, grpclib.const.Cardinality.UNARY_STREAM, service.slam.v1.slam_pb2.GetPointCloudMapRequest, service.slam.v1.slam_pb2.GetPointCloudMapResponse), '/viam.service.slam.v1.SLAMService/GetInternalState': grpclib.const.Handler(self.GetInternalState, grpclib.const.Cardinality.UNARY_STREAM, service.slam.v1.slam_pb2.GetInternalStateRequest, service.slam.v1.slam_pb2.GetInternalStateResponse), '/viam.service.slam.v1.SLAMService/GetProperties': grpclib.const.Handler(self.GetProperties, grpclib.const.Cardinality.UNARY_UNARY, service.slam.v1.slam_pb2.GetPropertiesRequest, service.slam.v1.slam_pb2.GetPropertiesResponse), '/viam.service.slam.v1.SLAMService/DoCommand': grpclib.const.Handler(self.DoCommand, grpclib.const.Cardinality.UNARY_UNARY, common.v1.common_pb2.DoCommandRequest, common.v1.common_pb2.DoCommandResponse)}

class UnimplementedSLAMServiceBase(SLAMServiceBase):

    async def GetPosition(self, stream: 'grpclib.server.Stream[service.slam.v1.slam_pb2.GetPositionRequest, service.slam.v1.slam_pb2.GetPositionResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def GetPointCloudMap(self, stream: 'grpclib.server.Stream[service.slam.v1.slam_pb2.GetPointCloudMapRequest, service.slam.v1.slam_pb2.GetPointCloudMapResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def GetInternalState(self, stream: 'grpclib.server.Stream[service.slam.v1.slam_pb2.GetInternalStateRequest, service.slam.v1.slam_pb2.GetInternalStateResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def GetProperties(self, stream: 'grpclib.server.Stream[service.slam.v1.slam_pb2.GetPropertiesRequest, service.slam.v1.slam_pb2.GetPropertiesResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def DoCommand(self, stream: 'grpclib.server.Stream[common.v1.common_pb2.DoCommandRequest, common.v1.common_pb2.DoCommandResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

class SLAMServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.GetPosition = grpclib.client.UnaryUnaryMethod(channel, '/viam.service.slam.v1.SLAMService/GetPosition', service.slam.v1.slam_pb2.GetPositionRequest, service.slam.v1.slam_pb2.GetPositionResponse)
        self.GetPointCloudMap = grpclib.client.UnaryStreamMethod(channel, '/viam.service.slam.v1.SLAMService/GetPointCloudMap', service.slam.v1.slam_pb2.GetPointCloudMapRequest, service.slam.v1.slam_pb2.GetPointCloudMapResponse)
        self.GetInternalState = grpclib.client.UnaryStreamMethod(channel, '/viam.service.slam.v1.SLAMService/GetInternalState', service.slam.v1.slam_pb2.GetInternalStateRequest, service.slam.v1.slam_pb2.GetInternalStateResponse)
        self.GetProperties = grpclib.client.UnaryUnaryMethod(channel, '/viam.service.slam.v1.SLAMService/GetProperties', service.slam.v1.slam_pb2.GetPropertiesRequest, service.slam.v1.slam_pb2.GetPropertiesResponse)
        self.DoCommand = grpclib.client.UnaryUnaryMethod(channel, '/viam.service.slam.v1.SLAMService/DoCommand', common.v1.common_pb2.DoCommandRequest, common.v1.common_pb2.DoCommandResponse)