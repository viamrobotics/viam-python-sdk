# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v7/services/customer_extension_setting_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.googleads.v7.enums import response_content_type_pb2 as google_dot_ads_dot_googleads_dot_v7_dot_enums_dot_response__content__type__pb2
from google.ads.googleads.v7.resources import customer_extension_setting_pb2 as google_dot_ads_dot_googleads_dot_v7_dot_resources_dot_customer__extension__setting__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import client_pb2 as google_dot_api_dot_client__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nIgoogle/ads/googleads/v7/services/customer_extension_setting_service.proto\x12 google.ads.googleads.v7.services\x1a\x39google/ads/googleads/v7/enums/response_content_type.proto\x1a\x42google/ads/googleads/v7/resources/customer_extension_setting.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a google/protobuf/field_mask.proto\x1a\x17google/rpc/status.proto\"\x85\x01\n\"GetCustomerExtensionSettingRequest\x12_\n\rresource_name\x18\x01 \x01(\tB:\xe2\x41\x01\x02\xfa\x41\x33\n1googleads.googleapis.com/CustomerExtensionSettingR\x0cresourceName\"\x88\x03\n&MutateCustomerExtensionSettingsRequest\x12%\n\x0b\x63ustomer_id\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02R\ncustomerId\x12i\n\noperations\x18\x02 \x03(\x0b\x32\x43.google.ads.googleads.v7.services.CustomerExtensionSettingOperationB\x04\xe2\x41\x01\x02R\noperations\x12\'\n\x0fpartial_failure\x18\x03 \x01(\x08R\x0epartialFailure\x12#\n\rvalidate_only\x18\x04 \x01(\x08R\x0cvalidateOnly\x12~\n\x15response_content_type\x18\x05 \x01(\x0e\x32J.google.ads.googleads.v7.enums.ResponseContentTypeEnum.ResponseContentTypeR\x13responseContentType\"\xb5\x02\n!CustomerExtensionSettingOperation\x12;\n\x0bupdate_mask\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\nupdateMask\x12U\n\x06\x63reate\x18\x01 \x01(\x0b\x32;.google.ads.googleads.v7.resources.CustomerExtensionSettingH\x00R\x06\x63reate\x12U\n\x06update\x18\x02 \x01(\x0b\x32;.google.ads.googleads.v7.resources.CustomerExtensionSettingH\x00R\x06update\x12\x18\n\x06remove\x18\x03 \x01(\tH\x00R\x06removeB\x0b\n\toperation\"\xd3\x01\n\'MutateCustomerExtensionSettingsResponse\x12\x46\n\x15partial_failure_error\x18\x03 \x01(\x0b\x32\x12.google.rpc.StatusR\x13partialFailureError\x12`\n\x07results\x18\x02 \x03(\x0b\x32\x46.google.ads.googleads.v7.services.MutateCustomerExtensionSettingResultR\x07results\"\xc6\x01\n$MutateCustomerExtensionSettingResult\x12#\n\rresource_name\x18\x01 \x01(\tR\x0cresourceName\x12y\n\x1a\x63ustomer_extension_setting\x18\x02 \x01(\x0b\x32;.google.ads.googleads.v7.resources.CustomerExtensionSettingR\x18\x63ustomerExtensionSetting2\xfd\x04\n\x1f\x43ustomerExtensionSettingService\x12\xf5\x01\n\x1bGetCustomerExtensionSetting\x12\x44.google.ads.googleads.v7.services.GetCustomerExtensionSettingRequest\x1a;.google.ads.googleads.v7.resources.CustomerExtensionSetting\"S\xda\x41\rresource_name\x82\xd3\xe4\x93\x02=\x12;/v7/{resource_name=customers/*/customerExtensionSettings/*}\x12\x9a\x02\n\x1fMutateCustomerExtensionSettings\x12H.google.ads.googleads.v7.services.MutateCustomerExtensionSettingsRequest\x1aI.google.ads.googleads.v7.services.MutateCustomerExtensionSettingsResponse\"b\xda\x41\x16\x63ustomer_id,operations\x82\xd3\xe4\x93\x02\x43\">/v7/customers/{customer_id=*}/customerExtensionSettings:mutate:\x01*\x1a\x45\xca\x41\x18googleads.googleapis.com\xd2\x41\'https://www.googleapis.com/auth/adwordsB\x8b\x02\n$com.google.ads.googleads.v7.servicesB$CustomerExtensionSettingServiceProtoP\x01ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v7/services;services\xa2\x02\x03GAA\xaa\x02 Google.Ads.GoogleAds.V7.Services\xca\x02 Google\\Ads\\GoogleAds\\V7\\Services\xea\x02$Google::Ads::GoogleAds::V7::Servicesb\x06proto3')



