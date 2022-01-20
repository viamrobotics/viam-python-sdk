# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v9/services/campaign_label_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.googleads.v9.resources import campaign_label_pb2 as google_dot_ads_dot_googleads_dot_v9_dot_resources_dot_campaign__label__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import client_pb2 as google_dot_api_dot_client__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n=google/ads/googleads/v9/services/campaign_label_service.proto\x12 google.ads.googleads.v9.services\x1a\x36google/ads/googleads/v9/resources/campaign_label.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x17google/rpc/status.proto\"o\n\x17GetCampaignLabelRequest\x12T\n\rresource_name\x18\x01 \x01(\tB/\xe2\x41\x01\x02\xfa\x41(\n&googleads.googleapis.com/CampaignLabelR\x0cresourceName\"\xf2\x01\n\x1bMutateCampaignLabelsRequest\x12%\n\x0b\x63ustomer_id\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02R\ncustomerId\x12^\n\noperations\x18\x02 \x03(\x0b\x32\x38.google.ads.googleads.v9.services.CampaignLabelOperationB\x04\xe2\x41\x01\x02R\noperations\x12\'\n\x0fpartial_failure\x18\x03 \x01(\x08R\x0epartialFailure\x12#\n\rvalidate_only\x18\x04 \x01(\x08R\x0cvalidateOnly\"\x8b\x01\n\x16\x43\x61mpaignLabelOperation\x12J\n\x06\x63reate\x18\x01 \x01(\x0b\x32\x30.google.ads.googleads.v9.resources.CampaignLabelH\x00R\x06\x63reate\x12\x18\n\x06remove\x18\x02 \x01(\tH\x00R\x06removeB\x0b\n\toperation\"\xbd\x01\n\x1cMutateCampaignLabelsResponse\x12\x46\n\x15partial_failure_error\x18\x03 \x01(\x0b\x32\x12.google.rpc.StatusR\x13partialFailureError\x12U\n\x07results\x18\x02 \x03(\x0b\x32;.google.ads.googleads.v9.services.MutateCampaignLabelResultR\x07results\"@\n\x19MutateCampaignLabelResult\x12#\n\rresource_name\x18\x01 \x01(\tR\x0cresourceName2\x9a\x04\n\x14\x43\x61mpaignLabelService\x12\xc9\x01\n\x10GetCampaignLabel\x12\x39.google.ads.googleads.v9.services.GetCampaignLabelRequest\x1a\x30.google.ads.googleads.v9.resources.CampaignLabel\"H\xda\x41\rresource_name\x82\xd3\xe4\x93\x02\x32\x12\x30/v9/{resource_name=customers/*/campaignLabels/*}\x12\xee\x01\n\x14MutateCampaignLabels\x12=.google.ads.googleads.v9.services.MutateCampaignLabelsRequest\x1a>.google.ads.googleads.v9.services.MutateCampaignLabelsResponse\"W\xda\x41\x16\x63ustomer_id,operations\x82\xd3\xe4\x93\x02\x38\"3/v9/customers/{customer_id=*}/campaignLabels:mutate:\x01*\x1a\x45\xca\x41\x18googleads.googleapis.com\xd2\x41\'https://www.googleapis.com/auth/adwordsB\x80\x02\n$com.google.ads.googleads.v9.servicesB\x19\x43\x61mpaignLabelServiceProtoP\x01ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v9/services;services\xa2\x02\x03GAA\xaa\x02 Google.Ads.GoogleAds.V9.Services\xca\x02 Google\\Ads\\GoogleAds\\V9\\Services\xea\x02$Google::Ads::GoogleAds::V9::Servicesb\x06proto3')



_GETCAMPAIGNLABELREQUEST = DESCRIPTOR.message_types_by_name['GetCampaignLabelRequest']
_MUTATECAMPAIGNLABELSREQUEST = DESCRIPTOR.message_types_by_name['MutateCampaignLabelsRequest']
_CAMPAIGNLABELOPERATION = DESCRIPTOR.message_types_by_name['CampaignLabelOperation']
_MUTATECAMPAIGNLABELSRESPONSE = DESCRIPTOR.message_types_by_name['MutateCampaignLabelsResponse']
_MUTATECAMPAIGNLABELRESULT = DESCRIPTOR.message_types_by_name['MutateCampaignLabelResult']
GetCampaignLabelRequest = _reflection.GeneratedProtocolMessageType('GetCampaignLabelRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETCAMPAIGNLABELREQUEST,
  '__module__' : 'google.ads.googleads.v9.services.campaign_label_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v9.services.GetCampaignLabelRequest)
  })
_sym_db.RegisterMessage(GetCampaignLabelRequest)

