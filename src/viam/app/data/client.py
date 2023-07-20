from datetime import datetime
from pathlib import Path
from typing import Any, List, Mapping, Optional, Tuple

from google.protobuf.struct_pb2 import Struct
from google.protobuf.timestamp_pb2 import Timestamp
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
    DataCaptureUploadRequest,
    DataCaptureUploadResponse,
    DataSyncServiceStub,
    DataType,
    FileData,
    FileUploadRequest,
    FileUploadResponse,
    SensorData,
    SensorMetadata,
    UploadMetadata,
)
from viam.utils import struct_to_dict

LOGGER = logging.getLogger(__name__)


class DataClient:
    """gRPC client for uploading and retrieving data from app.

    Constructor is used by `AppClient` to instantiate relevant service stubs. Calls to `DataClient` methods should be made through
    `AppClient`.
    """

    def __init__(self, channel: Channel, metadata: Mapping[str, str]):
        """Create a `DataClient` that maintains a connection to app.

        Args:
            channel (Channel): Connection to app.
            metadata (Mapping[str, str]): Required authorization token to send requests to app.
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
        """Filter and download tabular data.

        Args:
            filter (viam.proto.app.data.Filter): Optional `Filter` specifying tabular data to retrieve. No `Filter` implies all tabular
                data.
            dest (str): Optional filepath for writing retrieved data.

        Returns:
            List[Mapping[str, Any]]: The tabular data.
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
            data += [struct_to_dict(struct.data) for struct in response.data]
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
        """Filter and download binary data.

        Args:
            filter (viam.proto.app.data.Filter): Optional `Filter` specifying binary data to retrieve. No `Filter` implies all binary data.
            dest (str): Optional filepath for writing retrieved data.

        Returns:
            List[bytes]: The binary data.
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
            data += [data.binary for data in response.data]
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
        """Filter and download binary data.

        Args:
            binary_ids (List[viam.proto.app.data.BinaryID]): `BinaryID` objects specifying the desired data. Must be non-empty.
            dest (str): Optional filepath for writing retrieved data.

        Raises:
            GRPCError: If no `BinaryID` objects are provided.

        Returns:
            List[bytes]: The binary data.
        """
        request = BinaryDataByIDsRequest(binary_ids=binary_ids, include_binary=True)
        response: BinaryDataByIDsResponse = await self._data_client.BinaryDataByIDs(request, metadata=self._metadata)
        if dest:
            try:
                file = open(dest, "w")
                file.write(f"{response.data}")
            except Exception as e:
                LOGGER.error(f"Failed to write binary data to file {dest}", exc_info=e)
        return [binary_data.binary for binary_data in response.data]

    async def delete_tabular_data_by_filter(self, filter: Optional[Filter]) -> int:
        """Filter and delete tabular data.

        Args:
            filter (viam.proto.app.data.Filter): Optional `Filter` specifying tabular data to delete. Not passing a `Filter` will lead to
                all data being deleted. Exercise caution when using this option.
        """
        filter = filter if filter else Filter()
        request = DeleteTabularDataByFilterRequest(filter=filter)
        response: DeleteTabularDataByFilterResponse = await self._data_client.DeleteTabularDataByFilter(request, metadata=self._metadata)
        return response.deleted_count

    async def delete_binary_data_by_filter(self, filter: Optional[Filter]) -> int:
        """Filter and delete binary data.

        Args:
            filter (viam.proto.app.data.Filter): Optional `Filter` specifying binary data to delete. Not passing a `Filter` will lead to all
                data being deleted. Exercise caution when using this option.
        """
        filter = filter if filter else Filter()
        request = DeleteBinaryDataByFilterRequest(filter=filter)
        response: DeleteBinaryDataByFilterResponse = await self._data_client.DeleteBinaryDataByFilter(request, metadata=self._metadata)
        return response.deleted_count

    async def delete_binary_data_by_ids(self, binary_ids: List[BinaryID]) -> int:
        """Filter and delete binary data.

        Args:
            binary_ids (List[viam.proto.app.data.BinaryID]): `BinaryID` objects specifying the data to be deleted. Must be non-empty.

        Raises:
            GRPCError: If no `BinaryID` objects are provided.

        Returns:
            int: The number of items deleted.
        """
        request = DeleteBinaryDataByIDsRequest(binary_ids=binary_ids)
        response: DeleteBinaryDataByIDsResponse = await self._data_client.DeleteBinaryDataByIDs(request, metadata=self._metadata)
        return response.deleted_count

    async def add_tags_to_binary_data_by_ids(self, tags: List[str], binary_ids: List[BinaryID]) -> None:
        """Add tags to binary data.

        Args:
            tags (List[str]): List of tags to add to specified binary data. Must be non-empty.
            binary_ids (List[viam.app.proto.BinaryID]): List of `BinaryID` objects specifying binary data to tag. Must be non-empty.

        Raises:
            GRPCError: If no `BinaryID` objects or tags are provided.
        """
        request = AddTagsToBinaryDataByIDsRequest(binary_ids=binary_ids, tags=tags)
        _: AddTagsToBinaryDataByIDsResponse = await self._data_client.AddTagsToBinaryDataByIDs(request, metadata=self._metadata)

    async def add_tags_to_binary_data_by_filter(self, tags: List[str], filter: Optional[Filter] = None) -> None:
        """Add tags to binary data.

        Args:
            tags (List[str]): List of tags to add to specified binary data. Must be non-empty.
            filter (viam.proto.app.data.Filter): `Filter` specifying binary data to tag. If no `Filter` is provided, all data will be
                tagged.

        Raises:
            GRPCError: If no tags are provided.
        """
        filter = filter if filter else Filter()
        request = AddTagsToBinaryDataByFilterRequest(filter=filter, tags=tags)
        _: AddTagsToBinaryDataByFilterResponse = await self._data_client.AddTagsToBinaryDataByFilter(request, metadata=self._metadata)

    async def remove_tags_from_binary_data_by_ids(self, tags: List[str], binary_ids: List[BinaryID]) -> int:
        """Remove tags from binary.

        Args:
            tags (List[str]): List of tags to remove from specified binary data. Must be non-empty.
            file_ids (List[str]): List of `BinaryID` objects specifying binary data to untag. Must be non-empty.

        Raises:
            GRPCError: If no binary_ids or tags are provided.

        Returns:
            int: The number of tags removed.
        """
        request = RemoveTagsFromBinaryDataByIDsRequest(binary_ids=binary_ids, tags=tags)
        response: RemoveTagsFromBinaryDataByIDsResponse = await self._data_client.RemoveTagsFromBinaryDataByIDs(
            request, metadata=self._metadata
        )
        return response.deleted_count

    async def remove_tags_from_binary_data_by_filter(self, tags: List[str], filter: Optional[Filter] = None) -> int:
        """Remove tags from binary data.

        Args:
            tags (List[str]): List of tags to remove from specified binary data.
            filter (viam.proto.app.data.Filter): `Filter` specifying binary data to untag. If no `Filter` is provided, all data will be
                tagged.

        Raises:
            GRPCError: If no tags are provided.

        Returns:
            int: The number of tags removed.
        """
        filter = filter if filter else Filter()
        request = RemoveTagsFromBinaryDataByFilterRequest(filter=filter, tags=tags)
        response: RemoveTagsFromBinaryDataByFilterResponse = await self._data_client.RemoveTagsFromBinaryDataByFilter(
            request, metadata=self._metadata
        )
        return response.deleted_count

    async def tags_by_filter(self, filter: Optional[Filter] = None) -> List[str]:
        """Get a list of tags using a filter.

        Args:
            filter (viam.proto.app.data.Filter): `Filter` specifying data to retrieve from. If no `Filter` is provided, all data tags will
                return.

        Returns:
            List[str]: The list of tags.
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
        """Get a list of bounding box labels using a `Filter`.

        Args:
            filter (viam.proto.app.data.Filter): `Filter` specifying data to retrieve from. If no `Filter` is provided, all labels will
                return.

        Returns:
            List[str]: The list of bounding box labels.
        """
        filter = filter if filter else Filter()
        request = BoundingBoxLabelsByFilterRequest(filter=filter)
        response: BoundingBoxLabelsByFilterResponse = await self._data_client.BoundingBoxLabelsByFilter(request, metadata=self._metadata)
        return response.labels

    async def binary_data_capture_upload(
        self,
        part_id: str,
        component_type: str,
        component_name: str,
        method_name: str,
        method_parameters: Optional[Mapping[str, Any]],
        tags: Optional[List[str]],
        data_request_times: Optional[Tuple[Optional[datetime], Optional[datetime]]],
        binary_data: bytes,
    ) -> None:
        """Upload binary sensor data.

        Sync binary data collected on a robot through a specific component (e.g., a motor) along with the relevant metadata with
        app.viam.com. Binary data can be found under the "Files" tab in Data on app.viam.com.

        Args:
            part_id (str): Part ID of the component used to capture the data.
            component_type (str): Type of the component used to capture the data (e.g., "movement_sensor").
            component_name (str): Name of the component used to capture the data.
            method_name (str): Name of the method used to capture the data.
            method_parameters (Optional[Mapping[str, Any]]): Optional dictionary of method parameters. No longer in active use.
            tags (Optional[List[str]]): Optional list of tags to allow for tag-based data filtering when retrieving data.
            data_request_times (Optional[Tuple[datetime.datetime, datetime.datetime]]): Optional tuple containing `datetime`s denoting the
                times this data was requested[0] and received[1] by the appropriate sensor.
            binary_data (bytes): The data to be uploaded, respresented in bytes.

        Raises:
            GRPCError: If an invalid part ID is passed.
        """
        sensor_contents = SensorData(
            metadata=SensorMetadata(
                time_requested=(
                    self.datetime_to_timestamp(data_request_times[0]) if data_request_times and data_request_times[0] else None
                ),
                time_received=(self.datetime_to_timestamp(data_request_times[1]) if data_request_times and data_request_times[1] else None),
            ),
            struct=None,  # Used for tabular data.
            binary=binary_data,
        )
        metadata = UploadMetadata(
            part_id=part_id,
            component_type=component_type,
            component_name=component_name,
            method_name=method_name,
            type=DataType.DATA_TYPE_BINARY_SENSOR,
            file_name=None,  # Not used in app.
            method_parameters=method_parameters if method_parameters else None,
            file_extension=None,  # Will be stored as empty string "".
            tags=tags if tags else None,
        )
        _: DataCaptureUploadResponse = await self._data_capture_upload(metadata=metadata, sensor_contents=[sensor_contents])

    async def tabular_data_capture_upload(
        self,
        part_id: str,
        component_type: str,
        component_name: str,
        method_name: str,
        method_parameters: Optional[Mapping[str, Any]],
        tags: Optional[List[str]],
        data_request_times: Optional[List[Tuple[Optional[datetime], Optional[datetime]]]],
        tabular_data: List[Mapping[str, Any]],
    ) -> None:
        """Upload tabular sensor data.

        Sync tabular data collected on a robot through a specific component (e.g., a motor) along with the relevant metadata with
        app.viam.com. Tabular data can be found under the "Sensors" tab in Data on app.viam.com.

        Args:
            part_id (str): Part ID of the component used to capture the data.
            component_type (str): Type of the component used to capture the data (e.g., "movement_sensor").
            component_name (str): Name of the component used to capture the data.
            method_name (str): Name of the method used to capture the data.
            method_parameters (Optional[Mapping[str, Any]]): Optional dictionary of method parameters. No longer in active use.
            tags (Optional[List[str]]): Optional list of tags to allow for tag-based data filtering when retrieving data.
            data_request_times (Optional[List[Tuple[datetime.datetime, datetime.datetime]]]): Optional list of tuples, each containing
                `datetime`s denoting the times this data was requested[0] and received[1] by the appropriate sensor.
            tabular_data (List[Mapping[str, Any]]): List of the data to be uploaded, represented tabularly as a collection of dictionaries.

        Passing a list of tabular data and Timestamps with length n > 1 will result in n datapoints being uploaded, all tied to the same
        metadata.

        Raises:
            GRPCError: If an invalid part ID is passed.
            AssertionError: If a list of `Timestamp`s is provided and its length does not match the length of the list of tabular data.
        """
        sensor_contents = [None] * len(tabular_data)
        if data_request_times:
            assert len(data_request_times) == len(tabular_data)

        for i in range(len(tabular_data)):
            s = Struct()
            s.update(tabular_data[i])
            sensor_contents[i] = SensorData(
                metadata=SensorMetadata(
                    time_requested=(
                        self.datetime_to_timestamp(data_request_times[i][0]) if data_request_times and data_request_times[i][0] else None
                    ),
                    time_received=(
                        self.datetime_to_timestamp(data_request_times[i][1]) if data_request_times and data_request_times[i][1] else None
                    ),
                ),
                struct=s,
            )

        metadata = UploadMetadata(
            part_id=part_id,
            component_type=component_type,
            component_name=component_name,
            method_name=method_name,
            type=DataType.DATA_TYPE_TABULAR_SENSOR,
            file_name=None,  # Not used in app.
            method_parameters=method_parameters if method_parameters else None,
            file_extension=None,  # Will be stored as empty string "".
            tags=tags if tags else None,
        )
        _: DataCaptureUploadResponse = await self._data_capture_upload(metadata=metadata, sensor_contents=sensor_contents)

    async def _data_capture_upload(self, metadata: UploadMetadata, sensor_contents: List[SensorData]) -> DataCaptureUploadResponse:
        request = DataCaptureUploadRequest(metadata=metadata, sensor_contents=sensor_contents)
        response: DataCaptureUploadResponse = await self._data_sync_client.DataCaptureUpload(request, metadata=self._metadata)
        return response

    async def file_upload(
        self,
        part_id: str,
        component_type: Optional[str],
        component_name: Optional[str],
        method_name: Optional[str],
        file_name: Optional[str],
        method_parameters: Optional[Mapping[str, Any]],
        file_extension: Optional[str],
        tags: Optional[List[str]],
        data: Optional[bytes],
    ) -> None:
        """Upload arbitrary file data.

        Sync file data that may be stored on a robot along with the relevant metadata to app.viam.com.

        Args:
            part_id (str): Part ID of the resource associated with the file.
            component_type (Optional[str]): Optional type of the component associated with the file (e.g., "movement_sensor").
            component_name (Optional[str]): Optional name of the component associated with the file.
            method_name (Optional[str]): Optional name of the method associated with the file.
            file_name (Optional[str]): Optional name of the file. The empty string "" will be assigned as the file name if a one isn't
                provided.
            method_parameters (Optional[str]): Optional dictionary of the method parameters. No longer in active use.
            file_extension (Optional[str]): Optional file extension. The empty string "" will be assigned as the file extension if one isn't
                provided.
            tags (Optional[List[str]]): Optional list of tags to allow for tag-based filtering when retrieving data.
            data: (Optional[bytes]): Optional bytes representing file data to upload.

        Raises:
            GRPCError: If an invalid part ID is passed.
        """
        metadata = UploadMetadata(
            part_id=part_id,
            component_type=component_type if component_type else None,
            component_name=component_name if component_name else None,
            method_name=method_name if method_name else None,
            type=DataType.DATA_TYPE_FILE,
            file_name=file_name if file_name else None,
            method_parameters=method_parameters if method_parameters else None,
            file_extension=file_extension if file_extension else None,
            tags=tags if tags else None,
        )
        _: FileUploadResponse = await self._file_upload(metadata=metadata, file_contents=FileData(data=data))

    async def file_upload_from_path(
        self,
        part_id: str,
        component_type: Optional[str],
        component_name: Optional[str],
        method_name: Optional[str],
        method_parameters: Optional[Mapping[str, Any]],
        tags: Optional[List[str]],
        filepath: str,
    ) -> None:
        """Upload arbitrary file data.

        Sync file data that may be stored on a robot along with the relevant metadata to app.viam.com.

        Args:
            part_id (str): Part ID of the component associated with the file.
            component_type (Optional[str]): Optional type of the component associated with the file (e.g., "movement_sensor").
            component_name (Optional[str]): Optional name of the component associated with the file.
            method_name (Optional[str]): Optional name of the method associated with the file.
            method_parameters (Optional[str]): Optional dictionary of the method parameters. No longer in active use.
            tags (Optional[List[str]]): Optional list of tags to allow for tag-based filtering when retrieving data.
            filepath (str): Absolute filepath of file to be uploaded.

        Raises:
            GRPCError: If an invalid part ID is passed.
            FileNotFoundError: If the provided filepath is not found.
        """
        path = Path(filepath)
        file_name = path.stem
        file_extension = path.suffix if path.suffix != "" else None
        f = open(filepath, "rb")
        data = f.read()
        f.close()

        metadata = UploadMetadata(
            part_id=part_id,
            component_type=component_type if component_type else None,
            component_name=component_name if component_name else None,
            method_name=method_name if method_name else None,
            type=DataType.DATA_TYPE_FILE,
            file_name=file_name,
            method_parameters=method_parameters if method_parameters else None,
            file_extension=file_extension,
            tags=tags if tags else None,
        )
        _: FileUploadResponse = await self._file_upload(metadata=metadata, file_contents=FileData(data=data))

    async def _file_upload(self, metadata: UploadMetadata, file_contents: FileData) -> FileUploadResponse:
        request_metadata = FileUploadRequest(metadata=metadata)
        request_file_contents = FileUploadRequest(file_contents=file_contents)
        async with self._data_sync_client.FileUpload.open(metadata=self._metadata) as stream:
            await stream.send_message(request_metadata)
            await stream.send_message(request_file_contents, end=True)
            response: FileUploadResponse = await stream.recv_message()
            return response

    @staticmethod
    def datetime_to_timestamp(dt: datetime) -> Timestamp:
        """Convert a Python native `datetime` into a `Timestamp`.

        Args:
            dt (datetime.datetime): A `datetime` object. UTC is assumed in the conversion if the object is naive to timezone information.

        Returns:
            google.protobuf.timestamp_pb2.Timestamp: The `Timestamp` object.
        """
        timestamp = Timestamp()
        timestamp.FromDatetime(dt)
        return timestamp
