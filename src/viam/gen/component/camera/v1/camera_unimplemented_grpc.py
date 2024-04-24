import abc
import typing
import grpclib.const
import grpclib.exceptions
if typing.TYPE_CHECKING:
    import grpclib.server
from .... import common
import google.api.annotations_pb2
import google.api.httpbody_pb2
import google.protobuf.struct_pb2
from .... import component
from .camera_grpc import CameraServiceBase as _CameraServiceBase

class UnimplementedCameraServiceBase(_CameraServiceBase):

    async def GetImage(self, stream: 'grpclib.server.Stream[component.camera.v1.camera_pb2.GetImageRequest, component.camera.v1.camera_pb2.GetImageResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def GetImages(self, stream: 'grpclib.server.Stream[component.camera.v1.camera_pb2.GetImagesRequest, component.camera.v1.camera_pb2.GetImagesResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def RenderFrame(self, stream: 'grpclib.server.Stream[component.camera.v1.camera_pb2.RenderFrameRequest, google.api.httpbody_pb2.HttpBody]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def GetPointCloud(self, stream: 'grpclib.server.Stream[component.camera.v1.camera_pb2.GetPointCloudRequest, component.camera.v1.camera_pb2.GetPointCloudResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def GetProperties(self, stream: 'grpclib.server.Stream[component.camera.v1.camera_pb2.GetPropertiesRequest, component.camera.v1.camera_pb2.GetPropertiesResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def DoCommand(self, stream: 'grpclib.server.Stream[common.v1.common_pb2.DoCommandRequest, common.v1.common_pb2.DoCommandResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def GetGeometries(self, stream: 'grpclib.server.Stream[common.v1.common_pb2.GetGeometriesRequest, common.v1.common_pb2.GetGeometriesResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)