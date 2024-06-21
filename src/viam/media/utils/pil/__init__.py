from io import BytesIO

from PIL import Image

from ....media.video import CameraMimeType, ViamImage
from .viam_rgba_plugin import RGBA_FORMAT_LABEL

# Formats that are supported by PIL
LIBRARY_SUPPORTED_FORMATS = ["JPEG", "PNG", RGBA_FORMAT_LABEL]


def viam_to_pil_image(image: ViamImage) -> Image.Image:
    """
    Convert a ViamImage to a PIL.Image.

    In order to use this function, Pillow must be installed.
    https://python-pillow.org/

    Args:
        image (ViamImage): The image to convert.

    Returns:
        Image.Image: The resulting PIL.Image
    """
    return Image.open(BytesIO(image.data), formats=LIBRARY_SUPPORTED_FORMATS)


def pil_to_viam_image(image: Image.Image, mime_type: CameraMimeType) -> ViamImage:
    """
    Convert a PIL.Image to a ViamImage.

    In order to use this function, Pillow must be installed.
    https://python-pillow.org/

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
