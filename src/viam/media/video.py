from array import array
from enum import Enum
from io import BytesIO
from typing import List, Optional, Union

from PIL import Image, UnidentifiedImageError
from typing_extensions import Self

from viam.errors import NotSupportedError
from viam.proto.component.camera import Format

from .viam_rgba_plugin import RGBA_FORMAT_LABEL

# Formats that are supported by PIL
LIBRARY_SUPPORTED_FORMATS = ["JPEG", "PNG", RGBA_FORMAT_LABEL]


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

    Provides the raw data and the mime type.
    """

    _data: bytes
    _mime_type: CameraMimeType
    _image: Optional[Image.Image] = None
    _image_decoded = False
    _height: Optional[int] = None
    _width: Optional[int] = None

    def __init__(self, data: bytes, mime_type: CameraMimeType) -> None:
        self._data = data
        self._mime_type = mime_type

    @property
    def data(self) -> bytes:
        """The raw bytes of the image"""
        return self._data

    @property
    def mime_type(self) -> CameraMimeType:
        """The mime type of the image"""
        return self._mime_type

    @property
    def width(self) -> Union[int, None]:
        """The width of the image"""
        if self._width is not None:
            return self._width

        if not self._image_decoded:
            try:
                self._image = Image.open(BytesIO(self.data), formats=LIBRARY_SUPPORTED_FORMATS)
            except UnidentifiedImageError:
                self._image = None
            self._image_decoded = True
        # If we have decoded the image and the image is not none, then set the width so we don't have to do this again
        if self._image_decoded and self._image is not None:
            self._width = self._image.width
        return self._width

    @property
    def height(self) -> Union[int, None]:
        """The height of the image"""
        if self._height is not None:
            return self._height

        if not self._image_decoded:
            try:
                self._image = Image.open(BytesIO(self.data), formats=LIBRARY_SUPPORTED_FORMATS)
            except UnidentifiedImageError:
                self._image = None
            self._image_decoded = True
        # If we have decoded the image and the image is not none, then set the height so we don't have to do this again
        if self._image_decoded and self._image is not None:
            self._height = self._image.height
        return self._height

    def bytes_to_depth_array(self) -> List[List[int]]:
        """
        Decode the data of an image that has the custom depth MIME type ``image/vnd.viam.dep`` into a standard representation.

        Raises:
            NotSupportedError: Raised if the image is not of MIME type `image/vnd.viam.dep`.

        Returns:
            List[List[int]]: The standard representation of the image.
        """
        if self.mime_type != CameraMimeType.VIAM_RAW_DEPTH:
            raise NotSupportedError("Type must be `image/vnd.viam.dep` to use bytes_to_depth_array()")

        self._width = int.from_bytes(self.data[8:16], "big")
        self._height = int.from_bytes(self.data[16:24], "big")
        depth_arr = array("H", self.data[24:])
        depth_arr.byteswap()

        depth_arr_2d = [[depth_arr[row * self._width + col] for col in range(self._width)] for row in range(self._height)]
        return depth_arr_2d


class NamedImage(ViamImage):
    """An implementation of ViamImage that contains a name attribute."""

    name: str
    """The name of the image
    """

    def __init__(self, name: str, data: bytes, mime_type: CameraMimeType) -> None:
        self.name = name
        super().__init__(data, mime_type)
