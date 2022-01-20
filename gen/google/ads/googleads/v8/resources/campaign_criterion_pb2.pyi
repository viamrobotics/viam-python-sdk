"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.ads.googleads.v8.common.criteria_pb2
import google.ads.googleads.v8.enums.campaign_criterion_status_pb2
import google.ads.googleads.v8.enums.criterion_type_pb2
import google.protobuf.descriptor
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class CampaignCriterion(google.protobuf.message.Message):
    """Proto file describing the Campaign Criterion resource.

    A campaign criterion.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    RESOURCE_NAME_FIELD_NUMBER: builtins.int
    CAMPAIGN_FIELD_NUMBER: builtins.int
    CRITERION_ID_FIELD_NUMBER: builtins.int
    DISPLAY_NAME_FIELD_NUMBER: builtins.int
    BID_MODIFIER_FIELD_NUMBER: builtins.int
    NEGATIVE_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    KEYWORD_FIELD_NUMBER: builtins.int
    PLACEMENT_FIELD_NUMBER: builtins.int
    MOBILE_APP_CATEGORY_FIELD_NUMBER: builtins.int
    MOBILE_APPLICATION_FIELD_NUMBER: builtins.int
    LOCATION_FIELD_NUMBER: builtins.int
    DEVICE_FIELD_NUMBER: builtins.int
    AD_SCHEDULE_FIELD_NUMBER: builtins.int
    AGE_RANGE_FIELD_NUMBER: builtins.int
    GENDER_FIELD_NUMBER: builtins.int
    INCOME_RANGE_FIELD_NUMBER: builtins.int
    PARENTAL_STATUS_FIELD_NUMBER: builtins.int
    USER_LIST_FIELD_NUMBER: builtins.int
    YOUTUBE_VIDEO_FIELD_NUMBER: builtins.int
    YOUTUBE_CHANNEL_FIELD_NUMBER: builtins.int
    PROXIMITY_FIELD_NUMBER: builtins.int
    TOPIC_FIELD_NUMBER: builtins.int
    LISTING_SCOPE_FIELD_NUMBER: builtins.int
    LANGUAGE_FIELD_NUMBER: builtins.int
    IP_BLOCK_FIELD_NUMBER: builtins.int
    CONTENT_LABEL_FIELD_NUMBER: builtins.int
    CARRIER_FIELD_NUMBER: builtins.int
    USER_INTEREST_FIELD_NUMBER: builtins.int
    WEBPAGE_FIELD_NUMBER: builtins.int
    OPERATING_SYSTEM_VERSION_FIELD_NUMBER: builtins.int
    MOBILE_DEVICE_FIELD_NUMBER: builtins.int
    LOCATION_GROUP_FIELD_NUMBER: builtins.int
    CUSTOM_AFFINITY_FIELD_NUMBER: builtins.int
    CUSTOM_AUDIENCE_FIELD_NUMBER: builtins.int
    COMBINED_AUDIENCE_FIELD_NUMBER: builtins.int
    KEYWORD_THEME_FIELD_NUMBER: builtins.int
    resource_name: typing.Text = ...
    """Immutable. The resource name of the campaign criterion.
    Campaign criterion resource names have the form:

    `customers/{customer_id}/campaignCriteria/{campaign_id}~{criterion_id}`
    """

    campaign: typing.Text = ...
    """Immutable. The campaign to which the criterion belongs."""

    criterion_id: builtins.int = ...
    """Output only. The ID of the criterion.

    This field is ignored during mutate.
    """

    display_name: typing.Text = ...
    """Output only. The display name of the criterion.

    This field is ignored for mutates.
    """

    bid_modifier: builtins.float = ...
    """The modifier for the bids when the criterion matches. The modifier must be
    in the range: 0.1 - 10.0. Most targetable criteria types support modifiers.
    Use 0 to opt out of a Device type.
    """

    negative: builtins.bool = ...
    """Immutable. Whether to target (`false`) or exclude (`true`) the criterion."""

    type: google.ads.googleads.v8.enums.criterion_type_pb2.CriterionTypeEnum.CriterionType.ValueType = ...
    """Output only. The type of the criterion."""

    status: google.ads.googleads.v8.enums.campaign_criterion_status_pb2.CampaignCriterionStatusEnum.CampaignCriterionStatus.ValueType = ...
    """The status of the criterion."""

    @property
    def keyword(self) -> google.ads.googleads.v8.common.criteria_pb2.KeywordInfo:
        """Immutable. Keyword."""
        pass
    @property
    def placement(self) -> google.ads.googleads.v8.common.criteria_pb2.PlacementInfo:
        """Immutable. Placement."""
        pass
    @property
    def mobile_app_category(self) -> google.ads.googleads.v8.common.criteria_pb2.MobileAppCategoryInfo:
        """Immutable. Mobile app category."""
        pass
    @property
    def mobile_application(self) -> google.ads.googleads.v8.common.criteria_pb2.MobileApplicationInfo:
        """Immutable. Mobile application."""
        pass
    @property
    def location(self) -> google.ads.googleads.v8.common.criteria_pb2.LocationInfo:
        """Immutable. Location."""
        pass
    @property
    def device(self) -> google.ads.googleads.v8.common.criteria_pb2.DeviceInfo:
        """Immutable. Device."""
        pass
    @property
    def ad_schedule(self) -> google.ads.googleads.v8.common.criteria_pb2.AdScheduleInfo:
        """Immutable. Ad Schedule."""
        pass
    @property
    def age_range(self) -> google.ads.googleads.v8.common.criteria_pb2.AgeRangeInfo:
        """Immutable. Age range."""
        pass
    @property
    def gender(self) -> google.ads.googleads.v8.common.criteria_pb2.GenderInfo:
        """Immutable. Gender."""
        pass
    @property
    def income_range(self) -> google.ads.googleads.v8.common.criteria_pb2.IncomeRangeInfo:
        """Immutable. Income range."""
        pass
    @property
    def parental_status(self) -> google.ads.googleads.v8.common.criteria_pb2.ParentalStatusInfo:
        """Immutable. Parental status."""
        pass
    @property
    def user_list(self) -> google.ads.googleads.v8.common.criteria_pb2.UserListInfo:
        """Immutable. User List."""
        pass
    @property
    def youtube_video(self) -> google.ads.googleads.v8.common.criteria_pb2.YouTubeVideoInfo:
        """Immutable. YouTube Video."""
        pass
    @property
    def youtube_channel(self) -> google.ads.googleads.v8.common.criteria_pb2.YouTubeChannelInfo:
        """Immutable. YouTube Channel."""
        pass
    @property
    def proximity(self) -> google.ads.googleads.v8.common.criteria_pb2.ProximityInfo:
        """Immutable. Proximity."""
        pass
    @property
    def topic(self) -> google.ads.googleads.v8.common.criteria_pb2.TopicInfo:
        """Immutable. Topic."""
        pass
    @property
    def listing_scope(self) -> google.ads.googleads.v8.common.criteria_pb2.ListingScopeInfo:
        """Immutable. Listing scope."""
        pass
    @property
    def language(self) -> google.ads.googleads.v8.common.criteria_pb2.LanguageInfo:
        """Immutable. Language."""
        pass
    @property
    def ip_block(self) -> google.ads.googleads.v8.common.criteria_pb2.IpBlockInfo:
        """Immutable. IpBlock."""
        pass
    @property
    def content_label(self) -> google.ads.googleads.v8.common.criteria_pb2.ContentLabelInfo:
        """Immutable. ContentLabel."""
        pass
    @property
    def carrier(self) -> google.ads.googleads.v8.common.criteria_pb2.CarrierInfo:
        """Immutable. Carrier."""
        pass
    @property
    def user_interest(self) -> google.ads.googleads.v8.common.criteria_pb2.UserInterestInfo:
        """Immutable. User Interest."""
        pass
    @property
    def webpage(self) -> google.ads.googleads.v8.common.criteria_pb2.WebpageInfo:
        """Immutable. Webpage."""
        pass
    @property
    def operating_system_version(self) -> google.ads.googleads.v8.common.criteria_pb2.OperatingSystemVersionInfo:
        """Immutable. Operating system version."""
        pass
    @property
    def mobile_device(self) -> google.ads.googleads.v8.common.criteria_pb2.MobileDeviceInfo:
        """Immutable. Mobile Device."""
        pass
    @property
    def location_group(self) -> google.ads.googleads.v8.common.criteria_pb2.LocationGroupInfo:
        """Immutable. Location Group"""
        pass
    @property
    def custom_affinity(self) -> google.ads.googleads.v8.common.criteria_pb2.CustomAffinityInfo:
        """Immutable. Custom Affinity."""
        pass
    @property
    def custom_audience(self) -> google.ads.googleads.v8.common.criteria_pb2.CustomAudienceInfo:
        """Immutable. Custom Audience"""
        pass
    @property
    def combined_audience(self) -> google.ads.googleads.v8.common.criteria_pb2.CombinedAudienceInfo:
        """Immutable. Combined Audience."""
        pass
    @property
    def keyword_theme(self) -> google.ads.googleads.v8.common.criteria_pb2.KeywordThemeInfo:
        """Immutable. Smart Campaign Keyword Theme."""
        pass
    def __init__(self,
        *,
        resource_name : typing.Text = ...,
        campaign : typing.Optional[typing.Text] = ...,
        criterion_id : typing.Optional[builtins.int] = ...,
        display_name : typing.Text = ...,
        bid_modifier : typing.Optional[builtins.float] = ...,
        negative : typing.Optional[builtins.bool] = ...,
        type : google.ads.googleads.v8.enums.criterion_type_pb2.CriterionTypeEnum.CriterionType.ValueType = ...,
        status : google.ads.googleads.v8.enums.campaign_criterion_status_pb2.CampaignCriterionStatusEnum.CampaignCriterionStatus.ValueType = ...,
        keyword : typing.Optional[google.ads.googleads.v8.common.criteria_pb2.KeywordInfo] = ...,
        placement : typing.Optional[google.ads.googleads.v8.common.criteria_pb2.PlacementInfo] = ...,
        mobile_app_category : typing.Optional[google.ads.googleads.v8.common.criteria_pb2.MobileAppCategoryInfo] = ...,
        mobile_application : typing.Optional[google.ads.googleads.v8.common.criteria_pb2.MobileApplicationInfo] = ...,
        location : typing.Optional[google.ads.googleads.v8.common.criteria_pb2.LocationInfo] = ...,
        device : typing.Optional[google.ads.googleads.v8.common.criteria_pb2.DeviceInfo] = ...,
        ad_schedule : typing.Optional[google.ads.googleads.v8.common.criteria_pb2.AdScheduleInfo] = ...,
        age_range : typing.Optional[google.ads.googleads.v8.common.criteria_pb2.AgeRangeInfo] = ...,
        gender : typing.Optional[google.ads.googleads.v8.common.criteria_pb2.GenderInfo] = ...,
        income_range : typing.Optional[google.ads.googleads.v8.common.criteria_pb2.IncomeRangeInfo] = ...,
        parental_status : typing.Optional[google.ads.googleads.v8.common.criteria_pb2.ParentalStatusInfo] = ...,
        user_list : typing.Optional[google.ads.googleads.v8.common.criteria_pb2.UserListInfo] = ...,
        youtube_video : typing.Optional[google.ads.googleads.v8.common.criteria_pb2.YouTubeVideoInfo] = ...,
        youtube_channel : typing.Optional[google.ads.googleads.v8.common.criteria_pb2.YouTubeChannelInfo] = ...,
        proximity : typing.Optional[google.ads.googleads.v8.common.criteria_pb2.ProximityInfo] = ...,
        topic : typing.Optional[google.ads.googleads.v8.common.criteria_pb2.TopicInfo] = ...,
        listing_scope : typing.Optional[google.ads.googleads.v8.common.criteria_pb2.ListingScopeInfo] = ...,
        language : typing.Optional[google.ads.googleads.v8.common.criteria_pb2.LanguageInfo] = ...,
        ip_block : typing.Optional[google.ads.googleads.v8.common.criteria_pb2.IpBlockInfo] = ...,
        content_label : typing.Optional[google.ads.googleads.v8.common.criteria_pb2.ContentLabelInfo] = ...,
        carrier : typing.Optional[google.ads.googleads.v8.common.criteria_pb2.CarrierInfo] = ...,
        user_interest : typing.Optional[google.ads.googleads.v8.common.criteria_pb2.UserInterestInfo] = ...,
        webpage : typing.Optional[google.ads.googleads.v8.common.criteria_pb2.WebpageInfo] = ...,
        operating_system_version : typing.Optional[google.ads.googleads.v8.common.criteria_pb2.OperatingSystemVersionInfo] = ...,
        mobile_device : typing.Optional[google.ads.googleads.v8.common.criteria_pb2.MobileDeviceInfo] = ...,
        location_group : typing.Optional[google.ads.googleads.v8.common.criteria_pb2.LocationGroupInfo] = ...,
        custom_affinity : typing.Optional[google.ads.googleads.v8.common.criteria_pb2.CustomAffinityInfo] = ...,
        custom_audience : typing.Optional[google.ads.googleads.v8.common.criteria_pb2.CustomAudienceInfo] = ...,
        combined_audience : typing.Optional[google.ads.googleads.v8.common.criteria_pb2.CombinedAudienceInfo] = ...,
        keyword_theme : typing.Optional[google.ads.googleads.v8.common.criteria_pb2.KeywordThemeInfo] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["_bid_modifier",b"_bid_modifier","_campaign",b"_campaign","_criterion_id",b"_criterion_id","_negative",b"_negative","ad_schedule",b"ad_schedule","age_range",b"age_range","bid_modifier",b"bid_modifier","campaign",b"campaign","carrier",b"carrier","combined_audience",b"combined_audience","content_label",b"content_label","criterion",b"criterion","criterion_id",b"criterion_id","custom_affinity",b"custom_affinity","custom_audience",b"custom_audience","device",b"device","gender",b"gender","income_range",b"income_range","ip_block",b"ip_block","keyword",b"keyword","keyword_theme",b"keyword_theme","language",b"language","listing_scope",b"listing_scope","location",b"location","location_group",b"location_group","mobile_app_category",b"mobile_app_category","mobile_application",b"mobile_application","mobile_device",b"mobile_device","negative",b"negative","operating_system_version",b"operating_system_version","parental_status",b"parental_status","placement",b"placement","proximity",b"proximity","topic",b"topic","user_interest",b"user_interest","user_list",b"user_list","webpage",b"webpage","youtube_channel",b"youtube_channel","youtube_video",b"youtube_video"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["_bid_modifier",b"_bid_modifier","_campaign",b"_campaign","_criterion_id",b"_criterion_id","_negative",b"_negative","ad_schedule",b"ad_schedule","age_range",b"age_range","bid_modifier",b"bid_modifier","campaign",b"campaign","carrier",b"carrier","combined_audience",b"combined_audience","content_label",b"content_label","criterion",b"criterion","criterion_id",b"criterion_id","custom_affinity",b"custom_affinity","custom_audience",b"custom_audience","device",b"device","display_name",b"display_name","gender",b"gender","income_range",b"income_range","ip_block",b"ip_block","keyword",b"keyword","keyword_theme",b"keyword_theme","language",b"language","listing_scope",b"listing_scope","location",b"location","location_group",b"location_group","mobile_app_category",b"mobile_app_category","mobile_application",b"mobile_application","mobile_device",b"mobile_device","negative",b"negative","operating_system_version",b"operating_system_version","parental_status",b"parental_status","placement",b"placement","proximity",b"proximity","resource_name",b"resource_name","status",b"status","topic",b"topic","type",b"type","user_interest",b"user_interest","user_list",b"user_list","webpage",b"webpage","youtube_channel",b"youtube_channel","youtube_video",b"youtube_video"]) -> None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_bid_modifier",b"_bid_modifier"]) -> typing.Optional[typing_extensions.Literal["bid_modifier"]]: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_campaign",b"_campaign"]) -> typing.Optional[typing_extensions.Literal["campaign"]]: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_criterion_id",b"_criterion_id"]) -> typing.Optional[typing_extensions.Literal["criterion_id"]]: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_negative",b"_negative"]) -> typing.Optional[typing_extensions.Literal["negative"]]: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["criterion",b"criterion"]) -> typing.Optional[typing_extensions.Literal["keyword","placement","mobile_app_category","mobile_application","location","device","ad_schedule","age_range","gender","income_range","parental_status","user_list","youtube_video","youtube_channel","proximity","topic","listing_scope","language","ip_block","content_label","carrier","user_interest","webpage","operating_system_version","mobile_device","location_group","custom_affinity","custom_audience","combined_audience","keyword_theme"]]: ...
global___CampaignCriterion = CampaignCriterion
