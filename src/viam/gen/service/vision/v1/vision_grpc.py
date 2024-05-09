import abc
import typing
import grpclib.const
import grpclib.client
import grpclib.exceptions
if typing.TYPE_CHECKING:
    import grpclib.server
from .... import common
from .... import component
import google.api.annotations_pb2
import google.protobuf.struct_pb2
from .... import service

class VisionServiceBase(abc.ABC):

    @abc.abstractmethod
    async def GetDetectionsFromCamera(self, stream: 'grpclib.server.Stream[service.vision.v1.vision_pb2.GetDetectionsFromCameraRequest, service.vision.v1.vision_pb2.GetDetectionsFromCameraResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetDetections(self, stream: 'grpclib.server.Stream[service.vision.v1.vision_pb2.GetDetectionsRequest, service.vision.v1.vision_pb2.GetDetectionsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetClassificationsFromCamera(self, stream: 'grpclib.server.Stream[service.vision.v1.vision_pb2.GetClassificationsFromCameraRequest, service.vision.v1.vision_pb2.GetClassificationsFromCameraResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetClassifications(self, stream: 'grpclib.server.Stream[service.vision.v1.vision_pb2.GetClassificationsRequest, service.vision.v1.vision_pb2.GetClassificationsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetObjectPointClouds(self, stream: 'grpclib.server.Stream[service.vision.v1.vision_pb2.GetObjectPointCloudsRequest, service.vision.v1.vision_pb2.GetObjectPointCloudsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetProperties(self, stream: 'grpclib.server.Stream[service.vision.v1.vision_pb2.GetPropertiesRequest, service.vision.v1.vision_pb2.GetPropertiesResponse]') -> None:
        pass

    @abc.abstractmethod
    async def CaptureAllFromCamera(self, stream: 'grpclib.server.Stream[service.vision.v1.vision_pb2.CaptureAllFromCameraRequest, service.vision.v1.vision_pb2.CaptureAllFromCameraResponse]') -> None:
        pass

    @abc.abstractmethod
    async def DoCommand(self, stream: 'grpclib.server.Stream[common.v1.common_pb2.DoCommandRequest, common.v1.common_pb2.DoCommandResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/viam.service.vision.v1.VisionService/GetDetectionsFromCamera': grpclib.const.Handler(self.GetDetectionsFromCamera, grpclib.const.Cardinality.UNARY_UNARY, service.vision.v1.vision_pb2.GetDetectionsFromCameraRequest, service.vision.v1.vision_pb2.GetDetectionsFromCameraResponse), '/viam.service.vision.v1.VisionService/GetDetections': grpclib.const.Handler(self.GetDetections, grpclib.const.Cardinality.UNARY_UNARY, service.vision.v1.vision_pb2.GetDetectionsRequest, service.vision.v1.vision_pb2.GetDetectionsResponse), '/viam.service.vision.v1.VisionService/GetClassificationsFromCamera': grpclib.const.Handler(self.GetClassificationsFromCamera, grpclib.const.Cardinality.UNARY_UNARY, service.vision.v1.vision_pb2.GetClassificationsFromCameraRequest, service.vision.v1.vision_pb2.GetClassificationsFromCameraResponse), '/viam.service.vision.v1.VisionService/GetClassifications': grpclib.const.Handler(self.GetClassifications, grpclib.const.Cardinality.UNARY_UNARY, service.vision.v1.vision_pb2.GetClassificationsRequest, service.vision.v1.vision_pb2.GetClassificationsResponse), '/viam.service.vision.v1.VisionService/GetObjectPointClouds': grpclib.const.Handler(self.GetObjectPointClouds, grpclib.const.Cardinality.UNARY_UNARY, service.vision.v1.vision_pb2.GetObjectPointCloudsRequest, service.vision.v1.vision_pb2.GetObjectPointCloudsResponse), '/viam.service.vision.v1.VisionService/GetProperties': grpclib.const.Handler(self.GetProperties, grpclib.const.Cardinality.UNARY_UNARY, service.vision.v1.vision_pb2.GetPropertiesRequest, service.vision.v1.vision_pb2.GetPropertiesResponse), '/viam.service.vision.v1.VisionService/CaptureAllFromCamera': grpclib.const.Handler(self.CaptureAllFromCamera, grpclib.const.Cardinality.UNARY_UNARY, service.vision.v1.vision_pb2.CaptureAllFromCameraRequest, service.vision.v1.vision_pb2.CaptureAllFromCameraResponse), '/viam.service.vision.v1.VisionService/DoCommand': grpclib.const.Handler(self.DoCommand, grpclib.const.Cardinality.UNARY_UNARY, common.v1.common_pb2.DoCommandRequest, common.v1.common_pb2.DoCommandResponse)}

class UnimplementedVisionServiceBase(VisionServiceBase):

    async def GetDetectionsFromCamera(self, stream: 'grpclib.server.Stream[service.vision.v1.vision_pb2.GetDetectionsFromCameraRequest, service.vision.v1.vision_pb2.GetDetectionsFromCameraResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def GetDetections(self, stream: 'grpclib.server.Stream[service.vision.v1.vision_pb2.GetDetectionsRequest, service.vision.v1.vision_pb2.GetDetectionsResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def GetClassificationsFromCamera(self, stream: 'grpclib.server.Stream[service.vision.v1.vision_pb2.GetClassificationsFromCameraRequest, service.vision.v1.vision_pb2.GetClassificationsFromCameraResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def GetClassifications(self, stream: 'grpclib.server.Stream[service.vision.v1.vision_pb2.GetClassificationsRequest, service.vision.v1.vision_pb2.GetClassificationsResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def GetObjectPointClouds(self, stream: 'grpclib.server.Stream[service.vision.v1.vision_pb2.GetObjectPointCloudsRequest, service.vision.v1.vision_pb2.GetObjectPointCloudsResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def GetProperties(self, stream: 'grpclib.server.Stream[service.vision.v1.vision_pb2.GetPropertiesRequest, service.vision.v1.vision_pb2.GetPropertiesResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def CaptureAllFromCamera(self, stream: 'grpclib.server.Stream[service.vision.v1.vision_pb2.CaptureAllFromCameraRequest, service.vision.v1.vision_pb2.CaptureAllFromCameraResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def DoCommand(self, stream: 'grpclib.server.Stream[common.v1.common_pb2.DoCommandRequest, common.v1.common_pb2.DoCommandResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

class VisionServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.GetDetectionsFromCamera = grpclib.client.UnaryUnaryMethod(channel, '/viam.service.vision.v1.VisionService/GetDetectionsFromCamera', service.vision.v1.vision_pb2.GetDetectionsFromCameraRequest, service.vision.v1.vision_pb2.GetDetectionsFromCameraResponse)
        self.GetDetections = grpclib.client.UnaryUnaryMethod(channel, '/viam.service.vision.v1.VisionService/GetDetections', service.vision.v1.vision_pb2.GetDetectionsRequest, service.vision.v1.vision_pb2.GetDetectionsResponse)
        self.GetClassificationsFromCamera = grpclib.client.UnaryUnaryMethod(channel, '/viam.service.vision.v1.VisionService/GetClassificationsFromCamera', service.vision.v1.vision_pb2.GetClassificationsFromCameraRequest, service.vision.v1.vision_pb2.GetClassificationsFromCameraResponse)
        self.GetClassifications = grpclib.client.UnaryUnaryMethod(channel, '/viam.service.vision.v1.VisionService/GetClassifications', service.vision.v1.vision_pb2.GetClassificationsRequest, service.vision.v1.vision_pb2.GetClassificationsResponse)
        self.GetObjectPointClouds = grpclib.client.UnaryUnaryMethod(channel, '/viam.service.vision.v1.VisionService/GetObjectPointClouds', service.vision.v1.vision_pb2.GetObjectPointCloudsRequest, service.vision.v1.vision_pb2.GetObjectPointCloudsResponse)
        self.GetProperties = grpclib.client.UnaryUnaryMethod(channel, '/viam.service.vision.v1.VisionService/GetProperties', service.vision.v1.vision_pb2.GetPropertiesRequest, service.vision.v1.vision_pb2.GetPropertiesResponse)
        self.CaptureAllFromCamera = grpclib.client.UnaryUnaryMethod(channel, '/viam.service.vision.v1.VisionService/CaptureAllFromCamera', service.vision.v1.vision_pb2.CaptureAllFromCameraRequest, service.vision.v1.vision_pb2.CaptureAllFromCameraResponse)
        self.DoCommand = grpclib.client.UnaryUnaryMethod(channel, '/viam.service.vision.v1.VisionService/DoCommand', common.v1.common_pb2.DoCommandRequest, common.v1.common_pb2.DoCommandResponse)