# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v8/common/asset_policy.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.googleads.v8.common import policy_pb2 as google_dot_ads_dot_googleads_dot_v8_dot_common_dot_policy__pb2
from google.ads.googleads.v8.enums import policy_approval_status_pb2 as google_dot_ads_dot_googleads_dot_v8_dot_enums_dot_policy__approval__status__pb2
from google.ads.googleads.v8.enums import policy_review_status_pb2 as google_dot_ads_dot_googleads_dot_v8_dot_enums_dot_policy__review__status__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1google/ads/googleads/v8/common/asset_policy.proto\x12\x1egoogle.ads.googleads.v8.common\x1a+google/ads/googleads/v8/common/policy.proto\x1a:google/ads/googleads/v8/enums/policy_approval_status.proto\x1a\x38google/ads/googleads/v8/enums/policy_review_status.proto\x1a\x1cgoogle/api/annotations.proto\"\xe0\x02\n\x14\x41\x64\x41ssetPolicySummary\x12\x62\n\x14policy_topic_entries\x18\x01 \x03(\x0b\x32\x30.google.ads.googleads.v8.common.PolicyTopicEntryR\x12policyTopicEntries\x12m\n\rreview_status\x18\x02 \x01(\x0e\x32H.google.ads.googleads.v8.enums.PolicyReviewStatusEnum.PolicyReviewStatusR\x0creviewStatus\x12u\n\x0f\x61pproval_status\x18\x03 \x01(\x0e\x32L.google.ads.googleads.v8.enums.PolicyApprovalStatusEnum.PolicyApprovalStatusR\x0e\x61pprovalStatusB\xeb\x01\n\"com.google.ads.googleads.v8.commonB\x10\x41ssetPolicyProtoP\x01ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v8/common;common\xa2\x02\x03GAA\xaa\x02\x1eGoogle.Ads.GoogleAds.V8.Common\xca\x02\x1eGoogle\\Ads\\GoogleAds\\V8\\Common\xea\x02\"Google::Ads::GoogleAds::V8::Commonb\x06proto3')



_ADASSETPOLICYSUMMARY = DESCRIPTOR.message_types_by_name['AdAssetPolicySummary']
AdAssetPolicySummary = _reflection.GeneratedProtocolMessageType('AdAssetPolicySummary', (_message.Message,), {
  'DESCRIPTOR' : _ADASSETPOLICYSUMMARY,
  '__module__' : 'google.ads.googleads.v8.common.asset_policy_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v8.common.AdAssetPolicySummary)
  })
_sym_db.RegisterMessage(AdAssetPolicySummary)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\"com.google.ads.googleads.v8.commonB\020AssetPolicyProtoP\001ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v8/common;common\242\002\003GAA\252\002\036Google.Ads.GoogleAds.V8.Common\312\002\036Google\\Ads\\GoogleAds\\V8\\Common\352\002\"Google::Ads::GoogleAds::V8::Common'
  _ADASSETPOLICYSUMMARY._serialized_start=279
  _ADASSETPOLICYSUMMARY._serialized_end=631
# @@protoc_insertion_point(module_scope)
