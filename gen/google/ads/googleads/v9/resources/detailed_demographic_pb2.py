# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v9/resources/detailed_demographic.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.googleads.v9.common import criterion_category_availability_pb2 as google_dot_ads_dot_googleads_dot_v9_dot_common_dot_criterion__category__availability__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n<google/ads/googleads/v9/resources/detailed_demographic.proto\x12!google.ads.googleads.v9.resources\x1a\x44google/ads/googleads/v9/common/criterion_category_availability.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1cgoogle/api/annotations.proto\"\x86\x04\n\x13\x44\x65tailedDemographic\x12Z\n\rresource_name\x18\x01 \x01(\tB5\xe2\x41\x01\x03\xfa\x41.\n,googleads.googleapis.com/DetailedDemographicR\x0cresourceName\x12\x14\n\x02id\x18\x02 \x01(\x03\x42\x04\xe2\x41\x01\x03R\x02id\x12\x18\n\x04name\x18\x03 \x01(\tB\x04\xe2\x41\x01\x03R\x04name\x12M\n\x06parent\x18\x04 \x01(\tB5\xe2\x41\x01\x03\xfa\x41.\n,googleads.googleapis.com/DetailedDemographicR\x06parent\x12,\n\x0flaunched_to_all\x18\x05 \x01(\x08\x42\x04\xe2\x41\x01\x03R\rlaunchedToAll\x12k\n\x0e\x61vailabilities\x18\x06 \x03(\x0b\x32=.google.ads.googleads.v9.common.CriterionCategoryAvailabilityB\x04\xe2\x41\x01\x03R\x0e\x61vailabilities:y\xea\x41v\n,googleads.googleapis.com/DetailedDemographic\x12\x46\x63ustomers/{customer_id}/detailedDemographics/{detailed_demographic_id}B\x85\x02\n%com.google.ads.googleads.v9.resourcesB\x18\x44\x65tailedDemographicProtoP\x01ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v9/resources;resources\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V9.Resources\xca\x02!Google\\Ads\\GoogleAds\\V9\\Resources\xea\x02%Google::Ads::GoogleAds::V9::Resourcesb\x06proto3')



_DETAILEDDEMOGRAPHIC = DESCRIPTOR.message_types_by_name['DetailedDemographic']
DetailedDemographic = _reflection.GeneratedProtocolMessageType('DetailedDemographic', (_message.Message,), {
  'DESCRIPTOR' : _DETAILEDDEMOGRAPHIC,
  '__module__' : 'google.ads.googleads.v9.resources.detailed_demographic_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v9.resources.DetailedDemographic)
  })
_sym_db.RegisterMessage(DetailedDemographic)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n%com.google.ads.googleads.v9.resourcesB\030DetailedDemographicProtoP\001ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v9/resources;resources\242\002\003GAA\252\002!Google.Ads.GoogleAds.V9.Resources\312\002!Google\\Ads\\GoogleAds\\V9\\Resources\352\002%Google::Ads::GoogleAds::V9::Resources'
  _DETAILEDDEMOGRAPHIC.fields_by_name['resource_name']._options = None
  _DETAILEDDEMOGRAPHIC.fields_by_name['resource_name']._serialized_options = b'\342A\001\003\372A.\n,googleads.googleapis.com/DetailedDemographic'
  _DETAILEDDEMOGRAPHIC.fields_by_name['id']._options = None
  _DETAILEDDEMOGRAPHIC.fields_by_name['id']._serialized_options = b'\342A\001\003'
  _DETAILEDDEMOGRAPHIC.fields_by_name['name']._options = None
  _DETAILEDDEMOGRAPHIC.fields_by_name['name']._serialized_options = b'\342A\001\003'
  _DETAILEDDEMOGRAPHIC.fields_by_name['parent']._options = None
  _DETAILEDDEMOGRAPHIC.fields_by_name['parent']._serialized_options = b'\342A\001\003\372A.\n,googleads.googleapis.com/DetailedDemographic'
  _DETAILEDDEMOGRAPHIC.fields_by_name['launched_to_all']._options = None
  _DETAILEDDEMOGRAPHIC.fields_by_name['launched_to_all']._serialized_options = b'\342A\001\003'
  _DETAILEDDEMOGRAPHIC.fields_by_name['availabilities']._options = None
  _DETAILEDDEMOGRAPHIC.fields_by_name['availabilities']._serialized_options = b'\342A\001\003'
  _DETAILEDDEMOGRAPHIC._options = None
  _DETAILEDDEMOGRAPHIC._serialized_options = b'\352Av\n,googleads.googleapis.com/DetailedDemographic\022Fcustomers/{customer_id}/detailedDemographics/{detailed_demographic_id}'
  _DETAILEDDEMOGRAPHIC._serialized_start=260
  _DETAILEDDEMOGRAPHIC._serialized_end=778
# @@protoc_insertion_point(module_scope)
