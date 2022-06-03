from io import BytesIO

from google.api.httpbody_pb2 import HttpBody
from grpclib.server import Stream
from PIL.Image import Image
from viam.components.service_base import ComponentServiceBase
from viam.errors import ComponentNotFoundError
from viam.proto.api.component.camera import (CameraServiceBase,
                                             GetFrameRequest, GetFrameResponse,
                                             GetPointCloudRequest,
                                             GetPointCloudResponse,
                                             RenderFrameRequest)
from viam.components.types import CameraMimeType

from .camera import Camera


class CameraService(CameraServiceBase, ComponentServiceBase[Camera]):
    """
    gRPC Service for a generic Camera
    """

    RESOURCE_TYPE = Camera

    def _get_image_bytes(
        self,
        image: Image,
        mimetype: CameraMimeType
    ) -> bytes:
        if mimetype == CameraMimeType.RAW:
            return image.convert('RGBA').tobytes('raw', 'RGBA')
        elif mimetype == CameraMimeType.JPEG:
            buf = BytesIO()
            image.save(buf, format='JPEG')
            return buf.getvalue()
        elif mimetype == CameraMimeType.PNG:
            buf = BytesIO()
            image.save(buf, format='PNG')
            return buf.getvalue()
        else:
            raise ValueError(f'Cannot encode image to {mimetype}')

    async def GetFrame(
        self,
        stream: Stream[GetFrameRequest, GetFrameResponse]
    ) -> None:
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
                mimetype = CameraMimeType(request.mime_type or '')
            except ValueError:
                mimetype = CameraMimeType.RAW
            if mimetype == CameraMimeType.BEST:
                mimetype = CameraMimeType.RAW
            response = GetFrameResponse(
                mime_type=mimetype,
                width_px=image.width,
                height_px=image.height,
            )
            img_bytes = self._get_image_bytes(image, mimetype)
        finally:
            image.close()
        response.image = img_bytes
        await stream.send_message(response)

    async def RenderFrame(
        self,
        stream: Stream[RenderFrameRequest, HttpBody]
    ) -> None:
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
            img = self._get_image_bytes(await camera.get_frame(), mimetype)
        finally:
            image.close()
        response = HttpBody(data=img, content_type=mimetype)
        await stream.send_message(response)

    async def GetPointCloud(
        self,
        stream: Stream[GetPointCloudRequest, GetPointCloudResponse]
    ) -> None:
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
