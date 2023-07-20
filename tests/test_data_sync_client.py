import pytest
from datetime import datetime
from typing import List

from grpclib.testing import ChannelFor

from viam.app.data.client import DataClient
from viam.proto.app.datasync import (
    UploadMetadata,
    SensorData
)
from viam.utils import struct_to_dict

from .mocks.services import MockDataSync

COMPONENT_NAME = "component_name"
COMPONENT_TYPE = "component_type"
PART_ID = "part_id"
SECONDS_START = 1689256710
NANOS_START = 10
SECONDS_END = 1689256810
NANOS_END = 10
TAGS = ["tag"]
BINARY_DATA = b'binary_data'
METHOD_NAME = "method_name"
DATETIMES = (datetime.now(), datetime.now())
TIMESTAMPS = (DataClient.datetime_to_timestamp(DATETIMES[0]), DataClient.datetime_to_timestamp(DATETIMES[1]))
METHOD_PARAMETERS = {}
TABULAR_DATA = [{"key": "value"}]
FILE_NAME = "file_name"
FILE_EXT = ".file_extension"

AUTH_TOKEN = "auth_token"
DATA_SERVICE_METADATA = {"authorization": f"Bearer {AUTH_TOKEN}"}


@pytest.fixture(scope="function")
def service() -> MockDataSync:
    return MockDataSync()


class TestClient:
    @pytest.mark.asyncio
    async def test_binary_data_capture_upload(self, service: MockDataSync):
        async with ChannelFor([service]) as channel:
            client = DataClient(channel, DATA_SERVICE_METADATA)
            await client.binary_data_capture_upload(
                part_id=PART_ID,
                component_type=COMPONENT_TYPE,
                component_name=COMPONENT_NAME,
                method_name=METHOD_NAME,
                method_parameters=METHOD_PARAMETERS,
                tags=TAGS,
                data_request_times=DATETIMES,
                binary_data=BINARY_DATA
            )
            self.assert_sensor_contents(sensor_contents=service.sensor_contents, is_binary=True)
            self.assert_metadata(metadata=service.metadata)

    @pytest.mark.asyncio
    async def test_tabular_data_capture_upload(self, service: MockDataSync):
        async with ChannelFor([service]) as channel:
            client = DataClient(channel, DATA_SERVICE_METADATA)
            await client.tabular_data_capture_upload(
                part_id=PART_ID,
                component_type=COMPONENT_TYPE,
                component_name=COMPONENT_NAME,
                method_name=METHOD_NAME,
                method_parameters=METHOD_PARAMETERS,
                tags=TAGS,
                data_request_times=[DATETIMES],
                tabular_data=TABULAR_DATA
            )
            self.assert_sensor_contents(sensor_contents=service.sensor_contents, is_binary=False)
            self.assert_metadata(metadata=service.metadata)

    @pytest.mark.asyncio
    async def test_file_upload(self, service: MockDataSync):
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
            self.assert_metadata(service.metadata)
            assert service.metadata.file_name == FILE_NAME
            assert service.metadata.file_extension == FILE_EXT
            assert service.binary_data == BINARY_DATA

    @pytest.mark.asyncio
    async def test_file_upload_from_path(self, service: MockDataSync, tmp_path):
        async with ChannelFor([service]) as channel:
            client = DataClient(channel, DATA_SERVICE_METADATA)
            path = tmp_path / (FILE_NAME + FILE_EXT)
            path.write_bytes(BINARY_DATA)
            await client.file_upload_from_path(
                part_id=PART_ID,
                component_type=COMPONENT_TYPE,
                component_name=COMPONENT_NAME,
                method_name=METHOD_NAME,
                method_parameters=METHOD_PARAMETERS,
                tags=TAGS,
                filepath=path.resolve()
            )
            self.assert_metadata(service.metadata)
            assert service.metadata.file_name == FILE_NAME
            assert service.metadata.file_extension == FILE_EXT
            assert service.binary_data == BINARY_DATA

    def assert_sensor_contents(self, sensor_contents: List[SensorData], is_binary: bool):
        for i in range(len(sensor_contents)):
            assert sensor_contents[i].metadata.time_requested.seconds == TIMESTAMPS[0].seconds
            assert sensor_contents[i].metadata.time_requested.nanos == TIMESTAMPS[0].nanos
            assert sensor_contents[i].metadata.time_received.seconds == TIMESTAMPS[1].seconds
            assert sensor_contents[i].metadata.time_received.nanos == TIMESTAMPS[1].nanos
        if is_binary:
            assert sensor_contents[0].binary == BINARY_DATA
        else:
            assert struct_to_dict(sensor_contents[i].struct) == TABULAR_DATA[i]

    def assert_metadata(self, metadata: UploadMetadata) -> None:
        assert metadata.part_id == PART_ID
        assert metadata.component_type == COMPONENT_TYPE
        assert metadata.component_name == COMPONENT_NAME
        assert metadata.method_name == METHOD_NAME
        assert metadata.method_parameters == METHOD_PARAMETERS
        assert metadata.tags == TAGS
