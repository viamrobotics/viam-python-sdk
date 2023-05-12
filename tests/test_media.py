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
        assert len(standard_data) == 10
        assert len(standard_data[0]) == 20
        data_arr = array("H", image.data[24:])
        data_arr.byteswap()
        assert len(data_arr) == 200
        assert standard_data[0][0] == data_arr[0]
        assert standard_data[-1][3] == data_arr[183]
        assert standard_data[-1][3] == 9 * 3
        assert standard_data[4][4] == 4 * 4
