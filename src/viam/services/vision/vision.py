import abc
import sys
from typing import Final, List, Mapping, Optional

from viam.media.video import ViamImage
from viam.proto.common import PointCloudObject
from viam.proto.service.vision import Classification, Detection, GetPropertiesResponse
from viam.resource.types import API, RESOURCE_NAMESPACE_RDK, RESOURCE_TYPE_SERVICE
from viam.utils import ValueTypes

from ..service_base import ServiceBase

if sys.version_info >= (3, 10):
    from typing import TypeAlias
else:
    from typing_extensions import TypeAlias


class CaptureAllResult:
    """
    CaptureAllResult represents the collection of things that you have requested from the
    CaptureAllFromCamera method. This is used most often for visualization purposes, since normally,
    returning the image on every call to a classifier/detector/etc would be costly and unnecessary.
    The default result for each field is None rather than the empty list to distinguish between
    "there was no request for the classifier/detector to return a result" vs.
    "the classifier/detector was requested, but there were no results".
    """

    def __init__(
        self,
        image: Optional[ViamImage] = None,
        classifications: Optional[List[Classification]] = None,
        detections: Optional[List[Detection]] = None,
        objects: Optional[List[PointCloudObject]] = None,
        extra: Optional[Mapping[str, ValueTypes]] = None,
    ):
        """
        Args:
            image (ViamImage|None): The image from the GetImage request of the camera, if it was requested.
            classifications (List[Classification]|None): The classifications from GetClassifications, if it was requested.
            detections (List[Detection]|None): The detections from GetDetections, if it was requested.
            objects (List[PointCloudObject]|None): the object point clouds from GetObjectPointClouds, if it was requested.
            extra (dict): A catch all structure, usually for metadata, that a module writer might want to return. Default empty.

        Returns:
            None
        """
        self.image = image
        self.classifications = classifications
        self.detections = detections
        self.objects = objects
        self.extra = extra


