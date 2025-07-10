import warnings
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Mapping, Optional, Sequence, Tuple, Union, cast

import bson
from google.protobuf.struct_pb2 import Struct
from grpclib.client import Channel, Stream
from typing_extensions import Self

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
    CaptureInterval,
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
    ExportTabularDataRequest,
    ExportTabularDataResponse,
    Filter,
    GetDatabaseConnectionRequest,
    GetDatabaseConnectionResponse,
    GetLatestTabularDataRequest,
    GetLatestTabularDataResponse,
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
    TabularDataSource,
    TabularDataSourceType,
    TagsByFilterRequest,
    TagsByFilterResponse,
)
from viam.proto.app.datapipelines import (
    CreateDataPipelineRequest,
    CreateDataPipelineResponse,
    DataPipelineRunStatus,
    DataPipelinesServiceStub,
    DeleteDataPipelineRequest,
    GetDataPipelineRequest,
    GetDataPipelineResponse,
    ListDataPipelineRunsRequest,
    ListDataPipelineRunsResponse,
    ListDataPipelinesRequest,
    ListDataPipelinesResponse,
)
from viam.proto.app.datapipelines import (
    DataPipeline as ProtoDataPipeline,
)
from viam.proto.app.datapipelines import (
    DataPipelineRun as ProtoDataPipelineRun,
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
from viam.utils import ValueTypes, _alias_param, create_filter, datetime_to_timestamp, dict_to_struct, struct_to_dict

LOGGER = logging.getLogger(__name__)


class DataClient:
    """gRPC client for uploading and retrieving data from app.

    This class's constructor instantiates relevant service stubs. Always make :class:`DataClient` method calls through an instance of
    :class:`ViamClient`.

    Establish a connection::

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


    For more information, see `Data Client API <https://docs.viam.com/dev/reference/apis/data-client/>`_.
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

    @dataclass
    class TabularDataPoint:
        """Represents a tabular data point and its associated metadata."""

        part_id: str
        """The robot part ID"""

        resource_name: str
        """The resource name"""

        resource_api: str
        """The resource API. For example, rdk:component:sensor"""

        method_name: str
        """The method used for data capture. For example, Readings"""

        time_captured: datetime
        """The time at which the data point was captured"""

        organization_id: str
        """The organization ID"""

        location_id: str
        """The location ID"""

        robot_name: str
        """The robot name"""

        robot_id: str
        """The robot ID"""

        part_name: str
        """The robot part name"""

        method_parameters: Mapping[str, ValueTypes]
        """Additional parameters associated with the data capture method"""

        tags: List[str]
        """A list of tags associated with the data point"""

        payload: Mapping[str, ValueTypes]
        """The captured data"""

        def __str__(self) -> str:
            return (
                f"TabularDataPoint("
                f"robot='{self.robot_name}' (id={self.robot_id}), "
                f"part='{self.part_name}' (id={self.part_id}), "
                f"resource='{self.resource_name}' ({self.resource_api}), "
                f"method='{self.method_name}', "
                f"org={self.organization_id}, "
                f"location={self.location_id}, "
                f"time='{self.time_captured.isoformat()}', "
                f"params={self.method_parameters}, "
                f"tags={self.tags}, "
                f"payload={self.payload})"
            )

        def __eq__(self, other: object) -> bool:
            if isinstance(other, DataClient.TabularDataPoint):
                return str(self) == str(other)
            return False

        @property
        def resource_subtype(self) -> str:
            warnings.warn(
                "`TabularDataPoint.resource_subtype` is deprecated. Use `TabularDataPoint.resource_api` instead.",
                DeprecationWarning,
                stacklevel=2,
            )
            return self.resource_api

    @dataclass
    class DataPipeline:
        """Represents a data pipeline and its associated metadata."""

        id: str
        """The ID of the data pipeline"""

        organization_id: str
        """The organization ID"""

        name: str
        """The name of the data pipeline"""

        mql_binary: List[Dict[str, Any]]
        """The MQL binary of the data pipeline"""

        schedule: str
        """The schedule of the data pipeline"""

        created_on: datetime
        """The time the data pipeline was created"""

        updated_at: datetime
        """The time the data pipeline was last updated"""

        enabled: bool
        """Whether the data pipeline is enabled"""

        data_source_type: TabularDataSourceType.ValueType
        """The type of data source for the data pipeline"""

        @classmethod
        def from_proto(cls, data_pipeline: ProtoDataPipeline) -> Self:
            return cls(
                id=data_pipeline.id,
                organization_id=data_pipeline.organization_id,
                name=data_pipeline.name,
                mql_binary=[bson.decode(bson_bytes) for bson_bytes in data_pipeline.mql_binary],
                schedule=data_pipeline.schedule,
                created_on=data_pipeline.created_on.ToDatetime(),
                updated_at=data_pipeline.updated_at.ToDatetime(),
                enabled=data_pipeline.enabled,
                data_source_type=data_pipeline.data_source_type,
            )

    @dataclass
    class DataPipelineRun:
        """Represents a data pipeline run and its associated metadata."""

        id: str
        """The ID of the data pipeline run"""

        status: DataPipelineRunStatus.ValueType
        """The status of the data pipeline run"""

        start_time: datetime
        """The time the data pipeline run started"""

        end_time: datetime
        """The time the data pipeline run ended"""

        data_start_time: datetime
        """The start time of the data that was processed in the run."""
        data_end_time: datetime
        """The end time of the data that was processed in the run."""

        @classmethod
        def from_proto(cls, data_pipeline_run: ProtoDataPipelineRun) -> Self:
            return cls(
                id=data_pipeline_run.id,
                status=data_pipeline_run.status,
                start_time=data_pipeline_run.start_time.ToDatetime(),
                end_time=data_pipeline_run.end_time.ToDatetime(),
                data_start_time=data_pipeline_run.data_start_time.ToDatetime(),
                data_end_time=data_pipeline_run.data_end_time.ToDatetime(),
            )

    @dataclass
    class DataPipelineRunsPage:
        """Represents a page of data pipeline runs and provides pagination functionality."""

        _client: "DataClient"
        """The data client used to make API calls"""

        pipeline_id: str
        """The ID of the pipeline these runs belong to"""

        page_size: int
        """The number of runs per page"""

        runs: List["DataClient.DataPipelineRun"]
        """The list of runs in this page"""

        next_page_token: str
        """The token to use to get the next page of results"""

        async def next_page(self) -> "DataClient.DataPipelineRunsPage":
            """Get the next page of data pipeline runs.

            Returns:
                DataPipelineRunsPage: The next page of runs, or an empty page if there are no more runs
            """
            if not self.next_page_token:
                # no token, return empty next page
                return DataClient.DataPipelineRunsPage(
                    _client=self._client, pipeline_id=self.pipeline_id, page_size=self.page_size, runs=[], next_page_token=""
                )
            return await self._client._list_data_pipeline_runs(self.pipeline_id, self.page_size, self.next_page_token)

        @classmethod
        def from_proto(cls, data_pipeline_runs_page: ListDataPipelineRunsResponse, client: "DataClient", page_size: int) -> Self:
            return cls(
                _client=client,
                pipeline_id=data_pipeline_runs_page.pipeline_id,
                page_size=page_size,
                runs=[DataClient.DataPipelineRun.from_proto(run) for run in data_pipeline_runs_page.runs],
                next_page_token=data_pipeline_runs_page.next_page_token,
            )

    def __init__(self, channel: Channel, metadata: Mapping[str, str]):
        """Create a :class:`DataClient` that maintains a connection to app.

        Args:
            channel (grpclib.client.Channel): Connection to app.
            metadata (Mapping[str, str]): Required authorization token to send requests to app.
        """
        self._metadata = metadata
        self._data_client = DataServiceStub(channel)
        self._data_sync_client = DataSyncServiceStub(channel)
        self._dataset_client = DatasetServiceStub(channel)
        self._data_pipelines_client = DataPipelinesServiceStub(channel)
        self._channel = channel

    _data_client: DataServiceStub
    _data_sync_client: DataSyncServiceStub
    _dataset_client: DatasetServiceStub
    _data_pipelines_client: DataPipelinesServiceStub
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
        """Filter and download tabular data. The data will be paginated into pages of ``limit`` items; the returned tuple will include
        the pagination ID. If a destination is provided, this method saves returned data to that file, overwriting any existing file content.

        ::

            from viam.utils import create_filter

            my_data = []
            my_filter = create_filter(component_name="motor-1")
            last = None
            while True:
                tabular_data, count, last = await data_client.tabular_data_by_filter(my_filter, last=last)
                if not tabular_data:
                    break
                my_data.extend(tabular_data)

            print(f"My data: {my_data}")

        Args:
            filter (~viam.proto.app.data.Filter): Optional, specifies tabular data to retrieve. If missing, matches all tabular data.
            limit (int): The maximum number of entries to include in a page. Defaults to 50 if unspecified.
            sort_order (~viam.proto.app.data.Order): The desired sort order of the data.
            last (str): Optional string indicating the object identifier of the last-returned data.
                Returned by calls to :class:`TabularDataByFilter` as the ``last`` value.
                If provided, the server returns the next data entries after the last object identifier.
            count_only (bool): Whether to return only the total count of entries.
            include_internal_data (bool): Whether to return the internal data. Internal data is used for Viam-specific data ingestion,
                like cloud SLAM. Defaults to ``False``.
            dest (str): Optional filepath for writing retrieved data.

        Returns:
            Tuple[List[TabularData], int, str]: A tuple containing the following:

                - ``tabular_data`` (*List[TabularData]*): The tabular data.
                - ``count`` (*int*): The count (number of entries).
                - ``last`` (*str*): The last-returned page ID.

        For more information, see `Data Client API <https://docs.viam.com/dev/reference/apis/data-client/#tabulardatabyfilter>`_.
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

    async def tabular_data_by_sql(self, organization_id: str, sql_query: str) -> List[Dict[str, Union[ValueTypes, datetime]]]:
        """Obtain unified tabular data and metadata, queried with SQL.
        Make sure your API key has permissions at the organization level in order to use this.

        ::

            data = await data_client.tabular_data_by_sql(
                organization_id="<YOUR-ORG-ID>",
                sql_query="SELECT * FROM readings LIMIT 5"
            )

        Args:
            organization_id (str): The ID of the organization that owns the data.
                To find your organization ID, visit the organization settings page.
            sql_query (str): The SQL query to run.

        Returns:
            List[Dict[str, Union[ValueTypes, datetime]]]: An array of decoded BSON data objects.

        For more information, see `Data Client API <https://docs.viam.com/dev/reference/apis/data-client/#tabulardatabysql>`_.
        """
        request = TabularDataBySQLRequest(organization_id=organization_id, sql_query=sql_query)
        response: TabularDataBySQLResponse = await self._data_client.TabularDataBySQL(request, metadata=self._metadata)
        return [bson.decode(bson_bytes) for bson_bytes in response.raw_data]

    @_alias_param("query", param_alias="mql_binary")
    async def tabular_data_by_mql(
        self,
        organization_id: str,
        query: Union[List[bytes], List[Dict[str, Any]]],
        use_recent_data: Optional[bool] = None,
        tabular_data_source_type: TabularDataSourceType.ValueType = TabularDataSourceType.TABULAR_DATA_SOURCE_TYPE_STANDARD,
        pipeline_id: Optional[str] = None,
    ) -> List[Dict[str, Union[ValueTypes, datetime]]]:
        """Obtain unified tabular data and metadata, queried with MQL.

        ::

            import bson

            tabular_data = await data_client.tabular_data_by_mql(organization_id="<YOUR-ORG-ID>", query=[
                { '$match': { 'location_id': '<YOUR-LOCATION-ID>' } },
                { "$limit": 5 }
            ])

            print(f"Tabular Data: {tabular_data}")

        Args:
            organization_id (str): The ID of the organization that owns the data.
                To find your organization ID, visit the organization settings page.
            query (Union[List[bytes], List[Dict[str, Any]]]): The MQL query to run, as a list of MongoDB aggregation pipeline stages.
                Each stage can be provided as either a dictionary or raw BSON bytes, but support for bytes will be removed in the
                future, so prefer the dictionary option.
            use_recent_data (bool): Whether to query blob storage or your recent data store. Defaults to ``False``..
                Deprecated, use `tabular_data_source_type` instead.
            tabular_data_source_type (viam.proto.app.data.TabularDataSourceType): The data source to query.
                Defaults to `TABULAR_DATA_SOURCE_TYPE_STANDARD`.
            pipeline_id (str): The ID of the data pipeline to query. Defaults to `None`.
                Required if `tabular_data_source_type` is `TABULAR_DATA_SOURCE_TYPE_PIPELINE_SINK`.

        Returns:
            List[Dict[str, Union[ValueTypes, datetime]]]: An array of decoded BSON data objects.

        For more information, see `Data Client API <https://docs.viam.com/dev/reference/apis/data-client/#tabulardatabymql>`_.
        """
        binary: List[bytes] = [bson.encode(query) for query in query] if isinstance(query[0], dict) else query  # type: ignore
        data_source = TabularDataSource(type=tabular_data_source_type, pipeline_id=pipeline_id)
        if use_recent_data:
            data_source.type = TabularDataSourceType.TABULAR_DATA_SOURCE_TYPE_HOT_STORAGE
        request = TabularDataByMQLRequest(organization_id=organization_id, mql_binary=binary, data_source=data_source)
        response: TabularDataByMQLResponse = await self._data_client.TabularDataByMQL(request, metadata=self._metadata)
        return [bson.decode(bson_bytes) for bson_bytes in response.raw_data]

    @_alias_param("resource_api", param_alias="resource_subtype")
    async def get_latest_tabular_data(
        self,
        part_id: str,
        resource_name: str,
        resource_api: str,
        method_name: str,
        additional_params: Optional[Mapping[str, ValueTypes]] = None,
    ) -> Optional[Tuple[datetime, datetime, Dict[str, ValueTypes]]]:
        """Gets the most recent tabular data captured from the specified data source, as long as it was synced within the last year.

        ::

            tabular_data = await data_client.get_latest_tabular_data(
                part_id="77ae3145-7b91-123a-a234-e567cdca8910",
                resource_name="camera-1",
                resource_api="rdk:component:camera",
                method_name="GetImage",
                additional_params={"docommand_input": {"test": "test"}}
            )

            if tabular_data:
                time_captured, time_synced, payload = tabular_data
                print(f"Time Captured: {time_captured}")
                print(f"Time Synced: {time_synced}")
                print(f"Payload: {payload}")
            else:
                print(f"No data returned: {tabular_data}")

        Args:
            part_id (str): The ID of the part that owns the data.
            resource_name (str): The name of the requested resource that captured the data. For example, "my-sensor".
            resource_api (str): The API of the requested resource that captured the data. For example, "rdk:component:sensor".
            method_name (str): The data capture method name. For exampe, "Readings".
            additional_params (dict): Optional additional parameters of the resource that captured the data.

        Returns:
            Optional[Tuple[datetime, datetime, Dict[str, ValueTypes]]]:
            A return value of ``None`` means that this data source
            has not synced data in the last year. Otherwise, the data source has synced some data in the last year, so the returned
            tuple contains the following:

                - ``time_captured`` (*datetime*): The time captured.
                - ``time_synced`` (*datetime*): The time synced.
                - ``payload`` (*Dict[str, ValueTypes]*): The latest tabular data captured from the specified data source.

        For more information, see `Data Client API <https://docs.viam.com/dev/reference/apis/data-client/#getlatesttabulardata>`_.
        """

        request = GetLatestTabularDataRequest(
            part_id=part_id,
            resource_name=resource_name,
            resource_subtype=resource_api,
            method_name=method_name,
            additional_parameters=dict_to_struct(additional_params),
        )
        response: GetLatestTabularDataResponse = await self._data_client.GetLatestTabularData(request, metadata=self._metadata)
        if not response.payload:
            return None
        return response.time_captured.ToDatetime(), response.time_synced.ToDatetime(), struct_to_dict(response.payload)

    @_alias_param("resource_api", param_alias="resource_subtype")
    async def export_tabular_data(
        self,
        part_id: str,
        resource_name: str,
        resource_api: str,
        method_name: str,
        start_time: Optional[datetime] = None,
        end_time: Optional[datetime] = None,
        additional_params: Optional[Mapping[str, ValueTypes]] = None,
    ) -> List[TabularDataPoint]:
        """Obtain unified tabular data and metadata from the specified data source.

        ::

            tabular_data = await data_client.export_tabular_data(
                part_id="<PART-ID>",
                resource_name="<RESOURCE-NAME>",
                resource_api="<RESOURCE-API>",
                method_name="<METHOD-NAME>",
                start_time="<START_TIME>"
                end_time="<END_TIME>"
                additional_params="<ADDITIONAL_PARAMETERS>"
            )

            print(f"My data: {tabular_data}")

        Args:
            part_id (str): The ID of the part that owns the data.
            resource_name (str): The name of the requested resource that captured the data.
            resource_api (str): The API of the requested resource that captured the data.
            method_name (str): The data capture method name.
            start_time (datetime): Optional start time for requesting a specific range of data.
            end_time (datetime): Optional end time for requesting a specific range of data.
            additional_params (dict): Optional additional parameters of the resource that captured the data.

        Returns:
            List[TabularDataPoint]: The unified tabular data and metadata.

        For more information, see `Data Client API <https://docs.viam.com/dev/reference/apis/data-client/#exporttabulardata>`_.
        """

        interval = CaptureInterval(start=datetime_to_timestamp(start_time), end=datetime_to_timestamp(end_time))
        request = ExportTabularDataRequest(
            part_id=part_id,
            resource_name=resource_name,
            resource_subtype=resource_api,
            method_name=method_name,
            interval=interval,
            additional_parameters=dict_to_struct(additional_params),
        )
        response: List[ExportTabularDataResponse] = await self._data_client.ExportTabularData(request, metadata=self._metadata)

        return [
            DataClient.TabularDataPoint(
                part_id=resp.part_id,
                resource_name=resp.resource_name,
                resource_api=resp.resource_subtype,
                method_name=resp.method_name,
                time_captured=resp.time_captured.ToDatetime(),
                organization_id=resp.organization_id,
                location_id=resp.location_id,
                robot_name=resp.robot_name,
                robot_id=resp.robot_id,
                part_name=resp.part_name,
                method_parameters=struct_to_dict(resp.method_parameters),
                tags=list(resp.tags),
                payload=struct_to_dict(resp.payload),
            )
            for resp in response
        ]

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
        """Filter and download binary data. The data will be paginated into pages of ``limit`` items, and the pagination ID will be included
        in the returned tuple as ``last``. If a destination is provided, this method saves returned data to that file,
        overwriting any existing file content.

        ::

            from viam.utils import create_filter
            from viam.proto.app.data import Filter, TagsFilter, TagsFilterType

            # Get data captured from camera components
            my_data = []
            last = None
            my_filter = create_filter(component_name="camera-1")

            while True:
                data, count, last = await data_client.binary_data_by_filter(
                    my_filter, limit=1, last=last)
                if not data:
                    break
                my_data.extend(data)

            print(f"My data: {my_data}")

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
            filter (~viam.proto.app.data.Filter): Optional, specifies tabular data to retrieve. An empty filter matches all binary data.
            limit (int): The maximum number of entries to include in a page. Defaults to 50 if unspecified.
            sort_order (~viam.proto.app.data.Order): The desired sort order of the data.
            last (str): Optional string indicating the object identifier of the last-returned data.
                This object identifier is returned by calls to :meth:`binary_data_by_filter` as the ``last`` value.
                If provided, the server will return the next data entries after the last object identifier.
            include_binary_data (bool): Boolean specifying whether to actually include the binary file data with each retrieved file.
                Defaults to true (that is, both the files' data and metadata are returned).
            count_only (bool): Whether to return only the total count of entries.
            include_internal_data (bool): Whether to return the internal data. Internal data is used for Viam-specific data ingestion,
                like cloud SLAM. Defaults to ``False``.
            dest (str): Optional filepath for writing retrieved data.

        Returns:
            Tuple[List[~viam.proto.app.data.BinaryData], int, str]: A tuple containing the following:

                - ``data`` (*List[* :class:`~viam.proto.app.data.BinaryData` *]*): The binary data.
                - ``count`` (*int*): The count (number of entries).
                - ``last`` (*str*): The last-returned page ID.

        For more information, see `Data Client API <https://docs.viam.com/dev/reference/apis/data-client/#binarydatabyfilter>`_.
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
        binary_ids: Union[List[BinaryID], List[str]],
        dest: Optional[str] = None,
    ) -> List[BinaryData]:
        """Filter and download binary data.

        ::

            binary_metadata, count, last = await data_client.binary_data_by_filter(
                include_binary_data=False
            )

            my_ids = []

            for obj in binary_metadata:
                my_ids.append(obj.metadata.binary_data_id)

            binary_data = await data_client.binary_data_by_ids(my_ids)

        Args:
            binary_ids (Union[List[~viam.proto.app.data.BinaryID], List[str]]): Binary data ID strings specifying the desired data or
                :class:`BinaryID` objects. Must be non-empty.
                *DEPRECATED:* :class:`BinaryID` *is deprecated and will be removed in a future release. Instead, pass binary data IDs as a
                list of strings.*
            dest (str): Optional filepath for writing retrieved data.

        Raises:
            GRPCError: If no binary data ID strings or :class:`BinaryID` objects are provided.

        Returns:
            List[~viam.proto.app.data.BinaryData]: The binary data.

        For more information, see `Data Client API <https://docs.viam.com/dev/reference/apis/data-client/#binarydatabyids>`_.
        """
        request = BinaryDataByIDsRequest()
        if len(binary_ids) > 0 and isinstance(binary_ids[0], str):
            binary_data_ids = cast(List[str], binary_ids)
            request = BinaryDataByIDsRequest(binary_data_ids=binary_data_ids, include_binary=True)
        else:
            bin_ids = cast(List[BinaryID], binary_ids)
            request = BinaryDataByIDsRequest(binary_ids=bin_ids, include_binary=True)
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

            tabular_data = await data_client.delete_tabular_data(
                organization_id="<YOUR-ORG-ID>",
                delete_older_than_days=150
            )

        Args:
            organization_id (str): The ID of the organization to delete the data from.
                To find your organization ID, visit the organization settings page.
            delete_older_than_days (int): Delete data that was captured up to *this many* days ago. For example, a value of
                10 deletes any data that was captured up to 10 days ago. A value of 0 deletes *all* existing data.

        Returns:
            int: The number of items deleted.

        For more information, see `Data Client API <https://docs.viam.com/dev/reference/apis/data-client/#deletetabulardata>`_.
        """
        request = DeleteTabularDataRequest(organization_id=organization_id, delete_older_than_days=delete_older_than_days)
        response: DeleteTabularDataResponse = await self._data_client.DeleteTabularData(request, metadata=self._metadata)
        return response.deleted_count

    async def delete_tabular_data_by_filter(self, filter: Optional[Filter]) -> int:
        """Deprecated: use :meth:`delete_tabular_data` instead."""
        raise NotImplementedError()

    async def delete_binary_data_by_filter(self, filter: Optional[Filter]) -> int:
        """Filter and delete binary data.

        ::

            from viam.utils import create_filter

            my_filter = create_filter(component_name="left_motor", organization_ids=["<YOUR-ORG-ID>"])

            res = await data_client.delete_binary_data_by_filter(my_filter)

        Args:
            filter (~viam.proto.app.data.Filter): Optional, specifies binary data to delete.
                **CAUTION: Passing an empty** ``Filter`` **deletes all binary data!**
                You must specify an organization ID with ``organization_ids`` when using this option.
                To find your organization ID, visit the organization settings page.

        Returns:
            int: The number of items deleted.

        For more information, see `Data Client API <https://docs.viam.com/dev/reference/apis/data-client/#deletebinarydatabyfilter>`_.
        """
        filter = filter if filter else Filter()
        request = DeleteBinaryDataByFilterRequest(filter=filter)
        response: DeleteBinaryDataByFilterResponse = await self._data_client.DeleteBinaryDataByFilter(request, metadata=self._metadata)
        return response.deleted_count

    async def delete_binary_data_by_ids(self, binary_ids: Union[List[BinaryID], List[str]]) -> int:
        """Filter and delete binary data.

        ::

            from viam.proto.app.data import BinaryID
            from viam.utils import create_filter

            my_filter = create_filter(component_name="camera-1", organization_ids=["<YOUR-ORG-ID>"])
            binary_metadata, count, last = await data_client.binary_data_by_filter(
                filter=my_filter,
                limit=20,
                include_binary_data=False
            )

            my_ids = []

            for obj in binary_metadata:
                my_ids.append(
                    obj.metadata.binary_data_id
                )

            binary_data = await data_client.delete_binary_data_by_ids(my_ids)

        Args:
            binary_ids (Union[List[~viam.proto.app.data.BinaryID], List[str]]): Binary data ID strings specifying the data to be deleted or
                :class:`BinaryID` objects. Must be non-empty.
                *DEPRECATED:* :class:`BinaryID` *is deprecated and will be removed in a future release. Instead, pass binary data IDs as a
                list of strings.*

        Raises:
            GRPCError: If no binary data ID strings or :class:`BinaryID` objects are provided.

        Returns:
            int: The number of items deleted.

        For more information, see `Data Client API <https://docs.viam.com/dev/reference/apis/data-client/#deletebinarydatabyids>`_.
        """
        request = DeleteBinaryDataByIDsRequest()
        if len(binary_ids) > 0 and isinstance(binary_ids[0], str):
            binary_data_ids = cast(List[str], binary_ids)
            request = DeleteBinaryDataByIDsRequest(binary_data_ids=binary_data_ids)
        else:
            bin_ids = cast(List[BinaryID], binary_ids)
            request = DeleteBinaryDataByIDsRequest(binary_ids=bin_ids)
        response: DeleteBinaryDataByIDsResponse = await self._data_client.DeleteBinaryDataByIDs(request, metadata=self._metadata)
        return response.deleted_count

    async def add_tags_to_binary_data_by_ids(self, tags: List[str], binary_ids: Union[List[BinaryID], List[str]]) -> None:
        """Add tags to binary data.

        ::

            from viam.utils import create_filter

            tags = ["tag1", "tag2"]

            my_filter = create_filter(component_name="camera-1", organization_ids=["<YOUR-ORG-ID>"])
            binary_metadata, count, last = await data_client.binary_data_by_filter(
                filter=my_filter,
                limit=20,
                include_binary_data=False
            )

            my_ids = []

            for obj in binary_metadata:
                my_ids.append(
                    obj.metadata.binary_data_id
                )

            binary_data = await data_client.add_tags_to_binary_data_by_ids(tags, my_ids)

        Args:
            tags (List[str]): List of tags to add to specified binary data. Must be non-empty.
            binary_ids (Union[List[~viam.proto.app.data.BinaryID], List[str]]): Binary data ID strings specifying the data to be tagged or
                :class:`BinaryID` objects. Must be non-empty.
                *DEPRECATED:* :class:`BinaryID` *is deprecated and will be removed in a future release. Instead, pass binary data IDs as a
                list of strings.*

        Raises:
            GRPCError: If no binary data ID strings or :class:`BinaryID` objects are provided.

        For more information, see `Data Client API <https://docs.viam.com/dev/reference/apis/data-client/#addtagstobinarydatabyids>`_.
        """
        request = AddTagsToBinaryDataByIDsRequest()
        if len(binary_ids) > 0 and isinstance(binary_ids[0], str):
            binary_data_ids = cast(List[str], binary_ids)
            request = AddTagsToBinaryDataByIDsRequest(binary_data_ids=binary_data_ids, tags=tags)
        else:
            bin_ids = cast(List[BinaryID], binary_ids)
            request = AddTagsToBinaryDataByIDsRequest(binary_ids=bin_ids, tags=tags)
        await self._data_client.AddTagsToBinaryDataByIDs(request, metadata=self._metadata)

    async def add_tags_to_binary_data_by_filter(self, tags: List[str], filter: Optional[Filter] = None) -> None:
        """Add tags to binary data.

        ::

            from viam.utils import create_filter

            my_filter = create_filter(component_name="my_camera")
            tags = ["tag1", "tag2"]
            await data_client.add_tags_to_binary_data_by_filter(tags, my_filter)

        Args:
            tags (List[str]): List of tags to add to specified binary data. Must be non-empty.
            filter (~viam.proto.app.data.Filter): Specifies binary data to tag. If none is provided, tags all data.

        Raises:
            GRPCError: If no tags are provided.

        For more information, see `Data Client API <https://docs.viam.com/dev/reference/apis/data-client/#addtagstobinarydatabyfilter>`_.
        """
        filter = filter if filter else Filter()
        request = AddTagsToBinaryDataByFilterRequest(filter=filter, tags=tags)
        await self._data_client.AddTagsToBinaryDataByFilter(request, metadata=self._metadata)

    async def remove_tags_from_binary_data_by_ids(self, tags: List[str], binary_ids: Union[List[BinaryID], List[str]]) -> int:
        """Remove tags from binary data by IDs.

        ::

            from viam.utils import create_filter

            tags = ["tag1", "tag2"]

            my_filter = create_filter(component_name="camera-1")

            binary_metadata, count, last = await data_client.binary_data_by_filter(
                filter=my_filter,
                limit=50,
                include_binary_data=False
            )

            my_ids = []

            for obj in binary_metadata:
                my_ids.append(
                    obj.metadata.binary_data_id
                )

            binary_data = await data_client.remove_tags_from_binary_data_by_ids(
                tags, my_ids)

        Args:
            tags (List[str]): List of tags to remove from specified binary data. Must be non-empty.
            binary_ids (Union[List[~viam.proto.app.data.BinaryID], List[str]]): Binary data ID strings specifying the data to be untagged
                or `BinaryID` objects. Must be non-empty.
                *DEPRECATED:* :class:`BinaryID` *is deprecated and will be removed in a future release. Instead, pass binary data IDs as a
                list of strings.*

        Raises:
            GRPCError: If no binary data ID strings, :class:`BinaryID` objects, or tags are provided.

        Returns:
            int: The number of tags removed.

        For more information, see `Data Client API <https://docs.viam.com/dev/reference/apis/data-client/#removetagsfrombinarydatabyids>`_.
        """
        request = RemoveTagsFromBinaryDataByIDsRequest(tags=tags)
        if len(binary_ids) > 0 and isinstance(binary_ids[0], str):
            binary_data_ids = cast(List[str], binary_ids)
            request = RemoveTagsFromBinaryDataByIDsRequest(binary_data_ids=binary_data_ids, tags=tags)
        else:
            bin_ids = cast(List[BinaryID], binary_ids)
            request = RemoveTagsFromBinaryDataByIDsRequest(binary_ids=bin_ids, tags=tags)
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
            filter (~viam.proto.app.data.Filter): Specifies binary data to untag. If none is provided, removes tags from all data.

        Raises:
            GRPCError: If no tags are provided.

        Returns:
            int: The number of tags removed.

        For more information, see `Data Client API <https://docs.viam.com/dev/reference/apis/data-client/#removetagsfrombinarydatabyfilter>`_.
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
            filter (~viam.proto.app.data.Filter): Specifies subset ofdata to retrieve tags from. If none is provided, returns all tags.

        Returns:
            List[str]: The list of tags.

        For more information, see `Data Client API <https://docs.viam.com/dev/reference/apis/data-client/#tagsbyfilter>`_.
        """
        filter = filter if filter else Filter()
        request = TagsByFilterRequest(filter=filter)
        response: TagsByFilterResponse = await self._data_client.TagsByFilter(request, metadata=self._metadata)
        return list(response.tags)

    async def add_bounding_box_to_image_by_id(
        self,
        binary_id: Union[BinaryID, str],
        label: str,
        x_min_normalized: float,
        y_min_normalized: float,
        x_max_normalized: float,
        y_max_normalized: float,
    ) -> str:
        """Add a bounding box to an image.

        ::

            bbox_id = await data_client.add_bounding_box_to_image_by_id(
                binary_id="<YOUR-BINARY-DATA-ID>",
                label="label",
                x_min_normalized=0,
                y_min_normalized=.1,
                x_max_normalized=.2,
                y_max_normalized=.3
            )

            print(bbox_id)

        Args:
            binary_id (Union[~viam.proto.app.data.BinaryID, str]): The binary data ID or :class:`BinaryID` of the image to add the bounding
                box to. *DEPRECATED:* :class:`BinaryID` *is deprecated and will be removed in a future release. Instead, pass binary data
                IDs as a list of strings.*
            label (str): A label for the bounding box.
            x_min_normalized (float): Min X value of the bounding box normalized from 0 to 1.
            y_min_normalized (float): Min Y value of the bounding box normalized from 0 to 1.
            x_max_normalized (float): Max X value of the bounding box normalized from 0 to 1.
            y_max_normalized (float): Max Y value of the bounding box normalized from 0 to 1.

        Raises:
            GRPCError: If the X or Y values are outside of the [0, 1] range.

        Returns:
            str: The bounding box ID.

        For more information, see `Data Client API <https://docs.viam.com/dev/reference/apis/data-client/#addboundingboxtoimagebyid>`_.
        """
        request = AddBoundingBoxToImageByIDRequest()
        if isinstance(binary_id, str):
            request = AddBoundingBoxToImageByIDRequest(
                binary_data_id=binary_id,
                label=label,
                x_max_normalized=x_max_normalized,
                x_min_normalized=x_min_normalized,
                y_max_normalized=y_max_normalized,
                y_min_normalized=y_min_normalized,
            )
        else:
            request = AddBoundingBoxToImageByIDRequest(
                binary_id=binary_id,
                label=label,
                x_max_normalized=x_max_normalized,
                x_min_normalized=x_min_normalized,
                y_max_normalized=y_max_normalized,
                y_min_normalized=y_min_normalized,
            )
        response: AddBoundingBoxToImageByIDResponse = await self._data_client.AddBoundingBoxToImageByID(request, metadata=self._metadata)
        return response.bbox_id

    async def remove_bounding_box_from_image_by_id(self, bbox_id: str, binary_id: Union[BinaryID, str]) -> None:
        """Removes a bounding box from an image.

        ::

            await data_client.remove_bounding_box_from_image_by_id(
            binary_id="<YOUR-BINARY-DATA-ID>",
            bbox_id="your-bounding-box-id-to-delete"
            )

        Args:
            bbox_id (str): The ID of the bounding box to remove.
            binary_id (Union[~viam.proto.app.data.BinaryID, str]): The binary data ID or :class:`BinaryID` of the image to remove the
                bounding box from.
                *DEPRECATED:* :class:`BinaryID` *is deprecated and will be removed in a future release. Instead, pass binary data IDs as a
                list of strings.*

        For more information, see `Data Client API <https://docs.viam.com/dev/reference/apis/data-client/#removeboundingboxfromimagebyid>`_.
        """
        request = RemoveBoundingBoxFromImageByIDRequest()
        if isinstance(binary_id, str):
            request = RemoveBoundingBoxFromImageByIDRequest(binary_data_id=binary_id, bbox_id=bbox_id)
        else:
            request = RemoveBoundingBoxFromImageByIDRequest(binary_id=binary_id, bbox_id=bbox_id)

        await self._data_client.RemoveBoundingBoxFromImageByID(request, metadata=self._metadata)

    async def bounding_box_labels_by_filter(self, filter: Optional[Filter] = None) -> List[str]:
        """Get a list of bounding box labels using a `Filter`.

        ::

            from viam.utils import create_filter

            my_filter = create_filter(component_name="my_camera")
            bounding_box_labels = await data_client.bounding_box_labels_by_filter(
                my_filter)

            print(bounding_box_labels)

        Args:
            filter (~viam.proto.app.data.Filter): Specifies data to retrieve bounding box labels from. If none is provided, returns labels
            from all data.

        Returns:
            List[str]: The list of bounding box labels.

        For more information, see `Data Client API <https://docs.viam.com/dev/reference/apis/data-client/#boundingboxlabelsbyfilter>`_.
        """
        filter = filter if filter else Filter()
        request = BoundingBoxLabelsByFilterRequest(filter=filter)
        response: BoundingBoxLabelsByFilterResponse = await self._data_client.BoundingBoxLabelsByFilter(request, metadata=self._metadata)
        return list(response.labels)

    async def get_database_connection(self, organization_id: str) -> str:
        """Get a connection to access a MongoDB Atlas Data federation instance.

        ::

            hostname = await data_client.get_database_connection(organization_id="<YOUR-ORG-ID>")

        Args:
            organization_id (str): The ID of the organization you'd like to connect to.
                To find your organization ID, visit the organization settings page.

        Returns:
            str: The hostname of the federated database.

        For more information, see `Data Client API <https://docs.viam.com/dev/reference/apis/data-client/#getdatabaseconnection>`_.
        """
        request = GetDatabaseConnectionRequest(organization_id=organization_id)
        response: GetDatabaseConnectionResponse = await self._data_client.GetDatabaseConnection(request, metadata=self._metadata)
        return response.hostname

    async def configure_database_user(self, organization_id: str, password: str) -> None:
        """Configure a database user for the Viam organization's MongoDB Atlas Data Federation instance. It can also be used to reset the
        password of the existing database user.

        ::

            await data_client.configure_database_user(
                organization_id="<YOUR-ORG-ID>",
                password="Your_Password@1234"
            )

        Args:
            organization_id (str): The ID of the organization you'd like to configure a database user for.
                To find your organization ID, visit the organization settings page.
            password (str): The password of the user.

        For more information, see `Data Client API <https://docs.viam.com/dev/reference/apis/data-client/#configuredatabaseuser>`_.
        """
        request = ConfigureDatabaseUserRequest(organization_id=organization_id, password=password)
        await self._data_client.ConfigureDatabaseUser(request, metadata=self._metadata)

    async def create_dataset(self, name: str, organization_id: str) -> str:
        """Create a new dataset.

        ::

            dataset_id = await data_client.create_dataset(
                name="<DATASET-NAME>",
                organization_id="<YOUR-ORG-ID>"
            )
            print(dataset_id)

        Args:
            name (str): The name of the dataset being created.
            organization_id (str): The ID of the organization where the dataset is being created.
                To find your organization ID, visit the organization settings page.

        Returns:
            str: The dataset ID of the created dataset.

        For more information, see `Data Client API <https://docs.viam.com/dev/reference/apis/data-client/#createdataset>`_.
        """
        request = CreateDatasetRequest(name=name, organization_id=organization_id)
        response: CreateDatasetResponse = await self._dataset_client.CreateDataset(request, metadata=self._metadata)
        return response.id

    async def list_dataset_by_ids(self, ids: List[str]) -> Sequence[Dataset]:
        """Get a list of datasets using their IDs.

        ::

            datasets = await data_client.list_dataset_by_ids(
                ids=["<YOUR-DATASET-ID-1>, <YOUR-DATASET-ID-2>"]
            )
            print(datasets)

        Args:
            ids (List[str]): The IDs of the datasets that you would like to retrieve information about. To retrieve a dataset ID:

                - Navigate to the **DATASETS** tab of the **DATA** page.
                - Click on the dataset.
                - Click the **...** menu.
                - Select **Copy dataset ID**.

        Returns:
            Sequence[Dataset]: The list of datasets.

        For more information, see `Data Client API <https://docs.viam.com/dev/reference/apis/data-client/#listdatasetsbyids>`_.
        """
        request = ListDatasetsByIDsRequest(ids=ids)
        response: ListDatasetsByIDsResponse = await self._dataset_client.ListDatasetsByIDs(request, metadata=self._metadata)

        return response.datasets

    async def list_datasets_by_organization_id(self, organization_id: str) -> Sequence[Dataset]:
        """Get the datasets in an organization.

        ::

            datasets = await data_client.list_datasets_by_organization_id(
                organization_id="<YOUR-ORG-ID>"
            )
            print(datasets)

        Args:
            organization_id (str): The ID of the organization you'd like to retrieve datasets from.
                To find your organization ID, visit the organization settings page.

        Returns:
            Sequence[Dataset]: The list of datasets in the organization.

        For more information, see `Data Client API <https://docs.viam.com/dev/reference/apis/data-client/#listdatasetsbyorganizationid>`_.
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
                id="<YOUR-DATASET-ID>",
                name="MyDataset"
            )

        Args:
            id (str): The ID of the dataset. To retrieve the dataset ID:

                - Navigate to the **DATASETS** tab of the **DATA** page.
                - Click on the dataset.
                - Click the **...** menu.
                - Select **Copy dataset ID**.
            name (str): The new name of the dataset.

        For more information, see `Data Client API <https://docs.viam.com/dev/reference/apis/data-client/#renamedataset>`_.
        """
        request = RenameDatasetRequest(id=id, name=name)
        await self._dataset_client.RenameDataset(request, metadata=self._metadata)

    async def delete_dataset(self, id: str) -> None:
        """Delete a dataset.

        ::

            await data_client.delete_dataset(
                id="<YOUR-DATASET-ID>"
            )

        Args:
            id (str): The ID of the dataset. To retrieve the dataset ID:

                    - Navigate to the **DATASETS** tab of the **DATA** page.
                    - Click on the dataset.
                    - Click the **...** menu.
                    - Select **Copy dataset ID**.

        For more information, see `Data Client API <https://docs.viam.com/dev/reference/apis/data-client/#deletedataset>`_.
        """
        request = DeleteDatasetRequest(id=id)
        await self._dataset_client.DeleteDataset(request, metadata=self._metadata)

    async def add_binary_data_to_dataset_by_ids(self, binary_ids: Union[List[BinaryID], List[str]], dataset_id: str) -> None:
        """Add the BinaryData to the provided dataset.

        This BinaryData will be tagged with the VIAM_DATASET_{id} label.

        ::

            binary_metadata, count, last = await data_client.binary_data_by_filter(
                include_binary_data=False
            )

            my_binary_data_ids = []

            for obj in binary_metadata:
                my_binary_data_ids.append(
                    obj.metadata.binary_data_id
                    )

            await data_client.add_binary_data_to_dataset_by_ids(
                binary_ids=my_binary_data_ids,
                dataset_id="abcd-1234xyz-8765z-123abc"
            )

        Args:
            binary_ids (List[~viam.proto.app.data.BinaryID]): Unique identifiers for binary data to add to the dataset. To retrieve these IDs,
                navigate to the DATA page, click on an image, and copy its Binary Data ID from the details tab.
            dataset_id (str): The ID of the dataset to be added to.  To retrieve the dataset ID:

                - Navigate to the **DATASETS** tab of the **DATA** page.
                - Click on the dataset.
                - Click the **...** menu.
                - Select **Copy dataset ID**.

        For more information, see `Data Client API <https://docs.viam.com/dev/reference/apis/data-client/#addbinarydatatodatasetbyids>`_.
        """
        request = AddBinaryDataToDatasetByIDsRequest()
        if len(binary_ids) > 0 and isinstance(binary_ids[0], str):
            binary_data_ids = cast(List[str], binary_ids)
            request = AddBinaryDataToDatasetByIDsRequest(binary_data_ids=binary_data_ids, dataset_id=dataset_id)
        else:
            bin_ids = cast(List[BinaryID], binary_ids)
            request = AddBinaryDataToDatasetByIDsRequest(binary_ids=bin_ids, dataset_id=dataset_id)
        await self._data_client.AddBinaryDataToDatasetByIDs(request, metadata=self._metadata)

    async def remove_binary_data_from_dataset_by_ids(self, binary_ids: Union[List[BinaryID], List[str]], dataset_id: str) -> None:
        """Remove the BinaryData from the provided dataset.

        This BinaryData will lose the VIAM_DATASET_{id} tag.

        ::

            binary_metadata, count, last = await data_client.binary_data_by_filter(
                include_binary_data=False
            )

            my_binary_data_ids = []

            for obj in binary_metadata:
                my_binary_data_ids.append(
                    obj.metadata.binary_data_id
                )

            await data_client.remove_binary_data_from_dataset_by_ids(
                binary_ids=my_binary_data_ids,
                dataset_id="abcd-1234xyz-8765z-123abc"
            )

        Args:
            binary_ids (Union[List[~viam.proto.app.data.BinaryID], List[str]]): Unique identifiers for the binary data to remove from the dataset. To retrieve these IDs,
                navigate to the DATA page, click on an image and copy its Binary Data ID from the details tab.
                *DEPRECATED:* :class:`BinaryID` *is deprecated and will be removed in a future release. Instead, pass binary data IDs as a
                list of strings.*
            dataset_id (str): The ID of the dataset to be removed from. To retrieve the dataset ID:

                - Navigate to the **DATASETS** tab of the **DATA** page.
                - Click on the dataset.
                - Click the **...** menu.
                - Select **Copy dataset ID**.

        For more information, see `Data Client API <https://docs.viam.com/dev/reference/apis/data-client/#removebinarydatafromdatasetbyids>`_.
        """
        request = RemoveBinaryDataFromDatasetByIDsRequest()
        if len(binary_ids) > 0 and isinstance(binary_ids[0], str):
            binary_data_ids = cast(List[str], binary_ids)
            request = RemoveBinaryDataFromDatasetByIDsRequest(binary_data_ids=binary_data_ids, dataset_id=dataset_id)
        else:
            bin_ids = cast(List[BinaryID], binary_ids)
            request = RemoveBinaryDataFromDatasetByIDsRequest(binary_ids=bin_ids, dataset_id=dataset_id)
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

        Upload binary data collected on a robot through a specific component (for example, a motor), along with the relevant metadata.
        Binary data can be found on the **DATA** page.

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
            file_extension (str): The file extension of binary data, *including the period*, for example ``.jpg``, ``.png``, ``.pcd``.
                The backend routes the binary to its corresponding mime type based on this extension. Files with a ``.jpeg``, ``.jpg``,
                or ``.png`` extension will appear in the **Images** tab.
            method_parameters (Optional[Mapping[str, Any]]): Optional dictionary of method parameters. No longer in active use.
            tags (Optional[List[str]]): Optional list of tags to allow for tag-based data filtering when retrieving data.
            data_request_times (Optional[Tuple[datetime.datetime, datetime.datetime]]): Optional tuple containing datetime objects
                denoting the times this data was requested ``[0]`` by the robot and received ``[1]`` from the appropriate sensor.

        Raises:
            GRPCError: If an invalid part ID is passed.

        Returns:
            str: The binary data ID of the uploaded data.

        For more information, see `Data Client API <https://docs.viam.com/dev/reference/apis/data-client/#binarydatacaptureupload>`_.
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
        return response.binary_data_id

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

        Upload tabular data collected on a robot through a specific component (for example, a motor), along with the relevant metadata.
        Tabular data can be found under the **Sensors** tab of the **DATA** page.

        ::

            from datetime import datetime

            time_requested = datetime(2023, 6, 5, 11)
            time_received = datetime(2023, 6, 5, 11, 0, 3)
            file_id = await data_client.tabular_data_capture_upload(
                part_id="INSERT YOUR PART ID",
                component_type='rdk:component:movement_sensor',
                component_name='my_movement_sensor',
                method_name='Readings',
                tags=["sensor_data"],
                data_request_times=[(time_requested, time_received)],
                tabular_data=[{
                    'readings': {
                        'linear_velocity': {'x': 0.5, 'y': 0.0, 'z': 0.0},
                        'angular_velocity': {'x': 0.0, 'y': 0.0, 'z': 0.1}
                    }
                }]
            )

        Args:
            tabular_data (List[Mapping[str, Any]]): List of the data to be uploaded, represented tabularly as a collection of dictionaries.
                Must include the key ``readings`` for sensors.
            part_id (str): Part ID of the component used to capture the data.
            component_type (str): Type of the component used to capture the data (for example, ``rdk:component:movement_sensor``).
            component_name (str): Name of the component used to capture the data.
            method_name (str): Name of the method used to capture the data.
            data_request_times (List[Tuple[datetime.datetime, datetime.datetime]]): List of tuples, each containing ``datetime`` objects
                denoting the times this data was requested ``[0]`` by the robot and received ``[1]`` from the appropriate sensor.
                Pass a list of tabular data and timestamps with length ``n > 1`` to upload ``n`` datapoints, all with the same metadata.
            method_parameters (Optional[Mapping[str, Any]]): Optional dictionary of method parameters. No longer in active use.
            tags (Optional[List[str]]): Optional list of tags to allow for tag-based data filtering when retrieving data.

        Raises:
            GRPCError: If an invalid part ID is passed.
            ValueError: If the provided list of `Timestamp` objects has a length that does not match the length of the list of tabular
                data.

        Returns:
            str: The file ID of the uploaded data.

        For more information, see `Data Client API <https://docs.viam.com/dev/reference/apis/data-client/#tabulardatacaptureupload>`_.
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
                data_request_times=[time_requested, time_received],
                tags=["tag_1", "tag_2"]
            )

        Args:
            data (bytes): The data to be uploaded.
            part_id (str): Part ID of the resource associated with the file.
            file_ext (str): File extension type for the data. required for determining MIME type.
            component_type (Optional[str]): Optional type of the component associated with the file (for example, "movement_sensor").
            component_name (Optional[str]): Optional name of the component associated with the file.
            method_name (Optional[str]): Optional name of the method associated with the file.
            method_parameters (Optional[str]): Optional dictionary of the method parameters. No longer in active use.
            data_request_times (Optional[Tuple[datetime.datetime, datetime.datetime]]): Optional tuple containing datetime objects
                denoting the times this data was requested ``[0]`` by the robot and received ``[1]`` from the appropriate sensor.
            tags (Optional[List[str]]): Optional list of tags to allow for tag-based filtering when retrieving data.

        Raises:
            GRPCError: If an invalid part ID is passed.

        Returns:
            str: The binary data ID of the uploaded data.

        For more information, see `Data Client API <https://docs.viam.com/dev/reference/apis/data-client/#streamingdatacaptureupload>`_.
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
            return response.binary_data_id

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

        Upload file data that may be stored on a robot along with the relevant metadata. File data can be found in the
        **Files** tab of the **DATA** page.

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
            file_name (Optional[str]): Optional name of the file. The empty string ``""`` will be assigned as the file name if one isn't
                provided.
            method_parameters (Optional[str]): Optional dictionary of the method parameters. No longer in active use.
            file_extension (Optional[str]): Optional file extension. The empty string ``""`` will be assigned as the file extension if one
                isn't provided. Files with a ``.jpeg``, ``.jpg``, or ``.png`` extension will be saved to the **Images** tab.
            tags (Optional[List[str]]): Optional list of tags to allow for tag-based filtering when retrieving data.

        Raises:
            GRPCError: If an invalid part ID is passed.

        Returns:
            str: Binary data ID of the new file.

        For more information, see `Data Client API <https://docs.viam.com/dev/reference/apis/data-client/#fileupload>`_.
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
        return response.binary_data_id

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

        Upload file data that may be stored on a robot along with the relevant metadata. File data can be found in the
        **Files** tab of the **DATA** page.

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
            str: Binary data ID of the new file.

        For more information, see `Data Client API <https://docs.viam.com/dev/reference/apis/data-client/#fileuploadfrompath>`_.
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
        return response.binary_data_id

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

    async def get_data_pipeline(self, id: str) -> DataPipeline:
        """Get a data pipeline by its ID.

        ::

            data_pipeline = await data_client.get_data_pipeline(id="<YOUR-DATA-PIPELINE-ID>")

        Args:
            id (str): The ID of the data pipeline to get.

        Returns:
            DataPipeline: The data pipeline with the given ID.
        """
        request = GetDataPipelineRequest(id=id)
        response: GetDataPipelineResponse = await self._data_pipelines_client.GetDataPipeline(request, metadata=self._metadata)
        return DataClient.DataPipeline.from_proto(response.data_pipeline)

    async def list_data_pipelines(self, organization_id: str) -> List[DataPipeline]:
        """List all of the data pipelines for an organization.

        ::

            data_pipelines = await data_client.list_data_pipelines(organization_id="<YOUR-ORGANIZATION-ID>")

        Args:
            organization_id (str): The ID of the organization that owns the pipelines.
                You can obtain your organization ID from the organization settings page.

        Returns:
            List[DataPipeline]: A list of all of the data pipelines for the given organization.
        """
        request = ListDataPipelinesRequest(organization_id=organization_id)
        response: ListDataPipelinesResponse = await self._data_pipelines_client.ListDataPipelines(request, metadata=self._metadata)
        return [DataClient.DataPipeline.from_proto(pipeline) for pipeline in response.data_pipelines]

    async def create_data_pipeline(
        self,
        organization_id: str,
        name: str,
        mql_binary: List[Dict[str, Any]],
        schedule: str,
        enable_backfill: bool,
        data_source_type: TabularDataSourceType.ValueType = TabularDataSourceType.TABULAR_DATA_SOURCE_TYPE_STANDARD,
    ) -> str:
        """Create a new data pipeline.

        ::

            data_pipeline_id = await data_client.create_data_pipeline(
                organization_id="<YOUR-ORGANIZATION-ID>",
                name="<YOUR-PIPELINE-NAME>",
                mql_binary=[<YOUR-MQL-PIPELINE-AGGREGATION>],
                schedule="<YOUR-SCHEDULE>",
                data_source_type=TabularDataSourceType.TABULAR_DATA_SOURCE_TYPE_STANDARD,
            )

        Args:
            organization_id (str): The ID of the organization that will own the pipeline.
                You can obtain your organization ID from the organization settings page.
            name (str): The name of the pipeline.
            mql_binary (List[Dict[str, Any]]):The MQL pipeline to run, as a list of MongoDB aggregation pipeline stages.
            schedule (str): A cron expression representing the expected execution schedule in UTC (note this also
                defines the input time window; an hourly schedule would process 1 hour of data at a time).
            enable_backfill (bool):  When true, pipeline runs will be scheduled for the organization's past data.
            data_source_type (TabularDataSourceType): The type of data source to use for the pipeline.
                Defaults to TabularDataSourceType.TABULAR_DATA_SOURCE_TYPE_STANDARD.

        Returns:
            str: The ID of the newly created pipeline.
        """
        binary: List[bytes] = [bson.encode(query) for query in mql_binary]
        request = CreateDataPipelineRequest(
            organization_id=organization_id,
            name=name,
            mql_binary=binary,
            schedule=schedule,
            enable_backfill=enable_backfill,
            data_source_type=data_source_type,
        )
        response: CreateDataPipelineResponse = await self._data_pipelines_client.CreateDataPipeline(request, metadata=self._metadata)
        return response.id

    async def delete_data_pipeline(self, id: str) -> None:
        """Delete a data pipeline by its ID.

        ::

            await data_client.delete_data_pipeline(id="<YOUR-DATA-PIPELINE-ID>")

        Args:
            id (str): The ID of the data pipeline to delete.
        """
        request = DeleteDataPipelineRequest(id=id)
        await self._data_pipelines_client.DeleteDataPipeline(request, metadata=self._metadata)

    async def list_data_pipeline_runs(self, id: str, page_size: int = 10) -> DataPipelineRunsPage:
        """List all of the data pipeline runs for a data pipeline.

        ::

            data_pipeline_runs = await data_client.list_data_pipeline_runs(id="<YOUR-DATA-PIPELINE-ID>")
            while len(data_pipeline_runs.runs) > 0:
                data_pipeline_runs = await data_pipeline_runs.next_page()

        Args:
            id (str): The ID of the pipeline to list runs for
            page_size (int): The number of runs to return per page. Defaults to 10.

        Returns:
            DataPipelineRunsPage: A page of data pipeline runs with pagination support
        """
        return await self._list_data_pipeline_runs(id, page_size)

    async def _list_data_pipeline_runs(self, id: str, page_size: int, page_token: str = "") -> DataPipelineRunsPage:
        """Internal method to list data pipeline runs with pagination.

        Args:
            id (str): The ID of the pipeline to list runs for
            page_size (int): The number of runs to return per page
            page_token (str): The token to use to get the next page of results

        Returns:
            DataPipelineRunsPage: A page of data pipeline runs with pagination support
        """
        request = ListDataPipelineRunsRequest(id=id, page_size=page_size, page_token=page_token)
        response: ListDataPipelineRunsResponse = await self._data_pipelines_client.ListDataPipelineRuns(request, metadata=self._metadata)
        return DataClient.DataPipelineRunsPage.from_proto(response, self, page_size)

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
