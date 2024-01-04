import warnings
from datetime import datetime
from pathlib import Path
from typing import Any, List, Mapping, Optional, Tuple

from google.protobuf.struct_pb2 import Struct
from grpclib.client import Channel, Stream

from viam import logging
from viam.proto.app.data import (
    AddBoundingBoxToImageByIDRequest,
    AddBoundingBoxToImageByIDResponse,
    AddTagsToBinaryDataByFilterRequest,
    AddTagsToBinaryDataByIDsRequest,
    BinaryDataByFilterRequest,
    BinaryDataByFilterResponse,
    BinaryDataByIDsRequest,
    BinaryDataByIDsResponse,
    BinaryID,
    BinaryMetadata,
    BoundingBoxLabelsByFilterRequest,
    BoundingBoxLabelsByFilterResponse,
    CaptureMetadata,
    DataRequest,
    DataServiceStub,
    DeleteBinaryDataByFilterRequest,
    DeleteBinaryDataByFilterResponse,
    DeleteBinaryDataByIDsRequest,
    DeleteBinaryDataByIDsResponse,
    DeleteTabularDataRequest,
    DeleteTabularDataResponse,
    Filter,
    GetDatabaseConnectionRequest,
    GetDatabaseConnectionResponse,
    RemoveBoundingBoxFromImageByIDRequest,
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
    DataCaptureUploadMetadata,
    DataCaptureUploadRequest,
    DataCaptureUploadResponse,
    DataSyncServiceStub,
    DataType,
    FileData,
    FileUploadRequest,
    FileUploadResponse,
    SensorData,
    SensorMetadata,
    StreamingDataCaptureUploadRequest,
    StreamingDataCaptureUploadResponse,
    UploadMetadata,
)
from viam.utils import create_filter, datetime_to_timestamp, struct_to_dict

LOGGER = logging.getLogger(__name__)


