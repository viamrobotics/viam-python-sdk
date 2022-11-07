from io import BytesIO
from typing import Any, Dict, Optional, Tuple, Union

from grpclib.client import Channel
from PIL import Image

from viam.components.generic.client import do_command
from viam.media.video import CameraMimeType, RawImage, LIBRARY_SUPPORTED_FORMATS
from viam.proto.component.camera import (
    CameraServiceStub,
    GetImageRequest,
    GetImageResponse,
    GetPointCloudRequest,
    GetPointCloudResponse,
    GetPropertiesRequest,
    GetPropertiesResponse,
)

from .camera import Camera


class CameraClient(Camera):
    """
    gRPC client for the Camera component
    """

    def __init__(self, name: str, channel: Channel):
        self.channel = channel
        self.client = CameraServiceStub(channel)
        super().__init__(name)

    async def get_image(self, mime_type: str = CameraMimeType.PNG, *, timeout: Optional[float] = None) -> Union[Image.Image, RawImage]:
        request = GetImageRequest(name=self.name, mime_type=mime_type)
        response: GetImageResponse = await self.client.GetImage(request, timeout=timeout)
        _, is_lazy = CameraMimeType.from_lazy(request.mime_type)
        if is_lazy or not (CameraMimeType.is_supported(response.mime_type)):
            image = RawImage(response.image, response.mime_type)
            return image
        return Image.open(BytesIO(response.image), formats=LIBRARY_SUPPORTED_FORMATS)

    async def get_point_cloud(self, *, timeout: Optional[float] = None) -> Tuple[bytes, str]:
        request = GetPointCloudRequest(name=self.name, mime_type=CameraMimeType.PCD)
        response: GetPointCloudResponse = await self.client.GetPointCloud(request, timeout=timeout)
        return (response.point_cloud, response.mime_type)

    async def get_properties(self, *, timeout: Optional[float] = None) -> Camera.Properties:
        response: GetPropertiesResponse = await self.client.GetProperties(GetPropertiesRequest(name=self.name), timeout=timeout)
        return Camera.Properties(response.supports_pcd, response.intrinsic_parameters, response.distortion_parameters)

    async def do_command(self, command: Dict[str, Any], *, timeout: Optional[float] = None) -> Dict[str, Any]:
        return await do_command(self.channel, self.name, command, timeout=timeout)
