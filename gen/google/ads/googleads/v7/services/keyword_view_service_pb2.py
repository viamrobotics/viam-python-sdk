# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v7/services/keyword_view_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.googleads.v7.resources import keyword_view_pb2 as google_dot_ads_dot_googleads_dot_v7_dot_resources_dot_keyword__view__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import client_pb2 as google_dot_api_dot_client__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n;google/ads/googleads/v7/services/keyword_view_service.proto\x12 google.ads.googleads.v7.services\x1a\x34google/ads/googleads/v7/resources/keyword_view.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\"k\n\x15GetKeywordViewRequest\x12R\n\rresource_name\x18\x01 \x01(\tB-\xe2\x41\x01\x02\xfa\x41&\n$googleads.googleapis.com/KeywordViewR\x0cresourceName2\x9f\x02\n\x12KeywordViewService\x12\xc1\x01\n\x0eGetKeywordView\x12\x37.google.ads.googleads.v7.services.GetKeywordViewRequest\x1a..google.ads.googleads.v7.resources.KeywordView\"F\xda\x41\rresource_name\x82\xd3\xe4\x93\x02\x30\x12./v7/{resource_name=customers/*/keywordViews/*}\x1a\x45\xca\x41\x18googleads.googleapis.com\xd2\x41\'https://www.googleapis.com/auth/adwordsB\xfe\x01\n$com.google.ads.googleads.v7.servicesB\x17KeywordViewServiceProtoP\x01ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v7/services;services\xa2\x02\x03GAA\xaa\x02 Google.Ads.GoogleAds.V7.Services\xca\x02 Google\\Ads\\GoogleAds\\V7\\Services\xea\x02$Google::Ads::GoogleAds::V7::Servicesb\x06proto3')



_GETKEYWORDVIEWREQUEST = DESCRIPTOR.message_types_by_name['GetKeywordViewRequest']
GetKeywordViewRequest = _reflection.GeneratedProtocolMessageType('GetKeywordViewRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETKEYWORDVIEWREQUEST,
  '__module__' : 'google.ads.googleads.v7.services.keyword_view_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v7.services.GetKeywordViewRequest)
  })
_sym_db.RegisterMessage(GetKeywordViewRequest)

_KEYWORDVIEWSERVICE = DESCRIPTOR.services_by_name['KeywordViewService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n$com.google.ads.googleads.v7.servicesB\027KeywordViewServiceProtoP\001ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v7/services;services\242\002\003GAA\252\002 Google.Ads.GoogleAds.V7.Services\312\002 Google\\Ads\\GoogleAds\\V7\\Services\352\002$Google::Ads::GoogleAds::V7::Services'
  _GETKEYWORDVIEWREQUEST.fields_by_name['resource_name']._options = None
  _GETKEYWORDVIEWREQUEST.fields_by_name['resource_name']._serialized_options = b'\342A\001\002\372A&\n$googleads.googleapis.com/KeywordView'
  _KEYWORDVIEWSERVICE._options = None
  _KEYWORDVIEWSERVICE._serialized_options = b'\312A\030googleads.googleapis.com\322A\'https://www.googleapis.com/auth/adwords'
  _KEYWORDVIEWSERVICE.methods_by_name['GetKeywordView']._options = None
  _KEYWORDVIEWSERVICE.methods_by_name['GetKeywordView']._serialized_options = b'\332A\rresource_name\202\323\344\223\0020\022./v7/{resource_name=customers/*/keywordViews/*}'
  _GETKEYWORDVIEWREQUEST._serialized_start=266
  _GETKEYWORDVIEWREQUEST._serialized_end=373
  _KEYWORDVIEWSERVICE._serialized_start=376
  _KEYWORDVIEWSERVICE._serialized_end=663
# @@protoc_insertion_point(module_scope)
