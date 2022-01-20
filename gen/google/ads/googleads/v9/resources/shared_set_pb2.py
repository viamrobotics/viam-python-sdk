# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v9/resources/shared_set.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.googleads.v9.enums import shared_set_status_pb2 as google_dot_ads_dot_googleads_dot_v9_dot_enums_dot_shared__set__status__pb2
from google.ads.googleads.v9.enums import shared_set_type_pb2 as google_dot_ads_dot_googleads_dot_v9_dot_enums_dot_shared__set__type__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2google/ads/googleads/v9/resources/shared_set.proto\x12!google.ads.googleads.v9.resources\x1a\x35google/ads/googleads/v9/enums/shared_set_status.proto\x1a\x33google/ads/googleads/v9/enums/shared_set_type.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1cgoogle/api/annotations.proto\"\xc1\x04\n\tSharedSet\x12P\n\rresource_name\x18\x01 \x01(\tB+\xe2\x41\x01\x05\xfa\x41$\n\"googleads.googleapis.com/SharedSetR\x0cresourceName\x12\x19\n\x02id\x18\x08 \x01(\x03\x42\x04\xe2\x41\x01\x03H\x00R\x02id\x88\x01\x01\x12X\n\x04type\x18\x03 \x01(\x0e\x32>.google.ads.googleads.v9.enums.SharedSetTypeEnum.SharedSetTypeB\x04\xe2\x41\x01\x05R\x04type\x12\x17\n\x04name\x18\t \x01(\tH\x01R\x04name\x88\x01\x01\x12`\n\x06status\x18\x05 \x01(\x0e\x32\x42.google.ads.googleads.v9.enums.SharedSetStatusEnum.SharedSetStatusB\x04\xe2\x41\x01\x03R\x06status\x12,\n\x0cmember_count\x18\n \x01(\x03\x42\x04\xe2\x41\x01\x03H\x02R\x0bmemberCount\x88\x01\x01\x12\x32\n\x0freference_count\x18\x0b \x01(\x03\x42\x04\xe2\x41\x01\x03H\x03R\x0ereferenceCount\x88\x01\x01:[\xea\x41X\n\"googleads.googleapis.com/SharedSet\x12\x32\x63ustomers/{customer_id}/sharedSets/{shared_set_id}B\x05\n\x03_idB\x07\n\x05_nameB\x0f\n\r_member_countB\x12\n\x10_reference_countB\xfb\x01\n%com.google.ads.googleads.v9.resourcesB\x0eSharedSetProtoP\x01ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v9/resources;resources\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V9.Resources\xca\x02!Google\\Ads\\GoogleAds\\V9\\Resources\xea\x02%Google::Ads::GoogleAds::V9::Resourcesb\x06proto3')



_SHAREDSET = DESCRIPTOR.message_types_by_name['SharedSet']
SharedSet = _reflection.GeneratedProtocolMessageType('SharedSet', (_message.Message,), {
  'DESCRIPTOR' : _SHAREDSET,
  '__module__' : 'google.ads.googleads.v9.resources.shared_set_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v9.resources.SharedSet)
  })
_sym_db.RegisterMessage(SharedSet)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n%com.google.ads.googleads.v9.resourcesB\016SharedSetProtoP\001ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v9/resources;resources\242\002\003GAA\252\002!Google.Ads.GoogleAds.V9.Resources\312\002!Google\\Ads\\GoogleAds\\V9\\Resources\352\002%Google::Ads::GoogleAds::V9::Resources'
  _SHAREDSET.fields_by_name['resource_name']._options = None
  _SHAREDSET.fields_by_name['resource_name']._serialized_options = b'\342A\001\005\372A$\n\"googleads.googleapis.com/SharedSet'
  _SHAREDSET.fields_by_name['id']._options = None
  _SHAREDSET.fields_by_name['id']._serialized_options = b'\342A\001\003'
  _SHAREDSET.fields_by_name['type']._options = None
  _SHAREDSET.fields_by_name['type']._serialized_options = b'\342A\001\005'
  _SHAREDSET.fields_by_name['status']._options = None
  _SHAREDSET.fields_by_name['status']._serialized_options = b'\342A\001\003'
  _SHAREDSET.fields_by_name['member_count']._options = None
  _SHAREDSET.fields_by_name['member_count']._serialized_options = b'\342A\001\003'
  _SHAREDSET.fields_by_name['reference_count']._options = None
  _SHAREDSET.fields_by_name['reference_count']._serialized_options = b'\342A\001\003'
  _SHAREDSET._options = None
  _SHAREDSET._serialized_options = b'\352AX\n\"googleads.googleapis.com/SharedSet\0222customers/{customer_id}/sharedSets/{shared_set_id}'
  _SHAREDSET._serialized_start=288
  _SHAREDSET._serialized_end=865
# @@protoc_insertion_point(module_scope)
