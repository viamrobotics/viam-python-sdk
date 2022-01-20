# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v7/common/targeting_setting.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.googleads.v7.enums import targeting_dimension_pb2 as google_dot_ads_dot_googleads_dot_v7_dot_enums_dot_targeting__dimension__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n6google/ads/googleads/v7/common/targeting_setting.proto\x12\x1egoogle.ads.googleads.v7.common\x1a\x37google/ads/googleads/v7/enums/targeting_dimension.proto\x1a\x1cgoogle/api/annotations.proto\"\xf6\x01\n\x10TargetingSetting\x12\x62\n\x13target_restrictions\x18\x01 \x03(\x0b\x32\x31.google.ads.googleads.v7.common.TargetRestrictionR\x12targetRestrictions\x12~\n\x1dtarget_restriction_operations\x18\x02 \x03(\x0b\x32:.google.ads.googleads.v7.common.TargetRestrictionOperationR\x1btargetRestrictionOperations\"\xbb\x01\n\x11TargetRestriction\x12y\n\x13targeting_dimension\x18\x01 \x01(\x0e\x32H.google.ads.googleads.v7.enums.TargetingDimensionEnum.TargetingDimensionR\x12targetingDimension\x12\x1e\n\x08\x62id_only\x18\x03 \x01(\x08H\x00R\x07\x62idOnly\x88\x01\x01\x42\x0b\n\t_bid_only\"\x85\x02\n\x1aTargetRestrictionOperation\x12_\n\x08operator\x18\x01 \x01(\x0e\x32\x43.google.ads.googleads.v7.common.TargetRestrictionOperation.OperatorR\x08operator\x12G\n\x05value\x18\x02 \x01(\x0b\x32\x31.google.ads.googleads.v7.common.TargetRestrictionR\x05value\"=\n\x08Operator\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\x07\n\x03\x41\x44\x44\x10\x02\x12\n\n\x06REMOVE\x10\x03\x42\xf0\x01\n\"com.google.ads.googleads.v7.commonB\x15TargetingSettingProtoP\x01ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v7/common;common\xa2\x02\x03GAA\xaa\x02\x1eGoogle.Ads.GoogleAds.V7.Common\xca\x02\x1eGoogle\\Ads\\GoogleAds\\V7\\Common\xea\x02\"Google::Ads::GoogleAds::V7::Commonb\x06proto3')



_TARGETINGSETTING = DESCRIPTOR.message_types_by_name['TargetingSetting']
_TARGETRESTRICTION = DESCRIPTOR.message_types_by_name['TargetRestriction']
_TARGETRESTRICTIONOPERATION = DESCRIPTOR.message_types_by_name['TargetRestrictionOperation']
_TARGETRESTRICTIONOPERATION_OPERATOR = _TARGETRESTRICTIONOPERATION.enum_types_by_name['Operator']
TargetingSetting = _reflection.GeneratedProtocolMessageType('TargetingSetting', (_message.Message,), {
  'DESCRIPTOR' : _TARGETINGSETTING,
  '__module__' : 'google.ads.googleads.v7.common.targeting_setting_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v7.common.TargetingSetting)
  })
_sym_db.RegisterMessage(TargetingSetting)

TargetRestriction = _reflection.GeneratedProtocolMessageType('TargetRestriction', (_message.Message,), {
  'DESCRIPTOR' : _TARGETRESTRICTION,
  '__module__' : 'google.ads.googleads.v7.common.targeting_setting_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v7.common.TargetRestriction)
  })
_sym_db.RegisterMessage(TargetRestriction)

TargetRestrictionOperation = _reflection.GeneratedProtocolMessageType('TargetRestrictionOperation', (_message.Message,), {
  'DESCRIPTOR' : _TARGETRESTRICTIONOPERATION,
  '__module__' : 'google.ads.googleads.v7.common.targeting_setting_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v7.common.TargetRestrictionOperation)
  })
_sym_db.RegisterMessage(TargetRestrictionOperation)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\"com.google.ads.googleads.v7.commonB\025TargetingSettingProtoP\001ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v7/common;common\242\002\003GAA\252\002\036Google.Ads.GoogleAds.V7.Common\312\002\036Google\\Ads\\GoogleAds\\V7\\Common\352\002\"Google::Ads::GoogleAds::V7::Common'
  _TARGETINGSETTING._serialized_start=178
  _TARGETINGSETTING._serialized_end=424
  _TARGETRESTRICTION._serialized_start=427
  _TARGETRESTRICTION._serialized_end=614
  _TARGETRESTRICTIONOPERATION._serialized_start=617
  _TARGETRESTRICTIONOPERATION._serialized_end=878
  _TARGETRESTRICTIONOPERATION_OPERATOR._serialized_start=817
  _TARGETRESTRICTIONOPERATION_OPERATOR._serialized_end=878
# @@protoc_insertion_point(module_scope)
