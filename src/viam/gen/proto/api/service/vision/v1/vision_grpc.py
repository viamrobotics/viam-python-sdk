import abc
import typing
import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server
import google.api.annotations_pb2
import google.protobuf.struct_pb2
from ...... import proto

class VisionServiceBase(abc.ABC):

    @abc.abstractmethod
    async def GetModelParameterSchema(self, stream: 'grpclib.server.Stream[proto.api.service.vision.v1.vision_pb2.GetModelParameterSchemaRequest, proto.api.service.vision.v1.vision_pb2.GetModelParameterSchemaResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetDetectorNames(self, stream: 'grpclib.server.Stream[proto.api.service.vision.v1.vision_pb2.GetDetectorNamesRequest, proto.api.service.vision.v1.vision_pb2.GetDetectorNamesResponse]') -> None:
        pass

    @abc.abstractmethod
    async def AddDetector(self, stream: 'grpclib.server.Stream[proto.api.service.vision.v1.vision_pb2.AddDetectorRequest, proto.api.service.vision.v1.vision_pb2.AddDetectorResponse]') -> None:
        pass

    @abc.abstractmethod
    async def RemoveDetector(self, stream: 'grpclib.server.Stream[proto.api.service.vision.v1.vision_pb2.RemoveDetectorRequest, proto.api.service.vision.v1.vision_pb2.RemoveDetectorResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetDetectionsFromCamera(self, stream: 'grpclib.server.Stream[proto.api.service.vision.v1.vision_pb2.GetDetectionsFromCameraRequest, proto.api.service.vision.v1.vision_pb2.GetDetectionsFromCameraResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetDetections(self, stream: 'grpclib.server.Stream[proto.api.service.vision.v1.vision_pb2.GetDetectionsRequest, proto.api.service.vision.v1.vision_pb2.GetDetectionsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetClassifierNames(self, stream: 'grpclib.server.Stream[proto.api.service.vision.v1.vision_pb2.GetClassifierNamesRequest, proto.api.service.vision.v1.vision_pb2.GetClassifierNamesResponse]') -> None:
        pass

    @abc.abstractmethod
    async def AddClassifier(self, stream: 'grpclib.server.Stream[proto.api.service.vision.v1.vision_pb2.AddClassifierRequest, proto.api.service.vision.v1.vision_pb2.AddClassifierResponse]') -> None:
        pass

    @abc.abstractmethod
    async def RemoveClassifier(self, stream: 'grpclib.server.Stream[proto.api.service.vision.v1.vision_pb2.RemoveClassifierRequest, proto.api.service.vision.v1.vision_pb2.RemoveClassifierResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetClassificationsFromCamera(self, stream: 'grpclib.server.Stream[proto.api.service.vision.v1.vision_pb2.GetClassificationsFromCameraRequest, proto.api.service.vision.v1.vision_pb2.GetClassificationsFromCameraResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetClassifications(self, stream: 'grpclib.server.Stream[proto.api.service.vision.v1.vision_pb2.GetClassificationsRequest, proto.api.service.vision.v1.vision_pb2.GetClassificationsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetSegmenterNames(self, stream: 'grpclib.server.Stream[proto.api.service.vision.v1.vision_pb2.GetSegmenterNamesRequest, proto.api.service.vision.v1.vision_pb2.GetSegmenterNamesResponse]') -> None:
        pass

    @abc.abstractmethod
    async def AddSegmenter(self, stream: 'grpclib.server.Stream[proto.api.service.vision.v1.vision_pb2.AddSegmenterRequest, proto.api.service.vision.v1.vision_pb2.AddSegmenterResponse]') -> None:
        pass

    @abc.abstractmethod
    async def RemoveSegmenter(self, stream: 'grpclib.server.Stream[proto.api.service.vision.v1.vision_pb2.RemoveSegmenterRequest, proto.api.service.vision.v1.vision_pb2.RemoveSegmenterResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetObjectPointClouds(self, stream: 'grpclib.server.Stream[proto.api.service.vision.v1.vision_pb2.GetObjectPointCloudsRequest, proto.api.service.vision.v1.vision_pb2.GetObjectPointCloudsResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/proto.api.service.vision.v1.VisionService/GetModelParameterSchema': grpclib.const.Handler(self.GetModelParameterSchema, grpclib.const.Cardinality.UNARY_UNARY, proto.api.service.vision.v1.vision_pb2.GetModelParameterSchemaRequest, proto.api.service.vision.v1.vision_pb2.GetModelParameterSchemaResponse), '/proto.api.service.vision.v1.VisionService/GetDetectorNames': grpclib.const.Handler(self.GetDetectorNames, grpclib.const.Cardinality.UNARY_UNARY, proto.api.service.vision.v1.vision_pb2.GetDetectorNamesRequest, proto.api.service.vision.v1.vision_pb2.GetDetectorNamesResponse), '/proto.api.service.vision.v1.VisionService/AddDetector': grpclib.const.Handler(self.AddDetector, grpclib.const.Cardinality.UNARY_UNARY, proto.api.service.vision.v1.vision_pb2.AddDetectorRequest, proto.api.service.vision.v1.vision_pb2.AddDetectorResponse), '/proto.api.service.vision.v1.VisionService/RemoveDetector': grpclib.const.Handler(self.RemoveDetector, grpclib.const.Cardinality.UNARY_UNARY, proto.api.service.vision.v1.vision_pb2.RemoveDetectorRequest, proto.api.service.vision.v1.vision_pb2.RemoveDetectorResponse), '/proto.api.service.vision.v1.VisionService/GetDetectionsFromCamera': grpclib.const.Handler(self.GetDetectionsFromCamera, grpclib.const.Cardinality.UNARY_UNARY, proto.api.service.vision.v1.vision_pb2.GetDetectionsFromCameraRequest, proto.api.service.vision.v1.vision_pb2.GetDetectionsFromCameraResponse), '/proto.api.service.vision.v1.VisionService/GetDetections': grpclib.const.Handler(self.GetDetections, grpclib.const.Cardinality.UNARY_UNARY, proto.api.service.vision.v1.vision_pb2.GetDetectionsRequest, proto.api.service.vision.v1.vision_pb2.GetDetectionsResponse), '/proto.api.service.vision.v1.VisionService/GetClassifierNames': grpclib.const.Handler(self.GetClassifierNames, grpclib.const.Cardinality.UNARY_UNARY, proto.api.service.vision.v1.vision_pb2.GetClassifierNamesRequest, proto.api.service.vision.v1.vision_pb2.GetClassifierNamesResponse), '/proto.api.service.vision.v1.VisionService/AddClassifier': grpclib.const.Handler(self.AddClassifier, grpclib.const.Cardinality.UNARY_UNARY, proto.api.service.vision.v1.vision_pb2.AddClassifierRequest, proto.api.service.vision.v1.vision_pb2.AddClassifierResponse), '/proto.api.service.vision.v1.VisionService/RemoveClassifier': grpclib.const.Handler(self.RemoveClassifier, grpclib.const.Cardinality.UNARY_UNARY, proto.api.service.vision.v1.vision_pb2.RemoveClassifierRequest, proto.api.service.vision.v1.vision_pb2.RemoveClassifierResponse), '/proto.api.service.vision.v1.VisionService/GetClassificationsFromCamera': grpclib.const.Handler(self.GetClassificationsFromCamera, grpclib.const.Cardinality.UNARY_UNARY, proto.api.service.vision.v1.vision_pb2.GetClassificationsFromCameraRequest, proto.api.service.vision.v1.vision_pb2.GetClassificationsFromCameraResponse), '/proto.api.service.vision.v1.VisionService/GetClassifications': grpclib.const.Handler(self.GetClassifications, grpclib.const.Cardinality.UNARY_UNARY, proto.api.service.vision.v1.vision_pb2.GetClassificationsRequest, proto.api.service.vision.v1.vision_pb2.GetClassificationsResponse), '/proto.api.service.vision.v1.VisionService/GetSegmenterNames': grpclib.const.Handler(self.GetSegmenterNames, grpclib.const.Cardinality.UNARY_UNARY, proto.api.service.vision.v1.vision_pb2.GetSegmenterNamesRequest, proto.api.service.vision.v1.vision_pb2.GetSegmenterNamesResponse), '/proto.api.service.vision.v1.VisionService/AddSegmenter': grpclib.const.Handler(self.AddSegmenter, grpclib.const.Cardinality.UNARY_UNARY, proto.api.service.vision.v1.vision_pb2.AddSegmenterRequest, proto.api.service.vision.v1.vision_pb2.AddSegmenterResponse), '/proto.api.service.vision.v1.VisionService/RemoveSegmenter': grpclib.const.Handler(self.RemoveSegmenter, grpclib.const.Cardinality.UNARY_UNARY, proto.api.service.vision.v1.vision_pb2.RemoveSegmenterRequest, proto.api.service.vision.v1.vision_pb2.RemoveSegmenterResponse), '/proto.api.service.vision.v1.VisionService/GetObjectPointClouds': grpclib.const.Handler(self.GetObjectPointClouds, grpclib.const.Cardinality.UNARY_UNARY, proto.api.service.vision.v1.vision_pb2.GetObjectPointCloudsRequest, proto.api.service.vision.v1.vision_pb2.GetObjectPointCloudsResponse)}

class VisionServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.GetModelParameterSchema = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.service.vision.v1.VisionService/GetModelParameterSchema', proto.api.service.vision.v1.vision_pb2.GetModelParameterSchemaRequest, proto.api.service.vision.v1.vision_pb2.GetModelParameterSchemaResponse)
        self.GetDetectorNames = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.service.vision.v1.VisionService/GetDetectorNames', proto.api.service.vision.v1.vision_pb2.GetDetectorNamesRequest, proto.api.service.vision.v1.vision_pb2.GetDetectorNamesResponse)
        self.AddDetector = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.service.vision.v1.VisionService/AddDetector', proto.api.service.vision.v1.vision_pb2.AddDetectorRequest, proto.api.service.vision.v1.vision_pb2.AddDetectorResponse)
        self.RemoveDetector = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.service.vision.v1.VisionService/RemoveDetector', proto.api.service.vision.v1.vision_pb2.RemoveDetectorRequest, proto.api.service.vision.v1.vision_pb2.RemoveDetectorResponse)
        self.GetDetectionsFromCamera = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.service.vision.v1.VisionService/GetDetectionsFromCamera', proto.api.service.vision.v1.vision_pb2.GetDetectionsFromCameraRequest, proto.api.service.vision.v1.vision_pb2.GetDetectionsFromCameraResponse)
        self.GetDetections = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.service.vision.v1.VisionService/GetDetections', proto.api.service.vision.v1.vision_pb2.GetDetectionsRequest, proto.api.service.vision.v1.vision_pb2.GetDetectionsResponse)
        self.GetClassifierNames = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.service.vision.v1.VisionService/GetClassifierNames', proto.api.service.vision.v1.vision_pb2.GetClassifierNamesRequest, proto.api.service.vision.v1.vision_pb2.GetClassifierNamesResponse)
        self.AddClassifier = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.service.vision.v1.VisionService/AddClassifier', proto.api.service.vision.v1.vision_pb2.AddClassifierRequest, proto.api.service.vision.v1.vision_pb2.AddClassifierResponse)
        self.RemoveClassifier = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.service.vision.v1.VisionService/RemoveClassifier', proto.api.service.vision.v1.vision_pb2.RemoveClassifierRequest, proto.api.service.vision.v1.vision_pb2.RemoveClassifierResponse)
        self.GetClassificationsFromCamera = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.service.vision.v1.VisionService/GetClassificationsFromCamera', proto.api.service.vision.v1.vision_pb2.GetClassificationsFromCameraRequest, proto.api.service.vision.v1.vision_pb2.GetClassificationsFromCameraResponse)
        self.GetClassifications = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.service.vision.v1.VisionService/GetClassifications', proto.api.service.vision.v1.vision_pb2.GetClassificationsRequest, proto.api.service.vision.v1.vision_pb2.GetClassificationsResponse)
        self.GetSegmenterNames = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.service.vision.v1.VisionService/GetSegmenterNames', proto.api.service.vision.v1.vision_pb2.GetSegmenterNamesRequest, proto.api.service.vision.v1.vision_pb2.GetSegmenterNamesResponse)
        self.AddSegmenter = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.service.vision.v1.VisionService/AddSegmenter', proto.api.service.vision.v1.vision_pb2.AddSegmenterRequest, proto.api.service.vision.v1.vision_pb2.AddSegmenterResponse)
        self.RemoveSegmenter = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.service.vision.v1.VisionService/RemoveSegmenter', proto.api.service.vision.v1.vision_pb2.RemoveSegmenterRequest, proto.api.service.vision.v1.vision_pb2.RemoveSegmenterResponse)
        self.GetObjectPointClouds = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.service.vision.v1.VisionService/GetObjectPointClouds', proto.api.service.vision.v1.vision_pb2.GetObjectPointCloudsRequest, proto.api.service.vision.v1.vision_pb2.GetObjectPointCloudsResponse)