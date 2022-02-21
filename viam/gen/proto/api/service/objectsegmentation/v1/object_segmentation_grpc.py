import abc
import typing
import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server
import google.api.annotations_pb2
from ...... import proto
from ...... import proto

class ObjectSegmentationServiceBase(abc.ABC):

    @abc.abstractmethod
    async def GetObjectPointClouds(self, stream: 'grpclib.server.Stream[proto.api.service.objectsegmentation.v1.object_segmentation_pb2.GetObjectPointCloudsRequest, proto.api.service.objectsegmentation.v1.object_segmentation_pb2.GetObjectPointCloudsResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/proto.api.service.objectsegmentation.v1.ObjectSegmentationService/GetObjectPointClouds': grpclib.const.Handler(self.GetObjectPointClouds, grpclib.const.Cardinality.UNARY_UNARY, proto.api.service.objectsegmentation.v1.object_segmentation_pb2.GetObjectPointCloudsRequest, proto.api.service.objectsegmentation.v1.object_segmentation_pb2.GetObjectPointCloudsResponse)}

class ObjectSegmentationServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.GetObjectPointClouds = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.service.objectsegmentation.v1.ObjectSegmentationService/GetObjectPointClouds', proto.api.service.objectsegmentation.v1.object_segmentation_pb2.GetObjectPointCloudsRequest, proto.api.service.objectsegmentation.v1.object_segmentation_pb2.GetObjectPointCloudsResponse)