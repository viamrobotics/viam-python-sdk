import json
from dataclasses import dataclass
from enum import Enum
from typing import Any, List, Mapping, Sequence, Union

from grpclib.client import Channel
from PIL.Image import Image

from viam.components.types import CameraMimeType
from viam.proto.common import PointCloudObject
from viam.proto.service.vision import (
    AddClassifierRequest,
    AddDetectorRequest,
    AddSegmenterRequest,
    Classification,
    Detection,
    GetClassificationsFromCameraRequest,
    GetClassificationsFromCameraResponse,
    GetClassificationsRequest,
    GetClassificationsResponse,
    GetClassifierNamesRequest,
    GetClassifierNamesResponse,
    GetDetectionsFromCameraRequest,
    GetDetectionsFromCameraResponse,
    GetDetectionsRequest,
    GetDetectionsResponse,
    GetDetectorNamesRequest,
    GetDetectorNamesResponse,
    GetModelParameterSchemaRequest,
    GetModelParameterSchemaResponse,
    GetObjectPointCloudsRequest,
    GetObjectPointCloudsResponse,
    GetSegmenterNamesRequest,
    GetSegmenterNamesResponse,
    RemoveClassifierRequest,
    RemoveDetectorRequest,
    RemoveSegmenterRequest,
    VisionServiceStub,
)
from viam.services.service_client_base import ServiceClientBase
from viam.utils import dict_to_struct


class VisModelType(str, Enum):
    DETECTOR_TF_LITE = "tflite_detector"
    DETECTOR_TENSORFLOW = "tf_detector"
    DETECTOR_COLOR = "color_detector"
    CLASSIFIER_TFLITE = "tflite_classifier"
    CLASSIFIER_TENSORFLOW = "tf_classifier"
    DETECTOR_SEGMENTER = "detector_segmenter"
    RADIUS_CLUSTERING_SEGMENTER = "radius_clustering_segmenter"


