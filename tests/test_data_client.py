import pytest
from typing import List

from grpclib.testing import ChannelFor
from google.protobuf.timestamp_pb2 import Timestamp

from viam.app.data.client import DataClient
from viam.proto.app.data import (
    Filter,
    BinaryID,
    CaptureInterval,
    TagsFilter
)
from viam.proto.app.datasync import (
    UploadMetadata,
    SensorData
)
from viam.utils import struct_to_dict

from .mocks.services import MockData

COMPONENT_NAME = "component_name"
COMPONENT_TYPE = "component_type"
METHOD = "method"
ROBOT_NAME = "robot_name"
ROBOT_ID = "robot_id"
PART_NAME = "part_name"
PART_ID = "part_id"
LOCATION_ID = "location_id"
ORG_ID = "organization_id"
MIME_TYPE = "mime_type"
SECONDS_START = 1689256710
NANOS_START = 10
SECONDS_END = 1689256810
NANOS_END = 10
TAGS = ["tag"]
BBOX_LABELS = ["bbox_label"]
FILTER = Filter(
    component_name=COMPONENT_NAME,
    component_type=COMPONENT_TYPE,
    method=METHOD,
    robot_name=ROBOT_NAME,
    robot_id=ROBOT_ID,
    part_name=PART_NAME,
    part_id=PART_ID,
    location_ids=[LOCATION_ID],
    organization_ids=[ORG_ID],
    mime_type=[MIME_TYPE],
    interval=CaptureInterval(
        start=Timestamp(
            seconds=SECONDS_START,
            nanos=NANOS_START,
        ),
        end=Timestamp(
            seconds=SECONDS_END,
            nanos=NANOS_END
        )
    ),
    tags_filter=TagsFilter(
        tags=TAGS
    ),
    bbox_labels=BBOX_LABELS,

)
FILE_ID = "file_id"
LOCATION_ID = "location_id"
BINARY_IDS = [BinaryID(
    file_id=FILE_ID,
    organization_id=ORG_ID,
    location_id=LOCATION_ID
)]
BINARY_DATA = b'binary_data'
METHOD_NAME = "method_name"
TIMESTAMPS = (
    Timestamp(
        seconds=SECONDS_START,
        nanos=NANOS_START
    ),
    Timestamp(
        seconds=SECONDS_END,
        nanos=NANOS_END
    )
)
METHOD_PARAMETERS = None
TABULAR_DATA = [{"key": "value"}]
FILE_NAME = "file_name"
FILE_EXT = "file_extension"

TABULAR_RESPONSE = [{"key": "value"}]
BINARY_RESPONSE = [b'binary_data']
DELETE_REMOVE_RESPONSE = 1
TAGS_RESPONSE = ["tag"]
BBOX_LABELS_RESPONSE = ["bbox_label"]

AUTH_TOKEN = "auth_token"
DATA_SERVICE_METADATA = {"authorization": f"Bearer {AUTH_TOKEN}"}


@pytest.fixture(scope="function")
def service() -> MockData:
    return MockData(
        tabular_response=TABULAR_RESPONSE,
        binary_response=BINARY_RESPONSE,
        delete_remove_response=DELETE_REMOVE_RESPONSE,
        tags_response=TAGS_RESPONSE,
        bbox_labels_response=BBOX_LABELS
    )


