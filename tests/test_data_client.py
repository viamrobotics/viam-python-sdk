from typing import List

import pytest
from google.protobuf.timestamp_pb2 import Timestamp
from grpclib.testing import ChannelFor

from viam.app.data_client import DataClient
from viam.proto.app.data import Annotations, BinaryID, BinaryMetadata, BoundingBox, CaptureMetadata, Filter, Order
from viam.utils import create_filter

from .mocks.services import MockData

INCLUDE_BINARY = True
COMPONENT_NAME = "component_name"
COMPONENT_TYPE = "component_type"
METHOD = "method"
ROBOT_NAME = "robot_name"
ROBOT_ID = "robot_id"
PART_NAME = "part_name"
PART_ID = "part_id"
LOCATION_ID = "location_id"
LOCATION_IDS = [LOCATION_ID]
ORG_ID = "organization_id"
ORG_IDS = [ORG_ID]
PASSWORD = "password"
MIME_TYPE = "mime_type"
MIME_TYPES = [MIME_TYPE]
URI = "some.robot.uri"
SECONDS_START = 978310861
NANOS_START = 0
SECONDS_END = 978310861
NANOS_END = 0
START_TS = Timestamp(seconds=SECONDS_START, nanos=NANOS_START)
END_TS = Timestamp(seconds=SECONDS_END, nanos=NANOS_END)
START_DATETIME = START_TS.ToDatetime()
END_DATETIME = END_TS.ToDatetime()
TAGS = ["tag"]
BBOX_LABEL = "bbox_label"
BBOX_LABELS = [BBOX_LABEL]
DATASET_ID = "VIAM_DATASET_1"
FILTER = create_filter(
    component_name=COMPONENT_NAME,
    component_type=COMPONENT_TYPE,
    method=METHOD,
    robot_name=ROBOT_NAME,
    robot_id=ROBOT_ID,
    part_name=PART_NAME,
    part_id=PART_ID,
    location_ids=LOCATION_IDS,
    organization_ids=ORG_IDS,
    mime_type=MIME_TYPES,
    start_time=START_DATETIME,
    end_time=END_DATETIME,
    tags=TAGS,
    bbox_labels=BBOX_LABELS,
    dataset_id=DATASET_ID,
)

FILE_ID = "file_id"
BINARY_ID = BinaryID(file_id=FILE_ID, organization_id=ORG_ID, location_id=LOCATION_ID)
BINARY_IDS = [BINARY_ID]
BINARY_DATA = b"binary_data"
FILE_NAME = "file_name"
FILE_EXT = "file_extension"
BBOX = BoundingBox(
    id="id",
    label=BBOX_LABEL,
    x_min_normalized=0,
    y_min_normalized=0.1,
    x_max_normalized=0.2,
    y_max_normalized=0.3,
)
BBOXES = [BBOX]
SQL_QUERY = "sql_query"
MQL_BINARY = [b"mql_binary"]
TABULAR_DATA = {"key": "value"}
TABULAR_METADATA = CaptureMetadata(
    organization_id=ORG_ID,
    location_id=LOCATION_ID,
    robot_name=ROBOT_NAME,
    robot_id=ROBOT_ID,
    part_name=PART_NAME,
    part_id=PART_ID,
    component_type=COMPONENT_TYPE,
    component_name=COMPONENT_NAME,
    method_name=METHOD,
    method_parameters={},
    tags=TAGS,
    mime_type=MIME_TYPE,
)
BINARY_METADATA = BinaryMetadata(
    id="id",
    capture_metadata=TABULAR_METADATA,
    time_requested=START_TS,
    time_received=END_TS,
    file_name=FILE_NAME,
    file_ext=FILE_EXT,
    uri=URI,
    annotations=Annotations(bboxes=BBOXES),
)

