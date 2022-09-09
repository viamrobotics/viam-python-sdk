from enum import Enum
from io import BytesIO
from typing import NamedTuple, Union

from PIL.Image import Image


class RawImage(NamedTuple):
    """A raw bytes representation of an image.

    When requesting `CameraMimeType.RAW` or if the camera returns a mime type that is not supported,
    the returned type will be this RawImage type.
    """

    data: bytes
    """The raw data of the image"""

    mime_type: str
    """The mimetype of the image"""

    width: int
    """The width of the image"""

    height: int
    """The height of the image"""

    def close(self):
        """Close the image and release resources. For RawImage, this is a noop."""
        return


class CameraMimeType(str, Enum):
    RAW = "image/vnd.viam.rgba"
    JPEG = "image/jpeg"
    PNG = "image/png"
    PCD = "pointcloud/pcd"

    def encode_image(self, image: Union[Image, RawImage]) -> bytes:
        if isinstance(image, RawImage):
            return image.data
        if self == CameraMimeType.JPEG:
            buf = BytesIO()
            image.save(buf, format="JPEG")
            return buf.getvalue()
        if self == CameraMimeType.PNG:
            buf = BytesIO()
            image.save(buf, format="PNG")
            return buf.getvalue()
        else:
            raise ValueError(f"Cannot encode image to {self}")

    @classmethod
    def is_supported(cls, mime_type: str) -> bool:
        """Check if the provided mime_type is supported

        Args:
            mime_type (str): The mime_type to check

        Returns:
            bool: Whether the mime_type is supported
        """
        return mime_type in set(item.value for item in cls)
