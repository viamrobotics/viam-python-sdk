from enum import Enum
from io import BytesIO

from PIL.Image import Image


class CameraMimeType(str, Enum):
    RAW = "image/raw-rgba"
    JPEG = "image/jpeg"
    PNG = "image/png"
    PCD = "pointcloud/pcd"

    def encode_image(self, image: Image) -> bytes:
        if self == CameraMimeType.RAW:
            return image.convert("RGBA").tobytes("raw", "RGBA")
        elif self == CameraMimeType.JPEG:
            buf = BytesIO()
            image.save(buf, format="JPEG")
            return buf.getvalue()
        elif self == CameraMimeType.PNG:
            buf = BytesIO()
            image.save(buf, format="PNG")
            return buf.getvalue()
        else:
            raise ValueError(f"Cannot encode image to {self}")