TABULAR_RESPONSE = [DataClient.TabularData(TABULAR_DATA, TABULAR_METADATA, START_DATETIME, END_DATETIME)]
TABULAR_QUERY_RESPONSE = [
    {"key1": 1, "key2": "2", "key3": [1, 2, 3], "key4": {"key4sub1": 1}},
]
BINARY_RESPONSE = [DataClient.BinaryData(BINARY_DATA, BINARY_METADATA)]
DELETE_REMOVE_RESPONSE = 1
TAGS_RESPONSE = ["tag"]
HOSTNAME_RESPONSE = "host"

AUTH_TOKEN = "auth_token"
DATA_SERVICE_METADATA = {"authorization": f"Bearer {AUTH_TOKEN}"}


@pytest.fixture(scope="function")
def service() -> MockData:
    return MockData(
        tabular_response=TABULAR_RESPONSE,
        tabular_query_response=TABULAR_QUERY_RESPONSE,
        binary_response=BINARY_RESPONSE,
        delete_remove_response=DELETE_REMOVE_RESPONSE,
        tags_response=TAGS_RESPONSE,
        bbox_labels_response=BBOX_LABELS,
        hostname_response=HOSTNAME_RESPONSE,
    )


class TestClient:
    @pytest.mark.asyncio
    async def test_tabular_data_by_filter(self, service: MockData):
        async with ChannelFor([service]) as channel:
            client = DataClient(channel, DATA_SERVICE_METADATA)
            sort_order = Order.ORDER_ASCENDING
            limit = 100
            last = "LAST_TABULAR_ID"
            tabular_data, count, last_response = await client.tabular_data_by_filter(
                filter=FILTER,
                sort_order=sort_order,
                limit=100,
                last=last,
                count_only=True,
            )
            assert service.filter == FILTER
            assert service.order == sort_order
            assert service.limit == limit
            assert service.last == last
            assert service.count_only is True
            assert tabular_data == TABULAR_RESPONSE
            assert count == len(tabular_data)
            assert last_response != ""
            self.assert_filter(filter=service.filter)

    @pytest.mark.asyncio
    async def test_tabular_data_by_sql(self, service: MockData):
        async with ChannelFor([service]) as channel:
            client = DataClient(channel, DATA_SERVICE_METADATA)
            response = await client.tabular_data_by_sql(ORG_ID, SQL_QUERY)
            assert response == TABULAR_QUERY_RESPONSE

    @pytest.mark.asyncio
    async def test_tabular_data_by_mql(self, service: MockData):
        async with ChannelFor([service]) as channel:
            client = DataClient(channel, DATA_SERVICE_METADATA)
            response = await client.tabular_data_by_mql(ORG_ID, MQL_BINARY)
            assert response == TABULAR_QUERY_RESPONSE

    @pytest.mark.asyncio
    async def test_binary_data_by_filter(self, service: MockData):
        async with ChannelFor([service]) as channel:
            client = DataClient(channel, DATA_SERVICE_METADATA)
            sort_order = Order.ORDER_DESCENDING
            limit = 25
            last = "LAST_BINARY_ID"
            binary_data, count, last_response = await client.binary_data_by_filter(
                filter=FILTER,
                include_binary_data=INCLUDE_BINARY,
                sort_order=sort_order,
                limit=limit,
                count_only=False,
                include_internal_data=True,
                last=last,
            )
            assert service.filter == FILTER
            assert service.order == sort_order
            assert service.limit == limit
            assert service.include_binary == INCLUDE_BINARY
            assert service.count_only is False
            assert service.include_internal_data is True
            assert service.last == last
            assert binary_data == BINARY_RESPONSE
            assert count == len(binary_data)
            assert last_response != ""
            self.assert_filter(filter=service.filter)

    @pytest.mark.asyncio
    async def test_binary_data_by_ids(self, service: MockData):
        async with ChannelFor([service]) as channel:
            client = DataClient(channel, DATA_SERVICE_METADATA)
            binary_data = await client.binary_data_by_ids(binary_ids=BINARY_IDS)
            assert binary_data == BINARY_RESPONSE
            self.assert_binary_ids(binary_ids=list(service.binary_ids))

    @pytest.mark.asyncio
    async def test_delete_tabular_data(self, service: MockData):
        async with ChannelFor([service]) as channel:
            client = DataClient(channel, DATA_SERVICE_METADATA)
            deleted_count = await client.delete_tabular_data(organization_id=ORG_ID, delete_older_than_days=0)
            assert deleted_count == DELETE_REMOVE_RESPONSE

    @pytest.mark.asyncio
    async def test_delete_binary_data_by_filter(self, service: MockData):
        async with ChannelFor([service]) as channel:
            client = DataClient(channel, DATA_SERVICE_METADATA)
            deleted_count = await client.delete_binary_data_by_filter(filter=FILTER)
            assert deleted_count == DELETE_REMOVE_RESPONSE
            self.assert_filter(filter=service.filter)

    @pytest.mark.asyncio
    async def test_delete_binary_data_by_ids(self, service: MockData):
        async with ChannelFor([service]) as channel:
            client = DataClient(channel, DATA_SERVICE_METADATA)
            deleted_count = await client.delete_binary_data_by_ids(binary_ids=BINARY_IDS)
            assert deleted_count == DELETE_REMOVE_RESPONSE
            self.assert_binary_ids(binary_ids=list(service.binary_ids))

    @pytest.mark.asyncio
    async def test_add_tags_to_binary_data_by_ids(self, service: MockData):
        async with ChannelFor([service]) as channel:
            client = DataClient(channel, DATA_SERVICE_METADATA)
            await client.add_tags_to_binary_data_by_ids(tags=TAGS, binary_ids=BINARY_IDS)
            assert service.tags == TAGS
            self.assert_binary_ids(binary_ids=list(service.binary_ids))

    @pytest.mark.asyncio
    async def test_add_tags_to_binary_data_by_filter(self, service: MockData):
        async with ChannelFor([service]) as channel:
            client = DataClient(channel, DATA_SERVICE_METADATA)
            await client.add_tags_to_binary_data_by_filter(tags=TAGS, filter=FILTER)
            assert service.tags == TAGS
            self.assert_filter(filter=service.filter)

    @pytest.mark.asyncio
    async def test_remove_tags_from_binary_data_by_ids(self, service: MockData):
        async with ChannelFor([service]) as channel:
            client = DataClient(channel, DATA_SERVICE_METADATA)
            deleted_count = await client.remove_tags_from_binary_data_by_ids(tags=TAGS, binary_ids=BINARY_IDS)
            assert deleted_count == DELETE_REMOVE_RESPONSE
            assert service.tags == TAGS
            self.assert_binary_ids(binary_ids=list(service.binary_ids))

    @pytest.mark.asyncio
    async def test_remove_tags_from_binary_data_by_filter(self, service: MockData):
        async with ChannelFor([service]) as channel:
            client = DataClient(channel, DATA_SERVICE_METADATA)
            deleted_count = await client.remove_tags_from_binary_data_by_filter(tags=TAGS, filter=FILTER)
            assert deleted_count == DELETE_REMOVE_RESPONSE
            assert service.tags == TAGS
            self.assert_filter(filter=service.filter)

    @pytest.mark.asyncio
    async def test_tags_by_filter(self, service: MockData):
        async with ChannelFor([service]) as channel:
            client = DataClient(channel, DATA_SERVICE_METADATA)
            tags = await client.tags_by_filter(filter=FILTER)
            assert tags == TAGS_RESPONSE
            self.assert_filter(filter=service.filter)

    @pytest.mark.asyncio
    async def test_add_bounding_box_to_image_by_id(self, service: MockData):
        async with ChannelFor([service]) as channel:
            client = DataClient(channel, DATA_SERVICE_METADATA)
            bbox_label = await client.add_bounding_box_to_image_by_id(
                binary_id=BINARY_ID,
                label="label",
                x_min_normalized=0,
                y_min_normalized=0.1,
                x_max_normalized=0.2,
                y_max_normalized=0.3,
            )
            assert bbox_label == BBOX_LABEL

    @pytest.mark.asyncio
    async def test_remove_bounding_box_from_image_by_id(self, service: MockData):
        async with ChannelFor([service]) as channel:
            client = DataClient(channel, DATA_SERVICE_METADATA)
            await client.remove_bounding_box_from_image_by_id(BBOX_LABEL, BINARY_ID)
            assert service.removed_label == BBOX_LABEL
            assert service.removed_id == BINARY_ID

    @pytest.mark.asyncio
    async def test_bounding_box_labels_by_filter(self, service: MockData):
        async with ChannelFor([service]) as channel:
            client = DataClient(channel, DATA_SERVICE_METADATA)
            bbox_labels = await client.bounding_box_labels_by_filter(filter=FILTER)
            assert bbox_labels == BBOX_LABELS
            self.assert_filter(filter=service.filter)

    @pytest.mark.asyncio
    async def test_get_database_connection(self, service: MockData):
        async with ChannelFor([service]) as channel:
            client = DataClient(channel, DATA_SERVICE_METADATA)
            hostname = await client.get_database_connection(organization_id=ORG_ID)
            assert hostname == HOSTNAME_RESPONSE

    @pytest.mark.asyncio
    async def test_configure_database_user(self, service: MockData):
        async with ChannelFor([service]) as channel:
            client = DataClient(channel, DATA_SERVICE_METADATA)
            await client.configure_database_user(ORG_ID, PASSWORD)
            assert service.organization_id == ORG_ID
            assert service.password == PASSWORD

    @pytest.mark.asyncio
    async def test_add_binary_data_to_dataset_by_ids(self, service: MockData):
        async with ChannelFor([service]) as channel:
            client = DataClient(channel, DATA_SERVICE_METADATA)
            await client.add_binary_data_to_dataset_by_ids(binary_ids=BINARY_IDS, dataset_id=DATASET_ID)
            assert service.added_data_ids == BINARY_IDS
            assert service.dataset_id == DATASET_ID

    @pytest.mark.asyncio
    async def test_remove_binary_data_to_dataset_by_ids(self, service: MockData):
        async with ChannelFor([service]) as channel:
            client = DataClient(channel, DATA_SERVICE_METADATA)
            await client.remove_binary_data_from_dataset_by_ids(binary_ids=BINARY_IDS, dataset_id=DATASET_ID)
            assert service.removed_data_ids == BINARY_IDS
            assert service.dataset_id == DATASET_ID

    def assert_filter(self, filter: Filter) -> None:
        assert filter.component_name == COMPONENT_NAME
        assert filter.component_type == COMPONENT_TYPE
        assert filter.method == METHOD
        assert filter.robot_name == ROBOT_NAME
        assert filter.robot_id == ROBOT_ID
        assert filter.part_name == PART_NAME
        assert filter.part_id == PART_ID
        assert filter.location_ids == LOCATION_IDS
        assert filter.organization_ids == ORG_IDS
        assert filter.mime_type == MIME_TYPES
        assert filter.interval.start.seconds == SECONDS_START
        assert filter.interval.start.nanos == NANOS_START
        assert filter.interval.end.seconds == SECONDS_END
        assert filter.interval.end.nanos == NANOS_END
        assert filter.tags_filter.tags == TAGS
        assert filter.bbox_labels == BBOX_LABELS

    def assert_binary_ids(self, binary_ids: List[BinaryID]) -> None:
        for binary_id in binary_ids:
            assert binary_id.file_id == FILE_ID
            assert binary_id.organization_id == ORG_ID
            assert binary_id.location_id == LOCATION_ID
