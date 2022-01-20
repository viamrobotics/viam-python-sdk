# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v7/services/campaign_bid_modifier_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.googleads.v7.enums import response_content_type_pb2 as google_dot_ads_dot_googleads_dot_v7_dot_enums_dot_response__content__type__pb2
from google.ads.googleads.v7.resources import campaign_bid_modifier_pb2 as google_dot_ads_dot_googleads_dot_v7_dot_resources_dot_campaign__bid__modifier__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import client_pb2 as google_dot_api_dot_client__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nDgoogle/ads/googleads/v7/services/campaign_bid_modifier_service.proto\x12 google.ads.googleads.v7.services\x1a\x39google/ads/googleads/v7/enums/response_content_type.proto\x1a=google/ads/googleads/v7/resources/campaign_bid_modifier.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a google/protobuf/field_mask.proto\x1a\x17google/rpc/status.proto\"{\n\x1dGetCampaignBidModifierRequest\x12Z\n\rresource_name\x18\x01 \x01(\tB5\xe2\x41\x01\x02\xfa\x41.\n,googleads.googleapis.com/CampaignBidModifierR\x0cresourceName\"\xfe\x02\n!MutateCampaignBidModifiersRequest\x12%\n\x0b\x63ustomer_id\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02R\ncustomerId\x12\x64\n\noperations\x18\x02 \x03(\x0b\x32>.google.ads.googleads.v7.services.CampaignBidModifierOperationB\x04\xe2\x41\x01\x02R\noperations\x12\'\n\x0fpartial_failure\x18\x03 \x01(\x08R\x0epartialFailure\x12#\n\rvalidate_only\x18\x04 \x01(\x08R\x0cvalidateOnly\x12~\n\x15response_content_type\x18\x05 \x01(\x0e\x32J.google.ads.googleads.v7.enums.ResponseContentTypeEnum.ResponseContentTypeR\x13responseContentType\"\xa6\x02\n\x1c\x43\x61mpaignBidModifierOperation\x12;\n\x0bupdate_mask\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\nupdateMask\x12P\n\x06\x63reate\x18\x01 \x01(\x0b\x32\x36.google.ads.googleads.v7.resources.CampaignBidModifierH\x00R\x06\x63reate\x12P\n\x06update\x18\x02 \x01(\x0b\x32\x36.google.ads.googleads.v7.resources.CampaignBidModifierH\x00R\x06update\x12\x18\n\x06remove\x18\x03 \x01(\tH\x00R\x06removeB\x0b\n\toperation\"\xc9\x01\n\"MutateCampaignBidModifiersResponse\x12\x46\n\x15partial_failure_error\x18\x03 \x01(\x0b\x32\x12.google.rpc.StatusR\x13partialFailureError\x12[\n\x07results\x18\x02 \x03(\x0b\x32\x41.google.ads.googleads.v7.services.MutateCampaignBidModifierResultR\x07results\"\xb2\x01\n\x1fMutateCampaignBidModifierResult\x12#\n\rresource_name\x18\x01 \x01(\tR\x0cresourceName\x12j\n\x15\x63\x61mpaign_bid_modifier\x18\x02 \x01(\x0b\x32\x36.google.ads.googleads.v7.resources.CampaignBidModifierR\x13\x63\x61mpaignBidModifier2\xd0\x04\n\x1a\x43\x61mpaignBidModifierService\x12\xe1\x01\n\x16GetCampaignBidModifier\x12?.google.ads.googleads.v7.services.GetCampaignBidModifierRequest\x1a\x36.google.ads.googleads.v7.resources.CampaignBidModifier\"N\xda\x41\rresource_name\x82\xd3\xe4\x93\x02\x38\x12\x36/v7/{resource_name=customers/*/campaignBidModifiers/*}\x12\x86\x02\n\x1aMutateCampaignBidModifiers\x12\x43.google.ads.googleads.v7.services.MutateCampaignBidModifiersRequest\x1a\x44.google.ads.googleads.v7.services.MutateCampaignBidModifiersResponse\"]\xda\x41\x16\x63ustomer_id,operations\x82\xd3\xe4\x93\x02>\"9/v7/customers/{customer_id=*}/campaignBidModifiers:mutate:\x01*\x1a\x45\xca\x41\x18googleads.googleapis.com\xd2\x41\'https://www.googleapis.com/auth/adwordsB\x86\x02\n$com.google.ads.googleads.v7.servicesB\x1f\x43\x61mpaignBidModifierServiceProtoP\x01ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v7/services;services\xa2\x02\x03GAA\xaa\x02 Google.Ads.GoogleAds.V7.Services\xca\x02 Google\\Ads\\GoogleAds\\V7\\Services\xea\x02$Google::Ads::GoogleAds::V7::Servicesb\x06proto3')



_GETCAMPAIGNBIDMODIFIERREQUEST = DESCRIPTOR.message_types_by_name['GetCampaignBidModifierRequest']
_MUTATECAMPAIGNBIDMODIFIERSREQUEST = DESCRIPTOR.message_types_by_name['MutateCampaignBidModifiersRequest']
_CAMPAIGNBIDMODIFIEROPERATION = DESCRIPTOR.message_types_by_name['CampaignBidModifierOperation']
_MUTATECAMPAIGNBIDMODIFIERSRESPONSE = DESCRIPTOR.message_types_by_name['MutateCampaignBidModifiersResponse']
_MUTATECAMPAIGNBIDMODIFIERRESULT = DESCRIPTOR.message_types_by_name['MutateCampaignBidModifierResult']
GetCampaignBidModifierRequest = _reflection.GeneratedProtocolMessageType('GetCampaignBidModifierRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETCAMPAIGNBIDMODIFIERREQUEST,
  '__module__' : 'google.ads.googleads.v7.services.campaign_bid_modifier_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v7.services.GetCampaignBidModifierRequest)
  })
