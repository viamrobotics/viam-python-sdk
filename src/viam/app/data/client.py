from typing import List, Optional, Mapping, Any
from typing_extensions import Self

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
from viam.rpc.dial import DialOptions, _dial_app, _get_access_token
from viam import logging

LOGGER = logging.getLogger(__name__)


class DataClient:
    """gRPC client for uploading and retreiving data from app

    Use connect() to instantiate a DataClient::

            DataClient.connect(...)

    You must ``close()`` a DataClient after its use.
    """

    @classmethod
    async def connect(cls, dial_options: DialOptions) -> Self:
        """
        Create a data client that establishes a connection to app.

        Args:
            dial_options (DialOptions): Required information for authorization and connected to app, creds and auth_entity must be provided.

        Returns:
            Self: the DataClient.
        """
        self = cls()
        self._channel = await _dial_app(dial_options)
        access_token = await _get_access_token(self._channel, dial_options.auth_entity, dial_options)
        self._metadata = {"authorization": f"Bearer {access_token}"}
        self._data_client = DataServiceStub(self._channel)
        self._data_sync_client = DataSyncServiceStub(self._channel)
        return self

    _channel: Channel
    _data_client: DataServiceStub
    _data_sync_client: DataSyncServiceStub
    _metadata: str
    _closed: bool = False

    async def close(self):
        raise NotImplementedError()

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
