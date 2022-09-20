import abc
import typing
import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server
from .... import common
import google.api.annotations_pb2
import google.protobuf.struct_pb2
from .... import service

class VisionServiceBase(abc.ABC):

    @abc.abstractmethod
    async def GetModelParameterSchema(self, stream: 'grpclib.server.Stream[service.vision.v1.vision_pb2.GetModelParameterSchemaRequest, service.vision.v1.vision_pb2.GetModelParameterSchemaResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetDetectorNames(self, stream: 'grpclib.server.Stream[service.vision.v1.vision_pb2.GetDetectorNamesRequest, service.vision.v1.vision_pb2.GetDetectorNamesResponse]') -> None:
        pass

    @abc.abstractmethod
    async def AddDetector(self, stream: 'grpclib.server.Stream[service.vision.v1.vision_pb2.AddDetectorRequest, service.vision.v1.vision_pb2.AddDetectorResponse]') -> None:
        pass

    @abc.abstractmethod
    async def RemoveDetector(self, stream: 'grpclib.server.Stream[service.vision.v1.vision_pb2.RemoveDetectorRequest, service.vision.v1.vision_pb2.RemoveDetectorResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetDetectionsFromCamera(self, stream: 'grpclib.server.Stream[service.vision.v1.vision_pb2.GetDetectionsFromCameraRequest, service.vision.v1.vision_pb2.GetDetectionsFromCameraResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetDetections(self, stream: 'grpclib.server.Stream[service.vision.v1.vision_pb2.GetDetectionsRequest, service.vision.v1.vision_pb2.GetDetectionsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetClassifierNames(self, stream: 'grpclib.server.Stream[service.vision.v1.vision_pb2.GetClassifierNamesRequest, service.vision.v1.vision_pb2.GetClassifierNamesResponse]') -> None:
        pass

    @abc.abstractmethod
    async def AddClassifier(self, stream: 'grpclib.server.Stream[service.vision.v1.vision_pb2.AddClassifierRequest, service.vision.v1.vision_pb2.AddClassifierResponse]') -> None:
        pass

    @abc.abstractmethod
    async def RemoveClassifier(self, stream: 'grpclib.server.Stream[service.vision.v1.vision_pb2.RemoveClassifierRequest, service.vision.v1.vision_pb2.RemoveClassifierResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetClassificationsFromCamera(self, stream: 'grpclib.server.Stream[service.vision.v1.vision_pb2.GetClassificationsFromCameraRequest, service.vision.v1.vision_pb2.GetClassificationsFromCameraResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetClassifications(self, stream: 'grpclib.server.Stream[service.vision.v1.vision_pb2.GetClassificationsRequest, service.vision.v1.vision_pb2.GetClassificationsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetSegmenterNames(self, stream: 'grpclib.server.Stream[service.vision.v1.vision_pb2.GetSegmenterNamesRequest, service.vision.v1.vision_pb2.GetSegmenterNamesResponse]') -> None:
        pass

    @abc.abstractmethod
    async def AddSegmenter(self, stream: 'grpclib.server.Stream[service.vision.v1.vision_pb2.AddSegmenterRequest, service.vision.v1.vision_pb2.AddSegmenterResponse]') -> None:
        pass

    @abc.abstractmethod
    async def RemoveSegmenter(self, stream: 'grpclib.server.Stream[service.vision.v1.vision_pb2.RemoveSegmenterRequest, service.vision.v1.vision_pb2.RemoveSegmenterResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetObjectPointClouds(self, stream: 'grpclib.server.Stream[service.vision.v1.vision_pb2.GetObjectPointCloudsRequest, service.vision.v1.vision_pb2.GetObjectPointCloudsResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/viam.service.vision.v1.VisionService/GetModelParameterSchema': grpclib.const.Handler(self.GetModelParameterSchema, grpclib.const.Cardinality.UNARY_UNARY, service.vision.v1.vision_pb2.GetModelParameterSchemaRequest, service.vision.v1.vision_pb2.GetModelParameterSchemaResponse), '/viam.service.vision.v1.VisionService/GetDetectorNames': grpclib.const.Handler(self.GetDetectorNames, grpclib.const.Cardinality.UNARY_UNARY, service.vision.v1.vision_pb2.GetDetectorNamesRequest, service.vision.v1.vision_pb2.GetDetectorNamesResponse), '/viam.service.vision.v1.VisionService/AddDetector': grpclib.const.Handler(self.AddDetector, grpclib.const.Cardinality.UNARY_UNARY, service.vision.v1.vision_pb2.AddDetectorRequest, service.vision.v1.vision_pb2.AddDetectorResponse), '/viam.service.vision.v1.VisionService/RemoveDetector': grpclib.const.Handler(self.RemoveDetector, grpclib.const.Cardinality.UNARY_UNARY, service.vision.v1.vision_pb2.RemoveDetectorRequest, service.vision.v1.vision_pb2.RemoveDetectorResponse), '/viam.service.vision.v1.VisionService/GetDetectionsFromCamera': grpclib.const.Handler(self.GetDetectionsFromCamera, grpclib.const.Cardinality.UNARY_UNARY, service.vision.v1.vision_pb2.GetDetectionsFromCameraRequest, service.vision.v1.vision_pb2.GetDetectionsFromCameraResponse), '/viam.service.vision.v1.VisionService/GetDetections': grpclib.const.Handler(self.GetDetections, grpclib.const.Cardinality.UNARY_UNARY, service.vision.v1.vision_pb2.GetDetectionsRequest, service.vision.v1.vision_pb2.GetDetectionsResponse), '/viam.service.vision.v1.VisionService/GetClassifierNames': grpclib.const.Handler(self.GetClassifierNames, grpclib.const.Cardinality.UNARY_UNARY, service.vision.v1.vision_pb2.GetClassifierNamesRequest, service.vision.v1.vision_pb2.GetClassifierNamesResponse), '/viam.service.vision.v1.VisionService/AddClassifier': grpclib.const.Handler(self.AddClassifier, grpclib.const.Cardinality.UNARY_UNARY, service.vision.v1.vision_pb2.AddClassifierRequest, service.vision.v1.vision_pb2.AddClassifierResponse), '/viam.service.vision.v1.VisionService/RemoveClassifier': grpclib.const.Handler(self.RemoveClassifier, grpclib.const.Cardinality.UNARY_UNARY, service.vision.v1.vision_pb2.RemoveClassifierRequest, service.vision.v1.vision_pb2.RemoveClassifierResponse), '/viam.service.vision.v1.VisionService/GetClassificationsFromCamera': grpclib.const.Handler(self.GetClassificationsFromCamera, grpclib.const.Cardinality.UNARY_UNARY, service.vision.v1.vision_pb2.GetClassificationsFromCameraRequest, service.vision.v1.vision_pb2.GetClassificationsFromCameraResponse), '/viam.service.vision.v1.VisionService/GetClassifications': grpclib.const.Handler(self.GetClassifications, grpclib.const.Cardinality.UNARY_UNARY, service.vision.v1.vision_pb2.GetClassificationsRequest, service.vision.v1.vision_pb2.GetClassificationsResponse), '/viam.service.vision.v1.VisionService/GetSegmenterNames': grpclib.const.Handler(self.GetSegmenterNames, grpclib.const.Cardinality.UNARY_UNARY, service.vision.v1.vision_pb2.GetSegmenterNamesRequest, service.vision.v1.vision_pb2.GetSegmenterNamesResponse), '/viam.service.vision.v1.VisionService/AddSegmenter': grpclib.const.Handler(self.AddSegmenter, grpclib.const.Cardinality.UNARY_UNARY, service.vision.v1.vision_pb2.AddSegmenterRequest, service.vision.v1.vision_pb2.AddSegmenterResponse), '/viam.service.vision.v1.VisionService/RemoveSegmenter': grpclib.const.Handler(self.RemoveSegmenter, grpclib.const.Cardinality.UNARY_UNARY, service.vision.v1.vision_pb2.RemoveSegmenterRequest, service.vision.v1.vision_pb2.RemoveSegmenterResponse), '/viam.service.vision.v1.VisionService/GetObjectPointClouds': grpclib.const.Handler(self.GetObjectPointClouds, grpclib.const.Cardinality.UNARY_UNARY, service.vision.v1.vision_pb2.GetObjectPointCloudsRequest, service.vision.v1.vision_pb2.GetObjectPointCloudsResponse)}

class VisionServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.GetModelParameterSchema = grpclib.client.UnaryUnaryMethod(channel, '/viam.service.vision.v1.VisionService/GetModelParameterSchema', service.vision.v1.vision_pb2.GetModelParameterSchemaRequest, service.vision.v1.vision_pb2.GetModelParameterSchemaResponse)
        self.GetDetectorNames = grpclib.client.UnaryUnaryMethod(channel, '/viam.service.vision.v1.VisionService/GetDetectorNames', service.vision.v1.vision_pb2.GetDetectorNamesRequest, service.vision.v1.vision_pb2.GetDetectorNamesResponse)
        self.AddDetector = grpclib.client.UnaryUnaryMethod(channel, '/viam.service.vision.v1.VisionService/AddDetector', service.vision.v1.vision_pb2.AddDetectorRequest, service.vision.v1.vision_pb2.AddDetectorResponse)
        self.RemoveDetector = grpclib.client.UnaryUnaryMethod(channel, '/viam.service.vision.v1.VisionService/RemoveDetector', service.vision.v1.vision_pb2.RemoveDetectorRequest, service.vision.v1.vision_pb2.RemoveDetectorResponse)
        self.GetDetectionsFromCamera = grpclib.client.UnaryUnaryMethod(channel, '/viam.service.vision.v1.VisionService/GetDetectionsFromCamera', service.vision.v1.vision_pb2.GetDetectionsFromCameraRequest, service.vision.v1.vision_pb2.GetDetectionsFromCameraResponse)
        self.GetDetections = grpclib.client.UnaryUnaryMethod(channel, '/viam.service.vision.v1.VisionService/GetDetections', service.vision.v1.vision_pb2.GetDetectionsRequest, service.vision.v1.vision_pb2.GetDetectionsResponse)
        self.GetClassifierNames = grpclib.client.UnaryUnaryMethod(channel, '/viam.service.vision.v1.VisionService/GetClassifierNames', service.vision.v1.vision_pb2.GetClassifierNamesRequest, service.vision.v1.vision_pb2.GetClassifierNamesResponse)
        self.AddClassifier = grpclib.client.UnaryUnaryMethod(channel, '/viam.service.vision.v1.VisionService/AddClassifier', service.vision.v1.vision_pb2.AddClassifierRequest, service.vision.v1.vision_pb2.AddClassifierResponse)
        self.RemoveClassifier = grpclib.client.UnaryUnaryMethod(channel, '/viam.service.vision.v1.VisionService/RemoveClassifier', service.vision.v1.vision_pb2.RemoveClassifierRequest, service.vision.v1.vision_pb2.RemoveClassifierResponse)
        self.GetClassificationsFromCamera = grpclib.client.UnaryUnaryMethod(channel, '/viam.service.vision.v1.VisionService/GetClassificationsFromCamera', service.vision.v1.vision_pb2.GetClassificationsFromCameraRequest, service.vision.v1.vision_pb2.GetClassificationsFromCameraResponse)
        self.GetClassifications = grpclib.client.UnaryUnaryMethod(channel, '/viam.service.vision.v1.VisionService/GetClassifications', service.vision.v1.vision_pb2.GetClassificationsRequest, service.vision.v1.vision_pb2.GetClassificationsResponse)
        self.GetSegmenterNames = grpclib.client.UnaryUnaryMethod(channel, '/viam.service.vision.v1.VisionService/GetSegmenterNames', service.vision.v1.vision_pb2.GetSegmenterNamesRequest, service.vision.v1.vision_pb2.GetSegmenterNamesResponse)
        self.AddSegmenter = grpclib.client.UnaryUnaryMethod(channel, '/viam.service.vision.v1.VisionService/AddSegmenter', service.vision.v1.vision_pb2.AddSegmenterRequest, service.vision.v1.vision_pb2.AddSegmenterResponse)
        self.RemoveSegmenter = grpclib.client.UnaryUnaryMethod(channel, '/viam.service.vision.v1.VisionService/RemoveSegmenter', service.vision.v1.vision_pb2.RemoveSegmenterRequest, service.vision.v1.vision_pb2.RemoveSegmenterResponse)
        self.GetObjectPointClouds = grpclib.client.UnaryUnaryMethod(channel, '/viam.service.vision.v1.VisionService/GetObjectPointClouds', service.vision.v1.vision_pb2.GetObjectPointCloudsRequest, service.vision.v1.vision_pb2.GetObjectPointCloudsResponse)