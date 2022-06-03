from dataclasses import dataclass
from enum import Enum
from typing import Any, Dict, List, Tuple

from google.protobuf.struct_pb2 import Struct
from grpclib.client import Channel
from viam.components.types import CameraMimeType
from viam.proto.api.common import PointCloudObject
from viam.proto.api.service.vision import (AddDetectorRequest, Detection,
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
                                           VisionServiceStub)


class DetectorType(str, Enum):
    TF_LITE = 'tflite'
    TENSORFLOW = 'tensorflow'
    COLOR = 'color'


@dataclass
class DetectorConfig:
    name: str
    type: DetectorType
    parameters: Dict[str, Any]


class VisionClient:
    """
    Connect to the Vision service, which allows you to access various computer vision algorithms
    (like detection, segmentation, tracking, etc) that usually only require a camera or image input.
    """

    def __init__(self, channel: Channel):
        self.client = VisionServiceStub(channel)

    async def get_detector_names(self) -> List[str]:
        """Get the list of detectors in the registry.

        Returns:
            List[str]: The detector names
        """
        request = GetDetectorNamesRequest()
        response: GetDetectorNamesResponse = await self.client.GetDetectorNames(request)
        return list(response.detector_names)

    async def add_detector(self, detector: DetectorConfig):
        """Add a new detector to the registry.

        Args:
            detector (DetectorConfig): The configuration of the detector to add
        """
        params = Struct()
        params.update(detector.parameters)
        request = AddDetectorRequest(detector_name=detector.name, detector_model_type=detector.type, detector_parameters=params)
        await self.client.AddDetector(request)

    async def get_detections(self, camera_name: str, detector_name: str) -> List[Detection]:
        """Get a list of detections in the next image given a camera and a detector

        Args:
            camera_name (str): The name of the camera to use for detection
            detector_name (str): The name of the detector to use for detection

        Returns:
            List[Detection]: The detections
        """
        request = GetDetectionsRequest(camera_name=camera_name, detector_name=detector_name)
        response: GetDetectionsResponse = await self.client.GetDetections(request)
        return list(response.detections)

    async def get_segmenter_names(self) -> List[str]:
        """
        Get the list of segmenters in the registry

        Returns:
            List[str]: The segmenter names
        """
        request = GetSegmenterNamesRequest()
        response: GetSegmenterNamesResponse = \
            await self.client.GetSegmenterNames(request)
        return list(response.segmenter_names)

    async def get_segmenter_parameters(
        self,
        segmenter_name: str
    ) -> List[Tuple[str, str]]:
        """
        Get the parameter fields needed for the given segmenter.

        Args:
            segmenter_name (str): The name of the segmenter

        Returns:
            List[Tuple[str, str]]: A list of parameters for the segmenter.
                The first item in the tuple is the name of the parameter.
                The second item in the tuple is the type of the parameter.
        """
        request = GetSegmenterParametersRequest(segmenter_name=segmenter_name)
        response: GetSegmenterParametersResponse = \
            await self.client.GetSegmenterParameters(request)
        return [(x.name, x.type) for x in response.segmenter_parameters]

    async def get_object_point_clouds(
        self,
        camera_name: str,
        segmenter_name: str,
        parameters: Dict[str, Any]
    ) -> List[PointCloudObject]:
        """
        Get all the found objects in a pointcloud from a camera of the
        underlying robot, as well as the 3-vector center of each of the
        found objects.

        Args:
            camera_name (str): The name of the camera
            segmenter_name (str): The name of the segmenter
            parameters (Dict[str, Any]): The parameters for the pointcloud

        Returns:
            List[PointCloudObject]: The pointclouds
        """
        struct = Struct()
        struct.update(parameters)
        request = GetObjectPointCloudsRequest(
            camera_name=camera_name,
            segmenter_name=segmenter_name,
            mime_type=CameraMimeType.PCD.value,
            parameters=struct
        )
        response: GetObjectPointCloudsResponse = \
            await self.client.GetObjectPointClouds(request)
        return list(response.objects)
