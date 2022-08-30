from dataclasses import dataclass
from enum import Enum
from typing import Any, Dict, List, Tuple


from grpclib.client import Channel
from PIL.Image import Image
from viam.components.types import CameraMimeType
from viam.proto.api.common import PointCloudObject
from viam.proto.api.service.vision import (
    AddDetectorRequest,
    Detection,
    GetDetectionsFromCameraRequest,
    GetDetectionsFromCameraResponse,
    GetDetectionsRequest,
    GetDetectionsResponse,
    GetDetectorNamesRequest,
    GetDetectorNamesResponse,
    GetObjectPointCloudsRequest,
    GetObjectPointCloudsResponse,
    GetSegmenterNamesRequest,
    GetSegmenterNamesResponse,
    GetSegmenterParametersRequest,
    GetSegmenterParametersResponse,
    VisionServiceStub,
)
from viam.utils import dict_to_struct
from viam.services.service_client_base import ServiceClientBase


class DetectorType(str, Enum):
    TF_LITE = "tflite"
    TENSORFLOW = "tensorflow"
    COLOR = "color"


@dataclass
class DetectorConfig:
    name: str
    type: DetectorType
    parameters: Dict[str, Any]


class VisionServiceClient(ServiceClientBase):
    """
    Connect to the Vision service, which allows you to access various computer vision algorithms
    (like detection, segmentation, tracking, etc) that usually only require a camera or image input.
    """

    SERVICE_TYPE = "vision"

    def __init__(self, name: str, channel: Channel):
        self.client = VisionServiceStub(channel)
        self.name = name

    async def get_detector_names(self) -> List[str]:
        """Get the list of detectors currently registered in the service.

        Returns:
            List[str]: The detector names
        """
        request = GetDetectorNamesRequest(name=self.name)
        response: GetDetectorNamesResponse = await self.client.GetDetectorNames(request)
        return list(response.detector_names)

    async def add_detector(self, detector: DetectorConfig):
        """Add a new detector to the service. Returns nothing if successful, and an error if not.
        Registers a new detector just as if you had put it in the original "register_detectors" field
        in the robot config. Available types and their parameters can be found in the
        vision service documentation.

        Args:
            detector (DetectorConfig): The configuration of the detector to add.
        """
        request = AddDetectorRequest(
            name=self.name,
            detector_name=detector.name,
            detector_model_type=detector.type,
            detector_parameters=dict_to_struct(detector.parameters),
        )
        await self.client.AddDetector(request)

    async def get_detections_from_camera(self, camera_name: str, detector_name: str) -> List[Detection]:
        """Get a list of detections in the next image given a camera and a detector

        Args:
            camera_name (str): The name of the camera to use for detection
            detector_name (str): The name of the detector to use for detection

        Returns:
            List[Detection]: A list of 2D bounding boxes, their labels, and the
            confidence score of the labels, around the found objects in the next 2D image
            from the given camera, with the given detector applied to it.
        """
        request = GetDetectionsFromCameraRequest(name=self.name, camera_name=camera_name, detector_name=detector_name)
        response: GetDetectionsFromCameraResponse = await self.client.GetDetectionsFromCamera(request)
        return list(response.detections)

    async def get_detections(self, image: Image, detector_name: str) -> List[Detection]:
        """Get a list of detections in the given image using the specified detector

        Args:
            image (Image): The image to get detections from
            detector_name (str): The name of the detector to use for detection

        Returns:
            List[Detection]: A list of 2D bounding boxes, their labels, and the
            confidence score of the labels, around the found objects in the next 2D image
            from the given camera, with the given detector applied to it.
        """
        mime_type = CameraMimeType.PNG
        request = GetDetectionsRequest(
            name=self.name,
            image=mime_type.encode_image(image),
            width=image.width,
            height=image.height,
            mime_type=mime_type,
            detector_name=detector_name,
        )
        response: GetDetectionsResponse = await self.client.GetDetections(request)
        return list(response.detections)

    async def get_segmenter_names(self) -> List[str]:
        """
        Get the list of segmenters currently registered in the service.

        Returns:
            List[str]: The segmenter names
        """
        request = GetSegmenterNamesRequest(name=self.name)
        response: GetSegmenterNamesResponse = await self.client.GetSegmenterNames(request)
        return list(response.segmenter_names)

    async def get_segmenter_parameters(self, segmenter_name: str) -> List[Tuple[str, str]]:
        """
        Get the parameter fields needed for the given segmenter.

        Args:
            segmenter_name (str): The name of the segmenter

        Returns:
            List[Tuple[str, str]]: A list of parameters for the segmenter.
                The first item in the tuple is the name of the parameter.
                The second item in the tuple is the type of the parameter.
        """
        request = GetSegmenterParametersRequest(name=self.name, segmenter_name=segmenter_name)
        response: GetSegmenterParametersResponse = await self.client.GetSegmenterParameters(request)
        return [(x.name, x.type) for x in response.segmenter_parameters]

    async def get_object_point_clouds(self, camera_name: str, segmenter_name: str, parameters: Dict[str, Any]) -> List[PointCloudObject]:
        """
        Returns a list of the 3D point cloud objects and associated metadata in the latest
        picture obtained from the specified 3D camera (using the specified segmenter).
        The parameters are the necessary parameters that the given segmenter needs in order to work.

        Args:
            camera_name (str): The name of the camera
            segmenter_name (str): The name of the segmenter
            parameters (Dict[str, Any]): The parameters for the named segmenter

        Returns:
            List[PointCloudObject]: The pointcloud objects with metadata
        """
        request = GetObjectPointCloudsRequest(
            name=self.name,
            camera_name=camera_name,
            segmenter_name=segmenter_name,
            mime_type=CameraMimeType.PCD.value,
            parameters=dict_to_struct(parameters),
        )
        response: GetObjectPointCloudsResponse = await self.client.GetObjectPointClouds(request)
        return list(response.objects)
