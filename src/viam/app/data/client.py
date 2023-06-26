from typing import List, Optional, Mapping, Any

from grpclib.client import Channel

from viam.proto.app.data import (
    DataServiceStub,
    Filter,
)
from viam.proto.app.datasync import (
    UploadMetadata,
    SensorData,
    FileData
)
from viam.proto.app.datasync import DataSyncServiceStub
from viam import logging

LOGGER = logging.getLogger(__name__)


class DataClient:
    """gRPC client for uploading and retreiving data from app

    Constructor must be passed a channel to app, along with the required metadata.
    """

    def __init__(self, channel: Channel, metadata: str):
        """
        Create a data client that establishes a connection to app.

        Args:
            channel (Channel): an already-established connection to app.
            metadata (str): the required authorization token to send requests to app.
        """
        self._metadata = metadata
        self._data_client = DataServiceStub(channel)
        self._data_sync_client = DataSyncServiceStub(channel)

    _data_client: DataServiceStub
    _data_sync_client: DataSyncServiceStub
    _metadata: str

    async def tabular_data_by_filter(
        self,
        filter: Optional[Filter],
        dest: Optional[str]
    ) -> List[Mapping[str, Any]]:
        raise NotImplementedError()

    async def binary_data_by_filter(
        self,
        data_request: Optional[Filter],
        dest: Optional[str]
    ) -> List[bytes]:
        raise NotImplementedError()

    async def binary_data_by_ids(self, file_ids: Optional[List[str]]) -> List[bytes]:
        raise NotImplementedError()

    async def delete_tabular_data_by_filter(self, filter: Optional[Filter]) -> None:
        raise NotImplementedError()

    async def delete_binary_data_by_filter(self, filter: Optional[Filter]) -> None:
        raise NotImplementedError()

    async def delete_binary_data_by_ids(self, file_ids: Optional[List[str]]) -> None:
        raise NotImplementedError()

    async def add_tags_to_binary_data_by_file_ids(self, file_ids: Optional[List[str]], tags: Optional[List[str]]) -> None:
        raise NotImplementedError()

    async def add_tags_to_binary_data_by_filter(self, filter: Optional[Filter], tags: Optional[List[str]]) -> None:
        raise NotImplementedError()

    async def remove_tags_from_binary_data_by_file_ids(self, file_ids: Optional[List[str]], tags: Optional[List[str]]) -> None:
        raise NotImplementedError()

    async def remove_tags_from_binary_data_by_filter(self, filter: Optional[Filter], tags: Optional[List[str]]) -> None:
        raise NotImplementedError()

    async def tags_by_filter(self, filter: Optional[Filter]) -> List[str]:
        raise NotImplementedError()

    # to be defined and implemented last
    async def add_bounding_box_to_image_by_id(self):
        raise NotImplementedError()

    # to be defined and implemented last
    async def remove_bounding_box_from_image_by_id(self):
        raise NotImplementedError()

    async def bounding_box_labels_by_filter(self, filter: Optional[Filter]) -> List[str]:
        raise NotImplementedError()

    # TODO (RSDK-3637): confirm arguments
    async def data_capture_upload(self, metadata: Optional[UploadMetadata], sensor_contents: Optional[List[SensorData]]) -> None:
        raise NotImplementedError()

    # TODO (RSDK-3637): confirm arguments
    async def file_upload(self, metadata: Optional[UploadMetadata], file_contents: Optional[FileData]) -> None:
        raise NotImplementedError()
