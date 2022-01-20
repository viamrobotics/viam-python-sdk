# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v9/services/operating_system_version_constant_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.googleads.v9.resources import operating_system_version_constant_pb2 as google_dot_ads_dot_googleads_dot_v9_dot_resources_dot_operating__system__version__constant__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import client_pb2 as google_dot_api_dot_client__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nPgoogle/ads/googleads/v9/services/operating_system_version_constant_service.proto\x12 google.ads.googleads.v9.services\x1aIgoogle/ads/googleads/v9/resources/operating_system_version_constant.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\"\x91\x01\n(GetOperatingSystemVersionConstantRequest\x12\x65\n\rresource_name\x18\x01 \x01(\tB@\xe2\x41\x01\x02\xfa\x41\x39\n7googleads.googleapis.com/OperatingSystemVersionConstantR\x0cresourceName2\xf2\x02\n%OperatingSystemVersionConstantService\x12\x81\x02\n!GetOperatingSystemVersionConstant\x12J.google.ads.googleads.v9.services.GetOperatingSystemVersionConstantRequest\x1a\x41.google.ads.googleads.v9.resources.OperatingSystemVersionConstant\"M\xda\x41\rresource_name\x82\xd3\xe4\x93\x02\x37\x12\x35/v9/{resource_name=operatingSystemVersionConstants/*}\x1a\x45\xca\x41\x18googleads.googleapis.com\xd2\x41\'https://www.googleapis.com/auth/adwordsB\x91\x02\n$com.google.ads.googleads.v9.servicesB*OperatingSystemVersionConstantServiceProtoP\x01ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v9/services;services\xa2\x02\x03GAA\xaa\x02 Google.Ads.GoogleAds.V9.Services\xca\x02 Google\\Ads\\GoogleAds\\V9\\Services\xea\x02$Google::Ads::GoogleAds::V9::Servicesb\x06proto3')



_GETOPERATINGSYSTEMVERSIONCONSTANTREQUEST = DESCRIPTOR.message_types_by_name['GetOperatingSystemVersionConstantRequest']
GetOperatingSystemVersionConstantRequest = _reflection.GeneratedProtocolMessageType('GetOperatingSystemVersionConstantRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETOPERATINGSYSTEMVERSIONCONSTANTREQUEST,
  '__module__' : 'google.ads.googleads.v9.services.operating_system_version_constant_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v9.services.GetOperatingSystemVersionConstantRequest)
  })
_sym_db.RegisterMessage(GetOperatingSystemVersionConstantRequest)

_OPERATINGSYSTEMVERSIONCONSTANTSERVICE = DESCRIPTOR.services_by_name['OperatingSystemVersionConstantService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n$com.google.ads.googleads.v9.servicesB*OperatingSystemVersionConstantServiceProtoP\001ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v9/services;services\242\002\003GAA\252\002 Google.Ads.GoogleAds.V9.Services\312\002 Google\\Ads\\GoogleAds\\V9\\Services\352\002$Google::Ads::GoogleAds::V9::Services'
  _GETOPERATINGSYSTEMVERSIONCONSTANTREQUEST.fields_by_name['resource_name']._options = None
  _GETOPERATINGSYSTEMVERSIONCONSTANTREQUEST.fields_by_name['resource_name']._serialized_options = b'\342A\001\002\372A9\n7googleads.googleapis.com/OperatingSystemVersionConstant'
  _OPERATINGSYSTEMVERSIONCONSTANTSERVICE._options = None
  _OPERATINGSYSTEMVERSIONCONSTANTSERVICE._serialized_options = b'\312A\030googleads.googleapis.com\322A\'https://www.googleapis.com/auth/adwords'
  _OPERATINGSYSTEMVERSIONCONSTANTSERVICE.methods_by_name['GetOperatingSystemVersionConstant']._options = None
  _OPERATINGSYSTEMVERSIONCONSTANTSERVICE.methods_by_name['GetOperatingSystemVersionConstant']._serialized_options = b'\332A\rresource_name\202\323\344\223\0027\0225/v9/{resource_name=operatingSystemVersionConstants/*}'
  _GETOPERATINGSYSTEMVERSIONCONSTANTREQUEST._serialized_start=309
  _GETOPERATINGSYSTEMVERSIONCONSTANTREQUEST._serialized_end=454
  _OPERATINGSYSTEMVERSIONCONSTANTSERVICE._serialized_start=457
  _OPERATINGSYSTEMVERSIONCONSTANTSERVICE._serialized_end=827
# @@protoc_insertion_point(module_scope)
