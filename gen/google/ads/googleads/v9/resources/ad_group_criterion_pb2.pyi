"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.ads.googleads.v9.common.criteria_pb2
import google.ads.googleads.v9.common.custom_parameter_pb2
import google.ads.googleads.v9.enums.ad_group_criterion_approval_status_pb2
import google.ads.googleads.v9.enums.ad_group_criterion_status_pb2
import google.ads.googleads.v9.enums.bidding_source_pb2
import google.ads.googleads.v9.enums.criterion_system_serving_status_pb2
import google.ads.googleads.v9.enums.criterion_type_pb2
import google.ads.googleads.v9.enums.quality_score_bucket_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class AdGroupCriterion(google.protobuf.message.Message):
    """Proto file describing the ad group criterion resource.

    An ad group criterion.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class QualityInfo(google.protobuf.message.Message):
        """A container for ad group criterion quality information."""
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        QUALITY_SCORE_FIELD_NUMBER: builtins.int
        CREATIVE_QUALITY_SCORE_FIELD_NUMBER: builtins.int
        POST_CLICK_QUALITY_SCORE_FIELD_NUMBER: builtins.int
        SEARCH_PREDICTED_CTR_FIELD_NUMBER: builtins.int
        quality_score: builtins.int = ...
        """Output only. The quality score.

        This field may not be populated if Google does not have enough
        information to determine a value.
        """

        creative_quality_score: google.ads.googleads.v9.enums.quality_score_bucket_pb2.QualityScoreBucketEnum.QualityScoreBucket.ValueType = ...
        """Output only. The performance of the ad compared to other advertisers."""

        post_click_quality_score: google.ads.googleads.v9.enums.quality_score_bucket_pb2.QualityScoreBucketEnum.QualityScoreBucket.ValueType = ...
        """Output only. The quality score of the landing page."""

        search_predicted_ctr: google.ads.googleads.v9.enums.quality_score_bucket_pb2.QualityScoreBucketEnum.QualityScoreBucket.ValueType = ...
        """Output only. The click-through rate compared to that of other advertisers."""

        def __init__(self,
            *,
            quality_score : typing.Optional[builtins.int] = ...,
            creative_quality_score : google.ads.googleads.v9.enums.quality_score_bucket_pb2.QualityScoreBucketEnum.QualityScoreBucket.ValueType = ...,
            post_click_quality_score : google.ads.googleads.v9.enums.quality_score_bucket_pb2.QualityScoreBucketEnum.QualityScoreBucket.ValueType = ...,
            search_predicted_ctr : google.ads.googleads.v9.enums.quality_score_bucket_pb2.QualityScoreBucketEnum.QualityScoreBucket.ValueType = ...,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["_quality_score",b"_quality_score","quality_score",b"quality_score"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["_quality_score",b"_quality_score","creative_quality_score",b"creative_quality_score","post_click_quality_score",b"post_click_quality_score","quality_score",b"quality_score","search_predicted_ctr",b"search_predicted_ctr"]) -> None: ...
        def WhichOneof(self, oneof_group: typing_extensions.Literal["_quality_score",b"_quality_score"]) -> typing.Optional[typing_extensions.Literal["quality_score"]]: ...

    class PositionEstimates(google.protobuf.message.Message):
        """Estimates for criterion bids at various positions."""
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        FIRST_PAGE_CPC_MICROS_FIELD_NUMBER: builtins.int
        FIRST_POSITION_CPC_MICROS_FIELD_NUMBER: builtins.int
        TOP_OF_PAGE_CPC_MICROS_FIELD_NUMBER: builtins.int
        ESTIMATED_ADD_CLICKS_AT_FIRST_POSITION_CPC_FIELD_NUMBER: builtins.int
        ESTIMATED_ADD_COST_AT_FIRST_POSITION_CPC_FIELD_NUMBER: builtins.int
        first_page_cpc_micros: builtins.int = ...
        """Output only. The estimate of the CPC bid required for ad to be shown on first
        page of search results.
        """

        first_position_cpc_micros: builtins.int = ...
        """Output only. The estimate of the CPC bid required for ad to be displayed in first
        position, at the top of the first page of search results.
        """

        top_of_page_cpc_micros: builtins.int = ...
        """Output only. The estimate of the CPC bid required for ad to be displayed at the top
        of the first page of search results.
        """

        estimated_add_clicks_at_first_position_cpc: builtins.int = ...
        """Output only. Estimate of how many clicks per week you might get by changing your
        keyword bid to the value in first_position_cpc_micros.
        """

        estimated_add_cost_at_first_position_cpc: builtins.int = ...
        """Output only. Estimate of how your cost per week might change when changing your
        keyword bid to the value in first_position_cpc_micros.
        """

        def __init__(self,
            *,
            first_page_cpc_micros : typing.Optional[builtins.int] = ...,
            first_position_cpc_micros : typing.Optional[builtins.int] = ...,
            top_of_page_cpc_micros : typing.Optional[builtins.int] = ...,
            estimated_add_clicks_at_first_position_cpc : typing.Optional[builtins.int] = ...,
            estimated_add_cost_at_first_position_cpc : typing.Optional[builtins.int] = ...,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["_estimated_add_clicks_at_first_position_cpc",b"_estimated_add_clicks_at_first_position_cpc","_estimated_add_cost_at_first_position_cpc",b"_estimated_add_cost_at_first_position_cpc","_first_page_cpc_micros",b"_first_page_cpc_micros","_first_position_cpc_micros",b"_first_position_cpc_micros","_top_of_page_cpc_micros",b"_top_of_page_cpc_micros","estimated_add_clicks_at_first_position_cpc",b"estimated_add_clicks_at_first_position_cpc","estimated_add_cost_at_first_position_cpc",b"estimated_add_cost_at_first_position_cpc","first_page_cpc_micros",b"first_page_cpc_micros","first_position_cpc_micros",b"first_position_cpc_micros","top_of_page_cpc_micros",b"top_of_page_cpc_micros"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["_estimated_add_clicks_at_first_position_cpc",b"_estimated_add_clicks_at_first_position_cpc","_estimated_add_cost_at_first_position_cpc",b"_estimated_add_cost_at_first_position_cpc","_first_page_cpc_micros",b"_first_page_cpc_micros","_first_position_cpc_micros",b"_first_position_cpc_micros","_top_of_page_cpc_micros",b"_top_of_page_cpc_micros","estimated_add_clicks_at_first_position_cpc",b"estimated_add_clicks_at_first_position_cpc","estimated_add_cost_at_first_position_cpc",b"estimated_add_cost_at_first_position_cpc","first_page_cpc_micros",b"first_page_cpc_micros","first_position_cpc_micros",b"first_position_cpc_micros","top_of_page_cpc_micros",b"top_of_page_cpc_micros"]) -> None: ...
        @typing.overload
        def WhichOneof(self, oneof_group: typing_extensions.Literal["_estimated_add_clicks_at_first_position_cpc",b"_estimated_add_clicks_at_first_position_cpc"]) -> typing.Optional[typing_extensions.Literal["estimated_add_clicks_at_first_position_cpc"]]: ...
        @typing.overload
        def WhichOneof(self, oneof_group: typing_extensions.Literal["_estimated_add_cost_at_first_position_cpc",b"_estimated_add_cost_at_first_position_cpc"]) -> typing.Optional[typing_extensions.Literal["estimated_add_cost_at_first_position_cpc"]]: ...
        @typing.overload
        def WhichOneof(self, oneof_group: typing_extensions.Literal["_first_page_cpc_micros",b"_first_page_cpc_micros"]) -> typing.Optional[typing_extensions.Literal["first_page_cpc_micros"]]: ...
        @typing.overload
        def WhichOneof(self, oneof_group: typing_extensions.Literal["_first_position_cpc_micros",b"_first_position_cpc_micros"]) -> typing.Optional[typing_extensions.Literal["first_position_cpc_micros"]]: ...
        @typing.overload
        def WhichOneof(self, oneof_group: typing_extensions.Literal["_top_of_page_cpc_micros",b"_top_of_page_cpc_micros"]) -> typing.Optional[typing_extensions.Literal["top_of_page_cpc_micros"]]: ...

    RESOURCE_NAME_FIELD_NUMBER: builtins.int
    CRITERION_ID_FIELD_NUMBER: builtins.int
    DISPLAY_NAME_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    QUALITY_INFO_FIELD_NUMBER: builtins.int
    AD_GROUP_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    NEGATIVE_FIELD_NUMBER: builtins.int
    SYSTEM_SERVING_STATUS_FIELD_NUMBER: builtins.int
    APPROVAL_STATUS_FIELD_NUMBER: builtins.int
    DISAPPROVAL_REASONS_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    BID_MODIFIER_FIELD_NUMBER: builtins.int
    CPC_BID_MICROS_FIELD_NUMBER: builtins.int
    CPM_BID_MICROS_FIELD_NUMBER: builtins.int
    CPV_BID_MICROS_FIELD_NUMBER: builtins.int
    PERCENT_CPC_BID_MICROS_FIELD_NUMBER: builtins.int
    EFFECTIVE_CPC_BID_MICROS_FIELD_NUMBER: builtins.int
    EFFECTIVE_CPM_BID_MICROS_FIELD_NUMBER: builtins.int
    EFFECTIVE_CPV_BID_MICROS_FIELD_NUMBER: builtins.int
    EFFECTIVE_PERCENT_CPC_BID_MICROS_FIELD_NUMBER: builtins.int
    EFFECTIVE_CPC_BID_SOURCE_FIELD_NUMBER: builtins.int
    EFFECTIVE_CPM_BID_SOURCE_FIELD_NUMBER: builtins.int
    EFFECTIVE_CPV_BID_SOURCE_FIELD_NUMBER: builtins.int
    EFFECTIVE_PERCENT_CPC_BID_SOURCE_FIELD_NUMBER: builtins.int
    POSITION_ESTIMATES_FIELD_NUMBER: builtins.int
    FINAL_URLS_FIELD_NUMBER: builtins.int
    FINAL_MOBILE_URLS_FIELD_NUMBER: builtins.int
    FINAL_URL_SUFFIX_FIELD_NUMBER: builtins.int
    TRACKING_URL_TEMPLATE_FIELD_NUMBER: builtins.int
    URL_CUSTOM_PARAMETERS_FIELD_NUMBER: builtins.int
    KEYWORD_FIELD_NUMBER: builtins.int
    PLACEMENT_FIELD_NUMBER: builtins.int
    MOBILE_APP_CATEGORY_FIELD_NUMBER: builtins.int
    MOBILE_APPLICATION_FIELD_NUMBER: builtins.int
    LISTING_GROUP_FIELD_NUMBER: builtins.int
    AGE_RANGE_FIELD_NUMBER: builtins.int
    GENDER_FIELD_NUMBER: builtins.int
    INCOME_RANGE_FIELD_NUMBER: builtins.int
    PARENTAL_STATUS_FIELD_NUMBER: builtins.int
    USER_LIST_FIELD_NUMBER: builtins.int
    YOUTUBE_VIDEO_FIELD_NUMBER: builtins.int
    YOUTUBE_CHANNEL_FIELD_NUMBER: builtins.int
    TOPIC_FIELD_NUMBER: builtins.int
    USER_INTEREST_FIELD_NUMBER: builtins.int
    WEBPAGE_FIELD_NUMBER: builtins.int
    APP_PAYMENT_MODEL_FIELD_NUMBER: builtins.int
    CUSTOM_AFFINITY_FIELD_NUMBER: builtins.int
    CUSTOM_INTENT_FIELD_NUMBER: builtins.int
    CUSTOM_AUDIENCE_FIELD_NUMBER: builtins.int
    COMBINED_AUDIENCE_FIELD_NUMBER: builtins.int
    resource_name: typing.Text = ...
    """Immutable. The resource name of the ad group criterion.
    Ad group criterion resource names have the form:

    `customers/{customer_id}/adGroupCriteria/{ad_group_id}~{criterion_id}`
    """

    criterion_id: builtins.int = ...
    """Output only. The ID of the criterion.

    This field is ignored for mutates.
    """

    display_name: typing.Text = ...
    """Output only. The display name of the criterion.

    This field is ignored for mutates.
    """

    status: google.ads.googleads.v9.enums.ad_group_criterion_status_pb2.AdGroupCriterionStatusEnum.AdGroupCriterionStatus.ValueType = ...
    """The status of the criterion.

    This is the status of the ad group criterion entity, set by the client.
    Note: UI reports may incorporate additional information that affects
    whether a criterion is eligible to run. In some cases a criterion that's
    REMOVED in the API can still show as enabled in the UI.
    For example, campaigns by default show to users of all age ranges unless
    excluded. The UI will show each age range as "enabled", since they're
    eligible to see the ads; but AdGroupCriterion.status will show "removed",
    since no positive criterion was added.
    """

    @property
    def quality_info(self) -> global___AdGroupCriterion.QualityInfo:
        """Output only. Information regarding the quality of the criterion."""
        pass
    ad_group: typing.Text = ...
    """Immutable. The ad group to which the criterion belongs."""

    type: google.ads.googleads.v9.enums.criterion_type_pb2.CriterionTypeEnum.CriterionType.ValueType = ...
    """Output only. The type of the criterion."""

    negative: builtins.bool = ...
    """Immutable. Whether to target (`false`) or exclude (`true`) the criterion.

    This field is immutable. To switch a criterion from positive to negative,
    remove then re-add it.
    """

    system_serving_status: google.ads.googleads.v9.enums.criterion_system_serving_status_pb2.CriterionSystemServingStatusEnum.CriterionSystemServingStatus.ValueType = ...
    """Output only. Serving status of the criterion."""

    approval_status: google.ads.googleads.v9.enums.ad_group_criterion_approval_status_pb2.AdGroupCriterionApprovalStatusEnum.AdGroupCriterionApprovalStatus.ValueType = ...
    """Output only. Approval status of the criterion."""

    @property
    def disapproval_reasons(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]:
        """Output only. List of disapproval reasons of the criterion.

        The different reasons for disapproving a criterion can be found here:
        https://support.google.com/adspolicy/answer/6008942

        This field is read-only.
        """
        pass
    @property
    def labels(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]:
        """Output only. The resource names of labels attached to this ad group criterion."""
        pass
    bid_modifier: builtins.float = ...
    """The modifier for the bid when the criterion matches. The modifier must be
    in the range: 0.1 - 10.0. Most targetable criteria types support modifiers.
    """

    cpc_bid_micros: builtins.int = ...
    """The CPC (cost-per-click) bid."""

    cpm_bid_micros: builtins.int = ...
    """The CPM (cost-per-thousand viewable impressions) bid."""

    cpv_bid_micros: builtins.int = ...
    """The CPV (cost-per-view) bid."""

    percent_cpc_bid_micros: builtins.int = ...
    """The CPC bid amount, expressed as a fraction of the advertised price
    for some good or service. The valid range for the fraction is [0,1) and the
    value stored here is 1,000,000 * [fraction].
    """

    effective_cpc_bid_micros: builtins.int = ...
    """Output only. The effective CPC (cost-per-click) bid."""

    effective_cpm_bid_micros: builtins.int = ...
    """Output only. The effective CPM (cost-per-thousand viewable impressions) bid."""

    effective_cpv_bid_micros: builtins.int = ...
    """Output only. The effective CPV (cost-per-view) bid."""

    effective_percent_cpc_bid_micros: builtins.int = ...
    """Output only. The effective Percent CPC bid amount."""

    effective_cpc_bid_source: google.ads.googleads.v9.enums.bidding_source_pb2.BiddingSourceEnum.BiddingSource.ValueType = ...
    """Output only. Source of the effective CPC bid."""

    effective_cpm_bid_source: google.ads.googleads.v9.enums.bidding_source_pb2.BiddingSourceEnum.BiddingSource.ValueType = ...
    """Output only. Source of the effective CPM bid."""

    effective_cpv_bid_source: google.ads.googleads.v9.enums.bidding_source_pb2.BiddingSourceEnum.BiddingSource.ValueType = ...
    """Output only. Source of the effective CPV bid."""

    effective_percent_cpc_bid_source: google.ads.googleads.v9.enums.bidding_source_pb2.BiddingSourceEnum.BiddingSource.ValueType = ...
    """Output only. Source of the effective Percent CPC bid."""

    @property
    def position_estimates(self) -> global___AdGroupCriterion.PositionEstimates:
        """Output only. Estimates for criterion bids at various positions."""
        pass
    @property
    def final_urls(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]:
        """The list of possible final URLs after all cross-domain redirects for the
        ad.
        """
        pass
    @property
    def final_mobile_urls(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]:
        """The list of possible final mobile URLs after all cross-domain redirects."""
        pass
    final_url_suffix: typing.Text = ...
    """URL template for appending params to final URL."""

    tracking_url_template: typing.Text = ...
    """The URL template for constructing a tracking URL."""

    @property
    def url_custom_parameters(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[google.ads.googleads.v9.common.custom_parameter_pb2.CustomParameter]:
        """The list of mappings used to substitute custom parameter tags in a
        `tracking_url_template`, `final_urls`, or `mobile_final_urls`.
        """
        pass
    @property
    def keyword(self) -> google.ads.googleads.v9.common.criteria_pb2.KeywordInfo:
        """Immutable. Keyword."""
        pass
    @property
    def placement(self) -> google.ads.googleads.v9.common.criteria_pb2.PlacementInfo:
        """Immutable. Placement."""
        pass
    @property
    def mobile_app_category(self) -> google.ads.googleads.v9.common.criteria_pb2.MobileAppCategoryInfo:
        """Immutable. Mobile app category."""
        pass
    @property
    def mobile_application(self) -> google.ads.googleads.v9.common.criteria_pb2.MobileApplicationInfo:
        """Immutable. Mobile application."""
        pass
    @property
    def listing_group(self) -> google.ads.googleads.v9.common.criteria_pb2.ListingGroupInfo:
        """Immutable. Listing group."""
        pass
    @property
    def age_range(self) -> google.ads.googleads.v9.common.criteria_pb2.AgeRangeInfo:
        """Immutable. Age range."""
        pass
    @property
    def gender(self) -> google.ads.googleads.v9.common.criteria_pb2.GenderInfo:
        """Immutable. Gender."""
        pass
    @property
    def income_range(self) -> google.ads.googleads.v9.common.criteria_pb2.IncomeRangeInfo:
        """Immutable. Income range."""
        pass
    @property
    def parental_status(self) -> google.ads.googleads.v9.common.criteria_pb2.ParentalStatusInfo:
        """Immutable. Parental status."""
        pass
    @property
    def user_list(self) -> google.ads.googleads.v9.common.criteria_pb2.UserListInfo:
        """Immutable. User List."""
        pass
    @property
    def youtube_video(self) -> google.ads.googleads.v9.common.criteria_pb2.YouTubeVideoInfo:
        """Immutable. YouTube Video."""
        pass
    @property
    def youtube_channel(self) -> google.ads.googleads.v9.common.criteria_pb2.YouTubeChannelInfo:
        """Immutable. YouTube Channel."""
        pass
    @property
    def topic(self) -> google.ads.googleads.v9.common.criteria_pb2.TopicInfo:
        """Immutable. Topic."""
        pass
    @property
    def user_interest(self) -> google.ads.googleads.v9.common.criteria_pb2.UserInterestInfo:
        """Immutable. User Interest."""
        pass
    @property
    def webpage(self) -> google.ads.googleads.v9.common.criteria_pb2.WebpageInfo:
        """Immutable. Webpage"""
        pass
    @property
    def app_payment_model(self) -> google.ads.googleads.v9.common.criteria_pb2.AppPaymentModelInfo:
        """Immutable. App Payment Model."""
        pass
    @property
    def custom_affinity(self) -> google.ads.googleads.v9.common.criteria_pb2.CustomAffinityInfo:
        """Immutable. Custom Affinity."""
        pass
    @property
    def custom_intent(self) -> google.ads.googleads.v9.common.criteria_pb2.CustomIntentInfo:
        """Immutable. Custom Intent."""
        pass
    @property
    def custom_audience(self) -> google.ads.googleads.v9.common.criteria_pb2.CustomAudienceInfo:
        """Immutable. Custom Audience."""
        pass
    @property
    def combined_audience(self) -> google.ads.googleads.v9.common.criteria_pb2.CombinedAudienceInfo:
        """Immutable. Combined Audience."""
        pass
    def __init__(self,
        *,
        resource_name : typing.Text = ...,
        criterion_id : typing.Optional[builtins.int] = ...,
        display_name : typing.Text = ...,
        status : google.ads.googleads.v9.enums.ad_group_criterion_status_pb2.AdGroupCriterionStatusEnum.AdGroupCriterionStatus.ValueType = ...,
        quality_info : typing.Optional[global___AdGroupCriterion.QualityInfo] = ...,
        ad_group : typing.Optional[typing.Text] = ...,
        type : google.ads.googleads.v9.enums.criterion_type_pb2.CriterionTypeEnum.CriterionType.ValueType = ...,
        negative : typing.Optional[builtins.bool] = ...,
        system_serving_status : google.ads.googleads.v9.enums.criterion_system_serving_status_pb2.CriterionSystemServingStatusEnum.CriterionSystemServingStatus.ValueType = ...,
        approval_status : google.ads.googleads.v9.enums.ad_group_criterion_approval_status_pb2.AdGroupCriterionApprovalStatusEnum.AdGroupCriterionApprovalStatus.ValueType = ...,
        disapproval_reasons : typing.Optional[typing.Iterable[typing.Text]] = ...,
        labels : typing.Optional[typing.Iterable[typing.Text]] = ...,
        bid_modifier : typing.Optional[builtins.float] = ...,
        cpc_bid_micros : typing.Optional[builtins.int] = ...,
        cpm_bid_micros : typing.Optional[builtins.int] = ...,
        cpv_bid_micros : typing.Optional[builtins.int] = ...,
        percent_cpc_bid_micros : typing.Optional[builtins.int] = ...,
        effective_cpc_bid_micros : typing.Optional[builtins.int] = ...,
        effective_cpm_bid_micros : typing.Optional[builtins.int] = ...,
        effective_cpv_bid_micros : typing.Optional[builtins.int] = ...,
        effective_percent_cpc_bid_micros : typing.Optional[builtins.int] = ...,
        effective_cpc_bid_source : google.ads.googleads.v9.enums.bidding_source_pb2.BiddingSourceEnum.BiddingSource.ValueType = ...,
        effective_cpm_bid_source : google.ads.googleads.v9.enums.bidding_source_pb2.BiddingSourceEnum.BiddingSource.ValueType = ...,
        effective_cpv_bid_source : google.ads.googleads.v9.enums.bidding_source_pb2.BiddingSourceEnum.BiddingSource.ValueType = ...,
        effective_percent_cpc_bid_source : google.ads.googleads.v9.enums.bidding_source_pb2.BiddingSourceEnum.BiddingSource.ValueType = ...,
        position_estimates : typing.Optional[global___AdGroupCriterion.PositionEstimates] = ...,
        final_urls : typing.Optional[typing.Iterable[typing.Text]] = ...,
        final_mobile_urls : typing.Optional[typing.Iterable[typing.Text]] = ...,
        final_url_suffix : typing.Optional[typing.Text] = ...,
        tracking_url_template : typing.Optional[typing.Text] = ...,
        url_custom_parameters : typing.Optional[typing.Iterable[google.ads.googleads.v9.common.custom_parameter_pb2.CustomParameter]] = ...,
        keyword : typing.Optional[google.ads.googleads.v9.common.criteria_pb2.KeywordInfo] = ...,
        placement : typing.Optional[google.ads.googleads.v9.common.criteria_pb2.PlacementInfo] = ...,
        mobile_app_category : typing.Optional[google.ads.googleads.v9.common.criteria_pb2.MobileAppCategoryInfo] = ...,
        mobile_application : typing.Optional[google.ads.googleads.v9.common.criteria_pb2.MobileApplicationInfo] = ...,
        listing_group : typing.Optional[google.ads.googleads.v9.common.criteria_pb2.ListingGroupInfo] = ...,
        age_range : typing.Optional[google.ads.googleads.v9.common.criteria_pb2.AgeRangeInfo] = ...,
        gender : typing.Optional[google.ads.googleads.v9.common.criteria_pb2.GenderInfo] = ...,
        income_range : typing.Optional[google.ads.googleads.v9.common.criteria_pb2.IncomeRangeInfo] = ...,
        parental_status : typing.Optional[google.ads.googleads.v9.common.criteria_pb2.ParentalStatusInfo] = ...,
        user_list : typing.Optional[google.ads.googleads.v9.common.criteria_pb2.UserListInfo] = ...,
        youtube_video : typing.Optional[google.ads.googleads.v9.common.criteria_pb2.YouTubeVideoInfo] = ...,
        youtube_channel : typing.Optional[google.ads.googleads.v9.common.criteria_pb2.YouTubeChannelInfo] = ...,
        topic : typing.Optional[google.ads.googleads.v9.common.criteria_pb2.TopicInfo] = ...,
        user_interest : typing.Optional[google.ads.googleads.v9.common.criteria_pb2.UserInterestInfo] = ...,
        webpage : typing.Optional[google.ads.googleads.v9.common.criteria_pb2.WebpageInfo] = ...,
        app_payment_model : typing.Optional[google.ads.googleads.v9.common.criteria_pb2.AppPaymentModelInfo] = ...,
        custom_affinity : typing.Optional[google.ads.googleads.v9.common.criteria_pb2.CustomAffinityInfo] = ...,
        custom_intent : typing.Optional[google.ads.googleads.v9.common.criteria_pb2.CustomIntentInfo] = ...,
        custom_audience : typing.Optional[google.ads.googleads.v9.common.criteria_pb2.CustomAudienceInfo] = ...,
        combined_audience : typing.Optional[google.ads.googleads.v9.common.criteria_pb2.CombinedAudienceInfo] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["_ad_group",b"_ad_group","_bid_modifier",b"_bid_modifier","_cpc_bid_micros",b"_cpc_bid_micros","_cpm_bid_micros",b"_cpm_bid_micros","_cpv_bid_micros",b"_cpv_bid_micros","_criterion_id",b"_criterion_id","_effective_cpc_bid_micros",b"_effective_cpc_bid_micros","_effective_cpm_bid_micros",b"_effective_cpm_bid_micros","_effective_cpv_bid_micros",b"_effective_cpv_bid_micros","_effective_percent_cpc_bid_micros",b"_effective_percent_cpc_bid_micros","_final_url_suffix",b"_final_url_suffix","_negative",b"_negative","_percent_cpc_bid_micros",b"_percent_cpc_bid_micros","_tracking_url_template",b"_tracking_url_template","ad_group",b"ad_group","age_range",b"age_range","app_payment_model",b"app_payment_model","bid_modifier",b"bid_modifier","combined_audience",b"combined_audience","cpc_bid_micros",b"cpc_bid_micros","cpm_bid_micros",b"cpm_bid_micros","cpv_bid_micros",b"cpv_bid_micros","criterion",b"criterion","criterion_id",b"criterion_id","custom_affinity",b"custom_affinity","custom_audience",b"custom_audience","custom_intent",b"custom_intent","effective_cpc_bid_micros",b"effective_cpc_bid_micros","effective_cpm_bid_micros",b"effective_cpm_bid_micros","effective_cpv_bid_micros",b"effective_cpv_bid_micros","effective_percent_cpc_bid_micros",b"effective_percent_cpc_bid_micros","final_url_suffix",b"final_url_suffix","gender",b"gender","income_range",b"income_range","keyword",b"keyword","listing_group",b"listing_group","mobile_app_category",b"mobile_app_category","mobile_application",b"mobile_application","negative",b"negative","parental_status",b"parental_status","percent_cpc_bid_micros",b"percent_cpc_bid_micros","placement",b"placement","position_estimates",b"position_estimates","quality_info",b"quality_info","topic",b"topic","tracking_url_template",b"tracking_url_template","user_interest",b"user_interest","user_list",b"user_list","webpage",b"webpage","youtube_channel",b"youtube_channel","youtube_video",b"youtube_video"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["_ad_group",b"_ad_group","_bid_modifier",b"_bid_modifier","_cpc_bid_micros",b"_cpc_bid_micros","_cpm_bid_micros",b"_cpm_bid_micros","_cpv_bid_micros",b"_cpv_bid_micros","_criterion_id",b"_criterion_id","_effective_cpc_bid_micros",b"_effective_cpc_bid_micros","_effective_cpm_bid_micros",b"_effective_cpm_bid_micros","_effective_cpv_bid_micros",b"_effective_cpv_bid_micros","_effective_percent_cpc_bid_micros",b"_effective_percent_cpc_bid_micros","_final_url_suffix",b"_final_url_suffix","_negative",b"_negative","_percent_cpc_bid_micros",b"_percent_cpc_bid_micros","_tracking_url_template",b"_tracking_url_template","ad_group",b"ad_group","age_range",b"age_range","app_payment_model",b"app_payment_model","approval_status",b"approval_status","bid_modifier",b"bid_modifier","combined_audience",b"combined_audience","cpc_bid_micros",b"cpc_bid_micros","cpm_bid_micros",b"cpm_bid_micros","cpv_bid_micros",b"cpv_bid_micros","criterion",b"criterion","criterion_id",b"criterion_id","custom_affinity",b"custom_affinity","custom_audience",b"custom_audience","custom_intent",b"custom_intent","disapproval_reasons",b"disapproval_reasons","display_name",b"display_name","effective_cpc_bid_micros",b"effective_cpc_bid_micros","effective_cpc_bid_source",b"effective_cpc_bid_source","effective_cpm_bid_micros",b"effective_cpm_bid_micros","effective_cpm_bid_source",b"effective_cpm_bid_source","effective_cpv_bid_micros",b"effective_cpv_bid_micros","effective_cpv_bid_source",b"effective_cpv_bid_source","effective_percent_cpc_bid_micros",b"effective_percent_cpc_bid_micros","effective_percent_cpc_bid_source",b"effective_percent_cpc_bid_source","final_mobile_urls",b"final_mobile_urls","final_url_suffix",b"final_url_suffix","final_urls",b"final_urls","gender",b"gender","income_range",b"income_range","keyword",b"keyword","labels",b"labels","listing_group",b"listing_group","mobile_app_category",b"mobile_app_category","mobile_application",b"mobile_application","negative",b"negative","parental_status",b"parental_status","percent_cpc_bid_micros",b"percent_cpc_bid_micros","placement",b"placement","position_estimates",b"position_estimates","quality_info",b"quality_info","resource_name",b"resource_name","status",b"status","system_serving_status",b"system_serving_status","topic",b"topic","tracking_url_template",b"tracking_url_template","type",b"type","url_custom_parameters",b"url_custom_parameters","user_interest",b"user_interest","user_list",b"user_list","webpage",b"webpage","youtube_channel",b"youtube_channel","youtube_video",b"youtube_video"]) -> None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_ad_group",b"_ad_group"]) -> typing.Optional[typing_extensions.Literal["ad_group"]]: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_bid_modifier",b"_bid_modifier"]) -> typing.Optional[typing_extensions.Literal["bid_modifier"]]: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_cpc_bid_micros",b"_cpc_bid_micros"]) -> typing.Optional[typing_extensions.Literal["cpc_bid_micros"]]: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_cpm_bid_micros",b"_cpm_bid_micros"]) -> typing.Optional[typing_extensions.Literal["cpm_bid_micros"]]: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_cpv_bid_micros",b"_cpv_bid_micros"]) -> typing.Optional[typing_extensions.Literal["cpv_bid_micros"]]: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_criterion_id",b"_criterion_id"]) -> typing.Optional[typing_extensions.Literal["criterion_id"]]: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_effective_cpc_bid_micros",b"_effective_cpc_bid_micros"]) -> typing.Optional[typing_extensions.Literal["effective_cpc_bid_micros"]]: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_effective_cpm_bid_micros",b"_effective_cpm_bid_micros"]) -> typing.Optional[typing_extensions.Literal["effective_cpm_bid_micros"]]: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_effective_cpv_bid_micros",b"_effective_cpv_bid_micros"]) -> typing.Optional[typing_extensions.Literal["effective_cpv_bid_micros"]]: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_effective_percent_cpc_bid_micros",b"_effective_percent_cpc_bid_micros"]) -> typing.Optional[typing_extensions.Literal["effective_percent_cpc_bid_micros"]]: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_final_url_suffix",b"_final_url_suffix"]) -> typing.Optional[typing_extensions.Literal["final_url_suffix"]]: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_negative",b"_negative"]) -> typing.Optional[typing_extensions.Literal["negative"]]: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_percent_cpc_bid_micros",b"_percent_cpc_bid_micros"]) -> typing.Optional[typing_extensions.Literal["percent_cpc_bid_micros"]]: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_tracking_url_template",b"_tracking_url_template"]) -> typing.Optional[typing_extensions.Literal["tracking_url_template"]]: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["criterion",b"criterion"]) -> typing.Optional[typing_extensions.Literal["keyword","placement","mobile_app_category","mobile_application","listing_group","age_range","gender","income_range","parental_status","user_list","youtube_video","youtube_channel","topic","user_interest","webpage","app_payment_model","custom_affinity","custom_intent","custom_audience","combined_audience"]]: ...
global___AdGroupCriterion = AdGroupCriterion
