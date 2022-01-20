# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v9/errors/custom_interest_error.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n:google/ads/googleads/v9/errors/custom_interest_error.proto\x12\x1egoogle.ads.googleads.v9.errors\x1a\x1cgoogle/api/annotations.proto\"\xd9\x02\n\x17\x43ustomInterestErrorEnum\"\xbd\x02\n\x13\x43ustomInterestError\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\x15\n\x11NAME_ALREADY_USED\x10\x02\x12\x46\nBCUSTOM_INTEREST_MEMBER_ID_AND_TYPE_PARAMETER_NOT_PRESENT_IN_REMOVE\x10\x03\x12 \n\x1cTYPE_AND_PARAMETER_NOT_FOUND\x10\x04\x12&\n\"TYPE_AND_PARAMETER_ALREADY_EXISTED\x10\x05\x12\'\n#INVALID_CUSTOM_INTEREST_MEMBER_TYPE\x10\x06\x12\x1e\n\x1a\x43\x41NNOT_REMOVE_WHILE_IN_USE\x10\x07\x12\x16\n\x12\x43\x41NNOT_CHANGE_TYPE\x10\x08\x42\xf3\x01\n\"com.google.ads.googleads.v9.errorsB\x18\x43ustomInterestErrorProtoP\x01ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v9/errors;errors\xa2\x02\x03GAA\xaa\x02\x1eGoogle.Ads.GoogleAds.V9.Errors\xca\x02\x1eGoogle\\Ads\\GoogleAds\\V9\\Errors\xea\x02\"Google::Ads::GoogleAds::V9::Errorsb\x06proto3')



_CUSTOMINTERESTERRORENUM = DESCRIPTOR.message_types_by_name['CustomInterestErrorEnum']
_CUSTOMINTERESTERRORENUM_CUSTOMINTERESTERROR = _CUSTOMINTERESTERRORENUM.enum_types_by_name['CustomInterestError']
CustomInterestErrorEnum = _reflection.GeneratedProtocolMessageType('CustomInterestErrorEnum', (_message.Message,), {
  'DESCRIPTOR' : _CUSTOMINTERESTERRORENUM,
  '__module__' : 'google.ads.googleads.v9.errors.custom_interest_error_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v9.errors.CustomInterestErrorEnum)
  })
_sym_db.RegisterMessage(CustomInterestErrorEnum)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\"com.google.ads.googleads.v9.errorsB\030CustomInterestErrorProtoP\001ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v9/errors;errors\242\002\003GAA\252\002\036Google.Ads.GoogleAds.V9.Errors\312\002\036Google\\Ads\\GoogleAds\\V9\\Errors\352\002\"Google::Ads::GoogleAds::V9::Errors'
  _CUSTOMINTERESTERRORENUM._serialized_start=125
  _CUSTOMINTERESTERRORENUM._serialized_end=470
  _CUSTOMINTERESTERRORENUM_CUSTOMINTERESTERROR._serialized_start=153
  _CUSTOMINTERESTERRORENUM_CUSTOMINTERESTERROR._serialized_end=470
# @@protoc_insertion_point(module_scope)
