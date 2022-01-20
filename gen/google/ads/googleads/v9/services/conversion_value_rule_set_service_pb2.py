# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v9/services/conversion_value_rule_set_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.googleads.v9.enums import response_content_type_pb2 as google_dot_ads_dot_googleads_dot_v9_dot_enums_dot_response__content__type__pb2
from google.ads.googleads.v9.resources import conversion_value_rule_set_pb2 as google_dot_ads_dot_googleads_dot_v9_dot_resources_dot_conversion__value__rule__set__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import client_pb2 as google_dot_api_dot_client__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nHgoogle/ads/googleads/v9/services/conversion_value_rule_set_service.proto\x12 google.ads.googleads.v9.services\x1a\x39google/ads/googleads/v9/enums/response_content_type.proto\x1a\x41google/ads/googleads/v9/resources/conversion_value_rule_set.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a google/protobuf/field_mask.proto\x1a\x17google/rpc/status.proto\"\x81\x01\n GetConversionValueRuleSetRequest\x12]\n\rresource_name\x18\x01 \x01(\tB8\xe2\x41\x01\x02\xfa\x41\x31\n/googleads.googleapis.com/ConversionValueRuleSetR\x0cresourceName\"\x84\x03\n$MutateConversionValueRuleSetsRequest\x12%\n\x0b\x63ustomer_id\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02R\ncustomerId\x12g\n\noperations\x18\x02 \x03(\x0b\x32\x41.google.ads.googleads.v9.services.ConversionValueRuleSetOperationB\x04\xe2\x41\x01\x02R\noperations\x12\'\n\x0fpartial_failure\x18\x05 \x01(\x08R\x0epartialFailure\x12#\n\rvalidate_only\x18\x03 \x01(\x08R\x0cvalidateOnly\x12~\n\x15response_content_type\x18\x04 \x01(\x0e\x32J.google.ads.googleads.v9.enums.ResponseContentTypeEnum.ResponseContentTypeR\x13responseContentType\"\xaf\x02\n\x1f\x43onversionValueRuleSetOperation\x12;\n\x0bupdate_mask\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\nupdateMask\x12S\n\x06\x63reate\x18\x01 \x01(\x0b\x32\x39.google.ads.googleads.v9.resources.ConversionValueRuleSetH\x00R\x06\x63reate\x12S\n\x06update\x18\x02 \x01(\x0b\x32\x39.google.ads.googleads.v9.resources.ConversionValueRuleSetH\x00R\x06update\x12\x18\n\x06remove\x18\x03 \x01(\tH\x00R\x06removeB\x0b\n\toperation\"\xcf\x01\n%MutateConversionValueRuleSetsResponse\x12^\n\x07results\x18\x01 \x03(\x0b\x32\x44.google.ads.googleads.v9.services.MutateConversionValueRuleSetResultR\x07results\x12\x46\n\x15partial_failure_error\x18\x02 \x01(\x0b\x32\x12.google.rpc.StatusR\x13partialFailureError\"\xbf\x01\n\"MutateConversionValueRuleSetResult\x12#\n\rresource_name\x18\x01 \x01(\tR\x0cresourceName\x12t\n\x19\x63onversion_value_rule_set\x18\x02 \x01(\x0b\x32\x39.google.ads.googleads.v9.resources.ConversionValueRuleSetR\x16\x63onversionValueRuleSet2\xeb\x04\n\x1d\x43onversionValueRuleSetService\x12\xed\x01\n\x19GetConversionValueRuleSet\x12\x42.google.ads.googleads.v9.services.GetConversionValueRuleSetRequest\x1a\x39.google.ads.googleads.v9.resources.ConversionValueRuleSet\"Q\xda\x41\rresource_name\x82\xd3\xe4\x93\x02;\x12\x39/v9/{resource_name=customers/*/conversionValueRuleSets/*}\x12\x92\x02\n\x1dMutateConversionValueRuleSets\x12\x46.google.ads.googleads.v9.services.MutateConversionValueRuleSetsRequest\x1aG.google.ads.googleads.v9.services.MutateConversionValueRuleSetsResponse\"`\xda\x41\x16\x63ustomer_id,operations\x82\xd3\xe4\x93\x02\x41\"</v9/customers/{customer_id=*}/conversionValueRuleSets:mutate:\x01*\x1a\x45\xca\x41\x18googleads.googleapis.com\xd2\x41\'https://www.googleapis.com/auth/adwordsB\x89\x02\n$com.google.ads.googleads.v9.servicesB\"ConversionValueRuleSetServiceProtoP\x01ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v9/services;services\xa2\x02\x03GAA\xaa\x02 Google.Ads.GoogleAds.V9.Services\xca\x02 Google\\Ads\\GoogleAds\\V9\\Services\xea\x02$Google::Ads::GoogleAds::V9::Servicesb\x06proto3')



_GETCONVERSIONVALUERULESETREQUEST = DESCRIPTOR.message_types_by_name['GetConversionValueRuleSetRequest']
_MUTATECONVERSIONVALUERULESETSREQUEST = DESCRIPTOR.message_types_by_name['MutateConversionValueRuleSetsRequest']
_CONVERSIONVALUERULESETOPERATION = DESCRIPTOR.message_types_by_name['ConversionValueRuleSetOperation']
_MUTATECONVERSIONVALUERULESETSRESPONSE = DESCRIPTOR.message_types_by_name['MutateConversionValueRuleSetsResponse']
_MUTATECONVERSIONVALUERULESETRESULT = DESCRIPTOR.message_types_by_name['MutateConversionValueRuleSetResult']
GetConversionValueRuleSetRequest = _reflection.GeneratedProtocolMessageType('GetConversionValueRuleSetRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETCONVERSIONVALUERULESETREQUEST,
  '__module__' : 'google.ads.googleads.v9.services.conversion_value_rule_set_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v9.services.GetConversionValueRuleSetRequest)
  })
