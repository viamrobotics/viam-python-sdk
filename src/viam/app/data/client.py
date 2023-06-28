from typing import List, Optional, Mapping, Any

from grpclib.client import Channel

from viam.proto.app.data import (
    BinaryDataByFilterRequest,
    BinaryDataByFilterResponse,
    BinaryDataByIDsRequest,
    BinaryDataByIDsResponse,
    DataServiceStub,
    DataRequest,
    DeleteBinaryDataByIDsRequest,
    DeleteBinaryDataByIDsResponse,
    DeleteBinaryDataByFilterRequest,
    DeleteBinaryDataByFilterResponse,
    DeleteTabularDataByFilterRequest,
    DeleteTabularDataByFilterResponse,
    Filter,
    TabularDataByFilterRequest,
    TabularDataByFilterResponse,
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

    Constructor is used by AppClient to instantiate relevant service stubs. Calls to DataClient methods should be made through AppClient.
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
        """Filter and download tabular data

        Args:
            filter (viam.app.data.Filter): When supplied, the tabular data will be filtered based on the provided constraints.
                If not provided, all data will be returned.
            dest (str): When supplied, the tabular data will be saved to the provided file path

        Returns:
            List[Mapping[str, Any]]: A list of tabular data
        """
        filter = filter if filter else Filter()
        data_request = DataRequest(filter=filter, limit=100, last="")
        request = TabularDataByFilterRequest(data_request=data_request, count_only=False)
        response: TabularDataByFilterResponse = await self._data_client.TabularDataByFilter(request, metadata=self._metadata)

        resp = [map.data for map in response.data]
        if dest:
            try:
                file = open(dest, 'w')
                file.write(f"{resp}")
            except Exception as e:
                LOGGER.error(f"Failed to write tabular data to file {dest}", exc_info=e)
        return resp

    async def binary_data_by_filter(
        self,
        filter: Optional[Filter],
        dest: Optional[str]
    ) -> List[bytes]:
        """Filter and download binary data

        Args:
            filter (viam.app.data.Filter): When supplied, the binary data will be filtered based on the provided constraints.
                If not provided, all data will be returned.
            dest (str): When supplied, the binary data will be saved to the provided file path

        Returns:
            List[bytes]: The binary data
        """
        filter = filter if filter else Filter()
        data_request = DataRequest(filter=filter, limit=100, last="")
        request = BinaryDataByFilterRequest(data_request=data_request, count_only=False)
        response: BinaryDataByFilterResponse = await self._data_client.BinaryDataByFilter(request, metadata=self._metadata)
        if dest:
            try:
                file = open(dest, 'w')
                file.write(f"{response.data}")
            except Exception as e:
                LOGGER.error(f"Failed to write binary data to file {dest}", exc_info=e)
        return response.data

    async def binary_data_by_ids(self, file_ids: Optional[List[str]], dest: Optional[str]) -> List[bytes]:
        """Filter and download binary data

        Args:
            file_ids (List[str]): When supplied, limits binary data to the provided file IDs. If not provided, all data will be returned.
            dest (str): When supplied, the binary data will be saved to the provided file path

        Returns:
            List[bytes]: The binary data
        """
        file_ids = file_ids if file_ids else []
        request = BinaryDataByIDsRequest(file_ids=file_ids, include_binary=True)
        response: BinaryDataByIDsResponse = await self._data_client.BinaryDataByIDs(request, metadata=self._metadata)
        if dest:
            try:
                file = open(dest, 'w')
                file.write(f"{response.data}")
            except Exception as e:
                LOGGER.error(f"Failed to write binary data to file {dest}", exc_info=e)
        return response.data

    async def delete_tabular_data_by_filter(self, filter: Optional[Filter]) -> None:
        """Delete tabular data

        Args:
            filter (viam.app.data.Filter): When supplied, the tabular data to delete will be filtered based on the provided constraints.
                If not provided, all data will be deleted. Exercise caution before using this option.
        """
        filter = filter if filter else Filter()
        request = DeleteTabularDataByFilterRequest(filter=filter)
        response: DeleteTabularDataByFilterResponse = await self._data_client.DeleteTabularDataByFilter(request, metadata=self._metadata)

    async def delete_binary_data_by_filter(self, filter: Optional[Filter]) -> None:
        """Delete binary data

        Args:
            filter (viam.app.data.Filter): When supplied, the binary data to delete will be filtered based on the provided constraints.
                If not provided, all data will be deleted. Exercise caution before using this option.
        """
        filter = filter if filter else Filter()
        request = DeleteBinaryDataByFilterRequest(filter=filter)
        response: DeleteBinaryDataByFilterResponse = await self._data_client.DeleteBinaryDataByFilter(request, metadata=self._metadata)

    async def delete_binary_data_by_ids(self, file_ids: Optional[List[str]]) -> None:
        """Delete binary data

        Args:
            file_ids (List[str]): When supplied, only the binary data matching the file_ids will be deleted. If not provided,
                all data will be deleted. Exercise caution before using this option.
        """
        file_ids = file_ids if file_ids else []
        request = DeleteBinaryDataByIDsRequest(file_ids=file_ids)
        response: DeleteBinaryDataByIDsResponse = await self._data_client.DeleteBinaryDataByIDs(request, metadata=self._metadata)

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
