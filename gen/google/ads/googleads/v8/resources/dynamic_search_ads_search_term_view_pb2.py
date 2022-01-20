# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v8/resources/dynamic_search_ads_search_term_view.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nKgoogle/ads/googleads/v8/resources/dynamic_search_ads_search_term_view.proto\x12!google.ads.googleads.v8.resources\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1cgoogle/api/annotations.proto\"\xca\x06\n\x1e\x44ynamicSearchAdsSearchTermView\x12\x65\n\rresource_name\x18\x01 \x01(\tB@\xe2\x41\x01\x03\xfa\x41\x39\n7googleads.googleapis.com/DynamicSearchAdsSearchTermViewR\x0cresourceName\x12*\n\x0bsearch_term\x18\t \x01(\tB\x04\xe2\x41\x01\x03H\x00R\nsearchTerm\x88\x01\x01\x12%\n\x08headline\x18\n \x01(\tB\x04\xe2\x41\x01\x03H\x01R\x08headline\x88\x01\x01\x12,\n\x0clanding_page\x18\x0b \x01(\tB\x04\xe2\x41\x01\x03H\x02R\x0blandingPage\x88\x01\x01\x12$\n\x08page_url\x18\x0c \x01(\tB\x04\xe2\x41\x01\x03H\x03R\x07pageUrl\x88\x01\x01\x12;\n\x14has_negative_keyword\x18\r \x01(\x08\x42\x04\xe2\x41\x01\x03H\x04R\x12hasNegativeKeyword\x88\x01\x01\x12;\n\x14has_matching_keyword\x18\x0e \x01(\x08\x42\x04\xe2\x41\x01\x03H\x05R\x12hasMatchingKeyword\x88\x01\x01\x12\x33\n\x10has_negative_url\x18\x0f \x01(\x08\x42\x04\xe2\x41\x01\x03H\x06R\x0ehasNegativeUrl\x88\x01\x01:\xe8\x01\xea\x41\xe4\x01\n7googleads.googleapis.com/DynamicSearchAdsSearchTermView\x12\xa8\x01\x63ustomers/{customer_id}/dynamicSearchAdsSearchTermViews/{ad_group_id}~{search_term_fingerprint}~{headline_fingerprint}~{landing_page_fingerprint}~{page_url_fingerprint}B\x0e\n\x0c_search_termB\x0b\n\t_headlineB\x0f\n\r_landing_pageB\x0b\n\t_page_urlB\x17\n\x15_has_negative_keywordB\x17\n\x15_has_matching_keywordB\x13\n\x11_has_negative_urlB\x90\x02\n%com.google.ads.googleads.v8.resourcesB#DynamicSearchAdsSearchTermViewProtoP\x01ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v8/resources;resources\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V8.Resources\xca\x02!Google\\Ads\\GoogleAds\\V8\\Resources\xea\x02%Google::Ads::GoogleAds::V8::Resourcesb\x06proto3')



_DYNAMICSEARCHADSSEARCHTERMVIEW = DESCRIPTOR.message_types_by_name['DynamicSearchAdsSearchTermView']
DynamicSearchAdsSearchTermView = _reflection.GeneratedProtocolMessageType('DynamicSearchAdsSearchTermView', (_message.Message,), {
  'DESCRIPTOR' : _DYNAMICSEARCHADSSEARCHTERMVIEW,
  '__module__' : 'google.ads.googleads.v8.resources.dynamic_search_ads_search_term_view_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v8.resources.DynamicSearchAdsSearchTermView)
  })
_sym_db.RegisterMessage(DynamicSearchAdsSearchTermView)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n%com.google.ads.googleads.v8.resourcesB#DynamicSearchAdsSearchTermViewProtoP\001ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v8/resources;resources\242\002\003GAA\252\002!Google.Ads.GoogleAds.V8.Resources\312\002!Google\\Ads\\GoogleAds\\V8\\Resources\352\002%Google::Ads::GoogleAds::V8::Resources'
  _DYNAMICSEARCHADSSEARCHTERMVIEW.fields_by_name['resource_name']._options = None
  _DYNAMICSEARCHADSSEARCHTERMVIEW.fields_by_name['resource_name']._serialized_options = b'\342A\001\003\372A9\n7googleads.googleapis.com/DynamicSearchAdsSearchTermView'
  _DYNAMICSEARCHADSSEARCHTERMVIEW.fields_by_name['search_term']._options = None
  _DYNAMICSEARCHADSSEARCHTERMVIEW.fields_by_name['search_term']._serialized_options = b'\342A\001\003'
  _DYNAMICSEARCHADSSEARCHTERMVIEW.fields_by_name['headline']._options = None
  _DYNAMICSEARCHADSSEARCHTERMVIEW.fields_by_name['headline']._serialized_options = b'\342A\001\003'
  _DYNAMICSEARCHADSSEARCHTERMVIEW.fields_by_name['landing_page']._options = None
  _DYNAMICSEARCHADSSEARCHTERMVIEW.fields_by_name['landing_page']._serialized_options = b'\342A\001\003'
  _DYNAMICSEARCHADSSEARCHTERMVIEW.fields_by_name['page_url']._options = None
  _DYNAMICSEARCHADSSEARCHTERMVIEW.fields_by_name['page_url']._serialized_options = b'\342A\001\003'
  _DYNAMICSEARCHADSSEARCHTERMVIEW.fields_by_name['has_negative_keyword']._options = None
  _DYNAMICSEARCHADSSEARCHTERMVIEW.fields_by_name['has_negative_keyword']._serialized_options = b'\342A\001\003'
  _DYNAMICSEARCHADSSEARCHTERMVIEW.fields_by_name['has_matching_keyword']._options = None
  _DYNAMICSEARCHADSSEARCHTERMVIEW.fields_by_name['has_matching_keyword']._serialized_options = b'\342A\001\003'
  _DYNAMICSEARCHADSSEARCHTERMVIEW.fields_by_name['has_negative_url']._options = None
  _DYNAMICSEARCHADSSEARCHTERMVIEW.fields_by_name['has_negative_url']._serialized_options = b'\342A\001\003'
  _DYNAMICSEARCHADSSEARCHTERMVIEW._options = None
  _DYNAMICSEARCHADSSEARCHTERMVIEW._serialized_options = b'\352A\344\001\n7googleads.googleapis.com/DynamicSearchAdsSearchTermView\022\250\001customers/{customer_id}/dynamicSearchAdsSearchTermViews/{ad_group_id}~{search_term_fingerprint}~{headline_fingerprint}~{landing_page_fingerprint}~{page_url_fingerprint}'
  _DYNAMICSEARCHADSSEARCHTERMVIEW._serialized_start=205
  _DYNAMICSEARCHADSSEARCHTERMVIEW._serialized_end=1047
# @@protoc_insertion_point(module_scope)
