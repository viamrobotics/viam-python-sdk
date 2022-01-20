# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v9/services/keyword_plan_idea_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.googleads.v9.common import keyword_plan_common_pb2 as google_dot_ads_dot_googleads_dot_v9_dot_common_dot_keyword__plan__common__pb2
from google.ads.googleads.v9.enums import keyword_plan_keyword_annotation_pb2 as google_dot_ads_dot_googleads_dot_v9_dot_enums_dot_keyword__plan__keyword__annotation__pb2
from google.ads.googleads.v9.enums import keyword_plan_network_pb2 as google_dot_ads_dot_googleads_dot_v9_dot_enums_dot_keyword__plan__network__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import client_pb2 as google_dot_api_dot_client__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n@google/ads/googleads/v9/services/keyword_plan_idea_service.proto\x12 google.ads.googleads.v9.services\x1a\x38google/ads/googleads/v9/common/keyword_plan_common.proto\x1a\x43google/ads/googleads/v9/enums/keyword_plan_keyword_annotation.proto\x1a\x38google/ads/googleads/v9/enums/keyword_plan_network.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\"\xd3\x08\n\x1bGenerateKeywordIdeasRequest\x12\x1f\n\x0b\x63ustomer_id\x18\x01 \x01(\tR\ncustomerId\x12\x1f\n\x08language\x18\x0e \x01(\tH\x01R\x08language\x88\x01\x01\x12\x30\n\x14geo_target_constants\x18\x0f \x03(\tR\x12geoTargetConstants\x12\x34\n\x16include_adult_keywords\x18\n \x01(\x08R\x14includeAdultKeywords\x12\x1d\n\npage_token\x18\x0c \x01(\tR\tpageToken\x12\x1b\n\tpage_size\x18\r \x01(\x05R\x08pageSize\x12z\n\x14keyword_plan_network\x18\t \x01(\x0e\x32H.google.ads.googleads.v9.enums.KeywordPlanNetworkEnum.KeywordPlanNetworkR\x12keywordPlanNetwork\x12\x8b\x01\n\x12keyword_annotation\x18\x11 \x03(\x0e\x32\\.google.ads.googleads.v9.enums.KeywordPlanKeywordAnnotationEnum.KeywordPlanKeywordAnnotationR\x11keywordAnnotation\x12h\n\x11\x61ggregate_metrics\x18\x10 \x01(\x0b\x32;.google.ads.googleads.v9.common.KeywordPlanAggregateMetricsR\x10\x61ggregateMetrics\x12v\n\x1ahistorical_metrics_options\x18\x12 \x01(\x0b\x32\x38.google.ads.googleads.v9.common.HistoricalMetricsOptionsR\x18historicalMetricsOptions\x12\x66\n\x14keyword_and_url_seed\x18\x02 \x01(\x0b\x32\x33.google.ads.googleads.v9.services.KeywordAndUrlSeedH\x00R\x11keywordAndUrlSeed\x12R\n\x0ckeyword_seed\x18\x03 \x01(\x0b\x32-.google.ads.googleads.v9.services.KeywordSeedH\x00R\x0bkeywordSeed\x12\x46\n\x08url_seed\x18\x05 \x01(\x0b\x32).google.ads.googleads.v9.services.UrlSeedH\x00R\x07urlSeed\x12I\n\tsite_seed\x18\x0b \x01(\x0b\x32*.google.ads.googleads.v9.services.SiteSeedH\x00R\x08siteSeedB\x06\n\x04seedB\x0b\n\t_language\"N\n\x11KeywordAndUrlSeed\x12\x15\n\x03url\x18\x03 \x01(\tH\x00R\x03url\x88\x01\x01\x12\x1a\n\x08keywords\x18\x04 \x03(\tR\x08keywordsB\x06\n\x04_url\")\n\x0bKeywordSeed\x12\x1a\n\x08keywords\x18\x02 \x03(\tR\x08keywords\",\n\x08SiteSeed\x12\x17\n\x04site\x18\x02 \x01(\tH\x00R\x04site\x88\x01\x01\x42\x07\n\x05_site\"(\n\x07UrlSeed\x12\x15\n\x03url\x18\x02 \x01(\tH\x00R\x03url\x88\x01\x01\x42\x06\n\x04_url\"\xb8\x02\n\x1bGenerateKeywordIdeaResponse\x12U\n\x07results\x18\x01 \x03(\x0b\x32;.google.ads.googleads.v9.services.GenerateKeywordIdeaResultR\x07results\x12{\n\x18\x61ggregate_metric_results\x18\x04 \x01(\x0b\x32\x41.google.ads.googleads.v9.common.KeywordPlanAggregateMetricResultsR\x16\x61ggregateMetricResults\x12&\n\x0fnext_page_token\x18\x02 \x01(\tR\rnextPageToken\x12\x1d\n\ntotal_size\x18\x03 \x01(\x03R\ttotalSize\"\x92\x02\n\x19GenerateKeywordIdeaResult\x12\x17\n\x04text\x18\x05 \x01(\tH\x00R\x04text\x88\x01\x01\x12n\n\x14keyword_idea_metrics\x18\x03 \x01(\x0b\x32<.google.ads.googleads.v9.common.KeywordPlanHistoricalMetricsR\x12keywordIdeaMetrics\x12\x63\n\x13keyword_annotations\x18\x06 \x01(\x0b\x32\x32.google.ads.googleads.v9.common.KeywordAnnotationsR\x12keywordAnnotationsB\x07\n\x05_text2\xb5\x02\n\x16KeywordPlanIdeaService\x12\xd3\x01\n\x14GenerateKeywordIdeas\x12=.google.ads.googleads.v9.services.GenerateKeywordIdeasRequest\x1a=.google.ads.googleads.v9.services.GenerateKeywordIdeaResponse\"=\x82\xd3\xe4\x93\x02\x37\"2/v9/customers/{customer_id=*}:generateKeywordIdeas:\x01*\x1a\x45\xca\x41\x18googleads.googleapis.com\xd2\x41\'https://www.googleapis.com/auth/adwordsB\x82\x02\n$com.google.ads.googleads.v9.servicesB\x1bKeywordPlanIdeaServiceProtoP\x01ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v9/services;services\xa2\x02\x03GAA\xaa\x02 Google.Ads.GoogleAds.V9.Services\xca\x02 Google\\Ads\\GoogleAds\\V9\\Services\xea\x02$Google::Ads::GoogleAds::V9::Servicesb\x06proto3')



