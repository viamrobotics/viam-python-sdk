# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v9/services/distance_view_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.googleads.v9.resources import distance_view_pb2 as google_dot_ads_dot_googleads_dot_v9_dot_resources_dot_distance__view__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import client_pb2 as google_dot_api_dot_client__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n<google/ads/googleads/v9/services/distance_view_service.proto\x12 google.ads.googleads.v9.services\x1a\x35google/ads/googleads/v9/resources/distance_view.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\"m\n\x16GetDistanceViewRequest\x12S\n\rresource_name\x18\x01 \x01(\tB.\xe2\x41\x01\x02\xfa\x41\'\n%googleads.googleapis.com/DistanceViewR\x0cresourceName2\xa4\x02\n\x13\x44istanceViewService\x12\xc5\x01\n\x0fGetDistanceView\x12\x38.google.ads.googleads.v9.services.GetDistanceViewRequest\x1a/.google.ads.googleads.v9.resources.DistanceView\"G\xda\x41\rresource_name\x82\xd3\xe4\x93\x02\x31\x12//v9/{resource_name=customers/*/distanceViews/*}\x1a\x45\xca\x41\x18googleads.googleapis.com\xd2\x41\'https://www.googleapis.com/auth/adwordsB\xff\x01\n$com.google.ads.googleads.v9.servicesB\x18\x44istanceViewServiceProtoP\x01ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v9/services;services\xa2\x02\x03GAA\xaa\x02 Google.Ads.GoogleAds.V9.Services\xca\x02 Google\\Ads\\GoogleAds\\V9\\Services\xea\x02$Google::Ads::GoogleAds::V9::Servicesb\x06proto3')



_GETDISTANCEVIEWREQUEST = DESCRIPTOR.message_types_by_name['GetDistanceViewRequest']
GetDistanceViewRequest = _reflection.GeneratedProtocolMessageType('GetDistanceViewRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETDISTANCEVIEWREQUEST,
  '__module__' : 'google.ads.googleads.v9.services.distance_view_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v9.services.GetDistanceViewRequest)
  })
_sym_db.RegisterMessage(GetDistanceViewRequest)

_DISTANCEVIEWSERVICE = DESCRIPTOR.services_by_name['DistanceViewService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n$com.google.ads.googleads.v9.servicesB\030DistanceViewServiceProtoP\001ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v9/services;services\242\002\003GAA\252\002 Google.Ads.GoogleAds.V9.Services\312\002 Google\\Ads\\GoogleAds\\V9\\Services\352\002$Google::Ads::GoogleAds::V9::Services'
  _GETDISTANCEVIEWREQUEST.fields_by_name['resource_name']._options = None
  _GETDISTANCEVIEWREQUEST.fields_by_name['resource_name']._serialized_options = b'\342A\001\002\372A\'\n%googleads.googleapis.com/DistanceView'
  _DISTANCEVIEWSERVICE._options = None
  _DISTANCEVIEWSERVICE._serialized_options = b'\312A\030googleads.googleapis.com\322A\'https://www.googleapis.com/auth/adwords'
  _DISTANCEVIEWSERVICE.methods_by_name['GetDistanceView']._options = None
  _DISTANCEVIEWSERVICE.methods_by_name['GetDistanceView']._serialized_options = b'\332A\rresource_name\202\323\344\223\0021\022//v9/{resource_name=customers/*/distanceViews/*}'
  _GETDISTANCEVIEWREQUEST._serialized_start=268
  _GETDISTANCEVIEWREQUEST._serialized_end=377
  _DISTANCEVIEWSERVICE._serialized_start=380
  _DISTANCEVIEWSERVICE._serialized_end=672
# @@protoc_insertion_point(module_scope)
