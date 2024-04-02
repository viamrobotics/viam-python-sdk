import os
from array import array
from io import BytesIO

from PIL import Image

from viam.media.utils import bytes_to_depth_array, get_image_dimensions, viam_to_pil_image
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

    def test_mime_type_update(self):
        i = Image.new("RGBA", (100, 100), "#AABBCCDD")
        b = BytesIO()
        i.save(b, "PNG")
        img = ViamImage(b.getvalue(), CameraMimeType.PNG)
        assert img._mime_type == CameraMimeType.PNG

        img.mime_type = CameraMimeType.JPEG
        assert img._mime_type == CameraMimeType.JPEG
        img.close()


class TestNamedImage:
    def test_name(self):
        name = "img"
        img = NamedImage(name, b"123", CameraMimeType.JPEG)
        assert img.name == name


def test_viam_to_pil_image():
    i = Image.new("RGBA", (100, 100), "#AABBCCDD")
    b = BytesIO()
    i.save(b, "PNG")
    img = ViamImage(b.getvalue(), CameraMimeType.JPEG)
    pil_img = viam_to_pil_image(img)
    assert pil_img.tobytes() == i.tobytes()


def test_bytes_to_depth_array():
    with open(f"{os.path.dirname(__file__)}/../data/fakeDM.vnd.viam.dep", "rb") as depth_map:
        image = ViamImage(depth_map.read(), CameraMimeType.VIAM_RAW_DEPTH)
    assert isinstance(image, ViamImage)
    standard_data = bytes_to_depth_array(image)
    assert len(standard_data) == 10
    assert len(standard_data[0]) == 20
    data_arr = array("H", image.data[24:])
    data_arr.byteswap()
    assert len(data_arr) == 200
    assert standard_data[0][0] == data_arr[0]
    assert standard_data[-1][3] == data_arr[183]
    assert standard_data[-1][3] == 9 * 3
    assert standard_data[4][4] == 4 * 4
