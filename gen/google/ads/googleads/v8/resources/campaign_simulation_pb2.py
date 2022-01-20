# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v8/resources/campaign_simulation.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.googleads.v8.common import simulation_pb2 as google_dot_ads_dot_googleads_dot_v8_dot_common_dot_simulation__pb2
from google.ads.googleads.v8.enums import simulation_modification_method_pb2 as google_dot_ads_dot_googleads_dot_v8_dot_enums_dot_simulation__modification__method__pb2
from google.ads.googleads.v8.enums import simulation_type_pb2 as google_dot_ads_dot_googleads_dot_v8_dot_enums_dot_simulation__type__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n;google/ads/googleads/v8/resources/campaign_simulation.proto\x12!google.ads.googleads.v8.resources\x1a/google/ads/googleads/v8/common/simulation.proto\x1a\x42google/ads/googleads/v8/enums/simulation_modification_method.proto\x1a\x33google/ads/googleads/v8/enums/simulation_type.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1cgoogle/api/annotations.proto\"\xf3\t\n\x12\x43\x61mpaignSimulation\x12Y\n\rresource_name\x18\x01 \x01(\tB4\xe2\x41\x01\x03\xfa\x41-\n+googleads.googleapis.com/CampaignSimulationR\x0cresourceName\x12%\n\x0b\x63\x61mpaign_id\x18\x02 \x01(\x03\x42\x04\xe2\x41\x01\x03R\ncampaignId\x12Z\n\x04type\x18\x03 \x01(\x0e\x32@.google.ads.googleads.v8.enums.SimulationTypeEnum.SimulationTypeB\x04\xe2\x41\x01\x03R\x04type\x12\x93\x01\n\x13modification_method\x18\x04 \x01(\x0e\x32\\.google.ads.googleads.v8.enums.SimulationModificationMethodEnum.SimulationModificationMethodB\x04\xe2\x41\x01\x03R\x12modificationMethod\x12#\n\nstart_date\x18\x05 \x01(\tB\x04\xe2\x41\x01\x03R\tstartDate\x12\x1f\n\x08\x65nd_date\x18\x06 \x01(\tB\x04\xe2\x41\x01\x03R\x07\x65ndDate\x12n\n\x12\x63pc_bid_point_list\x18\x07 \x01(\x0b\x32\x39.google.ads.googleads.v8.common.CpcBidSimulationPointListB\x04\xe2\x41\x01\x03H\x00R\x0f\x63pcBidPointList\x12w\n\x15target_cpa_point_list\x18\x08 \x01(\x0b\x32<.google.ads.googleads.v8.common.TargetCpaSimulationPointListB\x04\xe2\x41\x01\x03H\x00R\x12targetCpaPointList\x12z\n\x16target_roas_point_list\x18\t \x01(\x0b\x32=.google.ads.googleads.v8.common.TargetRoasSimulationPointListB\x04\xe2\x41\x01\x03H\x00R\x13targetRoasPointList\x12\x9c\x01\n\"target_impression_share_point_list\x18\n \x01(\x0b\x32H.google.ads.googleads.v8.common.TargetImpressionShareSimulationPointListB\x04\xe2\x41\x01\x03H\x00R\x1etargetImpressionSharePointList\x12m\n\x11\x62udget_point_list\x18\x0b \x01(\x0b\x32\x39.google.ads.googleads.v8.common.BudgetSimulationPointListB\x04\xe2\x41\x01\x03H\x00R\x0f\x62udgetPointList:\xa1\x01\xea\x41\x9d\x01\n+googleads.googleapis.com/CampaignSimulation\x12ncustomers/{customer_id}/campaignSimulations/{campaign_id}~{type}~{modification_method}~{start_date}~{end_date}B\x0c\n\npoint_listB\x84\x02\n%com.google.ads.googleads.v8.resourcesB\x17\x43\x61mpaignSimulationProtoP\x01ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v8/resources;resources\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V8.Resources\xca\x02!Google\\Ads\\GoogleAds\\V8\\Resources\xea\x02%Google::Ads::GoogleAds::V8::Resourcesb\x06proto3')



