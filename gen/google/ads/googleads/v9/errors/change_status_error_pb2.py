# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v9/errors/change_status_error.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n8google/ads/googleads/v9/errors/change_status_error.proto\x12\x1egoogle.ads.googleads.v9.errors\x1a\x1cgoogle/api/annotations.proto\"\xd6\x01\n\x15\x43hangeStatusErrorEnum\"\xbc\x01\n\x11\x43hangeStatusError\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\x16\n\x12START_DATE_TOO_OLD\x10\x03\x12\x1e\n\x1a\x43HANGE_DATE_RANGE_INFINITE\x10\x04\x12\x1e\n\x1a\x43HANGE_DATE_RANGE_NEGATIVE\x10\x05\x12\x17\n\x13LIMIT_NOT_SPECIFIED\x10\x06\x12\x18\n\x14INVALID_LIMIT_CLAUSE\x10\x07\x42\xf1\x01\n\"com.google.ads.googleads.v9.errorsB\x16\x43hangeStatusErrorProtoP\x01ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v9/errors;errors\xa2\x02\x03GAA\xaa\x02\x1eGoogle.Ads.GoogleAds.V9.Errors\xca\x02\x1eGoogle\\Ads\\GoogleAds\\V9\\Errors\xea\x02\"Google::Ads::GoogleAds::V9::Errorsb\x06proto3')



_CHANGESTATUSERRORENUM = DESCRIPTOR.message_types_by_name['ChangeStatusErrorEnum']
_CHANGESTATUSERRORENUM_CHANGESTATUSERROR = _CHANGESTATUSERRORENUM.enum_types_by_name['ChangeStatusError']
ChangeStatusErrorEnum = _reflection.GeneratedProtocolMessageType('ChangeStatusErrorEnum', (_message.Message,), {
  'DESCRIPTOR' : _CHANGESTATUSERRORENUM,
  '__module__' : 'google.ads.googleads.v9.errors.change_status_error_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v9.errors.ChangeStatusErrorEnum)
  })
_sym_db.RegisterMessage(ChangeStatusErrorEnum)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\"com.google.ads.googleads.v9.errorsB\026ChangeStatusErrorProtoP\001ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v9/errors;errors\242\002\003GAA\252\002\036Google.Ads.GoogleAds.V9.Errors\312\002\036Google\\Ads\\GoogleAds\\V9\\Errors\352\002\"Google::Ads::GoogleAds::V9::Errors'
  _CHANGESTATUSERRORENUM._serialized_start=123
  _CHANGESTATUSERRORENUM._serialized_end=337
  _CHANGESTATUSERRORENUM_CHANGESTATUSERROR._serialized_start=149
  _CHANGESTATUSERRORENUM_CHANGESTATUSERROR._serialized_end=337
# @@protoc_insertion_point(module_scope)
