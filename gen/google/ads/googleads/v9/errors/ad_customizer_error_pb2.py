# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v9/errors/ad_customizer_error.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n8google/ads/googleads/v9/errors/ad_customizer_error.proto\x12\x1egoogle.ads.googleads.v9.errors\x1a\x1cgoogle/api/annotations.proto\"\xe8\x01\n\x15\x41\x64\x43ustomizerErrorEnum\"\xce\x01\n\x11\x41\x64\x43ustomizerError\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12!\n\x1d\x43OUNTDOWN_INVALID_DATE_FORMAT\x10\x02\x12\x1a\n\x16\x43OUNTDOWN_DATE_IN_PAST\x10\x03\x12\x1c\n\x18\x43OUNTDOWN_INVALID_LOCALE\x10\x04\x12\'\n#COUNTDOWN_INVALID_START_DAYS_BEFORE\x10\x05\x12\x15\n\x11UNKNOWN_USER_LIST\x10\x06\x42\xf1\x01\n\"com.google.ads.googleads.v9.errorsB\x16\x41\x64\x43ustomizerErrorProtoP\x01ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v9/errors;errors\xa2\x02\x03GAA\xaa\x02\x1eGoogle.Ads.GoogleAds.V9.Errors\xca\x02\x1eGoogle\\Ads\\GoogleAds\\V9\\Errors\xea\x02\"Google::Ads::GoogleAds::V9::Errorsb\x06proto3')



_ADCUSTOMIZERERRORENUM = DESCRIPTOR.message_types_by_name['AdCustomizerErrorEnum']
_ADCUSTOMIZERERRORENUM_ADCUSTOMIZERERROR = _ADCUSTOMIZERERRORENUM.enum_types_by_name['AdCustomizerError']
AdCustomizerErrorEnum = _reflection.GeneratedProtocolMessageType('AdCustomizerErrorEnum', (_message.Message,), {
  'DESCRIPTOR' : _ADCUSTOMIZERERRORENUM,
  '__module__' : 'google.ads.googleads.v9.errors.ad_customizer_error_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v9.errors.AdCustomizerErrorEnum)
  })
_sym_db.RegisterMessage(AdCustomizerErrorEnum)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\"com.google.ads.googleads.v9.errorsB\026AdCustomizerErrorProtoP\001ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v9/errors;errors\242\002\003GAA\252\002\036Google.Ads.GoogleAds.V9.Errors\312\002\036Google\\Ads\\GoogleAds\\V9\\Errors\352\002\"Google::Ads::GoogleAds::V9::Errors'
  _ADCUSTOMIZERERRORENUM._serialized_start=123
  _ADCUSTOMIZERERRORENUM._serialized_end=355
  _ADCUSTOMIZERERRORENUM_ADCUSTOMIZERERROR._serialized_start=149
  _ADCUSTOMIZERERRORENUM_ADCUSTOMIZERERROR._serialized_end=355
# @@protoc_insertion_point(module_scope)
