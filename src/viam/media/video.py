from array import array
from enum import Enum
from typing import List, Optional, Tuple

from typing_extensions import Self

from viam.errors import NotSupportedError
from viam.proto.component.camera import Format

from .viam_rgba import RGBA_HEADER_LENGTH, RGBA_MAGIC_NUMBER


class CameraMimeType(str, Enum):
    VIAM_RGBA = "image/vnd.viam.rgba"
    VIAM_RAW_DEPTH = "image/vnd.viam.dep"
    JPEG = "image/jpeg"
    PNG = "image/png"
    PCD = "pointcloud/pcd"

    @classmethod
    def from_string(cls, value: str) -> Self:
        """Return the mimetype from a string.

        Args:
            value (str): The mimetype as a string

        Returns:
            Self: The mimetype
        """
        value_mime = value[:-5] if value.endswith("+lazy") else value  # ViamImage lazy encodes by default
        return cls(value_mime)

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
    _height: Optional[int] = None
    _width: Optional[int] = None

    def __init__(self, data: bytes, mime_type: CameraMimeType) -> None:
        self._data = data
        self._mime_type = mime_type
        self._width, self._height = _getDimensions(data, mime_type)

    @property
    def data(self) -> bytes:
        """The raw bytes of the image"""
        return self._data

    @property
    def mime_type(self) -> CameraMimeType:
        """The mime type of the image"""
        return self._mime_type

    @property
    def width(self) -> Optional[int]:
        """The width of the image"""
        return self._width

    @property
    def height(self) -> Optional[int]:
        """The height of the image"""
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


def _getDimensions(image: bytes, mime_type: CameraMimeType) -> Tuple[Optional[int], Optional[int]]:
    try:
        if mime_type == CameraMimeType.JPEG:
            return _getDimensionsFromJPEG(image)
        if mime_type == CameraMimeType.PNG:
            return _getDimensionsFromPNG(image)
        if mime_type == CameraMimeType.VIAM_RGBA:
            return _getDimensionsFromRGBA(image)
    except ValueError:
        return (None, None)
    return (None, None)


def _getDimensionsFromJPEG(image: bytes) -> Tuple[int, int]:
    # JPEG Specification: https://www.w3.org/Graphics/JPEG/itu-t81.pdf
    # Specification for markers: Table B.1

    offset = 0
    while offset < len(image):
        while image[offset] == 0xFF:
            # Skip all 0xFF bytes
            offset += 1

        marker = image[offset]
        offset += 1
        if marker == 0x01:
            # Temporary/private use marker
            offset += 1
            continue
        if marker in range(0xD0, 0xD7):
            # Restart (RST) marker
            offset += 1
            continue
        if marker == 0xD8:
            # Start of image (SOI) marker
            offset += 1
            continue
        if marker == 0xD9:
            # End of image (EOI) marker
            break

        length = int.from_bytes(image[offset : offset + 1], byteorder="big")  # length of section
        if marker == 0xC0 or marker == 0xC2:
            height = int.from_bytes(image[offset + 3 : offset + 5], byteorder="big")
            width = int.from_bytes(image[offset + 5 : offset + 7], byteorder="big")
            return (width, height)

        offset += length

    raise ValueError("Invalid JPEG: Could not extract dimensions")


def _getDimensionsFromPNG(image: bytes) -> Tuple[int, int]:
    # PNG Specification: https://www.w3.org/TR/png/

    # PNG will always start with this signature
    signature = image[:8]
    if signature != [0x89, 0x50, 0x4E, 0x47, 0x0D, 0x0A, 0x1A, 0x0A]:
        ValueError("Invalid PNG: Invalid signature")

    header = image[12:24]
    chunk_type = header[:4].decode()
    if chunk_type != "IHDR":
        ValueError("Invalid PNG: Invalid headers")

    width = int.from_bytes(header[4:8], byteorder="big")
    height = int.from_bytes(header[8:], byteorder="big")
    return (width, height)


def _getDimensionsFromRGBA(image: bytes) -> Tuple[int, int]:
    # Viam RGBA header comes in 3 4-byte chunks:
    # * Magic Number/Signature
    # * Width
    # * Height
    header = image[:RGBA_HEADER_LENGTH]
    if header[:4] != RGBA_MAGIC_NUMBER:
        raise ValueError("Invalid Viam RGBA: Invalid headers")

    width = int.from_bytes(header[4:8], byteorder="big")
    height = int.from_bytes(header[8:], byteorder="big")
    return (width, height)
