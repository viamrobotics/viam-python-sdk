from google.api.httpbody_pb2 import HttpBody
from grpclib.server import Stream

from viam.components.service_base import ComponentServiceBase
from viam.components.types import CameraMimeType, RawImage
from viam.errors import ComponentNotFoundError
from viam.proto.api.component.camera import (
    CameraServiceBase,
    GetFrameRequest,
    GetFrameResponse,
    GetPointCloudRequest,
    GetPointCloudResponse,
    GetPropertiesRequest,
    GetPropertiesResponse,
    RenderFrameRequest,
)

from .camera import Camera


class CameraService(CameraServiceBase, ComponentServiceBase[Camera]):
    """
    gRPC Service for a generic Camera
    """

    RESOURCE_TYPE = Camera

    async def GetFrame(self, stream: Stream[GetFrameRequest, GetFrameResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        try:
            camera = self.get_component(name)
        except ComponentNotFoundError as e:
            raise e.grpc_error
        image = await camera.get_frame()
        try:
            try:
                mimetype = CameraMimeType(request.mime_type)
            except ValueError:
                mimetype = CameraMimeType.RAW
            response = GetFrameResponse(
                mime_type=image.mime_type if isinstance(image, RawImage) else mimetype,
                width_px=image.width,
                height_px=image.height,
            )
            img_bytes = mimetype.encode_image(image)
        finally:
            image.close()
        response.image = img_bytes
        await stream.send_message(response)

    async def RenderFrame(self, stream: Stream[RenderFrameRequest, HttpBody]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        try:
            camera = self.get_component(name)
        except ComponentNotFoundError as e:
            raise e.grpc_error
        mimetype = CameraMimeType(request.mime_type)
        if not mimetype:
            mimetype = CameraMimeType.JPEG
        image = await camera.get_frame()
        try:
            img = mimetype.encode_image(await camera.get_frame())
        finally:
            image.close()
        response = HttpBody(data=img, content_type=mimetype)
        await stream.send_message(response)

    async def GetPointCloud(self, stream: Stream[GetPointCloudRequest, GetPointCloudResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        try:
            camera = self.get_component(name)
        except ComponentNotFoundError as e:
            raise e.grpc_error
        pc, mimetype = await camera.get_point_cloud()
        response = GetPointCloudResponse(mime_type=mimetype, point_cloud=pc)
        await stream.send_message(response)

    async def GetProperties(self, stream: Stream[GetPropertiesRequest, GetPropertiesResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        try:
            camera = self.get_component(name)
        except ComponentNotFoundError as e:
            raise e.grpc_error
        properties = await camera.get_properties()
        response = GetPropertiesResponse(intrinsic_parameters=properties)
        await stream.send_message(response)
