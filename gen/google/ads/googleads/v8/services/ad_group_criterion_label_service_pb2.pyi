"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.ads.googleads.v8.resources.ad_group_criterion_label_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import google.rpc.status_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class GetAdGroupCriterionLabelRequest(google.protobuf.message.Message):
    """Request message for
    [AdGroupCriterionLabelService.GetAdGroupCriterionLabel][google.ads.googleads.v8.services.AdGroupCriterionLabelService.GetAdGroupCriterionLabel].
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    RESOURCE_NAME_FIELD_NUMBER: builtins.int
    resource_name: typing.Text = ...
    """Required. The resource name of the ad group criterion label to fetch."""

    def __init__(self,
        *,
        resource_name : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["resource_name",b"resource_name"]) -> None: ...
global___GetAdGroupCriterionLabelRequest = GetAdGroupCriterionLabelRequest

class MutateAdGroupCriterionLabelsRequest(google.protobuf.message.Message):
    """Request message for
    [AdGroupCriterionLabelService.MutateAdGroupCriterionLabels][google.ads.googleads.v8.services.AdGroupCriterionLabelService.MutateAdGroupCriterionLabels].
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    CUSTOMER_ID_FIELD_NUMBER: builtins.int
    OPERATIONS_FIELD_NUMBER: builtins.int
    PARTIAL_FAILURE_FIELD_NUMBER: builtins.int
    VALIDATE_ONLY_FIELD_NUMBER: builtins.int
    customer_id: typing.Text = ...
    """Required. ID of the customer whose ad group criterion labels are being modified."""

    @property
    def operations(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___AdGroupCriterionLabelOperation]:
        """Required. The list of operations to perform on ad group criterion labels."""
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

    def __init__(self,
        *,
        customer_id : typing.Text = ...,
        operations : typing.Optional[typing.Iterable[global___AdGroupCriterionLabelOperation]] = ...,
        partial_failure : builtins.bool = ...,
        validate_only : builtins.bool = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["customer_id",b"customer_id","operations",b"operations","partial_failure",b"partial_failure","validate_only",b"validate_only"]) -> None: ...
global___MutateAdGroupCriterionLabelsRequest = MutateAdGroupCriterionLabelsRequest

class AdGroupCriterionLabelOperation(google.protobuf.message.Message):
    """A single operation (create, remove) on an ad group criterion label."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    CREATE_FIELD_NUMBER: builtins.int
    REMOVE_FIELD_NUMBER: builtins.int
    @property
    def create(self) -> google.ads.googleads.v8.resources.ad_group_criterion_label_pb2.AdGroupCriterionLabel:
        """Create operation: No resource name is expected for the new ad group
        label.
        """
        pass
    remove: typing.Text = ...
    """Remove operation: A resource name for the ad group criterion label
    being removed, in this format:

    `customers/{customer_id}/adGroupCriterionLabels/{ad_group_id}~{criterion_id}~{label_id}`
    """

    def __init__(self,
        *,
        create : typing.Optional[google.ads.googleads.v8.resources.ad_group_criterion_label_pb2.AdGroupCriterionLabel] = ...,
        remove : typing.Text = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["create",b"create","operation",b"operation","remove",b"remove"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["create",b"create","operation",b"operation","remove",b"remove"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["operation",b"operation"]) -> typing.Optional[typing_extensions.Literal["create","remove"]]: ...
global___AdGroupCriterionLabelOperation = AdGroupCriterionLabelOperation

class MutateAdGroupCriterionLabelsResponse(google.protobuf.message.Message):
    """Response message for an ad group criterion labels mutate."""
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
    def results(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___MutateAdGroupCriterionLabelResult]:
        """All results for the mutate."""
        pass
    def __init__(self,
        *,
        partial_failure_error : typing.Optional[google.rpc.status_pb2.Status] = ...,
        results : typing.Optional[typing.Iterable[global___MutateAdGroupCriterionLabelResult]] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["partial_failure_error",b"partial_failure_error"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["partial_failure_error",b"partial_failure_error","results",b"results"]) -> None: ...
global___MutateAdGroupCriterionLabelsResponse = MutateAdGroupCriterionLabelsResponse

class MutateAdGroupCriterionLabelResult(google.protobuf.message.Message):
    """The result for an ad group criterion label mutate."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    RESOURCE_NAME_FIELD_NUMBER: builtins.int
    resource_name: typing.Text = ...
    """Returned for successful operations."""

    def __init__(self,
        *,
        resource_name : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["resource_name",b"resource_name"]) -> None: ...
global___MutateAdGroupCriterionLabelResult = MutateAdGroupCriterionLabelResult
