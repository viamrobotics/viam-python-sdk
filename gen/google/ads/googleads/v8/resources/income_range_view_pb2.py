# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v8/resources/income_range_view.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n9google/ads/googleads/v8/resources/income_range_view.proto\x12!google.ads.googleads.v8.resources\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1cgoogle/api/annotations.proto\"\xdf\x01\n\x0fIncomeRangeView\x12V\n\rresource_name\x18\x01 \x01(\tB1\xe2\x41\x01\x03\xfa\x41*\n(googleads.googleapis.com/IncomeRangeViewR\x0cresourceName:t\xea\x41q\n(googleads.googleapis.com/IncomeRangeView\x12\x45\x63ustomers/{customer_id}/incomeRangeViews/{ad_group_id}~{criterion_id}B\x81\x02\n%com.google.ads.googleads.v8.resourcesB\x14IncomeRangeViewProtoP\x01ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v8/resources;resources\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V8.Resources\xca\x02!Google\\Ads\\GoogleAds\\V8\\Resources\xea\x02%Google::Ads::GoogleAds::V8::Resourcesb\x06proto3')



_INCOMERANGEVIEW = DESCRIPTOR.message_types_by_name['IncomeRangeView']
IncomeRangeView = _reflection.GeneratedProtocolMessageType('IncomeRangeView', (_message.Message,), {
  'DESCRIPTOR' : _INCOMERANGEVIEW,
  '__module__' : 'google.ads.googleads.v8.resources.income_range_view_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v8.resources.IncomeRangeView)
  })
_sym_db.RegisterMessage(IncomeRangeView)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n%com.google.ads.googleads.v8.resourcesB\024IncomeRangeViewProtoP\001ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v8/resources;resources\242\002\003GAA\252\002!Google.Ads.GoogleAds.V8.Resources\312\002!Google\\Ads\\GoogleAds\\V8\\Resources\352\002%Google::Ads::GoogleAds::V8::Resources'
  _INCOMERANGEVIEW.fields_by_name['resource_name']._options = None
  _INCOMERANGEVIEW.fields_by_name['resource_name']._serialized_options = b'\342A\001\003\372A*\n(googleads.googleapis.com/IncomeRangeView'
  _INCOMERANGEVIEW._options = None
  _INCOMERANGEVIEW._serialized_options = b'\352Aq\n(googleads.googleapis.com/IncomeRangeView\022Ecustomers/{customer_id}/incomeRangeViews/{ad_group_id}~{criterion_id}'
  _INCOMERANGEVIEW._serialized_start=187
  _INCOMERANGEVIEW._serialized_end=410
# @@protoc_insertion_point(module_scope)
