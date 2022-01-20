# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v9/resources/search_term_view.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.googleads.v9.enums import search_term_targeting_status_pb2 as google_dot_ads_dot_googleads_dot_v9_dot_enums_dot_search__term__targeting__status__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n8google/ads/googleads/v9/resources/search_term_view.proto\x12!google.ads.googleads.v9.resources\x1a@google/ads/googleads/v9/enums/search_term_targeting_status.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1cgoogle/api/annotations.proto\"\xec\x03\n\x0eSearchTermView\x12U\n\rresource_name\x18\x01 \x01(\tB0\xe2\x41\x01\x03\xfa\x41)\n\'googleads.googleapis.com/SearchTermViewR\x0cresourceName\x12*\n\x0bsearch_term\x18\x05 \x01(\tB\x04\xe2\x41\x01\x03H\x00R\nsearchTerm\x88\x01\x01\x12I\n\x08\x61\x64_group\x18\x06 \x01(\tB)\xe2\x41\x01\x03\xfa\x41\"\n googleads.googleapis.com/AdGroupH\x01R\x07\x61\x64Group\x88\x01\x01\x12t\n\x06status\x18\x04 \x01(\x0e\x32V.google.ads.googleads.v9.enums.SearchTermTargetingStatusEnum.SearchTermTargetingStatusB\x04\xe2\x41\x01\x03R\x06status:y\xea\x41v\n\'googleads.googleapis.com/SearchTermView\x12Kcustomers/{customer_id}/searchTermViews/{campaign_id}~{ad_group_id}~{query}B\x0e\n\x0c_search_termB\x0b\n\t_ad_groupB\x80\x02\n%com.google.ads.googleads.v9.resourcesB\x13SearchTermViewProtoP\x01ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v9/resources;resources\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V9.Resources\xca\x02!Google\\Ads\\GoogleAds\\V9\\Resources\xea\x02%Google::Ads::GoogleAds::V9::Resourcesb\x06proto3')



_SEARCHTERMVIEW = DESCRIPTOR.message_types_by_name['SearchTermView']
SearchTermView = _reflection.GeneratedProtocolMessageType('SearchTermView', (_message.Message,), {
  'DESCRIPTOR' : _SEARCHTERMVIEW,
  '__module__' : 'google.ads.googleads.v9.resources.search_term_view_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v9.resources.SearchTermView)
  })
_sym_db.RegisterMessage(SearchTermView)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n%com.google.ads.googleads.v9.resourcesB\023SearchTermViewProtoP\001ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v9/resources;resources\242\002\003GAA\252\002!Google.Ads.GoogleAds.V9.Resources\312\002!Google\\Ads\\GoogleAds\\V9\\Resources\352\002%Google::Ads::GoogleAds::V9::Resources'
  _SEARCHTERMVIEW.fields_by_name['resource_name']._options = None
  _SEARCHTERMVIEW.fields_by_name['resource_name']._serialized_options = b'\342A\001\003\372A)\n\'googleads.googleapis.com/SearchTermView'
  _SEARCHTERMVIEW.fields_by_name['search_term']._options = None
  _SEARCHTERMVIEW.fields_by_name['search_term']._serialized_options = b'\342A\001\003'
  _SEARCHTERMVIEW.fields_by_name['ad_group']._options = None
  _SEARCHTERMVIEW.fields_by_name['ad_group']._serialized_options = b'\342A\001\003\372A\"\n googleads.googleapis.com/AdGroup'
  _SEARCHTERMVIEW.fields_by_name['status']._options = None
  _SEARCHTERMVIEW.fields_by_name['status']._serialized_options = b'\342A\001\003'
  _SEARCHTERMVIEW._options = None
  _SEARCHTERMVIEW._serialized_options = b'\352Av\n\'googleads.googleapis.com/SearchTermView\022Kcustomers/{customer_id}/searchTermViews/{campaign_id}~{ad_group_id}~{query}'
  _SEARCHTERMVIEW._serialized_start=252
  _SEARCHTERMVIEW._serialized_end=744
# @@protoc_insertion_point(module_scope)
