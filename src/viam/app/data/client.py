from typing import Any, List, Mapping, Optional

from grpclib.client import Channel

from viam import logging
from viam.proto.app.data import (
    AddTagsToBinaryDataByFilterRequest,
    AddTagsToBinaryDataByFilterResponse,
    AddTagsToBinaryDataByIDsRequest,
    AddTagsToBinaryDataByIDsResponse,
    BinaryDataByFilterRequest,
    BinaryDataByFilterResponse,
    BinaryDataByIDsRequest,
    BinaryDataByIDsResponse,
    BinaryID,
    BoundingBoxLabelsByFilterRequest,
    BoundingBoxLabelsByFilterResponse,
    DataRequest,
    DataServiceStub,
    DeleteBinaryDataByFilterRequest,
    DeleteBinaryDataByFilterResponse,
    DeleteBinaryDataByIDsRequest,
    DeleteBinaryDataByIDsResponse,
    DeleteTabularDataByFilterRequest,
    DeleteTabularDataByFilterResponse,
    Filter,
    RemoveTagsFromBinaryDataByFilterRequest,
    RemoveTagsFromBinaryDataByFilterResponse,
    RemoveTagsFromBinaryDataByIDsRequest,
    RemoveTagsFromBinaryDataByIDsResponse,
    TabularDataByFilterRequest,
    TabularDataByFilterResponse,
    TagsByFilterRequest,
    TagsByFilterResponse,
)
from viam.proto.app.datasync import (
    DataSyncServiceStub,
    FileData,
    SensorData,
    UploadMetadata,
    DataCaptureUploadRequest,
    DataCaptureUploadResponse,
    FileUploadRequest,
    FileUploadResponse
)

LOGGER = logging.getLogger(__name__)


