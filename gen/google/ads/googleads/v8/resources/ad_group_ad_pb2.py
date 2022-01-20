# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v8/resources/ad_group_ad.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.googleads.v8.common import policy_pb2 as google_dot_ads_dot_googleads_dot_v8_dot_common_dot_policy__pb2
from google.ads.googleads.v8.enums import ad_group_ad_status_pb2 as google_dot_ads_dot_googleads_dot_v8_dot_enums_dot_ad__group__ad__status__pb2
from google.ads.googleads.v8.enums import ad_strength_pb2 as google_dot_ads_dot_googleads_dot_v8_dot_enums_dot_ad__strength__pb2
from google.ads.googleads.v8.enums import policy_approval_status_pb2 as google_dot_ads_dot_googleads_dot_v8_dot_enums_dot_policy__approval__status__pb2
from google.ads.googleads.v8.enums import policy_review_status_pb2 as google_dot_ads_dot_googleads_dot_v8_dot_enums_dot_policy__review__status__pb2
from google.ads.googleads.v8.resources import ad_pb2 as google_dot_ads_dot_googleads_dot_v8_dot_resources_dot_ad__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3google/ads/googleads/v8/resources/ad_group_ad.proto\x12!google.ads.googleads.v8.resources\x1a+google/ads/googleads/v8/common/policy.proto\x1a\x36google/ads/googleads/v8/enums/ad_group_ad_status.proto\x1a/google/ads/googleads/v8/enums/ad_strength.proto\x1a:google/ads/googleads/v8/enums/policy_approval_status.proto\x1a\x38google/ads/googleads/v8/enums/policy_review_status.proto\x1a*google/ads/googleads/v8/resources/ad.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1cgoogle/api/annotations.proto\"\xed\x05\n\tAdGroupAd\x12P\n\rresource_name\x18\x01 \x01(\tB+\xe2\x41\x01\x05\xfa\x41$\n\"googleads.googleapis.com/AdGroupAdR\x0cresourceName\x12Z\n\x06status\x18\x03 \x01(\x0e\x32\x42.google.ads.googleads.v8.enums.AdGroupAdStatusEnum.AdGroupAdStatusR\x06status\x12I\n\x08\x61\x64_group\x18\t \x01(\tB)\xe2\x41\x01\x05\xfa\x41\"\n googleads.googleapis.com/AdGroupH\x00R\x07\x61\x64Group\x88\x01\x01\x12;\n\x02\x61\x64\x18\x05 \x01(\x0b\x32%.google.ads.googleads.v8.resources.AdB\x04\xe2\x41\x01\x05R\x02\x61\x64\x12\x66\n\x0epolicy_summary\x18\x06 \x01(\x0b\x32\x39.google.ads.googleads.v8.resources.AdGroupAdPolicySummaryB\x04\xe2\x41\x01\x03R\rpolicySummary\x12_\n\x0b\x61\x64_strength\x18\x07 \x01(\x0e\x32\x38.google.ads.googleads.v8.enums.AdStrengthEnum.AdStrengthB\x04\xe2\x41\x01\x03R\nadStrength\x12\'\n\x0c\x61\x63tion_items\x18\r \x03(\tB\x04\xe2\x41\x01\x03R\x0b\x61\x63tionItems\x12H\n\x06labels\x18\n \x03(\tB0\xe2\x41\x01\x03\xfa\x41)\n\'googleads.googleapis.com/AdGroupAdLabelR\x06labels:a\xea\x41^\n\"googleads.googleapis.com/AdGroupAd\x12\x38\x63ustomers/{customer_id}/adGroupAds/{ad_group_id}~{ad_id}B\x0b\n\t_ad_group\"\xf4\x02\n\x16\x41\x64GroupAdPolicySummary\x12h\n\x14policy_topic_entries\x18\x01 \x03(\x0b\x32\x30.google.ads.googleads.v8.common.PolicyTopicEntryB\x04\xe2\x41\x01\x03R\x12policyTopicEntries\x12s\n\rreview_status\x18\x02 \x01(\x0e\x32H.google.ads.googleads.v8.enums.PolicyReviewStatusEnum.PolicyReviewStatusB\x04\xe2\x41\x01\x03R\x0creviewStatus\x12{\n\x0f\x61pproval_status\x18\x03 \x01(\x0e\x32L.google.ads.googleads.v8.enums.PolicyApprovalStatusEnum.PolicyApprovalStatusB\x04\xe2\x41\x01\x03R\x0e\x61pprovalStatusB\xfb\x01\n%com.google.ads.googleads.v8.resourcesB\x0e\x41\x64GroupAdProtoP\x01ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v8/resources;resources\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V8.Resources\xca\x02!Google\\Ads\\GoogleAds\\V8\\Resources\xea\x02%Google::Ads::GoogleAds::V8::Resourcesb\x06proto3')



