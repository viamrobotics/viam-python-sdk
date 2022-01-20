# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v7/services/ad_group_label_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.googleads.v7.resources import ad_group_label_pb2 as google_dot_ads_dot_googleads_dot_v7_dot_resources_dot_ad__group__label__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import client_pb2 as google_dot_api_dot_client__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n=google/ads/googleads/v7/services/ad_group_label_service.proto\x12 google.ads.googleads.v7.services\x1a\x36google/ads/googleads/v7/resources/ad_group_label.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x17google/rpc/status.proto\"m\n\x16GetAdGroupLabelRequest\x12S\n\rresource_name\x18\x01 \x01(\tB.\xe2\x41\x01\x02\xfa\x41\'\n%googleads.googleapis.com/AdGroupLabelR\x0cresourceName\"\xf0\x01\n\x1aMutateAdGroupLabelsRequest\x12%\n\x0b\x63ustomer_id\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02R\ncustomerId\x12]\n\noperations\x18\x02 \x03(\x0b\x32\x37.google.ads.googleads.v7.services.AdGroupLabelOperationB\x04\xe2\x41\x01\x02R\noperations\x12\'\n\x0fpartial_failure\x18\x03 \x01(\x08R\x0epartialFailure\x12#\n\rvalidate_only\x18\x04 \x01(\x08R\x0cvalidateOnly\"\x89\x01\n\x15\x41\x64GroupLabelOperation\x12I\n\x06\x63reate\x18\x01 \x01(\x0b\x32/.google.ads.googleads.v7.resources.AdGroupLabelH\x00R\x06\x63reate\x12\x18\n\x06remove\x18\x02 \x01(\tH\x00R\x06removeB\x0b\n\toperation\"\xbb\x01\n\x1bMutateAdGroupLabelsResponse\x12\x46\n\x15partial_failure_error\x18\x03 \x01(\x0b\x32\x12.google.rpc.StatusR\x13partialFailureError\x12T\n\x07results\x18\x02 \x03(\x0b\x32:.google.ads.googleads.v7.services.MutateAdGroupLabelResultR\x07results\"?\n\x18MutateAdGroupLabelResult\x12#\n\rresource_name\x18\x01 \x01(\tR\x0cresourceName2\x91\x04\n\x13\x41\x64GroupLabelService\x12\xc5\x01\n\x0fGetAdGroupLabel\x12\x38.google.ads.googleads.v7.services.GetAdGroupLabelRequest\x1a/.google.ads.googleads.v7.resources.AdGroupLabel\"G\xda\x41\rresource_name\x82\xd3\xe4\x93\x02\x31\x12//v7/{resource_name=customers/*/adGroupLabels/*}\x12\xea\x01\n\x13MutateAdGroupLabels\x12<.google.ads.googleads.v7.services.MutateAdGroupLabelsRequest\x1a=.google.ads.googleads.v7.services.MutateAdGroupLabelsResponse\"V\xda\x41\x16\x63ustomer_id,operations\x82\xd3\xe4\x93\x02\x37\"2/v7/customers/{customer_id=*}/adGroupLabels:mutate:\x01*\x1a\x45\xca\x41\x18googleads.googleapis.com\xd2\x41\'https://www.googleapis.com/auth/adwordsB\xff\x01\n$com.google.ads.googleads.v7.servicesB\x18\x41\x64GroupLabelServiceProtoP\x01ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v7/services;services\xa2\x02\x03GAA\xaa\x02 Google.Ads.GoogleAds.V7.Services\xca\x02 Google\\Ads\\GoogleAds\\V7\\Services\xea\x02$Google::Ads::GoogleAds::V7::Servicesb\x06proto3')



_GETADGROUPLABELREQUEST = DESCRIPTOR.message_types_by_name['GetAdGroupLabelRequest']
_MUTATEADGROUPLABELSREQUEST = DESCRIPTOR.message_types_by_name['MutateAdGroupLabelsRequest']
_ADGROUPLABELOPERATION = DESCRIPTOR.message_types_by_name['AdGroupLabelOperation']
_MUTATEADGROUPLABELSRESPONSE = DESCRIPTOR.message_types_by_name['MutateAdGroupLabelsResponse']
_MUTATEADGROUPLABELRESULT = DESCRIPTOR.message_types_by_name['MutateAdGroupLabelResult']
GetAdGroupLabelRequest = _reflection.GeneratedProtocolMessageType('GetAdGroupLabelRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETADGROUPLABELREQUEST,
  '__module__' : 'google.ads.googleads.v7.services.ad_group_label_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v7.services.GetAdGroupLabelRequest)
  })
_sym_db.RegisterMessage(GetAdGroupLabelRequest)

