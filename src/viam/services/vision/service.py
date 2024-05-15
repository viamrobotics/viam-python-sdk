from io import BytesIO

from grpclib.server import Stream
from PIL import Image as PILImage

from viam.media.video import LIBRARY_SUPPORTED_FORMATS, CameraMimeType, RawImage
from viam.proto.common import DoCommandRequest, DoCommandResponse
from viam.proto.component.camera import Image
from viam.proto.service.vision import (
    CaptureAllFromCameraRequest,
    CaptureAllFromCameraResponse,
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
    UnimplementedVisionServiceBase,
)
from viam.resource.rpc_service_base import ResourceRPCServiceBase
from viam.utils import dict_to_struct, struct_to_dict

from .vision import Vision, CaptureAllRequest


class VisionRPCService(UnimplementedVisionServiceBase, ResourceRPCServiceBase):
    """
    gRPC service for a Vision service
    """

    RESOURCE_TYPE = Vision

    async def CaptureAllFromCamera(self, stream: Stream[CaptureAllFromCameraRequest, CaptureAllFromCameraResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        vision = self.get_resource(request.name)
        capture_request = CaptureAllRequest(
            request.return_image,
            request.return_classifications,
            request.return_detections,
            request.return_object_point_clouds,
        )
        extra = struct_to_dict(request.extra)
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        result = await vision.capture_all_from_camera(request.camera_name, capture_request, extra=extra, timeout=timeout)
        img = None
        if result.image is not None:
            try:
                fmt = result.image.mime_type.to_proto()
                img_bytes = result.image.data
                img = Image(source_name=request.name, format=fmt, image=img_bytes)
            finally:
                result.image.close()
        response = CaptureAllFromCameraResponse(
            image=img,
            detections=result.detections,
            classifications=result.classifications,
            objects=result.objects,
            extra=dict_to_struct(result.extra),
        )
        await stream.send_message(response)

    async def GetDetectionsFromCamera(self, stream: Stream[GetDetectionsFromCameraRequest, GetDetectionsFromCameraResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        vision = self.get_resource(request.name)
        extra = struct_to_dict(request.extra)
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        result = await vision.get_detections_from_camera(request.camera_name, extra=extra, timeout=timeout)
        response = GetDetectionsFromCameraResponse(detections=result)
        await stream.send_message(response)

    async def GetDetections(self, stream: Stream[GetDetectionsRequest, GetDetectionsResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        vision = self.get_resource(request.name)
        extra = struct_to_dict(request.extra)
        timeout = stream.deadline.time_remaining() if stream.deadline else None

        mime_type, is_lazy = CameraMimeType.from_lazy(request.mime_type)
        if is_lazy or not (CameraMimeType.is_supported(mime_type)):
            image = RawImage(request.image, request.mime_type)
        else:
            image = PILImage.open(BytesIO(request.image), formats=LIBRARY_SUPPORTED_FORMATS)

        result = await vision.get_detections(image, extra=extra, timeout=timeout)
        response = GetDetectionsResponse(detections=result)
        await stream.send_message(response)

    async def GetClassificationsFromCamera(
        self, stream: Stream[GetClassificationsFromCameraRequest, GetClassificationsFromCameraResponse]
    ) -> None:
        request = await stream.recv_message()
        assert request is not None
        vision = self.get_resource(request.name)
        extra = struct_to_dict(request.extra)
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        result = await vision.get_classifications_from_camera(request.camera_name, request.n, extra=extra, timeout=timeout)
        response = GetClassificationsFromCameraResponse(classifications=result)
        await stream.send_message(response)

    async def GetClassifications(self, stream: Stream[GetClassificationsRequest, GetClassificationsResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        vision = self.get_resource(request.name)
        extra = struct_to_dict(request.extra)
        timeout = stream.deadline.time_remaining() if stream.deadline else None

        mime_type, is_lazy = CameraMimeType.from_lazy(request.mime_type)
        if is_lazy or not (CameraMimeType.is_supported(mime_type)):
            image = RawImage(request.image, request.mime_type)
        else:
            image = PILImage.open(BytesIO(request.image), formats=LIBRARY_SUPPORTED_FORMATS)

        result = await vision.get_classifications(image, request.n, extra=extra, timeout=timeout)
        response = GetClassificationsResponse(classifications=result)
        await stream.send_message(response)

    async def GetObjectPointClouds(self, stream: Stream[GetObjectPointCloudsRequest, GetObjectPointCloudsResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        vision = self.get_resource(request.name)
        extra = struct_to_dict(request.extra)
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        result = await vision.get_object_point_clouds(request.camera_name, extra=extra, timeout=timeout)
        response = GetObjectPointCloudsResponse(mime_type=CameraMimeType.PCD.value, objects=result)
        await stream.send_message(response)

    async def GetProperties(self, stream: Stream[GetPropertiesRequest, GetPropertiesResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        vision = self.get_resource(name)
        extra = struct_to_dict(request.extra)
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        properties = await vision.get_properties(extra=extra, timeout=timeout)
        response = GetPropertiesResponse(
            classifications_supported=properties.classifications_supported,
            detections_supported=properties.detections_supported,
            object_point_clouds_supported=properties.object_point_clouds_supported,
        )
        await stream.send_message(response)

    async def DoCommand(self, stream: Stream[DoCommandRequest, DoCommandResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        vision = self.get_resource(request.name)
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        result = await vision.do_command(struct_to_dict(request.command), timeout=timeout)
        await stream.send_message(DoCommandResponse(result=dict_to_struct(result)))
