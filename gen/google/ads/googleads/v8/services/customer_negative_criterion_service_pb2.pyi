"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.ads.googleads.v8.enums.response_content_type_pb2
import google.ads.googleads.v8.resources.customer_negative_criterion_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import google.rpc.status_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class GetCustomerNegativeCriterionRequest(google.protobuf.message.Message):
    """Request message for
    [CustomerNegativeCriterionService.GetCustomerNegativeCriterion][google.ads.googleads.v8.services.CustomerNegativeCriterionService.GetCustomerNegativeCriterion].
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    RESOURCE_NAME_FIELD_NUMBER: builtins.int
    resource_name: typing.Text = ...
    """Required. The resource name of the criterion to fetch."""

    def __init__(self,
        *,
        resource_name : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["resource_name",b"resource_name"]) -> None: ...
global___GetCustomerNegativeCriterionRequest = GetCustomerNegativeCriterionRequest

class MutateCustomerNegativeCriteriaRequest(google.protobuf.message.Message):
    """Request message for
    [CustomerNegativeCriterionService.MutateCustomerNegativeCriteria][google.ads.googleads.v8.services.CustomerNegativeCriterionService.MutateCustomerNegativeCriteria].
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    CUSTOMER_ID_FIELD_NUMBER: builtins.int
    OPERATIONS_FIELD_NUMBER: builtins.int
    PARTIAL_FAILURE_FIELD_NUMBER: builtins.int
    VALIDATE_ONLY_FIELD_NUMBER: builtins.int
    RESPONSE_CONTENT_TYPE_FIELD_NUMBER: builtins.int
    customer_id: typing.Text = ...
    """Required. The ID of the customer whose criteria are being modified."""

    @property
    def operations(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___CustomerNegativeCriterionOperation]:
        """Required. The list of operations to perform on individual criteria."""
        pass
    partial_failure: builtins.bool = ...
    """If true, successful operations will be carried out and invalid
    operations will return errors. If false, all operations will be carried
    out in one transaction if and only if they are all valid.
    Default is false.
    """

    validate_only: builtins.bool = ...
    """If true, the request is validated but not executed. Only errors are
    returned, not results.
    """

    response_content_type: google.ads.googleads.v8.enums.response_content_type_pb2.ResponseContentTypeEnum.ResponseContentType.ValueType = ...
    """The response content type setting. Determines whether the mutable resource
    or just the resource name should be returned post mutation.
    """

    def __init__(self,
        *,
        customer_id : typing.Text = ...,
        operations : typing.Optional[typing.Iterable[global___CustomerNegativeCriterionOperation]] = ...,
        partial_failure : builtins.bool = ...,
        validate_only : builtins.bool = ...,
        response_content_type : google.ads.googleads.v8.enums.response_content_type_pb2.ResponseContentTypeEnum.ResponseContentType.ValueType = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["customer_id",b"customer_id","operations",b"operations","partial_failure",b"partial_failure","response_content_type",b"response_content_type","validate_only",b"validate_only"]) -> None: ...
global___MutateCustomerNegativeCriteriaRequest = MutateCustomerNegativeCriteriaRequest

class CustomerNegativeCriterionOperation(google.protobuf.message.Message):
    """A single operation (create or remove) on a customer level negative criterion."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    CREATE_FIELD_NUMBER: builtins.int
    REMOVE_FIELD_NUMBER: builtins.int
    @property
    def create(self) -> google.ads.googleads.v8.resources.customer_negative_criterion_pb2.CustomerNegativeCriterion:
        """Create operation: No resource name is expected for the new criterion."""
        pass
    remove: typing.Text = ...
    """Remove operation: A resource name for the removed criterion is expected,
    in this format:

    `customers/{customer_id}/customerNegativeCriteria/{criterion_id}`
    """

    def __init__(self,
        *,
        create : typing.Optional[google.ads.googleads.v8.resources.customer_negative_criterion_pb2.CustomerNegativeCriterion] = ...,
        remove : typing.Text = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["create",b"create","operation",b"operation","remove",b"remove"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["create",b"create","operation",b"operation","remove",b"remove"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["operation",b"operation"]) -> typing.Optional[typing_extensions.Literal["create","remove"]]: ...
global___CustomerNegativeCriterionOperation = CustomerNegativeCriterionOperation

class MutateCustomerNegativeCriteriaResponse(google.protobuf.message.Message):
    """Response message for customer negative criterion mutate."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    PARTIAL_FAILURE_ERROR_FIELD_NUMBER: builtins.int
    RESULTS_FIELD_NUMBER: builtins.int
    @property
    def partial_failure_error(self) -> google.rpc.status_pb2.Status:
        """Errors that pertain to operation failures in the partial failure mode.
        Returned only when partial_failure = true and all errors occur inside the
        operations. If any errors occur outside the operations (e.g. auth errors),
        we return an RPC level error.
        """
        pass
    @property
    def results(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___MutateCustomerNegativeCriteriaResult]:
        """All results for the mutate."""
        pass
    def __init__(self,
        *,
        partial_failure_error : typing.Optional[google.rpc.status_pb2.Status] = ...,
        results : typing.Optional[typing.Iterable[global___MutateCustomerNegativeCriteriaResult]] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["partial_failure_error",b"partial_failure_error"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["partial_failure_error",b"partial_failure_error","results",b"results"]) -> None: ...
global___MutateCustomerNegativeCriteriaResponse = MutateCustomerNegativeCriteriaResponse

class MutateCustomerNegativeCriteriaResult(google.protobuf.message.Message):
    """The result for the criterion mutate."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    RESOURCE_NAME_FIELD_NUMBER: builtins.int
    CUSTOMER_NEGATIVE_CRITERION_FIELD_NUMBER: builtins.int
    resource_name: typing.Text = ...
    """Returned for successful operations."""

    @property
    def customer_negative_criterion(self) -> google.ads.googleads.v8.resources.customer_negative_criterion_pb2.CustomerNegativeCriterion:
        """The mutated criterion with only mutable fields after mutate. The field will
        only be returned when response_content_type is set to "MUTABLE_RESOURCE".
        """
        pass
    def __init__(self,
        *,
        resource_name : typing.Text = ...,
        customer_negative_criterion : typing.Optional[google.ads.googleads.v8.resources.customer_negative_criterion_pb2.CustomerNegativeCriterion] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["customer_negative_criterion",b"customer_negative_criterion"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["customer_negative_criterion",b"customer_negative_criterion","resource_name",b"resource_name"]) -> None: ...
global___MutateCustomerNegativeCriteriaResult = MutateCustomerNegativeCriteriaResult
