import abc
import typing
import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server
import google.api.annotations_pb2
from ...... import proto
from ...... import proto

class SLAMServiceBase(abc.ABC):

    @abc.abstractmethod
    async def GetPosition(self, stream: 'grpclib.server.Stream[proto.api.service.slam.v1.slam_pb2.GetPositionRequest, proto.api.service.slam.v1.slam_pb2.GetPositionResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetMap(self, stream: 'grpclib.server.Stream[proto.api.service.slam.v1.slam_pb2.GetMapRequest, proto.api.service.slam.v1.slam_pb2.GetMapResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/proto.api.service.slam.v1.SLAMService/GetPosition': grpclib.const.Handler(self.GetPosition, grpclib.const.Cardinality.UNARY_UNARY, proto.api.service.slam.v1.slam_pb2.GetPositionRequest, proto.api.service.slam.v1.slam_pb2.GetPositionResponse), '/proto.api.service.slam.v1.SLAMService/GetMap': grpclib.const.Handler(self.GetMap, grpclib.const.Cardinality.UNARY_UNARY, proto.api.service.slam.v1.slam_pb2.GetMapRequest, proto.api.service.slam.v1.slam_pb2.GetMapResponse)}

class SLAMServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.GetPosition = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.service.slam.v1.SLAMService/GetPosition', proto.api.service.slam.v1.slam_pb2.GetPositionRequest, proto.api.service.slam.v1.slam_pb2.GetPositionResponse)
        self.GetMap = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.service.slam.v1.SLAMService/GetMap', proto.api.service.slam.v1.slam_pb2.GetMapRequest, proto.api.service.slam.v1.slam_pb2.GetMapResponse)