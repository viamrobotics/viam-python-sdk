from typing import List, Optional, Mapping, Any

from grpclib.client import Channel

from viam.proto.app.data import (
    BinaryDataByFilterRequest,
    BinaryDataByFilterResponse,
    BinaryDataByIDsRequest,
    BinaryDataByIDsResponse,
    BinaryID,
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
        filter: Optional[Filter] = None,
        dest: Optional[str] = None,
    ) -> List[Mapping[str, Any]]:
        """Filter and download tabular data

        Args:
            filter (viam.app.data.Filter): When supplied, the tabular data will be filtered based on the provided constraints. Otherwise, all data is returned.
            dest (str): When supplied, the tabular data will be saved to the provided file path.

        Returns:
            List[Mapping[str, Any]]: A list of tabular data
        """
        filter = filter if filter else Filter()
        last = ""
        data = []

        # `DataRequest`s are limited to 100 pieces of data, so we loop through calls until
        # we are certain we've received everything.
        while True:
            data_request = DataRequest(filter=filter, limit=100, last=last)
            request = TabularDataByFilterRequest(data_request=data_request, count_only=False)
            response: TabularDataByFilterResponse = await self._data_client.TabularDataByFilter(request, metadata=self._metadata)
            if not response.data or len(response.data) == 0:
                break
            data += [struct.data for struct in response.data]
            last = response.last

        if dest:
            try:
                file = open(dest, 'w')
                file.write(f"{data}")
            except Exception as e:
                LOGGER.error(f"Failed to write tabular data to file {dest}", exc_info=e)
        return data

    async def binary_data_by_filter(
        self,
        filter: Optional[Filter] = None,
        dest: Optional[str] = None,
    ) -> List[bytes]:
        """Filter and download binary data

        Args:
            filter (viam.app.data.Filter): When supplied, the binary data will be filtered based on the provided constraints. Otherwise, all data is returned.
            dest (str): When supplied, the binary data will be saved to the provided file path

        Returns:
            List[bytes]: The binary data
        """
        filter = filter if filter else Filter()
        last = ""
        data = []

        # `DataRequest`s are limited to 100 pieces of data, so we loop through calls until
        # we are certain we've received everything.
        while True:
            data_request = DataRequest(filter=filter, limit=100, last=last)
            request = BinaryDataByFilterRequest(data_request=data_request, count_only=False)
            response: BinaryDataByFilterResponse = await self._data_client.BinaryDataByFilter(request, metadata=self._metadata)
            if not response.data or len(response.data) == 0:
                break
            data += list(response.data)
            last = response.last

        if dest:
            try:
                file = open(dest, 'w')
                file.write(f"{data}")
            except Exception as e:
                LOGGER.error(f"Failed to write binary data to file {dest}", exc_info=e)

        return data

    async def binary_data_by_ids(
        self,
        binary_ids: List[BinaryID],
        dest: Optional[str] = None,
    ) -> List[bytes]:
        """Filter and download binary data

        Args:
            binary_ids (List[viam.proto.app.BinaryID]): IDs of the desired data. Must be non-empty.
            dest (str): When supplied, the binary data will be saved to the provided file path.

        Returns:
            List[bytes]: The binary data.

        Raises:
            GRPCError: if no binary_ids are provided.
        """
        request = BinaryDataByIDsRequest(binary_ids=binary_ids, include_binary=True)
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

    async def delete_binary_data_by_ids(self, binary_ids: List[BinaryID]) -> None:
        """Delete binary data

        Args:
            binary_ids (List[viam.proto.app.BinaryID]): The binary IDs of the data to be deleted. Must be non-empty.

        Raises:
            GRPCError: if no binary_ids are provided.
        """
        request = DeleteBinaryDataByIDsRequest(binary_ids=binary_ids)
        response: DeleteBinaryDataByIDsResponse = await self._data_client.DeleteBinaryDataByIDs(request, metadata=self._metadata)

    async def add_tags_to_binary_data_by_binary_ids(self, binary_ids: Optional[List[str]], tags: Optional[List[str]]) -> None:
        raise NotImplementedError()

    async def add_tags_to_binary_data_by_filter(self, filter: Optional[Filter], tags: Optional[List[str]]) -> None:
        raise NotImplementedError()

    async def remove_tags_from_binary_data_by_binary_ids(self, binary_ids: Optional[List[str]], tags: Optional[List[str]]) -> None:
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