class DataClient:
    """gRPC client for uploading and retreiving data from app

    Constructor is used by AppClient to instantiate relevant service stubs. Calls to DataClient methods should be made through AppClient
    """

    def __init__(self, channel: Channel, metadata: Mapping[str, str]):
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
    _metadata: Mapping[str, str]

    async def tabular_data_by_filter(
        self,
        filter: Optional[Filter] = None,
        dest: Optional[str] = None,
    ) -> List[Mapping[str, Any]]:
        """Filter and download tabular data

        Args:
            filter (viam.app.data.Filter): When supplied, the tabular data will be
            filtered based on the provided constraints. Otherwise, all data is returned.
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
                file = open(dest, "w")
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
            filter (viam.app.data.Filter): When supplied, the binary data will be
            filtered based on the provided constraints. Otherwise, all data is returned.
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
                file = open(dest, "w")
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
                file = open(dest, "w")
                file.write(f"{response.data}")
            except Exception as e:
                LOGGER.error(f"Failed to write binary data to file {dest}", exc_info=e)
        return response.data

    async def delete_tabular_data_by_filter(self, filter: Optional[Filter]) -> int:
        """Delete tabular data

        Args:
            filter (viam.app.data.Filter): When supplied, the tabular data to delete will be filtered based on the provided constraints.
                If not provided, all data will be deleted. Exercise caution before using this option.

        Returns:
            int: The number of items deleted
        """
        filter = filter if filter else Filter()
        request = DeleteTabularDataByFilterRequest(filter=filter)
        response: DeleteTabularDataByFilterResponse = await self._data_client.DeleteTabularDataByFilter(request, metadata=self._metadata)
        return response.deleted_count

    async def delete_binary_data_by_filter(self, filter: Optional[Filter]) -> int:
        """Delete binary data

        Args:
            filter (viam.app.data.Filter): When supplied, the binary data to delete will be filtered based on the provided constraints.
            If not provided, all data will be deleted. Exercise caution before using this option.

        Returns:
            int: the number of items deleted
        """
        filter = filter if filter else Filter()
        request = DeleteBinaryDataByFilterRequest(filter=filter)
        response: DeleteBinaryDataByFilterResponse = await self._data_client.DeleteBinaryDataByFilter(request, metadata=self._metadata)
        return response.deleted_count

    async def delete_binary_data_by_ids(self, binary_ids: List[BinaryID]) -> int:
        """Delete binary data

        Args:
            binary_ids (List[viam.proto.app.BinaryID]): The binary IDs of the data to be deleted. Must be non-empty.

        Raises:
            GRPCError: if no binary_ids are provided.
        """
        request = DeleteBinaryDataByIDsRequest(binary_ids=binary_ids)
        response: DeleteBinaryDataByIDsResponse = await self._data_client.DeleteBinaryDataByIDs(request, metadata=self._metadata)
        return response.deleted_count

    async def add_tags_to_binary_data_by_ids(self, tags: List[str], binary_ids: List[BinaryID]) -> None:
        """Add tags to binary data using BinaryIDs

        Args:
            tags (List[str]): List of tags to add to specified binary data. Must be non-empty
            binary_ids (List[viam.app.proto.BinaryID]): List of BinaryIDs specifying binary data to tag. Must be non-empty

        Raises:
            GRPCError: if no binary_ids or tags are provided
        """
        request = AddTagsToBinaryDataByIDsRequest(binary_ids=binary_ids, tags=tags)
        _: AddTagsToBinaryDataByIDsResponse = await self._data_client.AddTagsToBinaryDataByIDs(request, metadata=self._metadata)

    async def add_tags_to_binary_data_by_filter(self, tags: List[str], filter: Optional[Filter] = None) -> None:
        """Add tags to binary data using a filter

        Args:
            tags (List[str]): List of tags to add to specified binary data. Must be non-empty
            filter (viam.app.proto.Filter): Filter specifying binary data to tag. If no filter is provided, all data will be tagged

        Raises:
            GRPCError: if no tags are provided
        """
        filter = filter if filter else Filter()
        request = AddTagsToBinaryDataByFilterRequest(filter=filter, tags=tags)
        _: AddTagsToBinaryDataByFilterResponse = await self._data_client.AddTagsToBinaryDataByFilter(request, metadata=self._metadata)

    async def remove_tags_from_binary_data_by_ids(self, tags: List[str], binary_ids: List[BinaryID]) -> None:
        """Remove tags from binary data using BinaryIDs

        Args:
            tags (List[str]): List of tags to remove from specified binary data. Must be non-empty
            file_ids (List[str]): List of BinaryIDs specifying binary data to untag. Must be non-empty

        Raises:
            GRPCError: if no binary_ids or tags are provided

        Returns:
            int: the number of tags removed
        """
        request = RemoveTagsFromBinaryDataByIDsRequest(binary_ids=binary_ids, tags=tags)
        response: RemoveTagsFromBinaryDataByIDsResponse = await self._data_client.RemoveTagsFromBinaryDataByIDs(
            request,
            metadata=self._metadata
        )
        return response.deleted_count

    async def remove_tags_from_binary_data_by_filter(self, tags: List[str], filter: Optional[Filter] = None) -> None:
        """Remove tags from binary data using a filter

        Args:
            tags (List[str]): List of tags to remove from specified binary data
            filter (viam.app.proto.Filter): Filter specifying binary data to untag. If no filter is provided, all data will be tagged

        Raises:
            GRPCError: if no tags are provided

        Returns:
            int: the number of tags removed
        """
        filter = filter if filter else Filter()
        request = RemoveTagsFromBinaryDataByFilterRequest(filter=filter, tags=tags)
        response: RemoveTagsFromBinaryDataByFilterResponse = await self._data_client.RemoveTagsFromBinaryDataByFilter(
            request,
            metadata=self._metadata
        )
        return response.deleted_count

    async def tags_by_filter(self, filter: Optional[Filter] = None) -> List[str]:
        """Get a list of tags using a filter

        Args:
            filter (viam.app.proto.Filter): Filter specifying data to retreive from. If no filter is provided, all data tags will return

        Returns:
            List[str]: The list of tags
        """
        filter = filter if filter else Filter()
        request = TagsByFilterRequest(filter=filter)
        response: TagsByFilterResponse = await self._data_client.TagsByFilter(request, metadata=self._metadata)
        return response.tags

    # TODO: implement
    async def add_bounding_box_to_image_by_id(self):
        raise NotImplementedError()

    # TODO: implement
    async def remove_bounding_box_from_image_by_id(self):
        raise NotImplementedError()

    async def bounding_box_labels_by_filter(self, filter: Optional[Filter] = None) -> List[str]:
        """Get a list of bounding box labels using a filter

        Args:
            filter (viam.app.proto.Filter): Filter specifying data to retreive from. If no filter is provided, all labels will return

        Returns:
            List[str]: The list of bounding box labels
        """
        filter = filter if filter else Filter()
        request = BoundingBoxLabelsByFilterRequest(filter=filter)
        response: BoundingBoxLabelsByFilterResponse = await self._data_client.BoundingBoxLabelsByFilter(request, metadata=self._metadata)
        return response.labels

    async def data_capture_upload(self, metadata: UploadMetadata , sensor_contents: List[SensorData]) -> None:
        """Upload binary or tabular sensor data.

        Sync binary or tabular data collected on a robot through a specific component (i.e. a motor) along with the relevant metadata with
        app.viam.com.

        Args:
            metadata (viam.app.proto.datasync.UploadMetaData): Metadata relating the data collected with the corresponding robot part. Must
                specify a part ID, component type, component name, method name, and data type.
            sensor_contents (List[viam.app.proto.datasync.SensorData]): A list of the data to be uploaded. If the metadata specifies a
                binary data type, the "binary" field of sensor_contents will be uploaded. Alternatively, the "struct" field will be uploaded
                if the data type is tabular. Length of sensor_contents must be 1 if uploading a binary data capture. Otherwise, must simply
                be nonempty.

        Raises:
            GRPCError: If a required data field is not defined.
        """
        request = DataCaptureUploadRequest(metadata=metadata, sensor_contents=sensor_contents)
        _: DataCaptureUploadResponse = await self._data_sync_client.DataCaptureUpload(request, metadata=self._metadata)

    async def file_upload(self, metadata: UploadMetadata, file_contents: Optional[FileData]) -> None:
        """Upload arbitrary file data.

        Sync file data that may be stored on a robot along with the relevant metadata to app.viam.com.

        Args:
            metadata (viam.app.proto.datasync.UploadMetaData): Metadata for the file to be uploaded. Must specify a part ID.
            file_contents (List[viam.app.proto.datasync.FileData]): A FileData object containing binary data to upload as a file.

        Raises:
            GRPCError: If an invalid part ID is provided as metadata.
        """
        request_metadata = FileUploadRequest(metadata=metadata)
        request_file_contents = FileUploadRequest(file_contents=file_contents)
        async with self._data_sync_client.FileUpload.open(metadata=self._metadata, timeout=10) as stream:
            await stream.send_message(request_metadata)
            await stream.send_message(request_file_contents, end=True)
            _: FileUploadResponse = await stream.recv_message()
