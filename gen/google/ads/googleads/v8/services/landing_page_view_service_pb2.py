# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v8/services/landing_page_view_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.googleads.v8.resources import landing_page_view_pb2 as google_dot_ads_dot_googleads_dot_v8_dot_resources_dot_landing__page__view__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import client_pb2 as google_dot_api_dot_client__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n@google/ads/googleads/v8/services/landing_page_view_service.proto\x12 google.ads.googleads.v8.services\x1a\x39google/ads/googleads/v8/resources/landing_page_view.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\"s\n\x19GetLandingPageViewRequest\x12V\n\rresource_name\x18\x01 \x01(\tB1\xe2\x41\x01\x02\xfa\x41*\n(googleads.googleapis.com/LandingPageViewR\x0cresourceName2\xb3\x02\n\x16LandingPageViewService\x12\xd1\x01\n\x12GetLandingPageView\x12;.google.ads.googleads.v8.services.GetLandingPageViewRequest\x1a\x32.google.ads.googleads.v8.resources.LandingPageView\"J\xda\x41\rresource_name\x82\xd3\xe4\x93\x02\x34\x12\x32/v8/{resource_name=customers/*/landingPageViews/*}\x1a\x45\xca\x41\x18googleads.googleapis.com\xd2\x41\'https://www.googleapis.com/auth/adwordsB\x82\x02\n$com.google.ads.googleads.v8.servicesB\x1bLandingPageViewServiceProtoP\x01ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v8/services;services\xa2\x02\x03GAA\xaa\x02 Google.Ads.GoogleAds.V8.Services\xca\x02 Google\\Ads\\GoogleAds\\V8\\Services\xea\x02$Google::Ads::GoogleAds::V8::Servicesb\x06proto3')



_GETLANDINGPAGEVIEWREQUEST = DESCRIPTOR.message_types_by_name['GetLandingPageViewRequest']
GetLandingPageViewRequest = _reflection.GeneratedProtocolMessageType('GetLandingPageViewRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETLANDINGPAGEVIEWREQUEST,
  '__module__' : 'google.ads.googleads.v8.services.landing_page_view_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v8.services.GetLandingPageViewRequest)
  })
_sym_db.RegisterMessage(GetLandingPageViewRequest)

_LANDINGPAGEVIEWSERVICE = DESCRIPTOR.services_by_name['LandingPageViewService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n$com.google.ads.googleads.v8.servicesB\033LandingPageViewServiceProtoP\001ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v8/services;services\242\002\003GAA\252\002 Google.Ads.GoogleAds.V8.Services\312\002 Google\\Ads\\GoogleAds\\V8\\Services\352\002$Google::Ads::GoogleAds::V8::Services'
  _GETLANDINGPAGEVIEWREQUEST.fields_by_name['resource_name']._options = None
  _GETLANDINGPAGEVIEWREQUEST.fields_by_name['resource_name']._serialized_options = b'\342A\001\002\372A*\n(googleads.googleapis.com/LandingPageView'
  _LANDINGPAGEVIEWSERVICE._options = None
  _LANDINGPAGEVIEWSERVICE._serialized_options = b'\312A\030googleads.googleapis.com\322A\'https://www.googleapis.com/auth/adwords'
  _LANDINGPAGEVIEWSERVICE.methods_by_name['GetLandingPageView']._options = None
  _LANDINGPAGEVIEWSERVICE.methods_by_name['GetLandingPageView']._serialized_options = b'\332A\rresource_name\202\323\344\223\0024\0222/v8/{resource_name=customers/*/landingPageViews/*}'
  _GETLANDINGPAGEVIEWREQUEST._serialized_start=276
  _GETLANDINGPAGEVIEWREQUEST._serialized_end=391
  _LANDINGPAGEVIEWSERVICE._serialized_start=394
  _LANDINGPAGEVIEWSERVICE._serialized_end=701
# @@protoc_insertion_point(module_scope)