class DataClient:
    """gRPC client for uploading and retrieving data from app.

    Constructor is used by `ViamClient` to instantiate relevant service stubs. Calls to `DataClient` methods should be made through
    `ViamClient`.
    """

    class TabularData:
        """Class representing a piece of tabular data and associated metadata.

        Args:
            data (Mapping[str, Any]): the requested data.
            metadata (viam.proto.app.data.CaptureMetadata): the metadata from the request.
            time_requested (datetime): the time the data request was sent.
            time_received (datetime): the time the requested data was received.
        """

        def __init__(self, data: Mapping[str, Any], metadata: CaptureMetadata, time_requested: datetime, time_received: datetime) -> None:
            self.data = data
            self.metadata = metadata
            self.time_requested = time_requested
            self.time_received = time_received

        data: Mapping[str, Any]
        metadata: CaptureMetadata
        time_requested: datetime
        time_received: datetime

        def __str__(self) -> str:
            return f"{self.data}\n{self.metadata}Time requested: {self.time_requested}\nTime received: {self.time_received}\n"

        def __eq__(self, other: object) -> bool:
            if isinstance(other, DataClient.TabularData):
                return str(self) == str(other)
            return False

    class BinaryData:
        """Class representing a piece of binary data and associated metadata.

        Args:
            data (bytes): the requested data.
            metadata (viam.proto.app.data.BinaryMetadata): the metadata from the request.
        """

        def __init__(self, data: bytes, metadata: BinaryMetadata) -> None:
            self.data = data
            self.metadata = metadata

        data: bytes
        metadata: BinaryMetadata

        def __str__(self) -> str:
            return f"{self.data}\n{self.metadata}"

        def __eq__(self, other: object) -> bool:
            if isinstance(other, DataClient.BinaryData):
                return str(self) == str(other)
            return False

    def __init__(self, channel: Channel, metadata: Mapping[str, str]):
        """Create a `DataClient` that maintains a connection to app.

        Args:
            channel (grpclib.client.Channel): Connection to app.
            metadata (Mapping[str, str]): Required authorization token to send requests to app.
        """
        self._metadata = metadata
        self._data_client = DataServiceStub(channel)
        self._data_sync_client = DataSyncServiceStub(channel)
        self._channel = channel

    _data_client: DataServiceStub
    _data_sync_client: DataSyncServiceStub
    _metadata: Mapping[str, str]
    _channel: Channel

    async def tabular_data_by_filter(
        self,
        filter: Optional[Filter] = None,
        dest: Optional[str] = None,
    ) -> List[TabularData]:
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
            data += [
                DataClient.TabularData(
                    struct_to_dict(struct.data),
                    response.metadata[struct.metadata_index],
                    struct.time_requested.ToDatetime(),
                    struct.time_received.ToDatetime(),
                )
                for struct in response.data
            ]
            last = response.last

        if dest:
            try:
                file = open(dest, "w")
                file.write(f"{[str(d) for d in data]}")
                file.flush()
            except Exception as e:
                LOGGER.error(f"Failed to write tabular data to file {dest}", exc_info=e)
        return data

    async def binary_data_by_filter(
        self, filter: Optional[Filter] = None, dest: Optional[str] = None, include_file_data: bool = True, num_files: Optional[int] = None
    ) -> List[BinaryData]:
        """Filter and download binary data.

        Args:
            filter (Optional[viam.proto.app.data.Filter]): Optional `Filter` specifying binary data to retrieve. No `Filter` implies all
                binary data.
            dest (Optional[str]): Optional filepath for writing retrieved data.
            include_file_data (bool): Boolean specifying whether to actually include the binary file data with each retrieved file. Defaults
                to true (i.e., both the files' data and metadata are returned).
            num_files (Optional[str]): Number of binary data to return. Passing 0 returns all binary data matching the filter no matter.
                Defaults to 100 if no binary data is requested, otherwise 10. All binary data or the first `num_files` will be returned,
                    whichever comes first.

        Raises:
            ValueError: If `num_files` is less than 0.

        Returns:
            List[bytes]: The binary data.
        """
        num_files = num_files if num_files else 10 if include_file_data else 100
        if num_files < 0:
            raise ValueError("num_files must be at least 0.")
        filter = filter if filter else Filter()
        limit = 1 if include_file_data else 100
        last = ""
        data = []

        # `DataRequest`s are limited in pieces of data, so we loop through calls until
        # we are certain we've received everything.
        while True:
            new_data, last = await self._binary_data_by_filter(filter=filter, limit=limit, include_binary=include_file_data, last=last)
            if not new_data or len(new_data) == 0:
                break
            elif num_files != 0 and len(new_data) > num_files:
                data += new_data[0:num_files]
                break
            else:
                data += new_data
                num_files -= len(new_data)
                if num_files == 0:
                    break

        if dest:
            try:
                file = open(dest, "w")
                file.write(f"{[str(d) for d in data]}")
                file.flush()
            except Exception as e:
                LOGGER.error(f"Failed to write binary data to file {dest}", exc_info=e)

        return data

    async def _binary_data_by_filter(self, filter: Filter, limit: int, include_binary: bool, last: str) -> Tuple[List[BinaryData], str]:
        data_request = DataRequest(filter=filter, limit=limit, last=last)
        request = BinaryDataByFilterRequest(data_request=data_request, count_only=False, include_binary=include_binary)
        response: BinaryDataByFilterResponse = await self._data_client.BinaryDataByFilter(request, metadata=self._metadata)
        return [DataClient.BinaryData(data.binary, data.metadata) for data in response.data], response.last

    async def binary_data_by_ids(
        self,
        binary_ids: List[BinaryID],
        dest: Optional[str] = None,
    ) -> List[BinaryData]:
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
                file.flush()
            except Exception as e:
                LOGGER.error(f"Failed to write binary data to file {dest}", exc_info=e)
        return [DataClient.BinaryData(data.binary, data.metadata) for data in response.data]

    async def delete_tabular_data(self, organization_id: str, delete_older_than_days: int) -> int:
        """Delete tabular data older than a specified number of days.

        Args:
            organization_id (str): ID of organization to delete data from.
            delete_older_than_days (int): Delete data that was captured up to this many days ago. For example if `delete_older_than_days`
                is 10, this deletes any data that was captured up to 10 days ago. If it is 0, all existing data is deleted.
        """
        request = DeleteTabularDataRequest(organization_id=organization_id, delete_older_than_days=delete_older_than_days)
        response: DeleteTabularDataResponse = await self._data_client.DeleteTabularData(request, metadata=self._metadata)
        return response.deleted_count

    async def delete_tabular_data_by_filter(self, filter: Optional[Filter]) -> int:
        """Deprecated: use delete_tabular_data instead."""
        raise NotImplementedError()

    async def delete_binary_data_by_filter(self, filter: Optional[Filter]) -> int:
        """Filter and delete binary data.

        Args:
            filter (viam.proto.app.data.Filter): Optional `Filter` specifying binary data to delete. Passing an empty `Filter` will lead to
                all data being deleted. Exercise caution when using this option.
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
        await self._data_client.AddTagsToBinaryDataByIDs(request, metadata=self._metadata)

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
        await self._data_client.AddTagsToBinaryDataByFilter(request, metadata=self._metadata)

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
                untagged.

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
        return list(response.tags)

    async def add_bounding_box_to_image_by_id(
        self,
        binary_id: BinaryID,
        label: str,
        x_min_normalized: float,
        y_min_normalized: float,
        x_max_normalized: float,
        y_max_normalized: float,
    ) -> str:
        """Add a bounding box to an image.

        Args:
            binary_id (viam.proto.app.data.BinaryID): The ID of the image to add the bounding box to.
            label (str): A label for the bounding box.
            x_min_normalized (float): Min X value of the bounding box normalized from 0 to 1.
            y_min_normalized (float): Min Y value of the bounding box normalized from 0 to 1.
            x_max_normalized (float): Max X value of the bounding box normalized from 0 to 1.
            y_max_normalized (float): Max Y value of the bounding box normalized from 0 to 1.

        Raises:
            GRPCError: If the X or Y values are outside of the [0, 1] range.

        Returns:
            str: The bounding box ID
        """
        request = AddBoundingBoxToImageByIDRequest(
            label=label,
            binary_id=binary_id,
            x_max_normalized=x_max_normalized,
            x_min_normalized=x_min_normalized,
            y_max_normalized=y_max_normalized,
            y_min_normalized=y_min_normalized,
        )
        response: AddBoundingBoxToImageByIDResponse = await self._data_client.AddBoundingBoxToImageByID(request, metadata=self._metadata)
        return response.bbox_id

    async def remove_bounding_box_from_image_by_id(self, bbox_id: str, binary_id: BinaryID) -> None:
        """Removes a bounding box from an image.

        Args:
            bbox_id (str): The ID of the bounding box to remove.
            Binary_id (viam.proto.arr.data.BinaryID): Binary ID of the image to to remove the bounding box from
        """
        request = RemoveBoundingBoxFromImageByIDRequest(bbox_id=bbox_id, binary_id=binary_id)
        await self._data_client.RemoveBoundingBoxFromImageByID(request, metadata=self._metadata)

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
        return list(response.labels)

    async def get_database_connection(self, organization_id: str) -> str:
        """Get a connection to access a MongoDB Atlas Data federation instance.

        Args:
            organization_id (str): Organization to retrieve the connection for.

        Returns:
            str: The hostname of the federated database.
        """
        request = GetDatabaseConnectionRequest(organization_id=organization_id)
        response: GetDatabaseConnectionResponse = await self._data_client.GetDatabaseConnection(request, metadata=self._metadata)
        return response.hostname

    # TODO(RSDK-5569): implement
    async def configure_database_user(self, organization_id: str, password: str) -> None:
        raise NotImplementedError()

    async def binary_data_capture_upload(
        self,
        binary_data: bytes,
        part_id: str,
        component_type: str,
        component_name: str,
        method_name: str,
        file_extension: str,
        method_parameters: Optional[Mapping[str, Any]] = None,
        tags: Optional[List[str]] = None,
        data_request_times: Optional[Tuple[datetime, datetime]] = None,
    ) -> str:
        """Upload binary sensor data.

        Upload binary data collected on a robot through a specific component (e.g., a motor) along with the relevant metadata to
        app.viam.com. Binary data can be found under the "Files" subtab of the Data tab on app.viam.com.

        Args:
            binary_data (bytes): The data to be uploaded, represented in bytes.
            part_id (str): Part ID of the component used to capture the data.
            component_type (str): Type of the component used to capture the data (e.g., "movement_sensor").
            component_name (str): Name of the component used to capture the data.
            method_name (str): Name of the method used to capture the data.
            file_extension (str): The file extension of binary data including the period, e.g. .jpg, .png, .pcd.
                The backend will route the binary to its corresponding mime type based on this extension. Files with a .jpeg, .jpg,
                or .png extension will be saved to the images tab.
            method_parameters (Optional[Mapping[str, Any]]): Optional dictionary of method parameters. No longer in active use.
            tags (Optional[List[str]]): Optional list of tags to allow for tag-based data filtering when retrieving data.
            data_request_times (Optional[Tuple[datetime.datetime, datetime.datetime]]): Optional tuple containing `datetime`s objects
                denoting the times this data was requested[0] by the robot and received[1] from the appropriate sensor.

        Raises:
            GRPCError: If an invalid part ID is passed.
        """
        sensor_contents = SensorData(
            metadata=(
                SensorMetadata(
                    time_requested=datetime_to_timestamp(data_request_times[0]) if data_request_times else None,
                    time_received=datetime_to_timestamp(data_request_times[1]) if data_request_times else None,
                )
                if data_request_times
                else None
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
            method_parameters=method_parameters,
            tags=tags,
        )
        if file_extension:
            metadata.file_extension = file_extension if file_extension[0] == "." else f".{file_extension}"
        response = await self._data_capture_upload(metadata=metadata, sensor_contents=[sensor_contents])
        return response.file_id

    async def tabular_data_capture_upload(
        self,
        tabular_data: List[Mapping[str, Any]],
        part_id: str,
        component_type: str,
        component_name: str,
        method_name: str,
        method_parameters: Optional[Mapping[str, Any]] = None,
        tags: Optional[List[str]] = None,
        data_request_times: Optional[List[Tuple[datetime, datetime]]] = None,
    ) -> str:
        """Upload tabular sensor data.

        Upload tabular data collected on a robot through a specific component (e.g., a motor) along with the relevant metadata to
        app.viam.com. Tabular data can be found under the "Sensors" subtab of the Data tab on app.viam.com.

        Args:
            tabular_data (List[Mapping[str, Any]]): List of the data to be uploaded, represented tabularly as a collection of dictionaries.
            part_id (str): Part ID of the component used to capture the data.
            component_type (str): Type of the component used to capture the data (e.g., "movement_sensor").
            component_name (str): Name of the component used to capture the data.
            method_name (str): Name of the method used to capture the data.
            method_parameters (Optional[Mapping[str, Any]]): Optional dictionary of method parameters. No longer in active use.
            tags (Optional[List[str]]): Optional list of tags to allow for tag-based data filtering when retrieving data.
            data_request_times (Optional[List[Tuple[datetime.datetime, datetime.datetime]]]): Optional list of tuples, each containing
                `datetime` objects denoting the times this data was requested[0] by the robot and received[1] from the appropriate sensor.


        Passing a list of tabular data and Timestamps with length n > 1 will result in n datapoints being uploaded, all tied to the same
        metadata.

        Raises:
            GRPCError: If an invalid part ID is passed.
            ValueError: If a list of `Timestamp` objects is provided and its length does not match the length of the list of tabular
                data.
        """
        sensor_contents = []
        if data_request_times:
            if len(data_request_times) != len(tabular_data):
                raise ValueError("data_request_times and tabular_data lengths must be equal.")

        for idx, tab in enumerate(tabular_data):
            s = Struct()
            s.update(tab)
            sensor_contents.append(
                SensorData(
                    metadata=(
                        SensorMetadata(
                            time_requested=datetime_to_timestamp(data_request_times[idx][0]) if data_request_times else None,
                            time_received=datetime_to_timestamp(data_request_times[idx][1]) if data_request_times else None,
                        )
                        if data_request_times[idx]
                        else None
                    )
                    if data_request_times
                    else None,
                    struct=s,
                )
            )

        metadata = UploadMetadata(
            part_id=part_id,
            component_type=component_type,
            component_name=component_name,
            method_name=method_name,
            type=DataType.DATA_TYPE_TABULAR_SENSOR,
            method_parameters=method_parameters,
            tags=tags,
        )
        response = await self._data_capture_upload(metadata=metadata, sensor_contents=sensor_contents)
        return response.file_id

    async def _data_capture_upload(self, metadata: UploadMetadata, sensor_contents: List[SensorData]) -> DataCaptureUploadResponse:
        request = DataCaptureUploadRequest(metadata=metadata, sensor_contents=sensor_contents)
        response: DataCaptureUploadResponse = await self._data_sync_client.DataCaptureUpload(request, metadata=self._metadata)
        return response

    async def streaming_data_capture_upload(
        self,
        data: bytes,
        part_id: str,
        file_ext: str,
        component_type: Optional[str] = None,
        component_name: Optional[str] = None,
        method_name: Optional[str] = None,
        method_parameters: Optional[Mapping[str, Any]] = None,
        data_request_times: Optional[Tuple[datetime, datetime]] = None,
        tags: Optional[List[str]] = None,
    ) -> str:
        """Uploads the metadata and contents of streaming binary data.

        Args:
            data (bytes): the data to be uploaded.
            part_id (str): Part ID of the resource associated with the file.
            file_ext (str): file extension type for the data. required for determining MIME type.
            component_type (Optional[str]): Optional type of the component associated with the file (e.g., "movement_sensor").
            component_name (Optional[str]): Optional name of the component associated with the file.
            method_name (Optional[str]): Optional name of the method associated with the file.
            method_parameters (Optional[str]): Optional dictionary of the method parameters. No longer in active use.
            data_request_times (Optional[Tuple[datetime.datetime, datetime.datetime]]): Optional tuple containing `datetime`s objects
                denoting the times this data was requested[0] by the robot and received[1] from the appropriate sensor.
            tags (Optional[List[str]]): Optional list of tags to allow for tag-based filtering when retrieving data.

        Raises:
            GRPCError: If an invalid part ID is passed.

        Returns:
            str: the file_id of the uploaded data.
        """

        upload_metadata = UploadMetadata(
            part_id=part_id,
            component_type=component_type if component_type else "",
            component_name=component_name if component_name else "",
            method_name=method_name if method_name else "",
            method_parameters=method_parameters,
            type=DataType.DATA_TYPE_BINARY_SENSOR,
            file_extension=file_ext if file_ext[0] == "." else f".{file_ext}",
            tags=tags,
        )
        sensor_metadata = SensorMetadata(
            time_requested=datetime_to_timestamp(data_request_times[0]) if data_request_times else None,
            time_received=datetime_to_timestamp(data_request_times[1]) if data_request_times else None,
        )
        metadata = DataCaptureUploadMetadata(upload_metadata=upload_metadata, sensor_metadata=sensor_metadata)
        request_metadata = StreamingDataCaptureUploadRequest(metadata=metadata)
        stream: Stream[StreamingDataCaptureUploadRequest, StreamingDataCaptureUploadResponse]
        async with self._data_sync_client.StreamingDataCaptureUpload.open(metadata=self._metadata) as stream:
            await stream.send_message(request_metadata)
            await stream.send_message(StreamingDataCaptureUploadRequest(data=data), end=True)
            response = await stream.recv_message()
            if not response:
                await stream.recv_trailing_metadata()  # causes us to throw appropriate gRPC error
                raise TypeError("Response cannot be empty")
            return response.file_id

    async def file_upload(
        self,
        part_id: str,
        data: bytes,
        component_type: Optional[str] = None,
        component_name: Optional[str] = None,
        method_name: Optional[str] = None,
        file_name: Optional[str] = None,
        method_parameters: Optional[Mapping[str, Any]] = None,
        file_extension: Optional[str] = None,
        tags: Optional[List[str]] = None,
    ) -> str:
        """Upload arbitrary file data.

        Upload file data that may be stored on a robot along with the relevant metadata to app.viam.com. File data can be found under the
        "Files" subtab of the Data tab on app.viam.com.

        Args:
            part_id (str): Part ID of the resource associated with the file.
            data (bytes): Bytes representing file data to upload.
            component_type (Optional[str]): Optional type of the component associated with the file (e.g., "movement_sensor").
            component_name (Optional[str]): Optional name of the component associated with the file.
            method_name (Optional[str]): Optional name of the method associated with the file.
            file_name (Optional[str]): Optional name of the file. The empty string "" will be assigned as the file name if one isn't
                provided.
            method_parameters (Optional[str]): Optional dictionary of the method parameters. No longer in active use.
            file_extension (Optional[str]): Optional file extension. The empty string "" will be assigned as the file extension if one isn't
                provided. Files with a .jpeg, .jpg, or .png extension will be saved to the images tab.
            tags (Optional[List[str]]): Optional list of tags to allow for tag-based filtering when retrieving data.

        Raises:
            GRPCError: If an invalid part ID is passed.

        Returns:
            str: ID of the new file.
        """
        metadata = UploadMetadata(
            part_id=part_id,
            component_type=component_type if component_type else "",
            component_name=component_name if component_name else "",
            method_name=method_name if method_name else "",
            type=DataType.DATA_TYPE_FILE,
            file_name=file_name if file_name else "",
            method_parameters=method_parameters,
            file_extension=file_extension if file_extension else "",
            tags=tags,
        )
        response: FileUploadResponse = await self._file_upload(metadata=metadata, file_contents=FileData(data=data))
        return response.file_id

    async def file_upload_from_path(
        self,
        filepath: str,
        part_id: str,
        component_type: Optional[str] = None,
        component_name: Optional[str] = None,
        method_name: Optional[str] = None,
        method_parameters: Optional[Mapping[str, Any]] = None,
        tags: Optional[List[str]] = None,
    ) -> str:
        """Upload arbitrary file data.

        Upload file data that may be stored on a robot along with the relevant metadata to app.viam.com. File data can be found under the
        "Files" subtab of the Data tab on app.viam.com.

        Args:
            filepath (str): Absolute filepath of file to be uploaded.
            part_id (str): Part ID of the component associated with the file.
            component_type (Optional[str]): Optional type of the component associated with the file (e.g., "movement_sensor").
            component_name (Optional[str]): Optional name of the component associated with the file.
            method_name (Optional[str]): Optional name of the method associated with the file.
            method_parameters (Optional[str]): Optional dictionary of the method parameters. No longer in active use.
            tags (Optional[List[str]]): Optional list of tags to allow for tag-based filtering when retrieving data.


        Raises:
            GRPCError: If an invalid part ID is passed.
            FileNotFoundError: If the provided filepath is not found.

        Returns:
            str: ID of the new file.
        """
        path = Path(filepath)
        file_name = path.stem
        file_extension = path.suffix if path.suffix != "" else None
        f = open(filepath, "rb")
        data = f.read()
        f.close()

        metadata = UploadMetadata(
            part_id=part_id,
            component_type=component_type if component_type else "",
            component_name=component_name if component_name else "",
            method_name=method_name if method_name else "",
            type=DataType.DATA_TYPE_FILE,
            file_name=file_name,
            method_parameters=method_parameters,
            file_extension=file_extension if file_extension else "",
            tags=tags,
        )
        response: FileUploadResponse = await self._file_upload(metadata=metadata, file_contents=FileData(data=data if data else bytes()))
        return response.file_id

    async def _file_upload(self, metadata: UploadMetadata, file_contents: FileData) -> FileUploadResponse:
        request_metadata = FileUploadRequest(metadata=metadata)
        request_file_contents = FileUploadRequest(file_contents=file_contents)
        stream: Stream[FileUploadRequest, FileUploadResponse]
        async with self._data_sync_client.FileUpload.open(metadata=self._metadata) as stream:
            await stream.send_message(request_metadata)
            await stream.send_message(request_file_contents, end=True)
            response = await stream.recv_message()
            if not response:
                await stream.recv_trailing_metadata()  # causes us to throw appropriate gRPC error.
                raise TypeError("Response cannot be empty")
            return response

    @staticmethod
    def create_filter(
        component_name: Optional[str] = None,
        component_type: Optional[str] = None,
        method: Optional[str] = None,
        robot_name: Optional[str] = None,
        robot_id: Optional[str] = None,
        part_name: Optional[str] = None,
        part_id: Optional[str] = None,
        location_ids: Optional[List[str]] = None,
        organization_ids: Optional[List[str]] = None,
        mime_type: Optional[List[str]] = None,
        start_time: Optional[datetime] = None,
        end_time: Optional[datetime] = None,
        tags: Optional[List[str]] = None,
        bbox_labels: Optional[List[str]] = None,
    ) -> Filter:
        warnings.warn("DataClient.create_filter is deprecated. Use AppClient.create_filter instead.", DeprecationWarning, stacklevel=2)
        return create_filter(
            component_name,
            component_type,
            method,
            robot_name,
            robot_id,
            part_name,
            part_id,
            location_ids,
            organization_ids,
            mime_type,
            start_time,
            end_time,
            tags,
            bbox_labels,
        )
