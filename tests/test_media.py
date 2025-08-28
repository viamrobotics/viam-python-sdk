import os
from array import array
from io import BytesIO

import pytest
from PIL import Image

from viam.errors import NotSupportedError
from viam.media.utils.pil import pil_to_viam_image, viam_to_pil_image
from viam.media.video import CameraMimeType, Format, NamedImage, ViamImage

UNSUPPORTED_MIME_TYPE = "unsupported_string_mime_type"


class TestViamImage:
    UNSUPPORTED_MIME_TYPE = "unsupported_string_mime_type"

    def test_supported_image(self):
        i = Image.new("RGBA", (100, 100), "#AABBCCDD")
        b = BytesIO()
        i.save(b, "PNG")
        img = ViamImage(b.getvalue(), CameraMimeType.PNG)
        assert img._mime_type == CameraMimeType.PNG
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

        img3 = pil_to_viam_image(i, CameraMimeType.VIAM_RGBA.value)
        assert img3.width == WIDTH
        assert img3.height == HEIGHT

        img4 = ViamImage(b"data", CameraMimeType.PCD)
        assert img4.width is None
        assert img4.height is None

        img5 = ViamImage(b"data", CameraMimeType.CUSTOM(self.UNSUPPORTED_MIME_TYPE))
        assert img5.width is None
        assert img5.height is None

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


class TestCameraMimeType:
    def test_name(self):
        mime_type = CameraMimeType.VIAM_RGBA
        assert mime_type.name == "VIAM_RGBA"

        mime_type = CameraMimeType.VIAM_RAW_DEPTH
        assert mime_type.name == "VIAM_RAW_DEPTH"

        mime_type = CameraMimeType.JPEG
        assert mime_type.name == "JPEG"

        mime_type = CameraMimeType.PNG
        assert mime_type.name == "PNG"

        mime_type = CameraMimeType.PCD
        assert mime_type.name == "PCD"

        mime_type = CameraMimeType.CUSTOM("SOME CUSTOM MIME TYPE")
        assert mime_type.name == "CUSTOM"

    def test_value(self):
        mime_type = CameraMimeType.VIAM_RGBA
        assert mime_type.value == "image/vnd.viam.rgba"

        mime_type = CameraMimeType.VIAM_RAW_DEPTH
        assert mime_type.value == "image/vnd.viam.dep"

        mime_type = CameraMimeType.JPEG
        assert mime_type.value == "image/jpeg"

        mime_type = CameraMimeType.PNG
        assert mime_type.value == "image/png"

        mime_type = CameraMimeType.PCD
        assert mime_type.value == "pointcloud/pcd"

        mime_type = CameraMimeType.CUSTOM("SOME CUSTOM MIME TYPE")
        assert mime_type.value == "SOME CUSTOM MIME TYPE"

    def test_from_proto(self):
        format = Format.FORMAT_RAW_RGBA
        mime_type = CameraMimeType.from_proto(format)
        assert mime_type == CameraMimeType.VIAM_RGBA

        format = Format.FORMAT_RAW_DEPTH
        mime_type = CameraMimeType.from_proto(format)
        assert mime_type == CameraMimeType.VIAM_RAW_DEPTH

        format = Format.FORMAT_JPEG
        mime_type = CameraMimeType.from_proto(format)
        assert mime_type == CameraMimeType.JPEG

        format = Format.FORMAT_PNG
        mime_type = CameraMimeType.from_proto(format)
        assert mime_type == CameraMimeType.PNG

        format = Format.FORMAT_UNSPECIFIED
        mime_type = CameraMimeType.from_proto(format)
        assert mime_type == CameraMimeType.JPEG  # unspecified defaults to jpeg

    def test_to_proto(self):
        mime_type = CameraMimeType.VIAM_RGBA
        format = mime_type.proto
        assert format == Format.FORMAT_RAW_RGBA

        mime_type = CameraMimeType.VIAM_RAW_DEPTH
        format = mime_type.proto
        assert format == Format.FORMAT_RAW_DEPTH

        mime_type = CameraMimeType.JPEG
        format = mime_type.proto
        assert format == Format.FORMAT_JPEG

        mime_type = CameraMimeType.PNG
        format = mime_type.proto
        assert format == Format.FORMAT_PNG

        mime_type = CameraMimeType.PCD
        format = mime_type.proto
        assert format == Format.FORMAT_UNSPECIFIED

        mime_type = CameraMimeType.CUSTOM("some custom mime")
        format = mime_type.proto
        assert format == Format.FORMAT_UNSPECIFIED


def test_image_conversion():
    i = Image.new("RGBA", (100, 100), "#AABBCCDD")

    v_img = pil_to_viam_image(i, CameraMimeType.JPEG)
    assert isinstance(v_img, ViamImage)
    assert v_img.mime_type == CameraMimeType.JPEG

    pil_img = viam_to_pil_image(v_img)
    v_img2 = pil_to_viam_image(pil_img, CameraMimeType.JPEG)
    assert v_img2.data == v_img.data

    with pytest.raises(
        ValueError,
        match=f"Cannot encode to unsupported mimetype: {TestViamImage.UNSUPPORTED_MIME_TYPE}",
    ):
        pil_to_viam_image(i, CameraMimeType.CUSTOM(TestViamImage.UNSUPPORTED_MIME_TYPE))