_sym_db.RegisterMessage(GetCampaignBidModifierRequest)

MutateCampaignBidModifiersRequest = _reflection.GeneratedProtocolMessageType('MutateCampaignBidModifiersRequest', (_message.Message,), {
  'DESCRIPTOR' : _MUTATECAMPAIGNBIDMODIFIERSREQUEST,
  '__module__' : 'google.ads.googleads.v7.services.campaign_bid_modifier_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v7.services.MutateCampaignBidModifiersRequest)
  })
_sym_db.RegisterMessage(MutateCampaignBidModifiersRequest)

CampaignBidModifierOperation = _reflection.GeneratedProtocolMessageType('CampaignBidModifierOperation', (_message.Message,), {
  'DESCRIPTOR' : _CAMPAIGNBIDMODIFIEROPERATION,
  '__module__' : 'google.ads.googleads.v7.services.campaign_bid_modifier_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v7.services.CampaignBidModifierOperation)
  })
_sym_db.RegisterMessage(CampaignBidModifierOperation)

MutateCampaignBidModifiersResponse = _reflection.GeneratedProtocolMessageType('MutateCampaignBidModifiersResponse', (_message.Message,), {
  'DESCRIPTOR' : _MUTATECAMPAIGNBIDMODIFIERSRESPONSE,
  '__module__' : 'google.ads.googleads.v7.services.campaign_bid_modifier_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v7.services.MutateCampaignBidModifiersResponse)
  })
_sym_db.RegisterMessage(MutateCampaignBidModifiersResponse)

MutateCampaignBidModifierResult = _reflection.GeneratedProtocolMessageType('MutateCampaignBidModifierResult', (_message.Message,), {
  'DESCRIPTOR' : _MUTATECAMPAIGNBIDMODIFIERRESULT,
  '__module__' : 'google.ads.googleads.v7.services.campaign_bid_modifier_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v7.services.MutateCampaignBidModifierResult)
  })
_sym_db.RegisterMessage(MutateCampaignBidModifierResult)

_CAMPAIGNBIDMODIFIERSERVICE = DESCRIPTOR.services_by_name['CampaignBidModifierService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n$com.google.ads.googleads.v7.servicesB\037CampaignBidModifierServiceProtoP\001ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v7/services;services\242\002\003GAA\252\002 Google.Ads.GoogleAds.V7.Services\312\002 Google\\Ads\\GoogleAds\\V7\\Services\352\002$Google::Ads::GoogleAds::V7::Services'
  _GETCAMPAIGNBIDMODIFIERREQUEST.fields_by_name['resource_name']._options = None
  _GETCAMPAIGNBIDMODIFIERREQUEST.fields_by_name['resource_name']._serialized_options = b'\342A\001\002\372A.\n,googleads.googleapis.com/CampaignBidModifier'
  _MUTATECAMPAIGNBIDMODIFIERSREQUEST.fields_by_name['customer_id']._options = None
  _MUTATECAMPAIGNBIDMODIFIERSREQUEST.fields_by_name['customer_id']._serialized_options = b'\342A\001\002'
  _MUTATECAMPAIGNBIDMODIFIERSREQUEST.fields_by_name['operations']._options = None
  _MUTATECAMPAIGNBIDMODIFIERSREQUEST.fields_by_name['operations']._serialized_options = b'\342A\001\002'
  _CAMPAIGNBIDMODIFIERSERVICE._options = None
  _CAMPAIGNBIDMODIFIERSERVICE._serialized_options = b'\312A\030googleads.googleapis.com\322A\'https://www.googleapis.com/auth/adwords'
  _CAMPAIGNBIDMODIFIERSERVICE.methods_by_name['GetCampaignBidModifier']._options = None
  _CAMPAIGNBIDMODIFIERSERVICE.methods_by_name['GetCampaignBidModifier']._serialized_options = b'\332A\rresource_name\202\323\344\223\0028\0226/v7/{resource_name=customers/*/campaignBidModifiers/*}'
  _CAMPAIGNBIDMODIFIERSERVICE.methods_by_name['MutateCampaignBidModifiers']._options = None
  _CAMPAIGNBIDMODIFIERSERVICE.methods_by_name['MutateCampaignBidModifiers']._serialized_options = b'\332A\026customer_id,operations\202\323\344\223\002>\"9/v7/customers/{customer_id=*}/campaignBidModifiers:mutate:\001*'
  _GETCAMPAIGNBIDMODIFIERREQUEST._serialized_start=402
  _GETCAMPAIGNBIDMODIFIERREQUEST._serialized_end=525
  _MUTATECAMPAIGNBIDMODIFIERSREQUEST._serialized_start=528
  _MUTATECAMPAIGNBIDMODIFIERSREQUEST._serialized_end=910
  _CAMPAIGNBIDMODIFIEROPERATION._serialized_start=913
  _CAMPAIGNBIDMODIFIEROPERATION._serialized_end=1207
  _MUTATECAMPAIGNBIDMODIFIERSRESPONSE._serialized_start=1210
  _MUTATECAMPAIGNBIDMODIFIERSRESPONSE._serialized_end=1411
  _MUTATECAMPAIGNBIDMODIFIERRESULT._serialized_start=1414
  _MUTATECAMPAIGNBIDMODIFIERRESULT._serialized_end=1592
  _CAMPAIGNBIDMODIFIERSERVICE._serialized_start=1595
  _CAMPAIGNBIDMODIFIERSERVICE._serialized_end=2187
# @@protoc_insertion_point(module_scope)
