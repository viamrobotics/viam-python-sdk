"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.ads.googleads.v8.enums.response_content_type_pb2
import google.ads.googleads.v8.resources.batch_job_pb2
import google.ads.googleads.v8.services.google_ads_service_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import google.rpc.status_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class MutateBatchJobRequest(google.protobuf.message.Message):
    """Request message for [BatchJobService.MutateBatchJob][google.ads.googleads.v8.services.BatchJobService.MutateBatchJob]."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    CUSTOMER_ID_FIELD_NUMBER: builtins.int
    OPERATION_FIELD_NUMBER: builtins.int
    customer_id: typing.Text = ...
    """Required. The ID of the customer for which to create a batch job."""

    @property
    def operation(self) -> global___BatchJobOperation:
        """Required. The operation to perform on an individual batch job."""
        pass
    def __init__(self,
        *,
        customer_id : typing.Text = ...,
        operation : typing.Optional[global___BatchJobOperation] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["operation",b"operation"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["customer_id",b"customer_id","operation",b"operation"]) -> None: ...
global___MutateBatchJobRequest = MutateBatchJobRequest

class BatchJobOperation(google.protobuf.message.Message):
    """A single operation on a batch job."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    CREATE_FIELD_NUMBER: builtins.int
    @property
    def create(self) -> google.ads.googleads.v8.resources.batch_job_pb2.BatchJob:
        """Create operation: No resource name is expected for the new batch job."""
        pass
    def __init__(self,
        *,
        create : typing.Optional[google.ads.googleads.v8.resources.batch_job_pb2.BatchJob] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["create",b"create","operation",b"operation"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["create",b"create","operation",b"operation"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["operation",b"operation"]) -> typing.Optional[typing_extensions.Literal["create"]]: ...
global___BatchJobOperation = BatchJobOperation

class MutateBatchJobResponse(google.protobuf.message.Message):
    """Response message for [BatchJobService.MutateBatchJob][google.ads.googleads.v8.services.BatchJobService.MutateBatchJob]."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    RESULT_FIELD_NUMBER: builtins.int
    @property
    def result(self) -> global___MutateBatchJobResult:
        """The result for the mutate."""
        pass
    def __init__(self,
        *,
        result : typing.Optional[global___MutateBatchJobResult] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["result",b"result"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["result",b"result"]) -> None: ...
global___MutateBatchJobResponse = MutateBatchJobResponse

class MutateBatchJobResult(google.protobuf.message.Message):
    """The result for the batch job mutate."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    RESOURCE_NAME_FIELD_NUMBER: builtins.int
    resource_name: typing.Text = ...
    """The resource name of the batch job."""

    def __init__(self,
        *,
        resource_name : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["resource_name",b"resource_name"]) -> None: ...
global___MutateBatchJobResult = MutateBatchJobResult

class GetBatchJobRequest(google.protobuf.message.Message):
    """Request message for [BatchJobService.GetBatchJob][google.ads.googleads.v8.services.BatchJobService.GetBatchJob]."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    RESOURCE_NAME_FIELD_NUMBER: builtins.int
    resource_name: typing.Text = ...
    """Required. The resource name of the batch job to get."""

    def __init__(self,
        *,
        resource_name : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["resource_name",b"resource_name"]) -> None: ...
global___GetBatchJobRequest = GetBatchJobRequest

class RunBatchJobRequest(google.protobuf.message.Message):
    """Request message for [BatchJobService.RunBatchJob][google.ads.googleads.v8.services.BatchJobService.RunBatchJob]."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    RESOURCE_NAME_FIELD_NUMBER: builtins.int
    resource_name: typing.Text = ...
    """Required. The resource name of the BatchJob to run."""

    def __init__(self,
        *,
        resource_name : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["resource_name",b"resource_name"]) -> None: ...
global___RunBatchJobRequest = RunBatchJobRequest

class AddBatchJobOperationsRequest(google.protobuf.message.Message):
    """Request message for [BatchJobService.AddBatchJobOperations][google.ads.googleads.v8.services.BatchJobService.AddBatchJobOperations]."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    RESOURCE_NAME_FIELD_NUMBER: builtins.int
    SEQUENCE_TOKEN_FIELD_NUMBER: builtins.int
    MUTATE_OPERATIONS_FIELD_NUMBER: builtins.int
    resource_name: typing.Text = ...
    """Required. The resource name of the batch job."""

    sequence_token: typing.Text = ...
    """A token used to enforce sequencing.

    The first AddBatchJobOperations request for a batch job should not set
    sequence_token. Subsequent requests must set sequence_token to the value of
    next_sequence_token received in the previous AddBatchJobOperations
    response.
    """

    @property
    def mutate_operations(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[google.ads.googleads.v8.services.google_ads_service_pb2.MutateOperation]:
        """Required. The list of mutates being added.

        Operations can use negative integers as temp ids to signify dependencies
        between entities created in this batch job. For example, a customer with
        id = 1234 can create a campaign and an ad group in that same campaign by
        creating a campaign in the first operation with the resource name
        explicitly set to "customers/1234/campaigns/-1", and creating an ad group
        in the second operation with the campaign field also set to
        "customers/1234/campaigns/-1".
        """
        pass
    def __init__(self,
        *,
        resource_name : typing.Text = ...,
        sequence_token : typing.Text = ...,
        mutate_operations : typing.Optional[typing.Iterable[google.ads.googleads.v8.services.google_ads_service_pb2.MutateOperation]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["mutate_operations",b"mutate_operations","resource_name",b"resource_name","sequence_token",b"sequence_token"]) -> None: ...
global___AddBatchJobOperationsRequest = AddBatchJobOperationsRequest

class AddBatchJobOperationsResponse(google.protobuf.message.Message):
    """Response message for [BatchJobService.AddBatchJobOperations][google.ads.googleads.v8.services.BatchJobService.AddBatchJobOperations]."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    TOTAL_OPERATIONS_FIELD_NUMBER: builtins.int
    NEXT_SEQUENCE_TOKEN_FIELD_NUMBER: builtins.int
    total_operations: builtins.int = ...
    """The total number of operations added so far for this batch job."""

    next_sequence_token: typing.Text = ...
    """The sequence token to be used when calling AddBatchJobOperations again if
    more operations need to be added. The next AddBatchJobOperations request
    must set the sequence_token field to the value of this field.
    """

    def __init__(self,
        *,
        total_operations : builtins.int = ...,
        next_sequence_token : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["next_sequence_token",b"next_sequence_token","total_operations",b"total_operations"]) -> None: ...
global___AddBatchJobOperationsResponse = AddBatchJobOperationsResponse

class ListBatchJobResultsRequest(google.protobuf.message.Message):
    """Request message for [BatchJobService.ListBatchJobResults][google.ads.googleads.v8.services.BatchJobService.ListBatchJobResults]."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    RESOURCE_NAME_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    RESPONSE_CONTENT_TYPE_FIELD_NUMBER: builtins.int
    resource_name: typing.Text = ...
    """Required. The resource name of the batch job whose results are being listed."""

    page_token: typing.Text = ...
    """Token of the page to retrieve. If not specified, the first
    page of results will be returned. Use the value obtained from
    `next_page_token` in the previous response in order to request
    the next page of results.
    """

    page_size: builtins.int = ...
    """Number of elements to retrieve in a single page.
    When a page request is too large, the server may decide to
    further limit the number of returned resources.
    """

    response_content_type: google.ads.googleads.v8.enums.response_content_type_pb2.ResponseContentTypeEnum.ResponseContentType.ValueType = ...
    """The response content type setting. Determines whether the mutable resource
    or just the resource name should be returned.
    """

    def __init__(self,
        *,
        resource_name : typing.Text = ...,
        page_token : typing.Text = ...,
        page_size : builtins.int = ...,
        response_content_type : google.ads.googleads.v8.enums.response_content_type_pb2.ResponseContentTypeEnum.ResponseContentType.ValueType = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["page_size",b"page_size","page_token",b"page_token","resource_name",b"resource_name","response_content_type",b"response_content_type"]) -> None: ...
global___ListBatchJobResultsRequest = ListBatchJobResultsRequest

class ListBatchJobResultsResponse(google.protobuf.message.Message):
    """Response message for [BatchJobService.ListBatchJobResults][google.ads.googleads.v8.services.BatchJobService.ListBatchJobResults]."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    RESULTS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    @property
    def results(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___BatchJobResult]:
        """The list of rows that matched the query."""
        pass
    next_page_token: typing.Text = ...
    """Pagination token used to retrieve the next page of results.
    Pass the content of this string as the `page_token` attribute of
    the next request. `next_page_token` is not returned for the last
    page.
    """

    def __init__(self,
        *,
        results : typing.Optional[typing.Iterable[global___BatchJobResult]] = ...,
        next_page_token : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["next_page_token",b"next_page_token","results",b"results"]) -> None: ...
global___ListBatchJobResultsResponse = ListBatchJobResultsResponse

class BatchJobResult(google.protobuf.message.Message):
    """An individual batch job result."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    OPERATION_INDEX_FIELD_NUMBER: builtins.int
    MUTATE_OPERATION_RESPONSE_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    operation_index: builtins.int = ...
    """Index of the mutate operation."""

    @property
    def mutate_operation_response(self) -> google.ads.googleads.v8.services.google_ads_service_pb2.MutateOperationResponse:
        """Response for the mutate.
        May be empty if errors occurred.
        """
        pass
    @property
    def status(self) -> google.rpc.status_pb2.Status:
        """Details of the errors when processing the operation."""
        pass
    def __init__(self,
        *,
        operation_index : builtins.int = ...,
        mutate_operation_response : typing.Optional[google.ads.googleads.v8.services.google_ads_service_pb2.MutateOperationResponse] = ...,
        status : typing.Optional[google.rpc.status_pb2.Status] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["mutate_operation_response",b"mutate_operation_response","status",b"status"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["mutate_operation_response",b"mutate_operation_response","operation_index",b"operation_index","status",b"status"]) -> None: ...
global___BatchJobResult = BatchJobResult
