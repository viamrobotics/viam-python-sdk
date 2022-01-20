# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v9/errors/recommendation_error.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n9google/ads/googleads/v9/errors/recommendation_error.proto\x12\x1egoogle.ads.googleads.v9.errors\x1a\x1cgoogle/api/annotations.proto\"\xda\x03\n\x17RecommendationErrorEnum\"\xbe\x03\n\x13RecommendationError\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\x1b\n\x17\x42UDGET_AMOUNT_TOO_SMALL\x10\x02\x12\x1b\n\x17\x42UDGET_AMOUNT_TOO_LARGE\x10\x03\x12\x19\n\x15INVALID_BUDGET_AMOUNT\x10\x04\x12\x10\n\x0cPOLICY_ERROR\x10\x05\x12\x16\n\x12INVALID_BID_AMOUNT\x10\x06\x12\x19\n\x15\x41\x44GROUP_KEYWORD_LIMIT\x10\x07\x12\"\n\x1eRECOMMENDATION_ALREADY_APPLIED\x10\x08\x12\x1e\n\x1aRECOMMENDATION_INVALIDATED\x10\t\x12\x17\n\x13TOO_MANY_OPERATIONS\x10\n\x12\x11\n\rNO_OPERATIONS\x10\x0b\x12!\n\x1d\x44IFFERENT_TYPES_NOT_SUPPORTED\x10\x0c\x12\x1b\n\x17\x44UPLICATE_RESOURCE_NAME\x10\r\x12$\n RECOMMENDATION_ALREADY_DISMISSED\x10\x0e\x12\x19\n\x15INVALID_APPLY_REQUEST\x10\x0f\x42\xf3\x01\n\"com.google.ads.googleads.v9.errorsB\x18RecommendationErrorProtoP\x01ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v9/errors;errors\xa2\x02\x03GAA\xaa\x02\x1eGoogle.Ads.GoogleAds.V9.Errors\xca\x02\x1eGoogle\\Ads\\GoogleAds\\V9\\Errors\xea\x02\"Google::Ads::GoogleAds::V9::Errorsb\x06proto3')



_RECOMMENDATIONERRORENUM = DESCRIPTOR.message_types_by_name['RecommendationErrorEnum']
_RECOMMENDATIONERRORENUM_RECOMMENDATIONERROR = _RECOMMENDATIONERRORENUM.enum_types_by_name['RecommendationError']
RecommendationErrorEnum = _reflection.GeneratedProtocolMessageType('RecommendationErrorEnum', (_message.Message,), {
  'DESCRIPTOR' : _RECOMMENDATIONERRORENUM,
  '__module__' : 'google.ads.googleads.v9.errors.recommendation_error_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v9.errors.RecommendationErrorEnum)
  })
_sym_db.RegisterMessage(RecommendationErrorEnum)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\"com.google.ads.googleads.v9.errorsB\030RecommendationErrorProtoP\001ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v9/errors;errors\242\002\003GAA\252\002\036Google.Ads.GoogleAds.V9.Errors\312\002\036Google\\Ads\\GoogleAds\\V9\\Errors\352\002\"Google::Ads::GoogleAds::V9::Errors'
  _RECOMMENDATIONERRORENUM._serialized_start=124
  _RECOMMENDATIONERRORENUM._serialized_end=598
  _RECOMMENDATIONERRORENUM_RECOMMENDATIONERROR._serialized_start=152
  _RECOMMENDATIONERRORENUM_RECOMMENDATIONERROR._serialized_end=598
# @@protoc_insertion_point(module_scope)
