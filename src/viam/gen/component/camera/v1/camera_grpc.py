import abc
import typing
import grpclib.const
import grpclib.client
import grpclib.exceptions
if typing.TYPE_CHECKING:
    import grpclib.server
from .... import common
import google.api.annotations_pb2
import google.api.httpbody_pb2
import google.protobuf.struct_pb2
from .... import component

class CameraServiceBase(abc.ABC):

    @abc.abstractmethod
    async def GetImage(self, stream: 'grpclib.server.Stream[component.camera.v1.camera_pb2.GetImageRequest, component.camera.v1.camera_pb2.GetImageResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetImages(self, stream: 'grpclib.server.Stream[component.camera.v1.camera_pb2.GetImagesRequest, component.camera.v1.camera_pb2.GetImagesResponse]') -> None:
        pass

    @abc.abstractmethod
    async def RenderFrame(self, stream: 'grpclib.server.Stream[component.camera.v1.camera_pb2.RenderFrameRequest, google.api.httpbody_pb2.HttpBody]') -> None:
        pass

    @abc.abstractmethod
    async def GetPointCloud(self, stream: 'grpclib.server.Stream[component.camera.v1.camera_pb2.GetPointCloudRequest, component.camera.v1.camera_pb2.GetPointCloudResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetProperties(self, stream: 'grpclib.server.Stream[component.camera.v1.camera_pb2.GetPropertiesRequest, component.camera.v1.camera_pb2.GetPropertiesResponse]') -> None:
        pass

    @abc.abstractmethod
    async def DoCommand(self, stream: 'grpclib.server.Stream[common.v1.common_pb2.DoCommandRequest, common.v1.common_pb2.DoCommandResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetGeometries(self, stream: 'grpclib.server.Stream[common.v1.common_pb2.GetGeometriesRequest, common.v1.common_pb2.GetGeometriesResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/viam.component.camera.v1.CameraService/GetImage': grpclib.const.Handler(self.GetImage, grpclib.const.Cardinality.UNARY_UNARY, component.camera.v1.camera_pb2.GetImageRequest, component.camera.v1.camera_pb2.GetImageResponse), '/viam.component.camera.v1.CameraService/GetImages': grpclib.const.Handler(self.GetImages, grpclib.const.Cardinality.UNARY_UNARY, component.camera.v1.camera_pb2.GetImagesRequest, component.camera.v1.camera_pb2.GetImagesResponse), '/viam.component.camera.v1.CameraService/RenderFrame': grpclib.const.Handler(self.RenderFrame, grpclib.const.Cardinality.UNARY_UNARY, component.camera.v1.camera_pb2.RenderFrameRequest, google.api.httpbody_pb2.HttpBody), '/viam.component.camera.v1.CameraService/GetPointCloud': grpclib.const.Handler(self.GetPointCloud, grpclib.const.Cardinality.UNARY_UNARY, component.camera.v1.camera_pb2.GetPointCloudRequest, component.camera.v1.camera_pb2.GetPointCloudResponse), '/viam.component.camera.v1.CameraService/GetProperties': grpclib.const.Handler(self.GetProperties, grpclib.const.Cardinality.UNARY_UNARY, component.camera.v1.camera_pb2.GetPropertiesRequest, component.camera.v1.camera_pb2.GetPropertiesResponse), '/viam.component.camera.v1.CameraService/DoCommand': grpclib.const.Handler(self.DoCommand, grpclib.const.Cardinality.UNARY_UNARY, common.v1.common_pb2.DoCommandRequest, common.v1.common_pb2.DoCommandResponse), '/viam.component.camera.v1.CameraService/GetGeometries': grpclib.const.Handler(self.GetGeometries, grpclib.const.Cardinality.UNARY_UNARY, common.v1.common_pb2.GetGeometriesRequest, common.v1.common_pb2.GetGeometriesResponse)}

class UnimplementedCameraServiceBase(CameraServiceBase):

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

class CameraServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.GetImage = grpclib.client.UnaryUnaryMethod(channel, '/viam.component.camera.v1.CameraService/GetImage', component.camera.v1.camera_pb2.GetImageRequest, component.camera.v1.camera_pb2.GetImageResponse)
        self.GetImages = grpclib.client.UnaryUnaryMethod(channel, '/viam.component.camera.v1.CameraService/GetImages', component.camera.v1.camera_pb2.GetImagesRequest, component.camera.v1.camera_pb2.GetImagesResponse)
        self.RenderFrame = grpclib.client.UnaryUnaryMethod(channel, '/viam.component.camera.v1.CameraService/RenderFrame', component.camera.v1.camera_pb2.RenderFrameRequest, google.api.httpbody_pb2.HttpBody)
        self.GetPointCloud = grpclib.client.UnaryUnaryMethod(channel, '/viam.component.camera.v1.CameraService/GetPointCloud', component.camera.v1.camera_pb2.GetPointCloudRequest, component.camera.v1.camera_pb2.GetPointCloudResponse)
        self.GetProperties = grpclib.client.UnaryUnaryMethod(channel, '/viam.component.camera.v1.CameraService/GetProperties', component.camera.v1.camera_pb2.GetPropertiesRequest, component.camera.v1.camera_pb2.GetPropertiesResponse)
        self.DoCommand = grpclib.client.UnaryUnaryMethod(channel, '/viam.component.camera.v1.CameraService/DoCommand', common.v1.common_pb2.DoCommandRequest, common.v1.common_pb2.DoCommandResponse)
        self.GetGeometries = grpclib.client.UnaryUnaryMethod(channel, '/viam.component.camera.v1.CameraService/GetGeometries', common.v1.common_pb2.GetGeometriesRequest, common.v1.common_pb2.GetGeometriesResponse)