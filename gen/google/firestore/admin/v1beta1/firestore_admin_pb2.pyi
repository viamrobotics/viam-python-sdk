"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.firestore.admin.v1beta1.index_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import google.protobuf.timestamp_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class _OperationState:
    ValueType = typing.NewType('ValueType', builtins.int)
    V: typing_extensions.TypeAlias = ValueType
class _OperationStateEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_OperationState.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
    STATE_UNSPECIFIED: OperationState.ValueType = ...  # 0
    """Unspecified."""

    INITIALIZING: OperationState.ValueType = ...  # 1
    """Request is being prepared for processing."""

    PROCESSING: OperationState.ValueType = ...  # 2
    """Request is actively being processed."""

    CANCELLING: OperationState.ValueType = ...  # 3
    """Request is in the process of being cancelled after user called
    google.longrunning.Operations.CancelOperation on the operation.
    """

    FINALIZING: OperationState.ValueType = ...  # 4
    """Request has been processed and is in its finalization stage."""

    SUCCESSFUL: OperationState.ValueType = ...  # 5
    """Request has completed successfully."""

    FAILED: OperationState.ValueType = ...  # 6
    """Request has finished being processed, but encountered an error."""

    CANCELLED: OperationState.ValueType = ...  # 7
    """Request has finished being cancelled after user called
    google.longrunning.Operations.CancelOperation.
    """

class OperationState(_OperationState, metaclass=_OperationStateEnumTypeWrapper):
    """The various possible states for an ongoing Operation."""
    pass

STATE_UNSPECIFIED: OperationState.ValueType = ...  # 0
"""Unspecified."""

INITIALIZING: OperationState.ValueType = ...  # 1
"""Request is being prepared for processing."""

PROCESSING: OperationState.ValueType = ...  # 2
"""Request is actively being processed."""

CANCELLING: OperationState.ValueType = ...  # 3
"""Request is in the process of being cancelled after user called
google.longrunning.Operations.CancelOperation on the operation.
"""

FINALIZING: OperationState.ValueType = ...  # 4
"""Request has been processed and is in its finalization stage."""

SUCCESSFUL: OperationState.ValueType = ...  # 5
"""Request has completed successfully."""

FAILED: OperationState.ValueType = ...  # 6
"""Request has finished being processed, but encountered an error."""

CANCELLED: OperationState.ValueType = ...  # 7
"""Request has finished being cancelled after user called
google.longrunning.Operations.CancelOperation.
"""

global___OperationState = OperationState


class IndexOperationMetadata(google.protobuf.message.Message):
    """Metadata for index operations. This metadata populates
    the metadata field of [google.longrunning.Operation][google.longrunning.Operation].
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class _OperationType:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _OperationTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_OperationType.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        OPERATION_TYPE_UNSPECIFIED: IndexOperationMetadata.OperationType.ValueType = ...  # 0
        """Unspecified. Never set by server."""

        CREATING_INDEX: IndexOperationMetadata.OperationType.ValueType = ...  # 1
        """The operation is creating the index. Initiated by a `CreateIndex` call."""

    class OperationType(_OperationType, metaclass=_OperationTypeEnumTypeWrapper):
        """The type of index operation."""
        pass

    OPERATION_TYPE_UNSPECIFIED: IndexOperationMetadata.OperationType.ValueType = ...  # 0
    """Unspecified. Never set by server."""

    CREATING_INDEX: IndexOperationMetadata.OperationType.ValueType = ...  # 1
    """The operation is creating the index. Initiated by a `CreateIndex` call."""


    START_TIME_FIELD_NUMBER: builtins.int
    END_TIME_FIELD_NUMBER: builtins.int
    INDEX_FIELD_NUMBER: builtins.int
    OPERATION_TYPE_FIELD_NUMBER: builtins.int
    CANCELLED_FIELD_NUMBER: builtins.int
    DOCUMENT_PROGRESS_FIELD_NUMBER: builtins.int
    @property
    def start_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """The time that work began on the operation."""
        pass
    @property
    def end_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """The time the operation ended, either successfully or otherwise. Unset if
        the operation is still active.
        """
        pass
    index: typing.Text = ...
    """The index resource that this operation is acting on. For example:
    `projects/{project_id}/databases/{database_id}/indexes/{index_id}`
    """

    operation_type: global___IndexOperationMetadata.OperationType.ValueType = ...
    """The type of index operation."""

    cancelled: builtins.bool = ...
    """True if the [google.longrunning.Operation] was cancelled. If the
    cancellation is in progress, cancelled will be true but
    [google.longrunning.Operation.done][google.longrunning.Operation.done] will be false.
    """

    @property
    def document_progress(self) -> global___Progress:
        """Progress of the existing operation, measured in number of documents."""
        pass
    def __init__(self,
        *,
        start_time : typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        end_time : typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        index : typing.Text = ...,
        operation_type : global___IndexOperationMetadata.OperationType.ValueType = ...,
        cancelled : builtins.bool = ...,
        document_progress : typing.Optional[global___Progress] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["document_progress",b"document_progress","end_time",b"end_time","start_time",b"start_time"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["cancelled",b"cancelled","document_progress",b"document_progress","end_time",b"end_time","index",b"index","operation_type",b"operation_type","start_time",b"start_time"]) -> None: ...
global___IndexOperationMetadata = IndexOperationMetadata

class Progress(google.protobuf.message.Message):
    """Measures the progress of a particular metric."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    WORK_COMPLETED_FIELD_NUMBER: builtins.int
    WORK_ESTIMATED_FIELD_NUMBER: builtins.int
    work_completed: builtins.int = ...
    """An estimate of how much work has been completed. Note that this may be
    greater than `work_estimated`.
    """

    work_estimated: builtins.int = ...
    """An estimate of how much work needs to be performed. Zero if the
    work estimate is unavailable. May change as work progresses.
    """

    def __init__(self,
        *,
        work_completed : builtins.int = ...,
        work_estimated : builtins.int = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["work_completed",b"work_completed","work_estimated",b"work_estimated"]) -> None: ...
