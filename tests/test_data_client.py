import pytest

from grpclib.testing import ChannelFor

from viam.app.data import DataClient

from .mocks.services import MockData

AUTH_TOKEN = "auth_token"
DATA_SERVICE_METADATA = {"authorization": f"Bearer {AUTH_TOKEN}"}


@pytest.fixture(scope="function")
def service() -> MockData:
    return MockData()


class TestClient:
    @pytest.mark.asyncio
    async def test_tabular_data_by_filter(self, service: MockData):
        async with ChannelFor([service]) as channel:
            client = DataClient(channel, DATA_SERVICE_METADATA)

    @pytest.mark.asyncio
    async def test_binary_data_by_filter(self, service: MockData):
        pass

    @pytest.mark.asyncio
    async def test_binary_data_by_ids(self, service: MockData):
        pass

    @pytest.mark.asyncio
    async def test_delete_tabular_data_by_filter(self, service: MockData):
        pass

    @pytest.mark.asyncio
    async def test_delete_binary_data_by_filter(self, service: MockData):
        pass

    @pytest.mark.asyncio
    async def test_delete_binary_data_by_ids(self, service: MockData):
        pass

    @pytest.mark.asyncio
    async def test_add_tags_to_binary_data_by_ids(self, service: MockData):
        pass

    @pytest.mark.asyncio
    async def test_add_tags_to_binary_data_by_filter(self, service: MockData):
        pass

    @pytest.mark.asyncio
    async def test_remove_tags_from_binary_data_by_ids(self, service: MockData):
        pass

    @pytest.mark.asyncio
    async def test_remove_tags_from_binary_data_by_filter(self, service: MockData):
        pass

    @pytest.mark.asyncio
    async def test_tags_by_filter(self, service: MockData):
        pass

    @pytest.mark.asyncio
    async def test_add_bounding_box_to_image_by_id(self, service: MockData):
        pass

    @pytest.mark.asyncio
    async def test_remove_bounding_box_from_image_by_id(self, service: MockData):
        pass

    @pytest.mark.asyncio
    async def test_bounding_box_labels_by_filter(self, service: MockData):
        pass

    @pytest.mark.asyncio
    async def test_binary_data_capture_upload(self, service: MockData):
        pass

    @pytest.mark.asyncio
    async def test_tabular_data_capture_upload(self, service: MockData):
        pass

    @pytest.mark.asyncio
    async def test_file_upload(self, service: MockData):
        pass

    @pytest.mark.asyncio
    async def test_file_upload_from_path(self, service: MockData):
        pass
