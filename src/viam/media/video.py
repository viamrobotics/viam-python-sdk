from array import array
from enum import Enum
from io import BytesIO
from typing import List, NamedTuple, Tuple, Union

from PIL.Image import Image
from typing_extensions import Self

from viam.errors import NotSupportedError

from .viam_rgba_plugin import RGBA_FORMAT_LABEL

LAZY_SUFFIX = "+lazy"

# Formats that are supported by PIL
LIBRARY_SUPPORTED_FORMATS = ["JPEG", "PNG", RGBA_FORMAT_LABEL]


class RawImage(NamedTuple):
    """A raw bytes representation of an image.

    A RawImage should be returned instead of a PIL Image instance under one of
    the following conditions

    1) The requested mime type has the LAZY_SUFFIX string appended to it
    2) The requested mime type is not supported for decoding/encoding by Viam's
    Python SDK
    """

    data: bytes
    """The raw data of the image"""

    mime_type: str
    """The mimetype of the image"""

    def close(self):
        """Close the image and release resources. For RawImage, this is a noop."""
        return

    def bytes_to_depth_array(self) -> List[List[int]]:
        """Decode the data of an image that has the custom depth MIME type ``image/vnd.viam.dep`` into
        a standard representation.

        Raises:
            NotSupportedError: Raised if given an image that is not of MIME type `image/vnd.viam.dep`.

        Returns:
            List[List[int]]: The standard representation of the image.
        """
        if self.mime_type != "image/vnd.viam.dep":
            raise NotSupportedError("Type must be `image/vnd.viam.dep` to use bytes_to_depth_array()")

        width = int.from_bytes(self.data[8:16], "big")
        height = int.from_bytes(self.data[16:24], "big")
        depth_arr = array("H", self.data[24:])
        depth_arr.byteswap()

        depth_arr_2d = [[depth_arr[row * width + col] for col in range(width)] for row in range(height)]
        return depth_arr_2d


class CameraMimeType(str, Enum):
    VIAM_RGBA = "image/vnd.viam.rgba"
    JPEG = "image/jpeg"
    PNG = "image/png"
    PCD = "pointcloud/pcd"
    UNSUPPORTED = "unsupported"

    @classmethod
    def from_lazy(cls, value: str) -> Tuple[Self, bool]:
        is_lazy = False
        mime_type = value
        if value.endswith(LAZY_SUFFIX):
            mime_type = value[: (len(value) - len(LAZY_SUFFIX))]
            is_lazy = True
        if not cls.is_supported(value) and not is_lazy:
            mime_type = CameraMimeType.UNSUPPORTED
        return (cls(mime_type), is_lazy)

    @property
    def with_lazy_suffix(self) -> str:
        return f"{self.value}{LAZY_SUFFIX}"

    def encode_image(self, image: Union[Image, RawImage]) -> bytes:
        if isinstance(image, RawImage):
            return image.data

        if self.name in LIBRARY_SUPPORTED_FORMATS:
            buf = BytesIO()
            image.save(buf, format=self.name)
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
        if mime_type == cls.UNSUPPORTED:
            return False
        return mime_type in set(item.value for item in cls)
