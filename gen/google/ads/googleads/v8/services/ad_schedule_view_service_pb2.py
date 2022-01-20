# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v8/services/ad_schedule_view_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.googleads.v8.resources import ad_schedule_view_pb2 as google_dot_ads_dot_googleads_dot_v8_dot_resources_dot_ad__schedule__view__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import client_pb2 as google_dot_api_dot_client__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n?google/ads/googleads/v8/services/ad_schedule_view_service.proto\x12 google.ads.googleads.v8.services\x1a\x38google/ads/googleads/v8/resources/ad_schedule_view.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\"q\n\x18GetAdScheduleViewRequest\x12U\n\rresource_name\x18\x01 \x01(\tB0\xe2\x41\x01\x02\xfa\x41)\n\'googleads.googleapis.com/AdScheduleViewR\x0cresourceName2\xae\x02\n\x15\x41\x64ScheduleViewService\x12\xcd\x01\n\x11GetAdScheduleView\x12:.google.ads.googleads.v8.services.GetAdScheduleViewRequest\x1a\x31.google.ads.googleads.v8.resources.AdScheduleView\"I\xda\x41\rresource_name\x82\xd3\xe4\x93\x02\x33\x12\x31/v8/{resource_name=customers/*/adScheduleViews/*}\x1a\x45\xca\x41\x18googleads.googleapis.com\xd2\x41\'https://www.googleapis.com/auth/adwordsB\x81\x02\n$com.google.ads.googleads.v8.servicesB\x1a\x41\x64ScheduleViewServiceProtoP\x01ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v8/services;services\xa2\x02\x03GAA\xaa\x02 Google.Ads.GoogleAds.V8.Services\xca\x02 Google\\Ads\\GoogleAds\\V8\\Services\xea\x02$Google::Ads::GoogleAds::V8::Servicesb\x06proto3')



_GETADSCHEDULEVIEWREQUEST = DESCRIPTOR.message_types_by_name['GetAdScheduleViewRequest']
GetAdScheduleViewRequest = _reflection.GeneratedProtocolMessageType('GetAdScheduleViewRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETADSCHEDULEVIEWREQUEST,
  '__module__' : 'google.ads.googleads.v8.services.ad_schedule_view_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v8.services.GetAdScheduleViewRequest)
  })
_sym_db.RegisterMessage(GetAdScheduleViewRequest)

_ADSCHEDULEVIEWSERVICE = DESCRIPTOR.services_by_name['AdScheduleViewService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n$com.google.ads.googleads.v8.servicesB\032AdScheduleViewServiceProtoP\001ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v8/services;services\242\002\003GAA\252\002 Google.Ads.GoogleAds.V8.Services\312\002 Google\\Ads\\GoogleAds\\V8\\Services\352\002$Google::Ads::GoogleAds::V8::Services'
  _GETADSCHEDULEVIEWREQUEST.fields_by_name['resource_name']._options = None
  _GETADSCHEDULEVIEWREQUEST.fields_by_name['resource_name']._serialized_options = b'\342A\001\002\372A)\n\'googleads.googleapis.com/AdScheduleView'
  _ADSCHEDULEVIEWSERVICE._options = None
  _ADSCHEDULEVIEWSERVICE._serialized_options = b'\312A\030googleads.googleapis.com\322A\'https://www.googleapis.com/auth/adwords'
  _ADSCHEDULEVIEWSERVICE.methods_by_name['GetAdScheduleView']._options = None
  _ADSCHEDULEVIEWSERVICE.methods_by_name['GetAdScheduleView']._serialized_options = b'\332A\rresource_name\202\323\344\223\0023\0221/v8/{resource_name=customers/*/adScheduleViews/*}'
  _GETADSCHEDULEVIEWREQUEST._serialized_start=274
  _GETADSCHEDULEVIEWREQUEST._serialized_end=387
  _ADSCHEDULEVIEWSERVICE._serialized_start=390
  _ADSCHEDULEVIEWSERVICE._serialized_end=692
# @@protoc_insertion_point(module_scope)
