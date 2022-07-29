import abc
from typing import Tuple

from PIL.Image import Image
from viam.proto.api.component.camera import IntrinsicParameters

from ..component_base import ComponentBase


class Camera(ComponentBase):
    """
    Camera represents any physical hardware that can capture frames.

    This acts as an abstract base class for any drivers representing specific
    camera implementations. This cannot be used on its own. If the `__init__()` function is
    overriden, it must call the `super().__init__()` function.
    """

    @abc.abstractmethod
    async def get_frame(self) -> Image:
        """
        Get the next frame from the camera as an Image.
        Be sure to close the image when finished.

        Returns:
            Image: The frame.
        """
        ...

    @abc.abstractmethod
    async def get_point_cloud(self) -> Tuple[bytes, str]:
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
    async def get_properties(self) -> IntrinsicParameters:
        """
        Get the camera intrinsic parameters and camera distortion parameters

        Returns:
            IntrinsicParameters: The properties of the camera
        """
        ...
