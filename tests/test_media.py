import os
from array import array
from io import BytesIO

from PIL import Image

from viam.media.video import CameraMimeType, NamedImage, RawImage, ViamImage


class TestRawImage:
    def test_bytes_to_depth_array(self):
        with open(f"{os.path.dirname(__file__)}/../data/fakeDM.vnd.viam.dep", "rb") as depth_map:
            image = RawImage(depth_map.read(), "image/vnd.viam.dep")
        assert isinstance(image, RawImage)
        standard_data = image.bytes_to_depth_array()
        assert len(standard_data) == 10
        assert len(standard_data[0]) == 20
        data_arr = array("H", image.data[24:])
        data_arr.byteswap()
        assert len(data_arr) == 200
        assert standard_data[0][0] == data_arr[0]
        assert standard_data[-1][3] == data_arr[183]
        assert standard_data[-1][3] == 9 * 3
        assert standard_data[4][4] == 4 * 4


class TestViamImage:
    def test_unsupported_image(self):
        img = ViamImage(b"123", CameraMimeType.UNSUPPORTED)
        assert img._image is None
        assert img._image_decoded is False
        assert img.image is None
        assert img._image is None
        assert img._image_decoded is True
        img.close()

    def test_supported_image(self):
        i = Image.new("RGBA", (100, 100), "#AABBCCDD")
        b = BytesIO()
        i.save(b, "PNG")
        img = ViamImage(b.getvalue(), CameraMimeType.PNG)
        assert img._image is None
        assert img._image_decoded is False
        assert img.image is not None
        assert img.image.tobytes() == i.tobytes()
        assert img._image_decoded is True
        img.close()

    def test_mime_type_update(self):
        i = Image.new("RGBA", (100, 100), "#AABBCCDD")
        b = BytesIO()
        i.save(b, "PNG")
        img = ViamImage(b.getvalue(), CameraMimeType.PNG)

        assert img._mime_type == CameraMimeType.PNG
        assert img._image is None
        assert img._image_decoded is False
        assert img.image is not None
        assert img._image is not None
        assert img._image_decoded is True

        img.mime_type = CameraMimeType.JPEG
        assert img._mime_type == CameraMimeType.JPEG
        assert img._image is None
        assert img._image_decoded is False
        assert img.image is not None
        assert img._image is not None
        assert img._image_decoded is True
        img.close()

    def test_bytes_to_depth_array(self):
        with open(f"{os.path.dirname(__file__)}/../data/fakeDM.vnd.viam.dep", "rb") as depth_map:
            image = RawImage(depth_map.read(), "image/vnd.viam.dep")
        assert isinstance(image, RawImage)
        standard_data = image.bytes_to_depth_array()
        assert len(standard_data) == 10
        assert len(standard_data[0]) == 20
        data_arr = array("H", image.data[24:])
        data_arr.byteswap()
        assert len(data_arr) == 200
        assert standard_data[0][0] == data_arr[0]
        assert standard_data[-1][3] == data_arr[183]
        assert standard_data[-1][3] == 9 * 3
        assert standard_data[4][4] == 4 * 4


class TestNamedImage:
    def test_name(self):
        name = "img"
        img = NamedImage(name, b"123", CameraMimeType.UNSUPPORTED)
        assert img.name == name
