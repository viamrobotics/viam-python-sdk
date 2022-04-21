import abc
import typing
import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server
import google.api.annotations_pb2
import google.protobuf.struct_pb2
from ...... import proto
from ...... import proto

class ObjectDetectionServiceBase(abc.ABC):

    @abc.abstractmethod
    async def DetectorNames(self, stream: 'grpclib.server.Stream[proto.api.service.objectdetection.v1.object_detection_pb2.DetectorNamesRequest, proto.api.service.objectdetection.v1.object_detection_pb2.DetectorNamesResponse]') -> None:
        pass

    @abc.abstractmethod
    async def AddDetector(self, stream: 'grpclib.server.Stream[proto.api.service.objectdetection.v1.object_detection_pb2.AddDetectorRequest, proto.api.service.objectdetection.v1.object_detection_pb2.AddDetectorResponse]') -> None:
        pass

    @abc.abstractmethod
    async def Detect(self, stream: 'grpclib.server.Stream[proto.api.service.objectdetection.v1.object_detection_pb2.DetectRequest, proto.api.service.objectdetection.v1.object_detection_pb2.DetectResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/proto.api.service.objectdetection.v1.ObjectDetectionService/DetectorNames': grpclib.const.Handler(self.DetectorNames, grpclib.const.Cardinality.UNARY_UNARY, proto.api.service.objectdetection.v1.object_detection_pb2.DetectorNamesRequest, proto.api.service.objectdetection.v1.object_detection_pb2.DetectorNamesResponse), '/proto.api.service.objectdetection.v1.ObjectDetectionService/AddDetector': grpclib.const.Handler(self.AddDetector, grpclib.const.Cardinality.UNARY_UNARY, proto.api.service.objectdetection.v1.object_detection_pb2.AddDetectorRequest, proto.api.service.objectdetection.v1.object_detection_pb2.AddDetectorResponse), '/proto.api.service.objectdetection.v1.ObjectDetectionService/Detect': grpclib.const.Handler(self.Detect, grpclib.const.Cardinality.UNARY_UNARY, proto.api.service.objectdetection.v1.object_detection_pb2.DetectRequest, proto.api.service.objectdetection.v1.object_detection_pb2.DetectResponse)}

class ObjectDetectionServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.DetectorNames = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.service.objectdetection.v1.ObjectDetectionService/DetectorNames', proto.api.service.objectdetection.v1.object_detection_pb2.DetectorNamesRequest, proto.api.service.objectdetection.v1.object_detection_pb2.DetectorNamesResponse)
        self.AddDetector = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.service.objectdetection.v1.ObjectDetectionService/AddDetector', proto.api.service.objectdetection.v1.object_detection_pb2.AddDetectorRequest, proto.api.service.objectdetection.v1.object_detection_pb2.AddDetectorResponse)
        self.Detect = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.service.objectdetection.v1.ObjectDetectionService/Detect', proto.api.service.objectdetection.v1.object_detection_pb2.DetectRequest, proto.api.service.objectdetection.v1.object_detection_pb2.DetectResponse)