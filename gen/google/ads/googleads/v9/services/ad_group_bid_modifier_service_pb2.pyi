"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.ads.googleads.v9.enums.response_content_type_pb2
import google.ads.googleads.v9.resources.ad_group_bid_modifier_pb2
import google.protobuf.descriptor
import google.protobuf.field_mask_pb2
import google.protobuf.internal.containers
import google.protobuf.message
import google.rpc.status_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class GetAdGroupBidModifierRequest(google.protobuf.message.Message):
    """Request message for [AdGroupBidModifierService.GetAdGroupBidModifier][google.ads.googleads.v9.services.AdGroupBidModifierService.GetAdGroupBidModifier]."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    RESOURCE_NAME_FIELD_NUMBER: builtins.int
    resource_name: typing.Text = ...
    """Required. The resource name of the ad group bid modifier to fetch."""

    def __init__(self,
        *,
        resource_name : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["resource_name",b"resource_name"]) -> None: ...
global___GetAdGroupBidModifierRequest = GetAdGroupBidModifierRequest

class MutateAdGroupBidModifiersRequest(google.protobuf.message.Message):
    """Request message for [AdGroupBidModifierService.MutateAdGroupBidModifiers][google.ads.googleads.v9.services.AdGroupBidModifierService.MutateAdGroupBidModifiers]."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    CUSTOMER_ID_FIELD_NUMBER: builtins.int
    OPERATIONS_FIELD_NUMBER: builtins.int
    PARTIAL_FAILURE_FIELD_NUMBER: builtins.int
    VALIDATE_ONLY_FIELD_NUMBER: builtins.int
    RESPONSE_CONTENT_TYPE_FIELD_NUMBER: builtins.int
    customer_id: typing.Text = ...
    """Required. ID of the customer whose ad group bid modifiers are being modified."""

    @property
    def operations(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___AdGroupBidModifierOperation]:
        """Required. The list of operations to perform on individual ad group bid modifiers."""
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

    response_content_type: google.ads.googleads.v9.enums.response_content_type_pb2.ResponseContentTypeEnum.ResponseContentType.ValueType = ...
    """The response content type setting. Determines whether the mutable resource
    or just the resource name should be returned post mutation.
    """

    def __init__(self,
        *,
        customer_id : typing.Text = ...,
        operations : typing.Optional[typing.Iterable[global___AdGroupBidModifierOperation]] = ...,
        partial_failure : builtins.bool = ...,
        validate_only : builtins.bool = ...,
        response_content_type : google.ads.googleads.v9.enums.response_content_type_pb2.ResponseContentTypeEnum.ResponseContentType.ValueType = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["customer_id",b"customer_id","operations",b"operations","partial_failure",b"partial_failure","response_content_type",b"response_content_type","validate_only",b"validate_only"]) -> None: ...
global___MutateAdGroupBidModifiersRequest = MutateAdGroupBidModifiersRequest

class AdGroupBidModifierOperation(google.protobuf.message.Message):
    """A single operation (create, remove, update) on an ad group bid modifier."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    UPDATE_MASK_FIELD_NUMBER: builtins.int
    CREATE_FIELD_NUMBER: builtins.int
    UPDATE_FIELD_NUMBER: builtins.int
    REMOVE_FIELD_NUMBER: builtins.int
    @property
    def update_mask(self) -> google.protobuf.field_mask_pb2.FieldMask:
        """FieldMask that determines which resource fields are modified in an update."""
        pass
    @property
    def create(self) -> google.ads.googleads.v9.resources.ad_group_bid_modifier_pb2.AdGroupBidModifier:
        """Create operation: No resource name is expected for the new ad group bid
        modifier.
        """
        pass
    @property
    def update(self) -> google.ads.googleads.v9.resources.ad_group_bid_modifier_pb2.AdGroupBidModifier:
        """Update operation: The ad group bid modifier is expected to have a valid
        resource name.
        """
        pass
    remove: typing.Text = ...
    """Remove operation: A resource name for the removed ad group bid modifier
    is expected, in this format:

    `customers/{customer_id}/adGroupBidModifiers/{ad_group_id}~{criterion_id}`
    """

    def __init__(self,
        *,
        update_mask : typing.Optional[google.protobuf.field_mask_pb2.FieldMask] = ...,
        create : typing.Optional[google.ads.googleads.v9.resources.ad_group_bid_modifier_pb2.AdGroupBidModifier] = ...,
        update : typing.Optional[google.ads.googleads.v9.resources.ad_group_bid_modifier_pb2.AdGroupBidModifier] = ...,
        remove : typing.Text = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["create",b"create","operation",b"operation","remove",b"remove","update",b"update","update_mask",b"update_mask"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["create",b"create","operation",b"operation","remove",b"remove","update",b"update","update_mask",b"update_mask"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["operation",b"operation"]) -> typing.Optional[typing_extensions.Literal["create","update","remove"]]: ...
global___AdGroupBidModifierOperation = AdGroupBidModifierOperation

class MutateAdGroupBidModifiersResponse(google.protobuf.message.Message):
    """Response message for ad group bid modifiers mutate."""
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
    def results(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___MutateAdGroupBidModifierResult]:
        """All results for the mutate."""
        pass
    def __init__(self,
        *,
        partial_failure_error : typing.Optional[google.rpc.status_pb2.Status] = ...,
        results : typing.Optional[typing.Iterable[global___MutateAdGroupBidModifierResult]] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["partial_failure_error",b"partial_failure_error"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["partial_failure_error",b"partial_failure_error","results",b"results"]) -> None: ...
global___MutateAdGroupBidModifiersResponse = MutateAdGroupBidModifiersResponse

class MutateAdGroupBidModifierResult(google.protobuf.message.Message):
    """The result for the criterion mutate."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    RESOURCE_NAME_FIELD_NUMBER: builtins.int
    AD_GROUP_BID_MODIFIER_FIELD_NUMBER: builtins.int
    resource_name: typing.Text = ...
    """Returned for successful operations."""

    @property
    def ad_group_bid_modifier(self) -> google.ads.googleads.v9.resources.ad_group_bid_modifier_pb2.AdGroupBidModifier:
        """The mutated ad group bid modifier with only mutable fields after mutate.
        The field will only be returned when response_content_type is set to
        "MUTABLE_RESOURCE".
        """
        pass
    def __init__(self,
        *,
        resource_name : typing.Text = ...,
        ad_group_bid_modifier : typing.Optional[google.ads.googleads.v9.resources.ad_group_bid_modifier_pb2.AdGroupBidModifier] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["ad_group_bid_modifier",b"ad_group_bid_modifier"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["ad_group_bid_modifier",b"ad_group_bid_modifier","resource_name",b"resource_name"]) -> None: ...
global___MutateAdGroupBidModifierResult = MutateAdGroupBidModifierResult
