import os
from array import array
from io import BytesIO

import pytest
from PIL import Image

from viam.errors import NotSupportedError
from viam.media.utils import bytes_to_depth_array, determine_image_dimensions, pil_to_viam_image, viam_to_pil_image
from viam.media.video import CameraMimeType, NamedImage, ViamImage


class TestViamImage:
    def test_supported_image(self):
        i = Image.new("RGBA", (100, 100), "#AABBCCDD")
        b = BytesIO()
        i.save(b, "PNG")
        img = ViamImage(b.getvalue(), CameraMimeType.PNG)
        assert img._mime_type == CameraMimeType.PNG
        pil_img = viam_to_pil_image(img)
        assert pil_img.tobytes() == i.tobytes()

    def test_set_image_dimensions(self):
        img = ViamImage(b"data", CameraMimeType.JPEG)
        with pytest.raises(AttributeError):
            img.width
        with pytest.raises(AttributeError):
            img.height
        img.width = 100
        img.height = 100
        assert img.width == 100
        assert img.height == 100


class TestNamedImage:
    def test_name(self):
        name = "img"
        img = NamedImage(name, b"123", CameraMimeType.JPEG)
        assert img.name == name


def test_image_conversion():
    i = Image.new("RGBA", (100, 100), "#AABBCCDD")

    v_img = pil_to_viam_image(i, CameraMimeType.JPEG)
    assert isinstance(v_img, ViamImage)
    assert v_img.mime_type == CameraMimeType.JPEG

    pil_img = viam_to_pil_image(v_img)
    v_img2 = pil_to_viam_image(pil_img, CameraMimeType.JPEG)
    assert v_img2.data == v_img.data


def test_bytes_to_depth_array():
    with open(f"{os.path.dirname(__file__)}/../data/fakeDM.vnd.viam.dep", "rb") as depth_map:
        img = ViamImage(depth_map.read(), CameraMimeType.VIAM_RAW_DEPTH)
    assert isinstance(img, ViamImage)
    standard_data = bytes_to_depth_array(img)
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
        bytes_to_depth_array(img2)


def test_determine_image_dimensions():
    i = Image.new("RGBA", (100, 100), "#AABBCCDD")
    b = BytesIO()
    i.save(b, "PNG")
    img = ViamImage(b.getvalue(), CameraMimeType.PNG)
    with pytest.raises(AttributeError):
        img.width
    with pytest.raises(AttributeError):
        img.height
    determine_image_dimensions(img)
    assert img.width == 100
    assert img.height == 100

    i2 = Image.new("RGBA", (100, 100), "#AABBCCDD")
    b2 = BytesIO()
    i2.save(b2, "VIAM_RGBA")
    img2 = ViamImage(b.getvalue(), CameraMimeType.VIAM_RGBA)
    with pytest.raises(AttributeError):
        img2.width
    with pytest.raises(AttributeError):
        img2.height
    determine_image_dimensions(img2)
    assert img2.width == 100
    assert img2.height == 100

    i3 = Image.new("RGB", (100, 100), "#AABBCCDD")
    b3 = BytesIO()
    i3.save(b3, "JPEG")
    img3 = ViamImage(b.getvalue(), CameraMimeType.JPEG)
    with pytest.raises(AttributeError):
        img3.width
    with pytest.raises(AttributeError):
        img3.height
    determine_image_dimensions(img3)
    assert img3.width == 100
    assert img3.height == 100

    img4 = ViamImage(b"data", CameraMimeType.PCD)
    with pytest.raises(AttributeError):
        img4.width
    with pytest.raises(AttributeError):
        img4.height
    determine_image_dimensions(img4)
    with pytest.raises(AttributeError):
        img4.width
    with pytest.raises(AttributeError):
        img4.height
