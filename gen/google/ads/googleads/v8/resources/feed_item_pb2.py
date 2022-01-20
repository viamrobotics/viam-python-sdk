# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v8/resources/feed_item.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.googleads.v8.common import custom_parameter_pb2 as google_dot_ads_dot_googleads_dot_v8_dot_common_dot_custom__parameter__pb2
from google.ads.googleads.v8.common import feed_common_pb2 as google_dot_ads_dot_googleads_dot_v8_dot_common_dot_feed__common__pb2
from google.ads.googleads.v8.common import policy_pb2 as google_dot_ads_dot_googleads_dot_v8_dot_common_dot_policy__pb2
from google.ads.googleads.v8.enums import feed_item_quality_approval_status_pb2 as google_dot_ads_dot_googleads_dot_v8_dot_enums_dot_feed__item__quality__approval__status__pb2
from google.ads.googleads.v8.enums import feed_item_quality_disapproval_reason_pb2 as google_dot_ads_dot_googleads_dot_v8_dot_enums_dot_feed__item__quality__disapproval__reason__pb2
from google.ads.googleads.v8.enums import feed_item_status_pb2 as google_dot_ads_dot_googleads_dot_v8_dot_enums_dot_feed__item__status__pb2
from google.ads.googleads.v8.enums import feed_item_validation_status_pb2 as google_dot_ads_dot_googleads_dot_v8_dot_enums_dot_feed__item__validation__status__pb2
from google.ads.googleads.v8.enums import geo_targeting_restriction_pb2 as google_dot_ads_dot_googleads_dot_v8_dot_enums_dot_geo__targeting__restriction__pb2
from google.ads.googleads.v8.enums import placeholder_type_pb2 as google_dot_ads_dot_googleads_dot_v8_dot_enums_dot_placeholder__type__pb2
from google.ads.googleads.v8.enums import policy_approval_status_pb2 as google_dot_ads_dot_googleads_dot_v8_dot_enums_dot_policy__approval__status__pb2
from google.ads.googleads.v8.enums import policy_review_status_pb2 as google_dot_ads_dot_googleads_dot_v8_dot_enums_dot_policy__review__status__pb2
from google.ads.googleads.v8.errors import feed_item_validation_error_pb2 as google_dot_ads_dot_googleads_dot_v8_dot_errors_dot_feed__item__validation__error__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1google/ads/googleads/v8/resources/feed_item.proto\x12!google.ads.googleads.v8.resources\x1a\x35google/ads/googleads/v8/common/custom_parameter.proto\x1a\x30google/ads/googleads/v8/common/feed_common.proto\x1a+google/ads/googleads/v8/common/policy.proto\x1a\x45google/ads/googleads/v8/enums/feed_item_quality_approval_status.proto\x1aHgoogle/ads/googleads/v8/enums/feed_item_quality_disapproval_reason.proto\x1a\x34google/ads/googleads/v8/enums/feed_item_status.proto\x1a?google/ads/googleads/v8/enums/feed_item_validation_status.proto\x1a=google/ads/googleads/v8/enums/geo_targeting_restriction.proto\x1a\x34google/ads/googleads/v8/enums/placeholder_type.proto\x1a:google/ads/googleads/v8/enums/policy_approval_status.proto\x1a\x38google/ads/googleads/v8/enums/policy_review_status.proto\x1a?google/ads/googleads/v8/errors/feed_item_validation_error.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1cgoogle/api/annotations.proto\"\xce\x07\n\x08\x46\x65\x65\x64Item\x12O\n\rresource_name\x18\x01 \x01(\tB*\xe2\x41\x01\x05\xfa\x41#\n!googleads.googleapis.com/FeedItemR\x0cresourceName\x12?\n\x04\x66\x65\x65\x64\x18\x0b \x01(\tB&\xe2\x41\x01\x05\xfa\x41\x1f\n\x1dgoogleads.googleapis.com/FeedH\x00R\x04\x66\x65\x65\x64\x88\x01\x01\x12\x19\n\x02id\x18\x0c \x01(\x03\x42\x04\xe2\x41\x01\x03H\x01R\x02id\x88\x01\x01\x12+\n\x0fstart_date_time\x18\r \x01(\tH\x02R\rstartDateTime\x88\x01\x01\x12\'\n\rend_date_time\x18\x0e \x01(\tH\x03R\x0b\x65ndDateTime\x88\x01\x01\x12\x64\n\x10\x61ttribute_values\x18\x06 \x03(\x0b\x32\x39.google.ads.googleads.v8.resources.FeedItemAttributeValueR\x0f\x61ttributeValues\x12\x8e\x01\n\x19geo_targeting_restriction\x18\x07 \x01(\x0e\x32R.google.ads.googleads.v8.enums.GeoTargetingRestrictionEnum.GeoTargetingRestrictionR\x17geoTargetingRestriction\x12\x63\n\x15url_custom_parameters\x18\x08 \x03(\x0b\x32/.google.ads.googleads.v8.common.CustomParameterR\x13urlCustomParameters\x12^\n\x06status\x18\t \x01(\x0e\x32@.google.ads.googleads.v8.enums.FeedItemStatusEnum.FeedItemStatusB\x04\xe2\x41\x01\x03R\x06status\x12i\n\x0cpolicy_infos\x18\n \x03(\x0b\x32@.google.ads.googleads.v8.resources.FeedItemPlaceholderPolicyInfoB\x04\xe2\x41\x01\x03R\x0bpolicyInfos:b\xea\x41_\n!googleads.googleapis.com/FeedItem\x12:customers/{customer_id}/feedItems/{feed_id}~{feed_item_id}B\x07\n\x05_feedB\x05\n\x03_idB\x12\n\x10_start_date_timeB\x10\n\x0e_end_date_time\"\xa9\x04\n\x16\x46\x65\x65\x64ItemAttributeValue\x12/\n\x11\x66\x65\x65\x64_attribute_id\x18\x0b \x01(\x03H\x00R\x0f\x66\x65\x65\x64\x41ttributeId\x88\x01\x01\x12(\n\rinteger_value\x18\x0c \x01(\x03H\x01R\x0cintegerValue\x88\x01\x01\x12(\n\rboolean_value\x18\r \x01(\x08H\x02R\x0c\x62ooleanValue\x88\x01\x01\x12&\n\x0cstring_value\x18\x0e \x01(\tH\x03R\x0bstringValue\x88\x01\x01\x12&\n\x0c\x64ouble_value\x18\x0f \x01(\x01H\x04R\x0b\x64oubleValue\x88\x01\x01\x12\x46\n\x0bprice_value\x18\x06 \x01(\x0b\x32%.google.ads.googleads.v8.common.MoneyR\npriceValue\x12%\n\x0einteger_values\x18\x10 \x03(\x03R\rintegerValues\x12%\n\x0e\x62oolean_values\x18\x11 \x03(\x08R\rbooleanValues\x12#\n\rstring_values\x18\x12 \x03(\tR\x0cstringValues\x12#\n\rdouble_values\x18\x13 \x03(\x01R\x0c\x64oubleValuesB\x14\n\x12_feed_attribute_idB\x10\n\x0e_integer_valueB\x10\n\x0e_boolean_valueB\x0f\n\r_string_valueB\x0f\n\r_double_value\"\xa5\t\n\x1d\x46\x65\x65\x64ItemPlaceholderPolicyInfo\x12|\n\x15placeholder_type_enum\x18\n \x01(\x0e\x32\x42.google.ads.googleads.v8.enums.PlaceholderTypeEnum.PlaceholderTypeB\x04\xe2\x41\x01\x03R\x13placeholderTypeEnum\x12\x46\n\x1a\x66\x65\x65\x64_mapping_resource_name\x18\x0b \x01(\tB\x04\xe2\x41\x01\x03H\x00R\x17\x66\x65\x65\x64MappingResourceName\x88\x01\x01\x12s\n\rreview_status\x18\x03 \x01(\x0e\x32H.google.ads.googleads.v8.enums.PolicyReviewStatusEnum.PolicyReviewStatusB\x04\xe2\x41\x01\x03R\x0creviewStatus\x12{\n\x0f\x61pproval_status\x18\x04 \x01(\x0e\x32L.google.ads.googleads.v8.enums.PolicyApprovalStatusEnum.PolicyApprovalStatusB\x04\xe2\x41\x01\x03R\x0e\x61pprovalStatus\x12h\n\x14policy_topic_entries\x18\x05 \x03(\x0b\x32\x30.google.ads.googleads.v8.common.PolicyTopicEntryB\x04\xe2\x41\x01\x03R\x12policyTopicEntries\x12\x87\x01\n\x11validation_status\x18\x06 \x01(\x0e\x32T.google.ads.googleads.v8.enums.FeedItemValidationStatusEnum.FeedItemValidationStatusB\x04\xe2\x41\x01\x03R\x10validationStatus\x12m\n\x11validation_errors\x18\x07 \x03(\x0b\x32:.google.ads.googleads.v8.resources.FeedItemValidationErrorB\x04\xe2\x41\x01\x03R\x10validationErrors\x12\x9c\x01\n\x17quality_approval_status\x18\x08 \x01(\x0e\x32^.google.ads.googleads.v8.enums.FeedItemQualityApprovalStatusEnum.FeedItemQualityApprovalStatusB\x04\xe2\x41\x01\x03R\x15qualityApprovalStatus\x12\xaa\x01\n\x1bquality_disapproval_reasons\x18\t \x03(\x0e\x32\x64.google.ads.googleads.v8.enums.FeedItemQualityDisapprovalReasonEnum.FeedItemQualityDisapprovalReasonB\x04\xe2\x41\x01\x03R\x19qualityDisapprovalReasonsB\x1d\n\x1b_feed_mapping_resource_name\"\xca\x02\n\x17\x46\x65\x65\x64ItemValidationError\x12\x84\x01\n\x10validation_error\x18\x01 \x01(\x0e\x32S.google.ads.googleads.v8.errors.FeedItemValidationErrorEnum.FeedItemValidationErrorB\x04\xe2\x41\x01\x03R\x0fvalidationError\x12+\n\x0b\x64\x65scription\x18\x06 \x01(\tB\x04\xe2\x41\x01\x03H\x00R\x0b\x64\x65scription\x88\x01\x01\x12\x32\n\x12\x66\x65\x65\x64_attribute_ids\x18\x07 \x03(\x03\x42\x04\xe2\x41\x01\x03R\x10\x66\x65\x65\x64\x41ttributeIds\x12(\n\nextra_info\x18\x08 \x01(\tB\x04\xe2\x41\x01\x03H\x01R\textraInfo\x88\x01\x01\x42\x0e\n\x0c_descriptionB\r\n\x0b_extra_infoB\xfa\x01\n%com.google.ads.googleads.v8.resourcesB\rFeedItemProtoP\x01ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v8/resources;resources\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V8.Resources\xca\x02!Google\\Ads\\GoogleAds\\V8\\Resources\xea\x02%Google::Ads::GoogleAds::V8::Resourcesb\x06proto3')



