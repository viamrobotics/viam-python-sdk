from datetime import datetime

import pytest
from grpclib.testing import ChannelFor

from viam.app.data_client import DataClient
from viam.proto.app.data import TabularDataSourceType
from viam.proto.app.datapipelines import DataPipeline, DataPipelineRun, DataPipelineRunStatus
from viam.utils import datetime_to_timestamp

from .mocks.services import MockDataPipelines

ID = "VIAM_DATAPIPELINE_1"
NAME = "datapipeline"
ORG_ID = "org_id"
SCHEDULE = "0 0 * * *"
UPDATED_SCHEDULE = "0 1 * * *"
MQL_BINARY = []
ENABLE_BACKFILL = True
DATA_SOURCE_TYPE = TabularDataSourceType.TABULAR_DATA_SOURCE_TYPE_UNSPECIFIED
STANDARD_DATA_SOURCE_TYPE = TabularDataSourceType.TABULAR_DATA_SOURCE_TYPE_STANDARD

TIMESTAMP = datetime.fromtimestamp(0)
TIMESTAMP_PROTO = datetime_to_timestamp(TIMESTAMP)

PROTO_DATA_PIPELINE = DataPipeline(
    id=ID,
    name=NAME,
    organization_id=ORG_ID,
    schedule=SCHEDULE,
    mql_binary=MQL_BINARY,
    enabled=True,
    created_on=TIMESTAMP_PROTO,
    updated_at=TIMESTAMP_PROTO,
    data_source_type=DATA_SOURCE_TYPE,
)
PROTO_DATA_PIPELINES = [PROTO_DATA_PIPELINE]

DATA_PIPELINE = DataClient.DataPipeline.from_proto(PROTO_DATA_PIPELINE)
DATA_PIPELINES = [DATA_PIPELINE]

RUN_ID = "VIAM_DATAPIPELINE_RUN_1"

PROTO_DATA_PIPELINE_RUN = DataPipelineRun(
    id=RUN_ID,
    status=DataPipelineRunStatus.DATA_PIPELINE_RUN_STATUS_COMPLETED,
    start_time=TIMESTAMP_PROTO,
    end_time=TIMESTAMP_PROTO,
    data_start_time=TIMESTAMP_PROTO,
    data_end_time=TIMESTAMP_PROTO,
)
PROTO_DATA_PIPELINE_RUNS = [PROTO_DATA_PIPELINE_RUN]

DATA_PIPELINE_RUNS = [
    DataClient.DataPipelineRun(
        id=RUN_ID,
        status=DataPipelineRunStatus.DATA_PIPELINE_RUN_STATUS_COMPLETED,
        start_time=TIMESTAMP,
        end_time=TIMESTAMP,
        data_start_time=TIMESTAMP,
        data_end_time=TIMESTAMP,
    )
]

DATA_PIPELINE_RUNS_PAGE = DataClient.DataPipelineRunsPage(
    _client=None, next_page_token="", pipeline_id=ID, runs=DATA_PIPELINE_RUNS, page_size=10
)

AUTH_TOKEN = "auth_token"
DATA_SERVICE_METADATA = {"authorization": f"Bearer {AUTH_TOKEN}"}


@pytest.fixture(scope="function")
def service() -> MockDataPipelines:
    return MockDataPipelines(
        ID,
        PROTO_DATA_PIPELINES,
        PROTO_DATA_PIPELINE_RUNS,
    )


class TestClient:
    async def test_create_data_pipeline(self, service: MockDataPipelines):
        async with ChannelFor([service]) as channel:
            client = DataClient(channel, DATA_SERVICE_METADATA)
            id = await client.create_data_pipeline(ORG_ID, NAME, MQL_BINARY, SCHEDULE, ENABLE_BACKFILL)
            assert id == ID
            assert service.name == NAME
            assert service.org_id == ORG_ID
            assert service.schedule == SCHEDULE
            assert service.mql_binary == MQL_BINARY
            assert service.enable_backfill == ENABLE_BACKFILL
            assert service.data_source_type == STANDARD_DATA_SOURCE_TYPE

    async def test_get_data_pipeline(self, service: MockDataPipelines):
        async with ChannelFor([service]) as channel:
            client = DataClient(channel, DATA_SERVICE_METADATA)
            pipeline = await client.get_data_pipeline(ID)
            assert pipeline == DATA_PIPELINE

    async def test_list_data_pipelines(self, service: MockDataPipelines):
        async with ChannelFor([service]) as channel:
            client = DataClient(channel, DATA_SERVICE_METADATA)
            pipelines = await client.list_data_pipelines(ORG_ID)
            assert pipelines == DATA_PIPELINES

    async def test_delete_data_pipeline(self, service: MockDataPipelines):
        async with ChannelFor([service]) as channel:
            client = DataClient(channel, DATA_SERVICE_METADATA)
            await client.delete_data_pipeline(ID)
            assert service.deleted_id == ID

    async def test_list_data_pipeline_runs(self, service: MockDataPipelines):
        async with ChannelFor([service]) as channel:
            client = DataClient(channel, DATA_SERVICE_METADATA)
            runs = await client.list_data_pipeline_runs(ID)
            runs._client = None
            assert runs == DATA_PIPELINE_RUNS_PAGE
