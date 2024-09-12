import warnings
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Mapping, Optional, Sequence, Tuple

from google.protobuf.struct_pb2 import Struct
from grpclib.client import Channel, Stream

from viam import logging
from viam.proto.app.data import (
    AddBinaryDataToDatasetByIDsRequest,
    AddBoundingBoxToImageByIDRequest,
    AddBoundingBoxToImageByIDResponse,
    AddTagsToBinaryDataByFilterRequest,
    AddTagsToBinaryDataByIDsRequest,
    BinaryData,
    BinaryDataByFilterRequest,
    BinaryDataByFilterResponse,
    BinaryDataByIDsRequest,
    BinaryDataByIDsResponse,
    BinaryID,
    BoundingBoxLabelsByFilterRequest,
    BoundingBoxLabelsByFilterResponse,
    CaptureMetadata,
    ConfigureDatabaseUserRequest,
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
    Order,
    RemoveBinaryDataFromDatasetByIDsRequest,
    RemoveBoundingBoxFromImageByIDRequest,
    RemoveTagsFromBinaryDataByFilterRequest,
    RemoveTagsFromBinaryDataByFilterResponse,
    RemoveTagsFromBinaryDataByIDsRequest,
    RemoveTagsFromBinaryDataByIDsResponse,
    TabularDataByFilterRequest,
    TabularDataByFilterResponse,
    TabularDataByMQLRequest,
    TabularDataByMQLResponse,
    TabularDataBySQLRequest,
    TabularDataBySQLResponse,
    TagsByFilterRequest,
    TagsByFilterResponse,
)
from viam.proto.app.dataset import (
    CreateDatasetRequest,
    CreateDatasetResponse,
    Dataset,
    DatasetServiceStub,
    DeleteDatasetRequest,
    ListDatasetsByIDsRequest,
    ListDatasetsByIDsResponse,
    ListDatasetsByOrganizationIDRequest,
    ListDatasetsByOrganizationIDResponse,
    RenameDatasetRequest,
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
from viam.utils import ValueTypes, create_filter, datetime_to_timestamp, struct_to_dict

LOGGER = logging.getLogger(__name__)


class DataClient:
    """gRPC client for uploading and retrieving data from app.

    Constructor is used by `ViamClient` to instantiate relevant service stubs. Calls to `DataClient` methods should be made through
    `ViamClient`.

    Establish a Connection::

        import asyncio

        from viam.rpc.dial import DialOptions, Credentials
        from viam.app.viam_client import ViamClient


        async def connect() -> ViamClient:
            # Replace "<API-KEY>" (including brackets) with your API key and "<API-KEY-ID>" with your API key ID
            dial_options = DialOptions.with_api_key("<API-KEY>", "<API-KEY-ID>")
            return await ViamClient.create_from_dial_options(dial_options)


        async def main():
            # Make a ViamClient
            viam_client = await connect()
            # Instantiate a DataClient to run data client API methods on
            data_client = viam_client.data_client

            viam_client.close()

        if __name__ == '__main__':
            asyncio.run(main())


    For more information, see `Data Client API <https://docs.viam.com/appendix/apis/data-client/>`_.
    """

    @dataclass
    class TabularData:
        """Class representing a piece of tabular data and associated metadata."""

        data: Mapping[str, Any]
        """The requested data"""

        metadata: CaptureMetadata
        """The metadata associated with the data"""

        time_requested: datetime
        """The time the data were requested"""

        time_received: datetime
        """The time the data were received"""

        def __str__(self) -> str:
            return f"{self.data}\n{self.metadata}Time requested: {self.time_requested}\nTime received: {self.time_received}\n"

        def __eq__(self, other: object) -> bool:
            if isinstance(other, DataClient.TabularData):
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
        self._dataset_client = DatasetServiceStub(channel)
        self._channel = channel

    _data_client: DataServiceStub
    _data_sync_client: DataSyncServiceStub
    _dataset_client: DatasetServiceStub
    _metadata: Mapping[str, str]
    _channel: Channel

    async def tabular_data_by_filter(
        self,
        filter: Optional[Filter] = None,
        limit: Optional[int] = None,
        sort_order: Optional[Order.ValueType] = None,
        last: Optional[str] = None,
        count_only: bool = False,
        include_internal_data: bool = False,
        dest: Optional[str] = None,
    ) -> Tuple[List[TabularData], int, str]:
        """Filter and download tabular data. The data will be paginated into pages of `limit` items, and the pagination ID will be included
        in the returned tuple. If a destination is provided, the data will be saved to that file.
        If the file is not empty, it will be overwritten.

        ::

            from viam.utils import create_filter

            my_data = []
            last = None
            my_filter = create_filter(component_name="left_motor")
            while True:
                tabular_data, count, last = await data_client.tabular_data_by_filter(my_filter, last)
                if not tabular_data:
                    break
                my_data.extend(tabular_data)


        Args:
            filter (viam.proto.app.data.Filter): Optional `Filter` specifying tabular data to retrieve. No `Filter` implies all tabular
                data.
            limit (int): The maximum number of entries to include in a page. Defaults to 50 if unspecified.
            sort_order (viam.proto.app.data.Order): The desired sort order of the data.
            last (str): Optional string indicating the object identifier of the last-returned data.
                        This object identifier is returned by calls to `TabularDataByFilter` as the `last` value.
                        If provided, the server will return the next data entries after the last object identifier.
            count_only (bool): Whether to return only the total count of entries.
            include_internal_data (bool): Whether to return the internal data. Internal data is used for Viam-specific data ingestion,
                                          like cloud SLAM. Defaults to `False`.
            dest (str): Optional filepath for writing retrieved data.

        Returns:
            Tuple[List[TabularData], int, str]: A tuple containing the following:
            List[TabularData]: The tabular data,
            int: The count (number of entries),
            str: The last-returned page ID.

        For more information, see `Data Client API <https://docs.viam.com/appendix/apis/data-client/>`_.
        """
        filter = filter if filter else Filter()

        data_request = DataRequest(filter=filter)
        if limit:
            data_request.limit = limit
        if sort_order:
            data_request.sort_order = sort_order
        if last:
            data_request.last = last
        request = TabularDataByFilterRequest(data_request=data_request, count_only=count_only, include_internal_data=include_internal_data)
        response: TabularDataByFilterResponse = await self._data_client.TabularDataByFilter(request, metadata=self._metadata)
        data = [
            DataClient.TabularData(
                struct_to_dict(struct.data),
                response.metadata[struct.metadata_index],
                struct.time_requested.ToDatetime(),
                struct.time_received.ToDatetime(),
            )
            for struct in response.data
        ]

        if dest:
            try:
                file = open(dest, "w")
                file.write(f"{[str(d) for d in data]}")
                file.flush()
            except Exception as e:
                LOGGER.error(f"Failed to write tabular data to file {dest}", exc_info=e)
        return data, response.count, response.last

    async def tabular_data_by_sql(self, organization_id: str, sql_query: str) -> List[Dict[str, ValueTypes]]:
        """Obtain unified tabular data and metadata, queried with SQL.

        ::

            data = await data_client.tabular_data_by_sql(organization_id="<your-org-id>", sql_query="SELECT * FROM readings LIMIT 5")


        Args:
            organization_id (str): The ID of the organization that owns the data.
                You can obtain your organization ID from the Viam app's organization settings page.
            sql_query (str): The SQL query to run.

        Returns:
            List[Dict[str, ValueTypes]]: An array of data objects.

        For more information, see `Data Client API <https://docs.viam.com/appendix/apis/data-client/>`_.
        """
        request = TabularDataBySQLRequest(organization_id=organization_id, sql_query=sql_query)
        response: TabularDataBySQLResponse = await self._data_client.TabularDataBySQL(request, metadata=self._metadata)
        return [struct_to_dict(struct) for struct in response.data]

    async def tabular_data_by_mql(self, organization_id: str, mql_binary: List[bytes]) -> List[Dict[str, ValueTypes]]:
        """Obtain unified tabular data and metadata, queried with MQL.

        ::

            # using bson
            import bson
            tabular_data = await data_client.tabular_data_by_mql(org_id="<your-org-id>", mql_binary=[
                bson.dumps({ '$match': { 'location_id': '<location-id>' } }),
                bson.dumps({ "$limit": 5 })
            ])

            # using pymongo
            import bson
            tabular_data = await data_client.tabular_data_by_mql(org_id="<your-org-id>", mql_binary=[
                bson.encode({ '$match': { 'location_id': '<location-id>' } }),
                bson.encode({ "$limit": 5 })
            ])


        Args:
            organization_id (str): The ID of the organization that owns the data.
                You can obtain your organization ID from the Viam app's organization settings page.
            mql_binary (List[bytes]): The MQL query to run as a list of BSON queries. You can encode your bson queries using a library like
                `pymongo` or `bson`.

        Returns:
            List[Dict[str, ValueTypes]]: An array of data objects.

        For more information, see `Data Client API <https://docs.viam.com/appendix/apis/data-client/>`_.
        """
        request = TabularDataByMQLRequest(organization_id=organization_id, mql_binary=mql_binary)
        response: TabularDataByMQLResponse = await self._data_client.TabularDataByMQL(request, metadata=self._metadata)
        return [struct_to_dict(struct) for struct in response.data]

    async def binary_data_by_filter(
        self,
        filter: Optional[Filter] = None,
        limit: Optional[int] = None,
        sort_order: Optional[Order.ValueType] = None,
        last: Optional[str] = None,
        include_binary_data: bool = True,
        count_only: bool = False,
        include_internal_data: bool = False,
        dest: Optional[str] = None,
    ) -> Tuple[List[BinaryData], int, str]:
        """Filter and download binary data. The data will be paginated into pages of `limit` items, and the pagination ID will be included
        in the returned tuple. If a destination is provided, the data will be saved to that file.
        If the file is not empty, it will be overwritten.

        ::

            from viam.utils import create_filter
            from viam.proto.app.data import Filter, TagsFilter, TagsFilterType


            # Get data captured from camera components
            my_data = []
            last = None
            my_filter = create_filter(component_name="camera")
            while True:
                data, count, last = await data_client.binary_data_by_filter(my_filter, last)
                if not data:
                    break
                my_data.extend(data)

            # Get untagged data from a dataset

            my_untagged_data = []
            last = None
            tags_filter = TagsFilter(type=TagsFilterType.TAGS_FILTER_TYPE_UNTAGGED)
            my_filter = Filter(
                dataset_id="66db6fe7d93d1ade24cd1dc3",
                tags_filter=tags_filter
            )

            while True:
                data, count, last = await data_client.binary_data_by_filter(
                    my_filter, last=last, include_binary_data=False)
                if not data:
                    break
                my_untagged_data.extend(data)

        Args:
            filter (viam.proto.app.data.Filter): Optional `Filter` specifying tabular data to retrieve. No `Filter` implies all binary
                data.
            limit (int): The maximum number of entries to include in a page. Defaults to 50 if unspecified.
            sort_order (viam.proto.app.data.Order): The desired sort order of the data.
            last (str): Optional string indicating the object identifier of the last-returned data.
                        This object identifier is returned by calls to `BinaryDataByFilter` as the `last` value.
                        If provided, the server will return the next data entries after the last object identifier.
            include_binary_data (bool): Boolean specifying whether to actually include the binary file data with each retrieved file.
                                        Defaults to true (that is, both the files' data and metadata are returned).
            count_only (bool): Whether to return only the total count of entries.
            include_internal_data (bool): Whether to return the internal data. Internal data is used for Viam-specific data ingestion,
                                          like cloud SLAM. Defaults to `False`.
            dest (str): Optional filepath for writing retrieved data.

        Returns:
            Tuple[List[viam.proto.app.data.BinaryData], int, str]: A tuple containing the following:
            List[viam.proto.app.data.BinaryData]: The binary data,
            int: The count (number of entries),
            str: The last-returned page ID.

        For more information, see `Data Client API <https://docs.viam.com/appendix/apis/data-client/>`_.
        """

        data_request = DataRequest(filter=filter)
        if limit:
            data_request.limit = limit
        if sort_order:
            data_request.sort_order = sort_order
        if last:
            data_request.last = last
        request = BinaryDataByFilterRequest(
            data_request=data_request,
            include_binary=include_binary_data,
            count_only=count_only,
            include_internal_data=include_internal_data,
        )
        response: BinaryDataByFilterResponse = await self._data_client.BinaryDataByFilter(request, metadata=self._metadata)
        data = list(response.data)
        if dest:
            try:
                file = open(dest, "w")
                file.write(f"{[str(d) for d in data]}")
                file.flush()
            except Exception as e:
                LOGGER.error(f"Failed to write binary data to file {dest}", exc_info=e)

        return data, response.count, response.last

    async def binary_data_by_ids(
        self,
        binary_ids: List[BinaryID],
        dest: Optional[str] = None,
    ) -> List[BinaryData]:
        """Filter and download binary data.

        ::

            from viam.proto.app.data import BinaryID

            binary_metadata, _, _ = await data_client.binary_data_by_filter(
                include_binary_data=False
            )

            my_ids = []

            for obj in binary_metadata:
                my_ids.append(
                    BinaryID(
                        file_id=obj.metadata.id,
                        organization_id=obj.metadata.capture_metadata.organization_id,
                        location_id=obj.metadata.capture_metadata.location_id
                    )
                )

            binary_data = await data_client.binary_data_by_ids(my_ids)

        Args:
            binary_ids (List[viam.proto.app.data.BinaryID]): `BinaryID` objects specifying the desired data. Must be non-empty.
            dest (str): Optional filepath for writing retrieved data.

        Raises:
            GRPCError: If no `BinaryID` objects are provided.

        Returns:
            List[viam.proto.app.data.BinaryData]: The binary data.

        For more information, see `Data Client API <https://docs.viam.com/appendix/apis/data-client/>`_.
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
        return list(response.data)

    async def delete_tabular_data(self, organization_id: str, delete_older_than_days: int) -> int:
        """Delete tabular data older than a specified number of days.

        ::

            from viam.utils import create_filter

            my_filter = create_filter(component_name="left_motor")
            days_of_data_to_delete = 10
            tabular_data = await data_client.delete_tabular_data(
                org_id="a12b3c4e-1234-1abc-ab1c-ab1c2d345abc", days_of_data_to_delete)

        Args:
            organization_id (str): ID of organization to delete data from.
                You can obtain your organization ID from the Viam app's organization settings page.
            delete_older_than_days (int): Delete data that was captured up to this many days ago. For example if `delete_older_than_days`
                is 10, this deletes any data that was captured up to 10 days ago. If it is 0, all existing data is deleted.

        Returns:
            int: The number of items deleted.

        For more information, see `Data Client API <https://docs.viam.com/appendix/apis/data-client/>`_.
        """
        request = DeleteTabularDataRequest(organization_id=organization_id, delete_older_than_days=delete_older_than_days)
        response: DeleteTabularDataResponse = await self._data_client.DeleteTabularData(request, metadata=self._metadata)
        return response.deleted_count

    async def delete_tabular_data_by_filter(self, filter: Optional[Filter]) -> int:
        """Deprecated: use delete_tabular_data instead."""
        raise NotImplementedError()

    async def delete_binary_data_by_filter(self, filter: Optional[Filter]) -> int:
        """Filter and delete binary data.

        ::

            from viam.utils import create_filter

            my_filter = create_filter(component_name="left_motor")
            res = await data_client.delete_binary_data_by_filter(my_filter)

        Args:
            filter (viam.proto.app.data.Filter): Optional `Filter` specifying binary data to delete. Passing an empty `Filter` will lead to
                all data being deleted. Exercise caution when using this option.

        Returns:
            int: The number of items deleted.

        For more information, see `Data Client API <https://docs.viam.com/appendix/apis/data-client/>`_.
        """
        filter = filter if filter else Filter()
        request = DeleteBinaryDataByFilterRequest(filter=filter)
        response: DeleteBinaryDataByFilterResponse = await self._data_client.DeleteBinaryDataByFilter(request, metadata=self._metadata)
        return response.deleted_count

    async def delete_binary_data_by_ids(self, binary_ids: List[BinaryID]) -> int:
        """Filter and delete binary data.

        ::

            from viam.proto.app.data import BinaryID

            binary_metadata, _, _ = await data_client.binary_data_by_filter(
                include_binary_data=False
            )

            my_ids = []

            for obj in binary_metadata:
                my_ids.append(
                    BinaryID(
                        file_id=obj.metadata.id,
                        organization_id=obj.metadata.capture_metadata.organization_id,
                        location_id=obj.metadata.capture_metadata.location_id
                    )
                )

            binary_data = await data_client.delete_binary_data_by_ids(my_ids)

        Args:
            binary_ids (List[viam.proto.app.data.BinaryID]): `BinaryID` objects specifying the data to be deleted. Must be non-empty.

        Raises:
            GRPCError: If no `BinaryID` objects are provided.

        Returns:
            int: The number of items deleted.

        For more information, see `Data Client API <https://docs.viam.com/appendix/apis/data-client/>`_.
        """
        request = DeleteBinaryDataByIDsRequest(binary_ids=binary_ids)
        response: DeleteBinaryDataByIDsResponse = await self._data_client.DeleteBinaryDataByIDs(request, metadata=self._metadata)
        return response.deleted_count

    async def add_tags_to_binary_data_by_ids(self, tags: List[str], binary_ids: List[BinaryID]) -> None:
        """Add tags to binary data.

        ::

            from viam.proto.app.data import BinaryID

            tags = ["tag1", "tag2"]

            binary_metadata, _, _ = await data_client.binary_data_by_filter(
                include_binary_data=False
            )

            my_ids = []

            for obj in binary_metadata:
                my_ids.append(
                    BinaryID(
                        file_id=obj.metadata.id,
                        organization_id=obj.metadata.capture_metadata.organization_id,
                        location_id=obj.metadata.capture_metadata.location_id
                    )
                )

            binary_data = await data_client.add_tags_to_binary_data_by_ids(tags, my_ids)

        Args:
            tags (List[str]): List of tags to add to specified binary data. Must be non-empty.
            binary_ids (List[viam.app.proto.BinaryID]): List of `BinaryID` objects specifying binary data to tag. Must be non-empty.

        Raises:
            GRPCError: If no `BinaryID` objects or tags are provided.

        For more information, see `Data Client API <https://docs.viam.com/appendix/apis/data-client/>`_.
        """
        request = AddTagsToBinaryDataByIDsRequest(binary_ids=binary_ids, tags=tags)
        await self._data_client.AddTagsToBinaryDataByIDs(request, metadata=self._metadata)

    async def add_tags_to_binary_data_by_filter(self, tags: List[str], filter: Optional[Filter] = None) -> None:
        """Add tags to binary data.

        ::

            from viam.utils import create_filter

            my_filter = create_filter(component_name="my_camera")
            tags = ["tag1", "tag2"]
            res = await data_client.add_tags_to_binary_data_by_filter(tags, my_filter)

        Args:
            tags (List[str]): List of tags to add to specified binary data. Must be non-empty.
            filter (viam.proto.app.data.Filter): `Filter` specifying binary data to tag. If no `Filter` is provided, all data will be
                tagged.

        Raises:
            GRPCError: If no tags are provided.

        For more information, see `Data Client API <https://docs.viam.com/appendix/apis/data-client/>`_.
        """
        filter = filter if filter else Filter()
        request = AddTagsToBinaryDataByFilterRequest(filter=filter, tags=tags)
        await self._data_client.AddTagsToBinaryDataByFilter(request, metadata=self._metadata)

    async def remove_tags_from_binary_data_by_ids(self, tags: List[str], binary_ids: List[BinaryID]) -> int:
        """Remove tags from binary data by IDs.

        ::

            from viam.proto.app.data import BinaryID

            tags = ["tag1", "tag2"]

            binary_metadata, _, _ = await data_client.binary_data_by_filter(
                include_binary_data=False
            )

            my_ids = []

            for obj in binary_metadata:
                my_ids.append(
                    BinaryID(
                        file_id=obj.metadata.id,
                        organization_id=obj.metadata.capture_metadata.organization_id,
                        location_id=obj.metadata.capture_metadata.location_id
                    )
                )

            binary_data = await data_client.remove_tags_from_binary_data_by_ids(
                tags, my_ids)

        Args:
            tags (List[str]): List of tags to remove from specified binary data. Must be non-empty.
            binary_ids (List[BinaryID]): List of `BinaryID` objects specifying binary data to untag. Must be non-empty.

        Raises:
            GRPCError: If no binary_ids or tags are provided.

        Returns:
            int: The number of tags removed.

        For more information, see `Data Client API <https://docs.viam.com/appendix/apis/data-client/>`_.
        """
        request = RemoveTagsFromBinaryDataByIDsRequest(binary_ids=binary_ids, tags=tags)
        response: RemoveTagsFromBinaryDataByIDsResponse = await self._data_client.RemoveTagsFromBinaryDataByIDs(
            request, metadata=self._metadata
        )
        return response.deleted_count

    async def remove_tags_from_binary_data_by_filter(self, tags: List[str], filter: Optional[Filter] = None) -> int:
        """Remove tags from binary data.

        ::

            from viam.utils import create_filter

            my_filter = create_filter(component_name="my_camera")
            tags = ["tag1", "tag2"]
            res = await data_client.remove_tags_from_binary_data_by_filter(tags, my_filter)

        Args:
            tags (List[str]): List of tags to remove from specified binary data.
            filter (viam.proto.app.data.Filter): `Filter` specifying binary data to untag. If no `Filter` is provided, all data will be
                untagged.

        Raises:
            GRPCError: If no tags are provided.

        Returns:
            int: The number of tags removed.

        For more information, see `Data Client API <https://docs.viam.com/appendix/apis/data-client/>`_.
        """
        filter = filter if filter else Filter()
        request = RemoveTagsFromBinaryDataByFilterRequest(filter=filter, tags=tags)
        response: RemoveTagsFromBinaryDataByFilterResponse = await self._data_client.RemoveTagsFromBinaryDataByFilter(
            request, metadata=self._metadata
        )
        return response.deleted_count

    async def tags_by_filter(self, filter: Optional[Filter] = None) -> List[str]:
        """Get a list of tags using a filter.

        ::

            from viam.utils import create_filter

            my_filter = create_filter(component_name="my_camera")
            tags = await data_client.tags_by_filter(my_filter)

        Args:
            filter (viam.proto.app.data.Filter): `Filter` specifying data to retrieve from. If no `Filter` is provided, all data tags will
                return.

        Returns:
            List[str]: The list of tags.

        For more information, see `Data Client API <https://docs.viam.com/appendix/apis/data-client/>`_.
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

        ::

            from viam.proto.app.data import BinaryID

            MY_BINARY_ID = BinaryID(
                file_id=your-file_id,
                organization_id=your-org-id,
                location_id=your-location-id
            )

            bbox_label = await data_client.add_bounding_box_to_image_by_id(
                binary_id=MY_BINARY_ID,
                label="label",
                x_min_normalized=0,
                y_min_normalized=.1,
                x_max_normalized=.2,
                y_max_normalized=.3
            )

            print(bbox_label)

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
            str: The bounding box ID.

        For more information, see `Data Client API <https://docs.viam.com/appendix/apis/data-client/>`_.
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

        ::

            from viam.proto.app.data import BinaryID

            MY_BINARY_ID = BinaryID(
                file_id=your-file_id,
                organization_id=your-org-id,
                location_id=your-location-id
            )

            await data_client.remove_bounding_box_from_image_by_id(
            binary_id=MY_BINARY_ID,
            bbox_id="your-bounding-box-id-to-delete"
            )

        Args:
            bbox_id (str): The ID of the bounding box to remove.
            binary_id (viam.proto.arr.data.BinaryID): Binary ID of the image to remove the bounding box from.

        For more information, see `Data Client API <https://docs.viam.com/appendix/apis/data-client/>`_.
        """
        request = RemoveBoundingBoxFromImageByIDRequest(bbox_id=bbox_id, binary_id=binary_id)
        await self._data_client.RemoveBoundingBoxFromImageByID(request, metadata=self._metadata)

    async def bounding_box_labels_by_filter(self, filter: Optional[Filter] = None) -> List[str]:
        """Get a list of bounding box labels using a `Filter`.

        ::

            from viam.utils import create_filter

            my_filter = create_filter(component_name="my_camera")
            bounding_box_labels = await data_client.bounding_box_labels_by_filter(
                my_filter)

        Args:
            filter (viam.proto.app.data.Filter): `Filter` specifying data to retrieve from. If no `Filter` is provided, all labels will
                return.

        Returns:
            List[str]: The list of bounding box labels.

        For more information, see `Data Client API <https://docs.viam.com/appendix/apis/data-client/>`_.
        """
        filter = filter if filter else Filter()
        request = BoundingBoxLabelsByFilterRequest(filter=filter)
        response: BoundingBoxLabelsByFilterResponse = await self._data_client.BoundingBoxLabelsByFilter(request, metadata=self._metadata)
        return list(response.labels)

    async def get_database_connection(self, organization_id: str) -> str:
        """Get a connection to access a MongoDB Atlas Data federation instance.

        ::

            data_client.get_database_connection(org_id="a12b3c4e-1234-1abc-ab1c-ab1c2d345abc")

        Args:
            organization_id (str): Organization to retrieve the connection for.
                You can obtain your organization ID from the Viam app's organization settings page.

        Returns:
            str: The hostname of the federated database.

        For more information, see `Data Client API <https://docs.viam.com/appendix/apis/data-client/>`_.
        """
        request = GetDatabaseConnectionRequest(organization_id=organization_id)
        response: GetDatabaseConnectionResponse = await self._data_client.GetDatabaseConnection(request, metadata=self._metadata)
        return response.hostname

    async def configure_database_user(self, organization_id: str, password: str) -> None:
        """Configure a database user for the Viam organization's MongoDB Atlas Data Federation instance. It can also be used to reset the
        password of the existing database user.

        ::

            await data_client.configure_database_user(
                organization_id="<your-org-id>",
                password="your_password"
            )

        Args:
            organization_id (str): The ID of the organization.
                You can obtain your organization ID from the Viam app's organization settings page.
            password (str): The password of the user.

        For more information, see `Data Client API <https://docs.viam.com/appendix/apis/data-client/>`_.
        """
        request = ConfigureDatabaseUserRequest(organization_id=organization_id, password=password)
        await self._data_client.ConfigureDatabaseUser(request, metadata=self._metadata)

    async def create_dataset(self, name: str, organization_id: str) -> str:
        """Create a new dataset.

        ::

            dataset_id = await data_client.create_dataset(
                name="<dataset-name>",
                organization_id="<your-org-id>"
            )
            print(dataset_id)

        Args:
            name (str): The name of the dataset being created.
            organization_id (str): The ID of the organization where the dataset is being created.
                You can obtain your organization ID from the Viam app's organization settings page.

        Returns:
            str: The dataset ID of the created dataset.

        For more information, see `Data Client API <https://docs.viam.com/appendix/apis/data-client/>`_.
        """
        request = CreateDatasetRequest(name=name, organization_id=organization_id)
        response: CreateDatasetResponse = await self._dataset_client.CreateDataset(request, metadata=self._metadata)
        return response.id

    async def list_dataset_by_ids(self, ids: List[str]) -> Sequence[Dataset]:
        """Get a list of datasets using their IDs.

        ::

            datasets = await data_client.list_dataset_by_ids(
                ids=["abcd-1234xyz-8765z-123abc"]
            )
            print(datasets)

        Args:
            ids (List[str]): The IDs of the datasets being called for. To retrieve these IDs,
                navigate to your dataset's page in the Viam app,
                click **...** in the left-hand menu, and click **Copy dataset ID**.

        Returns:
            Sequence[Dataset]: The list of datasets.

        For more information, see `Data Client API <https://docs.viam.com/appendix/apis/data-client/>`_.
        """
        request = ListDatasetsByIDsRequest(ids=ids)
        response: ListDatasetsByIDsResponse = await self._dataset_client.ListDatasetsByIDs(request, metadata=self._metadata)

        return response.datasets

    async def list_datasets_by_organization_id(self, organization_id: str) -> Sequence[Dataset]:
        """Get the datasets in an organization.

        ::

            datasets = await data_client.list_dataset_by_organization_id(
                organization_id=[""a12b3c4e-1234-1abc-ab1c-ab1c2d345abc""]
            )
            print(datasets)

        Args:
            organization_id (str): The ID of the organization.
                You can obtain your organization ID from the Viam app's organization settings page.

        Returns:
            Sequence[Dataset]: The list of datasets in the organization.

        For more information, see `Data Client API <https://docs.viam.com/appendix/apis/data-client/>`_.
        """
        request = ListDatasetsByOrganizationIDRequest(organization_id=organization_id)
        response: ListDatasetsByOrganizationIDResponse = await self._dataset_client.ListDatasetsByOrganizationID(
            request, metadata=self._metadata
        )

        return response.datasets

    async def rename_dataset(self, id: str, name: str) -> None:
        """Rename a dataset specified by the dataset ID.

        ::

            await data_client.rename_dataset(
                id="abcd-1234xyz-8765z-123abc",
                name="<dataset-name>"
            )

        Args:
            id (str): The ID of the dataset.
            name (str): The new name of the dataset.

        For more information, see `Data Client API <https://docs.viam.com/appendix/apis/data-client/>`_.
        """
        request = RenameDatasetRequest(id=id, name=name)
        await self._dataset_client.RenameDataset(request, metadata=self._metadata)

    async def delete_dataset(self, id: str) -> None:
        """Delete a dataset.

        ::

            await data_client.delete_dataset(
                id="abcd-1234xyz-8765z-123abc"
            )

        Args:
            id (str): The ID of the dataset.

        For more information, see `Data Client API <https://docs.viam.com/appendix/apis/data-client/>`_.
        """
        request = DeleteDatasetRequest(id=id)
        await self._dataset_client.DeleteDataset(request, metadata=self._metadata)

    async def add_binary_data_to_dataset_by_ids(self, binary_ids: List[BinaryID], dataset_id: str) -> None:
        """Add the BinaryData to the provided dataset.

        This BinaryData will be tagged with the VIAM_DATASET_{id} label.

        ::

            from viam.proto.app.data import BinaryID

            binary_metadata, _, _ = await data_client.binary_data_by_filter(
                include_binary_data=False
            )

            my_binary_ids = []

            for obj in binary_metadata:
                my_binary_ids.append(
                    BinaryID(
                        file_id=obj.metadata.id,
                        organization_id=obj.metadata.capture_metadata.organization_id,
                        location_id=obj.metadata.capture_metadata.location_id
                        )
                    )

            await data_client.add_binary_data_to_dataset_by_ids(
                binary_ids=my_binary_ids,
                dataset_id="abcd-1234xyz-8765z-123abc"
            )

        Args:
            binary_ids (List[BinaryID]): The IDs of binary data to add to dataset. To retrieve these IDs,
                navigate to your dataset's page in the Viam app,
                click **...** in the left-hand menu, and click **Copy dataset ID**.
            dataset_id (str): The ID of the dataset to be added to.

        For more information, see `Data Client API <https://docs.viam.com/appendix/apis/data-client/>`_.
        """
        request = AddBinaryDataToDatasetByIDsRequest(binary_ids=binary_ids, dataset_id=dataset_id)
        await self._data_client.AddBinaryDataToDatasetByIDs(request, metadata=self._metadata)

    async def remove_binary_data_from_dataset_by_ids(self, binary_ids: List[BinaryID], dataset_id: str) -> None:
        """Remove the BinaryData from the provided dataset.

        This BinaryData will lose the VIAM_DATASET_{id} tag.

        ::

            from viam.proto.app.data import BinaryID

            binary_metadata, _, _ = await data_client.binary_data_by_filter(
                include_binary_data=False
            )

            my_binary_ids = []

            for obj in binary_metadata:
                my_binary_ids.append(
                    BinaryID(
                        file_id=obj.metadata.id,
                        organization_id=obj.metadata.capture_metadata.organization_id,
                        location_id=obj.metadata.capture_metadata.location_id
                    )
                )

            await data_client.remove_binary_data_from_dataset_by_ids(
                binary_ids=my_binary_ids,
                dataset_id="abcd-1234xyz-8765z-123abc"
            )

        Args:
            binary_ids (List[BinaryID]): The IDs of binary data to remove from dataset. To retrieve these IDs,
                navigate to your dataset's page in the Viam app,
                click **...** in the left-hand menu, and click **Copy dataset ID**.
            dataset_id (str): The ID of the dataset to be removed from.

        For more information, see `Data Client API <https://docs.viam.com/appendix/apis/data-client/>`_.
        """
        request = RemoveBinaryDataFromDatasetByIDsRequest(binary_ids=binary_ids, dataset_id=dataset_id)
        await self._data_client.RemoveBinaryDataFromDatasetByIDs(request, metadata=self._metadata)

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

        Upload binary data collected on a robot through a specific component (for example, a motor) along with the relevant metadata to
        app.viam.com. Binary data can be found under the "Files" subtab of the Data tab on app.viam.com.

        ::

            time_requested = datetime(2023, 6, 5, 11)
            time_received = datetime(2023, 6, 5, 11, 0, 3)

            file_id = await data_client.binary_data_capture_upload(
                part_id="INSERT YOUR PART ID",
                component_type='camera',
                component_name='my_camera',
                method_name='GetImages',
                method_parameters=None,
                tags=["tag_1", "tag_2"],
                data_request_times=[time_requested, time_received],
                file_extension=".jpg",
                binary_data=b"Encoded image bytes"
            )

        Args:
            binary_data (bytes): The data to be uploaded, represented in bytes.
            part_id (str): Part ID of the component used to capture the data.
            component_type (str): Type of the component used to capture the data (for example, "movement_sensor").
            component_name (str): Name of the component used to capture the data.
            method_name (str): Name of the method used to capture the data.
            file_extension (str): The file extension of binary data including the period, for example .jpg, .png, .pcd.
                The backend will route the binary to its corresponding mime type based on this extension. Files with a .jpeg, .jpg,
                or .png extension will be saved to the images tab.
            method_parameters (Optional[Mapping[str, Any]]): Optional dictionary of method parameters. No longer in active use.
            tags (Optional[List[str]]): Optional list of tags to allow for tag-based data filtering when retrieving data.
            data_request_times (Optional[Tuple[datetime.datetime, datetime.datetime]]): Optional tuple containing datetime objects
                denoting the times this data was requested[0] by the robot and received[1] from the appropriate sensor.

        Raises:
            GRPCError: If an invalid part ID is passed.

        Returns:
            str: The file_id of the uploaded data.

        For more information, see `Data Client API <https://docs.viam.com/appendix/apis/data-client/>`_.
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
        data_request_times: List[Tuple[datetime, datetime]],
        method_parameters: Optional[Mapping[str, Any]] = None,
        tags: Optional[List[str]] = None,
    ) -> str:
        """Upload tabular sensor data.

        Upload tabular data collected on a robot through a specific component (for example, a motor) along with the relevant metadata to
        app.viam.com. Tabular data can be found under the "Sensors" subtab of the Data tab on app.viam.com.

        ::

            time_requested = datetime(2023, 6, 5, 11)
            time_received = datetime(2023, 6, 5, 11, 0, 3)

            file_id = await data_client.tabular_data_capture_upload(
                part_id="INSERT YOUR PART ID",
                component_type='rdk:component:motor',
                component_name='left_motor',
                method_name='IsPowered',
                tags=["tag_1", "tag_2"],
                data_request_times=[(time_requested, time_received)],
                tabular_data=[{'PowerPCT': 0, 'IsPowered': False}]
            )

        Args:
            tabular_data (List[Mapping[str, Any]]): List of the data to be uploaded, represented tabularly as a collection of dictionaries.
            part_id (str): Part ID of the component used to capture the data.
            component_type (str): Type of the component used to capture the data (for example, "rdk:component:movement_sensor").
            component_name (str): Name of the component used to capture the data.
            method_name (str): Name of the method used to capture the data.
            data_request_times (List[Tuple[datetime.datetime, datetime.datetime]]): List of tuples, each containing `datetime` objects
                denoting the times this data was requested[0] by the robot and received[1] from the appropriate sensor. Passing a list of
                tabular data and Timestamps with length n > 1 will result in n datapoints being uploaded, all tied to the same metadata.
            method_parameters (Optional[Mapping[str, Any]]): Optional dictionary of method parameters. No longer in active use.
            tags (Optional[List[str]]): Optional list of tags to allow for tag-based data filtering when retrieving data.

        Raises:
            GRPCError: If an invalid part ID is passed.
            ValueError: If a list of `Timestamp` objects is provided and its length does not match the length of the list of tabular
                data.

        Returns:
            str: The file_id of the uploaded data.

        For more information, see `Data Client API <https://docs.viam.com/appendix/apis/data-client/>`_.
        """
        sensor_contents = []
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

        ::

            time_requested = datetime(2023, 6, 5, 11)
            time_received = datetime(2023, 6, 5, 11, 0, 3)

            file_id = await data_client.streaming_data_capture_upload(
                data="byte-data-to-upload",
                part_id="INSERT YOUR PART ID",
                file_ext="png",
                component_type='motor',
                component_name='left_motor',
                method_name='IsPowered',
                data_request_times=[(time_requested, time_received)],
                tags=["tag_1", "tag_2"]
            )

        Args:
            data (bytes): the data to be uploaded.
            part_id (str): Part ID of the resource associated with the file.
            file_ext (str): file extension type for the data. required for determining MIME type.
            component_type (Optional[str]): Optional type of the component associated with the file (for example, "movement_sensor").
            component_name (Optional[str]): Optional name of the component associated with the file.
            method_name (Optional[str]): Optional name of the method associated with the file.
            method_parameters (Optional[str]): Optional dictionary of the method parameters. No longer in active use.
            data_request_times (Optional[Tuple[datetime.datetime, datetime.datetime]]): Optional tuple containing datetime objects
                denoting the times this data was requested[0] by the robot and received[1] from the appropriate sensor.
            tags (Optional[List[str]]): Optional list of tags to allow for tag-based filtering when retrieving data.

        Raises:
            GRPCError: If an invalid part ID is passed.

        Returns:
            str: The file_id of the uploaded data.

        For more information, see `Data Client API <https://docs.viam.com/appendix/apis/data-client/>`_.
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

        ::

            file_id = await data_client.file_upload(
                data=b"Encoded image bytes",
                part_id="INSERT YOUR PART ID",
                tags=["tag_1", "tag_2"],
                file_name="your-file",
                file_extension=".txt"
            )

        Args:
            part_id (str): Part ID of the resource associated with the file.
            data (bytes): Bytes representing file data to upload.
            component_type (Optional[str]): Optional type of the component associated with the file (for example, "movement_sensor").
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

        For more information, see `Data Client API <https://docs.viam.com/appendix/apis/data-client/>`_.
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

        ::

            file_id = await data_client.file_upload_from_path(
                part_id="INSERT YOUR PART ID",
                tags=["tag_1", "tag_2"],
                filepath="/Users/<your-username>/<your-directory>/<your-file.txt>"
            )

        Args:
            filepath (str): Absolute filepath of file to be uploaded.
            part_id (str): Part ID of the component associated with the file.
            component_type (Optional[str]): Optional type of the component associated with the file (for example, "movement_sensor").
            component_name (Optional[str]): Optional name of the component associated with the file.
            method_name (Optional[str]): Optional name of the method associated with the file.
            method_parameters (Optional[str]): Optional dictionary of the method parameters. No longer in active use.
            tags (Optional[List[str]]): Optional list of tags to allow for tag-based filtering when retrieving data.


        Raises:
            GRPCError: If an invalid part ID is passed.
            FileNotFoundError: If the provided filepath is not found.

        Returns:
            str: ID of the new file.

        For more information, see `Data Client API <https://docs.viam.com/appendix/apis/data-client/>`_.
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
        dataset_id: Optional[str] = None,
    ) -> Filter:
        warnings.warn("DataClient.create_filter is deprecated. Use utils.create_filter instead.", DeprecationWarning, stacklevel=2)
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
            dataset_id,
        )
