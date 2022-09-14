import abc
from typing import NamedTuple, Tuple, Union

from PIL.Image import Image
from viam.components.types import CameraMimeType, RawImage
from viam.proto.component.camera import IntrinsicParameters, DistortionParameters

from ..component_base import ComponentBase


class Camera(ComponentBase):
    """
    Camera represents any physical hardware that can capture frames.

    This acts as an abstract base class for any drivers representing specific
    camera implementations. This cannot be used on its own. If the `__init__()` function is
    overridden, it must call the `super().__init__()` function.
    """

    class Properties(NamedTuple):
        """The camera's supported features and settings"""

        supports_pcd: bool
        """Whether the camera has a valid implementation of `get_point_cloud`"""

        intrinsic_parameters: IntrinsicParameters
        """The properties of the camera"""

        distortion_parameters: DistortionParameters
        """The distortion parameters of the camera"""

    @abc.abstractmethod
    async def get_image(self, mime_type: str = CameraMimeType.PNG, **kwargs) -> Union[Image, RawImage]:
        """Get the next image from the camera as an Image or RawImage.
        Be sure to close the image when finished.

        Args:
            mime_type (str): The desired mime type of the image. This does not guarantee output type

        Returns:
            Image | RawImage: The frame
        """
        ...

    @abc.abstractmethod
    async def get_point_cloud(self, **kwargs) -> Tuple[bytes, str]:
        """
        Get the next point cloud from the camera. This will be
        returned as bytes with a mimetype describing
        the structure of the data. The consumer of this call
        should encode the bytes into the formatted suggested
        by the mimetype.

        Returns:
            bytes: The pointcloud data.
            str: The mimetype of the pointcloud (e.g. PCD).
        """
        ...

    @abc.abstractmethod
    async def get_properties(self, **kwargs) -> Properties:
        """
        Get the camera intrinsic parameters and camera distortion parameters

        Returns:
            Properties: The properties of the camera
        """
        ...
