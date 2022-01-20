# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v8/resources/bidding_strategy.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.googleads.v8.common import bidding_pb2 as google_dot_ads_dot_googleads_dot_v8_dot_common_dot_bidding__pb2
from google.ads.googleads.v8.enums import bidding_strategy_status_pb2 as google_dot_ads_dot_googleads_dot_v8_dot_enums_dot_bidding__strategy__status__pb2
from google.ads.googleads.v8.enums import bidding_strategy_type_pb2 as google_dot_ads_dot_googleads_dot_v8_dot_enums_dot_bidding__strategy__type__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n8google/ads/googleads/v8/resources/bidding_strategy.proto\x12!google.ads.googleads.v8.resources\x1a,google/ads/googleads/v8/common/bidding.proto\x1a;google/ads/googleads/v8/enums/bidding_strategy_status.proto\x1a\x39google/ads/googleads/v8/enums/bidding_strategy_type.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1cgoogle/api/annotations.proto\"\xc2\x0b\n\x0f\x42iddingStrategy\x12V\n\rresource_name\x18\x01 \x01(\tB1\xe2\x41\x01\x05\xfa\x41*\n(googleads.googleapis.com/BiddingStrategyR\x0cresourceName\x12\x19\n\x02id\x18\x10 \x01(\x03\x42\x04\xe2\x41\x01\x03H\x01R\x02id\x88\x01\x01\x12\x17\n\x04name\x18\x11 \x01(\tH\x02R\x04name\x88\x01\x01\x12l\n\x06status\x18\x0f \x01(\x0e\x32N.google.ads.googleads.v8.enums.BiddingStrategyStatusEnum.BiddingStrategyStatusB\x04\xe2\x41\x01\x03R\x06status\x12\x64\n\x04type\x18\x05 \x01(\x0e\x32J.google.ads.googleads.v8.enums.BiddingStrategyTypeEnum.BiddingStrategyTypeB\x04\xe2\x41\x01\x03R\x04type\x12)\n\rcurrency_code\x18\x17 \x01(\tB\x04\xe2\x41\x01\x05R\x0c\x63urrencyCode\x12\x41\n\x17\x65\x66\x66\x65\x63tive_currency_code\x18\x14 \x01(\tB\x04\xe2\x41\x01\x03H\x03R\x15\x65\x66\x66\x65\x63tiveCurrencyCode\x88\x01\x01\x12\x30\n\x0e\x63\x61mpaign_count\x18\x12 \x01(\x03\x42\x04\xe2\x41\x01\x03H\x04R\rcampaignCount\x88\x01\x01\x12\x46\n\x1anon_removed_campaign_count\x18\x13 \x01(\x03\x42\x04\xe2\x41\x01\x03H\x05R\x17nonRemovedCampaignCount\x88\x01\x01\x12P\n\x0c\x65nhanced_cpc\x18\x07 \x01(\x0b\x32+.google.ads.googleads.v8.common.EnhancedCpcH\x00R\x0b\x65nhancedCpc\x12u\n\x19maximize_conversion_value\x18\x15 \x01(\x0b\x32\x37.google.ads.googleads.v8.common.MaximizeConversionValueH\x00R\x17maximizeConversionValue\x12h\n\x14maximize_conversions\x18\x16 \x01(\x0b\x32\x33.google.ads.googleads.v8.common.MaximizeConversionsH\x00R\x13maximizeConversions\x12J\n\ntarget_cpa\x18\t \x01(\x0b\x32).google.ads.googleads.v8.common.TargetCpaH\x00R\ttargetCpa\x12o\n\x17target_impression_share\x18\x30 \x01(\x0b\x32\x35.google.ads.googleads.v8.common.TargetImpressionShareH\x00R\x15targetImpressionShare\x12M\n\x0btarget_roas\x18\x0b \x01(\x0b\x32*.google.ads.googleads.v8.common.TargetRoasH\x00R\ntargetRoas\x12P\n\x0ctarget_spend\x18\x0c \x01(\x0b\x32+.google.ads.googleads.v8.common.TargetSpendH\x00R\x0btargetSpend:n\xea\x41k\n(googleads.googleapis.com/BiddingStrategy\x12?customers/{customer_id}/biddingStrategies/{bidding_strategy_id}B\x08\n\x06schemeB\x05\n\x03_idB\x07\n\x05_nameB\x1a\n\x18_effective_currency_codeB\x11\n\x0f_campaign_countB\x1d\n\x1b_non_removed_campaign_countB\x81\x02\n%com.google.ads.googleads.v8.resourcesB\x14\x42iddingStrategyProtoP\x01ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v8/resources;resources\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V8.Resources\xca\x02!Google\\Ads\\GoogleAds\\V8\\Resources\xea\x02%Google::Ads::GoogleAds::V8::Resourcesb\x06proto3')



