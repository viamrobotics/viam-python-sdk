# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v7/resources/ad_group_criterion_simulation.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.googleads.v7.common import simulation_pb2 as google_dot_ads_dot_googleads_dot_v7_dot_common_dot_simulation__pb2
from google.ads.googleads.v7.enums import simulation_modification_method_pb2 as google_dot_ads_dot_googleads_dot_v7_dot_enums_dot_simulation__modification__method__pb2
from google.ads.googleads.v7.enums import simulation_type_pb2 as google_dot_ads_dot_googleads_dot_v7_dot_enums_dot_simulation__type__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nEgoogle/ads/googleads/v7/resources/ad_group_criterion_simulation.proto\x12!google.ads.googleads.v7.resources\x1a/google/ads/googleads/v7/common/simulation.proto\x1a\x42google/ads/googleads/v7/enums/simulation_modification_method.proto\x1a\x33google/ads/googleads/v7/enums/simulation_type.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1cgoogle/api/annotations.proto\"\xa0\x08\n\x1a\x41\x64GroupCriterionSimulation\x12\x61\n\rresource_name\x18\x01 \x01(\tB<\xe2\x41\x01\x03\xfa\x41\x35\n3googleads.googleapis.com/AdGroupCriterionSimulationR\x0cresourceName\x12)\n\x0b\x61\x64_group_id\x18\t \x01(\x03\x42\x04\xe2\x41\x01\x03H\x01R\tadGroupId\x88\x01\x01\x12,\n\x0c\x63riterion_id\x18\n \x01(\x03\x42\x04\xe2\x41\x01\x03H\x02R\x0b\x63riterionId\x88\x01\x01\x12Z\n\x04type\x18\x04 \x01(\x0e\x32@.google.ads.googleads.v7.enums.SimulationTypeEnum.SimulationTypeB\x04\xe2\x41\x01\x03R\x04type\x12\x93\x01\n\x13modification_method\x18\x05 \x01(\x0e\x32\\.google.ads.googleads.v7.enums.SimulationModificationMethodEnum.SimulationModificationMethodB\x04\xe2\x41\x01\x03R\x12modificationMethod\x12(\n\nstart_date\x18\x0b \x01(\tB\x04\xe2\x41\x01\x03H\x03R\tstartDate\x88\x01\x01\x12$\n\x08\x65nd_date\x18\x0c \x01(\tB\x04\xe2\x41\x01\x03H\x04R\x07\x65ndDate\x88\x01\x01\x12n\n\x12\x63pc_bid_point_list\x18\x08 \x01(\x0b\x32\x39.google.ads.googleads.v7.common.CpcBidSimulationPointListB\x04\xe2\x41\x01\x03H\x00R\x0f\x63pcBidPointList\x12\x84\x01\n\x1apercent_cpc_bid_point_list\x18\r \x01(\x0b\x32@.google.ads.googleads.v7.common.PercentCpcBidSimulationPointListB\x04\xe2\x41\x01\x03H\x00R\x16percentCpcBidPointList:\xc1\x01\xea\x41\xbd\x01\n3googleads.googleapis.com/AdGroupCriterionSimulation\x12\x85\x01\x63ustomers/{customer_id}/adGroupCriterionSimulations/{ad_group_id}~{criterion_id}~{type}~{modification_method}~{start_date}~{end_date}B\x0c\n\npoint_listB\x0e\n\x0c_ad_group_idB\x0f\n\r_criterion_idB\r\n\x0b_start_dateB\x0b\n\t_end_dateB\x8c\x02\n%com.google.ads.googleads.v7.resourcesB\x1f\x41\x64GroupCriterionSimulationProtoP\x01ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v7/resources;resources\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V7.Resources\xca\x02!Google\\Ads\\GoogleAds\\V7\\Resources\xea\x02%Google::Ads::GoogleAds::V7::Resourcesb\x06proto3')



_ADGROUPCRITERIONSIMULATION = DESCRIPTOR.message_types_by_name['AdGroupCriterionSimulation']
AdGroupCriterionSimulation = _reflection.GeneratedProtocolMessageType('AdGroupCriterionSimulation', (_message.Message,), {
  'DESCRIPTOR' : _ADGROUPCRITERIONSIMULATION,
  '__module__' : 'google.ads.googleads.v7.resources.ad_group_criterion_simulation_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v7.resources.AdGroupCriterionSimulation)
  })
_sym_db.RegisterMessage(AdGroupCriterionSimulation)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n%com.google.ads.googleads.v7.resourcesB\037AdGroupCriterionSimulationProtoP\001ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v7/resources;resources\242\002\003GAA\252\002!Google.Ads.GoogleAds.V7.Resources\312\002!Google\\Ads\\GoogleAds\\V7\\Resources\352\002%Google::Ads::GoogleAds::V7::Resources'
  _ADGROUPCRITERIONSIMULATION.fields_by_name['resource_name']._options = None
  _ADGROUPCRITERIONSIMULATION.fields_by_name['resource_name']._serialized_options = b'\342A\001\003\372A5\n3googleads.googleapis.com/AdGroupCriterionSimulation'
  _ADGROUPCRITERIONSIMULATION.fields_by_name['ad_group_id']._options = None
  _ADGROUPCRITERIONSIMULATION.fields_by_name['ad_group_id']._serialized_options = b'\342A\001\003'
  _ADGROUPCRITERIONSIMULATION.fields_by_name['criterion_id']._options = None
  _ADGROUPCRITERIONSIMULATION.fields_by_name['criterion_id']._serialized_options = b'\342A\001\003'
  _ADGROUPCRITERIONSIMULATION.fields_by_name['type']._options = None
  _ADGROUPCRITERIONSIMULATION.fields_by_name['type']._serialized_options = b'\342A\001\003'
  _ADGROUPCRITERIONSIMULATION.fields_by_name['modification_method']._options = None
  _ADGROUPCRITERIONSIMULATION.fields_by_name['modification_method']._serialized_options = b'\342A\001\003'
  _ADGROUPCRITERIONSIMULATION.fields_by_name['start_date']._options = None
  _ADGROUPCRITERIONSIMULATION.fields_by_name['start_date']._serialized_options = b'\342A\001\003'
  _ADGROUPCRITERIONSIMULATION.fields_by_name['end_date']._options = None
  _ADGROUPCRITERIONSIMULATION.fields_by_name['end_date']._serialized_options = b'\342A\001\003'
  _ADGROUPCRITERIONSIMULATION.fields_by_name['cpc_bid_point_list']._options = None
  _ADGROUPCRITERIONSIMULATION.fields_by_name['cpc_bid_point_list']._serialized_options = b'\342A\001\003'
  _ADGROUPCRITERIONSIMULATION.fields_by_name['percent_cpc_bid_point_list']._options = None
  _ADGROUPCRITERIONSIMULATION.fields_by_name['percent_cpc_bid_point_list']._serialized_options = b'\342A\001\003'
  _ADGROUPCRITERIONSIMULATION._options = None
  _ADGROUPCRITERIONSIMULATION._serialized_options = b'\352A\275\001\n3googleads.googleapis.com/AdGroupCriterionSimulation\022\205\001customers/{customer_id}/adGroupCriterionSimulations/{ad_group_id}~{criterion_id}~{type}~{modification_method}~{start_date}~{end_date}'
  _ADGROUPCRITERIONSIMULATION._serialized_start=369
  _ADGROUPCRITERIONSIMULATION._serialized_end=1425
# @@protoc_insertion_point(module_scope)
