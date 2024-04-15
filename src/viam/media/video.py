from enum import Enum
from typing import Optional, Union

from typing_extensions import Self

from viam.proto.component.camera import Format


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

    _height: Optional[int]
    _width: Optional[int]
    _data: bytes
    _mime_type: CameraMimeType

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


class NamedImage(ViamImage):
    """An implementation of ViamImage that contains a name attribute."""

    name: str
    """The name of the image
    """

    def __init__(self, name: str, data: bytes, mime_type: CameraMimeType) -> None:
        self.name = name
        super().__init__(data, mime_type)
