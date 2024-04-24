import abc
import typing
import grpclib.const
import grpclib.exceptions
if typing.TYPE_CHECKING:
    import grpclib.server
from .... import common
import google.api.annotations_pb2
import google.protobuf.struct_pb2
from .... import service
from .vision_grpc import VisionServiceBase as _VisionServiceBase

class UnimplementedVisionServiceBase(_VisionServiceBase):

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

    async def DoCommand(self, stream: 'grpclib.server.Stream[common.v1.common_pb2.DoCommandRequest, common.v1.common_pb2.DoCommandResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)