_ADGROUPAD = DESCRIPTOR.message_types_by_name['AdGroupAd']
_ADGROUPADPOLICYSUMMARY = DESCRIPTOR.message_types_by_name['AdGroupAdPolicySummary']
AdGroupAd = _reflection.GeneratedProtocolMessageType('AdGroupAd', (_message.Message,), {
  'DESCRIPTOR' : _ADGROUPAD,
  '__module__' : 'google.ads.googleads.v8.resources.ad_group_ad_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v8.resources.AdGroupAd)
  })
_sym_db.RegisterMessage(AdGroupAd)

AdGroupAdPolicySummary = _reflection.GeneratedProtocolMessageType('AdGroupAdPolicySummary', (_message.Message,), {
  'DESCRIPTOR' : _ADGROUPADPOLICYSUMMARY,
  '__module__' : 'google.ads.googleads.v8.resources.ad_group_ad_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v8.resources.AdGroupAdPolicySummary)
  })
_sym_db.RegisterMessage(AdGroupAdPolicySummary)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n%com.google.ads.googleads.v8.resourcesB\016AdGroupAdProtoP\001ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v8/resources;resources\242\002\003GAA\252\002!Google.Ads.GoogleAds.V8.Resources\312\002!Google\\Ads\\GoogleAds\\V8\\Resources\352\002%Google::Ads::GoogleAds::V8::Resources'
  _ADGROUPAD.fields_by_name['resource_name']._options = None
  _ADGROUPAD.fields_by_name['resource_name']._serialized_options = b'\342A\001\005\372A$\n\"googleads.googleapis.com/AdGroupAd'
  _ADGROUPAD.fields_by_name['ad_group']._options = None
  _ADGROUPAD.fields_by_name['ad_group']._serialized_options = b'\342A\001\005\372A\"\n googleads.googleapis.com/AdGroup'
  _ADGROUPAD.fields_by_name['ad']._options = None
  _ADGROUPAD.fields_by_name['ad']._serialized_options = b'\342A\001\005'
  _ADGROUPAD.fields_by_name['policy_summary']._options = None
  _ADGROUPAD.fields_by_name['policy_summary']._serialized_options = b'\342A\001\003'
  _ADGROUPAD.fields_by_name['ad_strength']._options = None
  _ADGROUPAD.fields_by_name['ad_strength']._serialized_options = b'\342A\001\003'
  _ADGROUPAD.fields_by_name['action_items']._options = None
  _ADGROUPAD.fields_by_name['action_items']._serialized_options = b'\342A\001\003'
  _ADGROUPAD.fields_by_name['labels']._options = None
  _ADGROUPAD.fields_by_name['labels']._serialized_options = b'\342A\001\003\372A)\n\'googleads.googleapis.com/AdGroupAdLabel'
  _ADGROUPAD._options = None
  _ADGROUPAD._serialized_options = b'\352A^\n\"googleads.googleapis.com/AdGroupAd\0228customers/{customer_id}/adGroupAds/{ad_group_id}~{ad_id}'
  _ADGROUPADPOLICYSUMMARY.fields_by_name['policy_topic_entries']._options = None
  _ADGROUPADPOLICYSUMMARY.fields_by_name['policy_topic_entries']._serialized_options = b'\342A\001\003'
  _ADGROUPADPOLICYSUMMARY.fields_by_name['review_status']._options = None
  _ADGROUPADPOLICYSUMMARY.fields_by_name['review_status']._serialized_options = b'\342A\001\003'
  _ADGROUPADPOLICYSUMMARY.fields_by_name['approval_status']._options = None
  _ADGROUPADPOLICYSUMMARY.fields_by_name['approval_status']._serialized_options = b'\342A\001\003'
  _ADGROUPAD._serialized_start=493
  _ADGROUPAD._serialized_end=1242
  _ADGROUPADPOLICYSUMMARY._serialized_start=1245
  _ADGROUPADPOLICYSUMMARY._serialized_end=1617
# @@protoc_insertion_point(module_scope)
