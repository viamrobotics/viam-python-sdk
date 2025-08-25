import os
from array import array
from io import BytesIO

import pytest
from PIL import Image

from viam.errors import NotSupportedError
from viam.media.utils.pil import pil_to_viam_image, viam_to_pil_image
from viam.media.video import CameraMimeType, NamedImage, ViamImage


class TestViamImage:
    def test_supported_image(self):
        i = Image.new("RGBA", (100, 100), "#AABBCCDD")
        b = BytesIO()
        i.save(b, "PNG")
        img = ViamImage(b.getvalue(), CameraMimeType.PNG)
        assert img._mime_type == "image/png"
        pil_img = viam_to_pil_image(img)
        assert pil_img.tobytes() == i.tobytes()

    def test_dimensions(self):
        WIDTH = 400
        HEIGHT = 300
        i = Image.new("RGBA", (WIDTH, HEIGHT), "#AABBCCDD")

        img1 = pil_to_viam_image(i, CameraMimeType.JPEG)
        assert img1.width == WIDTH
        assert img1.height == HEIGHT

        img2 = pil_to_viam_image(i, CameraMimeType.PNG)
        assert img2.width == WIDTH
        assert img2.height == HEIGHT

        img3 = pil_to_viam_image(i, CameraMimeType.VIAM_RGBA)
        assert img3.width == WIDTH
        assert img3.height == HEIGHT

        img4 = ViamImage(b"data", CameraMimeType.PCD)
        assert img4.width is None
        assert img4.height is None

    def test_bytes_to_depth_array(self):
        with open(f"{os.path.dirname(__file__)}/data/fakeDM.vnd.viam.dep", "rb") as depth_map:
            img = ViamImage(depth_map.read(), CameraMimeType.VIAM_RAW_DEPTH)
        assert isinstance(img, ViamImage)
        standard_data = img.bytes_to_depth_array()
        assert len(standard_data) == 10
        assert len(standard_data[0]) == 20
        data_arr = array("H", img.data[24:])
        data_arr.byteswap()
        assert len(data_arr) == 200
        assert standard_data[0][0] == data_arr[0]
        assert standard_data[-1][3] == data_arr[183]
        assert standard_data[-1][3] == 9 * 3
        assert standard_data[4][4] == 4 * 4

        img2 = ViamImage(b"data", CameraMimeType.PCD)
        with pytest.raises(NotSupportedError):
            img2.bytes_to_depth_array()


class TestNamedImage:
    def test_name(self):
        name = "img"
        img = NamedImage(name, b"123", CameraMimeType.JPEG)
        assert img.name == name


def test_image_conversion():
    i = Image.new("RGBA", (100, 100), "#AABBCCDD")

    v_img = pil_to_viam_image(i, CameraMimeType.JPEG)
    assert isinstance(v_img, ViamImage)
    assert v_img.mime_type == "image/jpeg"

    pil_img = viam_to_pil_image(v_img)
    v_img2 = pil_to_viam_image(pil_img, CameraMimeType.JPEG)
    assert v_img2.data == v_img.data
