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
    async def GetDetectorNames(self, stream: 'grpclib.server.Stream[proto.api.service.vision.v1.vision_pb2.GetDetectorNamesRequest, proto.api.service.vision.v1.vision_pb2.GetDetectorNamesResponse]') -> None:
        pass

    @abc.abstractmethod
    async def AddDetector(self, stream: 'grpclib.server.Stream[proto.api.service.vision.v1.vision_pb2.AddDetectorRequest, proto.api.service.vision.v1.vision_pb2.AddDetectorResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetDetectionsFromCamera(self, stream: 'grpclib.server.Stream[proto.api.service.vision.v1.vision_pb2.GetDetectionsFromCameraRequest, proto.api.service.vision.v1.vision_pb2.GetDetectionsFromCameraResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetDetections(self, stream: 'grpclib.server.Stream[proto.api.service.vision.v1.vision_pb2.GetDetectionsRequest, proto.api.service.vision.v1.vision_pb2.GetDetectionsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetSegmenterNames(self, stream: 'grpclib.server.Stream[proto.api.service.vision.v1.vision_pb2.GetSegmenterNamesRequest, proto.api.service.vision.v1.vision_pb2.GetSegmenterNamesResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetSegmenterParameters(self, stream: 'grpclib.server.Stream[proto.api.service.vision.v1.vision_pb2.GetSegmenterParametersRequest, proto.api.service.vision.v1.vision_pb2.GetSegmenterParametersResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetObjectPointClouds(self, stream: 'grpclib.server.Stream[proto.api.service.vision.v1.vision_pb2.GetObjectPointCloudsRequest, proto.api.service.vision.v1.vision_pb2.GetObjectPointCloudsResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/proto.api.service.vision.v1.VisionService/GetDetectorNames': grpclib.const.Handler(self.GetDetectorNames, grpclib.const.Cardinality.UNARY_UNARY, proto.api.service.vision.v1.vision_pb2.GetDetectorNamesRequest, proto.api.service.vision.v1.vision_pb2.GetDetectorNamesResponse), '/proto.api.service.vision.v1.VisionService/AddDetector': grpclib.const.Handler(self.AddDetector, grpclib.const.Cardinality.UNARY_UNARY, proto.api.service.vision.v1.vision_pb2.AddDetectorRequest, proto.api.service.vision.v1.vision_pb2.AddDetectorResponse), '/proto.api.service.vision.v1.VisionService/GetDetectionsFromCamera': grpclib.const.Handler(self.GetDetectionsFromCamera, grpclib.const.Cardinality.UNARY_UNARY, proto.api.service.vision.v1.vision_pb2.GetDetectionsFromCameraRequest, proto.api.service.vision.v1.vision_pb2.GetDetectionsFromCameraResponse), '/proto.api.service.vision.v1.VisionService/GetDetections': grpclib.const.Handler(self.GetDetections, grpclib.const.Cardinality.UNARY_UNARY, proto.api.service.vision.v1.vision_pb2.GetDetectionsRequest, proto.api.service.vision.v1.vision_pb2.GetDetectionsResponse), '/proto.api.service.vision.v1.VisionService/GetSegmenterNames': grpclib.const.Handler(self.GetSegmenterNames, grpclib.const.Cardinality.UNARY_UNARY, proto.api.service.vision.v1.vision_pb2.GetSegmenterNamesRequest, proto.api.service.vision.v1.vision_pb2.GetSegmenterNamesResponse), '/proto.api.service.vision.v1.VisionService/GetSegmenterParameters': grpclib.const.Handler(self.GetSegmenterParameters, grpclib.const.Cardinality.UNARY_UNARY, proto.api.service.vision.v1.vision_pb2.GetSegmenterParametersRequest, proto.api.service.vision.v1.vision_pb2.GetSegmenterParametersResponse), '/proto.api.service.vision.v1.VisionService/GetObjectPointClouds': grpclib.const.Handler(self.GetObjectPointClouds, grpclib.const.Cardinality.UNARY_UNARY, proto.api.service.vision.v1.vision_pb2.GetObjectPointCloudsRequest, proto.api.service.vision.v1.vision_pb2.GetObjectPointCloudsResponse)}

class VisionServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.GetDetectorNames = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.service.vision.v1.VisionService/GetDetectorNames', proto.api.service.vision.v1.vision_pb2.GetDetectorNamesRequest, proto.api.service.vision.v1.vision_pb2.GetDetectorNamesResponse)
        self.AddDetector = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.service.vision.v1.VisionService/AddDetector', proto.api.service.vision.v1.vision_pb2.AddDetectorRequest, proto.api.service.vision.v1.vision_pb2.AddDetectorResponse)
        self.GetDetectionsFromCamera = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.service.vision.v1.VisionService/GetDetectionsFromCamera', proto.api.service.vision.v1.vision_pb2.GetDetectionsFromCameraRequest, proto.api.service.vision.v1.vision_pb2.GetDetectionsFromCameraResponse)
        self.GetDetections = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.service.vision.v1.VisionService/GetDetections', proto.api.service.vision.v1.vision_pb2.GetDetectionsRequest, proto.api.service.vision.v1.vision_pb2.GetDetectionsResponse)
        self.GetSegmenterNames = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.service.vision.v1.VisionService/GetSegmenterNames', proto.api.service.vision.v1.vision_pb2.GetSegmenterNamesRequest, proto.api.service.vision.v1.vision_pb2.GetSegmenterNamesResponse)
        self.GetSegmenterParameters = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.service.vision.v1.VisionService/GetSegmenterParameters', proto.api.service.vision.v1.vision_pb2.GetSegmenterParametersRequest, proto.api.service.vision.v1.vision_pb2.GetSegmenterParametersResponse)
        self.GetObjectPointClouds = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.service.vision.v1.VisionService/GetObjectPointClouds', proto.api.service.vision.v1.vision_pb2.GetObjectPointCloudsRequest, proto.api.service.vision.v1.vision_pb2.GetObjectPointCloudsResponse)