@dataclass
class VisModelConfig:
    name: str
    type: VisModelType
    parameters: Mapping[str, Any]


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

    async def add_detector(self, config: VisModelConfig):
        """Add a new detector to the service. Returns nothing if successful, and an error if not.
        Registers a new detector just as if you had put it in the original "register_models" field
        in the robot config. Available types and their parameters can be found in the
        vision service documentation.

        Args:
            config (VisModelConfig): The configuration of the detector to add.
        """
        request = AddDetectorRequest(
            name=self.name,
            detector_name=config.name,
            detector_model_type=config.type,
            detector_parameters=dict_to_struct(config.parameters),
        )
        await self.client.AddDetector(request)

    async def remove_detector(self, detector_name: str):
        """Remove the detector with the given name from the service. Returns nothing if successful.

        Args:
            detector_name (str): The name of the detector to remove
        """
        request = RemoveDetectorRequest(name=self.name, detector_name=detector_name)
        await self.client.RemoveDetector(request)

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
        mime_type = CameraMimeType.JPEG
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

    async def get_classifier_names(self) -> List[str]:
        """Get the list of classifiers currently registered to the service

        Returns:
            List[str]: The list of classifier names
        """
        request = GetClassifierNamesRequest(name=self.name)
        response: GetClassifierNamesResponse = await self.client.GetClassifierNames(request)
        return list(response.classifier_names)

    async def add_classifier(self, config: VisModelConfig):
        """Add a classifier to the service.

        Args:
            config (VisModelConfig): The configuration of the classifier
        """
        request = AddClassifierRequest(
            name=self.name,
            classifier_name=config.name,
            classifier_model_type=config.type,
            classifier_parameters=dict_to_struct(config.parameters),
        )
        await self.client.AddClassifier(request)

    async def remove_classifier(self, classifier_name: str):
        """Remove the classifier with the given name from the service. Returns nothing if successful.

        Args:
            classifier_name (str): The name of the classifier to remove
        """
        request = RemoveClassifierRequest(name=self.name, classifier_name=classifier_name)
        await self.client.RemoveClassifier(request)

    async def get_classifications_from_camera(self, camera_name: str, classifier_name: str, count: int) -> List[Classification]:
        """Get a list of classifications in the next image given a camera and a classifier

        Args:
            camera_name (str): The name of the camera to use for detection
            classifier_name (str): The name of the classifier to use for classification
            count (int): The number of classifications desired

        returns:
            List[Classification]: The list of Classifications
        """
        request = GetClassificationsFromCameraRequest(name=self.name, camera_name=camera_name, classifier_name=classifier_name, n=count)
        response: GetClassificationsFromCameraResponse = await self.client.GetClassificationsFromCamera(request)
        return list(response.classifications)

    async def get_classifications(self, image: Image, classifier_name: str) -> List[Classification]:
        """Get a list of detections in the given image using the specified detector

        Args:
            image (Image): The image to get detections from
            classifier_name (str): The name of the detector to use for detection

        Returns:
            List[Classification]: The list of Classifications
        """
        mime_type = CameraMimeType.JPEG
        request = GetClassificationsRequest(
            name=self.name,
            image=mime_type.encode_image(image),
            width=image.width,
            height=image.height,
            mime_type=mime_type,
            classifier_name=classifier_name,
        )
        response: GetClassificationsResponse = await self.client.GetClassifications(request)
        return list(response.classifications)

    async def get_segmenter_names(self) -> List[str]:
        """
        Get the list of segmenters currently registered in the service.

        Returns:
            List[str]: The segmenter names
        """
        request = GetSegmenterNamesRequest(name=self.name)
        response: GetSegmenterNamesResponse = await self.client.GetSegmenterNames(request)
        return list(response.segmenter_names)

    async def add_segmenter(self, config: VisModelConfig):
        """Add a segmenter to the service

        Args:
            config (VisModelConfig): The configuration of the segmenter
        """
        request = AddSegmenterRequest(
            name=self.name,
            segmenter_name=config.name,
            segmenter_model_type=config.type,
            segmenter_parameters=dict_to_struct(config.parameters),
        )
        await self.client.AddSegmenter(request)

    async def remove_segmenter(self, segmenter_name: str):
        """Remove the segmenter with the given name from the service. Returns nothing if successful.

        Args:
            segmenter_name (str): The name of the segmenter to remove
        """
        request = RemoveSegmenterRequest(name=self.name, segmenter_name=segmenter_name)
        await self.client.RemoveSegmenter(request)

    async def get_model_parameters_schema(self, model_type: VisModelType) -> Mapping[str, Union[str, int, float, bool, Sequence, Mapping]]:
        """
        Get the parameters needed to add a model to the vision registry.

        Args:
            model_type (VisModelType): The name of model

        Returns:
            Mapping[str, str | int | float | bool | Sequence | Mapping]: A dictionary representing the parameters as JSONSchema
        """
        request = GetModelParameterSchemaRequest(name=self.name, model_type=model_type)
        response: GetModelParameterSchemaResponse = await self.client.GetModelParameterSchema(request)
        return json.loads(response.model_parameter_schema)

    async def get_object_point_clouds(self, camera_name: str, segmenter_name: str) -> List[PointCloudObject]:
        """
        Returns a list of the 3D point cloud objects and associated metadata in the latest
        picture obtained from the specified 3D camera (using the specified segmenter).

        Args:
            camera_name (str): The name of the camera
            segmenter_name (str): The name of the segmenter

        Returns:
            List[PointCloudObject]: The pointcloud objects with metadata
        """
        request = GetObjectPointCloudsRequest(
            name=self.name,
            camera_name=camera_name,
            segmenter_name=segmenter_name,
            mime_type=CameraMimeType.PCD,
        )
        response: GetObjectPointCloudsResponse = await self.client.GetObjectPointClouds(request)
        return list(response.objects)
