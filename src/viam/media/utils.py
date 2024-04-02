import struct
from array import array
from io import BytesIO
from typing import List

from PIL import Image

from viam.errors import NotSupportedError, ViamError
from viam.media.video import CameraMimeType, ViamImage

from .viam_rgba_plugin import RGBA_FORMAT_LABEL

# Formats that are supported by PIL
LIBRARY_SUPPORTED_FORMATS = ["JPEG", "PNG", RGBA_FORMAT_LABEL]


def viam_to_pil_image(image: ViamImage) -> Image.Image:
    return Image.open(BytesIO(image.data), formats=LIBRARY_SUPPORTED_FORMATS)


def bytes_to_depth_array(image: ViamImage) -> List[List[int]]:
    """Decode the data of an image that has the custom depth MIME type ``image/vnd.viam.dep`` into
    a standard representation.

    Raises:
        NotSupportedError: Raised if given an image that is not of MIME type `image/vnd.viam.dep`.

    Returns:
        List[List[int]]: The standard representation of the image.
    """
    if image.mime_type != CameraMimeType.VIAM_RAW_DEPTH.value:
        raise NotSupportedError("Type must be `image/vnd.viam.dep` to use bytes_to_depth_array()")

    width = int.from_bytes(image.data[8:16], "big")
    height = int.from_bytes(image.data[16:24], "big")
    image.width = width
    image.height = height
    depth_arr = array("H", image.data[24:])
    depth_arr.byteswap()

    depth_arr_2d = [[depth_arr[row * width + col] for col in range(width)] for row in range(height)]
    return depth_arr_2d


def get_image_dimensions(image: ViamImage) -> None:
    """
    Get image dimensions from the data of an image that has the MIME type ``image/jpeg``, ``image/png``, or ``image/vnd.viam.rgba``.
    """
    data = str(image.data)
    size = len(image.data)
    if image.mime_type not in [CameraMimeType.JPEG, CameraMimeType.PNG, CameraMimeType.VIAM_RGBA]:
        NotSupportedError("Type must be `image/jpeg`, `image/png`, or `image/vnd.viam.rgba` to use get_image_dimensions()")

    # See PNG 2. Edition spec (http://www.w3.org/TR/PNG/)
    # Bytes 0-7 are below, 4-byte chunk length, then 'IHDR'
    # and finally the 4-byte width, height
    if (size >= 24) and data.startswith("\211PNG\r\n\032\n") and (data[12:16] == "IHDR"):
        w, h = struct.unpack(">LL", image.data[16:24])
        image.width = int(w)
        image.height = int(h)
        return
    # This is for an older PNG version.
    elif (size >= 16) and data.startswith("\211PNG\r\n\032\n"):
        # Check to see if we have the right content type
        w, h = struct.unpack(">LL", image.data[8:16])
        image.width = int(w)
        image.height = int(h)
        return
    # handle JPEGs
    elif (size >= 2) and data.startswith("\377\330"):
        jpeg = BytesIO(image.data)
        jpeg.read(2)
        b = jpeg.read(1)
        try:
            while b and ord(b) != 0xDA:
                while ord(b) != 0xFF:
                    b = jpeg.read(1)
                while ord(b) == 0xFF:
                    b = jpeg.read(1)
                if ord(b) >= 0xC0 and ord(b) <= 0xC3:
                    jpeg.read(3)
                    h, w = struct.unpack(">HH", jpeg.read(4))
                    break
                else:
                    jpeg.read(int(struct.unpack(">H", jpeg.read(2))[0]) - 2)
                b = jpeg.read(1)
            image.width = int(w)
            image.height = int(h)
            return
        except struct.error:
            pass
        except ValueError:
            pass

    raise ViamError(f"Could not find image dimensions of image {image}")
