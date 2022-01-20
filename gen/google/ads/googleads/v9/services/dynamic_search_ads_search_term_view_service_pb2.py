# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v9/services/dynamic_search_ads_search_term_view_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.googleads.v9.resources import dynamic_search_ads_search_term_view_pb2 as google_dot_ads_dot_googleads_dot_v9_dot_resources_dot_dynamic__search__ads__search__term__view__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import client_pb2 as google_dot_api_dot_client__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nRgoogle/ads/googleads/v9/services/dynamic_search_ads_search_term_view_service.proto\x12 google.ads.googleads.v9.services\x1aKgoogle/ads/googleads/v9/resources/dynamic_search_ads_search_term_view.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\"\x91\x01\n(GetDynamicSearchAdsSearchTermViewRequest\x12\x65\n\rresource_name\x18\x01 \x01(\tB@\xe2\x41\x01\x02\xfa\x41\x39\n7googleads.googleapis.com/DynamicSearchAdsSearchTermViewR\x0cresourceName2\xfe\x02\n%DynamicSearchAdsSearchTermViewService\x12\x8d\x02\n!GetDynamicSearchAdsSearchTermView\x12J.google.ads.googleads.v9.services.GetDynamicSearchAdsSearchTermViewRequest\x1a\x41.google.ads.googleads.v9.resources.DynamicSearchAdsSearchTermView\"Y\xda\x41\rresource_name\x82\xd3\xe4\x93\x02\x43\x12\x41/v9/{resource_name=customers/*/dynamicSearchAdsSearchTermViews/*}\x1a\x45\xca\x41\x18googleads.googleapis.com\xd2\x41\'https://www.googleapis.com/auth/adwordsB\x91\x02\n$com.google.ads.googleads.v9.servicesB*DynamicSearchAdsSearchTermViewServiceProtoP\x01ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v9/services;services\xa2\x02\x03GAA\xaa\x02 Google.Ads.GoogleAds.V9.Services\xca\x02 Google\\Ads\\GoogleAds\\V9\\Services\xea\x02$Google::Ads::GoogleAds::V9::Servicesb\x06proto3')



_GETDYNAMICSEARCHADSSEARCHTERMVIEWREQUEST = DESCRIPTOR.message_types_by_name['GetDynamicSearchAdsSearchTermViewRequest']
GetDynamicSearchAdsSearchTermViewRequest = _reflection.GeneratedProtocolMessageType('GetDynamicSearchAdsSearchTermViewRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETDYNAMICSEARCHADSSEARCHTERMVIEWREQUEST,
  '__module__' : 'google.ads.googleads.v9.services.dynamic_search_ads_search_term_view_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v9.services.GetDynamicSearchAdsSearchTermViewRequest)
  })
_sym_db.RegisterMessage(GetDynamicSearchAdsSearchTermViewRequest)

_DYNAMICSEARCHADSSEARCHTERMVIEWSERVICE = DESCRIPTOR.services_by_name['DynamicSearchAdsSearchTermViewService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n$com.google.ads.googleads.v9.servicesB*DynamicSearchAdsSearchTermViewServiceProtoP\001ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v9/services;services\242\002\003GAA\252\002 Google.Ads.GoogleAds.V9.Services\312\002 Google\\Ads\\GoogleAds\\V9\\Services\352\002$Google::Ads::GoogleAds::V9::Services'
  _GETDYNAMICSEARCHADSSEARCHTERMVIEWREQUEST.fields_by_name['resource_name']._options = None
  _GETDYNAMICSEARCHADSSEARCHTERMVIEWREQUEST.fields_by_name['resource_name']._serialized_options = b'\342A\001\002\372A9\n7googleads.googleapis.com/DynamicSearchAdsSearchTermView'
  _DYNAMICSEARCHADSSEARCHTERMVIEWSERVICE._options = None
  _DYNAMICSEARCHADSSEARCHTERMVIEWSERVICE._serialized_options = b'\312A\030googleads.googleapis.com\322A\'https://www.googleapis.com/auth/adwords'
  _DYNAMICSEARCHADSSEARCHTERMVIEWSERVICE.methods_by_name['GetDynamicSearchAdsSearchTermView']._options = None
  _DYNAMICSEARCHADSSEARCHTERMVIEWSERVICE.methods_by_name['GetDynamicSearchAdsSearchTermView']._serialized_options = b'\332A\rresource_name\202\323\344\223\002C\022A/v9/{resource_name=customers/*/dynamicSearchAdsSearchTermViews/*}'
  _GETDYNAMICSEARCHADSSEARCHTERMVIEWREQUEST._serialized_start=313
  _GETDYNAMICSEARCHADSSEARCHTERMVIEWREQUEST._serialized_end=458
  _DYNAMICSEARCHADSSEARCHTERMVIEWSERVICE._serialized_start=461
  _DYNAMICSEARCHADSSEARCHTERMVIEWSERVICE._serialized_end=843
# @@protoc_insertion_point(module_scope)
