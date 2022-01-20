# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v8/errors/authorization_error.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n8google/ads/googleads/v8/errors/authorization_error.proto\x12\x1egoogle.ads.googleads.v8.errors\x1a\x1cgoogle/api/annotations.proto\"\xda\x03\n\x16\x41uthorizationErrorEnum\"\xbf\x03\n\x12\x41uthorizationError\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\x1a\n\x16USER_PERMISSION_DENIED\x10\x02\x12$\n DEVELOPER_TOKEN_NOT_ON_ALLOWLIST\x10\r\x12\x1e\n\x1a\x44\x45VELOPER_TOKEN_PROHIBITED\x10\x04\x12\x14\n\x10PROJECT_DISABLED\x10\x05\x12\x17\n\x13\x41UTHORIZATION_ERROR\x10\x06\x12\x18\n\x14\x41\x43TION_NOT_PERMITTED\x10\x07\x12\x15\n\x11INCOMPLETE_SIGNUP\x10\x08\x12\x18\n\x14\x43USTOMER_NOT_ENABLED\x10\x18\x12\x0f\n\x0bMISSING_TOS\x10\t\x12 \n\x1c\x44\x45VELOPER_TOKEN_NOT_APPROVED\x10\n\x12=\n9INVALID_LOGIN_CUSTOMER_ID_SERVING_CUSTOMER_ID_COMBINATION\x10\x0b\x12\x19\n\x15SERVICE_ACCESS_DENIED\x10\x0c\x12\"\n\x1e\x41\x43\x43\x45SS_DENIED_FOR_ACCOUNT_TYPE\x10\x19\x42\xf2\x01\n\"com.google.ads.googleads.v8.errorsB\x17\x41uthorizationErrorProtoP\x01ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v8/errors;errors\xa2\x02\x03GAA\xaa\x02\x1eGoogle.Ads.GoogleAds.V8.Errors\xca\x02\x1eGoogle\\Ads\\GoogleAds\\V8\\Errors\xea\x02\"Google::Ads::GoogleAds::V8::Errorsb\x06proto3')



_AUTHORIZATIONERRORENUM = DESCRIPTOR.message_types_by_name['AuthorizationErrorEnum']
_AUTHORIZATIONERRORENUM_AUTHORIZATIONERROR = _AUTHORIZATIONERRORENUM.enum_types_by_name['AuthorizationError']
AuthorizationErrorEnum = _reflection.GeneratedProtocolMessageType('AuthorizationErrorEnum', (_message.Message,), {
  'DESCRIPTOR' : _AUTHORIZATIONERRORENUM,
  '__module__' : 'google.ads.googleads.v8.errors.authorization_error_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v8.errors.AuthorizationErrorEnum)
  })
_sym_db.RegisterMessage(AuthorizationErrorEnum)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\"com.google.ads.googleads.v8.errorsB\027AuthorizationErrorProtoP\001ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v8/errors;errors\242\002\003GAA\252\002\036Google.Ads.GoogleAds.V8.Errors\312\002\036Google\\Ads\\GoogleAds\\V8\\Errors\352\002\"Google::Ads::GoogleAds::V8::Errors'
  _AUTHORIZATIONERRORENUM._serialized_start=123
  _AUTHORIZATIONERRORENUM._serialized_end=597
  _AUTHORIZATIONERRORENUM_AUTHORIZATIONERROR._serialized_start=150
  _AUTHORIZATIONERRORENUM_AUTHORIZATIONERROR._serialized_end=597
# @@protoc_insertion_point(module_scope)
