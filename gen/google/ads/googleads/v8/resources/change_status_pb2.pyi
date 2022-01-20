"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.ads.googleads.v8.enums.change_status_operation_pb2
import google.ads.googleads.v8.enums.change_status_resource_type_pb2
import google.protobuf.descriptor
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class ChangeStatus(google.protobuf.message.Message):
    """Proto file describing the Change Status resource.

    Describes the status of returned resource. ChangeStatus could have up to 3
    minutes delay to reflect a new change.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    RESOURCE_NAME_FIELD_NUMBER: builtins.int
    LAST_CHANGE_DATE_TIME_FIELD_NUMBER: builtins.int
    RESOURCE_TYPE_FIELD_NUMBER: builtins.int
    CAMPAIGN_FIELD_NUMBER: builtins.int
    AD_GROUP_FIELD_NUMBER: builtins.int
    RESOURCE_STATUS_FIELD_NUMBER: builtins.int
    AD_GROUP_AD_FIELD_NUMBER: builtins.int
    AD_GROUP_CRITERION_FIELD_NUMBER: builtins.int
    CAMPAIGN_CRITERION_FIELD_NUMBER: builtins.int
    FEED_FIELD_NUMBER: builtins.int
    FEED_ITEM_FIELD_NUMBER: builtins.int
    AD_GROUP_FEED_FIELD_NUMBER: builtins.int
    CAMPAIGN_FEED_FIELD_NUMBER: builtins.int
    AD_GROUP_BID_MODIFIER_FIELD_NUMBER: builtins.int
    SHARED_SET_FIELD_NUMBER: builtins.int
    CAMPAIGN_SHARED_SET_FIELD_NUMBER: builtins.int
    ASSET_FIELD_NUMBER: builtins.int
    CUSTOMER_ASSET_FIELD_NUMBER: builtins.int
    CAMPAIGN_ASSET_FIELD_NUMBER: builtins.int
    AD_GROUP_ASSET_FIELD_NUMBER: builtins.int
    resource_name: typing.Text = ...
    """Output only. The resource name of the change status.
    Change status resource names have the form:

    `customers/{customer_id}/changeStatus/{change_status_id}`
    """

    last_change_date_time: typing.Text = ...
    """Output only. Time at which the most recent change has occurred on this resource."""

    resource_type: google.ads.googleads.v8.enums.change_status_resource_type_pb2.ChangeStatusResourceTypeEnum.ChangeStatusResourceType.ValueType = ...
    """Output only. Represents the type of the changed resource. This dictates what fields
    will be set. For example, for AD_GROUP, campaign and ad_group fields will
    be set.
    """

    campaign: typing.Text = ...
    """Output only. The Campaign affected by this change."""

    ad_group: typing.Text = ...
    """Output only. The AdGroup affected by this change."""

    resource_status: google.ads.googleads.v8.enums.change_status_operation_pb2.ChangeStatusOperationEnum.ChangeStatusOperation.ValueType = ...
    """Output only. Represents the status of the changed resource."""

    ad_group_ad: typing.Text = ...
    """Output only. The AdGroupAd affected by this change."""

    ad_group_criterion: typing.Text = ...
    """Output only. The AdGroupCriterion affected by this change."""

    campaign_criterion: typing.Text = ...
    """Output only. The CampaignCriterion affected by this change."""

    feed: typing.Text = ...
    """Output only. The Feed affected by this change."""

    feed_item: typing.Text = ...
    """Output only. The FeedItem affected by this change."""

    ad_group_feed: typing.Text = ...
    """Output only. The AdGroupFeed affected by this change."""

    campaign_feed: typing.Text = ...
    """Output only. The CampaignFeed affected by this change."""

    ad_group_bid_modifier: typing.Text = ...
    """Output only. The AdGroupBidModifier affected by this change."""

    shared_set: typing.Text = ...
    """Output only. The SharedSet affected by this change."""

    campaign_shared_set: typing.Text = ...
    """Output only. The CampaignSharedSet affected by this change."""

    asset: typing.Text = ...
    """Output only. The Asset affected by this change."""

    customer_asset: typing.Text = ...
    """Output only. The CustomerAsset affected by this change."""

    campaign_asset: typing.Text = ...
    """Output only. The CampaignAsset affected by this change."""

    ad_group_asset: typing.Text = ...
    """Output only. The AdGroupAsset affected by this change."""

    def __init__(self,
        *,
        resource_name : typing.Text = ...,
        last_change_date_time : typing.Optional[typing.Text] = ...,
        resource_type : google.ads.googleads.v8.enums.change_status_resource_type_pb2.ChangeStatusResourceTypeEnum.ChangeStatusResourceType.ValueType = ...,
        campaign : typing.Optional[typing.Text] = ...,
        ad_group : typing.Optional[typing.Text] = ...,
        resource_status : google.ads.googleads.v8.enums.change_status_operation_pb2.ChangeStatusOperationEnum.ChangeStatusOperation.ValueType = ...,
        ad_group_ad : typing.Optional[typing.Text] = ...,
        ad_group_criterion : typing.Optional[typing.Text] = ...,
        campaign_criterion : typing.Optional[typing.Text] = ...,
        feed : typing.Optional[typing.Text] = ...,
        feed_item : typing.Optional[typing.Text] = ...,
        ad_group_feed : typing.Optional[typing.Text] = ...,
        campaign_feed : typing.Optional[typing.Text] = ...,
        ad_group_bid_modifier : typing.Optional[typing.Text] = ...,
        shared_set : typing.Text = ...,
        campaign_shared_set : typing.Text = ...,
        asset : typing.Text = ...,
        customer_asset : typing.Text = ...,
        campaign_asset : typing.Text = ...,
        ad_group_asset : typing.Text = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["_ad_group",b"_ad_group","_ad_group_ad",b"_ad_group_ad","_ad_group_bid_modifier",b"_ad_group_bid_modifier","_ad_group_criterion",b"_ad_group_criterion","_ad_group_feed",b"_ad_group_feed","_campaign",b"_campaign","_campaign_criterion",b"_campaign_criterion","_campaign_feed",b"_campaign_feed","_feed",b"_feed","_feed_item",b"_feed_item","_last_change_date_time",b"_last_change_date_time","ad_group",b"ad_group","ad_group_ad",b"ad_group_ad","ad_group_bid_modifier",b"ad_group_bid_modifier","ad_group_criterion",b"ad_group_criterion","ad_group_feed",b"ad_group_feed","campaign",b"campaign","campaign_criterion",b"campaign_criterion","campaign_feed",b"campaign_feed","feed",b"feed","feed_item",b"feed_item","last_change_date_time",b"last_change_date_time"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["_ad_group",b"_ad_group","_ad_group_ad",b"_ad_group_ad","_ad_group_bid_modifier",b"_ad_group_bid_modifier","_ad_group_criterion",b"_ad_group_criterion","_ad_group_feed",b"_ad_group_feed","_campaign",b"_campaign","_campaign_criterion",b"_campaign_criterion","_campaign_feed",b"_campaign_feed","_feed",b"_feed","_feed_item",b"_feed_item","_last_change_date_time",b"_last_change_date_time","ad_group",b"ad_group","ad_group_ad",b"ad_group_ad","ad_group_asset",b"ad_group_asset","ad_group_bid_modifier",b"ad_group_bid_modifier","ad_group_criterion",b"ad_group_criterion","ad_group_feed",b"ad_group_feed","asset",b"asset","campaign",b"campaign","campaign_asset",b"campaign_asset","campaign_criterion",b"campaign_criterion","campaign_feed",b"campaign_feed","campaign_shared_set",b"campaign_shared_set","customer_asset",b"customer_asset","feed",b"feed","feed_item",b"feed_item","last_change_date_time",b"last_change_date_time","resource_name",b"resource_name","resource_status",b"resource_status","resource_type",b"resource_type","shared_set",b"shared_set"]) -> None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_ad_group",b"_ad_group"]) -> typing.Optional[typing_extensions.Literal["ad_group"]]: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_ad_group_ad",b"_ad_group_ad"]) -> typing.Optional[typing_extensions.Literal["ad_group_ad"]]: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_ad_group_bid_modifier",b"_ad_group_bid_modifier"]) -> typing.Optional[typing_extensions.Literal["ad_group_bid_modifier"]]: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_ad_group_criterion",b"_ad_group_criterion"]) -> typing.Optional[typing_extensions.Literal["ad_group_criterion"]]: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_ad_group_feed",b"_ad_group_feed"]) -> typing.Optional[typing_extensions.Literal["ad_group_feed"]]: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_campaign",b"_campaign"]) -> typing.Optional[typing_extensions.Literal["campaign"]]: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_campaign_criterion",b"_campaign_criterion"]) -> typing.Optional[typing_extensions.Literal["campaign_criterion"]]: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_campaign_feed",b"_campaign_feed"]) -> typing.Optional[typing_extensions.Literal["campaign_feed"]]: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_feed",b"_feed"]) -> typing.Optional[typing_extensions.Literal["feed"]]: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_feed_item",b"_feed_item"]) -> typing.Optional[typing_extensions.Literal["feed_item"]]: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_last_change_date_time",b"_last_change_date_time"]) -> typing.Optional[typing_extensions.Literal["last_change_date_time"]]: ...
global___ChangeStatus = ChangeStatus