_FEEDITEM = DESCRIPTOR.message_types_by_name['FeedItem']
_FEEDITEMATTRIBUTEVALUE = DESCRIPTOR.message_types_by_name['FeedItemAttributeValue']
_FEEDITEMPLACEHOLDERPOLICYINFO = DESCRIPTOR.message_types_by_name['FeedItemPlaceholderPolicyInfo']
_FEEDITEMVALIDATIONERROR = DESCRIPTOR.message_types_by_name['FeedItemValidationError']
FeedItem = _reflection.GeneratedProtocolMessageType('FeedItem', (_message.Message,), {
  'DESCRIPTOR' : _FEEDITEM,
  '__module__' : 'google.ads.googleads.v8.resources.feed_item_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v8.resources.FeedItem)
  })
_sym_db.RegisterMessage(FeedItem)

FeedItemAttributeValue = _reflection.GeneratedProtocolMessageType('FeedItemAttributeValue', (_message.Message,), {
  'DESCRIPTOR' : _FEEDITEMATTRIBUTEVALUE,
  '__module__' : 'google.ads.googleads.v8.resources.feed_item_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v8.resources.FeedItemAttributeValue)
  })
_sym_db.RegisterMessage(FeedItemAttributeValue)

FeedItemPlaceholderPolicyInfo = _reflection.GeneratedProtocolMessageType('FeedItemPlaceholderPolicyInfo', (_message.Message,), {
  'DESCRIPTOR' : _FEEDITEMPLACEHOLDERPOLICYINFO,
  '__module__' : 'google.ads.googleads.v8.resources.feed_item_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v8.resources.FeedItemPlaceholderPolicyInfo)
  })
