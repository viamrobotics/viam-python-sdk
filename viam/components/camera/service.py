from typing import final
from google.api.httpbody_pb2 import HttpBody
from grpclib.server import Stream
from viam.components.service_base import ComponentServiceBase
from viam.errors import ComponentNotFoundError
from viam.proto.api.component.camera import (CameraServiceBase,
                                             GetFrameRequest, GetFrameResponse,
                                             GetPointCloudRequest,
                                             GetPointCloudResponse,
                                             RenderFrameRequest)

from .camera import Camera


class SensorService(CameraServiceBase, ComponentServiceBase[Camera]):
    """
    gRPC Service for a generic Camera
    """

    RESOURCE_TYPE = Camera

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
            raise e.grpc_error()
        image, release = await camera.next()
        try:
            mimetype = request.mime_type
            width = image.width
            height = image.height
            response = GetFrameResponse(
                mime_type=mimetype,
                width_px=width,
                height_px=height,
            )
            await stream.send_message(response)

        finally:
            if release:
                release()

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
            raise e.grpc_error()

        response = HttpBody()
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
            raise e.grpc_error()

        response = GetPointCloudResponse()
        await stream.send_message(response)
