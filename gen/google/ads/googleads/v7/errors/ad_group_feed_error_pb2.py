# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v7/errors/ad_group_feed_error.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n8google/ads/googleads/v7/errors/ad_group_feed_error.proto\x12\x1egoogle.ads.googleads.v7.errors\x1a\x1cgoogle/api/annotations.proto\"\xdc\x02\n\x14\x41\x64GroupFeedErrorEnum\"\xc3\x02\n\x10\x41\x64GroupFeedError\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12,\n(FEED_ALREADY_EXISTS_FOR_PLACEHOLDER_TYPE\x10\x02\x12\"\n\x1e\x43\x41NNOT_CREATE_FOR_REMOVED_FEED\x10\x03\x12\x1f\n\x1b\x41\x44GROUP_FEED_ALREADY_EXISTS\x10\x04\x12*\n&CANNOT_OPERATE_ON_REMOVED_ADGROUP_FEED\x10\x05\x12\x1c\n\x18INVALID_PLACEHOLDER_TYPE\x10\x06\x12,\n(MISSING_FEEDMAPPING_FOR_PLACEHOLDER_TYPE\x10\x07\x12&\n\"NO_EXISTING_LOCATION_CUSTOMER_FEED\x10\x08\x42\xf0\x01\n\"com.google.ads.googleads.v7.errorsB\x15\x41\x64GroupFeedErrorProtoP\x01ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v7/errors;errors\xa2\x02\x03GAA\xaa\x02\x1eGoogle.Ads.GoogleAds.V7.Errors\xca\x02\x1eGoogle\\Ads\\GoogleAds\\V7\\Errors\xea\x02\"Google::Ads::GoogleAds::V7::Errorsb\x06proto3')



_ADGROUPFEEDERRORENUM = DESCRIPTOR.message_types_by_name['AdGroupFeedErrorEnum']
_ADGROUPFEEDERRORENUM_ADGROUPFEEDERROR = _ADGROUPFEEDERRORENUM.enum_types_by_name['AdGroupFeedError']
AdGroupFeedErrorEnum = _reflection.GeneratedProtocolMessageType('AdGroupFeedErrorEnum', (_message.Message,), {
  'DESCRIPTOR' : _ADGROUPFEEDERRORENUM,
  '__module__' : 'google.ads.googleads.v7.errors.ad_group_feed_error_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v7.errors.AdGroupFeedErrorEnum)
  })
_sym_db.RegisterMessage(AdGroupFeedErrorEnum)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\"com.google.ads.googleads.v7.errorsB\025AdGroupFeedErrorProtoP\001ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v7/errors;errors\242\002\003GAA\252\002\036Google.Ads.GoogleAds.V7.Errors\312\002\036Google\\Ads\\GoogleAds\\V7\\Errors\352\002\"Google::Ads::GoogleAds::V7::Errors'
  _ADGROUPFEEDERRORENUM._serialized_start=123
  _ADGROUPFEEDERRORENUM._serialized_end=471
  _ADGROUPFEEDERRORENUM_ADGROUPFEEDERROR._serialized_start=148
  _ADGROUPFEEDERRORENUM_ADGROUPFEEDERROR._serialized_end=471
# @@protoc_insertion_point(module_scope)