global___Progress = Progress

class CreateIndexRequest(google.protobuf.message.Message):
    """The request for [FirestoreAdmin.CreateIndex][google.firestore.admin.v1beta1.FirestoreAdmin.CreateIndex]."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    PARENT_FIELD_NUMBER: builtins.int
    INDEX_FIELD_NUMBER: builtins.int
    parent: typing.Text = ...
    """The name of the database this index will apply to. For example:
    `projects/{project_id}/databases/{database_id}`
    """

    @property
    def index(self) -> google.firestore.admin.v1beta1.index_pb2.Index:
        """The index to create. The name and state fields are output only and will be
        ignored. Certain single field indexes cannot be created or deleted.
        """
        pass
    def __init__(self,
        *,
        parent : typing.Text = ...,
        index : typing.Optional[google.firestore.admin.v1beta1.index_pb2.Index] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["index",b"index"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["index",b"index","parent",b"parent"]) -> None: ...
global___CreateIndexRequest = CreateIndexRequest

class GetIndexRequest(google.protobuf.message.Message):
    """The request for [FirestoreAdmin.GetIndex][google.firestore.admin.v1beta1.FirestoreAdmin.GetIndex]."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    """The name of the index. For example:
    `projects/{project_id}/databases/{database_id}/indexes/{index_id}`
    """

    def __init__(self,
        *,
        name : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["name",b"name"]) -> None: ...
global___GetIndexRequest = GetIndexRequest

class ListIndexesRequest(google.protobuf.message.Message):
    """The request for [FirestoreAdmin.ListIndexes][google.firestore.admin.v1beta1.FirestoreAdmin.ListIndexes]."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    PARENT_FIELD_NUMBER: builtins.int
    FILTER_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    parent: typing.Text = ...
    """The database name. For example:
    `projects/{project_id}/databases/{database_id}`
    """

    filter: typing.Text = ...
    page_size: builtins.int = ...
    """The standard List page size."""

    page_token: typing.Text = ...
    """The standard List page token."""

    def __init__(self,
        *,
        parent : typing.Text = ...,
        filter : typing.Text = ...,
        page_size : builtins.int = ...,
        page_token : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["filter",b"filter","page_size",b"page_size","page_token",b"page_token","parent",b"parent"]) -> None: ...
global___ListIndexesRequest = ListIndexesRequest

