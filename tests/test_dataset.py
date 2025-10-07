import pytest
from google.protobuf.timestamp_pb2 import Timestamp
from grpclib.testing import ChannelFor

from viam.app.data_client import DataClient
from viam.proto.app.dataset import Dataset

from .mocks.services import MockDataset

CREATED_ID = "VIAM_DATASET_0"
MERGED_NAME = "VIAM_DATASET_MERGED"
ID = "VIAM_DATASET_1"
ID2 = "VIAM_DATASET_2"
MERGED_ID = f'{ID}{ID2}'
NAME = "dataset"
ORG_ID = "org_id"
SECONDS = 978310861
NANOS = 0
TIME = Timestamp(seconds=SECONDS, nanos=NANOS)
DATASET = Dataset(id=ID, name=NAME, organization_id=ORG_ID, time_created=TIME)
DATASETS = [DATASET]
AUTH_TOKEN = "auth_token"
DATA_SERVICE_METADATA = {"authorization": f"Bearer {AUTH_TOKEN}"}


@pytest.fixture(scope="function")
def service() -> MockDataset:
    return MockDataset(CREATED_ID, DATASETS, MERGED_ID)


class TestClient:
    async def test_create_dataset(self, service: MockDataset):
        async with ChannelFor([service]) as channel:
            client = DataClient(channel, DATA_SERVICE_METADATA)
            id = await client.create_dataset(NAME, ORG_ID)
            assert service.name == NAME
            assert service.org_id == ORG_ID
            assert id == CREATED_ID

    async def test_merge_datasets(self, service: MockDataset):
        async with ChannelFor([service]) as channel:
            client = DataClient(channel, DATA_SERVICE_METADATA)
            id = await client.merge_datasets(MERGED_NAME, ORG_ID, [ID, ID2])
            assert service.name == MERGED_NAME
            assert service.org_id == ORG_ID
            assert id == MERGED_ID

    async def test_delete_dataset(self, service: MockDataset):
        async with ChannelFor([service]) as channel:
            client = DataClient(channel, DATA_SERVICE_METADATA)
            await client.delete_dataset(ID)
            assert service.deleted_id == ID

    async def test_list_datasets_by_ids(self, service: MockDataset):
        async with ChannelFor([service]) as channel:
            client = DataClient(channel, DATA_SERVICE_METADATA)
            datasets = await client.list_dataset_by_ids([ID])
            assert service.ids == [ID]
            assert datasets == DATASETS

    async def test_list_datasets_by_organization_id(self, service: MockDataset):
        async with ChannelFor([service]) as channel:
            client = DataClient(channel, DATA_SERVICE_METADATA)
            datasets = await client.list_datasets_by_organization_id(ORG_ID)
            assert service.org_id == ORG_ID
            assert datasets == DATASETS

    async def test_rename_dataset(self, service: MockDataset):
        async with ChannelFor([service]) as channel:
            client = DataClient(channel, DATA_SERVICE_METADATA)
            await client.rename_dataset(ID, NAME)
            assert service.id == ID
            assert service.name == NAME