_CAMPAIGNSIMULATION = DESCRIPTOR.message_types_by_name['CampaignSimulation']
CampaignSimulation = _reflection.GeneratedProtocolMessageType('CampaignSimulation', (_message.Message,), {
  'DESCRIPTOR' : _CAMPAIGNSIMULATION,
  '__module__' : 'google.ads.googleads.v8.resources.campaign_simulation_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v8.resources.CampaignSimulation)
  })
_sym_db.RegisterMessage(CampaignSimulation)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n%com.google.ads.googleads.v8.resourcesB\027CampaignSimulationProtoP\001ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v8/resources;resources\242\002\003GAA\252\002!Google.Ads.GoogleAds.V8.Resources\312\002!Google\\Ads\\GoogleAds\\V8\\Resources\352\002%Google::Ads::GoogleAds::V8::Resources'
  _CAMPAIGNSIMULATION.fields_by_name['resource_name']._options = None
  _CAMPAIGNSIMULATION.fields_by_name['resource_name']._serialized_options = b'\342A\001\003\372A-\n+googleads.googleapis.com/CampaignSimulation'
  _CAMPAIGNSIMULATION.fields_by_name['campaign_id']._options = None
  _CAMPAIGNSIMULATION.fields_by_name['campaign_id']._serialized_options = b'\342A\001\003'
  _CAMPAIGNSIMULATION.fields_by_name['type']._options = None
  _CAMPAIGNSIMULATION.fields_by_name['type']._serialized_options = b'\342A\001\003'
  _CAMPAIGNSIMULATION.fields_by_name['modification_method']._options = None
  _CAMPAIGNSIMULATION.fields_by_name['modification_method']._serialized_options = b'\342A\001\003'
  _CAMPAIGNSIMULATION.fields_by_name['start_date']._options = None
  _CAMPAIGNSIMULATION.fields_by_name['start_date']._serialized_options = b'\342A\001\003'
  _CAMPAIGNSIMULATION.fields_by_name['end_date']._options = None
  _CAMPAIGNSIMULATION.fields_by_name['end_date']._serialized_options = b'\342A\001\003'
  _CAMPAIGNSIMULATION.fields_by_name['cpc_bid_point_list']._options = None
  _CAMPAIGNSIMULATION.fields_by_name['cpc_bid_point_list']._serialized_options = b'\342A\001\003'
  _CAMPAIGNSIMULATION.fields_by_name['target_cpa_point_list']._options = None
  _CAMPAIGNSIMULATION.fields_by_name['target_cpa_point_list']._serialized_options = b'\342A\001\003'
  _CAMPAIGNSIMULATION.fields_by_name['target_roas_point_list']._options = None
  _CAMPAIGNSIMULATION.fields_by_name['target_roas_point_list']._serialized_options = b'\342A\001\003'
  _CAMPAIGNSIMULATION.fields_by_name['target_impression_share_point_list']._options = None
  _CAMPAIGNSIMULATION.fields_by_name['target_impression_share_point_list']._serialized_options = b'\342A\001\003'
  _CAMPAIGNSIMULATION.fields_by_name['budget_point_list']._options = None
  _CAMPAIGNSIMULATION.fields_by_name['budget_point_list']._serialized_options = b'\342A\001\003'
  _CAMPAIGNSIMULATION._options = None
  _CAMPAIGNSIMULATION._serialized_options = b'\352A\235\001\n+googleads.googleapis.com/CampaignSimulation\022ncustomers/{customer_id}/campaignSimulations/{campaign_id}~{type}~{modification_method}~{start_date}~{end_date}'
  _CAMPAIGNSIMULATION._serialized_start=359
  _CAMPAIGNSIMULATION._serialized_end=1626
# @@protoc_insertion_point(module_scope)