class DeleteIndexRequest(google.protobuf.message.Message):
    """The request for [FirestoreAdmin.DeleteIndex][google.firestore.admin.v1beta1.FirestoreAdmin.DeleteIndex]."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    """The index name. For example:
    `projects/{project_id}/databases/{database_id}/indexes/{index_id}`
    """

    def __init__(self,
        *,
        name : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["name",b"name"]) -> None: ...
global___DeleteIndexRequest = DeleteIndexRequest

class ListIndexesResponse(google.protobuf.message.Message):
    """The response for [FirestoreAdmin.ListIndexes][google.firestore.admin.v1beta1.FirestoreAdmin.ListIndexes]."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    INDEXES_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    @property
    def indexes(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[google.firestore.admin.v1beta1.index_pb2.Index]:
        """The indexes."""
        pass
    next_page_token: typing.Text = ...
    """The standard List next-page token."""

    def __init__(self,
        *,
        indexes : typing.Optional[typing.Iterable[google.firestore.admin.v1beta1.index_pb2.Index]] = ...,
        next_page_token : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["indexes",b"indexes","next_page_token",b"next_page_token"]) -> None: ...
global___ListIndexesResponse = ListIndexesResponse

class ExportDocumentsRequest(google.protobuf.message.Message):
    """The request for [FirestoreAdmin.ExportDocuments][google.firestore.admin.v1beta1.FirestoreAdmin.ExportDocuments]."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    COLLECTION_IDS_FIELD_NUMBER: builtins.int
    OUTPUT_URI_PREFIX_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    """Database to export. Should be of the form:
    `projects/{project_id}/databases/{database_id}`.
    """

    @property
    def collection_ids(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]:
        """Which collection ids to export. Unspecified means all collections."""
        pass
    output_uri_prefix: typing.Text = ...
    """The output URI. Currently only supports Google Cloud Storage URIs of the
    form: `gs://BUCKET_NAME[/NAMESPACE_PATH]`, where `BUCKET_NAME` is the name
    of the Google Cloud Storage bucket and `NAMESPACE_PATH` is an optional
    Google Cloud Storage namespace path. When
    choosing a name, be sure to consider Google Cloud Storage naming
    guidelines: https://cloud.google.com/storage/docs/naming.
    If the URI is a bucket (without a namespace path), a prefix will be
    generated based on the start time.
    """

    def __init__(self,
        *,
        name : typing.Text = ...,
        collection_ids : typing.Optional[typing.Iterable[typing.Text]] = ...,
        output_uri_prefix : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["collection_ids",b"collection_ids","name",b"name","output_uri_prefix",b"output_uri_prefix"]) -> None: ...
global___ExportDocumentsRequest = ExportDocumentsRequest

class ImportDocumentsRequest(google.protobuf.message.Message):
    """The request for [FirestoreAdmin.ImportDocuments][google.firestore.admin.v1beta1.FirestoreAdmin.ImportDocuments]."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    COLLECTION_IDS_FIELD_NUMBER: builtins.int
    INPUT_URI_PREFIX_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    """Database to import into. Should be of the form:
    `projects/{project_id}/databases/{database_id}`.
    """

    @property
    def collection_ids(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]:
        """Which collection ids to import. Unspecified means all collections included
        in the import.
        """
        pass
    input_uri_prefix: typing.Text = ...
    """Location of the exported files.
    This must match the output_uri_prefix of an ExportDocumentsResponse from
    an export that has completed successfully.
    See:
    [google.firestore.admin.v1beta1.ExportDocumentsResponse.output_uri_prefix][google.firestore.admin.v1beta1.ExportDocumentsResponse.output_uri_prefix].
    """

    def __init__(self,
        *,
        name : typing.Text = ...,
        collection_ids : typing.Optional[typing.Iterable[typing.Text]] = ...,
        input_uri_prefix : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["collection_ids",b"collection_ids","input_uri_prefix",b"input_uri_prefix","name",b"name"]) -> None: ...
global___ImportDocumentsRequest = ImportDocumentsRequest

class ExportDocumentsResponse(google.protobuf.message.Message):
    """Returned in the [google.longrunning.Operation][google.longrunning.Operation] response field."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    OUTPUT_URI_PREFIX_FIELD_NUMBER: builtins.int
    output_uri_prefix: typing.Text = ...
    """Location of the output files. This can be used to begin an import
    into Cloud Firestore (this project or another project) after the operation
    completes successfully.
    """

    def __init__(self,
        *,
        output_uri_prefix : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["output_uri_prefix",b"output_uri_prefix"]) -> None: ...
global___ExportDocumentsResponse = ExportDocumentsResponse

class ExportDocumentsMetadata(google.protobuf.message.Message):
    """Metadata for ExportDocuments operations."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    START_TIME_FIELD_NUMBER: builtins.int
    END_TIME_FIELD_NUMBER: builtins.int
    OPERATION_STATE_FIELD_NUMBER: builtins.int
    PROGRESS_DOCUMENTS_FIELD_NUMBER: builtins.int
    PROGRESS_BYTES_FIELD_NUMBER: builtins.int
    COLLECTION_IDS_FIELD_NUMBER: builtins.int
    OUTPUT_URI_PREFIX_FIELD_NUMBER: builtins.int
    @property
    def start_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """The time that work began on the operation."""
        pass
    @property
    def end_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """The time the operation ended, either successfully or otherwise. Unset if
        the operation is still active.
        """
        pass
    operation_state: global___OperationState.ValueType = ...
    """The state of the export operation."""

    @property
    def progress_documents(self) -> global___Progress:
        """An estimate of the number of documents processed."""
        pass
    @property
    def progress_bytes(self) -> global___Progress:
        """An estimate of the number of bytes processed."""
        pass
    @property
    def collection_ids(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]:
        """Which collection ids are being exported."""
        pass
    output_uri_prefix: typing.Text = ...
    """Where the entities are being exported to."""

    def __init__(self,
        *,
        start_time : typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        end_time : typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        operation_state : global___OperationState.ValueType = ...,
        progress_documents : typing.Optional[global___Progress] = ...,
        progress_bytes : typing.Optional[global___Progress] = ...,
        collection_ids : typing.Optional[typing.Iterable[typing.Text]] = ...,
        output_uri_prefix : typing.Text = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["end_time",b"end_time","progress_bytes",b"progress_bytes","progress_documents",b"progress_documents","start_time",b"start_time"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["collection_ids",b"collection_ids","end_time",b"end_time","operation_state",b"operation_state","output_uri_prefix",b"output_uri_prefix","progress_bytes",b"progress_bytes","progress_documents",b"progress_documents","start_time",b"start_time"]) -> None: ...
global___ExportDocumentsMetadata = ExportDocumentsMetadata

class ImportDocumentsMetadata(google.protobuf.message.Message):
    """Metadata for ImportDocuments operations."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    START_TIME_FIELD_NUMBER: builtins.int
    END_TIME_FIELD_NUMBER: builtins.int
    OPERATION_STATE_FIELD_NUMBER: builtins.int
    PROGRESS_DOCUMENTS_FIELD_NUMBER: builtins.int
    PROGRESS_BYTES_FIELD_NUMBER: builtins.int
    COLLECTION_IDS_FIELD_NUMBER: builtins.int
    INPUT_URI_PREFIX_FIELD_NUMBER: builtins.int
    @property
    def start_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """The time that work began on the operation."""
        pass
    @property
    def end_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """The time the operation ended, either successfully or otherwise. Unset if
        the operation is still active.
        """
        pass
    operation_state: global___OperationState.ValueType = ...
    """The state of the import operation."""

    @property
    def progress_documents(self) -> global___Progress:
        """An estimate of the number of documents processed."""
        pass
    @property
    def progress_bytes(self) -> global___Progress:
        """An estimate of the number of bytes processed."""
        pass
    @property
    def collection_ids(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]:
        """Which collection ids are being imported."""
        pass
    input_uri_prefix: typing.Text = ...
    """The location of the documents being imported."""

    def __init__(self,
        *,
        start_time : typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        end_time : typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        operation_state : global___OperationState.ValueType = ...,
        progress_documents : typing.Optional[global___Progress] = ...,
        progress_bytes : typing.Optional[global___Progress] = ...,
        collection_ids : typing.Optional[typing.Iterable[typing.Text]] = ...,
        input_uri_prefix : typing.Text = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["end_time",b"end_time","progress_bytes",b"progress_bytes","progress_documents",b"progress_documents","start_time",b"start_time"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["collection_ids",b"collection_ids","end_time",b"end_time","input_uri_prefix",b"input_uri_prefix","operation_state",b"operation_state","progress_bytes",b"progress_bytes","progress_documents",b"progress_documents","start_time",b"start_time"]) -> None: ...
global___ImportDocumentsMetadata = ImportDocumentsMetadata
