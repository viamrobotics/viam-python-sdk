import abc
import typing
import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server
import google.api.annotations_pb2
import google.api.httpbody_pb2
from ..... import proto
from ..... import proto

class CameraServiceBase(abc.ABC):

    @abc.abstractmethod
    async def GetFrame(self, stream: 'grpclib.server.Stream[proto.api.component.v1.camera_pb2.CameraServiceGetFrameRequest, proto.api.component.v1.camera_pb2.CameraServiceGetFrameResponse]') -> None:
        pass

    @abc.abstractmethod
    async def RenderFrame(self, stream: 'grpclib.server.Stream[proto.api.component.v1.camera_pb2.CameraServiceRenderFrameRequest, google.api.httpbody_pb2.HttpBody]') -> None:
        pass

    @abc.abstractmethod
    async def GetPointCloud(self, stream: 'grpclib.server.Stream[proto.api.component.v1.camera_pb2.CameraServiceGetPointCloudRequest, proto.api.component.v1.camera_pb2.CameraServiceGetPointCloudResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetObjectPointClouds(self, stream: 'grpclib.server.Stream[proto.api.component.v1.camera_pb2.CameraServiceGetObjectPointCloudsRequest, proto.api.component.v1.camera_pb2.CameraServiceGetObjectPointCloudsResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/proto.api.component.v1.CameraService/GetFrame': grpclib.const.Handler(self.GetFrame, grpclib.const.Cardinality.UNARY_UNARY, proto.api.component.v1.camera_pb2.CameraServiceGetFrameRequest, proto.api.component.v1.camera_pb2.CameraServiceGetFrameResponse), '/proto.api.component.v1.CameraService/RenderFrame': grpclib.const.Handler(self.RenderFrame, grpclib.const.Cardinality.UNARY_UNARY, proto.api.component.v1.camera_pb2.CameraServiceRenderFrameRequest, google.api.httpbody_pb2.HttpBody), '/proto.api.component.v1.CameraService/GetPointCloud': grpclib.const.Handler(self.GetPointCloud, grpclib.const.Cardinality.UNARY_UNARY, proto.api.component.v1.camera_pb2.CameraServiceGetPointCloudRequest, proto.api.component.v1.camera_pb2.CameraServiceGetPointCloudResponse), '/proto.api.component.v1.CameraService/GetObjectPointClouds': grpclib.const.Handler(self.GetObjectPointClouds, grpclib.const.Cardinality.UNARY_UNARY, proto.api.component.v1.camera_pb2.CameraServiceGetObjectPointCloudsRequest, proto.api.component.v1.camera_pb2.CameraServiceGetObjectPointCloudsResponse)}

class CameraServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.GetFrame = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.component.v1.CameraService/GetFrame', proto.api.component.v1.camera_pb2.CameraServiceGetFrameRequest, proto.api.component.v1.camera_pb2.CameraServiceGetFrameResponse)
        self.RenderFrame = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.component.v1.CameraService/RenderFrame', proto.api.component.v1.camera_pb2.CameraServiceRenderFrameRequest, google.api.httpbody_pb2.HttpBody)
        self.GetPointCloud = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.component.v1.CameraService/GetPointCloud', proto.api.component.v1.camera_pb2.CameraServiceGetPointCloudRequest, proto.api.component.v1.camera_pb2.CameraServiceGetPointCloudResponse)
        self.GetObjectPointClouds = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.component.v1.CameraService/GetObjectPointClouds', proto.api.component.v1.camera_pb2.CameraServiceGetObjectPointCloudsRequest, proto.api.component.v1.camera_pb2.CameraServiceGetObjectPointCloudsResponse)