_GETCUSTOMEREXTENSIONSETTINGREQUEST = DESCRIPTOR.message_types_by_name['GetCustomerExtensionSettingRequest']
_MUTATECUSTOMEREXTENSIONSETTINGSREQUEST = DESCRIPTOR.message_types_by_name['MutateCustomerExtensionSettingsRequest']
_CUSTOMEREXTENSIONSETTINGOPERATION = DESCRIPTOR.message_types_by_name['CustomerExtensionSettingOperation']
_MUTATECUSTOMEREXTENSIONSETTINGSRESPONSE = DESCRIPTOR.message_types_by_name['MutateCustomerExtensionSettingsResponse']
_MUTATECUSTOMEREXTENSIONSETTINGRESULT = DESCRIPTOR.message_types_by_name['MutateCustomerExtensionSettingResult']
GetCustomerExtensionSettingRequest = _reflection.GeneratedProtocolMessageType('GetCustomerExtensionSettingRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETCUSTOMEREXTENSIONSETTINGREQUEST,
  '__module__' : 'google.ads.googleads.v7.services.customer_extension_setting_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v7.services.GetCustomerExtensionSettingRequest)
  })
_sym_db.RegisterMessage(GetCustomerExtensionSettingRequest)

MutateCustomerExtensionSettingsRequest = _reflection.GeneratedProtocolMessageType('MutateCustomerExtensionSettingsRequest', (_message.Message,), {
  'DESCRIPTOR' : _MUTATECUSTOMEREXTENSIONSETTINGSREQUEST,
  '__module__' : 'google.ads.googleads.v7.services.customer_extension_setting_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v7.services.MutateCustomerExtensionSettingsRequest)
  })
_sym_db.RegisterMessage(MutateCustomerExtensionSettingsRequest)

CustomerExtensionSettingOperation = _reflection.GeneratedProtocolMessageType('CustomerExtensionSettingOperation', (_message.Message,), {
  'DESCRIPTOR' : _CUSTOMEREXTENSIONSETTINGOPERATION,
  '__module__' : 'google.ads.googleads.v7.services.customer_extension_setting_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v7.services.CustomerExtensionSettingOperation)
  })
_sym_db.RegisterMessage(CustomerExtensionSettingOperation)

MutateCustomerExtensionSettingsResponse = _reflection.GeneratedProtocolMessageType('MutateCustomerExtensionSettingsResponse', (_message.Message,), {
  'DESCRIPTOR' : _MUTATECUSTOMEREXTENSIONSETTINGSRESPONSE,
  '__module__' : 'google.ads.googleads.v7.services.customer_extension_setting_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v7.services.MutateCustomerExtensionSettingsResponse)
  })
_sym_db.RegisterMessage(MutateCustomerExtensionSettingsResponse)

MutateCustomerExtensionSettingResult = _reflection.GeneratedProtocolMessageType('MutateCustomerExtensionSettingResult', (_message.Message,), {
  'DESCRIPTOR' : _MUTATECUSTOMEREXTENSIONSETTINGRESULT,
  '__module__' : 'google.ads.googleads.v7.services.customer_extension_setting_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v7.services.MutateCustomerExtensionSettingResult)
  })