class Vision(ServiceBase):
    """
    Vision represents a Vision service.

    This acts as an abstract base class for any drivers representing specific
    vision implementations. This cannot be used on its own. If the ``__init__()`` function is
    overridden, it must call the ``super().__init__()`` function.

    For more information, see `Computer Vision service <https://docs.viam.com/dev/reference/apis/services/vision/>`_.
    """

    API: Final = API(  # pyright: ignore [reportIncompatibleVariableOverride]
        RESOURCE_NAMESPACE_RDK, RESOURCE_TYPE_SERVICE, "vision"
    )

    Properties: "TypeAlias" = GetPropertiesResponse
    """
    Properties is a class that states what features are supported on the associated vision service.
    Currently, these are the following properties:
    - classifications_supported (bool): GetClassifications and GetClassificationsFromCamera are implemented.
    - detections_supported (bool): GetDetections and GetDetectionsFromCamera are implemented.
    - object_point_clouds_supported (bool): GetObjectPointClouds is implemented.
    """

    @abc.abstractmethod
    async def capture_all_from_camera(
        self,
        camera_name: str,
        return_image: bool = False,
        return_classifications: bool = False,
        return_detections: bool = False,
        return_object_point_clouds: bool = False,
        *,
        extra: Optional[Mapping[str, ValueTypes]] = None,
        timeout: Optional[float] = None,
    ) -> CaptureAllResult:
        """Get the next image, detections, classifications, and objects all together,
        given a camera name. Used for visualization.

        ::

            my_detector = VisionClient.from_robot(machine, "my_detector")

            # Get the captured data for a camera
            result = await my_detector.capture_all_from_camera(
                "my_camera",
                return_image=True,
                return_detections=True,
            )
            image = result.image
            detections = result.detections

        Args:
            camera_name (str): The name of the camera to use for detection
            return_image (bool): Ask the vision service to return the camera's latest image
            return_classifications (bool): Ask the vision service to return its latest classifications
            return_detections (bool): Ask the vision service to return its latest detections
            return_object_point_clouds (bool): Ask the vision service to return its latest 3D segmentations

        Returns:
            vision.CaptureAllResult: A class that stores all potential returns from the vision service.
            It can  return the image from the camera along with its associated detections, classifications,
            and objects, as well as any extra info the model may provide.

        For more information, see `Computer Vision service <https://docs.viam.com/dev/reference/apis/services/vision/#captureallfromcamera>`_.
        """
        ...

    @abc.abstractmethod
    async def get_detections_from_camera(
        self,
        camera_name: str,
        *,
        extra: Optional[Mapping[str, ValueTypes]] = None,
        timeout: Optional[float] = None,
    ) -> List[Detection]:
        """Get a list of detections in the next image given a camera and a detector

        ::

            my_detector = VisionClient.from_robot(robot=machine, "my_detector")

            # Get detections for the next image from the specified camera
            detections = await my_detector.get_detections_from_camera("my_camera")

        Args:
            camera_name (str): The name of the camera to use for detection

        Raises:
            ViamError: Raised if given an image without a specified width and height

        Returns:
            List[viam.proto.service.vision.Detection]: A list of 2D bounding boxes, their labels, and the
            confidence score of the labels, around the found objects in the next 2D image
            from the given camera, with the given detector applied to it.

        For more information, see `Computer Vision service <https://docs.viam.com/dev/reference/apis/services/vision/#getdetectionsfromcamera>`_.
        """
        ...

    @abc.abstractmethod
    async def get_detections(
        self,
        image: ViamImage,
        *,
        extra: Optional[Mapping[str, ValueTypes]] = None,
        timeout: Optional[float] = None,
    ) -> List[Detection]:
        """Get a list of detections in the given image using the specified detector

        ::

            my_camera = Camera.from_robot(robot=machine, "my_camera")
            my_detector = VisionClient.from_robot(robot=machine, "my_detector")

            # Get an image from the camera
            img = await my_camera.get_image()

            # Get detections for that image
            detections = await my_detector.get_detections(img)

        Args:
            image (ViamImage): The image to get detections for

        Raises:
            ViamError: Raised if given an image without a specified width and height

        Returns:
            List[viam.proto.service.vision.Detection]: A list of 2D bounding boxes, their labels, and the
            confidence score of the labels, around the found objects in the next 2D image
            from the given camera, with the given detector applied to it.

        For more information, see `Computer Vision service <https://docs.viam.com/dev/reference/apis/services/vision/#getdetections>`_.
        """
        ...

    @abc.abstractmethod
    async def get_classifications_from_camera(
        self,
        camera_name: str,
        count: int,
        *,
        extra: Optional[Mapping[str, ValueTypes]] = None,
        timeout: Optional[float] = None,
    ) -> List[Classification]:
        """Get a list of classifications in the next image given a camera and a classifier

        ::

            my_classifier = VisionClient.from_robot(robot=machine, "my_classifier")

            # Get the 2 classifications with the highest confidence scores for the next image from the camera
            classifications = await my_classifier.get_classifications_from_camera(
                "my_camera", 2)

        Args:
            camera_name (str): The name of the camera to use for detection
            count (int): The number of classifications desired

        returns:
            List[viam.proto.service.vision.Classification]: The list of Classifications

        For more information, see `Computer Vision service <https://docs.viam.com/dev/reference/apis/services/vision/#getclassificationsfromcamera>`_.
        """
        ...

    @abc.abstractmethod
    async def get_classifications(
        self,
        image: ViamImage,
        count: int,
        *,
        extra: Optional[Mapping[str, ValueTypes]] = None,
        timeout: Optional[float] = None,
    ) -> List[Classification]:
        """Get a list of classifications in the given image using the specified classifier

        ::

            my_camera = Camera.from_robot(robot=machine, "my_camera")
            my_classifier = VisionClient.from_robot(robot=machine, "my_classifier")

            # Get an image from the camera
            img = await my_camera.get_image()

            # Get the 2 classifications with the highest confidence scores for the image
            classifications = await my_classifier.get_classifications(img, 2)

        Args:
            image (ViamImage): The image to get detections for
            count (int): The number of classifications desired

        Returns:
            List[viam.proto.service.vision.Classification]: The list of Classifications

        For more information, see `Computer Vision service <https://docs.viam.com/dev/reference/apis/services/vision/#getclassifications>`_.
        """
        ...

    @abc.abstractmethod
    async def get_object_point_clouds(
        self,
        camera_name: str,
        *,
        extra: Optional[Mapping[str, ValueTypes]] = None,
        timeout: Optional[float] = None,
    ) -> List[PointCloudObject]:
        """
        Returns a list of the 3D point cloud objects and associated metadata in the latest
        picture obtained from the specified 3D camera (using the specified segmenter).

        To deserialize the returned information into a numpy array, use the Open3D library.

        ::

            import numpy as np
            import open3d as o3d

            my_segmenter = VisionClient.from_robot(robot=machine, "my_segmenter")
            # Get the objects from the camera output
            objects = await my_segmenter.get_object_point_clouds("my_camera")
            # write the first object point cloud into a temporary file
            with open("/tmp/pointcloud_data.pcd", "wb") as f:
                f.write(objects[0].point_cloud)
            pcd = o3d.io.read_point_cloud("/tmp/pointcloud_data.pcd")
            points = np.asarray(pcd.points)

        Args:
            camera_name (str): The name of the camera

        Returns:
            List[viam.proto.common.PointCloudObject]: The pointcloud objects with metadata

        For more information, see `Computer Vision service <https://docs.viam.com/dev/reference/apis/services/vision/#getobjectpointclouds>`_.
        """
        ...

    @abc.abstractmethod
    async def get_properties(
        self,
        *,
        extra: Optional[Mapping[str, ValueTypes]] = None,
        timeout: Optional[float] = None,
    ) -> Properties:
        """
        Get info about what vision methods the vision service provides. Currently returns boolean values that
        state whether the service implements the classification, detection, and/or 3D object segmentation methods.

        ::

            my_detector = VisionClient.from_robot(robot=machine, "my_detector")
            properties = await my_detector.get_properties()
            detections_supported = properties.detections_supported
            classifications_supported = properties.classifications_supported

        Returns:
            Properties: The properties of the vision service

        For more information, see `Computer Vision service <https://docs.viam.com/dev/reference/apis/services/vision/#getproperties>`_.
        """
        ...
