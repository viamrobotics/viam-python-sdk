# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v8/resources/campaign_bid_modifier.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.googleads.v8.common import criteria_pb2 as google_dot_ads_dot_googleads_dot_v8_dot_common_dot_criteria__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n=google/ads/googleads/v8/resources/campaign_bid_modifier.proto\x12!google.ads.googleads.v8.resources\x1a-google/ads/googleads/v8/common/criteria.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1cgoogle/api/annotations.proto\"\xb6\x04\n\x13\x43\x61mpaignBidModifier\x12Z\n\rresource_name\x18\x01 \x01(\tB5\xe2\x41\x01\x05\xfa\x41.\n,googleads.googleapis.com/CampaignBidModifierR\x0cresourceName\x12K\n\x08\x63\x61mpaign\x18\x06 \x01(\tB*\xe2\x41\x01\x03\xfa\x41#\n!googleads.googleapis.com/CampaignH\x01R\x08\x63\x61mpaign\x88\x01\x01\x12,\n\x0c\x63riterion_id\x18\x07 \x01(\x03\x42\x04\xe2\x41\x01\x03H\x02R\x0b\x63riterionId\x88\x01\x01\x12&\n\x0c\x62id_modifier\x18\x08 \x01(\x01H\x03R\x0b\x62idModifier\x88\x01\x01\x12\x66\n\x10interaction_type\x18\x05 \x01(\x0b\x32\x33.google.ads.googleads.v8.common.InteractionTypeInfoB\x04\xe2\x41\x01\x05H\x00R\x0finteractionType:|\xea\x41y\n,googleads.googleapis.com/CampaignBidModifier\x12Icustomers/{customer_id}/campaignBidModifiers/{campaign_id}~{criterion_id}B\x0b\n\tcriterionB\x0b\n\t_campaignB\x0f\n\r_criterion_idB\x0f\n\r_bid_modifierB\x85\x02\n%com.google.ads.googleads.v8.resourcesB\x18\x43\x61mpaignBidModifierProtoP\x01ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v8/resources;resources\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V8.Resources\xca\x02!Google\\Ads\\GoogleAds\\V8\\Resources\xea\x02%Google::Ads::GoogleAds::V8::Resourcesb\x06proto3')



_CAMPAIGNBIDMODIFIER = DESCRIPTOR.message_types_by_name['CampaignBidModifier']
CampaignBidModifier = _reflection.GeneratedProtocolMessageType('CampaignBidModifier', (_message.Message,), {
  'DESCRIPTOR' : _CAMPAIGNBIDMODIFIER,
  '__module__' : 'google.ads.googleads.v8.resources.campaign_bid_modifier_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v8.resources.CampaignBidModifier)
  })
_sym_db.RegisterMessage(CampaignBidModifier)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n%com.google.ads.googleads.v8.resourcesB\030CampaignBidModifierProtoP\001ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v8/resources;resources\242\002\003GAA\252\002!Google.Ads.GoogleAds.V8.Resources\312\002!Google\\Ads\\GoogleAds\\V8\\Resources\352\002%Google::Ads::GoogleAds::V8::Resources'
  _CAMPAIGNBIDMODIFIER.fields_by_name['resource_name']._options = None
  _CAMPAIGNBIDMODIFIER.fields_by_name['resource_name']._serialized_options = b'\342A\001\005\372A.\n,googleads.googleapis.com/CampaignBidModifier'
  _CAMPAIGNBIDMODIFIER.fields_by_name['campaign']._options = None
  _CAMPAIGNBIDMODIFIER.fields_by_name['campaign']._serialized_options = b'\342A\001\003\372A#\n!googleads.googleapis.com/Campaign'
  _CAMPAIGNBIDMODIFIER.fields_by_name['criterion_id']._options = None
  _CAMPAIGNBIDMODIFIER.fields_by_name['criterion_id']._serialized_options = b'\342A\001\003'
  _CAMPAIGNBIDMODIFIER.fields_by_name['interaction_type']._options = None
  _CAMPAIGNBIDMODIFIER.fields_by_name['interaction_type']._serialized_options = b'\342A\001\005'
  _CAMPAIGNBIDMODIFIER._options = None
  _CAMPAIGNBIDMODIFIER._serialized_options = b'\352Ay\n,googleads.googleapis.com/CampaignBidModifier\022Icustomers/{customer_id}/campaignBidModifiers/{campaign_id}~{criterion_id}'
  _CAMPAIGNBIDMODIFIER._serialized_start=238
  _CAMPAIGNBIDMODIFIER._serialized_end=804
# @@protoc_insertion_point(module_scope)