_sym_db.RegisterMessage(MutateCustomerExtensionSettingResult)

_CUSTOMEREXTENSIONSETTINGSERVICE = DESCRIPTOR.services_by_name['CustomerExtensionSettingService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n$com.google.ads.googleads.v7.servicesB$CustomerExtensionSettingServiceProtoP\001ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v7/services;services\242\002\003GAA\252\002 Google.Ads.GoogleAds.V7.Services\312\002 Google\\Ads\\GoogleAds\\V7\\Services\352\002$Google::Ads::GoogleAds::V7::Services'
  _GETCUSTOMEREXTENSIONSETTINGREQUEST.fields_by_name['resource_name']._options = None
  _GETCUSTOMEREXTENSIONSETTINGREQUEST.fields_by_name['resource_name']._serialized_options = b'\342A\001\002\372A3\n1googleads.googleapis.com/CustomerExtensionSetting'
  _MUTATECUSTOMEREXTENSIONSETTINGSREQUEST.fields_by_name['customer_id']._options = None
  _MUTATECUSTOMEREXTENSIONSETTINGSREQUEST.fields_by_name['customer_id']._serialized_options = b'\342A\001\002'
  _MUTATECUSTOMEREXTENSIONSETTINGSREQUEST.fields_by_name['operations']._options = None
  _MUTATECUSTOMEREXTENSIONSETTINGSREQUEST.fields_by_name['operations']._serialized_options = b'\342A\001\002'
  _CUSTOMEREXTENSIONSETTINGSERVICE._options = None
  _CUSTOMEREXTENSIONSETTINGSERVICE._serialized_options = b'\312A\030googleads.googleapis.com\322A\'https://www.googleapis.com/auth/adwords'
  _CUSTOMEREXTENSIONSETTINGSERVICE.methods_by_name['GetCustomerExtensionSetting']._options = None
  _CUSTOMEREXTENSIONSETTINGSERVICE.methods_by_name['GetCustomerExtensionSetting']._serialized_options = b'\332A\rresource_name\202\323\344\223\002=\022;/v7/{resource_name=customers/*/customerExtensionSettings/*}'
  _CUSTOMEREXTENSIONSETTINGSERVICE.methods_by_name['MutateCustomerExtensionSettings']._options = None
  _CUSTOMEREXTENSIONSETTINGSERVICE.methods_by_name['MutateCustomerExtensionSettings']._serialized_options = b'\332A\026customer_id,operations\202\323\344\223\002C\">/v7/customers/{customer_id=*}/customerExtensionSettings:mutate:\001*'
  _GETCUSTOMEREXTENSIONSETTINGREQUEST._serialized_start=413
  _GETCUSTOMEREXTENSIONSETTINGREQUEST._serialized_end=546
  _MUTATECUSTOMEREXTENSIONSETTINGSREQUEST._serialized_start=549
  _MUTATECUSTOMEREXTENSIONSETTINGSREQUEST._serialized_end=941
  _CUSTOMEREXTENSIONSETTINGOPERATION._serialized_start=944
  _CUSTOMEREXTENSIONSETTINGOPERATION._serialized_end=1253
  _MUTATECUSTOMEREXTENSIONSETTINGSRESPONSE._serialized_start=1256
  _MUTATECUSTOMEREXTENSIONSETTINGSRESPONSE._serialized_end=1467
  _MUTATECUSTOMEREXTENSIONSETTINGRESULT._serialized_start=1470
  _MUTATECUSTOMEREXTENSIONSETTINGRESULT._serialized_end=1668
  _CUSTOMEREXTENSIONSETTINGSERVICE._serialized_start=1671
  _CUSTOMEREXTENSIONSETTINGSERVICE._serialized_end=2308
# @@protoc_insertion_point(module_scope)
