from io import BytesIO
from typing import Any, Dict, List, Mapping, Optional, Tuple, Union

from grpclib.client import Channel
from PIL import Image

from viam.media.video import LIBRARY_SUPPORTED_FORMATS, CameraMimeType, NamedImage
from viam.proto.common import DoCommandRequest, DoCommandResponse, Geometry, ResponseMetadata
from viam.proto.component.camera import (
    CameraServiceStub,
    GetImageRequest,
    GetImageResponse,
    GetImagesRequest,
    GetImagesResponse,
    GetPointCloudRequest,
    GetPointCloudResponse,
    GetPropertiesRequest,
)
from viam.resource.rpc_client_base import ReconfigurableResourceRPCClientBase
from viam.utils import ValueTypes, dict_to_struct, get_geometries, struct_to_dict

from . import Camera, RawImage


def get_image_from_response(data: bytes, response_mime_type: str, request_mime_type: str) -> Union[Image.Image, RawImage]:
    if not request_mime_type:
        request_mime_type = response_mime_type
    mime_type, is_lazy = CameraMimeType.from_lazy(request_mime_type)
    if is_lazy or mime_type._should_be_raw:
        image = RawImage(data=data, mime_type=response_mime_type)
        return image
    return Image.open(BytesIO(data), formats=LIBRARY_SUPPORTED_FORMATS)


class CameraClient(Camera, ReconfigurableResourceRPCClientBase):
    """
    gRPC client for the Camera component
    """

    def __init__(self, name: str, channel: Channel):
        self.channel = channel
        self.client = CameraServiceStub(channel)
        super().__init__(name)

    async def get_image(
        self,
        mime_type: str = "",
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
        **__,
    ) -> Union[Image.Image, RawImage]:
        if extra is None:
            extra = {}
        request = GetImageRequest(name=self.name, mime_type=mime_type, extra=dict_to_struct(extra))
        response: GetImageResponse = await self.client.GetImage(request, timeout=timeout)
        return get_image_from_response(response.image, response_mime_type=response.mime_type, request_mime_type=request.mime_type)

    async def get_images(
        self,
        *,
        timeout: Optional[float] = None,
        **__,
    ) -> Tuple[List[NamedImage], ResponseMetadata]:
        request = GetImagesRequest(name=self.name)
        response: GetImagesResponse = await self.client.GetImages(request, timeout=timeout)
        imgs = []
        for img_data in response.images:
            mime_type = CameraMimeType.from_proto(img_data.format)
            img = NamedImage(img_data.source_name, img_data.image, mime_type)
            imgs.append(img)
        resp_metadata: ResponseMetadata = response.response_metadata
        return imgs, resp_metadata

    async def get_point_cloud(
        self,
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
        **__,
    ) -> Tuple[bytes, str]:
        if extra is None:
            extra = {}
        request = GetPointCloudRequest(name=self.name, mime_type=CameraMimeType.PCD, extra=dict_to_struct(extra))
        response: GetPointCloudResponse = await self.client.GetPointCloud(request, timeout=timeout)
        return (response.point_cloud, response.mime_type)

    async def get_properties(
        self,
        *,
        timeout: Optional[float] = None,
        **__,
    ) -> Camera.Properties:
        return await self.client.GetProperties(GetPropertiesRequest(name=self.name), timeout=timeout)

    async def do_command(
        self,
        command: Mapping[str, ValueTypes],
        *,
        timeout: Optional[float] = None,
        **__,
    ) -> Mapping[str, ValueTypes]:
        request = DoCommandRequest(name=self.name, command=dict_to_struct(command))
        response: DoCommandResponse = await self.client.DoCommand(request, timeout=timeout)
        return struct_to_dict(response.result)

    async def get_geometries(self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None) -> List[Geometry]:
        return await get_geometries(self.client, self.name, extra, timeout)