_sym_db.RegisterMessage(GetConversionValueRuleSetRequest)

MutateConversionValueRuleSetsRequest = _reflection.GeneratedProtocolMessageType('MutateConversionValueRuleSetsRequest', (_message.Message,), {
  'DESCRIPTOR' : _MUTATECONVERSIONVALUERULESETSREQUEST,
  '__module__' : 'google.ads.googleads.v9.services.conversion_value_rule_set_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v9.services.MutateConversionValueRuleSetsRequest)
  })
_sym_db.RegisterMessage(MutateConversionValueRuleSetsRequest)

ConversionValueRuleSetOperation = _reflection.GeneratedProtocolMessageType('ConversionValueRuleSetOperation', (_message.Message,), {
  'DESCRIPTOR' : _CONVERSIONVALUERULESETOPERATION,
  '__module__' : 'google.ads.googleads.v9.services.conversion_value_rule_set_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v9.services.ConversionValueRuleSetOperation)
  })
_sym_db.RegisterMessage(ConversionValueRuleSetOperation)

MutateConversionValueRuleSetsResponse = _reflection.GeneratedProtocolMessageType('MutateConversionValueRuleSetsResponse', (_message.Message,), {
  'DESCRIPTOR' : _MUTATECONVERSIONVALUERULESETSRESPONSE,
  '__module__' : 'google.ads.googleads.v9.services.conversion_value_rule_set_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v9.services.MutateConversionValueRuleSetsResponse)
  })
_sym_db.RegisterMessage(MutateConversionValueRuleSetsResponse)

MutateConversionValueRuleSetResult = _reflection.GeneratedProtocolMessageType('MutateConversionValueRuleSetResult', (_message.Message,), {
  'DESCRIPTOR' : _MUTATECONVERSIONVALUERULESETRESULT,
  '__module__' : 'google.ads.googleads.v9.services.conversion_value_rule_set_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v9.services.MutateConversionValueRuleSetResult)
  })
_sym_db.RegisterMessage(MutateConversionValueRuleSetResult)

_CONVERSIONVALUERULESETSERVICE = DESCRIPTOR.services_by_name['ConversionValueRuleSetService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n$com.google.ads.googleads.v9.servicesB\"ConversionValueRuleSetServiceProtoP\001ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v9/services;services\242\002\003GAA\252\002 Google.Ads.GoogleAds.V9.Services\312\002 Google\\Ads\\GoogleAds\\V9\\Services\352\002$Google::Ads::GoogleAds::V9::Services'
  _GETCONVERSIONVALUERULESETREQUEST.fields_by_name['resource_name']._options = None
  _GETCONVERSIONVALUERULESETREQUEST.fields_by_name['resource_name']._serialized_options = b'\342A\001\002\372A1\n/googleads.googleapis.com/ConversionValueRuleSet'
  _MUTATECONVERSIONVALUERULESETSREQUEST.fields_by_name['customer_id']._options = None
  _MUTATECONVERSIONVALUERULESETSREQUEST.fields_by_name['customer_id']._serialized_options = b'\342A\001\002'
  _MUTATECONVERSIONVALUERULESETSREQUEST.fields_by_name['operations']._options = None
  _MUTATECONVERSIONVALUERULESETSREQUEST.fields_by_name['operations']._serialized_options = b'\342A\001\002'
  _CONVERSIONVALUERULESETSERVICE._options = None
  _CONVERSIONVALUERULESETSERVICE._serialized_options = b'\312A\030googleads.googleapis.com\322A\'https://www.googleapis.com/auth/adwords'
  _CONVERSIONVALUERULESETSERVICE.methods_by_name['GetConversionValueRuleSet']._options = None
  _CONVERSIONVALUERULESETSERVICE.methods_by_name['GetConversionValueRuleSet']._serialized_options = b'\332A\rresource_name\202\323\344\223\002;\0229/v9/{resource_name=customers/*/conversionValueRuleSets/*}'
  _CONVERSIONVALUERULESETSERVICE.methods_by_name['MutateConversionValueRuleSets']._options = None
  _CONVERSIONVALUERULESETSERVICE.methods_by_name['MutateConversionValueRuleSets']._serialized_options = b'\332A\026customer_id,operations\202\323\344\223\002A\"</v9/customers/{customer_id=*}/conversionValueRuleSets:mutate:\001*'
  _GETCONVERSIONVALUERULESETREQUEST._serialized_start=411
  _GETCONVERSIONVALUERULESETREQUEST._serialized_end=540
  _MUTATECONVERSIONVALUERULESETSREQUEST._serialized_start=543
  _MUTATECONVERSIONVALUERULESETSREQUEST._serialized_end=931
  _CONVERSIONVALUERULESETOPERATION._serialized_start=934
  _CONVERSIONVALUERULESETOPERATION._serialized_end=1237
  _MUTATECONVERSIONVALUERULESETSRESPONSE._serialized_start=1240
  _MUTATECONVERSIONVALUERULESETSRESPONSE._serialized_end=1447
  _MUTATECONVERSIONVALUERULESETRESULT._serialized_start=1450
  _MUTATECONVERSIONVALUERULESETRESULT._serialized_end=1641
  _CONVERSIONVALUERULESETSERVICE._serialized_start=1644
  _CONVERSIONVALUERULESETSERVICE._serialized_end=2263
# @@protoc_insertion_point(module_scope)
