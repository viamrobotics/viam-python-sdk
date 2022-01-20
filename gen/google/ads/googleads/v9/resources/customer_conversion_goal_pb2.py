# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v9/resources/customer_conversion_goal.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.googleads.v9.enums import conversion_action_category_pb2 as google_dot_ads_dot_googleads_dot_v9_dot_enums_dot_conversion__action__category__pb2
from google.ads.googleads.v9.enums import conversion_origin_pb2 as google_dot_ads_dot_googleads_dot_v9_dot_enums_dot_conversion__origin__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n@google/ads/googleads/v9/resources/customer_conversion_goal.proto\x12!google.ads.googleads.v9.resources\x1a>google/ads/googleads/v9/enums/conversion_action_category.proto\x1a\x35google/ads/googleads/v9/enums/conversion_origin.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1cgoogle/api/annotations.proto\"\xde\x03\n\x16\x43ustomerConversionGoal\x12]\n\rresource_name\x18\x01 \x01(\tB8\xe2\x41\x01\x05\xfa\x41\x31\n/googleads.googleapis.com/CustomerConversionGoalR\x0cresourceName\x12p\n\x08\x63\x61tegory\x18\x02 \x01(\x0e\x32T.google.ads.googleads.v9.enums.ConversionActionCategoryEnum.ConversionActionCategoryR\x08\x63\x61tegory\x12\\\n\x06origin\x18\x03 \x01(\x0e\x32\x44.google.ads.googleads.v9.enums.ConversionOriginEnum.ConversionOriginR\x06origin\x12\x1a\n\x08\x62iddable\x18\x04 \x01(\x08R\x08\x62iddable:y\xea\x41v\n/googleads.googleapis.com/CustomerConversionGoal\x12\x43\x63ustomers/{customer_id}/customerConversionGoals/{category}~{source}B\x88\x02\n%com.google.ads.googleads.v9.resourcesB\x1b\x43ustomerConversionGoalProtoP\x01ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v9/resources;resources\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V9.Resources\xca\x02!Google\\Ads\\GoogleAds\\V9\\Resources\xea\x02%Google::Ads::GoogleAds::V9::Resourcesb\x06proto3')



_CUSTOMERCONVERSIONGOAL = DESCRIPTOR.message_types_by_name['CustomerConversionGoal']
CustomerConversionGoal = _reflection.GeneratedProtocolMessageType('CustomerConversionGoal', (_message.Message,), {
  'DESCRIPTOR' : _CUSTOMERCONVERSIONGOAL,
  '__module__' : 'google.ads.googleads.v9.resources.customer_conversion_goal_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v9.resources.CustomerConversionGoal)
  })
_sym_db.RegisterMessage(CustomerConversionGoal)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n%com.google.ads.googleads.v9.resourcesB\033CustomerConversionGoalProtoP\001ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v9/resources;resources\242\002\003GAA\252\002!Google.Ads.GoogleAds.V9.Resources\312\002!Google\\Ads\\GoogleAds\\V9\\Resources\352\002%Google::Ads::GoogleAds::V9::Resources'
  _CUSTOMERCONVERSIONGOAL.fields_by_name['resource_name']._options = None
  _CUSTOMERCONVERSIONGOAL.fields_by_name['resource_name']._serialized_options = b'\342A\001\005\372A1\n/googleads.googleapis.com/CustomerConversionGoal'
  _CUSTOMERCONVERSIONGOAL._options = None
  _CUSTOMERCONVERSIONGOAL._serialized_options = b'\352Av\n/googleads.googleapis.com/CustomerConversionGoal\022Ccustomers/{customer_id}/customerConversionGoals/{category}~{source}'
  _CUSTOMERCONVERSIONGOAL._serialized_start=313
  _CUSTOMERCONVERSIONGOAL._serialized_end=791
# @@protoc_insertion_point(module_scope)
