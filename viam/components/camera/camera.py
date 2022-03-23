import abc
from typing import Tuple

from PIL.Image import Image

from ..component_base import ComponentBase


class Camera(ComponentBase):
    """
    Abstract camera representing anything that can capture frames

    If you override the init function,
    you must call the super init function.
    """

    @abc.abstractmethod
    async def next(self) -> Image:
        """
        Get the next frame from the camera as an Image.
        Be sure to close the image when finished.

        Returns:
            Image: The next frame
        """
        ...

    @abc.abstractmethod
    async def next_point_cloud(self) -> Tuple[bytes, str]:
        """
        Get the next point cloud from the camera. This will be
        returned as bytes with a mimetype describing
        the structure of the data. The consumer of this call
        should encode the bytes into the formatted suggested
        by the mimetype

        Returns:
            bytes: The pointcloud data
            str: The mimetype of the pointcloud (e.g. PCD)
        """
        ...
