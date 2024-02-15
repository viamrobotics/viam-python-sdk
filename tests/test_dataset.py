from datetime import datetime

import pytest
from grpclib.testing import ChannelFor

from viam.app.data_client import DataClient

from .mocks.services import MockDataset

CREATED_ID = "VIAM_DATASET_0"
ID = "VIAM_DATASET_1"
NAME = "dataset"
ORG_ID = "org_id"
DATETIME = datetime.now()
DATASET = DataClient.Dataset(id=ID, name=NAME, organization_id=ORG_ID, time_created=DATETIME)
DATASETS = [DATASET]
AUTH_TOKEN = "auth_token"
DATA_SERVICE_METADATA = {"authorization": f"Bearer {AUTH_TOKEN}"}


@pytest.fixture(scope="function")
def service() -> MockDataset:
    return MockDataset(CREATED_ID, DATASETS)


class TestClient:
    @pytest.mark.asyncio
    async def test_create_dataset(self, service: MockDataset):
        async with ChannelFor([service]) as channel:
            client = DataClient(channel, DATA_SERVICE_METADATA)
            id = await client.create_dataset(NAME, ORG_ID)
            assert service.name == NAME
            assert service.org_id == ORG_ID
            assert id == CREATED_ID
