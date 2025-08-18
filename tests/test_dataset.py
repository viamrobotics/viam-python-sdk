import pytest
from google.protobuf.timestamp_pb2 import Timestamp
from grpclib.testing import ChannelFor

from viam.app.data_client import DataClient
from viam.proto.app.dataset import Dataset, MergeDatasetsRequest, MergeDatasetsResponse

from .mocks.services import MockDataset

CREATED_ID = "VIAM_DATASET_0"
ID = "VIAM_DATASET_1"
NAME = "dataset"
ORG_ID = "org_id"
SECONDS = 978310861
NANOS = 0
TIME = Timestamp(seconds=SECONDS, nanos=NANOS)
DATASET = Dataset(id=ID, name=NAME, organization_id=ORG_ID, time_created=TIME)
DATASETS = [DATASET]
AUTH_TOKEN = "auth_token"
DATA_SERVICE_METADATA = {"authorization": f"Bearer {AUTH_TOKEN}"}

MERGE_DATASET_IDS = ["dataset_1", "dataset_2"]
MERGE_NAME = "merged_dataset"
MERGE_ORG_ID = "merged_org_id"
MERGED_DATASET_ID = "merged_dataset_id"


@pytest.fixture(scope="function")
def service() -> MockDataset:
    return MockDataset(CREATED_ID, DATASETS)


class TestClient:
    async def test_create_dataset(self, service: MockDataset):
        async with ChannelFor([service]) as channel:
            client = DataClient(channel, DATA_SERVICE_METADATA)
            id = await client.create_dataset(NAME, ORG_ID)
            assert service.name == NAME
            assert service.org_id == ORG_ID
            assert id == CREATED_ID

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

    async def test_merge_datasets(self, service: MockDataset):
        async with ChannelFor([service]) as channel:
            client = DataClient(channel, DATA_SERVICE_METADATA)
            merged_id = await client.merge_datasets(MERGE_DATASET_IDS, MERGE_NAME, MERGE_ORG_ID)
            assert service.merge_dataset_ids == MERGE_DATASET_IDS
            assert service.merge_name == MERGE_NAME
            assert service.merge_org_id == MERGE_ORG_ID
            assert merged_id == MERGED_DATASET_ID