_GENERATEKEYWORDIDEASREQUEST = DESCRIPTOR.message_types_by_name['GenerateKeywordIdeasRequest']
_KEYWORDANDURLSEED = DESCRIPTOR.message_types_by_name['KeywordAndUrlSeed']
_KEYWORDSEED = DESCRIPTOR.message_types_by_name['KeywordSeed']
_SITESEED = DESCRIPTOR.message_types_by_name['SiteSeed']
_URLSEED = DESCRIPTOR.message_types_by_name['UrlSeed']
_GENERATEKEYWORDIDEARESPONSE = DESCRIPTOR.message_types_by_name['GenerateKeywordIdeaResponse']
_GENERATEKEYWORDIDEARESULT = DESCRIPTOR.message_types_by_name['GenerateKeywordIdeaResult']
GenerateKeywordIdeasRequest = _reflection.GeneratedProtocolMessageType('GenerateKeywordIdeasRequest', (_message.Message,), {
  'DESCRIPTOR' : _GENERATEKEYWORDIDEASREQUEST,
  '__module__' : 'google.ads.googleads.v9.services.keyword_plan_idea_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v9.services.GenerateKeywordIdeasRequest)
  })
_sym_db.RegisterMessage(GenerateKeywordIdeasRequest)

KeywordAndUrlSeed = _reflection.GeneratedProtocolMessageType('KeywordAndUrlSeed', (_message.Message,), {
  'DESCRIPTOR' : _KEYWORDANDURLSEED,
  '__module__' : 'google.ads.googleads.v9.services.keyword_plan_idea_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v9.services.KeywordAndUrlSeed)
  })
_sym_db.RegisterMessage(KeywordAndUrlSeed)