MutateAdGroupLabelsRequest = _reflection.GeneratedProtocolMessageType('MutateAdGroupLabelsRequest', (_message.Message,), {
  'DESCRIPTOR' : _MUTATEADGROUPLABELSREQUEST,
  '__module__' : 'google.ads.googleads.v7.services.ad_group_label_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v7.services.MutateAdGroupLabelsRequest)
  })
_sym_db.RegisterMessage(MutateAdGroupLabelsRequest)

AdGroupLabelOperation = _reflection.GeneratedProtocolMessageType('AdGroupLabelOperation', (_message.Message,), {
  'DESCRIPTOR' : _ADGROUPLABELOPERATION,
  '__module__' : 'google.ads.googleads.v7.services.ad_group_label_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v7.services.AdGroupLabelOperation)
  })
_sym_db.RegisterMessage(AdGroupLabelOperation)

MutateAdGroupLabelsResponse = _reflection.GeneratedProtocolMessageType('MutateAdGroupLabelsResponse', (_message.Message,), {
  'DESCRIPTOR' : _MUTATEADGROUPLABELSRESPONSE,
  '__module__' : 'google.ads.googleads.v7.services.ad_group_label_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v7.services.MutateAdGroupLabelsResponse)
  })
_sym_db.RegisterMessage(MutateAdGroupLabelsResponse)

MutateAdGroupLabelResult = _reflection.GeneratedProtocolMessageType('MutateAdGroupLabelResult', (_message.Message,), {
  'DESCRIPTOR' : _MUTATEADGROUPLABELRESULT,
  '__module__' : 'google.ads.googleads.v7.services.ad_group_label_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v7.services.MutateAdGroupLabelResult)
  })
_sym_db.RegisterMessage(MutateAdGroupLabelResult)

_ADGROUPLABELSERVICE = DESCRIPTOR.services_by_name['AdGroupLabelService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n$com.google.ads.googleads.v7.servicesB\030AdGroupLabelServiceProtoP\001ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v7/services;services\242\002\003GAA\252\002 Google.Ads.GoogleAds.V7.Services\312\002 Google\\Ads\\GoogleAds\\V7\\Services\352\002$Google::Ads::GoogleAds::V7::Services'
  _GETADGROUPLABELREQUEST.fields_by_name['resource_name']._options = None
  _GETADGROUPLABELREQUEST.fields_by_name['resource_name']._serialized_options = b'\342A\001\002\372A\'\n%googleads.googleapis.com/AdGroupLabel'
  _MUTATEADGROUPLABELSREQUEST.fields_by_name['customer_id']._options = None
  _MUTATEADGROUPLABELSREQUEST.fields_by_name['customer_id']._serialized_options = b'\342A\001\002'
  _MUTATEADGROUPLABELSREQUEST.fields_by_name['operations']._options = None
  _MUTATEADGROUPLABELSREQUEST.fields_by_name['operations']._serialized_options = b'\342A\001\002'
  _ADGROUPLABELSERVICE._options = None
  _ADGROUPLABELSERVICE._serialized_options = b'\312A\030googleads.googleapis.com\322A\'https://www.googleapis.com/auth/adwords'
  _ADGROUPLABELSERVICE.methods_by_name['GetAdGroupLabel']._options = None
  _ADGROUPLABELSERVICE.methods_by_name['GetAdGroupLabel']._serialized_options = b'\332A\rresource_name\202\323\344\223\0021\022//v7/{resource_name=customers/*/adGroupLabels/*}'
  _ADGROUPLABELSERVICE.methods_by_name['MutateAdGroupLabels']._options = None
  _ADGROUPLABELSERVICE.methods_by_name['MutateAdGroupLabels']._serialized_options = b'\332A\026customer_id,operations\202\323\344\223\0027\"2/v7/customers/{customer_id=*}/adGroupLabels:mutate:\001*'
  _GETADGROUPLABELREQUEST._serialized_start=295
  _GETADGROUPLABELREQUEST._serialized_end=404
  _MUTATEADGROUPLABELSREQUEST._serialized_start=407
  _MUTATEADGROUPLABELSREQUEST._serialized_end=647
  _ADGROUPLABELOPERATION._serialized_start=650
  _ADGROUPLABELOPERATION._serialized_end=787
  _MUTATEADGROUPLABELSRESPONSE._serialized_start=790
  _MUTATEADGROUPLABELSRESPONSE._serialized_end=977
  _MUTATEADGROUPLABELRESULT._serialized_start=979
  _MUTATEADGROUPLABELRESULT._serialized_end=1042
  _ADGROUPLABELSERVICE._serialized_start=1045
  _ADGROUPLABELSERVICE._serialized_end=1574
# @@protoc_insertion_point(module_scope)
