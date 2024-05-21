from typing import Any, List, Mapping, Optional

from grpclib.client import Channel

from viam.errors import ViamError
from viam.media.video import CameraMimeType, ViamImage
from viam.proto.common import DoCommandRequest, DoCommandResponse, PointCloudObject
from viam.proto.service.vision import (
    CaptureAllFromCameraRequest,
    CaptureAllFromCameraResponse,
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
    GetPropertiesRequest,
    GetPropertiesResponse,
    VisionServiceStub,
)
from viam.resource.rpc_client_base import ReconfigurableResourceRPCClientBase
from viam.utils import ValueTypes, dict_to_struct, struct_to_dict

from .vision import CaptureAllResult, Vision


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

    async def capture_all_from_camera(
        self,
        camera_name: str,
        return_image: bool = False,
        return_classifications: bool = False,
        return_detections: bool = False,
        return_object_point_clouds: bool = False,
        *,
        extra: Optional[Mapping[str, Any]] = None,
        timeout: Optional[float] = None,
    ) -> CaptureAllResult:
        if extra is None:
            extra = {}
        request = CaptureAllFromCameraRequest(
            name=self.name,
            camera_name=camera_name,
            return_image=return_image,
            return_classifications=return_classifications,
            return_detections=return_detections,
            return_object_point_clouds=return_object_point_clouds,
            extra=dict_to_struct(extra),
        )
        response: CaptureAllFromCameraResponse = await self.client.CaptureAllFromCamera(request, timeout=timeout)
        result = CaptureAllResult()
        result.extra = struct_to_dict(response.extra)
        if return_image:
            mime_type = CameraMimeType.from_proto(response.image.format)
            img = ViamImage(response.image.image, mime_type)
            result.image = img
        if return_classifications:
            result.classifications = list(response.classifications)
        if return_detections:
            result.detections = list(response.detections)
        if return_object_point_clouds:
            result.objects = list(response.objects)
        return result

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
        image: ViamImage,
        *,
        extra: Optional[Mapping[str, Any]] = None,
        timeout: Optional[float] = None,
    ) -> List[Detection]:
        if extra is None:
            extra = {}
        mime_type = CameraMimeType.JPEG

        if image.width is None or image.height is None:
            raise ViamError(f"image {image} needs to have a specified width and height")
        else:
            request = GetDetectionsRequest(
                name=self.name,
                image=image.data,
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
        image: ViamImage,
        count: int,
        *,
        extra: Optional[Mapping[str, Any]] = None,
        timeout: Optional[float] = None,
    ) -> List[Classification]:
        if extra is None:
            extra = {}

        mime_type = CameraMimeType.JPEG
        if image.width is None or image.height is None:
            raise ViamError(f"image {image} needs to have a specified width and height")
        request = GetClassificationsRequest(
            name=self.name,
            image=image.data,
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

    async def get_properties(
        self,
        *,
        extra: Optional[Mapping[str, Any]] = None,
        timeout: Optional[float] = None,
    ) -> Vision.Properties:
        if extra is None:
            extra = {}
        request = GetPropertiesRequest(
            name=self.name,
            extra=dict_to_struct(extra),
        )
        response: GetPropertiesResponse = await self.client.GetProperties(request, timeout=timeout)
        return response

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
