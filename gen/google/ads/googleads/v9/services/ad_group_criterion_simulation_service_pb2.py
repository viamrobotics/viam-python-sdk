# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v9/services/ad_group_criterion_simulation_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.googleads.v9.resources import ad_group_criterion_simulation_pb2 as google_dot_ads_dot_googleads_dot_v9_dot_resources_dot_ad__group__criterion__simulation__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import client_pb2 as google_dot_api_dot_client__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nLgoogle/ads/googleads/v9/services/ad_group_criterion_simulation_service.proto\x12 google.ads.googleads.v9.services\x1a\x45google/ads/googleads/v9/resources/ad_group_criterion_simulation.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\"\x89\x01\n$GetAdGroupCriterionSimulationRequest\x12\x61\n\rresource_name\x18\x01 \x01(\tB<\xe2\x41\x01\x02\xfa\x41\x35\n3googleads.googleapis.com/AdGroupCriterionSimulationR\x0cresourceName2\xea\x02\n!AdGroupCriterionSimulationService\x12\xfd\x01\n\x1dGetAdGroupCriterionSimulation\x12\x46.google.ads.googleads.v9.services.GetAdGroupCriterionSimulationRequest\x1a=.google.ads.googleads.v9.resources.AdGroupCriterionSimulation\"U\xda\x41\rresource_name\x82\xd3\xe4\x93\x02?\x12=/v9/{resource_name=customers/*/adGroupCriterionSimulations/*}\x1a\x45\xca\x41\x18googleads.googleapis.com\xd2\x41\'https://www.googleapis.com/auth/adwordsB\x8d\x02\n$com.google.ads.googleads.v9.servicesB&AdGroupCriterionSimulationServiceProtoP\x01ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v9/services;services\xa2\x02\x03GAA\xaa\x02 Google.Ads.GoogleAds.V9.Services\xca\x02 Google\\Ads\\GoogleAds\\V9\\Services\xea\x02$Google::Ads::GoogleAds::V9::Servicesb\x06proto3')



_GETADGROUPCRITERIONSIMULATIONREQUEST = DESCRIPTOR.message_types_by_name['GetAdGroupCriterionSimulationRequest']
GetAdGroupCriterionSimulationRequest = _reflection.GeneratedProtocolMessageType('GetAdGroupCriterionSimulationRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETADGROUPCRITERIONSIMULATIONREQUEST,
  '__module__' : 'google.ads.googleads.v9.services.ad_group_criterion_simulation_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v9.services.GetAdGroupCriterionSimulationRequest)
  })
_sym_db.RegisterMessage(GetAdGroupCriterionSimulationRequest)

_ADGROUPCRITERIONSIMULATIONSERVICE = DESCRIPTOR.services_by_name['AdGroupCriterionSimulationService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n$com.google.ads.googleads.v9.servicesB&AdGroupCriterionSimulationServiceProtoP\001ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v9/services;services\242\002\003GAA\252\002 Google.Ads.GoogleAds.V9.Services\312\002 Google\\Ads\\GoogleAds\\V9\\Services\352\002$Google::Ads::GoogleAds::V9::Services'
  _GETADGROUPCRITERIONSIMULATIONREQUEST.fields_by_name['resource_name']._options = None
  _GETADGROUPCRITERIONSIMULATIONREQUEST.fields_by_name['resource_name']._serialized_options = b'\342A\001\002\372A5\n3googleads.googleapis.com/AdGroupCriterionSimulation'
  _ADGROUPCRITERIONSIMULATIONSERVICE._options = None
  _ADGROUPCRITERIONSIMULATIONSERVICE._serialized_options = b'\312A\030googleads.googleapis.com\322A\'https://www.googleapis.com/auth/adwords'
  _ADGROUPCRITERIONSIMULATIONSERVICE.methods_by_name['GetAdGroupCriterionSimulation']._options = None
  _ADGROUPCRITERIONSIMULATIONSERVICE.methods_by_name['GetAdGroupCriterionSimulation']._serialized_options = b'\332A\rresource_name\202\323\344\223\002?\022=/v9/{resource_name=customers/*/adGroupCriterionSimulations/*}'
  _GETADGROUPCRITERIONSIMULATIONREQUEST._serialized_start=301
  _GETADGROUPCRITERIONSIMULATIONREQUEST._serialized_end=438
  _ADGROUPCRITERIONSIMULATIONSERVICE._serialized_start=441
  _ADGROUPCRITERIONSIMULATIONSERVICE._serialized_end=803
# @@protoc_insertion_point(module_scope)
