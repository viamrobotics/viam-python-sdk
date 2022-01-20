"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.datastore.admin.v1.index_pb2
import google.datastore.admin.v1.migration_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import google.protobuf.timestamp_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class _OperationType:
    ValueType = typing.NewType('ValueType', builtins.int)
    V: typing_extensions.TypeAlias = ValueType
class _OperationTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_OperationType.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
    OPERATION_TYPE_UNSPECIFIED: OperationType.ValueType = ...  # 0
    """Unspecified."""

    EXPORT_ENTITIES: OperationType.ValueType = ...  # 1
    """ExportEntities."""

    IMPORT_ENTITIES: OperationType.ValueType = ...  # 2
    """ImportEntities."""

    CREATE_INDEX: OperationType.ValueType = ...  # 3
    """CreateIndex."""

    DELETE_INDEX: OperationType.ValueType = ...  # 4
    """DeleteIndex."""

class OperationType(_OperationType, metaclass=_OperationTypeEnumTypeWrapper):
    """Operation types."""
    pass

OPERATION_TYPE_UNSPECIFIED: OperationType.ValueType = ...  # 0
"""Unspecified."""

EXPORT_ENTITIES: OperationType.ValueType = ...  # 1
"""ExportEntities."""

IMPORT_ENTITIES: OperationType.ValueType = ...  # 2
"""ImportEntities."""

CREATE_INDEX: OperationType.ValueType = ...  # 3
"""CreateIndex."""

DELETE_INDEX: OperationType.ValueType = ...  # 4
"""DeleteIndex."""

global___OperationType = OperationType


class CommonMetadata(google.protobuf.message.Message):
    """Metadata common to all Datastore Admin operations."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class _State:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _StateEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_State.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        STATE_UNSPECIFIED: CommonMetadata.State.ValueType = ...  # 0
        """Unspecified."""

        INITIALIZING: CommonMetadata.State.ValueType = ...  # 1
        """Request is being prepared for processing."""

        PROCESSING: CommonMetadata.State.ValueType = ...  # 2
        """Request is actively being processed."""

        CANCELLING: CommonMetadata.State.ValueType = ...  # 3
        """Request is in the process of being cancelled after user called
        google.longrunning.Operations.CancelOperation on the operation.
        """

        FINALIZING: CommonMetadata.State.ValueType = ...  # 4
        """Request has been processed and is in its finalization stage."""

        SUCCESSFUL: CommonMetadata.State.ValueType = ...  # 5
        """Request has completed successfully."""

        FAILED: CommonMetadata.State.ValueType = ...  # 6
        """Request has finished being processed, but encountered an error."""

        CANCELLED: CommonMetadata.State.ValueType = ...  # 7
        """Request has finished being cancelled after user called
        google.longrunning.Operations.CancelOperation.
        """

    class State(_State, metaclass=_StateEnumTypeWrapper):
        """The various possible states for an ongoing Operation."""
        pass

    STATE_UNSPECIFIED: CommonMetadata.State.ValueType = ...  # 0
    """Unspecified."""

    INITIALIZING: CommonMetadata.State.ValueType = ...  # 1
    """Request is being prepared for processing."""

    PROCESSING: CommonMetadata.State.ValueType = ...  # 2
    """Request is actively being processed."""

    CANCELLING: CommonMetadata.State.ValueType = ...  # 3
    """Request is in the process of being cancelled after user called
    google.longrunning.Operations.CancelOperation on the operation.
    """

    FINALIZING: CommonMetadata.State.ValueType = ...  # 4
    """Request has been processed and is in its finalization stage."""

    SUCCESSFUL: CommonMetadata.State.ValueType = ...  # 5
    """Request has completed successfully."""

    FAILED: CommonMetadata.State.ValueType = ...  # 6
    """Request has finished being processed, but encountered an error."""

    CANCELLED: CommonMetadata.State.ValueType = ...  # 7
    """Request has finished being cancelled after user called
    google.longrunning.Operations.CancelOperation.
    """


    class LabelsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: typing.Text = ...
        value: typing.Text = ...
        def __init__(self,
            *,
            key : typing.Text = ...,
            value : typing.Text = ...,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["key",b"key","value",b"value"]) -> None: ...

    START_TIME_FIELD_NUMBER: builtins.int
    END_TIME_FIELD_NUMBER: builtins.int
    OPERATION_TYPE_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    STATE_FIELD_NUMBER: builtins.int
    @property
    def start_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """The time that work began on the operation."""
        pass
    @property
    def end_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """The time the operation ended, either successfully or otherwise."""
        pass
    operation_type: global___OperationType.ValueType = ...
    """The type of the operation. Can be used as a filter in
    ListOperationsRequest.
    """

    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[typing.Text, typing.Text]:
        """The client-assigned labels which were provided when the operation was
        created. May also include additional labels.
        """
        pass
    state: global___CommonMetadata.State.ValueType = ...
    """The current state of the Operation."""

    def __init__(self,
        *,
        start_time : typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        end_time : typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        operation_type : global___OperationType.ValueType = ...,
        labels : typing.Optional[typing.Mapping[typing.Text, typing.Text]] = ...,
        state : global___CommonMetadata.State.ValueType = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["end_time",b"end_time","start_time",b"start_time"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["end_time",b"end_time","labels",b"labels","operation_type",b"operation_type","start_time",b"start_time","state",b"state"]) -> None: ...
global___CommonMetadata = CommonMetadata

class Progress(google.protobuf.message.Message):
    """Measures the progress of a particular metric."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    WORK_COMPLETED_FIELD_NUMBER: builtins.int
    WORK_ESTIMATED_FIELD_NUMBER: builtins.int
    work_completed: builtins.int = ...
    """The amount of work that has been completed. Note that this may be greater
    than work_estimated.
    """

    work_estimated: builtins.int = ...
    """An estimate of how much work needs to be performed. May be zero if the
    work estimate is unavailable.
    """

    def __init__(self,
        *,
        work_completed : builtins.int = ...,
        work_estimated : builtins.int = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["work_completed",b"work_completed","work_estimated",b"work_estimated"]) -> None: ...
