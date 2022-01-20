# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v8/resources/ad_parameter.proto
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


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n4google/ads/googleads/v8/resources/ad_parameter.proto\x12!google.ads.googleads.v8.resources\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1cgoogle/api/annotations.proto\"\xe6\x03\n\x0b\x41\x64Parameter\x12R\n\rresource_name\x18\x01 \x01(\tB-\xe2\x41\x01\x05\xfa\x41&\n$googleads.googleapis.com/AdParameterR\x0cresourceName\x12\x65\n\x12\x61\x64_group_criterion\x18\x05 \x01(\tB2\xe2\x41\x01\x05\xfa\x41+\n)googleads.googleapis.com/AdGroupCriterionH\x00R\x10\x61\x64GroupCriterion\x88\x01\x01\x12\x32\n\x0fparameter_index\x18\x06 \x01(\x03\x42\x04\xe2\x41\x01\x05H\x01R\x0eparameterIndex\x88\x01\x01\x12*\n\x0einsertion_text\x18\x07 \x01(\tH\x02R\rinsertionText\x88\x01\x01:~\xea\x41{\n$googleads.googleapis.com/AdParameter\x12Scustomers/{customer_id}/adParameters/{ad_group_id}~{criterion_id}~{parameter_index}B\x15\n\x13_ad_group_criterionB\x12\n\x10_parameter_indexB\x11\n\x0f_insertion_textB\xfd\x01\n%com.google.ads.googleads.v8.resourcesB\x10\x41\x64ParameterProtoP\x01ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v8/resources;resources\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V8.Resources\xca\x02!Google\\Ads\\GoogleAds\\V8\\Resources\xea\x02%Google::Ads::GoogleAds::V8::Resourcesb\x06proto3')



_ADPARAMETER = DESCRIPTOR.message_types_by_name['AdParameter']
AdParameter = _reflection.GeneratedProtocolMessageType('AdParameter', (_message.Message,), {
  'DESCRIPTOR' : _ADPARAMETER,
  '__module__' : 'google.ads.googleads.v8.resources.ad_parameter_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v8.resources.AdParameter)
  })
_sym_db.RegisterMessage(AdParameter)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n%com.google.ads.googleads.v8.resourcesB\020AdParameterProtoP\001ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v8/resources;resources\242\002\003GAA\252\002!Google.Ads.GoogleAds.V8.Resources\312\002!Google\\Ads\\GoogleAds\\V8\\Resources\352\002%Google::Ads::GoogleAds::V8::Resources'
  _ADPARAMETER.fields_by_name['resource_name']._options = None
  _ADPARAMETER.fields_by_name['resource_name']._serialized_options = b'\342A\001\005\372A&\n$googleads.googleapis.com/AdParameter'
  _ADPARAMETER.fields_by_name['ad_group_criterion']._options = None
  _ADPARAMETER.fields_by_name['ad_group_criterion']._serialized_options = b'\342A\001\005\372A+\n)googleads.googleapis.com/AdGroupCriterion'
  _ADPARAMETER.fields_by_name['parameter_index']._options = None
  _ADPARAMETER.fields_by_name['parameter_index']._serialized_options = b'\342A\001\005'
  _ADPARAMETER._options = None
  _ADPARAMETER._serialized_options = b'\352A{\n$googleads.googleapis.com/AdParameter\022Scustomers/{customer_id}/adParameters/{ad_group_id}~{criterion_id}~{parameter_index}'
  _ADPARAMETER._serialized_start=182
  _ADPARAMETER._serialized_end=668
# @@protoc_insertion_point(module_scope)
