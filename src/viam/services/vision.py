import json
from dataclasses import dataclass
from enum import Enum
from io import BytesIO
from typing import Any, List, Mapping, Optional, Sequence, Union

from grpclib.client import Channel
from viam.media.viam_rgba_plugin import Image

from viam.media.video import CameraMimeType, RawImage
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

    async def get_detector_names(self, *, extra: Optional[Mapping[str, Any]] = None, timeout: Optional[float] = None) -> List[str]:
        """Get the list of detectors currently registered in the service.

        Returns:
            List[str]: The detector names
        """
        if extra is None:
            extra = {}
        request = GetDetectorNamesRequest(name=self.name, extra=dict_to_struct(extra))
        response: GetDetectorNamesResponse = await self.client.GetDetectorNames(request, timeout=timeout)
        return list(response.detector_names)

    async def add_detector(self, config: VisModelConfig, *, extra: Optional[Mapping[str, Any]] = None, timeout: Optional[float] = None):
        """Add a new detector to the service. Returns nothing if successful, and an error if not.
        Registers a new detector just as if you had put it in the original "register_models" field
        in the robot config. Available types and their parameters can be found in the
        vision service documentation.

        Args:
            config (VisModelConfig): The configuration of the detector to add.
        """
        if extra is None:
            extra = {}
        request = AddDetectorRequest(
            name=self.name,
            detector_name=config.name,
            detector_model_type=config.type,
            detector_parameters=dict_to_struct(config.parameters),
            extra=dict_to_struct(extra),
        )
        await self.client.AddDetector(request, timeout=timeout)

    async def remove_detector(self, detector_name: str, *, extra: Optional[Mapping[str, Any]] = None, timeout: Optional[float] = None):
        """Remove the detector with the given name from the service. Returns nothing if successful.

        Args:
            detector_name (str): The name of the detector to remove
        """
        if extra is None:
            extra = {}
        request = RemoveDetectorRequest(name=self.name, detector_name=detector_name, extra=dict_to_struct(extra))
        await self.client.RemoveDetector(request, timeout=timeout)

    async def get_detections_from_camera(
        self, camera_name: str, detector_name: str, *, extra: Optional[Mapping[str, Any]] = None, timeout: Optional[float] = None
    ) -> List[Detection]:
        """Get a list of detections in the next image given a camera and a detector

        Args:
            camera_name (str): The name of the camera to use for detection
            detector_name (str): The name of the detector to use for detection

        Returns:
            List[Detection]: A list of 2D bounding boxes, their labels, and the
            confidence score of the labels, around the found objects in the next 2D image
            from the given camera, with the given detector applied to it.
        """
        if extra is None:
            extra = {}
        request = GetDetectionsFromCameraRequest(
            name=self.name, camera_name=camera_name, detector_name=detector_name, extra=dict_to_struct(extra)
        )
        response: GetDetectionsFromCameraResponse = await self.client.GetDetectionsFromCamera(request, timeout=timeout)
        return list(response.detections)

    async def get_detections(
        self,
        image: Union[Image.Image, RawImage],
        detector_name: str,
        *,
        extra: Optional[Mapping[str, Any]] = None,
        timeout: Optional[float] = None,
    ) -> List[Detection]:
        """Get a list of detections in the given image using the specified detector

        Args:
            image (Image): The image to get detections from
            detector_name (str): The name of the detector to use for detection

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
            detector_name=detector_name,
            extra=dict_to_struct(extra),
        )
        response: GetDetectionsResponse = await self.client.GetDetections(request, timeout=timeout)
        return list(response.detections)

    async def get_classifier_names(self, *, extra: Optional[Mapping[str, Any]] = None, timeout: Optional[float] = None) -> List[str]:
        """Get the list of classifiers currently registered to the service

        Returns:
            List[str]: The list of classifier names
        """
        if extra is None:
            extra = {}
        request = GetClassifierNamesRequest(name=self.name, extra=dict_to_struct(extra))
        response: GetClassifierNamesResponse = await self.client.GetClassifierNames(request, timeout=timeout)
        return list(response.classifier_names)

    async def add_classifier(self, config: VisModelConfig, *, extra: Optional[Mapping[str, Any]] = None, timeout: Optional[float] = None):
        """Add a classifier to the service.

        Args:
            config (VisModelConfig): The configuration of the classifier
        """
        if extra is None:
            extra = {}
        request = AddClassifierRequest(
            name=self.name,
            classifier_name=config.name,
            classifier_model_type=config.type,
            classifier_parameters=dict_to_struct(config.parameters),
            extra=dict_to_struct(extra),
        )
        await self.client.AddClassifier(request, timeout=timeout)

    async def remove_classifier(self, classifier_name: str, *, extra: Optional[Mapping[str, Any]] = None, timeout: Optional[float] = None):
        """Remove the classifier with the given name from the service. Returns nothing if successful.

        Args:
            classifier_name (str): The name of the classifier to remove
        """
        if extra is None:
            extra = {}
        request = RemoveClassifierRequest(name=self.name, classifier_name=classifier_name, extra=dict_to_struct(extra))
        await self.client.RemoveClassifier(request, timeout=timeout)

    async def get_classifications_from_camera(
        self,
        camera_name: str,
        classifier_name: str,
        count: int,
        *,
        extra: Optional[Mapping[str, Any]] = None,
        timeout: Optional[float] = None,
    ) -> List[Classification]:
        """Get a list of classifications in the next image given a camera and a classifier

        Args:
            camera_name (str): The name of the camera to use for detection
            classifier_name (str): The name of the classifier to use for classification
            count (int): The number of classifications desired

        returns:
            List[Classification]: The list of Classifications
        """
        if extra is None:
            extra = {}
        request = GetClassificationsFromCameraRequest(
            name=self.name, camera_name=camera_name, classifier_name=classifier_name, n=count, extra=dict_to_struct(extra)
        )
        response: GetClassificationsFromCameraResponse = await self.client.GetClassificationsFromCamera(request, timeout=timeout)
        return list(response.classifications)

    async def get_classifications(
        self,
        image: Union[Image.Image, RawImage],
        classifier_name: str,
        *,
        extra: Optional[Mapping[str, Any]] = None,
        timeout: Optional[float] = None,
    ) -> List[Classification]:
        """Get a list of detections in the given image using the specified detector

        Args:
            image (Image): The image to get detections from
            classifier_name (str): The name of the detector to use for detection

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
            classifier_name=classifier_name,
            extra=dict_to_struct(extra),
        )
        response: GetClassificationsResponse = await self.client.GetClassifications(request, timeout=timeout)
        return list(response.classifications)

    async def get_segmenter_names(self, *, extra: Optional[Mapping[str, Any]] = None, timeout: Optional[float] = None) -> List[str]:
        """
        Get the list of segmenters currently registered in the service.

        Returns:
            List[str]: The segmenter names
        """
        if extra is None:
            extra = {}
        request = GetSegmenterNamesRequest(name=self.name, extra=dict_to_struct(extra))
        response: GetSegmenterNamesResponse = await self.client.GetSegmenterNames(request, timeout=timeout)
        return list(response.segmenter_names)

    async def add_segmenter(self, config: VisModelConfig, *, extra: Optional[Mapping[str, Any]] = None, timeout: Optional[float] = None):
        """Add a segmenter to the service

        Args:
            config (VisModelConfig): The configuration of the segmenter
        """
        if extra is None:
            extra = {}
        request = AddSegmenterRequest(
            name=self.name,
            segmenter_name=config.name,
            segmenter_model_type=config.type,
            segmenter_parameters=dict_to_struct(config.parameters),
            extra=dict_to_struct(extra),
        )
        await self.client.AddSegmenter(request, timeout=timeout)

    async def remove_segmenter(self, segmenter_name: str, *, extra: Optional[Mapping[str, Any]] = None, timeout: Optional[float] = None):
        """Remove the segmenter with the given name from the service. Returns nothing if successful.

        Args:
            segmenter_name (str): The name of the segmenter to remove
        """
        if extra is None:
            extra = {}
        request = RemoveSegmenterRequest(name=self.name, segmenter_name=segmenter_name, extra=dict_to_struct(extra))
        await self.client.RemoveSegmenter(request, timeout=timeout)

    async def get_model_parameters_schema(
        self, model_type: VisModelType, *, extra: Optional[Mapping[str, Any]] = None, timeout: Optional[float] = None
    ) -> Mapping[str, Union[str, int, float, bool, Sequence, Mapping]]:
        """
        Get the parameters needed to add a model to the vision registry.

        Args:
            model_type (VisModelType): The name of model

        Returns:
            Mapping[str, str | int | float | bool | Sequence | Mapping]: A dictionary representing the parameters as JSONSchema
        """
        if extra is None:
            extra = {}
        request = GetModelParameterSchemaRequest(name=self.name, model_type=model_type, extra=dict_to_struct(extra))
        response: GetModelParameterSchemaResponse = await self.client.GetModelParameterSchema(request, timeout=timeout)
        return json.loads(response.model_parameter_schema)

    async def get_object_point_clouds(
        self, camera_name: str, segmenter_name: str, *, extra: Optional[Mapping[str, Any]] = None, timeout: Optional[float] = None
    ) -> List[PointCloudObject]:
        """
        Returns a list of the 3D point cloud objects and associated metadata in the latest
        picture obtained from the specified 3D camera (using the specified segmenter).

        Args:
            camera_name (str): The name of the camera
            segmenter_name (str): The name of the segmenter

        Returns:
            List[PointCloudObject]: The pointcloud objects with metadata
        """
        if extra is None:
            extra = {}
        request = GetObjectPointCloudsRequest(
            name=self.name,
            camera_name=camera_name,
            segmenter_name=segmenter_name,
            mime_type=CameraMimeType.PCD,
            extra=dict_to_struct(extra),
        )
        response: GetObjectPointCloudsResponse = await self.client.GetObjectPointClouds(request, timeout=timeout)
        return list(response.objects)
