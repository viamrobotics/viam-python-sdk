"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.ads.googleads.v9.enums.asset_field_type_pb2
import google.ads.googleads.v9.enums.asset_link_status_pb2
import google.protobuf.descriptor
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class AdGroupAsset(google.protobuf.message.Message):
    """Proto file describing the AdGroupAsset resource.

    A link between an ad group and an asset.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    RESOURCE_NAME_FIELD_NUMBER: builtins.int
    AD_GROUP_FIELD_NUMBER: builtins.int
    ASSET_FIELD_NUMBER: builtins.int
    FIELD_TYPE_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    resource_name: typing.Text = ...
    """Immutable. The resource name of the ad group asset.
    AdGroupAsset resource names have the form:

    `customers/{customer_id}/adGroupAssets/{ad_group_id}~{asset_id}~{field_type}`
    """

    ad_group: typing.Text = ...
    """Required. Immutable. The ad group to which the asset is linked."""

    asset: typing.Text = ...
    """Required. Immutable. The asset which is linked to the ad group."""

    field_type: google.ads.googleads.v9.enums.asset_field_type_pb2.AssetFieldTypeEnum.AssetFieldType.ValueType = ...
    """Required. Immutable. Role that the asset takes under the linked ad group."""

    status: google.ads.googleads.v9.enums.asset_link_status_pb2.AssetLinkStatusEnum.AssetLinkStatus.ValueType = ...
    """Status of the ad group asset."""

    def __init__(self,
        *,
        resource_name : typing.Text = ...,
        ad_group : typing.Text = ...,
        asset : typing.Text = ...,
        field_type : google.ads.googleads.v9.enums.asset_field_type_pb2.AssetFieldTypeEnum.AssetFieldType.ValueType = ...,
        status : google.ads.googleads.v9.enums.asset_link_status_pb2.AssetLinkStatusEnum.AssetLinkStatus.ValueType = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["ad_group",b"ad_group","asset",b"asset","field_type",b"field_type","resource_name",b"resource_name","status",b"status"]) -> None: ...
global___AdGroupAsset = AdGroupAsset
