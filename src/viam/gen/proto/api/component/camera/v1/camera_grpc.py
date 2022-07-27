import abc
import typing
import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server
import google.api.annotations_pb2
import google.api.httpbody_pb2
from ...... import proto

class CameraServiceBase(abc.ABC):

    @abc.abstractmethod
    async def GetFrame(self, stream: 'grpclib.server.Stream[proto.api.component.camera.v1.camera_pb2.GetFrameRequest, proto.api.component.camera.v1.camera_pb2.GetFrameResponse]') -> None:
        pass

    @abc.abstractmethod
    async def RenderFrame(self, stream: 'grpclib.server.Stream[proto.api.component.camera.v1.camera_pb2.RenderFrameRequest, google.api.httpbody_pb2.HttpBody]') -> None:
        pass

    @abc.abstractmethod
    async def GetPointCloud(self, stream: 'grpclib.server.Stream[proto.api.component.camera.v1.camera_pb2.GetPointCloudRequest, proto.api.component.camera.v1.camera_pb2.GetPointCloudResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetProperties(self, stream: 'grpclib.server.Stream[proto.api.component.camera.v1.camera_pb2.GetPropertiesRequest, proto.api.component.camera.v1.camera_pb2.GetPropertiesResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/proto.api.component.camera.v1.CameraService/GetFrame': grpclib.const.Handler(self.GetFrame, grpclib.const.Cardinality.UNARY_UNARY, proto.api.component.camera.v1.camera_pb2.GetFrameRequest, proto.api.component.camera.v1.camera_pb2.GetFrameResponse), '/proto.api.component.camera.v1.CameraService/RenderFrame': grpclib.const.Handler(self.RenderFrame, grpclib.const.Cardinality.UNARY_UNARY, proto.api.component.camera.v1.camera_pb2.RenderFrameRequest, google.api.httpbody_pb2.HttpBody), '/proto.api.component.camera.v1.CameraService/GetPointCloud': grpclib.const.Handler(self.GetPointCloud, grpclib.const.Cardinality.UNARY_UNARY, proto.api.component.camera.v1.camera_pb2.GetPointCloudRequest, proto.api.component.camera.v1.camera_pb2.GetPointCloudResponse), '/proto.api.component.camera.v1.CameraService/GetProperties': grpclib.const.Handler(self.GetProperties, grpclib.const.Cardinality.UNARY_UNARY, proto.api.component.camera.v1.camera_pb2.GetPropertiesRequest, proto.api.component.camera.v1.camera_pb2.GetPropertiesResponse)}

class CameraServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.GetFrame = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.component.camera.v1.CameraService/GetFrame', proto.api.component.camera.v1.camera_pb2.GetFrameRequest, proto.api.component.camera.v1.camera_pb2.GetFrameResponse)
        self.RenderFrame = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.component.camera.v1.CameraService/RenderFrame', proto.api.component.camera.v1.camera_pb2.RenderFrameRequest, google.api.httpbody_pb2.HttpBody)
        self.GetPointCloud = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.component.camera.v1.CameraService/GetPointCloud', proto.api.component.camera.v1.camera_pb2.GetPointCloudRequest, proto.api.component.camera.v1.camera_pb2.GetPointCloudResponse)
        self.GetProperties = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.component.camera.v1.CameraService/GetProperties', proto.api.component.camera.v1.camera_pb2.GetPropertiesRequest, proto.api.component.camera.v1.camera_pb2.GetPropertiesResponse)