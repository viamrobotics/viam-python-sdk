# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v9/errors/feed_item_set_error.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n8google/ads/googleads/v9/errors/feed_item_set_error.proto\x12\x1egoogle.ads.googleads.v9.errors\x1a\x1cgoogle/api/annotations.proto\"\xa0\x02\n\x14\x46\x65\x65\x64ItemSetErrorEnum\"\x87\x02\n\x10\x46\x65\x65\x64ItemSetError\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\x19\n\x15\x46\x45\x45\x44_ITEM_SET_REMOVED\x10\x02\x12\x1f\n\x1b\x43\x41NNOT_CLEAR_DYNAMIC_FILTER\x10\x03\x12 \n\x1c\x43\x41NNOT_CREATE_DYNAMIC_FILTER\x10\x04\x12\x15\n\x11INVALID_FEED_TYPE\x10\x05\x12\x12\n\x0e\x44UPLICATE_NAME\x10\x06\x12&\n\"WRONG_DYNAMIC_FILTER_FOR_FEED_TYPE\x10\x07\x12$\n DYNAMIC_FILTER_INVALID_CHAIN_IDS\x10\x08\x42\xf0\x01\n\"com.google.ads.googleads.v9.errorsB\x15\x46\x65\x65\x64ItemSetErrorProtoP\x01ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v9/errors;errors\xa2\x02\x03GAA\xaa\x02\x1eGoogle.Ads.GoogleAds.V9.Errors\xca\x02\x1eGoogle\\Ads\\GoogleAds\\V9\\Errors\xea\x02\"Google::Ads::GoogleAds::V9::Errorsb\x06proto3')



_FEEDITEMSETERRORENUM = DESCRIPTOR.message_types_by_name['FeedItemSetErrorEnum']
_FEEDITEMSETERRORENUM_FEEDITEMSETERROR = _FEEDITEMSETERRORENUM.enum_types_by_name['FeedItemSetError']
FeedItemSetErrorEnum = _reflection.GeneratedProtocolMessageType('FeedItemSetErrorEnum', (_message.Message,), {
  'DESCRIPTOR' : _FEEDITEMSETERRORENUM,
  '__module__' : 'google.ads.googleads.v9.errors.feed_item_set_error_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v9.errors.FeedItemSetErrorEnum)
  })
_sym_db.RegisterMessage(FeedItemSetErrorEnum)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\"com.google.ads.googleads.v9.errorsB\025FeedItemSetErrorProtoP\001ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v9/errors;errors\242\002\003GAA\252\002\036Google.Ads.GoogleAds.V9.Errors\312\002\036Google\\Ads\\GoogleAds\\V9\\Errors\352\002\"Google::Ads::GoogleAds::V9::Errors'
  _FEEDITEMSETERRORENUM._serialized_start=123
  _FEEDITEMSETERRORENUM._serialized_end=411
  _FEEDITEMSETERRORENUM_FEEDITEMSETERROR._serialized_start=148
  _FEEDITEMSETERRORENUM_FEEDITEMSETERROR._serialized_end=411
# @@protoc_insertion_point(module_scope)
