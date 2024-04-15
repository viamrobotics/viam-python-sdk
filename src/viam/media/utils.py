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


def pil_to_viam_image(image: Image.Image, mime_type: CameraMimeType) -> ViamImage:
    """
    Convert a PIL.Image to a ViamImage.

    Args:
        image (Image.Image): The image to convert.
        mime_type (CameraMimeType): The mime type to convert the image to.

    Returns:
        ViamImage: The resulting ViamImage
    """
    if mime_type.name in LIBRARY_SUPPORTED_FORMATS:
        buf = BytesIO()
        if image.mode == "RGBA" and mime_type == CameraMimeType.JPEG:
            image = image.convert("RGB")
        image.save(buf, format=mime_type.name)
        data = buf.getvalue()
    else:
        raise ValueError(f"Cannot encode image to {mime_type}")

    return ViamImage(data, mime_type)


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
    if image.mime_type != CameraMimeType.VIAM_RAW_DEPTH:
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
    """
    if image.mime_type.name not in LIBRARY_SUPPORTED_FORMATS:
        return

    pil_img = viam_to_pil_image(image)
    image.width = pil_img.width
    image.height = pil_img.height
    pil_img.close()
