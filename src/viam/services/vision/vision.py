import abc
from typing import Any, Final, List, Mapping, Optional, Union

from PIL import Image

from viam.media.video import RawImage
from viam.proto.common import PointCloudObject
from viam.proto.service.vision import Classification, Detection
from viam.resource.types import RESOURCE_NAMESPACE_RDK, RESOURCE_TYPE_SERVICE, Subtype

from ..service_base import ServiceBase


class Vision(ServiceBase):
    """
    Vision represents a Vision service.

    This acts as an abstract base class for any drivers representing specific
    arm implementations. This cannot be used on its own. If the ``__init__()`` function is
    overridden, it must call the ``super().__init__()`` function.
    """

    SUBTYPE: Final = Subtype(  # pyright: ignore [reportIncompatibleVariableOverride]
        RESOURCE_NAMESPACE_RDK, RESOURCE_TYPE_SERVICE, "vision"
    )

    @abc.abstractmethod
    async def get_detections_from_camera(
        self,
        camera_name: str,
        *,
        extra: Optional[Mapping[str, Any]] = None,
        timeout: Optional[float] = None,
    ) -> List[Detection]:
        """Get a list of detections in the next image given a camera and a detector

        ::

            camera_name = "cam1"

            # Grab the detector you configured on your machine
            my_detector = VisionClient.from_robot(robot, "my_detector")

            # Get detections from the next image from the camera
            detections = await my_detector.get_detections_from_camera(camera_name)

        Args:
            camera_name (str): The name of the camera to use for detection

        Returns:
            List[viam.proto.service.vision.Detection]: A list of 2D bounding boxes, their labels, and the
            confidence score of the labels, around the found objects in the next 2D image
            from the given camera, with the given detector applied to it.
        """
        ...

    @abc.abstractmethod
    async def get_detections(
        self,
        image: Union[Image.Image, RawImage],
        *,
        extra: Optional[Mapping[str, Any]] = None,
        timeout: Optional[float] = None,
    ) -> List[Detection]:
        """Get a list of detections in the given image using the specified detector

        ::

            # Grab camera from the machine
            cam1 = Camera.from_robot(robot, "cam1")

            # Get the detector you configured on your machine
            my_detector = VisionClient.from_robot(robot, "my_detector")

            # Get an image from the camera
            img = await cam1.get_image()

            # Get detections from that image
            detections = await my_detector.get_detections(img)

        Args:
            image (Image): The image to get detections from

        Returns:
            List[viam.proto.service.vision.Detection]: A list of 2D bounding boxes, their labels, and the
            confidence score of the labels, around the found objects in the next 2D image
            from the given camera, with the given detector applied to it.
        """
        ...

    @abc.abstractmethod
    async def get_classifications_from_camera(
        self,
        camera_name: str,
        count: int,
        *,
        extra: Optional[Mapping[str, Any]] = None,
        timeout: Optional[float] = None,
    ) -> List[Classification]:
        """Get a list of classifications in the next image given a camera and a classifier

        ::

            camera_name = "cam1"

            # Grab the classifier you configured on your machine
            my_classifier = VisionClient.from_robot(robot, "my_classifier")

            # Get the 2 classifications with the highest confidence scores from the next image from the camera
            classifications = await my_classifier.get_classifications_from_camera(
                camera_name, 2)

        Args:
            camera_name (str): The name of the camera to use for detection
            count (int): The number of classifications desired

        returns:
            List[viam.proto.service.vision.Classification]: The list of Classifications
        """
        ...

    @abc.abstractmethod
    async def get_classifications(
        self,
        image: Union[Image.Image, RawImage],
        count: int,
        *,
        extra: Optional[Mapping[str, Any]] = None,
        timeout: Optional[float] = None,
    ) -> List[Classification]:
        """Get a list of classifications in the given image using the specified classifier

        ::

            # Grab camera from the machine
            cam1 = Camera.from_robot(robot, "cam1")

            # Get the classifier you configured on your machine
            my_classifier = VisionClient.from_robot(robot, "my_classifier")

            # Get an image from the camera
            img = await cam1.get_image()

            # Get the 2 classifications with the highest confidence scores
            classifications = await my_classifier.get_classifications(img, 2)

        Args:
            image (Image): The image to get detections from
            count (int): The number of classifications desired

        Returns:
            List[viam.proto.service.vision.Classification]: The list of Classifications
        """
        ...

    @abc.abstractmethod
    async def get_object_point_clouds(
        self,
        camera_name: str,
        *,
        extra: Optional[Mapping[str, Any]] = None,
        timeout: Optional[float] = None,
    ) -> List[PointCloudObject]:
        """
        Returns a list of the 3D point cloud objects and associated metadata in the latest
        picture obtained from the specified 3D camera (using the specified segmenter).

        To deserialize the returned information into a numpy array, use the Open3D library.

        ::

            import numpy as np
            import open3d as o3d

            # Grab the 3D camera from the machine
            cam1 = Camera.from_robot(robot, "cam1")
            # Grab the object segmenter you configured on your machine
            my_segmenter = VisionClient.from_robot(robot, "my_segmenter")
            # Get the objects from the camera output
            objects = await my_segmenter.get_object_point_clouds(cam1)
            # write the first object point cloud into a temporary file
            with open("/tmp/pointcloud_data.pcd", "wb") as f:
                f.write(objects[0].point_cloud)
            pcd = o3d.io.read_point_cloud("/tmp/pointcloud_data.pcd")
            points = np.asarray(pcd.points)

        Args:
            camera_name (str): The name of the camera

        Returns:
            List[viam.proto.common.PointCloudObject]: The pointcloud objects with metadata
        """
        ...
