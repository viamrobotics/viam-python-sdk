from array import array
from enum import Enum
from io import BytesIO
from typing import List, NamedTuple, Optional, Union

from PIL import Image, UnidentifiedImageError
from typing_extensions import Self

from viam.errors import NotSupportedError
from viam.proto.component.camera import Format

from .viam_rgba_plugin import RGBA_FORMAT_LABEL

# Formats that are supported by PIL
LIBRARY_SUPPORTED_FORMATS = ["JPEG", "PNG", RGBA_FORMAT_LABEL]


class RawImage(NamedTuple):
    """**DEPRECATED** Use ``ViamImage`` instead

    A raw bytes representation of an image.

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
        if self.mime_type != CameraMimeType.VIAM_RAW_DEPTH.value:
            raise NotSupportedError("Type must be `image/vnd.viam.dep` to use bytes_to_depth_array()")

        width = int.from_bytes(self.data[8:16], "big")
        height = int.from_bytes(self.data[16:24], "big")
        depth_arr = array("H", self.data[24:])
        depth_arr.byteswap()

        depth_arr_2d = [[depth_arr[row * width + col] for col in range(width)] for row in range(height)]
        return depth_arr_2d


class CameraMimeType(str, Enum):
    VIAM_RGBA = "image/vnd.viam.rgba"
    VIAM_RAW_DEPTH = "image/vnd.viam.dep"
    JPEG = "image/jpeg"
    PNG = "image/png"
    PCD = "pointcloud/pcd"

    @classmethod
    def from_string(cls, value: str) -> Self:
        return cls(value)

    @classmethod
    def from_proto(cls, format: Format.ValueType) -> "CameraMimeType":
        """Returns the mimetype from a proto enum.

        Args:
            format (Format.ValueType): The mimetype in a proto enum.

        Returns:
            Self: The mimetype.
        """
        mimetypes = {
            Format.FORMAT_RAW_RGBA: CameraMimeType.VIAM_RGBA,
            Format.FORMAT_RAW_DEPTH: CameraMimeType.VIAM_RAW_DEPTH,
            Format.FORMAT_JPEG: CameraMimeType.JPEG,
            Format.FORMAT_PNG: CameraMimeType.PNG,
        }
        return mimetypes.get(format, CameraMimeType.JPEG)

    def to_proto(self) -> Format.ValueType:
        """Returns the mimetype in a proto enum.

        Returns:
            Format.ValueType: The mimetype in a proto enum.
        """
        formats = {
            self.VIAM_RGBA: Format.FORMAT_RAW_RGBA,
            self.VIAM_RAW_DEPTH: Format.FORMAT_RAW_DEPTH,
            self.JPEG: Format.FORMAT_JPEG,
            self.PNG: Format.FORMAT_PNG,
        }
        return formats.get(self, Format.FORMAT_UNSPECIFIED)


class ViamImage:
    """A native implementation of an image.

    Provides the raw data and the mime type, as well as lazily loading and caching the PIL.Image representation.
    """

    _height: Optional[int]
    _width: Optional[int]
    _data: bytes
    _mime_type: CameraMimeType
    _image: Optional[Image.Image] = None
    _image_decoded = False

    def __init__(self, data: bytes, mime_type: CameraMimeType) -> None:
        self._data = data
        self._mime_type = mime_type
        self._get_image_dimensions()

    @property
    def data(self) -> bytes:
        """The raw bytes of the image"""
        return self._data

    @property
    def mime_type(self) -> CameraMimeType:
        """The mime type of the image"""
        return self._mime_type

    @mime_type.setter
    def mime_type(self, value: CameraMimeType):
        if value == self.mime_type:
            return
        self._mime_type = value
        self.close()
        self._image_decoded = False
        self._image = None

    @property
    def width(self) -> Union[int, None]:
        """The width of the image"""
        return self._width

    @width.setter
    def width(self, width: int):
        self._width = width

    @property
    def height(self) -> Union[int, None]:
        """The height of the image"""
        return self._height

    @height.setter
    def height(self, height: int):
        self._height = height

    @property
    def image(self) -> Optional[Image.Image]:
        """The PIL.Image representation of the image. If the mime type is not supported, this will be None."""
        try:
            self._image = Image.open(BytesIO(self.data), formats=LIBRARY_SUPPORTED_FORMATS)
        except UnidentifiedImageError:
            self._image = None
        self._image_decoded = True
        return self._image

    def close(self):
        """Close the image and release resources."""
        if self._image is not None:
            self._image.close()

    def bytes_to_depth_array(self) -> List[List[int]]:
        """Decode the data of an image that has the custom depth MIME type ``image/vnd.viam.dep`` into
        a standard representation.

        Raises:
            NotSupportedError: Raised if given an image that is not of MIME type `image/vnd.viam.dep`.

        Returns:
            List[List[int]]: The standard representation of the image.
        """
        if self.mime_type != CameraMimeType.VIAM_RAW_DEPTH.value:
            raise NotSupportedError("Type must be `image/vnd.viam.dep` to use bytes_to_depth_array()")

        width = int.from_bytes(self.data[8:16], "big")
        height = int.from_bytes(self.data[16:24], "big")
        self.width = width
        self.height = height
        depth_arr = array("H", self.data[24:])
        depth_arr.byteswap()

        depth_arr_2d = [[depth_arr[row * width + col] for col in range(width)] for row in range(height)]
        return depth_arr_2d

    def _get_image_dimensions(self) -> None:
        """
        Get image dimensions from the data of an image that has the MIME type ``image/jpeg``, ``image/png``, or ``image/vnd.viam.rgba``.
        """

        if self.mime_type not in [CameraMimeType.JPEG, CameraMimeType.PNG, CameraMimeType.VIAM_RGBA]:
            return

        try:
            image = Image.open(BytesIO(self.data), formats=LIBRARY_SUPPORTED_FORMATS)
        except UnidentifiedImageError:
            return

        self._width = image.width
        self._height = image.height


class NamedImage(ViamImage):
    """An implementation of ViamImage that contains a name attribute."""

    name: str
    """The name of the image
    """

    def __init__(self, name: str, data: bytes, mime_type: CameraMimeType) -> None:
        self.name = name
        super().__init__(data, mime_type)