MutateCampaignLabelsRequest = _reflection.GeneratedProtocolMessageType('MutateCampaignLabelsRequest', (_message.Message,), {
  'DESCRIPTOR' : _MUTATECAMPAIGNLABELSREQUEST,
  '__module__' : 'google.ads.googleads.v9.services.campaign_label_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v9.services.MutateCampaignLabelsRequest)
  })
_sym_db.RegisterMessage(MutateCampaignLabelsRequest)

CampaignLabelOperation = _reflection.GeneratedProtocolMessageType('CampaignLabelOperation', (_message.Message,), {
  'DESCRIPTOR' : _CAMPAIGNLABELOPERATION,
  '__module__' : 'google.ads.googleads.v9.services.campaign_label_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v9.services.CampaignLabelOperation)
  })
_sym_db.RegisterMessage(CampaignLabelOperation)

MutateCampaignLabelsResponse = _reflection.GeneratedProtocolMessageType('MutateCampaignLabelsResponse', (_message.Message,), {
  'DESCRIPTOR' : _MUTATECAMPAIGNLABELSRESPONSE,
  '__module__' : 'google.ads.googleads.v9.services.campaign_label_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v9.services.MutateCampaignLabelsResponse)
  })
_sym_db.RegisterMessage(MutateCampaignLabelsResponse)

MutateCampaignLabelResult = _reflection.GeneratedProtocolMessageType('MutateCampaignLabelResult', (_message.Message,), {
  'DESCRIPTOR' : _MUTATECAMPAIGNLABELRESULT,
  '__module__' : 'google.ads.googleads.v9.services.campaign_label_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v9.services.MutateCampaignLabelResult)
  })
_sym_db.RegisterMessage(MutateCampaignLabelResult)

_CAMPAIGNLABELSERVICE = DESCRIPTOR.services_by_name['CampaignLabelService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n$com.google.ads.googleads.v9.servicesB\031CampaignLabelServiceProtoP\001ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v9/services;services\242\002\003GAA\252\002 Google.Ads.GoogleAds.V9.Services\312\002 Google\\Ads\\GoogleAds\\V9\\Services\352\002$Google::Ads::GoogleAds::V9::Services'
  _GETCAMPAIGNLABELREQUEST.fields_by_name['resource_name']._options = None
  _GETCAMPAIGNLABELREQUEST.fields_by_name['resource_name']._serialized_options = b'\342A\001\002\372A(\n&googleads.googleapis.com/CampaignLabel'
  _MUTATECAMPAIGNLABELSREQUEST.fields_by_name['customer_id']._options = None
  _MUTATECAMPAIGNLABELSREQUEST.fields_by_name['customer_id']._serialized_options = b'\342A\001\002'
  _MUTATECAMPAIGNLABELSREQUEST.fields_by_name['operations']._options = None
  _MUTATECAMPAIGNLABELSREQUEST.fields_by_name['operations']._serialized_options = b'\342A\001\002'
  _CAMPAIGNLABELSERVICE._options = None
  _CAMPAIGNLABELSERVICE._serialized_options = b'\312A\030googleads.googleapis.com\322A\'https://www.googleapis.com/auth/adwords'
  _CAMPAIGNLABELSERVICE.methods_by_name['GetCampaignLabel']._options = None
  _CAMPAIGNLABELSERVICE.methods_by_name['GetCampaignLabel']._serialized_options = b'\332A\rresource_name\202\323\344\223\0022\0220/v9/{resource_name=customers/*/campaignLabels/*}'
  _CAMPAIGNLABELSERVICE.methods_by_name['MutateCampaignLabels']._options = None
  _CAMPAIGNLABELSERVICE.methods_by_name['MutateCampaignLabels']._serialized_options = b'\332A\026customer_id,operations\202\323\344\223\0028\"3/v9/customers/{customer_id=*}/campaignLabels:mutate:\001*'
  _GETCAMPAIGNLABELREQUEST._serialized_start=295
  _GETCAMPAIGNLABELREQUEST._serialized_end=406
  _MUTATECAMPAIGNLABELSREQUEST._serialized_start=409
  _MUTATECAMPAIGNLABELSREQUEST._serialized_end=651
  _CAMPAIGNLABELOPERATION._serialized_start=654
  _CAMPAIGNLABELOPERATION._serialized_end=793
  _MUTATECAMPAIGNLABELSRESPONSE._serialized_start=796
  _MUTATECAMPAIGNLABELSRESPONSE._serialized_end=985
  _MUTATECAMPAIGNLABELRESULT._serialized_start=987
  _MUTATECAMPAIGNLABELRESULT._serialized_end=1051
  _CAMPAIGNLABELSERVICE._serialized_start=1054
  _CAMPAIGNLABELSERVICE._serialized_end=1592
# @@protoc_insertion_point(module_scope)
