from array import array
from io import BytesIO
from typing import List

from PIL import Image

from viam.errors import NotSupportedError
from viam.media.video import CameraMimeType, ViamImage

from .viam_rgba_plugin import RGBA_FORMAT_LABEL

# Formats that are supported by PIL
LIBRARY_SUPPORTED_FORMATS = ["JPEG", "PNG", RGBA_FORMAT_LABEL]


def viam_to_pil_image(image: ViamImage) -> Image.Image:
    """
    Convert a ViamImage to a PIL.Image.

    Args:
        image (ViamImage): The image to convert.

    Returns:
        Image.Image: The resulting PIL.Image
    """
    return Image.open(BytesIO(image.data), formats=LIBRARY_SUPPORTED_FORMATS)


def bytes_to_depth_array(image: ViamImage) -> List[List[int]]:
    """
    Decode the data of an image that has the custom depth MIME type ``image/vnd.viam.dep`` into a standard representation.

    Args:
        image (ViamImage): The image to be decoded.

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


def determine_image_dimensions(image: ViamImage) -> None:
    """
    Get image dimensions from the data of an image that has the MIME type ``image/jpeg``, ``image/png``, or ``image/vnd.viam.rgba`` and set
    the corresponding properties of the image.

    Alternatively, image dimensions can be set manually as well (i.e.: image.width = 100)

    Args:
        image (ViamImage): The image to get dimensions of.

    Raises:
        NotSupportedError: Raised if given an image that is not of MIME type `image/vnd.viam.dep`.
    """
    if image.mime_type not in [CameraMimeType.JPEG, CameraMimeType.PNG, CameraMimeType.VIAM_RGBA]:
        raise NotSupportedError("Type must be `image/jpeg`, `image/png`, or `image/vnd.viam.rgba` to use determine_image_dimensions()")

    pil_img = viam_to_pil_image(image)
    image.width = pil_img.width
    image.height = pil_img.height
    pil_img.close()
