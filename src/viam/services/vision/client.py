from io import BytesIO
from typing import Any, List, Mapping, Optional, Union

from grpclib.client import Channel

from viam.media.viam_rgba_plugin import Image
from viam.media.video import CameraMimeType, RawImage
from viam.proto.common import DoCommandRequest, DoCommandResponse, PointCloudObject
from viam.proto.service.vision import (
    Classification,
    Detection,
    GetClassificationsFromCameraRequest,
    GetClassificationsFromCameraResponse,
    GetClassificationsRequest,
    GetClassificationsResponse,
    GetDetectionsFromCameraRequest,
    GetDetectionsFromCameraResponse,
    GetDetectionsRequest,
    GetDetectionsResponse,
    GetObjectPointCloudsRequest,
    GetObjectPointCloudsResponse,
    VisionServiceStub,
)
from viam.resource.rpc_client_base import ReconfigurableResourceRPCClientBase
from viam.utils import ValueTypes, dict_to_struct, struct_to_dict

from .vision import Vision


class VisionClient(Vision, ReconfigurableResourceRPCClientBase):
    """
    Connect to the Vision service, which allows you to access various computer vision algorithms
    (like detection, segmentation, tracking, etc) that usually only require a camera or image input.
    """

    client: VisionServiceStub

    def __init__(self, name: str, channel: Channel):
        super().__init__(name)
        self.channel = channel
        self.client = VisionServiceStub(channel)

    async def get_detections_from_camera(
        self,
        camera_name: str,
        *,
        extra: Optional[Mapping[str, Any]] = None,
        timeout: Optional[float] = None,
    ) -> List[Detection]:
        if extra is None:
            extra = {}
        request = GetDetectionsFromCameraRequest(name=self.name, camera_name=camera_name, extra=dict_to_struct(extra))
        response: GetDetectionsFromCameraResponse = await self.client.GetDetectionsFromCamera(request, timeout=timeout)
        return list(response.detections)

    async def get_detections(
        self,
        image: Union[Image.Image, RawImage],
        *,
        extra: Optional[Mapping[str, Any]] = None,
        timeout: Optional[float] = None,
    ) -> List[Detection]:
        if extra is None:
            extra = {}
        mime_type = CameraMimeType.JPEG
        if isinstance(image, RawImage):
            image = Image.open(BytesIO(image.data), formats=[mime_type.name])

        request = GetDetectionsRequest(
            name=self.name,
            image=mime_type.encode_image(image),
            width=image.width,
            height=image.height,
            mime_type=mime_type,
            extra=dict_to_struct(extra),
        )
        response: GetDetectionsResponse = await self.client.GetDetections(request, timeout=timeout)
        return list(response.detections)

    async def get_classifications_from_camera(
        self,
        camera_name: str,
        count: int,
        *,
        extra: Optional[Mapping[str, Any]] = None,
        timeout: Optional[float] = None,
    ) -> List[Classification]:
        if extra is None:
            extra = {}
        request = GetClassificationsFromCameraRequest(name=self.name, camera_name=camera_name, n=count, extra=dict_to_struct(extra))
        response: GetClassificationsFromCameraResponse = await self.client.GetClassificationsFromCamera(request, timeout=timeout)
        return list(response.classifications)

    async def get_classifications(
        self,
        image: Union[Image.Image, RawImage],
        count: int,
        *,
        extra: Optional[Mapping[str, Any]] = None,
        timeout: Optional[float] = None,
    ) -> List[Classification]:
        if extra is None:
            extra = {}
        mime_type = CameraMimeType.JPEG
        if isinstance(image, RawImage):
            image = Image.open(BytesIO(image.data), formats=[mime_type.name])

        request = GetClassificationsRequest(
            name=self.name,
            image=mime_type.encode_image(image),
            width=image.width,
            height=image.height,
            mime_type=mime_type,
            n=count,
            extra=dict_to_struct(extra),
        )
        response: GetClassificationsResponse = await self.client.GetClassifications(request, timeout=timeout)
        return list(response.classifications)

    async def get_object_point_clouds(
        self,
        camera_name: str,
        *,
        extra: Optional[Mapping[str, Any]] = None,
        timeout: Optional[float] = None,
    ) -> List[PointCloudObject]:
        if extra is None:
            extra = {}
        request = GetObjectPointCloudsRequest(
            name=self.name,
            camera_name=camera_name,
            mime_type=CameraMimeType.PCD,
            extra=dict_to_struct(extra),
        )
        response: GetObjectPointCloudsResponse = await self.client.GetObjectPointClouds(request, timeout=timeout)
        return list(response.objects)

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
