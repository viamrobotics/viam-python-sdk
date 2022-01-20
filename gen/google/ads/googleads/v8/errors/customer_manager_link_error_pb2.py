# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v8/errors/customer_manager_link_error.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n@google/ads/googleads/v8/errors/customer_manager_link_error.proto\x12\x1egoogle.ads.googleads.v8.errors\x1a\x1cgoogle/api/annotations.proto\"\xd0\x03\n\x1c\x43ustomerManagerLinkErrorEnum\"\xaf\x03\n\x18\x43ustomerManagerLinkError\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\x15\n\x11NO_PENDING_INVITE\x10\x02\x12\'\n#SAME_CLIENT_MORE_THAN_ONCE_PER_CALL\x10\x03\x12-\n)MANAGER_HAS_MAX_NUMBER_OF_LINKED_ACCOUNTS\x10\x04\x12-\n)CANNOT_UNLINK_ACCOUNT_WITHOUT_ACTIVE_USER\x10\x05\x12+\n\'CANNOT_REMOVE_LAST_CLIENT_ACCOUNT_OWNER\x10\x06\x12+\n\'CANNOT_CHANGE_ROLE_BY_NON_ACCOUNT_OWNER\x10\x07\x12\x32\n.CANNOT_CHANGE_ROLE_FOR_NON_ACTIVE_LINK_ACCOUNT\x10\x08\x12\x19\n\x15\x44UPLICATE_CHILD_FOUND\x10\t\x12.\n*TEST_ACCOUNT_LINKS_TOO_MANY_CHILD_ACCOUNTS\x10\nB\xf8\x01\n\"com.google.ads.googleads.v8.errorsB\x1d\x43ustomerManagerLinkErrorProtoP\x01ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v8/errors;errors\xa2\x02\x03GAA\xaa\x02\x1eGoogle.Ads.GoogleAds.V8.Errors\xca\x02\x1eGoogle\\Ads\\GoogleAds\\V8\\Errors\xea\x02\"Google::Ads::GoogleAds::V8::Errorsb\x06proto3')



_CUSTOMERMANAGERLINKERRORENUM = DESCRIPTOR.message_types_by_name['CustomerManagerLinkErrorEnum']
_CUSTOMERMANAGERLINKERRORENUM_CUSTOMERMANAGERLINKERROR = _CUSTOMERMANAGERLINKERRORENUM.enum_types_by_name['CustomerManagerLinkError']
CustomerManagerLinkErrorEnum = _reflection.GeneratedProtocolMessageType('CustomerManagerLinkErrorEnum', (_message.Message,), {
  'DESCRIPTOR' : _CUSTOMERMANAGERLINKERRORENUM,
  '__module__' : 'google.ads.googleads.v8.errors.customer_manager_link_error_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v8.errors.CustomerManagerLinkErrorEnum)
  })
_sym_db.RegisterMessage(CustomerManagerLinkErrorEnum)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\"com.google.ads.googleads.v8.errorsB\035CustomerManagerLinkErrorProtoP\001ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v8/errors;errors\242\002\003GAA\252\002\036Google.Ads.GoogleAds.V8.Errors\312\002\036Google\\Ads\\GoogleAds\\V8\\Errors\352\002\"Google::Ads::GoogleAds::V8::Errors'
  _CUSTOMERMANAGERLINKERRORENUM._serialized_start=131
  _CUSTOMERMANAGERLINKERRORENUM._serialized_end=595
  _CUSTOMERMANAGERLINKERRORENUM_CUSTOMERMANAGERLINKERROR._serialized_start=164
  _CUSTOMERMANAGERLINKERRORENUM_CUSTOMERMANAGERLINKERROR._serialized_end=595
# @@protoc_insertion_point(module_scope)
