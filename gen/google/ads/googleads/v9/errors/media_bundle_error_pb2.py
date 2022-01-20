# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v9/errors/media_bundle_error.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n7google/ads/googleads/v9/errors/media_bundle_error.proto\x12\x1egoogle.ads.googleads.v9.errors\x1a\x1cgoogle/api/annotations.proto\"\xb8\x05\n\x14MediaBundleErrorEnum\"\x9f\x05\n\x10MediaBundleError\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\x0f\n\x0b\x42\x41\x44_REQUEST\x10\x03\x12\"\n\x1e\x44OUBLECLICK_BUNDLE_NOT_ALLOWED\x10\x04\x12\x1c\n\x18\x45XTERNAL_URL_NOT_ALLOWED\x10\x05\x12\x12\n\x0e\x46ILE_TOO_LARGE\x10\x06\x12.\n*GOOGLE_WEB_DESIGNER_ZIP_FILE_NOT_PUBLISHED\x10\x07\x12\x11\n\rINVALID_INPUT\x10\x08\x12\x18\n\x14INVALID_MEDIA_BUNDLE\x10\t\x12\x1e\n\x1aINVALID_MEDIA_BUNDLE_ENTRY\x10\n\x12\x15\n\x11INVALID_MIME_TYPE\x10\x0b\x12\x10\n\x0cINVALID_PATH\x10\x0c\x12\x19\n\x15INVALID_URL_REFERENCE\x10\r\x12\x18\n\x14MEDIA_DATA_TOO_LARGE\x10\x0e\x12&\n\"MISSING_PRIMARY_MEDIA_BUNDLE_ENTRY\x10\x0f\x12\x10\n\x0cSERVER_ERROR\x10\x10\x12\x11\n\rSTORAGE_ERROR\x10\x11\x12\x1d\n\x19SWIFFY_BUNDLE_NOT_ALLOWED\x10\x12\x12\x12\n\x0eTOO_MANY_FILES\x10\x13\x12\x13\n\x0fUNEXPECTED_SIZE\x10\x14\x12/\n+UNSUPPORTED_GOOGLE_WEB_DESIGNER_ENVIRONMENT\x10\x15\x12\x1d\n\x19UNSUPPORTED_HTML5_FEATURE\x10\x16\x12)\n%URL_IN_MEDIA_BUNDLE_NOT_SSL_COMPLIANT\x10\x17\x12\x1b\n\x17\x43USTOM_EXIT_NOT_ALLOWED\x10\x18\x42\xf0\x01\n\"com.google.ads.googleads.v9.errorsB\x15MediaBundleErrorProtoP\x01ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v9/errors;errors\xa2\x02\x03GAA\xaa\x02\x1eGoogle.Ads.GoogleAds.V9.Errors\xca\x02\x1eGoogle\\Ads\\GoogleAds\\V9\\Errors\xea\x02\"Google::Ads::GoogleAds::V9::Errorsb\x06proto3')



_MEDIABUNDLEERRORENUM = DESCRIPTOR.message_types_by_name['MediaBundleErrorEnum']
_MEDIABUNDLEERRORENUM_MEDIABUNDLEERROR = _MEDIABUNDLEERRORENUM.enum_types_by_name['MediaBundleError']
MediaBundleErrorEnum = _reflection.GeneratedProtocolMessageType('MediaBundleErrorEnum', (_message.Message,), {
  'DESCRIPTOR' : _MEDIABUNDLEERRORENUM,
  '__module__' : 'google.ads.googleads.v9.errors.media_bundle_error_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v9.errors.MediaBundleErrorEnum)
  })
_sym_db.RegisterMessage(MediaBundleErrorEnum)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\"com.google.ads.googleads.v9.errorsB\025MediaBundleErrorProtoP\001ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v9/errors;errors\242\002\003GAA\252\002\036Google.Ads.GoogleAds.V9.Errors\312\002\036Google\\Ads\\GoogleAds\\V9\\Errors\352\002\"Google::Ads::GoogleAds::V9::Errors'
  _MEDIABUNDLEERRORENUM._serialized_start=122
  _MEDIABUNDLEERRORENUM._serialized_end=818
  _MEDIABUNDLEERRORENUM_MEDIABUNDLEERROR._serialized_start=147
  _MEDIABUNDLEERRORENUM_MEDIABUNDLEERROR._serialized_end=818
# @@protoc_insertion_point(module_scope)