_sym_db.RegisterMessage(FeedItemPlaceholderPolicyInfo)

FeedItemValidationError = _reflection.GeneratedProtocolMessageType('FeedItemValidationError', (_message.Message,), {
  'DESCRIPTOR' : _FEEDITEMVALIDATIONERROR,
  '__module__' : 'google.ads.googleads.v8.resources.feed_item_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v8.resources.FeedItemValidationError)
  })
_sym_db.RegisterMessage(FeedItemValidationError)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n%com.google.ads.googleads.v8.resourcesB\rFeedItemProtoP\001ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v8/resources;resources\242\002\003GAA\252\002!Google.Ads.GoogleAds.V8.Resources\312\002!Google\\Ads\\GoogleAds\\V8\\Resources\352\002%Google::Ads::GoogleAds::V8::Resources'
  _FEEDITEM.fields_by_name['resource_name']._options = None
  _FEEDITEM.fields_by_name['resource_name']._serialized_options = b'\342A\001\005\372A#\n!googleads.googleapis.com/FeedItem'
  _FEEDITEM.fields_by_name['feed']._options = None
  _FEEDITEM.fields_by_name['feed']._serialized_options = b'\342A\001\005\372A\037\n\035googleads.googleapis.com/Feed'
  _FEEDITEM.fields_by_name['id']._options = None
  _FEEDITEM.fields_by_name['id']._serialized_options = b'\342A\001\003'
  _FEEDITEM.fields_by_name['status']._options = None
  _FEEDITEM.fields_by_name['status']._serialized_options = b'\342A\001\003'
  _FEEDITEM.fields_by_name['policy_infos']._options = None
  _FEEDITEM.fields_by_name['policy_infos']._serialized_options = b'\342A\001\003'
  _FEEDITEM._options = None
  _FEEDITEM._serialized_options = b'\352A_\n!googleads.googleapis.com/FeedItem\022:customers/{customer_id}/feedItems/{feed_id}~{feed_item_id}'
  _FEEDITEMPLACEHOLDERPOLICYINFO.fields_by_name['placeholder_type_enum']._options = None
  _FEEDITEMPLACEHOLDERPOLICYINFO.fields_by_name['placeholder_type_enum']._serialized_options = b'\342A\001\003'
  _FEEDITEMPLACEHOLDERPOLICYINFO.fields_by_name['feed_mapping_resource_name']._options = None
  _FEEDITEMPLACEHOLDERPOLICYINFO.fields_by_name['feed_mapping_resource_name']._serialized_options = b'\342A\001\003'
  _FEEDITEMPLACEHOLDERPOLICYINFO.fields_by_name['review_status']._options = None
  _FEEDITEMPLACEHOLDERPOLICYINFO.fields_by_name['review_status']._serialized_options = b'\342A\001\003'
  _FEEDITEMPLACEHOLDERPOLICYINFO.fields_by_name['approval_status']._options = None
  _FEEDITEMPLACEHOLDERPOLICYINFO.fields_by_name['approval_status']._serialized_options = b'\342A\001\003'
  _FEEDITEMPLACEHOLDERPOLICYINFO.fields_by_name['policy_topic_entries']._options = None
  _FEEDITEMPLACEHOLDERPOLICYINFO.fields_by_name['policy_topic_entries']._serialized_options = b'\342A\001\003'
  _FEEDITEMPLACEHOLDERPOLICYINFO.fields_by_name['validation_status']._options = None
  _FEEDITEMPLACEHOLDERPOLICYINFO.fields_by_name['validation_status']._serialized_options = b'\342A\001\003'
  _FEEDITEMPLACEHOLDERPOLICYINFO.fields_by_name['validation_errors']._options = None
  _FEEDITEMPLACEHOLDERPOLICYINFO.fields_by_name['validation_errors']._serialized_options = b'\342A\001\003'
  _FEEDITEMPLACEHOLDERPOLICYINFO.fields_by_name['quality_approval_status']._options = None
  _FEEDITEMPLACEHOLDERPOLICYINFO.fields_by_name['quality_approval_status']._serialized_options = b'\342A\001\003'
  _FEEDITEMPLACEHOLDERPOLICYINFO.fields_by_name['quality_disapproval_reasons']._options = None
  _FEEDITEMPLACEHOLDERPOLICYINFO.fields_by_name['quality_disapproval_reasons']._serialized_options = b'\342A\001\003'
  _FEEDITEMVALIDATIONERROR.fields_by_name['validation_error']._options = None
  _FEEDITEMVALIDATIONERROR.fields_by_name['validation_error']._serialized_options = b'\342A\001\003'
  _FEEDITEMVALIDATIONERROR.fields_by_name['description']._options = None
  _FEEDITEMVALIDATIONERROR.fields_by_name['description']._serialized_options = b'\342A\001\003'
  _FEEDITEMVALIDATIONERROR.fields_by_name['feed_attribute_ids']._options = None
  _FEEDITEMVALIDATIONERROR.fields_by_name['feed_attribute_ids']._serialized_options = b'\342A\001\003'
  _FEEDITEMVALIDATIONERROR.fields_by_name['extra_info']._options = None
  _FEEDITEMVALIDATIONERROR.fields_by_name['extra_info']._serialized_options = b'\342A\001\003'
  _FEEDITEM._serialized_start=893
  _FEEDITEM._serialized_end=1867
  _FEEDITEMATTRIBUTEVALUE._serialized_start=1870
  _FEEDITEMATTRIBUTEVALUE._serialized_end=2423
  _FEEDITEMPLACEHOLDERPOLICYINFO._serialized_start=2426
  _FEEDITEMPLACEHOLDERPOLICYINFO._serialized_end=3615
  _FEEDITEMVALIDATIONERROR._serialized_start=3618
  _FEEDITEMVALIDATIONERROR._serialized_end=3948
# @@protoc_insertion_point(module_scope)