class TestClient:
    @pytest.mark.asyncio
    async def test_tabular_data_by_filter(self, service: MockData):
        async with ChannelFor([service]) as channel:
            client = DataClient(channel, DATA_SERVICE_METADATA)
            tabular_data = await client.tabular_data_by_filter(filter=FILTER)
            assert tabular_data == TABULAR_RESPONSE
            TestClient.assert_filter(filter=service.filter)

    @pytest.mark.asyncio
    async def test_binary_data_by_filter(self, service: MockData):
        async with ChannelFor([service]) as channel:
            client = DataClient(channel, DATA_SERVICE_METADATA)
            binary_data = await client.binary_data_by_filter(filter=FILTER)
            assert binary_data == BINARY_RESPONSE
            TestClient.assert_filter(filter=service.filter)

    @pytest.mark.asyncio
    async def test_binary_data_by_ids(self, service: MockData):
        async with ChannelFor([service]) as channel:
            client = DataClient(channel, DATA_SERVICE_METADATA)
            binary_data = await client.binary_data_by_ids(binary_ids=BINARY_IDS)
            assert binary_data == BINARY_RESPONSE
            TestClient.assert_binary_ids(binary_ids=service.binary_ids)

    @pytest.mark.asyncio
    async def test_delete_tabular_data_by_filter(self, service: MockData):
        async with ChannelFor([service]) as channel:
            client = DataClient(channel, DATA_SERVICE_METADATA)
            deleted_count = await client.delete_tabular_data_by_filter(filter=FILTER)
            assert deleted_count == DELETE_REMOVE_RESPONSE
            TestClient.assert_filter(service.filter)

    @pytest.mark.asyncio
    async def test_delete_binary_data_by_filter(self, service: MockData):
        async with ChannelFor([service]) as channel:
            client = DataClient(channel, DATA_SERVICE_METADATA)
            deleted_count = await client.delete_binary_data_by_filter(filter=FILTER)
            assert deleted_count == DELETE_REMOVE_RESPONSE
            TestClient.assert_filter(service.filter)

    @pytest.mark.asyncio
    async def test_delete_binary_data_by_ids(self, service: MockData):
        async with ChannelFor([service]) as channel:
            client = DataClient(channel, DATA_SERVICE_METADATA)
            deleted_count = await client.delete_binary_data_by_ids(binary_ids=BINARY_IDS)
            assert deleted_count == DELETE_REMOVE_RESPONSE
            TestClient.assert_binary_ids(service.binary_ids)

    @pytest.mark.asyncio
    async def test_add_tags_to_binary_data_by_ids(self, service: MockData):
        async with ChannelFor([service]) as channel:
            client = DataClient(channel, DATA_SERVICE_METADATA)
            await client.add_tags_to_binary_data_by_ids(tags=TAGS, binary_ids=BINARY_IDS)
            assert service.tags == TAGS
            TestClient.assert_binary_ids(service.binary_ids)

    @pytest.mark.asyncio
    async def test_add_tags_to_binary_data_by_filter(self, service: MockData):
        async with ChannelFor([service]) as channel:
            client = DataClient(channel, DATA_SERVICE_METADATA)
            await client.add_tags_to_binary_data_by_filter(tags=TAGS, filter=FILTER)
            assert service.tags == TAGS
            TestClient.assert_filter(service.filter)

    @pytest.mark.asyncio
    async def test_remove_tags_from_binary_data_by_ids(self, service: MockData):
        async with ChannelFor([service]) as channel:
            client = DataClient(channel, DATA_SERVICE_METADATA)
            deleted_count = await client.remove_tags_from_binary_data_by_ids(tags=TAGS, binary_ids=BINARY_IDS)
            assert deleted_count == DELETE_REMOVE_RESPONSE
            assert service.tags == TAGS
            TestClient.assert_binary_ids(service.binary_ids)

    @pytest.mark.asyncio
    async def test_remove_tags_from_binary_data_by_filter(self, service: MockData):
        async with ChannelFor([service]) as channel:
            client = DataClient(channel, DATA_SERVICE_METADATA)
            deleted_count = await client.remove_tags_from_binary_data_by_filter(tags=TAGS, filter=FILTER)
            assert deleted_count == DELETE_REMOVE_RESPONSE
            assert service.tags == TAGS
            TestClient.assert_binary_ids(service.binary_ids)

    @pytest.mark.asyncio
    async def test_tags_by_filter(self, service: MockData):
        async with ChannelFor([service]) as channel:
            client = DataClient(channel, DATA_SERVICE_METADATA)
            tags = await client.tags_by_filter(filter=FILTER)
            assert tags == TAGS_RESPONSE
            TestClient.assert_filter(service.filter)

    @pytest.mark.asyncio
    async def test_add_bounding_box_to_image_by_id(self, service: MockData):
        assert True

    @pytest.mark.asyncio
    async def test_remove_bounding_box_from_image_by_id(self, service: MockData):
        assert True

    @pytest.mark.asyncio
    async def test_bounding_box_labels_by_filter(self, service: MockData):
        async with ChannelFor([service]) as channel:
            client = DataClient(channel, DATA_SERVICE_METADATA)
            bbox_labels = client.bounding_box_labels_by_filter(filter=FILTER)
            assert bbox_labels == BBOX_LABELS_RESPONSE
            TestClient.assert_filter(service.filter)

    @pytest.mark.asyncio
    async def test_binary_data_capture_upload(self, service: MockData):
        async with ChannelFor([service]) as channel:
            client = DataClient(channel, DATA_SERVICE_METADATA)
            await client.binary_data_capture_upload(
                part_id=PART_ID,
                component_type=COMPONENT_TYPE,
                component_name=COMPONENT_NAME,
                method_name=METHOD_NAME,
                method_parameters=METHOD_PARAMETERS,
                tags=TAGS,
                timestamps=TIMESTAMPS,
                binary_data=BINARY_DATA
            )
            TestClient.assert_sensor_contents(service.sensor_contents)
            TestClient.assert_metadata(service.metadata)

    @pytest.mark.asyncio
    async def test_tabular_data_capture_upload(self, service: MockData):
        async with ChannelFor([service]) as channel:
            client = DataClient(channel, DATA_SERVICE_METADATA)
            await client.binary_data_capture_upload(
                part_id=PART_ID,
                component_type=COMPONENT_TYPE,
                component_name=COMPONENT_NAME,
                method_name=METHOD_NAME,
                method_parameters=METHOD_PARAMETERS,
                tags=TAGS,
                timestamps=TIMESTAMPS,
                tabular_data=TABULAR_DATA
            )
            TestClient.assert_sensor_contents(service.sensor_contents)
            TestClient.assert_metadata(service.metadata)

    @pytest.mark.asyncio
    async def test_file_upload(self, service: MockData):
        async with ChannelFor([service]) as channel:
            client = DataClient(channel, DATA_SERVICE_METADATA)
            await client.file_upload(
                part_id=PART_ID,
                component_type=COMPONENT_TYPE,
                component_name=COMPONENT_NAME,
                method_name=METHOD_NAME,
                file_name=FILE_NAME,
                method_parameters=METHOD_PARAMETERS,
                file_extension=FILE_EXT,
                tags=TAGS,
                data=BINARY_DATA
            )
            TestClient.assert_metadata(service.metadata)
            assert service.metadata.file_name == FILE_NAME
            assert service.metadata.file_extension == FILE_EXT
            assert service.binary_data == BINARY_DATA

    @pytest.mark.asyncio
    async def test_file_upload_from_path(self, service: MockData, tmp_path):
        async with ChannelFor([service]) as channel:
            client = DataClient(channel, DATA_SERVICE_METADATA)
            path = tmp_path / (FILE_NAME + FILE_EXT)
            path.write_bytes(BINARY_DATA)
            await client.file_upload(
                part_id=PART_ID,
                component_type=COMPONENT_TYPE,
                component_name=COMPONENT_NAME,
                method_name=METHOD_NAME,
                method_parameters=METHOD_PARAMETERS,
                tags=TAGS,
                filepath=path.resolve()
            )
            TestClient.assert_metadata(service.metadata)
            assert service.metadata.file_name == FILE_NAME
            assert service.metadata.file_extension == FILE_EXT
            assert service.binary_data == BINARY_DATA

    def assert_filter(filter: Filter) -> None:
        assert filter.component_name == COMPONENT_NAME
        assert filter.component_type == COMPONENT_TYPE
        assert filter.method == METHOD
        assert filter.robot_name == ROBOT_NAME
        assert filter.robot_id == ROBOT_ID
        assert filter.part_name == PART_NAME
        assert filter.part_id == PART_ID
        assert filter.location_id == LOCATION_ID
        assert filter.org_id == ORG_ID
        assert filter.mime_type == MIME_TYPE
        assert filter.interval.start.seconds_start == SECONDS_START
        assert filter.interval.start.nanos_start == NANOS_START
        assert filter.interval.end.seconds_end == SECONDS_END
        assert filter.interval.end.nanos_end == NANOS_END
        assert filter.tags_filter.tags == TAGS
        assert filter.bbox_labels == BBOX_LABELS

    def assert_binary_ids(binary_ids: List[BinaryID]) -> None:
        for binary_id in binary_ids:
            assert binary_id.file_id == FILE_ID
            assert binary_id.organization_id == ORG_ID
            assert binary_id.location_id == LOCATION_ID

    def assert_sensor_contents(sensor_contents: List[SensorData], is_binary: bool):
        for i, data in sensor_contents:
            assert data.metadata.time_requested.seconds == TIMESTAMPS[0].seconds
            assert data.metadata.time_requested.nanos == TIMESTAMPS[0].nanos
            assert data.metadata.time_reeived.seconds == TIMESTAMPS[1].seconds
            assert data.metadata.time_received.nanos == TIMESTAMPS[1].nanos
            if is_binary:
                assert data.binary == BINARY_DATA
            else:
                assert struct_to_dict(data.struct) == TABULAR_DATA[i]

    def assert_metadata(metadata: UploadMetadata) -> None:
        assert metadata.part_id == PART_ID
        assert metadata.component_type == COMPONENT_TYPE
        assert metadata.component_name == COMPONENT_NAME
        assert metadata.method_name == METHOD_NAME
        assert metadata.method_parameters == METHOD_PARAMETERS
        assert metadata.tags == TAGS
