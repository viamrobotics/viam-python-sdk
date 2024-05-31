from typing import ClassVar, Tuple

from PIL import Image
from PIL.ImageFile import ImageFile, PyDecoder, PyEncoder, _safe_read  # type: ignore -- (njooma) this exists, manually checked
from PIL.ImageFile import _save as image_save  # type: ignore -- (njooma) this exists, manually checked

from ...viam_rgba import RGBA_FORMAT_LABEL, RGBA_HEADER_LENGTH, RGBA_MAGIC_NUMBER


def _accept(prefix: str):
    return prefix[:4] == RGBA_MAGIC_NUMBER


class RGBAEncoder(PyEncoder):
    ENCODER_NAME = RGBA_FORMAT_LABEL

    _pushes_fd = True

    def encode(self, bufsize):  # pyright: ignore [reportIncompatibleMethodOverride]
        data_arr = bytearray()
        width, height = self.im.size
        for y in range(height):
            for x in range(width):
                data_arr.extend(self.im.getpixel((x, y)))
        data = bytes(data_arr)

        return len(data), 0, data


def _save_rgba(img, fp, filename):
    width, height = img.size
    fp.write(RGBA_MAGIC_NUMBER)
    fp.write(width.to_bytes(4, byteorder="big"))
    fp.write(height.to_bytes(4, byteorder="big"))

    image_save(img, fp, [(RGBAEncoder.ENCODER_NAME, (0, 0, width, height), 0, ("RGBA", 0, 1))])


class RGBAImage(ImageFile):
    format: ClassVar[str] = RGBA_FORMAT_LABEL  # pyright: ignore [reportIncompatibleVariableOverride]
    format_description = "Viam's Raw RGBA Format"

    def _open(self):
        header = self.fp.read(RGBA_HEADER_LENGTH)

        width = int.from_bytes(header[4:8], "big")
        height = int.from_bytes(header[8:12], "big")
        self._size = width, height
        if hasattr(self, "_mode"):
            self._mode = "RGBA"
        else:
            self.mode = "RGBA"  # type: ignore -- (njooma) newer versions of PIL hide this behind _mode, which is why we check

        # data descriptor
        self.tile = [(RGBAEncoder.ENCODER_NAME, (0, 0, width, height), RGBA_HEADER_LENGTH, (self.mode, 0, 1))]


class RGBADecoder(PyDecoder):
    _pulls_fd = True

    def decode(self, buffer) -> Tuple[int, int]:
        width, height = self.im.size
        self.set_as_raw(_safe_read(self.fd, width * height * 4))
        return -1, 0


# Register Viam's custom RGBA format so that it can be read using Image.open
Image.register_open(RGBAImage.format, RGBAImage, _accept)
Image.register_save(RGBAImage.format, _save_rgba)
Image.register_mime(RGBAImage.format, "image/vnd.viam.rgba")
Image.register_extension(RGBAImage.format, ".viam.rgba")
Image.register_encoder(RGBAEncoder.ENCODER_NAME, RGBAEncoder)
Image.register_decoder(RGBA_FORMAT_LABEL, RGBADecoder)
