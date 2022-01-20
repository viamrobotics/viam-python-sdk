"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.ads.googleads.v7.common.criteria_pb2
import google.ads.googleads.v7.enums.feed_item_target_device_pb2
import google.ads.googleads.v7.enums.feed_item_target_status_pb2
import google.ads.googleads.v7.enums.feed_item_target_type_pb2
import google.protobuf.descriptor
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class FeedItemTarget(google.protobuf.message.Message):
    """Proto file describing the FeedItemTarget resource.

    A feed item target.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    RESOURCE_NAME_FIELD_NUMBER: builtins.int
    FEED_ITEM_FIELD_NUMBER: builtins.int
    FEED_ITEM_TARGET_TYPE_FIELD_NUMBER: builtins.int
    FEED_ITEM_TARGET_ID_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    CAMPAIGN_FIELD_NUMBER: builtins.int
    AD_GROUP_FIELD_NUMBER: builtins.int
    KEYWORD_FIELD_NUMBER: builtins.int
    GEO_TARGET_CONSTANT_FIELD_NUMBER: builtins.int
    DEVICE_FIELD_NUMBER: builtins.int
    AD_SCHEDULE_FIELD_NUMBER: builtins.int
    resource_name: typing.Text = ...
    """Immutable. The resource name of the feed item target.
    Feed item target resource names have the form:
    `customers/{customer_id}/feedItemTargets/{feed_id}~{feed_item_id}~{feed_item_target_type}~{feed_item_target_id}`
    """

    feed_item: typing.Text = ...
    """Immutable. The feed item to which this feed item target belongs."""

    feed_item_target_type: google.ads.googleads.v7.enums.feed_item_target_type_pb2.FeedItemTargetTypeEnum.FeedItemTargetType.ValueType = ...
    """Output only. The target type of this feed item target. This field is read-only."""

    feed_item_target_id: builtins.int = ...
    """Output only. The ID of the targeted resource. This field is read-only."""

    status: google.ads.googleads.v7.enums.feed_item_target_status_pb2.FeedItemTargetStatusEnum.FeedItemTargetStatus.ValueType = ...
    """Output only. Status of the feed item target.
    This field is read-only.
    """

    campaign: typing.Text = ...
    """Immutable. The targeted campaign."""

    ad_group: typing.Text = ...
    """Immutable. The targeted ad group."""

    @property
    def keyword(self) -> google.ads.googleads.v7.common.criteria_pb2.KeywordInfo:
        """Immutable. The targeted keyword."""
        pass
    geo_target_constant: typing.Text = ...
    """Immutable. The targeted geo target constant resource name."""

    device: google.ads.googleads.v7.enums.feed_item_target_device_pb2.FeedItemTargetDeviceEnum.FeedItemTargetDevice.ValueType = ...
    """Immutable. The targeted device."""

    @property
    def ad_schedule(self) -> google.ads.googleads.v7.common.criteria_pb2.AdScheduleInfo:
        """Immutable. The targeted schedule."""
        pass
    def __init__(self,
        *,
        resource_name : typing.Text = ...,
        feed_item : typing.Optional[typing.Text] = ...,
        feed_item_target_type : google.ads.googleads.v7.enums.feed_item_target_type_pb2.FeedItemTargetTypeEnum.FeedItemTargetType.ValueType = ...,
        feed_item_target_id : typing.Optional[builtins.int] = ...,
        status : google.ads.googleads.v7.enums.feed_item_target_status_pb2.FeedItemTargetStatusEnum.FeedItemTargetStatus.ValueType = ...,
        campaign : typing.Text = ...,
        ad_group : typing.Text = ...,
        keyword : typing.Optional[google.ads.googleads.v7.common.criteria_pb2.KeywordInfo] = ...,
        geo_target_constant : typing.Text = ...,
        device : google.ads.googleads.v7.enums.feed_item_target_device_pb2.FeedItemTargetDeviceEnum.FeedItemTargetDevice.ValueType = ...,
        ad_schedule : typing.Optional[google.ads.googleads.v7.common.criteria_pb2.AdScheduleInfo] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["_feed_item",b"_feed_item","_feed_item_target_id",b"_feed_item_target_id","ad_group",b"ad_group","ad_schedule",b"ad_schedule","campaign",b"campaign","device",b"device","feed_item",b"feed_item","feed_item_target_id",b"feed_item_target_id","geo_target_constant",b"geo_target_constant","keyword",b"keyword","target",b"target"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["_feed_item",b"_feed_item","_feed_item_target_id",b"_feed_item_target_id","ad_group",b"ad_group","ad_schedule",b"ad_schedule","campaign",b"campaign","device",b"device","feed_item",b"feed_item","feed_item_target_id",b"feed_item_target_id","feed_item_target_type",b"feed_item_target_type","geo_target_constant",b"geo_target_constant","keyword",b"keyword","resource_name",b"resource_name","status",b"status","target",b"target"]) -> None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_feed_item",b"_feed_item"]) -> typing.Optional[typing_extensions.Literal["feed_item"]]: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_feed_item_target_id",b"_feed_item_target_id"]) -> typing.Optional[typing_extensions.Literal["feed_item_target_id"]]: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["target",b"target"]) -> typing.Optional[typing_extensions.Literal["campaign","ad_group","keyword","geo_target_constant","device","ad_schedule"]]: ...
global___FeedItemTarget = FeedItemTarget
