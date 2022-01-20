# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v8/services/gender_view_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.googleads.v8.resources import gender_view_pb2 as google_dot_ads_dot_googleads_dot_v8_dot_resources_dot_gender__view__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import client_pb2 as google_dot_api_dot_client__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n:google/ads/googleads/v8/services/gender_view_service.proto\x12 google.ads.googleads.v8.services\x1a\x33google/ads/googleads/v8/resources/gender_view.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\"i\n\x14GetGenderViewRequest\x12Q\n\rresource_name\x18\x01 \x01(\tB,\xe2\x41\x01\x02\xfa\x41%\n#googleads.googleapis.com/GenderViewR\x0cresourceName2\x9a\x02\n\x11GenderViewService\x12\xbd\x01\n\rGetGenderView\x12\x36.google.ads.googleads.v8.services.GetGenderViewRequest\x1a-.google.ads.googleads.v8.resources.GenderView\"E\xda\x41\rresource_name\x82\xd3\xe4\x93\x02/\x12-/v8/{resource_name=customers/*/genderViews/*}\x1a\x45\xca\x41\x18googleads.googleapis.com\xd2\x41\'https://www.googleapis.com/auth/adwordsB\xfd\x01\n$com.google.ads.googleads.v8.servicesB\x16GenderViewServiceProtoP\x01ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v8/services;services\xa2\x02\x03GAA\xaa\x02 Google.Ads.GoogleAds.V8.Services\xca\x02 Google\\Ads\\GoogleAds\\V8\\Services\xea\x02$Google::Ads::GoogleAds::V8::Servicesb\x06proto3')



_GETGENDERVIEWREQUEST = DESCRIPTOR.message_types_by_name['GetGenderViewRequest']
GetGenderViewRequest = _reflection.GeneratedProtocolMessageType('GetGenderViewRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETGENDERVIEWREQUEST,
  '__module__' : 'google.ads.googleads.v8.services.gender_view_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v8.services.GetGenderViewRequest)
  })
_sym_db.RegisterMessage(GetGenderViewRequest)

_GENDERVIEWSERVICE = DESCRIPTOR.services_by_name['GenderViewService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n$com.google.ads.googleads.v8.servicesB\026GenderViewServiceProtoP\001ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v8/services;services\242\002\003GAA\252\002 Google.Ads.GoogleAds.V8.Services\312\002 Google\\Ads\\GoogleAds\\V8\\Services\352\002$Google::Ads::GoogleAds::V8::Services'
  _GETGENDERVIEWREQUEST.fields_by_name['resource_name']._options = None
  _GETGENDERVIEWREQUEST.fields_by_name['resource_name']._serialized_options = b'\342A\001\002\372A%\n#googleads.googleapis.com/GenderView'
  _GENDERVIEWSERVICE._options = None
  _GENDERVIEWSERVICE._serialized_options = b'\312A\030googleads.googleapis.com\322A\'https://www.googleapis.com/auth/adwords'
  _GENDERVIEWSERVICE.methods_by_name['GetGenderView']._options = None
  _GENDERVIEWSERVICE.methods_by_name['GetGenderView']._serialized_options = b'\332A\rresource_name\202\323\344\223\002/\022-/v8/{resource_name=customers/*/genderViews/*}'
  _GETGENDERVIEWREQUEST._serialized_start=264
  _GETGENDERVIEWREQUEST._serialized_end=369
  _GENDERVIEWSERVICE._serialized_start=372
  _GENDERVIEWSERVICE._serialized_end=654
# @@protoc_insertion_point(module_scope)