_BIDDINGSTRATEGY = DESCRIPTOR.message_types_by_name['BiddingStrategy']
BiddingStrategy = _reflection.GeneratedProtocolMessageType('BiddingStrategy', (_message.Message,), {
  'DESCRIPTOR' : _BIDDINGSTRATEGY,
  '__module__' : 'google.ads.googleads.v8.resources.bidding_strategy_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v8.resources.BiddingStrategy)
  })
_sym_db.RegisterMessage(BiddingStrategy)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n%com.google.ads.googleads.v8.resourcesB\024BiddingStrategyProtoP\001ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v8/resources;resources\242\002\003GAA\252\002!Google.Ads.GoogleAds.V8.Resources\312\002!Google\\Ads\\GoogleAds\\V8\\Resources\352\002%Google::Ads::GoogleAds::V8::Resources'
  _BIDDINGSTRATEGY.fields_by_name['resource_name']._options = None
  _BIDDINGSTRATEGY.fields_by_name['resource_name']._serialized_options = b'\342A\001\005\372A*\n(googleads.googleapis.com/BiddingStrategy'
  _BIDDINGSTRATEGY.fields_by_name['id']._options = None
  _BIDDINGSTRATEGY.fields_by_name['id']._serialized_options = b'\342A\001\003'
  _BIDDINGSTRATEGY.fields_by_name['status']._options = None
  _BIDDINGSTRATEGY.fields_by_name['status']._serialized_options = b'\342A\001\003'
  _BIDDINGSTRATEGY.fields_by_name['type']._options = None
  _BIDDINGSTRATEGY.fields_by_name['type']._serialized_options = b'\342A\001\003'
  _BIDDINGSTRATEGY.fields_by_name['currency_code']._options = None
  _BIDDINGSTRATEGY.fields_by_name['currency_code']._serialized_options = b'\342A\001\005'
  _BIDDINGSTRATEGY.fields_by_name['effective_currency_code']._options = None
  _BIDDINGSTRATEGY.fields_by_name['effective_currency_code']._serialized_options = b'\342A\001\003'
  _BIDDINGSTRATEGY.fields_by_name['campaign_count']._options = None
  _BIDDINGSTRATEGY.fields_by_name['campaign_count']._serialized_options = b'\342A\001\003'
  _BIDDINGSTRATEGY.fields_by_name['non_removed_campaign_count']._options = None
  _BIDDINGSTRATEGY.fields_by_name['non_removed_campaign_count']._serialized_options = b'\342A\001\003'
  _BIDDINGSTRATEGY._options = None
  _BIDDINGSTRATEGY._serialized_options = b'\352Ak\n(googleads.googleapis.com/BiddingStrategy\022?customers/{customer_id}/biddingStrategies/{bidding_strategy_id}'
  _BIDDINGSTRATEGY._serialized_start=352
  _BIDDINGSTRATEGY._serialized_end=1826
# @@protoc_insertion_point(module_scope)
