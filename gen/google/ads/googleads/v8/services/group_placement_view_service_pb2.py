# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v8/services/group_placement_view_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.googleads.v8.resources import group_placement_view_pb2 as google_dot_ads_dot_googleads_dot_v8_dot_resources_dot_group__placement__view__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import client_pb2 as google_dot_api_dot_client__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nCgoogle/ads/googleads/v8/services/group_placement_view_service.proto\x12 google.ads.googleads.v8.services\x1a<google/ads/googleads/v8/resources/group_placement_view.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\"y\n\x1cGetGroupPlacementViewRequest\x12Y\n\rresource_name\x18\x01 \x01(\tB4\xe2\x41\x01\x02\xfa\x41-\n+googleads.googleapis.com/GroupPlacementViewR\x0cresourceName2\xc2\x02\n\x19GroupPlacementViewService\x12\xdd\x01\n\x15GetGroupPlacementView\x12>.google.ads.googleads.v8.services.GetGroupPlacementViewRequest\x1a\x35.google.ads.googleads.v8.resources.GroupPlacementView\"M\xda\x41\rresource_name\x82\xd3\xe4\x93\x02\x37\x12\x35/v8/{resource_name=customers/*/groupPlacementViews/*}\x1a\x45\xca\x41\x18googleads.googleapis.com\xd2\x41\'https://www.googleapis.com/auth/adwordsB\x85\x02\n$com.google.ads.googleads.v8.servicesB\x1eGroupPlacementViewServiceProtoP\x01ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v8/services;services\xa2\x02\x03GAA\xaa\x02 Google.Ads.GoogleAds.V8.Services\xca\x02 Google\\Ads\\GoogleAds\\V8\\Services\xea\x02$Google::Ads::GoogleAds::V8::Servicesb\x06proto3')



_GETGROUPPLACEMENTVIEWREQUEST = DESCRIPTOR.message_types_by_name['GetGroupPlacementViewRequest']
GetGroupPlacementViewRequest = _reflection.GeneratedProtocolMessageType('GetGroupPlacementViewRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETGROUPPLACEMENTVIEWREQUEST,
  '__module__' : 'google.ads.googleads.v8.services.group_placement_view_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v8.services.GetGroupPlacementViewRequest)
  })
_sym_db.RegisterMessage(GetGroupPlacementViewRequest)

_GROUPPLACEMENTVIEWSERVICE = DESCRIPTOR.services_by_name['GroupPlacementViewService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n$com.google.ads.googleads.v8.servicesB\036GroupPlacementViewServiceProtoP\001ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v8/services;services\242\002\003GAA\252\002 Google.Ads.GoogleAds.V8.Services\312\002 Google\\Ads\\GoogleAds\\V8\\Services\352\002$Google::Ads::GoogleAds::V8::Services'
  _GETGROUPPLACEMENTVIEWREQUEST.fields_by_name['resource_name']._options = None
  _GETGROUPPLACEMENTVIEWREQUEST.fields_by_name['resource_name']._serialized_options = b'\342A\001\002\372A-\n+googleads.googleapis.com/GroupPlacementView'
  _GROUPPLACEMENTVIEWSERVICE._options = None
  _GROUPPLACEMENTVIEWSERVICE._serialized_options = b'\312A\030googleads.googleapis.com\322A\'https://www.googleapis.com/auth/adwords'
  _GROUPPLACEMENTVIEWSERVICE.methods_by_name['GetGroupPlacementView']._options = None
  _GROUPPLACEMENTVIEWSERVICE.methods_by_name['GetGroupPlacementView']._serialized_options = b'\332A\rresource_name\202\323\344\223\0027\0225/v8/{resource_name=customers/*/groupPlacementViews/*}'
  _GETGROUPPLACEMENTVIEWREQUEST._serialized_start=282
  _GETGROUPPLACEMENTVIEWREQUEST._serialized_end=403
  _GROUPPLACEMENTVIEWSERVICE._serialized_start=406
  _GROUPPLACEMENTVIEWSERVICE._serialized_end=728
# @@protoc_insertion_point(module_scope)
