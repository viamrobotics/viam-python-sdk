# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v7/services/shopping_performance_view_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.googleads.v7.resources import shopping_performance_view_pb2 as google_dot_ads_dot_googleads_dot_v7_dot_resources_dot_shopping__performance__view__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import client_pb2 as google_dot_api_dot_client__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nHgoogle/ads/googleads/v7/services/shopping_performance_view_service.proto\x12 google.ads.googleads.v7.services\x1a\x41google/ads/googleads/v7/resources/shopping_performance_view.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\"\x83\x01\n!GetShoppingPerformanceViewRequest\x12^\n\rresource_name\x18\x01 \x01(\tB9\xe2\x41\x01\x02\xfa\x41\x32\n0googleads.googleapis.com/ShoppingPerformanceViewR\x0cresourceName2\xd8\x02\n\x1eShoppingPerformanceViewService\x12\xee\x01\n\x1aGetShoppingPerformanceView\x12\x43.google.ads.googleads.v7.services.GetShoppingPerformanceViewRequest\x1a:.google.ads.googleads.v7.resources.ShoppingPerformanceView\"O\xda\x41\rresource_name\x82\xd3\xe4\x93\x02\x39\x12\x37/v7/{resource_name=customers/*/shoppingPerformanceView}\x1a\x45\xca\x41\x18googleads.googleapis.com\xd2\x41\'https://www.googleapis.com/auth/adwordsB\x8a\x02\n$com.google.ads.googleads.v7.servicesB#ShoppingPerformanceViewServiceProtoP\x01ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v7/services;services\xa2\x02\x03GAA\xaa\x02 Google.Ads.GoogleAds.V7.Services\xca\x02 Google\\Ads\\GoogleAds\\V7\\Services\xea\x02$Google::Ads::GoogleAds::V7::Servicesb\x06proto3')



_GETSHOPPINGPERFORMANCEVIEWREQUEST = DESCRIPTOR.message_types_by_name['GetShoppingPerformanceViewRequest']
GetShoppingPerformanceViewRequest = _reflection.GeneratedProtocolMessageType('GetShoppingPerformanceViewRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETSHOPPINGPERFORMANCEVIEWREQUEST,
  '__module__' : 'google.ads.googleads.v7.services.shopping_performance_view_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v7.services.GetShoppingPerformanceViewRequest)
  })
_sym_db.RegisterMessage(GetShoppingPerformanceViewRequest)

_SHOPPINGPERFORMANCEVIEWSERVICE = DESCRIPTOR.services_by_name['ShoppingPerformanceViewService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n$com.google.ads.googleads.v7.servicesB#ShoppingPerformanceViewServiceProtoP\001ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v7/services;services\242\002\003GAA\252\002 Google.Ads.GoogleAds.V7.Services\312\002 Google\\Ads\\GoogleAds\\V7\\Services\352\002$Google::Ads::GoogleAds::V7::Services'
  _GETSHOPPINGPERFORMANCEVIEWREQUEST.fields_by_name['resource_name']._options = None
  _GETSHOPPINGPERFORMANCEVIEWREQUEST.fields_by_name['resource_name']._serialized_options = b'\342A\001\002\372A2\n0googleads.googleapis.com/ShoppingPerformanceView'
  _SHOPPINGPERFORMANCEVIEWSERVICE._options = None
  _SHOPPINGPERFORMANCEVIEWSERVICE._serialized_options = b'\312A\030googleads.googleapis.com\322A\'https://www.googleapis.com/auth/adwords'
  _SHOPPINGPERFORMANCEVIEWSERVICE.methods_by_name['GetShoppingPerformanceView']._options = None
  _SHOPPINGPERFORMANCEVIEWSERVICE.methods_by_name['GetShoppingPerformanceView']._serialized_options = b'\332A\rresource_name\202\323\344\223\0029\0227/v7/{resource_name=customers/*/shoppingPerformanceView}'
  _GETSHOPPINGPERFORMANCEVIEWREQUEST._serialized_start=293
  _GETSHOPPINGPERFORMANCEVIEWREQUEST._serialized_end=424
  _SHOPPINGPERFORMANCEVIEWSERVICE._serialized_start=427
  _SHOPPINGPERFORMANCEVIEWSERVICE._serialized_end=771
# @@protoc_insertion_point(module_scope)
