"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.ads.googleads.v9.enums.response_content_type_pb2
import google.ads.googleads.v9.resources.ad_group_asset_pb2
import google.protobuf.descriptor
import google.protobuf.field_mask_pb2
import google.protobuf.internal.containers
import google.protobuf.message
import google.rpc.status_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class GetAdGroupAssetRequest(google.protobuf.message.Message):
    """Request message for [AdGroupAssetService.GetAdGroupAsset][google.ads.googleads.v9.services.AdGroupAssetService.GetAdGroupAsset]."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    RESOURCE_NAME_FIELD_NUMBER: builtins.int
    resource_name: typing.Text = ...
    """Required. The resource name of the ad group asset to fetch."""

    def __init__(self,
        *,
        resource_name : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["resource_name",b"resource_name"]) -> None: ...
global___GetAdGroupAssetRequest = GetAdGroupAssetRequest

class MutateAdGroupAssetsRequest(google.protobuf.message.Message):
    """Request message for [AdGroupAssetService.MutateAdGroupAssets][google.ads.googleads.v9.services.AdGroupAssetService.MutateAdGroupAssets]."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    CUSTOMER_ID_FIELD_NUMBER: builtins.int
    OPERATIONS_FIELD_NUMBER: builtins.int
    PARTIAL_FAILURE_FIELD_NUMBER: builtins.int
    VALIDATE_ONLY_FIELD_NUMBER: builtins.int
    RESPONSE_CONTENT_TYPE_FIELD_NUMBER: builtins.int
    customer_id: typing.Text = ...
    """Required. The ID of the customer whose ad group assets are being modified."""

    @property
    def operations(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___AdGroupAssetOperation]:
        """Required. The list of operations to perform on individual ad group assets."""
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
        operations : typing.Optional[typing.Iterable[global___AdGroupAssetOperation]] = ...,
        partial_failure : builtins.bool = ...,
        validate_only : builtins.bool = ...,
        response_content_type : google.ads.googleads.v9.enums.response_content_type_pb2.ResponseContentTypeEnum.ResponseContentType.ValueType = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["customer_id",b"customer_id","operations",b"operations","partial_failure",b"partial_failure","response_content_type",b"response_content_type","validate_only",b"validate_only"]) -> None: ...
global___MutateAdGroupAssetsRequest = MutateAdGroupAssetsRequest

class AdGroupAssetOperation(google.protobuf.message.Message):
    """A single operation (create, update, remove) on an ad group asset."""
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
    def create(self) -> google.ads.googleads.v9.resources.ad_group_asset_pb2.AdGroupAsset:
        """Create operation: No resource name is expected for the new ad group
        asset.
        """
        pass
    @property
    def update(self) -> google.ads.googleads.v9.resources.ad_group_asset_pb2.AdGroupAsset:
        """Update operation: The ad group asset is expected to have a valid resource
        name.
        """
        pass
    remove: typing.Text = ...
    """Remove operation: A resource name for the removed ad group asset is
    expected, in this format:

    `customers/{customer_id}/adGroupAssets/{ad_group_id}~{asset_id}~{field_type}`
    """

    def __init__(self,
        *,
        update_mask : typing.Optional[google.protobuf.field_mask_pb2.FieldMask] = ...,
        create : typing.Optional[google.ads.googleads.v9.resources.ad_group_asset_pb2.AdGroupAsset] = ...,
        update : typing.Optional[google.ads.googleads.v9.resources.ad_group_asset_pb2.AdGroupAsset] = ...,
        remove : typing.Text = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["create",b"create","operation",b"operation","remove",b"remove","update",b"update","update_mask",b"update_mask"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["create",b"create","operation",b"operation","remove",b"remove","update",b"update","update_mask",b"update_mask"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["operation",b"operation"]) -> typing.Optional[typing_extensions.Literal["create","update","remove"]]: ...
global___AdGroupAssetOperation = AdGroupAssetOperation

class MutateAdGroupAssetsResponse(google.protobuf.message.Message):
    """Response message for an ad group asset mutate."""
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
    def results(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___MutateAdGroupAssetResult]:
        """All results for the mutate."""
        pass
    def __init__(self,
        *,
        partial_failure_error : typing.Optional[google.rpc.status_pb2.Status] = ...,
        results : typing.Optional[typing.Iterable[global___MutateAdGroupAssetResult]] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["partial_failure_error",b"partial_failure_error"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["partial_failure_error",b"partial_failure_error","results",b"results"]) -> None: ...
global___MutateAdGroupAssetsResponse = MutateAdGroupAssetsResponse

class MutateAdGroupAssetResult(google.protobuf.message.Message):
    """The result for the ad group asset mutate."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    RESOURCE_NAME_FIELD_NUMBER: builtins.int
    AD_GROUP_ASSET_FIELD_NUMBER: builtins.int
    resource_name: typing.Text = ...
    """Returned for successful operations."""

    @property
    def ad_group_asset(self) -> google.ads.googleads.v9.resources.ad_group_asset_pb2.AdGroupAsset:
        """The mutated ad group asset with only mutable fields after
        mutate. The field will only be returned when response_content_type is set
        to "MUTABLE_RESOURCE".
        """
        pass
    def __init__(self,
        *,
        resource_name : typing.Text = ...,
        ad_group_asset : typing.Optional[google.ads.googleads.v9.resources.ad_group_asset_pb2.AdGroupAsset] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["ad_group_asset",b"ad_group_asset"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["ad_group_asset",b"ad_group_asset","resource_name",b"resource_name"]) -> None: ...
global___MutateAdGroupAssetResult = MutateAdGroupAssetResult
