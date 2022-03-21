import abc
from typing import Callable, Tuple

from PIL.Image import Image

from ..component_base import ComponentBase


class Camera(ComponentBase):
    """
    Abstract camera representing anything that can capture frames

    If you override the init function,
    you must call the super init function.
    """

    @abc.abstractmethod
    async def next(self) -> Tuple[Image, Callable]:
        """
        Return an image along with a function to release
        the image once it is no longer used.

        Returns:
            Tuple[Image, Callable]: An image and a function to release it
        """
        ...
