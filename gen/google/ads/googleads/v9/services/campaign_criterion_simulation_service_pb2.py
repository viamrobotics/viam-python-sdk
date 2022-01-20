# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v9/services/campaign_criterion_simulation_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.googleads.v9.resources import campaign_criterion_simulation_pb2 as google_dot_ads_dot_googleads_dot_v9_dot_resources_dot_campaign__criterion__simulation__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import client_pb2 as google_dot_api_dot_client__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nLgoogle/ads/googleads/v9/services/campaign_criterion_simulation_service.proto\x12 google.ads.googleads.v9.services\x1a\x45google/ads/googleads/v9/resources/campaign_criterion_simulation.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\"\x8b\x01\n%GetCampaignCriterionSimulationRequest\x12\x62\n\rresource_name\x18\x01 \x01(\tB=\xe2\x41\x01\x02\xfa\x41\x36\n4googleads.googleapis.com/CampaignCriterionSimulationR\x0cresourceName2\xef\x02\n\"CampaignCriterionSimulationService\x12\x81\x02\n\x1eGetCampaignCriterionSimulation\x12G.google.ads.googleads.v9.services.GetCampaignCriterionSimulationRequest\x1a>.google.ads.googleads.v9.resources.CampaignCriterionSimulation\"V\xda\x41\rresource_name\x82\xd3\xe4\x93\x02@\x12>/v9/{resource_name=customers/*/campaignCriterionSimulations/*}\x1a\x45\xca\x41\x18googleads.googleapis.com\xd2\x41\'https://www.googleapis.com/auth/adwordsB\x8e\x02\n$com.google.ads.googleads.v9.servicesB\'CampaignCriterionSimulationServiceProtoP\x01ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v9/services;services\xa2\x02\x03GAA\xaa\x02 Google.Ads.GoogleAds.V9.Services\xca\x02 Google\\Ads\\GoogleAds\\V9\\Services\xea\x02$Google::Ads::GoogleAds::V9::Servicesb\x06proto3')



_GETCAMPAIGNCRITERIONSIMULATIONREQUEST = DESCRIPTOR.message_types_by_name['GetCampaignCriterionSimulationRequest']
GetCampaignCriterionSimulationRequest = _reflection.GeneratedProtocolMessageType('GetCampaignCriterionSimulationRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETCAMPAIGNCRITERIONSIMULATIONREQUEST,
  '__module__' : 'google.ads.googleads.v9.services.campaign_criterion_simulation_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v9.services.GetCampaignCriterionSimulationRequest)
  })
_sym_db.RegisterMessage(GetCampaignCriterionSimulationRequest)

_CAMPAIGNCRITERIONSIMULATIONSERVICE = DESCRIPTOR.services_by_name['CampaignCriterionSimulationService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n$com.google.ads.googleads.v9.servicesB\'CampaignCriterionSimulationServiceProtoP\001ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v9/services;services\242\002\003GAA\252\002 Google.Ads.GoogleAds.V9.Services\312\002 Google\\Ads\\GoogleAds\\V9\\Services\352\002$Google::Ads::GoogleAds::V9::Services'
  _GETCAMPAIGNCRITERIONSIMULATIONREQUEST.fields_by_name['resource_name']._options = None
  _GETCAMPAIGNCRITERIONSIMULATIONREQUEST.fields_by_name['resource_name']._serialized_options = b'\342A\001\002\372A6\n4googleads.googleapis.com/CampaignCriterionSimulation'
  _CAMPAIGNCRITERIONSIMULATIONSERVICE._options = None
  _CAMPAIGNCRITERIONSIMULATIONSERVICE._serialized_options = b'\312A\030googleads.googleapis.com\322A\'https://www.googleapis.com/auth/adwords'
  _CAMPAIGNCRITERIONSIMULATIONSERVICE.methods_by_name['GetCampaignCriterionSimulation']._options = None
  _CAMPAIGNCRITERIONSIMULATIONSERVICE.methods_by_name['GetCampaignCriterionSimulation']._serialized_options = b'\332A\rresource_name\202\323\344\223\002@\022>/v9/{resource_name=customers/*/campaignCriterionSimulations/*}'
  _GETCAMPAIGNCRITERIONSIMULATIONREQUEST._serialized_start=301
  _GETCAMPAIGNCRITERIONSIMULATIONREQUEST._serialized_end=440
  _CAMPAIGNCRITERIONSIMULATIONSERVICE._serialized_start=443
  _CAMPAIGNCRITERIONSIMULATIONSERVICE._serialized_end=810
# @@protoc_insertion_point(module_scope)
