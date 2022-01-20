# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: google/ads/googleads/v9/services/google_ads_service.proto
# plugin: grpclib.plugin.main
import abc
import typing

import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server

import google.ads.googleads.v9.common.metrics_pb2
import google.ads.googleads.v9.common.segments_pb2
import google.ads.googleads.v9.enums.response_content_type_pb2
import google.ads.googleads.v9.enums.summary_row_setting_pb2
import google.ads.googleads.v9.resources.accessible_bidding_strategy_pb2
import google.ads.googleads.v9.resources.account_budget_pb2
import google.ads.googleads.v9.resources.account_budget_proposal_pb2
import google.ads.googleads.v9.resources.account_link_pb2
import google.ads.googleads.v9.resources.ad_group_pb2
import google.ads.googleads.v9.resources.ad_group_ad_pb2
import google.ads.googleads.v9.resources.ad_group_ad_asset_view_pb2
import google.ads.googleads.v9.resources.ad_group_ad_label_pb2
import google.ads.googleads.v9.resources.ad_group_asset_pb2
import google.ads.googleads.v9.resources.ad_group_audience_view_pb2
import google.ads.googleads.v9.resources.ad_group_bid_modifier_pb2
import google.ads.googleads.v9.resources.ad_group_criterion_pb2
import google.ads.googleads.v9.resources.ad_group_criterion_customizer_pb2
import google.ads.googleads.v9.resources.ad_group_criterion_label_pb2
import google.ads.googleads.v9.resources.ad_group_criterion_simulation_pb2
import google.ads.googleads.v9.resources.ad_group_customizer_pb2
import google.ads.googleads.v9.resources.ad_group_extension_setting_pb2
import google.ads.googleads.v9.resources.ad_group_feed_pb2
import google.ads.googleads.v9.resources.ad_group_label_pb2
import google.ads.googleads.v9.resources.ad_group_simulation_pb2
import google.ads.googleads.v9.resources.ad_parameter_pb2
import google.ads.googleads.v9.resources.ad_schedule_view_pb2
import google.ads.googleads.v9.resources.age_range_view_pb2
import google.ads.googleads.v9.resources.asset_pb2
import google.ads.googleads.v9.resources.asset_field_type_view_pb2
import google.ads.googleads.v9.resources.asset_group_pb2
import google.ads.googleads.v9.resources.asset_group_asset_pb2
import google.ads.googleads.v9.resources.asset_group_listing_group_filter_pb2
import google.ads.googleads.v9.resources.asset_group_product_group_view_pb2
import google.ads.googleads.v9.resources.asset_set_pb2
import google.ads.googleads.v9.resources.asset_set_asset_pb2
import google.ads.googleads.v9.resources.batch_job_pb2
import google.ads.googleads.v9.resources.bidding_data_exclusion_pb2
import google.ads.googleads.v9.resources.bidding_seasonality_adjustment_pb2
import google.ads.googleads.v9.resources.bidding_strategy_pb2
import google.ads.googleads.v9.resources.bidding_strategy_simulation_pb2
import google.ads.googleads.v9.resources.billing_setup_pb2
import google.ads.googleads.v9.resources.call_view_pb2
import google.ads.googleads.v9.resources.campaign_pb2
import google.ads.googleads.v9.resources.campaign_asset_pb2
import google.ads.googleads.v9.resources.campaign_asset_set_pb2
import google.ads.googleads.v9.resources.campaign_audience_view_pb2
import google.ads.googleads.v9.resources.campaign_bid_modifier_pb2
import google.ads.googleads.v9.resources.campaign_budget_pb2
import google.ads.googleads.v9.resources.campaign_conversion_goal_pb2
import google.ads.googleads.v9.resources.campaign_criterion_pb2
import google.ads.googleads.v9.resources.campaign_criterion_simulation_pb2
import google.ads.googleads.v9.resources.campaign_customizer_pb2
import google.ads.googleads.v9.resources.campaign_draft_pb2
import google.ads.googleads.v9.resources.campaign_experiment_pb2
import google.ads.googleads.v9.resources.campaign_extension_setting_pb2
import google.ads.googleads.v9.resources.campaign_feed_pb2
import google.ads.googleads.v9.resources.campaign_label_pb2
import google.ads.googleads.v9.resources.campaign_shared_set_pb2
import google.ads.googleads.v9.resources.campaign_simulation_pb2
import google.ads.googleads.v9.resources.carrier_constant_pb2
import google.ads.googleads.v9.resources.change_event_pb2
import google.ads.googleads.v9.resources.change_status_pb2
import google.ads.googleads.v9.resources.click_view_pb2
import google.ads.googleads.v9.resources.combined_audience_pb2
import google.ads.googleads.v9.resources.conversion_action_pb2
import google.ads.googleads.v9.resources.conversion_custom_variable_pb2
import google.ads.googleads.v9.resources.conversion_goal_campaign_config_pb2
import google.ads.googleads.v9.resources.conversion_value_rule_pb2
import google.ads.googleads.v9.resources.conversion_value_rule_set_pb2
import google.ads.googleads.v9.resources.currency_constant_pb2
import google.ads.googleads.v9.resources.custom_audience_pb2
import google.ads.googleads.v9.resources.custom_conversion_goal_pb2
import google.ads.googleads.v9.resources.custom_interest_pb2
import google.ads.googleads.v9.resources.customer_pb2
import google.ads.googleads.v9.resources.customer_asset_pb2
import google.ads.googleads.v9.resources.customer_client_pb2
import google.ads.googleads.v9.resources.customer_client_link_pb2
import google.ads.googleads.v9.resources.customer_conversion_goal_pb2
import google.ads.googleads.v9.resources.customer_customizer_pb2
import google.ads.googleads.v9.resources.customer_extension_setting_pb2
import google.ads.googleads.v9.resources.customer_feed_pb2
import google.ads.googleads.v9.resources.customer_label_pb2
import google.ads.googleads.v9.resources.customer_manager_link_pb2
import google.ads.googleads.v9.resources.customer_negative_criterion_pb2
import google.ads.googleads.v9.resources.customer_user_access_pb2
import google.ads.googleads.v9.resources.customer_user_access_invitation_pb2
import google.ads.googleads.v9.resources.customizer_attribute_pb2
import google.ads.googleads.v9.resources.detail_placement_view_pb2
import google.ads.googleads.v9.resources.detailed_demographic_pb2
import google.ads.googleads.v9.resources.display_keyword_view_pb2
import google.ads.googleads.v9.resources.distance_view_pb2
import google.ads.googleads.v9.resources.domain_category_pb2
import google.ads.googleads.v9.resources.dynamic_search_ads_search_term_view_pb2
import google.ads.googleads.v9.resources.expanded_landing_page_view_pb2
import google.ads.googleads.v9.resources.extension_feed_item_pb2
import google.ads.googleads.v9.resources.feed_pb2
import google.ads.googleads.v9.resources.feed_item_pb2
import google.ads.googleads.v9.resources.feed_item_set_pb2
import google.ads.googleads.v9.resources.feed_item_set_link_pb2
import google.ads.googleads.v9.resources.feed_item_target_pb2
import google.ads.googleads.v9.resources.feed_mapping_pb2
import google.ads.googleads.v9.resources.feed_placeholder_view_pb2
import google.ads.googleads.v9.resources.gender_view_pb2
import google.ads.googleads.v9.resources.geo_target_constant_pb2
import google.ads.googleads.v9.resources.geographic_view_pb2
import google.ads.googleads.v9.resources.group_placement_view_pb2
import google.ads.googleads.v9.resources.hotel_group_view_pb2
import google.ads.googleads.v9.resources.hotel_performance_view_pb2
import google.ads.googleads.v9.resources.hotel_reconciliation_pb2
import google.ads.googleads.v9.resources.income_range_view_pb2
import google.ads.googleads.v9.resources.keyword_plan_pb2
import google.ads.googleads.v9.resources.keyword_plan_ad_group_pb2
import google.ads.googleads.v9.resources.keyword_plan_ad_group_keyword_pb2
import google.ads.googleads.v9.resources.keyword_plan_campaign_pb2
import google.ads.googleads.v9.resources.keyword_plan_campaign_keyword_pb2
import google.ads.googleads.v9.resources.keyword_theme_constant_pb2
import google.ads.googleads.v9.resources.keyword_view_pb2
import google.ads.googleads.v9.resources.label_pb2
import google.ads.googleads.v9.resources.landing_page_view_pb2
import google.ads.googleads.v9.resources.language_constant_pb2
import google.ads.googleads.v9.resources.life_event_pb2
import google.ads.googleads.v9.resources.location_view_pb2
import google.ads.googleads.v9.resources.managed_placement_view_pb2
import google.ads.googleads.v9.resources.media_file_pb2
import google.ads.googleads.v9.resources.mobile_app_category_constant_pb2
import google.ads.googleads.v9.resources.mobile_device_constant_pb2
import google.ads.googleads.v9.resources.offline_user_data_job_pb2
import google.ads.googleads.v9.resources.operating_system_version_constant_pb2
import google.ads.googleads.v9.resources.paid_organic_search_term_view_pb2
import google.ads.googleads.v9.resources.parental_status_view_pb2
import google.ads.googleads.v9.resources.product_bidding_category_constant_pb2
import google.ads.googleads.v9.resources.product_group_view_pb2
import google.ads.googleads.v9.resources.recommendation_pb2
import google.ads.googleads.v9.resources.remarketing_action_pb2
import google.ads.googleads.v9.resources.search_term_view_pb2
import google.ads.googleads.v9.resources.shared_criterion_pb2
import google.ads.googleads.v9.resources.shared_set_pb2
import google.ads.googleads.v9.resources.shopping_performance_view_pb2
import google.ads.googleads.v9.resources.smart_campaign_search_term_view_pb2
import google.ads.googleads.v9.resources.smart_campaign_setting_pb2
import google.ads.googleads.v9.resources.third_party_app_analytics_link_pb2
import google.ads.googleads.v9.resources.topic_constant_pb2
import google.ads.googleads.v9.resources.topic_view_pb2
import google.ads.googleads.v9.resources.user_interest_pb2
import google.ads.googleads.v9.resources.user_list_pb2
import google.ads.googleads.v9.resources.user_location_view_pb2
import google.ads.googleads.v9.resources.video_pb2
import google.ads.googleads.v9.resources.webpage_view_pb2
import google.ads.googleads.v9.services.ad_group_ad_label_service_pb2
import google.ads.googleads.v9.services.ad_group_ad_service_pb2
import google.ads.googleads.v9.services.ad_group_asset_service_pb2
import google.ads.googleads.v9.services.ad_group_bid_modifier_service_pb2
import google.ads.googleads.v9.services.ad_group_criterion_customizer_service_pb2
import google.ads.googleads.v9.services.ad_group_criterion_label_service_pb2
import google.ads.googleads.v9.services.ad_group_criterion_service_pb2
import google.ads.googleads.v9.services.ad_group_customizer_service_pb2
import google.ads.googleads.v9.services.ad_group_extension_setting_service_pb2
import google.ads.googleads.v9.services.ad_group_feed_service_pb2
import google.ads.googleads.v9.services.ad_group_label_service_pb2
import google.ads.googleads.v9.services.ad_group_service_pb2
import google.ads.googleads.v9.services.ad_parameter_service_pb2
import google.ads.googleads.v9.services.ad_service_pb2
import google.ads.googleads.v9.services.asset_group_asset_service_pb2
import google.ads.googleads.v9.services.asset_group_listing_group_filter_service_pb2
import google.ads.googleads.v9.services.asset_group_service_pb2
import google.ads.googleads.v9.services.asset_service_pb2
import google.ads.googleads.v9.services.asset_set_asset_service_pb2
import google.ads.googleads.v9.services.asset_set_service_pb2
import google.ads.googleads.v9.services.bidding_data_exclusion_service_pb2
import google.ads.googleads.v9.services.bidding_seasonality_adjustment_service_pb2
import google.ads.googleads.v9.services.bidding_strategy_service_pb2
import google.ads.googleads.v9.services.campaign_asset_service_pb2
import google.ads.googleads.v9.services.campaign_asset_set_service_pb2
import google.ads.googleads.v9.services.campaign_bid_modifier_service_pb2
import google.ads.googleads.v9.services.campaign_budget_service_pb2
import google.ads.googleads.v9.services.campaign_conversion_goal_service_pb2
import google.ads.googleads.v9.services.campaign_criterion_service_pb2
import google.ads.googleads.v9.services.campaign_customizer_service_pb2
import google.ads.googleads.v9.services.campaign_draft_service_pb2
import google.ads.googleads.v9.services.campaign_experiment_service_pb2
import google.ads.googleads.v9.services.campaign_extension_setting_service_pb2
import google.ads.googleads.v9.services.campaign_feed_service_pb2
import google.ads.googleads.v9.services.campaign_label_service_pb2
import google.ads.googleads.v9.services.campaign_service_pb2
import google.ads.googleads.v9.services.campaign_shared_set_service_pb2
import google.ads.googleads.v9.services.conversion_action_service_pb2
import google.ads.googleads.v9.services.conversion_custom_variable_service_pb2
import google.ads.googleads.v9.services.conversion_goal_campaign_config_service_pb2
import google.ads.googleads.v9.services.conversion_value_rule_service_pb2
import google.ads.googleads.v9.services.conversion_value_rule_set_service_pb2
import google.ads.googleads.v9.services.custom_conversion_goal_service_pb2
import google.ads.googleads.v9.services.customer_asset_service_pb2
import google.ads.googleads.v9.services.customer_conversion_goal_service_pb2
import google.ads.googleads.v9.services.customer_customizer_service_pb2
import google.ads.googleads.v9.services.customer_extension_setting_service_pb2
import google.ads.googleads.v9.services.customer_feed_service_pb2
import google.ads.googleads.v9.services.customer_label_service_pb2
import google.ads.googleads.v9.services.customer_negative_criterion_service_pb2
import google.ads.googleads.v9.services.customer_service_pb2
import google.ads.googleads.v9.services.customizer_attribute_service_pb2
import google.ads.googleads.v9.services.extension_feed_item_service_pb2
import google.ads.googleads.v9.services.feed_item_service_pb2
import google.ads.googleads.v9.services.feed_item_set_link_service_pb2
import google.ads.googleads.v9.services.feed_item_set_service_pb2
import google.ads.googleads.v9.services.feed_item_target_service_pb2
import google.ads.googleads.v9.services.feed_mapping_service_pb2
import google.ads.googleads.v9.services.feed_service_pb2
import google.ads.googleads.v9.services.keyword_plan_ad_group_keyword_service_pb2
import google.ads.googleads.v9.services.keyword_plan_ad_group_service_pb2
import google.ads.googleads.v9.services.keyword_plan_campaign_keyword_service_pb2
import google.ads.googleads.v9.services.keyword_plan_campaign_service_pb2
import google.ads.googleads.v9.services.keyword_plan_service_pb2
import google.ads.googleads.v9.services.label_service_pb2
import google.ads.googleads.v9.services.media_file_service_pb2
import google.ads.googleads.v9.services.remarketing_action_service_pb2
import google.ads.googleads.v9.services.shared_criterion_service_pb2
import google.ads.googleads.v9.services.shared_set_service_pb2
import google.ads.googleads.v9.services.smart_campaign_setting_service_pb2
import google.ads.googleads.v9.services.user_list_service_pb2
import google.api.annotations_pb2
import google.api.client_pb2
import google.api.field_behavior_pb2
import google.protobuf.field_mask_pb2
import google.rpc.status_pb2
import google.ads.googleads.v9.services.google_ads_service_pb2


