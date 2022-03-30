from io import BytesIO
from typing import Tuple

from grpclib.client import Channel
from PIL import Image
from viam.proto.api.component.camera import (CameraServiceStub,
                                             GetFrameRequest, GetFrameResponse,
                                             GetPointCloudRequest,
                                             GetPointCloudResponse)
from viam.utils import CameraMimeType

from .camera import Camera


class CameraClient(Camera):
    """
    gRPC client for the Camera component
    """

    def __init__(self, name: str, channel: Channel):
        self.client = CameraServiceStub(channel)
        super().__init__(name)

    async def get_frame(self) -> Image.Image:
        request = GetFrameRequest(
            name=self.name, mime_type=CameraMimeType.BEST.value)
        response: GetFrameResponse = await self.client.GetFrame(request)
        mimetype = CameraMimeType(response.mime_type)
        if mimetype == CameraMimeType.RAW:
            image = Image.frombytes(
                'RGBA',
                (response.width_px, response.height_px),
                response.image,
                'raw'
            )
            return image

        return Image.open(BytesIO(response.image), formats=['JPEG', 'PNG'])

    async def get_point_cloud(self) -> Tuple[bytes, str]:
        request = GetPointCloudRequest(
            name=self.name, mime_type=CameraMimeType.PCD.value)
        response: GetPointCloudResponse = \
            await self.client.GetPointCloud(request)
        return (response.point_cloud, response.mime_type)
