from .viam_rgba_plugin import RGBA_FORMAT_LABEL, RGBA_MAGIC_NUMBER
from enum import Enum
from io import BytesIO
from typing import NamedTuple, Union, Tuple
from PIL.Image import Image

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


class CameraMimeType(str, Enum):
    VIAM_RGBA = "image/vnd.viam.rgba"
    JPEG = "image/jpeg"
    PNG = "image/png"
    PCD = "pointcloud/pcd"
    UNSUPPORTED = "unsupported"

    @classmethod
    def extract_from_lazy(cls, value: str) -> Tuple["CameraMimeType", bool]:
        is_lazy = False
        mime_type = value
        if value.endswith(LAZY_SUFFIX):
            mime_type = value[: (len(value) - len(LAZY_SUFFIX))]
            is_lazy = True
        if not cls.is_supported(value) and not is_lazy:
            mime_type = CameraMimeType(CameraMimeType.UNSUPPORTED)
        return (cls(mime_type), is_lazy)

    def encode_image(self, image: Union[Image, RawImage]) -> bytes:
        if isinstance(image, RawImage):
            return image.data

        if self == CameraMimeType.VIAM_RGBA:
            data = bytearray()
            width, height = image.size
            data.extend(RGBA_MAGIC_NUMBER)
            data.extend(width.to_bytes(4, byteorder="big"))
            data.extend(height.to_bytes(4, byteorder="big"))
            for y in range(height):
                for x in range(width):
                    data.extend(image.getpixel((x, y)))
            return bytes(data)
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
        if mime_type == cls.UNSUPPORTED:
            return False
        return mime_type in set(item.value for item in cls)
