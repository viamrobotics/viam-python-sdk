# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v8/errors/field_error.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0google/ads/googleads/v8/errors/field_error.proto\x12\x1egoogle.ads.googleads.v8.errors\x1a\x1cgoogle/api/annotations.proto\"\xd8\x01\n\x0e\x46ieldErrorEnum\"\xc5\x01\n\nFieldError\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\x0c\n\x08REQUIRED\x10\x02\x12\x13\n\x0fIMMUTABLE_FIELD\x10\x03\x12\x11\n\rINVALID_VALUE\x10\x04\x12\x17\n\x13VALUE_MUST_BE_UNSET\x10\x05\x12\x1a\n\x16REQUIRED_NONEMPTY_LIST\x10\x06\x12\x1b\n\x17\x46IELD_CANNOT_BE_CLEARED\x10\x07\x12\x11\n\rBLOCKED_VALUE\x10\tB\xea\x01\n\"com.google.ads.googleads.v8.errorsB\x0f\x46ieldErrorProtoP\x01ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v8/errors;errors\xa2\x02\x03GAA\xaa\x02\x1eGoogle.Ads.GoogleAds.V8.Errors\xca\x02\x1eGoogle\\Ads\\GoogleAds\\V8\\Errors\xea\x02\"Google::Ads::GoogleAds::V8::Errorsb\x06proto3')



_FIELDERRORENUM = DESCRIPTOR.message_types_by_name['FieldErrorEnum']
_FIELDERRORENUM_FIELDERROR = _FIELDERRORENUM.enum_types_by_name['FieldError']
FieldErrorEnum = _reflection.GeneratedProtocolMessageType('FieldErrorEnum', (_message.Message,), {
  'DESCRIPTOR' : _FIELDERRORENUM,
  '__module__' : 'google.ads.googleads.v8.errors.field_error_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v8.errors.FieldErrorEnum)
  })
_sym_db.RegisterMessage(FieldErrorEnum)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\"com.google.ads.googleads.v8.errorsB\017FieldErrorProtoP\001ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v8/errors;errors\242\002\003GAA\252\002\036Google.Ads.GoogleAds.V8.Errors\312\002\036Google\\Ads\\GoogleAds\\V8\\Errors\352\002\"Google::Ads::GoogleAds::V8::Errors'
  _FIELDERRORENUM._serialized_start=115
  _FIELDERRORENUM._serialized_end=331
  _FIELDERRORENUM_FIELDERROR._serialized_start=134
  _FIELDERRORENUM_FIELDERROR._serialized_end=331
# @@protoc_insertion_point(module_scope)
