from io import BytesIO
from typing import Any, Final, List, Mapping, Optional, Union

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
from viam.resource.types import RESOURCE_NAMESPACE_RDK, RESOURCE_TYPE_SERVICE, Subtype
from viam.services.service_client_base import ServiceClientBase
from viam.utils import ValueTypes, dict_to_struct, struct_to_dict


class VisionServiceClient(ServiceClientBase, ReconfigurableResourceRPCClientBase):
    """
    Connect to the Vision service, which allows you to access various computer vision algorithms
    (like detection, segmentation, tracking, etc) that usually only require a camera or image input.
    """

    SUBTYPE: Final = Subtype(RESOURCE_NAMESPACE_RDK, RESOURCE_TYPE_SERVICE, "vision")

    def __init__(self, name: str, channel: Channel):
        super().__init__(name, channel)
        self.client = VisionServiceStub(channel)

    async def get_detections_from_camera(
        self, camera_name: str, *, extra: Optional[Mapping[str, Any]] = None, timeout: Optional[float] = None
    ) -> List[Detection]:
        """Get a list of detections in the next image given a camera and a detector

        Args:
            camera_name (str): The name of the camera to use for detection

        Returns:
            List[Detection]: A list of 2D bounding boxes, their labels, and the
            confidence score of the labels, around the found objects in the next 2D image
            from the given camera, with the given detector applied to it.
        """
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
        """Get a list of detections in the given image using the specified detector

        Args:
            image (Image): The image to get detections from

        Returns:
            List[Detection]: A list of 2D bounding boxes, their labels, and the
            confidence score of the labels, around the found objects in the next 2D image
            from the given camera, with the given detector applied to it.
        """
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
        """Get a list of classifications in the next image given a camera and a classifier

        Args:
            camera_name (str): The name of the camera to use for detection
            count (int): The number of classifications desired

        returns:
            List[Classification]: The list of Classifications
        """
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
        """Get a list of detections in the given image using the specified detector

        Args:
            image (Image): The image to get detections from

        Returns:
            List[Classification]: The list of Classifications
        """
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
        self, camera_name: str, *, extra: Optional[Mapping[str, Any]] = None, timeout: Optional[float] = None
    ) -> List[PointCloudObject]:
        """
        Returns a list of the 3D point cloud objects and associated metadata in the latest
        picture obtained from the specified 3D camera (using the specified segmenter).

        To deserialize the returned information into a numpy array, use the Open3D library.
        ::

            import numpy as np
            import open3d as o3d

            object_point_clouds = await vision.get_object_point_clouds(camera_name, segmenter_name)

            # write the first object point cloud into a temporary file
            with open("/tmp/pointcloud_data.pcd", "wb") as f:
                f.write(object_point_clouds[0].point_cloud)
            pcd = o3d.io.read_point_cloud("/tmp/pointcloud_data.pcd")
            points = np.asarray(pcd.points)

        Args:
            camera_name (str): The name of the camera

        Returns:
            List[PointCloudObject]: The pointcloud objects with metadata
        """
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

    async def do_command(self, command: Mapping[str, ValueTypes], *, timeout: Optional[float] = None) -> Mapping[str, ValueTypes]:
        """Send/receive arbitrary commands

        Args:
            command (Dict[str, ValueTypes]): The command to execute

        Returns:
            Dict[str, ValueTypes]: Result of the executed command
        """
        request = DoCommandRequest(name=self.name, command=dict_to_struct(command))
        response: DoCommandResponse = await self.client.DoCommand(request, timeout=timeout)
        return struct_to_dict(response.result)
