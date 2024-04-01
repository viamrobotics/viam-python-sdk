from io import BytesIO
from PIL import Image

from viam.media.video import ViamImage

from .viam_rgba_plugin import RGBA_FORMAT_LABEL


LIBRARY_SUPPORTED_FORMATS = ["JPEG", "PNG", RGBA_FORMAT_LABEL]


def viam_to_pil_image(v_img: ViamImage) -> Image.Image:
    image = Image.open(BytesIO(v_img.data), formats=LIBRARY_SUPPORTED_FORMATS)
    return image
