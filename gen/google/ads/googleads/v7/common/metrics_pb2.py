# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v7/common/metrics.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.googleads.v7.enums import interaction_event_type_pb2 as google_dot_ads_dot_googleads_dot_v7_dot_enums_dot_interaction__event__type__pb2
from google.ads.googleads.v7.enums import quality_score_bucket_pb2 as google_dot_ads_dot_googleads_dot_v7_dot_enums_dot_quality__score__bucket__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,google/ads/googleads/v7/common/metrics.proto\x12\x1egoogle.ads.googleads.v7.common\x1a:google/ads/googleads/v7/enums/interaction_event_type.proto\x1a\x38google/ads/googleads/v7/enums/quality_score_bucket.proto\x1a\x1cgoogle/api/annotations.proto\"\xf1Z\n\x07Metrics\x12Q\n\"absolute_top_impression_percentage\x18\xb7\x01 \x01(\x01H\x00R\x1f\x61\x62soluteTopImpressionPercentage\x88\x01\x01\x12,\n\x0f\x61\x63tive_view_cpm\x18\xb8\x01 \x01(\x01H\x01R\ractiveViewCpm\x88\x01\x01\x12,\n\x0f\x61\x63tive_view_ctr\x18\xb9\x01 \x01(\x01H\x02R\ractiveViewCtr\x88\x01\x01\x12<\n\x17\x61\x63tive_view_impressions\x18\xba\x01 \x01(\x03H\x03R\x15\x61\x63tiveViewImpressions\x88\x01\x01\x12@\n\x19\x61\x63tive_view_measurability\x18\xbb\x01 \x01(\x01H\x04R\x17\x61\x63tiveViewMeasurability\x88\x01\x01\x12P\n\"active_view_measurable_cost_micros\x18\xbc\x01 \x01(\x03H\x05R\x1e\x61\x63tiveViewMeasurableCostMicros\x88\x01\x01\x12Q\n\"active_view_measurable_impressions\x18\xbd\x01 \x01(\x03H\x06R\x1f\x61\x63tiveViewMeasurableImpressions\x88\x01\x01\x12<\n\x17\x61\x63tive_view_viewability\x18\xbe\x01 \x01(\x01H\x07R\x15\x61\x63tiveViewViewability\x88\x01\x01\x12X\n&all_conversions_from_interactions_rate\x18\xbf\x01 \x01(\x01H\x08R\"allConversionsFromInteractionsRate\x88\x01\x01\x12\x38\n\x15\x61ll_conversions_value\x18\xc0\x01 \x01(\x01H\tR\x13\x61llConversionsValue\x88\x01\x01\x12V\n(all_conversions_value_by_conversion_date\x18\xf0\x01 \x01(\x01R#allConversionsValueByConversionDate\x12-\n\x0f\x61ll_conversions\x18\xc1\x01 \x01(\x01H\nR\x0e\x61llConversions\x88\x01\x01\x12K\n\"all_conversions_by_conversion_date\x18\xf1\x01 \x01(\x01R\x1e\x61llConversionsByConversionDate\x12H\n\x1e\x61ll_conversions_value_per_cost\x18\xc2\x01 \x01(\x01H\x0bR\x1a\x61llConversionsValuePerCost\x88\x01\x01\x12O\n\"all_conversions_from_click_to_call\x18\xc3\x01 \x01(\x01H\x0cR\x1d\x61llConversionsFromClickToCall\x88\x01\x01\x12K\n\x1f\x61ll_conversions_from_directions\x18\xc4\x01 \x01(\x01H\rR\x1c\x61llConversionsFromDirections\x88\x01\x01\x12x\n7all_conversions_from_interactions_value_per_interaction\x18\xc5\x01 \x01(\x01H\x0eR1allConversionsFromInteractionsValuePerInteraction\x88\x01\x01\x12?\n\x19\x61ll_conversions_from_menu\x18\xc6\x01 \x01(\x01H\x0fR\x16\x61llConversionsFromMenu\x88\x01\x01\x12\x41\n\x1a\x61ll_conversions_from_order\x18\xc7\x01 \x01(\x01H\x10R\x17\x61llConversionsFromOrder\x88\x01\x01\x12V\n%all_conversions_from_other_engagement\x18\xc8\x01 \x01(\x01H\x11R!allConversionsFromOtherEngagement\x88\x01\x01\x12L\n all_conversions_from_store_visit\x18\xc9\x01 \x01(\x01H\x12R\x1c\x61llConversionsFromStoreVisit\x88\x01\x01\x12P\n\"all_conversions_from_store_website\x18\xca\x01 \x01(\x01H\x13R\x1e\x61llConversionsFromStoreWebsite\x88\x01\x01\x12\'\n\x0c\x61verage_cost\x18\xcb\x01 \x01(\x01H\x14R\x0b\x61verageCost\x88\x01\x01\x12%\n\x0b\x61verage_cpc\x18\xcc\x01 \x01(\x01H\x15R\naverageCpc\x88\x01\x01\x12%\n\x0b\x61verage_cpe\x18\xcd\x01 \x01(\x01H\x16R\naverageCpe\x88\x01\x01\x12%\n\x0b\x61verage_cpm\x18\xce\x01 \x01(\x01H\x17R\naverageCpm\x88\x01\x01\x12%\n\x0b\x61verage_cpv\x18\xcf\x01 \x01(\x01H\x18R\naverageCpv\x88\x01\x01\x12\x32\n\x12\x61verage_page_views\x18\xd0\x01 \x01(\x01H\x19R\x10\x61veragePageViews\x88\x01\x01\x12\x35\n\x14\x61verage_time_on_site\x18\xd1\x01 \x01(\x01H\x1aR\x11\x61verageTimeOnSite\x88\x01\x01\x12?\n\x19\x62\x65nchmark_average_max_cpc\x18\xd2\x01 \x01(\x01H\x1bR\x16\x62\x65nchmarkAverageMaxCpc\x88\x01\x01\x12)\n\rbenchmark_ctr\x18\xd3\x01 \x01(\x01H\x1cR\x0c\x62\x65nchmarkCtr\x88\x01\x01\x12%\n\x0b\x62ounce_rate\x18\xd4\x01 \x01(\x01H\x1dR\nbounceRate\x88\x01\x01\x12\x1c\n\x06\x63licks\x18\x83\x01 \x01(\x03H\x1eR\x06\x63licks\x88\x01\x01\x12-\n\x0f\x63ombined_clicks\x18\x9c\x01 \x01(\x03H\x1fR\x0e\x63ombinedClicks\x88\x01\x01\x12?\n\x19\x63ombined_clicks_per_query\x18\x9d\x01 \x01(\x01H R\x16\x63ombinedClicksPerQuery\x88\x01\x01\x12/\n\x10\x63ombined_queries\x18\x9e\x01 \x01(\x03H!R\x0f\x63ombinedQueries\x88\x01\x01\x12T\n$content_budget_lost_impression_share\x18\x9f\x01 \x01(\x01H\"R contentBudgetLostImpressionShare\x88\x01\x01\x12>\n\x18\x63ontent_impression_share\x18\xa0\x01 \x01(\x01H#R\x16\x63ontentImpressionShare\x88\x01\x01\x12_\n*conversion_last_received_request_date_time\x18\xa1\x01 \x01(\tH$R%conversionLastReceivedRequestDateTime\x88\x01\x01\x12K\n\x1f\x63onversion_last_conversion_date\x18\xa2\x01 \x01(\tH%R\x1c\x63onversionLastConversionDate\x88\x01\x01\x12P\n\"content_rank_lost_impression_share\x18\xa3\x01 \x01(\x01H&R\x1e\x63ontentRankLostImpressionShare\x88\x01\x01\x12Q\n\"conversions_from_interactions_rate\x18\xa4\x01 \x01(\x01H\'R\x1f\x63onversionsFromInteractionsRate\x88\x01\x01\x12\x31\n\x11\x63onversions_value\x18\xa5\x01 \x01(\x01H(R\x10\x63onversionsValue\x88\x01\x01\x12O\n$conversions_value_by_conversion_date\x18\xf2\x01 \x01(\x01R conversionsValueByConversionDate\x12\x41\n\x1a\x63onversions_value_per_cost\x18\xa6\x01 \x01(\x01H)R\x17\x63onversionsValuePerCost\x88\x01\x01\x12q\n3conversions_from_interactions_value_per_interaction\x18\xa7\x01 \x01(\x01H*R.conversionsFromInteractionsValuePerInteraction\x88\x01\x01\x12&\n\x0b\x63onversions\x18\xa8\x01 \x01(\x01H+R\x0b\x63onversions\x88\x01\x01\x12\x44\n\x1e\x63onversions_by_conversion_date\x18\xf3\x01 \x01(\x01R\x1b\x63onversionsByConversionDate\x12%\n\x0b\x63ost_micros\x18\xa9\x01 \x01(\x03H,R\ncostMicros\x88\x01\x01\x12=\n\x18\x63ost_per_all_conversions\x18\xaa\x01 \x01(\x01H-R\x15\x63ostPerAllConversions\x88\x01\x01\x12\x34\n\x13\x63ost_per_conversion\x18\xab\x01 \x01(\x01H.R\x11\x63ostPerConversion\x88\x01\x01\x12\x63\n,cost_per_current_model_attributed_conversion\x18\xac\x01 \x01(\x01H/R\'costPerCurrentModelAttributedConversion\x88\x01\x01\x12>\n\x18\x63ross_device_conversions\x18\xad\x01 \x01(\x01H0R\x16\x63rossDeviceConversions\x88\x01\x01\x12\x16\n\x03\x63tr\x18\xae\x01 \x01(\x01H1R\x03\x63tr\x88\x01\x01\x12U\n$current_model_attributed_conversions\x18\xaf\x01 \x01(\x01H2R!currentModelAttributedConversions\x88\x01\x01\x12\x80\x01\n;current_model_attributed_conversions_from_interactions_rate\x18\xb0\x01 \x01(\x01H3R5currentModelAttributedConversionsFromInteractionsRate\x88\x01\x01\x12\xa0\x01\nLcurrent_model_attributed_conversions_from_interactions_value_per_interaction\x18\xb1\x01 \x01(\x01H4RDcurrentModelAttributedConversionsFromInteractionsValuePerInteraction\x88\x01\x01\x12`\n*current_model_attributed_conversions_value\x18\xb2\x01 \x01(\x01H5R&currentModelAttributedConversionsValue\x88\x01\x01\x12p\n3current_model_attributed_conversions_value_per_cost\x18\xb3\x01 \x01(\x01H6R-currentModelAttributedConversionsValuePerCost\x88\x01\x01\x12-\n\x0f\x65ngagement_rate\x18\xb4\x01 \x01(\x01H7R\x0e\x65ngagementRate\x88\x01\x01\x12&\n\x0b\x65ngagements\x18\xb5\x01 \x01(\x03H8R\x0b\x65ngagements\x88\x01\x01\x12J\n\x1fhotel_average_lead_value_micros\x18\xd5\x01 \x01(\x01H9R\x1bhotelAverageLeadValueMicros\x88\x01\x01\x12O\n!hotel_price_difference_percentage\x18\xd6\x01 \x01(\x01H:R\x1ehotelPriceDifferencePercentage\x88\x01\x01\x12\x42\n\x1ahotel_eligible_impressions\x18\xd7\x01 \x01(\x03H;R\x18hotelEligibleImpressions\x88\x01\x01\x12\x93\x01\n!historical_creative_quality_score\x18P \x01(\x0e\x32H.google.ads.googleads.v7.enums.QualityScoreBucketEnum.QualityScoreBucketR\x1ehistoricalCreativeQualityScore\x12\x9a\x01\n%historical_landing_page_quality_score\x18Q \x01(\x0e\x32H.google.ads.googleads.v7.enums.QualityScoreBucketEnum.QualityScoreBucketR!historicalLandingPageQualityScore\x12>\n\x18historical_quality_score\x18\xd8\x01 \x01(\x03H<R\x16historicalQualityScore\x88\x01\x01\x12\x8f\x01\n\x1fhistorical_search_predicted_ctr\x18S \x01(\x0e\x32H.google.ads.googleads.v7.enums.QualityScoreBucketEnum.QualityScoreBucketR\x1chistoricalSearchPredictedCtr\x12+\n\x0egmail_forwards\x18\xd9\x01 \x01(\x03H=R\rgmailForwards\x88\x01\x01\x12%\n\x0bgmail_saves\x18\xda\x01 \x01(\x03H>R\ngmailSaves\x88\x01\x01\x12:\n\x16gmail_secondary_clicks\x18\xdb\x01 \x01(\x03H?R\x14gmailSecondaryClicks\x88\x01\x01\x12\x45\n\x1cimpressions_from_store_reach\x18\xdc\x01 \x01(\x03H@R\x19impressionsFromStoreReach\x88\x01\x01\x12&\n\x0bimpressions\x18\xdd\x01 \x01(\x03HAR\x0bimpressions\x88\x01\x01\x12/\n\x10interaction_rate\x18\xde\x01 \x01(\x01HBR\x0finteractionRate\x88\x01\x01\x12(\n\x0cinteractions\x18\xdf\x01 \x01(\x03HCR\x0cinteractions\x88\x01\x01\x12\x84\x01\n\x17interaction_event_types\x18\x64 \x03(\x0e\x32L.google.ads.googleads.v7.enums.InteractionEventTypeEnum.InteractionEventTypeR\x15interactionEventTypes\x12\x32\n\x12invalid_click_rate\x18\xe0\x01 \x01(\x01HDR\x10invalidClickRate\x88\x01\x01\x12+\n\x0einvalid_clicks\x18\xe1\x01 \x01(\x03HER\rinvalidClicks\x88\x01\x01\x12)\n\rmessage_chats\x18\xe2\x01 \x01(\x03HFR\x0cmessageChats\x88\x01\x01\x12\x35\n\x13message_impressions\x18\xe3\x01 \x01(\x03HGR\x12messageImpressions\x88\x01\x01\x12\x30\n\x11message_chat_rate\x18\xe4\x01 \x01(\x01HHR\x0fmessageChatRate\x88\x01\x01\x12O\n!mobile_friendly_clicks_percentage\x18\xe5\x01 \x01(\x01HIR\x1emobileFriendlyClicksPercentage\x88\x01\x01\x12+\n\x0eorganic_clicks\x18\xe6\x01 \x01(\x03HJR\rorganicClicks\x88\x01\x01\x12=\n\x18organic_clicks_per_query\x18\xe7\x01 \x01(\x01HKR\x15organicClicksPerQuery\x88\x01\x01\x12\x35\n\x13organic_impressions\x18\xe8\x01 \x01(\x03HLR\x12organicImpressions\x88\x01\x01\x12G\n\x1dorganic_impressions_per_query\x18\xe9\x01 \x01(\x01HMR\x1aorganicImpressionsPerQuery\x88\x01\x01\x12-\n\x0forganic_queries\x18\xea\x01 \x01(\x03HNR\x0eorganicQueries\x88\x01\x01\x12\x36\n\x14percent_new_visitors\x18\xeb\x01 \x01(\x01HOR\x12percentNewVisitors\x88\x01\x01\x12%\n\x0bphone_calls\x18\xec\x01 \x01(\x03HPR\nphoneCalls\x88\x01\x01\x12\x31\n\x11phone_impressions\x18\xed\x01 \x01(\x03HQR\x10phoneImpressions\x88\x01\x01\x12\x32\n\x12phone_through_rate\x18\xee\x01 \x01(\x01HRR\x10phoneThroughRate\x88\x01\x01\x12\'\n\x0crelative_ctr\x18\xef\x01 \x01(\x01HSR\x0brelativeCtr\x88\x01\x01\x12T\n$search_absolute_top_impression_share\x18\x88\x01 \x01(\x01HTR searchAbsoluteTopImpressionShare\x88\x01\x01\x12j\n0search_budget_lost_absolute_top_impression_share\x18\x89\x01 \x01(\x01HUR*searchBudgetLostAbsoluteTopImpressionShare\x88\x01\x01\x12R\n#search_budget_lost_impression_share\x18\x8a\x01 \x01(\x01HVR\x1fsearchBudgetLostImpressionShare\x88\x01\x01\x12Y\n\'search_budget_lost_top_impression_share\x18\x8b\x01 \x01(\x01HWR\"searchBudgetLostTopImpressionShare\x88\x01\x01\x12\x32\n\x12search_click_share\x18\x8c\x01 \x01(\x01HXR\x10searchClickShare\x88\x01\x01\x12R\n#search_exact_match_impression_share\x18\x8d\x01 \x01(\x01HYR\x1fsearchExactMatchImpressionShare\x88\x01\x01\x12<\n\x17search_impression_share\x18\x8e\x01 \x01(\x01HZR\x15searchImpressionShare\x88\x01\x01\x12\x66\n.search_rank_lost_absolute_top_impression_share\x18\x8f\x01 \x01(\x01H[R(searchRankLostAbsoluteTopImpressionShare\x88\x01\x01\x12N\n!search_rank_lost_impression_share\x18\x90\x01 \x01(\x01H\\R\x1dsearchRankLostImpressionShare\x88\x01\x01\x12U\n%search_rank_lost_top_impression_share\x18\x91\x01 \x01(\x01H]R searchRankLostTopImpressionShare\x88\x01\x01\x12\x43\n\x1bsearch_top_impression_share\x18\x92\x01 \x01(\x01H^R\x18searchTopImpressionShare\x88\x01\x01\x12%\n\x0bspeed_score\x18\x93\x01 \x01(\x03H_R\nspeedScore\x88\x01\x01\x12@\n\x19top_impression_percentage\x18\x94\x01 \x01(\x01H`R\x17topImpressionPercentage\x88\x01\x01\x12k\n0valid_accelerated_mobile_pages_clicks_percentage\x18\x95\x01 \x01(\x01HaR+validAcceleratedMobilePagesClicksPercentage\x88\x01\x01\x12?\n\x19value_per_all_conversions\x18\x96\x01 \x01(\x01HbR\x16valuePerAllConversions\x88\x01\x01\x12\x62\n,value_per_all_conversions_by_conversion_date\x18\xf4\x01 \x01(\x01HcR&valuePerAllConversionsByConversionDate\x88\x01\x01\x12\x36\n\x14value_per_conversion\x18\x97\x01 \x01(\x01HdR\x12valuePerConversion\x88\x01\x01\x12[\n(value_per_conversions_by_conversion_date\x18\xf5\x01 \x01(\x01HeR#valuePerConversionsByConversionDate\x88\x01\x01\x12\x65\n-value_per_current_model_attributed_conversion\x18\x98\x01 \x01(\x01HfR(valuePerCurrentModelAttributedConversion\x88\x01\x01\x12=\n\x18video_quartile_p100_rate\x18\x84\x01 \x01(\x01HgR\x15videoQuartileP100Rate\x88\x01\x01\x12;\n\x17video_quartile_p25_rate\x18\x85\x01 \x01(\x01HhR\x14videoQuartileP25Rate\x88\x01\x01\x12;\n\x17video_quartile_p50_rate\x18\x86\x01 \x01(\x01HiR\x14videoQuartileP50Rate\x88\x01\x01\x12;\n\x17video_quartile_p75_rate\x18\x87\x01 \x01(\x01HjR\x14videoQuartileP75Rate\x88\x01\x01\x12,\n\x0fvideo_view_rate\x18\x99\x01 \x01(\x01HkR\rvideoViewRate\x88\x01\x01\x12%\n\x0bvideo_views\x18\x9a\x01 \x01(\x03HlR\nvideoViews\x88\x01\x01\x12>\n\x18view_through_conversions\x18\x9b\x01 \x01(\x03HmR\x16viewThroughConversions\x88\x01\x01\x12:\n\x19sk_ad_network_conversions\x18\xf6\x01 \x01(\x03R\x16skAdNetworkConversionsB%\n#_absolute_top_impression_percentageB\x12\n\x10_active_view_cpmB\x12\n\x10_active_view_ctrB\x1a\n\x18_active_view_impressionsB\x1c\n\x1a_active_view_measurabilityB%\n#_active_view_measurable_cost_microsB%\n#_active_view_measurable_impressionsB\x1a\n\x18_active_view_viewabilityB)\n\'_all_conversions_from_interactions_rateB\x18\n\x16_all_conversions_valueB\x12\n\x10_all_conversionsB!\n\x1f_all_conversions_value_per_costB%\n#_all_conversions_from_click_to_callB\"\n _all_conversions_from_directionsB:\n8_all_conversions_from_interactions_value_per_interactionB\x1c\n\x1a_all_conversions_from_menuB\x1d\n\x1b_all_conversions_from_orderB(\n&_all_conversions_from_other_engagementB#\n!_all_conversions_from_store_visitB%\n#_all_conversions_from_store_websiteB\x0f\n\r_average_costB\x0e\n\x0c_average_cpcB\x0e\n\x0c_average_cpeB\x0e\n\x0c_average_cpmB\x0e\n\x0c_average_cpvB\x15\n\x13_average_page_viewsB\x17\n\x15_average_time_on_siteB\x1c\n\x1a_benchmark_average_max_cpcB\x10\n\x0e_benchmark_ctrB\x0e\n\x0c_bounce_rateB\t\n\x07_clicksB\x12\n\x10_combined_clicksB\x1c\n\x1a_combined_clicks_per_queryB\x13\n\x11_combined_queriesB\'\n%_content_budget_lost_impression_shareB\x1b\n\x19_content_impression_shareB-\n+_conversion_last_received_request_date_timeB\"\n _conversion_last_conversion_dateB%\n#_content_rank_lost_impression_shareB%\n#_conversions_from_interactions_rateB\x14\n\x12_conversions_valueB\x1d\n\x1b_conversions_value_per_costB6\n4_conversions_from_interactions_value_per_interactionB\x0e\n\x0c_conversionsB\x0e\n\x0c_cost_microsB\x1b\n\x19_cost_per_all_conversionsB\x16\n\x14_cost_per_conversionB/\n-_cost_per_current_model_attributed_conversionB\x1b\n\x19_cross_device_conversionsB\x06\n\x04_ctrB\'\n%_current_model_attributed_conversionsB>\n<_current_model_attributed_conversions_from_interactions_rateBO\nM_current_model_attributed_conversions_from_interactions_value_per_interactionB-\n+_current_model_attributed_conversions_valueB6\n4_current_model_attributed_conversions_value_per_costB\x12\n\x10_engagement_rateB\x0e\n\x0c_engagementsB\"\n _hotel_average_lead_value_microsB$\n\"_hotel_price_difference_percentageB\x1d\n\x1b_hotel_eligible_impressionsB\x1b\n\x19_historical_quality_scoreB\x11\n\x0f_gmail_forwardsB\x0e\n\x0c_gmail_savesB\x19\n\x17_gmail_secondary_clicksB\x1f\n\x1d_impressions_from_store_reachB\x0e\n\x0c_impressionsB\x13\n\x11_interaction_rateB\x0f\n\r_interactionsB\x15\n\x13_invalid_click_rateB\x11\n\x0f_invalid_clicksB\x10\n\x0e_message_chatsB\x16\n\x14_message_impressionsB\x14\n\x12_message_chat_rateB$\n\"_mobile_friendly_clicks_percentageB\x11\n\x0f_organic_clicksB\x1b\n\x19_organic_clicks_per_queryB\x16\n\x14_organic_impressionsB \n\x1e_organic_impressions_per_queryB\x12\n\x10_organic_queriesB\x17\n\x15_percent_new_visitorsB\x0e\n\x0c_phone_callsB\x14\n\x12_phone_impressionsB\x15\n\x13_phone_through_rateB\x0f\n\r_relative_ctrB\'\n%_search_absolute_top_impression_shareB3\n1_search_budget_lost_absolute_top_impression_shareB&\n$_search_budget_lost_impression_shareB*\n(_search_budget_lost_top_impression_shareB\x15\n\x13_search_click_shareB&\n$_search_exact_match_impression_shareB\x1a\n\x18_search_impression_shareB1\n/_search_rank_lost_absolute_top_impression_shareB$\n\"_search_rank_lost_impression_shareB(\n&_search_rank_lost_top_impression_shareB\x1e\n\x1c_search_top_impression_shareB\x0e\n\x0c_speed_scoreB\x1c\n\x1a_top_impression_percentageB3\n1_valid_accelerated_mobile_pages_clicks_percentageB\x1c\n\x1a_value_per_all_conversionsB/\n-_value_per_all_conversions_by_conversion_dateB\x17\n\x15_value_per_conversionB+\n)_value_per_conversions_by_conversion_dateB0\n._value_per_current_model_attributed_conversionB\x1b\n\x19_video_quartile_p100_rateB\x1a\n\x18_video_quartile_p25_rateB\x1a\n\x18_video_quartile_p50_rateB\x1a\n\x18_video_quartile_p75_rateB\x12\n\x10_video_view_rateB\x0e\n\x0c_video_viewsB\x1b\n\x19_view_through_conversionsB\xe7\x01\n\"com.google.ads.googleads.v7.commonB\x0cMetricsProtoP\x01ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v7/common;common\xa2\x02\x03GAA\xaa\x02\x1eGoogle.Ads.GoogleAds.V7.Common\xca\x02\x1eGoogle\\Ads\\GoogleAds\\V7\\Common\xea\x02\"Google::Ads::GoogleAds::V7::Commonb\x06proto3')



_METRICS = DESCRIPTOR.message_types_by_name['Metrics']
Metrics = _reflection.GeneratedProtocolMessageType('Metrics', (_message.Message,), {
  'DESCRIPTOR' : _METRICS,
  '__module__' : 'google.ads.googleads.v7.common.metrics_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v7.common.Metrics)
  })
_sym_db.RegisterMessage(Metrics)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\"com.google.ads.googleads.v7.commonB\014MetricsProtoP\001ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v7/common;common\242\002\003GAA\252\002\036Google.Ads.GoogleAds.V7.Common\312\002\036Google\\Ads\\GoogleAds\\V7\\Common\352\002\"Google::Ads::GoogleAds::V7::Common'
  _METRICS._serialized_start=229
  _METRICS._serialized_end=11862
# @@protoc_insertion_point(module_scope)
