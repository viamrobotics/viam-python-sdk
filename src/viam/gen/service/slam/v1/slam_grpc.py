import abc
import typing
import grpclib.const
import grpclib.client
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
    async def GetMap(self, stream: 'grpclib.server.Stream[service.slam.v1.slam_pb2.GetMapRequest, service.slam.v1.slam_pb2.GetMapResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/viam.service.slam.v1.SLAMService/GetPosition': grpclib.const.Handler(self.GetPosition, grpclib.const.Cardinality.UNARY_UNARY, service.slam.v1.slam_pb2.GetPositionRequest, service.slam.v1.slam_pb2.GetPositionResponse), '/viam.service.slam.v1.SLAMService/GetMap': grpclib.const.Handler(self.GetMap, grpclib.const.Cardinality.UNARY_UNARY, service.slam.v1.slam_pb2.GetMapRequest, service.slam.v1.slam_pb2.GetMapResponse)}

class SLAMServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.GetPosition = grpclib.client.UnaryUnaryMethod(channel, '/viam.service.slam.v1.SLAMService/GetPosition', service.slam.v1.slam_pb2.GetPositionRequest, service.slam.v1.slam_pb2.GetPositionResponse)
        self.GetMap = grpclib.client.UnaryUnaryMethod(channel, '/viam.service.slam.v1.SLAMService/GetMap', service.slam.v1.slam_pb2.GetMapRequest, service.slam.v1.slam_pb2.GetMapResponse)