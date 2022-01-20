"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.ads.googleads.v9.common.policy_pb2
import google.ads.googleads.v9.enums.response_content_type_pb2
import google.ads.googleads.v9.resources.ad_pb2
import google.protobuf.descriptor
import google.protobuf.field_mask_pb2
import google.protobuf.internal.containers
import google.protobuf.message
import google.rpc.status_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class GetAdRequest(google.protobuf.message.Message):
    """Request message for [AdService.GetAd][google.ads.googleads.v9.services.AdService.GetAd]."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    RESOURCE_NAME_FIELD_NUMBER: builtins.int
    resource_name: typing.Text = ...
    """Required. The resource name of the ad to fetch."""

    def __init__(self,
        *,
        resource_name : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["resource_name",b"resource_name"]) -> None: ...
global___GetAdRequest = GetAdRequest

class MutateAdsRequest(google.protobuf.message.Message):
    """Request message for [AdService.MutateAds][google.ads.googleads.v9.services.AdService.MutateAds]."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    CUSTOMER_ID_FIELD_NUMBER: builtins.int
    OPERATIONS_FIELD_NUMBER: builtins.int
    PARTIAL_FAILURE_FIELD_NUMBER: builtins.int
    RESPONSE_CONTENT_TYPE_FIELD_NUMBER: builtins.int
    VALIDATE_ONLY_FIELD_NUMBER: builtins.int
    customer_id: typing.Text = ...
    """Required. The ID of the customer whose ads are being modified."""

    @property
    def operations(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___AdOperation]:
        """Required. The list of operations to perform on individual ads."""
        pass
    partial_failure: builtins.bool = ...
    """If true, successful operations will be carried out and invalid
    operations will return errors. If false, all operations will be carried
    out in one transaction if and only if they are all valid.
    Default is false.
    """

    response_content_type: google.ads.googleads.v9.enums.response_content_type_pb2.ResponseContentTypeEnum.ResponseContentType.ValueType = ...
    """The response content type setting. Determines whether the mutable resource
    or just the resource name should be returned post mutation.
    """

    validate_only: builtins.bool = ...
    """If true, the request is validated but not executed. Only errors are
    returned, not results.
    """

    def __init__(self,
        *,
        customer_id : typing.Text = ...,
        operations : typing.Optional[typing.Iterable[global___AdOperation]] = ...,
        partial_failure : builtins.bool = ...,
        response_content_type : google.ads.googleads.v9.enums.response_content_type_pb2.ResponseContentTypeEnum.ResponseContentType.ValueType = ...,
        validate_only : builtins.bool = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["customer_id",b"customer_id","operations",b"operations","partial_failure",b"partial_failure","response_content_type",b"response_content_type","validate_only",b"validate_only"]) -> None: ...
global___MutateAdsRequest = MutateAdsRequest

class AdOperation(google.protobuf.message.Message):
    """A single update operation on an ad."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    UPDATE_MASK_FIELD_NUMBER: builtins.int
    POLICY_VALIDATION_PARAMETER_FIELD_NUMBER: builtins.int
    UPDATE_FIELD_NUMBER: builtins.int
    @property
    def update_mask(self) -> google.protobuf.field_mask_pb2.FieldMask:
        """FieldMask that determines which resource fields are modified in an update."""
        pass
    @property
    def policy_validation_parameter(self) -> google.ads.googleads.v9.common.policy_pb2.PolicyValidationParameter:
        """Configuration for how policies are validated."""
        pass
    @property
    def update(self) -> google.ads.googleads.v9.resources.ad_pb2.Ad:
        """Update operation: The ad is expected to have a valid resource name
        in this format:

        `customers/{customer_id}/ads/{ad_id}`
        """
        pass
    def __init__(self,
        *,
        update_mask : typing.Optional[google.protobuf.field_mask_pb2.FieldMask] = ...,
        policy_validation_parameter : typing.Optional[google.ads.googleads.v9.common.policy_pb2.PolicyValidationParameter] = ...,
        update : typing.Optional[google.ads.googleads.v9.resources.ad_pb2.Ad] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["operation",b"operation","policy_validation_parameter",b"policy_validation_parameter","update",b"update","update_mask",b"update_mask"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["operation",b"operation","policy_validation_parameter",b"policy_validation_parameter","update",b"update","update_mask",b"update_mask"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["operation",b"operation"]) -> typing.Optional[typing_extensions.Literal["update"]]: ...
global___AdOperation = AdOperation

class MutateAdsResponse(google.protobuf.message.Message):
    """Response message for an ad mutate."""
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
    def results(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___MutateAdResult]:
        """All results for the mutate."""
        pass
    def __init__(self,
        *,
        partial_failure_error : typing.Optional[google.rpc.status_pb2.Status] = ...,
        results : typing.Optional[typing.Iterable[global___MutateAdResult]] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["partial_failure_error",b"partial_failure_error"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["partial_failure_error",b"partial_failure_error","results",b"results"]) -> None: ...
global___MutateAdsResponse = MutateAdsResponse

class MutateAdResult(google.protobuf.message.Message):
    """The result for the ad mutate."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    RESOURCE_NAME_FIELD_NUMBER: builtins.int
    AD_FIELD_NUMBER: builtins.int
    resource_name: typing.Text = ...
    """The resource name returned for successful operations."""

    @property
    def ad(self) -> google.ads.googleads.v9.resources.ad_pb2.Ad:
        """The mutated ad with only mutable fields after mutate. The field will only
        be returned when response_content_type is set to "MUTABLE_RESOURCE".
        """
        pass
    def __init__(self,
        *,
        resource_name : typing.Text = ...,
        ad : typing.Optional[google.ads.googleads.v9.resources.ad_pb2.Ad] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["ad",b"ad"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["ad",b"ad","resource_name",b"resource_name"]) -> None: ...
global___MutateAdResult = MutateAdResult
