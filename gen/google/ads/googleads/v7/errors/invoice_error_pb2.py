# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v7/errors/invoice_error.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2google/ads/googleads/v7/errors/invoice_error.proto\x12\x1egoogle.ads.googleads.v7.errors\x1a\x1cgoogle/api/annotations.proto\"s\n\x10InvoiceErrorEnum\"_\n\x0cInvoiceError\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\x16\n\x12YEAR_MONTH_TOO_OLD\x10\x02\x12\x19\n\x15NOT_INVOICED_CUSTOMER\x10\x03\x42\xec\x01\n\"com.google.ads.googleads.v7.errorsB\x11InvoiceErrorProtoP\x01ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v7/errors;errors\xa2\x02\x03GAA\xaa\x02\x1eGoogle.Ads.GoogleAds.V7.Errors\xca\x02\x1eGoogle\\Ads\\GoogleAds\\V7\\Errors\xea\x02\"Google::Ads::GoogleAds::V7::Errorsb\x06proto3')



_INVOICEERRORENUM = DESCRIPTOR.message_types_by_name['InvoiceErrorEnum']
_INVOICEERRORENUM_INVOICEERROR = _INVOICEERRORENUM.enum_types_by_name['InvoiceError']
InvoiceErrorEnum = _reflection.GeneratedProtocolMessageType('InvoiceErrorEnum', (_message.Message,), {
  'DESCRIPTOR' : _INVOICEERRORENUM,
  '__module__' : 'google.ads.googleads.v7.errors.invoice_error_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v7.errors.InvoiceErrorEnum)
  })
_sym_db.RegisterMessage(InvoiceErrorEnum)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\"com.google.ads.googleads.v7.errorsB\021InvoiceErrorProtoP\001ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v7/errors;errors\242\002\003GAA\252\002\036Google.Ads.GoogleAds.V7.Errors\312\002\036Google\\Ads\\GoogleAds\\V7\\Errors\352\002\"Google::Ads::GoogleAds::V7::Errors'
  _INVOICEERRORENUM._serialized_start=116
  _INVOICEERRORENUM._serialized_end=231
  _INVOICEERRORENUM_INVOICEERROR._serialized_start=136
  _INVOICEERRORENUM_INVOICEERROR._serialized_end=231
# @@protoc_insertion_point(module_scope)
