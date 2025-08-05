from datetime import datetime
from typing import Any, List, Mapping, Tuple, cast

import pytest
from google.protobuf.timestamp_pb2 import Timestamp
from grpclib.testing import ChannelFor

from viam.app.data_client import DataClient
from viam.proto.app.datasync import SensorData, UploadMetadata
from viam.utils import datetime_to_timestamp, struct_to_dict

from .mocks.services import MockDataSync

COMPONENT_NAME = "component_name"
COMPONENT_TYPE = "component_type"
PART_ID = "part_id"
SECONDS_START = 1689256710
NANOS_START = 10
SECONDS_END = 1689256810
NANOS_END = 10
TAGS = ["tag"]
DATASET_IDS = ["dataset_1"]
BINARY_DATA = b"binary_data"
METHOD_NAME = "method_name"
DATETIMES = (datetime.now(), datetime.now())
TIMESTAMPS = cast(Tuple[Timestamp, Timestamp], (datetime_to_timestamp(DATETIMES[0]), datetime_to_timestamp(DATETIMES[1])))
METHOD_PARAMETERS = {}
TABULAR_DATA = [{"key": "value"}]
FILE_NAME = "file_name"
FILE_EXT = ".file_extension"
FILE_UPLOAD_RESPONSE = "ID"

AUTH_TOKEN = "auth_token"
DATA_SERVICE_METADATA = {"authorization": f"Bearer {AUTH_TOKEN}"}


@pytest.fixture(scope="function")
def service() -> MockDataSync:
    return MockDataSync(file_upload_response=FILE_UPLOAD_RESPONSE)


class TestClient:
    async def test_binary_data_capture_upload(self, service: MockDataSync):
        async with ChannelFor([service]) as channel:
            client = DataClient(channel, DATA_SERVICE_METADATA)
            file_id = await client.binary_data_capture_upload(
                part_id=PART_ID,
                component_type=COMPONENT_TYPE,
                component_name=COMPONENT_NAME,
                method_name=METHOD_NAME,
                method_parameters=METHOD_PARAMETERS,
                tags=TAGS,
                data_request_times=DATETIMES,
                binary_data=BINARY_DATA,
                file_extension=".txt",
                dataset_ids=DATASET_IDS,
            )
            self.assert_sensor_contents(sensor_contents=list(service.sensor_contents), is_binary=True)
            self.assert_metadata(metadata=service.metadata)
            assert service.metadata.file_extension == ".txt"
            assert file_id == FILE_UPLOAD_RESPONSE

            # Test extension dot prepend
            file_id = await client.binary_data_capture_upload(
                part_id=PART_ID,
                component_type=COMPONENT_TYPE,
                component_name=COMPONENT_NAME,
                method_name=METHOD_NAME,
                method_parameters=METHOD_PARAMETERS,
                tags=TAGS,
                data_request_times=DATETIMES,
                binary_data=BINARY_DATA,
                file_extension="txt",
                dataset_ids=["dataset_1"],
            )
            assert service.metadata.file_extension == ".txt"

    async def test_tabular_data_capture_upload(self, service: MockDataSync):
        async with ChannelFor([service]) as channel:
            client = DataClient(channel, DATA_SERVICE_METADATA)
            file_id = await client.tabular_data_capture_upload(
                part_id=PART_ID,
                component_type=COMPONENT_TYPE,
                component_name=COMPONENT_NAME,
                method_name=METHOD_NAME,
                method_parameters=METHOD_PARAMETERS,
                tags=TAGS,
                data_request_times=[DATETIMES],
                tabular_data=cast(List[Mapping[str, Any]], TABULAR_DATA),
            )
            self.assert_sensor_contents(sensor_contents=list(service.sensor_contents), is_binary=False)
            self.assert_metadata(metadata=service.metadata, test_dataset_ids=False)
            assert file_id == FILE_UPLOAD_RESPONSE

    async def test_file_upload(self, service: MockDataSync):
        async with ChannelFor([service]) as channel:
            client = DataClient(channel, DATA_SERVICE_METADATA)
            file_id = await client.file_upload(
                part_id=PART_ID,
                component_type=COMPONENT_TYPE,
                component_name=COMPONENT_NAME,
                method_name=METHOD_NAME,
                file_name=FILE_NAME,
                method_parameters=METHOD_PARAMETERS,
                file_extension=FILE_EXT,
                tags=TAGS,
                data=BINARY_DATA,
                dataset_ids=DATASET_IDS,
            )
            assert file_id == FILE_UPLOAD_RESPONSE
            self.assert_metadata(service.metadata)
            assert service.metadata.file_name == FILE_NAME
            assert service.metadata.file_extension == FILE_EXT
            assert service.binary_data == BINARY_DATA

    async def test_file_upload_from_path(self, service: MockDataSync, tmp_path):
        async with ChannelFor([service]) as channel:
            client = DataClient(channel, DATA_SERVICE_METADATA)
            path = tmp_path / (FILE_NAME + FILE_EXT)
            path.write_bytes(BINARY_DATA)
            file_id = await client.file_upload_from_path(
                part_id=PART_ID,
                component_type=COMPONENT_TYPE,
                component_name=COMPONENT_NAME,
                method_name=METHOD_NAME,
                method_parameters=METHOD_PARAMETERS,
                tags=TAGS,
                dataset_ids=DATASET_IDS,
                filepath=path.resolve(),
            )
            assert file_id == FILE_UPLOAD_RESPONSE
            self.assert_metadata(service.metadata)
            assert service.metadata.file_name == FILE_NAME
            assert service.metadata.file_extension == FILE_EXT
            assert service.binary_data == BINARY_DATA

    async def test_streaming_data_capture_upload(self, service: MockDataSync):
        async with ChannelFor([service]) as channel:
            client = DataClient(channel, DATA_SERVICE_METADATA)
            file_id = await client.streaming_data_capture_upload(
                data=BINARY_DATA,
                part_id=PART_ID,
                file_ext=FILE_EXT,
                component_type=COMPONENT_TYPE,
                component_name=COMPONENT_NAME,
                method_name=METHOD_NAME,
                method_parameters=METHOD_PARAMETERS,
                data_request_times=DATETIMES,
                tags=TAGS,
                dataset_ids=DATASET_IDS,
            )
            assert file_id == FILE_UPLOAD_RESPONSE
            self.assert_metadata(service.metadata)
            assert service.metadata.file_extension == FILE_EXT
            assert service.binary_data == BINARY_DATA

    def assert_sensor_contents(self, sensor_contents: List[SensorData], is_binary: bool):
        for idx, sensor_content in enumerate(sensor_contents):
            assert sensor_content.metadata.time_requested.seconds == TIMESTAMPS[0].seconds
            assert sensor_content.metadata.time_requested.nanos == TIMESTAMPS[0].nanos
            assert sensor_content.metadata.time_received.seconds == TIMESTAMPS[1].seconds
            assert sensor_content.metadata.time_received.nanos == TIMESTAMPS[1].nanos
            if is_binary:
                assert sensor_content.binary == BINARY_DATA
            else:
                assert struct_to_dict(sensor_content.struct) == TABULAR_DATA[idx]

    def assert_metadata(self, metadata: UploadMetadata, test_dataset_ids: bool = True) -> None:
        assert metadata.part_id == PART_ID
        assert metadata.component_type == COMPONENT_TYPE
        assert metadata.component_name == COMPONENT_NAME
        assert metadata.method_name == METHOD_NAME
        assert metadata.method_parameters == METHOD_PARAMETERS
        assert metadata.tags == TAGS
        if test_dataset_ids:
            assert metadata.dataset_ids == DATASET_IDS