class GoogleAdsServiceBase(abc.ABC):

    @abc.abstractmethod
    async def Search(self, stream: 'grpclib.server.Stream[google.ads.googleads.v9.services.google_ads_service_pb2.SearchGoogleAdsRequest, google.ads.googleads.v9.services.google_ads_service_pb2.SearchGoogleAdsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def SearchStream(self, stream: 'grpclib.server.Stream[google.ads.googleads.v9.services.google_ads_service_pb2.SearchGoogleAdsStreamRequest, google.ads.googleads.v9.services.google_ads_service_pb2.SearchGoogleAdsStreamResponse]') -> None:
        pass

    @abc.abstractmethod
    async def Mutate(self, stream: 'grpclib.server.Stream[google.ads.googleads.v9.services.google_ads_service_pb2.MutateGoogleAdsRequest, google.ads.googleads.v9.services.google_ads_service_pb2.MutateGoogleAdsResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/google.ads.googleads.v9.services.GoogleAdsService/Search': grpclib.const.Handler(
                self.Search,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.ads.googleads.v9.services.google_ads_service_pb2.SearchGoogleAdsRequest,
                google.ads.googleads.v9.services.google_ads_service_pb2.SearchGoogleAdsResponse,
            ),
            '/google.ads.googleads.v9.services.GoogleAdsService/SearchStream': grpclib.const.Handler(
                self.SearchStream,
                grpclib.const.Cardinality.UNARY_STREAM,
                google.ads.googleads.v9.services.google_ads_service_pb2.SearchGoogleAdsStreamRequest,
                google.ads.googleads.v9.services.google_ads_service_pb2.SearchGoogleAdsStreamResponse,
            ),
            '/google.ads.googleads.v9.services.GoogleAdsService/Mutate': grpclib.const.Handler(
                self.Mutate,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.ads.googleads.v9.services.google_ads_service_pb2.MutateGoogleAdsRequest,
                google.ads.googleads.v9.services.google_ads_service_pb2.MutateGoogleAdsResponse,
            ),
        }


class GoogleAdsServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.Search = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.ads.googleads.v9.services.GoogleAdsService/Search',
            google.ads.googleads.v9.services.google_ads_service_pb2.SearchGoogleAdsRequest,
            google.ads.googleads.v9.services.google_ads_service_pb2.SearchGoogleAdsResponse,
        )
        self.SearchStream = grpclib.client.UnaryStreamMethod(
            channel,
            '/google.ads.googleads.v9.services.GoogleAdsService/SearchStream',
            google.ads.googleads.v9.services.google_ads_service_pb2.SearchGoogleAdsStreamRequest,
            google.ads.googleads.v9.services.google_ads_service_pb2.SearchGoogleAdsStreamResponse,
        )
        self.Mutate = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.ads.googleads.v9.services.GoogleAdsService/Mutate',
            google.ads.googleads.v9.services.google_ads_service_pb2.MutateGoogleAdsRequest,
            google.ads.googleads.v9.services.google_ads_service_pb2.MutateGoogleAdsResponse,
        )