KeywordSeed = _reflection.GeneratedProtocolMessageType('KeywordSeed', (_message.Message,), {
  'DESCRIPTOR' : _KEYWORDSEED,
  '__module__' : 'google.ads.googleads.v9.services.keyword_plan_idea_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v9.services.KeywordSeed)
  })
_sym_db.RegisterMessage(KeywordSeed)

SiteSeed = _reflection.GeneratedProtocolMessageType('SiteSeed', (_message.Message,), {
  'DESCRIPTOR' : _SITESEED,
  '__module__' : 'google.ads.googleads.v9.services.keyword_plan_idea_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v9.services.SiteSeed)
  })
_sym_db.RegisterMessage(SiteSeed)

UrlSeed = _reflection.GeneratedProtocolMessageType('UrlSeed', (_message.Message,), {
  'DESCRIPTOR' : _URLSEED,
  '__module__' : 'google.ads.googleads.v9.services.keyword_plan_idea_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v9.services.UrlSeed)
  })
_sym_db.RegisterMessage(UrlSeed)

GenerateKeywordIdeaResponse = _reflection.GeneratedProtocolMessageType('GenerateKeywordIdeaResponse', (_message.Message,), {
  'DESCRIPTOR' : _GENERATEKEYWORDIDEARESPONSE,
  '__module__' : 'google.ads.googleads.v9.services.keyword_plan_idea_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v9.services.GenerateKeywordIdeaResponse)
  })
_sym_db.RegisterMessage(GenerateKeywordIdeaResponse)

GenerateKeywordIdeaResult = _reflection.GeneratedProtocolMessageType('GenerateKeywordIdeaResult', (_message.Message,), {
  'DESCRIPTOR' : _GENERATEKEYWORDIDEARESULT,
  '__module__' : 'google.ads.googleads.v9.services.keyword_plan_idea_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v9.services.GenerateKeywordIdeaResult)
  })
_sym_db.RegisterMessage(GenerateKeywordIdeaResult)

_KEYWORDPLANIDEASERVICE = DESCRIPTOR.services_by_name['KeywordPlanIdeaService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n$com.google.ads.googleads.v9.servicesB\033KeywordPlanIdeaServiceProtoP\001ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v9/services;services\242\002\003GAA\252\002 Google.Ads.GoogleAds.V9.Services\312\002 Google\\Ads\\GoogleAds\\V9\\Services\352\002$Google::Ads::GoogleAds::V9::Services'
  _KEYWORDPLANIDEASERVICE._options = None
  _KEYWORDPLANIDEASERVICE._serialized_options = b'\312A\030googleads.googleapis.com\322A\'https://www.googleapis.com/auth/adwords'
  _KEYWORDPLANIDEASERVICE.methods_by_name['GenerateKeywordIdeas']._options = None
  _KEYWORDPLANIDEASERVICE.methods_by_name['GenerateKeywordIdeas']._serialized_options = b'\202\323\344\223\0027\"2/v9/customers/{customer_id=*}:generateKeywordIdeas:\001*'
  _GENERATEKEYWORDIDEASREQUEST._serialized_start=343
  _GENERATEKEYWORDIDEASREQUEST._serialized_end=1450
  _KEYWORDANDURLSEED._serialized_start=1452
  _KEYWORDANDURLSEED._serialized_end=1530
  _KEYWORDSEED._serialized_start=1532
  _KEYWORDSEED._serialized_end=1573
  _SITESEED._serialized_start=1575
  _SITESEED._serialized_end=1619
  _URLSEED._serialized_start=1621
  _URLSEED._serialized_end=1661
  _GENERATEKEYWORDIDEARESPONSE._serialized_start=1664
  _GENERATEKEYWORDIDEARESPONSE._serialized_end=1976
  _GENERATEKEYWORDIDEARESULT._serialized_start=1979
  _GENERATEKEYWORDIDEARESULT._serialized_end=2253
  _KEYWORDPLANIDEASERVICE._serialized_start=2256
  _KEYWORDPLANIDEASERVICE._serialized_end=2565
# @@protoc_insertion_point(module_scope)
