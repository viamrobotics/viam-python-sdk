# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v7/errors/billing_setup_error.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n8google/ads/googleads/v7/errors/billing_setup_error.proto\x12\x1egoogle.ads.googleads.v7.errors\x1a\x1cgoogle/api/annotations.proto\"\xd9\x05\n\x15\x42illingSetupErrorEnum\"\xbf\x05\n\x11\x42illingSetupError\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\'\n#CANNOT_USE_EXISTING_AND_NEW_ACCOUNT\x10\x02\x12\'\n#CANNOT_REMOVE_STARTED_BILLING_SETUP\x10\x03\x12\x32\n.CANNOT_CHANGE_BILLING_TO_SAME_PAYMENTS_ACCOUNT\x10\x04\x12\x33\n/BILLING_SETUP_NOT_PERMITTED_FOR_CUSTOMER_STATUS\x10\x05\x12\x1c\n\x18INVALID_PAYMENTS_ACCOUNT\x10\x06\x12\x35\n1BILLING_SETUP_NOT_PERMITTED_FOR_CUSTOMER_CATEGORY\x10\x07\x12\x1b\n\x17INVALID_START_TIME_TYPE\x10\x08\x12#\n\x1fTHIRD_PARTY_ALREADY_HAS_BILLING\x10\t\x12\x1d\n\x19\x42ILLING_SETUP_IN_PROGRESS\x10\n\x12\x18\n\x14NO_SIGNUP_PERMISSION\x10\x0b\x12!\n\x1d\x43HANGE_OF_BILL_TO_IN_PROGRESS\x10\x0c\x12\x1e\n\x1aPAYMENTS_PROFILE_NOT_FOUND\x10\r\x12\x1e\n\x1aPAYMENTS_ACCOUNT_NOT_FOUND\x10\x0e\x12\x1f\n\x1bPAYMENTS_PROFILE_INELIGIBLE\x10\x0f\x12\x1f\n\x1bPAYMENTS_ACCOUNT_INELIGIBLE\x10\x10\x12$\n CUSTOMER_NEEDS_INTERNAL_APPROVAL\x10\x11\x12\x36\n2PAYMENTS_ACCOUNT_INELIGIBLE_CURRENCY_CODE_MISMATCH\x10\x13\x42\xf1\x01\n\"com.google.ads.googleads.v7.errorsB\x16\x42illingSetupErrorProtoP\x01ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v7/errors;errors\xa2\x02\x03GAA\xaa\x02\x1eGoogle.Ads.GoogleAds.V7.Errors\xca\x02\x1eGoogle\\Ads\\GoogleAds\\V7\\Errors\xea\x02\"Google::Ads::GoogleAds::V7::Errorsb\x06proto3')



_BILLINGSETUPERRORENUM = DESCRIPTOR.message_types_by_name['BillingSetupErrorEnum']
_BILLINGSETUPERRORENUM_BILLINGSETUPERROR = _BILLINGSETUPERRORENUM.enum_types_by_name['BillingSetupError']
BillingSetupErrorEnum = _reflection.GeneratedProtocolMessageType('BillingSetupErrorEnum', (_message.Message,), {
  'DESCRIPTOR' : _BILLINGSETUPERRORENUM,
  '__module__' : 'google.ads.googleads.v7.errors.billing_setup_error_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v7.errors.BillingSetupErrorEnum)
  })
_sym_db.RegisterMessage(BillingSetupErrorEnum)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\"com.google.ads.googleads.v7.errorsB\026BillingSetupErrorProtoP\001ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v7/errors;errors\242\002\003GAA\252\002\036Google.Ads.GoogleAds.V7.Errors\312\002\036Google\\Ads\\GoogleAds\\V7\\Errors\352\002\"Google::Ads::GoogleAds::V7::Errors'
  _BILLINGSETUPERRORENUM._serialized_start=123
  _BILLINGSETUPERRORENUM._serialized_end=852
  _BILLINGSETUPERRORENUM_BILLINGSETUPERROR._serialized_start=149
  _BILLINGSETUPERRORENUM_BILLINGSETUPERROR._serialized_end=852
# @@protoc_insertion_point(module_scope)
