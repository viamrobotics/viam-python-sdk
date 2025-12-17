from typing import Any, Dict, Mapping, Optional, Sequence, Tuple

from grpclib.client import Channel

from viam.media.video import CameraMimeType, NamedImage
from viam.proto.common import DoCommandRequest, DoCommandResponse, Geometry, ResponseMetadata
from viam.proto.component.camera import (
    CameraServiceStub,
    GetImagesRequest,
    GetImagesResponse,
    GetPointCloudRequest,
    GetPointCloudResponse,
    GetPropertiesRequest,
)
from viam.resource.rpc_client_base import ReconfigurableResourceRPCClientBase
from viam.utils import ValueTypes, dict_to_struct, get_geometries, struct_to_dict

from . import Camera


class CameraClient(Camera, ReconfigurableResourceRPCClientBase):
    """
    gRPC client for the Camera component
    """

    def __init__(self, name: str, channel: Channel):
        self.channel = channel
        self.client = CameraServiceStub(channel)
        super().__init__(name)

    async def get_images(
        self,
        *,
        filter_source_names: Optional[Sequence[str]] = None,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ) -> Tuple[Sequence[NamedImage], ResponseMetadata]:
        md = kwargs.get("metadata", self.Metadata()).proto
        request = GetImagesRequest(name=self.name, extra=dict_to_struct(extra), filter_source_names=filter_source_names)
        response: GetImagesResponse = await self.client.GetImages(request, timeout=timeout, metadata=md)
        imgs = []
        for img_data in response.images:
            mime_type = CameraMimeType.from_string(img_data.mime_type)
            img = NamedImage(img_data.source_name, img_data.image, mime_type)
            imgs.append(img)
        resp_metadata: ResponseMetadata = response.response_metadata
        return imgs, resp_metadata

    async def get_point_cloud(
        self,
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ) -> Tuple[bytes, str]:
        md = kwargs.get("metadata", self.Metadata()).proto
        request = GetPointCloudRequest(name=self.name, mime_type=CameraMimeType.PCD, extra=dict_to_struct(extra))
        response: GetPointCloudResponse = await self.client.GetPointCloud(request, timeout=timeout, metadata=md)
        return (response.point_cloud, response.mime_type)

    async def get_properties(
        self,
        *,
        timeout: Optional[float] = None,
        **kwargs,
    ) -> Camera.Properties:
        md = kwargs.get("metadata", self.Metadata()).proto
        return await self.client.GetProperties(GetPropertiesRequest(name=self.name), timeout=timeout, metadata=md)

    async def do_command(
        self,
        command: Mapping[str, ValueTypes],
        *,
        timeout: Optional[float] = None,
        **kwargs,
    ) -> Mapping[str, ValueTypes]:
        md = kwargs.get("metadata", self.Metadata()).proto
        request = DoCommandRequest(name=self.name, command=dict_to_struct(command))
        response: DoCommandResponse = await self.client.DoCommand(request, timeout=timeout, metadata=md)
        return struct_to_dict(response.result)

    async def get_geometries(
        self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs
    ) -> Sequence[Geometry]:
        md = kwargs.get("metadata", self.Metadata())
        return await get_geometries(self.client, self.name, extra, timeout, md)
