from array import array
import os
import pytest

from viam.media.video import RawImage


class TestRawImage:
    @pytest.mark.asyncio
    async def test_bytes_to_depth_array(self):
        with open(f"{os.path.dirname(__file__)}/../data/fakeDM.vnd.viam.dep", "rb") as depth_map:
            image = RawImage(depth_map.read(), "image/vnd.viam.dep")
        assert isinstance(image, RawImage)
        standard_data = image.bytes_to_depth_array()
        assert len(standard_data) == int.from_bytes(image.data[16:24], "big")
        assert len(standard_data[0]) == int.from_bytes(image.data[8:16], "big")
        data_arr = array("H", image.data[24:])
        assert len(data_arr) == 200
        assert data_arr[0] == standard_data[0][0]
        assert data_arr[183] == standard_data[-1][3]
