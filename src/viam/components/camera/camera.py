import abc
import sys
from typing import Any, Dict, Final, List, Optional, Tuple

from viam.media.video import NamedImage, ViamImage
from viam.proto.common import ResponseMetadata
from viam.proto.component.camera import GetPropertiesResponse
from viam.resource.types import RESOURCE_NAMESPACE_RDK, RESOURCE_TYPE_COMPONENT, Subtype

from ..component_base import ComponentBase

if sys.version_info >= (3, 10):
    from typing import TypeAlias
else:
    from typing_extensions import TypeAlias


class Camera(ComponentBase):
    """
    Camera represents any physical hardware that can capture frames.

    This acts as an abstract base class for any drivers representing specific
    camera implementations. This cannot be used on its own. If the ``__init__()`` function is
    overridden, it must call the ``super().__init__()`` function.

    ::

        from viam.components.camera import Camera

    For more information, see `Camera component <https://docs.viam.com/components/camera/>`_.
    """

    SUBTYPE: Final = Subtype(  # pyright: ignore [reportIncompatibleVariableOverride]
        RESOURCE_NAMESPACE_RDK, RESOURCE_TYPE_COMPONENT, "camera"
    )

    Properties: "TypeAlias" = GetPropertiesResponse

    @abc.abstractmethod
    async def get_image(
        self, mime_type: str = "", *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs
    ) -> ViamImage:
        """Get the next image from the camera as a ViamImage.
        Be sure to close the image when finished.

        NOTE: If the mime type is ``image/vnd.viam.dep`` you can use :func:`viam.media.video.ViamImage.bytes_to_depth_array`
        to convert the data to a standard representation.

        ::

            my_camera = Camera.from_robot(robot=robot, name="my_camera")

            # Assume "frame" has a mime_type of "image/vnd.viam.dep"
            frame = await my_camera.get_image(mime_type = CameraMimeType.VIAM_RAW_DEPTH)

            # Convert "frame" to a standard 2D image representation.
            # Remove the 1st 3x8 bytes and reshape the raw bytes to List[List[Int]].
            standard_frame = frame.bytes_to_depth_array()

        Args:
            mime_type (str): The desired mime type of the image. This does not guarantee output type

        Returns:
            ViamImage: The frame.

        For more information, see `Camera component <https://docs.viam.com/components/camera/>`_.
        """
        ...

    @abc.abstractmethod
    async def get_images(self, *, timeout: Optional[float] = None, **kwargs) -> Tuple[List[NamedImage], ResponseMetadata]:
        """Get simultaneous images from different imagers, along with associated metadata.
        This should not be used for getting a time series of images from the same imager.

        ::

            my_camera = Camera.from_robot(robot=robot, name="my_camera")

            images, metadata = await my_camera.get_images()
            img0 = images[0].image
            timestamp = metadata.captured_at

        Returns:
            Tuple[List[NamedImage], ResponseMetadata]: A tuple containing two values; the first [0] a list of images
            returned from the camera system, and the second [1] the metadata associated with this response.

        For more information, see `Camera component <https://docs.viam.com/components/camera/>`_.
        """
        ...

    @abc.abstractmethod
    async def get_point_cloud(
        self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs
    ) -> Tuple[bytes, str]:
        """
        Get the next point cloud from the camera. This will be
        returned as bytes with a mimetype describing
        the structure of the data. The consumer of this call
        should encode the bytes into the formatted suggested
        by the mimetype.

        To deserialize the returned information into a numpy array, use the Open3D library.
        ::

            import numpy as np
            import open3d as o3d

            data, _ = await camera.get_point_cloud()

            # write the point cloud into a temporary file
            with open("/tmp/pointcloud_data.pcd", "wb") as f:
                f.write(data)
            pcd = o3d.io.read_point_cloud("/tmp/pointcloud_data.pcd")
            points = np.asarray(pcd.points)

        Returns:
            Tuple[bytes, str]: A tuple containing two values; the first [0] the pointcloud data,
            and the second [1] the mimetype of the pointcloud (for example, PCD).

        For more information, see `Camera component <https://docs.viam.com/components/camera/>`_.
        """
        ...

    @abc.abstractmethod
    async def get_properties(self, *, timeout: Optional[float] = None, **kwargs) -> Properties:
        """
        Get the camera intrinsic parameters and camera distortion parameters

        ::

            my_camera = Camera.from_robot(robot=robot, name="my_camera")

            properties = await my_camera.get_properties()

        Returns:
            Properties: The properties of the camera.

        For more information, see `Camera component <https://docs.viam.com/components/camera/>`_.
        """
        ...