global___Progress = Progress

class ExportEntitiesRequest(google.protobuf.message.Message):
    """The request for
    [google.datastore.admin.v1.DatastoreAdmin.ExportEntities][google.datastore.admin.v1.DatastoreAdmin.ExportEntities].
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class LabelsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: typing.Text = ...
        value: typing.Text = ...
        def __init__(self,
            *,
            key : typing.Text = ...,
            value : typing.Text = ...,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["key",b"key","value",b"value"]) -> None: ...

    PROJECT_ID_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    ENTITY_FILTER_FIELD_NUMBER: builtins.int
    OUTPUT_URL_PREFIX_FIELD_NUMBER: builtins.int
    project_id: typing.Text = ...
    """Required. Project ID against which to make the request."""

    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[typing.Text, typing.Text]:
        """Client-assigned labels."""
        pass
    @property
    def entity_filter(self) -> global___EntityFilter:
        """Description of what data from the project is included in the export."""
        pass
    output_url_prefix: typing.Text = ...
    """Required. Location for the export metadata and data files.

    The full resource URL of the external storage location. Currently, only
    Google Cloud Storage is supported. So output_url_prefix should be of the
    form: `gs://BUCKET_NAME[/NAMESPACE_PATH]`, where `BUCKET_NAME` is the
    name of the Cloud Storage bucket and `NAMESPACE_PATH` is an optional Cloud
    Storage namespace path (this is not a Cloud Datastore namespace). For more
    information about Cloud Storage namespace paths, see
    [Object name
    considerations](https://cloud.google.com/storage/docs/naming#object-considerations).

    The resulting files will be nested deeper than the specified URL prefix.
    The final output URL will be provided in the
    [google.datastore.admin.v1.ExportEntitiesResponse.output_url][google.datastore.admin.v1.ExportEntitiesResponse.output_url] field. That
    value should be used for subsequent ImportEntities operations.

    By nesting the data files deeper, the same Cloud Storage bucket can be used
    in multiple ExportEntities operations without conflict.
    """

    def __init__(self,
        *,
        project_id : typing.Text = ...,
        labels : typing.Optional[typing.Mapping[typing.Text, typing.Text]] = ...,
        entity_filter : typing.Optional[global___EntityFilter] = ...,
        output_url_prefix : typing.Text = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["entity_filter",b"entity_filter"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["entity_filter",b"entity_filter","labels",b"labels","output_url_prefix",b"output_url_prefix","project_id",b"project_id"]) -> None: ...
global___ExportEntitiesRequest = ExportEntitiesRequest

class ImportEntitiesRequest(google.protobuf.message.Message):
    """The request for
    [google.datastore.admin.v1.DatastoreAdmin.ImportEntities][google.datastore.admin.v1.DatastoreAdmin.ImportEntities].
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class LabelsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: typing.Text = ...
        value: typing.Text = ...
        def __init__(self,
            *,
            key : typing.Text = ...,
            value : typing.Text = ...,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["key",b"key","value",b"value"]) -> None: ...

    PROJECT_ID_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    INPUT_URL_FIELD_NUMBER: builtins.int
    ENTITY_FILTER_FIELD_NUMBER: builtins.int
    project_id: typing.Text = ...
    """Required. Project ID against which to make the request."""

    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[typing.Text, typing.Text]:
        """Client-assigned labels."""
        pass
    input_url: typing.Text = ...
    """Required. The full resource URL of the external storage location. Currently, only
    Google Cloud Storage is supported. So input_url should be of the form:
    `gs://BUCKET_NAME[/NAMESPACE_PATH]/OVERALL_EXPORT_METADATA_FILE`, where
    `BUCKET_NAME` is the name of the Cloud Storage bucket, `NAMESPACE_PATH` is
    an optional Cloud Storage namespace path (this is not a Cloud Datastore
    namespace), and `OVERALL_EXPORT_METADATA_FILE` is the metadata file written
    by the ExportEntities operation. For more information about Cloud Storage
    namespace paths, see
    [Object name
    considerations](https://cloud.google.com/storage/docs/naming#object-considerations).

    For more information, see
    [google.datastore.admin.v1.ExportEntitiesResponse.output_url][google.datastore.admin.v1.ExportEntitiesResponse.output_url].
    """

    @property
    def entity_filter(self) -> global___EntityFilter:
        """Optionally specify which kinds/namespaces are to be imported. If provided,
        the list must be a subset of the EntityFilter used in creating the export,
        otherwise a FAILED_PRECONDITION error will be returned. If no filter is
        specified then all entities from the export are imported.
        """
        pass
    def __init__(self,
        *,
        project_id : typing.Text = ...,
        labels : typing.Optional[typing.Mapping[typing.Text, typing.Text]] = ...,
        input_url : typing.Text = ...,
        entity_filter : typing.Optional[global___EntityFilter] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["entity_filter",b"entity_filter"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["entity_filter",b"entity_filter","input_url",b"input_url","labels",b"labels","project_id",b"project_id"]) -> None: ...
global___ImportEntitiesRequest = ImportEntitiesRequest

class ExportEntitiesResponse(google.protobuf.message.Message):
    """The response for
    [google.datastore.admin.v1.DatastoreAdmin.ExportEntities][google.datastore.admin.v1.DatastoreAdmin.ExportEntities].
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    OUTPUT_URL_FIELD_NUMBER: builtins.int
    output_url: typing.Text = ...
    """Location of the output metadata file. This can be used to begin an import
    into Cloud Datastore (this project or another project). See
    [google.datastore.admin.v1.ImportEntitiesRequest.input_url][google.datastore.admin.v1.ImportEntitiesRequest.input_url].
    Only present if the operation completed successfully.
    """

    def __init__(self,
        *,
        output_url : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["output_url",b"output_url"]) -> None: ...
global___ExportEntitiesResponse = ExportEntitiesResponse

class ExportEntitiesMetadata(google.protobuf.message.Message):
    """Metadata for ExportEntities operations."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    COMMON_FIELD_NUMBER: builtins.int
    PROGRESS_ENTITIES_FIELD_NUMBER: builtins.int
    PROGRESS_BYTES_FIELD_NUMBER: builtins.int
    ENTITY_FILTER_FIELD_NUMBER: builtins.int
    OUTPUT_URL_PREFIX_FIELD_NUMBER: builtins.int
    @property
    def common(self) -> global___CommonMetadata:
        """Metadata common to all Datastore Admin operations."""
        pass
    @property
    def progress_entities(self) -> global___Progress:
        """An estimate of the number of entities processed."""
        pass
    @property
    def progress_bytes(self) -> global___Progress:
        """An estimate of the number of bytes processed."""
        pass
    @property
    def entity_filter(self) -> global___EntityFilter:
        """Description of which entities are being exported."""
        pass
    output_url_prefix: typing.Text = ...
    """Location for the export metadata and data files. This will be the same
    value as the
    [google.datastore.admin.v1.ExportEntitiesRequest.output_url_prefix][google.datastore.admin.v1.ExportEntitiesRequest.output_url_prefix]
    field. The final output location is provided in
    [google.datastore.admin.v1.ExportEntitiesResponse.output_url][google.datastore.admin.v1.ExportEntitiesResponse.output_url].
    """

    def __init__(self,
        *,
        common : typing.Optional[global___CommonMetadata] = ...,
        progress_entities : typing.Optional[global___Progress] = ...,
        progress_bytes : typing.Optional[global___Progress] = ...,
        entity_filter : typing.Optional[global___EntityFilter] = ...,
        output_url_prefix : typing.Text = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["common",b"common","entity_filter",b"entity_filter","progress_bytes",b"progress_bytes","progress_entities",b"progress_entities"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["common",b"common","entity_filter",b"entity_filter","output_url_prefix",b"output_url_prefix","progress_bytes",b"progress_bytes","progress_entities",b"progress_entities"]) -> None: ...
global___ExportEntitiesMetadata = ExportEntitiesMetadata

class ImportEntitiesMetadata(google.protobuf.message.Message):
    """Metadata for ImportEntities operations."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    COMMON_FIELD_NUMBER: builtins.int
    PROGRESS_ENTITIES_FIELD_NUMBER: builtins.int
    PROGRESS_BYTES_FIELD_NUMBER: builtins.int
    ENTITY_FILTER_FIELD_NUMBER: builtins.int
    INPUT_URL_FIELD_NUMBER: builtins.int
    @property
    def common(self) -> global___CommonMetadata:
        """Metadata common to all Datastore Admin operations."""
        pass
    @property
    def progress_entities(self) -> global___Progress:
        """An estimate of the number of entities processed."""
        pass
    @property
    def progress_bytes(self) -> global___Progress:
        """An estimate of the number of bytes processed."""
        pass
    @property
    def entity_filter(self) -> global___EntityFilter:
        """Description of which entities are being imported."""
        pass
    input_url: typing.Text = ...
    """The location of the import metadata file. This will be the same value as
    the [google.datastore.admin.v1.ExportEntitiesResponse.output_url][google.datastore.admin.v1.ExportEntitiesResponse.output_url] field.
    """

    def __init__(self,
        *,
        common : typing.Optional[global___CommonMetadata] = ...,
        progress_entities : typing.Optional[global___Progress] = ...,
        progress_bytes : typing.Optional[global___Progress] = ...,
        entity_filter : typing.Optional[global___EntityFilter] = ...,
        input_url : typing.Text = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["common",b"common","entity_filter",b"entity_filter","progress_bytes",b"progress_bytes","progress_entities",b"progress_entities"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["common",b"common","entity_filter",b"entity_filter","input_url",b"input_url","progress_bytes",b"progress_bytes","progress_entities",b"progress_entities"]) -> None: ...
global___ImportEntitiesMetadata = ImportEntitiesMetadata

class EntityFilter(google.protobuf.message.Message):
    """Identifies a subset of entities in a project. This is specified as
    combinations of kinds and namespaces (either or both of which may be all, as
    described in the following examples).
    Example usage:

    Entire project:
      kinds=[], namespace_ids=[]

    Kinds Foo and Bar in all namespaces:
      kinds=['Foo', 'Bar'], namespace_ids=[]

    Kinds Foo and Bar only in the default namespace:
      kinds=['Foo', 'Bar'], namespace_ids=['']

    Kinds Foo and Bar in both the default and Baz namespaces:
      kinds=['Foo', 'Bar'], namespace_ids=['', 'Baz']

    The entire Baz namespace:
      kinds=[], namespace_ids=['Baz']
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    KINDS_FIELD_NUMBER: builtins.int
    NAMESPACE_IDS_FIELD_NUMBER: builtins.int
    @property
    def kinds(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]:
        """If empty, then this represents all kinds."""
        pass
    @property
    def namespace_ids(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]:
        """An empty list represents all namespaces. This is the preferred
        usage for projects that don't use namespaces.

        An empty string element represents the default namespace. This should be
        used if the project has data in non-default namespaces, but doesn't want to
        include them.
        Each namespace in this list must be unique.
        """
        pass
    def __init__(self,
        *,
        kinds : typing.Optional[typing.Iterable[typing.Text]] = ...,
        namespace_ids : typing.Optional[typing.Iterable[typing.Text]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["kinds",b"kinds","namespace_ids",b"namespace_ids"]) -> None: ...
global___EntityFilter = EntityFilter

class CreateIndexRequest(google.protobuf.message.Message):
    """The request for
    [google.datastore.admin.v1.DatastoreAdmin.CreateIndex][google.datastore.admin.v1.DatastoreAdmin.CreateIndex].
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    PROJECT_ID_FIELD_NUMBER: builtins.int
    INDEX_FIELD_NUMBER: builtins.int
    project_id: typing.Text = ...
    """Project ID against which to make the request."""

    @property
    def index(self) -> google.datastore.admin.v1.index_pb2.Index:
        """The index to create. The name and state fields are output only and will be
        ignored. Single property indexes cannot be created or deleted.
        """
        pass
    def __init__(self,
        *,
        project_id : typing.Text = ...,
        index : typing.Optional[google.datastore.admin.v1.index_pb2.Index] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["index",b"index"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["index",b"index","project_id",b"project_id"]) -> None: ...
global___CreateIndexRequest = CreateIndexRequest

class DeleteIndexRequest(google.protobuf.message.Message):
    """The request for
    [google.datastore.admin.v1.DatastoreAdmin.DeleteIndex][google.datastore.admin.v1.DatastoreAdmin.DeleteIndex].
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    PROJECT_ID_FIELD_NUMBER: builtins.int
    INDEX_ID_FIELD_NUMBER: builtins.int
    project_id: typing.Text = ...
    """Project ID against which to make the request."""

    index_id: typing.Text = ...
    """The resource ID of the index to delete."""

    def __init__(self,
        *,
        project_id : typing.Text = ...,
        index_id : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["index_id",b"index_id","project_id",b"project_id"]) -> None: ...
global___DeleteIndexRequest = DeleteIndexRequest

class GetIndexRequest(google.protobuf.message.Message):
    """The request for [google.datastore.admin.v1.DatastoreAdmin.GetIndex][google.datastore.admin.v1.DatastoreAdmin.GetIndex]."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    PROJECT_ID_FIELD_NUMBER: builtins.int
    INDEX_ID_FIELD_NUMBER: builtins.int
    project_id: typing.Text = ...
    """Project ID against which to make the request."""

    index_id: typing.Text = ...
    """The resource ID of the index to get."""

    def __init__(self,
        *,
        project_id : typing.Text = ...,
        index_id : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["index_id",b"index_id","project_id",b"project_id"]) -> None: ...
global___GetIndexRequest = GetIndexRequest

class ListIndexesRequest(google.protobuf.message.Message):
    """The request for
    [google.datastore.admin.v1.DatastoreAdmin.ListIndexes][google.datastore.admin.v1.DatastoreAdmin.ListIndexes].
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    PROJECT_ID_FIELD_NUMBER: builtins.int
    FILTER_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    project_id: typing.Text = ...
    """Project ID against which to make the request."""

    filter: typing.Text = ...
    page_size: builtins.int = ...
    """The maximum number of items to return.  If zero, then all results will be
    returned.
    """

    page_token: typing.Text = ...
    """The next_page_token value returned from a previous List request, if any."""

    def __init__(self,
        *,
        project_id : typing.Text = ...,
        filter : typing.Text = ...,
        page_size : builtins.int = ...,
        page_token : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["filter",b"filter","page_size",b"page_size","page_token",b"page_token","project_id",b"project_id"]) -> None: ...
global___ListIndexesRequest = ListIndexesRequest

class ListIndexesResponse(google.protobuf.message.Message):
    """The response for
    [google.datastore.admin.v1.DatastoreAdmin.ListIndexes][google.datastore.admin.v1.DatastoreAdmin.ListIndexes].
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    INDEXES_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    @property
    def indexes(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[google.datastore.admin.v1.index_pb2.Index]:
        """The indexes."""
        pass
    next_page_token: typing.Text = ...
    """The standard List next-page token."""

    def __init__(self,
        *,
        indexes : typing.Optional[typing.Iterable[google.datastore.admin.v1.index_pb2.Index]] = ...,
        next_page_token : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["indexes",b"indexes","next_page_token",b"next_page_token"]) -> None: ...
global___ListIndexesResponse = ListIndexesResponse

class IndexOperationMetadata(google.protobuf.message.Message):
    """Metadata for Index operations."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    COMMON_FIELD_NUMBER: builtins.int
    PROGRESS_ENTITIES_FIELD_NUMBER: builtins.int
    INDEX_ID_FIELD_NUMBER: builtins.int
    @property
    def common(self) -> global___CommonMetadata:
        """Metadata common to all Datastore Admin operations."""
        pass
    @property
    def progress_entities(self) -> global___Progress:
        """An estimate of the number of entities processed."""
        pass
    index_id: typing.Text = ...
    """The index resource ID that this operation is acting on."""

    def __init__(self,
        *,
        common : typing.Optional[global___CommonMetadata] = ...,
        progress_entities : typing.Optional[global___Progress] = ...,
        index_id : typing.Text = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["common",b"common","progress_entities",b"progress_entities"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["common",b"common","index_id",b"index_id","progress_entities",b"progress_entities"]) -> None: ...
global___IndexOperationMetadata = IndexOperationMetadata

class DatastoreFirestoreMigrationMetadata(google.protobuf.message.Message):
    """Metadata for Datastore to Firestore migration operations.

    The DatastoreFirestoreMigration operation is not started by the end-user via
    an explicit "creation" method. This is an intentional deviation from the LRO
    design pattern.

    This singleton resource can be accessed at:
    `projects/{project_id}/datastore-firestore-migration`
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    MIGRATION_STATE_FIELD_NUMBER: builtins.int
    MIGRATION_STEP_FIELD_NUMBER: builtins.int
    migration_state: google.datastore.admin.v1.migration_pb2.MigrationState.ValueType = ...
    """The current state of migration from Cloud Datastore to Cloud Firestore in
    Datastore mode.
    """

    migration_step: google.datastore.admin.v1.migration_pb2.MigrationStep.ValueType = ...
    """The current step of migration from Cloud Datastore to Cloud Firestore in
    Datastore mode.
    """

    def __init__(self,
        *,
        migration_state : google.datastore.admin.v1.migration_pb2.MigrationState.ValueType = ...,
        migration_step : google.datastore.admin.v1.migration_pb2.MigrationStep.ValueType = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["migration_state",b"migration_state","migration_step",b"migration_step"]) -> None: ...
global___DatastoreFirestoreMigrationMetadata = DatastoreFirestoreMigrationMetadata
