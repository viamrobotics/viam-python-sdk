# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v9/services/invoice_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.googleads.v9.enums import month_of_year_pb2 as google_dot_ads_dot_googleads_dot_v9_dot_enums_dot_month__of__year__pb2
from google.ads.googleads.v9.resources import invoice_pb2 as google_dot_ads_dot_googleads_dot_v9_dot_resources_dot_invoice__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import client_pb2 as google_dot_api_dot_client__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n6google/ads/googleads/v9/services/invoice_service.proto\x12 google.ads.googleads.v9.services\x1a\x31google/ads/googleads/v9/enums/month_of_year.proto\x1a/google/ads/googleads/v9/resources/invoice.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\"\xef\x01\n\x13ListInvoicesRequest\x12%\n\x0b\x63ustomer_id\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02R\ncustomerId\x12)\n\rbilling_setup\x18\x02 \x01(\tB\x04\xe2\x41\x01\x02R\x0c\x62illingSetup\x12#\n\nissue_year\x18\x03 \x01(\tB\x04\xe2\x41\x01\x02R\tissueYear\x12\x61\n\x0bissue_month\x18\x04 \x01(\x0e\x32:.google.ads.googleads.v9.enums.MonthOfYearEnum.MonthOfYearB\x04\xe2\x41\x01\x02R\nissueMonth\"^\n\x14ListInvoicesResponse\x12\x46\n\x08invoices\x18\x01 \x03(\x0b\x32*.google.ads.googleads.v9.resources.InvoiceR\x08invoices2\xba\x02\n\x0eInvoiceService\x12\xe0\x01\n\x0cListInvoices\x12\x35.google.ads.googleads.v9.services.ListInvoicesRequest\x1a\x36.google.ads.googleads.v9.services.ListInvoicesResponse\"a\xda\x41\x30\x63ustomer_id,billing_setup,issue_year,issue_month\x82\xd3\xe4\x93\x02(\x12&/v9/customers/{customer_id=*}/invoices\x1a\x45\xca\x41\x18googleads.googleapis.com\xd2\x41\'https://www.googleapis.com/auth/adwordsB\xfa\x01\n$com.google.ads.googleads.v9.servicesB\x13InvoiceServiceProtoP\x01ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v9/services;services\xa2\x02\x03GAA\xaa\x02 Google.Ads.GoogleAds.V9.Services\xca\x02 Google\\Ads\\GoogleAds\\V9\\Services\xea\x02$Google::Ads::GoogleAds::V9::Servicesb\x06proto3')



_LISTINVOICESREQUEST = DESCRIPTOR.message_types_by_name['ListInvoicesRequest']
_LISTINVOICESRESPONSE = DESCRIPTOR.message_types_by_name['ListInvoicesResponse']
ListInvoicesRequest = _reflection.GeneratedProtocolMessageType('ListInvoicesRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTINVOICESREQUEST,
  '__module__' : 'google.ads.googleads.v9.services.invoice_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v9.services.ListInvoicesRequest)
  })
_sym_db.RegisterMessage(ListInvoicesRequest)

ListInvoicesResponse = _reflection.GeneratedProtocolMessageType('ListInvoicesResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTINVOICESRESPONSE,
  '__module__' : 'google.ads.googleads.v9.services.invoice_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v9.services.ListInvoicesResponse)
  })
_sym_db.RegisterMessage(ListInvoicesResponse)

_INVOICESERVICE = DESCRIPTOR.services_by_name['InvoiceService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n$com.google.ads.googleads.v9.servicesB\023InvoiceServiceProtoP\001ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v9/services;services\242\002\003GAA\252\002 Google.Ads.GoogleAds.V9.Services\312\002 Google\\Ads\\GoogleAds\\V9\\Services\352\002$Google::Ads::GoogleAds::V9::Services'
  _LISTINVOICESREQUEST.fields_by_name['customer_id']._options = None
  _LISTINVOICESREQUEST.fields_by_name['customer_id']._serialized_options = b'\342A\001\002'
  _LISTINVOICESREQUEST.fields_by_name['billing_setup']._options = None
  _LISTINVOICESREQUEST.fields_by_name['billing_setup']._serialized_options = b'\342A\001\002'
  _LISTINVOICESREQUEST.fields_by_name['issue_year']._options = None
  _LISTINVOICESREQUEST.fields_by_name['issue_year']._serialized_options = b'\342A\001\002'
  _LISTINVOICESREQUEST.fields_by_name['issue_month']._options = None
  _LISTINVOICESREQUEST.fields_by_name['issue_month']._serialized_options = b'\342A\001\002'
  _INVOICESERVICE._options = None
  _INVOICESERVICE._serialized_options = b'\312A\030googleads.googleapis.com\322A\'https://www.googleapis.com/auth/adwords'
  _INVOICESERVICE.methods_by_name['ListInvoices']._options = None
  _INVOICESERVICE.methods_by_name['ListInvoices']._serialized_options = b'\332A0customer_id,billing_setup,issue_year,issue_month\202\323\344\223\002(\022&/v9/customers/{customer_id=*}/invoices'
  _LISTINVOICESREQUEST._serialized_start=281
  _LISTINVOICESREQUEST._serialized_end=520
  _LISTINVOICESRESPONSE._serialized_start=522
  _LISTINVOICESRESPONSE._serialized_end=616
  _INVOICESERVICE._serialized_start=619
  _INVOICESERVICE._serialized_end=933
# @@protoc_insertion_point(module_scope)
