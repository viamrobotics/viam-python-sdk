# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v9/services/customer_customizer_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.googleads.v9.enums import response_content_type_pb2 as google_dot_ads_dot_googleads_dot_v9_dot_enums_dot_response__content__type__pb2
from google.ads.googleads.v9.resources import customer_customizer_pb2 as google_dot_ads_dot_googleads_dot_v9_dot_resources_dot_customer__customizer__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import client_pb2 as google_dot_api_dot_client__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nBgoogle/ads/googleads/v9/services/customer_customizer_service.proto\x12 google.ads.googleads.v9.services\x1a\x39google/ads/googleads/v9/enums/response_content_type.proto\x1a;google/ads/googleads/v9/resources/customer_customizer.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x17google/rpc/status.proto\"\xfc\x02\n MutateCustomerCustomizersRequest\x12%\n\x0b\x63ustomer_id\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02R\ncustomerId\x12\x63\n\noperations\x18\x02 \x03(\x0b\x32=.google.ads.googleads.v9.services.CustomerCustomizerOperationB\x04\xe2\x41\x01\x02R\noperations\x12\'\n\x0fpartial_failure\x18\x03 \x01(\x08R\x0epartialFailure\x12#\n\rvalidate_only\x18\x04 \x01(\x08R\x0cvalidateOnly\x12~\n\x15response_content_type\x18\x05 \x01(\x0e\x32J.google.ads.googleads.v9.enums.ResponseContentTypeEnum.ResponseContentTypeR\x13responseContentType\"\x95\x01\n\x1b\x43ustomerCustomizerOperation\x12O\n\x06\x63reate\x18\x01 \x01(\x0b\x32\x35.google.ads.googleads.v9.resources.CustomerCustomizerH\x00R\x06\x63reate\x12\x18\n\x06remove\x18\x02 \x01(\tH\x00R\x06removeB\x0b\n\toperation\"\xc7\x01\n!MutateCustomerCustomizersResponse\x12Z\n\x07results\x18\x01 \x03(\x0b\x32@.google.ads.googleads.v9.services.MutateCustomerCustomizerResultR\x07results\x12\x46\n\x15partial_failure_error\x18\x02 \x01(\x0b\x32\x12.google.rpc.StatusR\x13partialFailureError\"\xad\x01\n\x1eMutateCustomerCustomizerResult\x12#\n\rresource_name\x18\x01 \x01(\tR\x0cresourceName\x12\x66\n\x13\x63ustomer_customizer\x18\x02 \x01(\x0b\x32\x35.google.ads.googleads.v9.resources.CustomerCustomizerR\x12\x63ustomerCustomizer2\xe7\x02\n\x19\x43ustomerCustomizerService\x12\x82\x02\n\x19MutateCustomerCustomizers\x12\x42.google.ads.googleads.v9.services.MutateCustomerCustomizersRequest\x1a\x43.google.ads.googleads.v9.services.MutateCustomerCustomizersResponse\"\\\xda\x41\x16\x63ustomer_id,operations\x82\xd3\xe4\x93\x02=\"8/v9/customers/{customer_id=*}/CustomerCustomizers:mutate:\x01*\x1a\x45\xca\x41\x18googleads.googleapis.com\xd2\x41\'https://www.googleapis.com/auth/adwordsB\x85\x02\n$com.google.ads.googleads.v9.servicesB\x1e\x43ustomerCustomizerServiceProtoP\x01ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v9/services;services\xa2\x02\x03GAA\xaa\x02 Google.Ads.GoogleAds.V9.Services\xca\x02 Google\\Ads\\GoogleAds\\V9\\Services\xea\x02$Google::Ads::GoogleAds::V9::Servicesb\x06proto3')



_MUTATECUSTOMERCUSTOMIZERSREQUEST = DESCRIPTOR.message_types_by_name['MutateCustomerCustomizersRequest']
_CUSTOMERCUSTOMIZEROPERATION = DESCRIPTOR.message_types_by_name['CustomerCustomizerOperation']
_MUTATECUSTOMERCUSTOMIZERSRESPONSE = DESCRIPTOR.message_types_by_name['MutateCustomerCustomizersResponse']
_MUTATECUSTOMERCUSTOMIZERRESULT = DESCRIPTOR.message_types_by_name['MutateCustomerCustomizerResult']
MutateCustomerCustomizersRequest = _reflection.GeneratedProtocolMessageType('MutateCustomerCustomizersRequest', (_message.Message,), {
  'DESCRIPTOR' : _MUTATECUSTOMERCUSTOMIZERSREQUEST,
  '__module__' : 'google.ads.googleads.v9.services.customer_customizer_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v9.services.MutateCustomerCustomizersRequest)
  })
_sym_db.RegisterMessage(MutateCustomerCustomizersRequest)

CustomerCustomizerOperation = _reflection.GeneratedProtocolMessageType('CustomerCustomizerOperation', (_message.Message,), {
  'DESCRIPTOR' : _CUSTOMERCUSTOMIZEROPERATION,
  '__module__' : 'google.ads.googleads.v9.services.customer_customizer_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v9.services.CustomerCustomizerOperation)
  })
_sym_db.RegisterMessage(CustomerCustomizerOperation)

MutateCustomerCustomizersResponse = _reflection.GeneratedProtocolMessageType('MutateCustomerCustomizersResponse', (_message.Message,), {
  'DESCRIPTOR' : _MUTATECUSTOMERCUSTOMIZERSRESPONSE,
  '__module__' : 'google.ads.googleads.v9.services.customer_customizer_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v9.services.MutateCustomerCustomizersResponse)
  })
_sym_db.RegisterMessage(MutateCustomerCustomizersResponse)

MutateCustomerCustomizerResult = _reflection.GeneratedProtocolMessageType('MutateCustomerCustomizerResult', (_message.Message,), {
  'DESCRIPTOR' : _MUTATECUSTOMERCUSTOMIZERRESULT,
  '__module__' : 'google.ads.googleads.v9.services.customer_customizer_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v9.services.MutateCustomerCustomizerResult)
  })
_sym_db.RegisterMessage(MutateCustomerCustomizerResult)

_CUSTOMERCUSTOMIZERSERVICE = DESCRIPTOR.services_by_name['CustomerCustomizerService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n$com.google.ads.googleads.v9.servicesB\036CustomerCustomizerServiceProtoP\001ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v9/services;services\242\002\003GAA\252\002 Google.Ads.GoogleAds.V9.Services\312\002 Google\\Ads\\GoogleAds\\V9\\Services\352\002$Google::Ads::GoogleAds::V9::Services'
  _MUTATECUSTOMERCUSTOMIZERSREQUEST.fields_by_name['customer_id']._options = None
  _MUTATECUSTOMERCUSTOMIZERSREQUEST.fields_by_name['customer_id']._serialized_options = b'\342A\001\002'
  _MUTATECUSTOMERCUSTOMIZERSREQUEST.fields_by_name['operations']._options = None
  _MUTATECUSTOMERCUSTOMIZERSREQUEST.fields_by_name['operations']._serialized_options = b'\342A\001\002'
  _CUSTOMERCUSTOMIZERSERVICE._options = None
  _CUSTOMERCUSTOMIZERSERVICE._serialized_options = b'\312A\030googleads.googleapis.com\322A\'https://www.googleapis.com/auth/adwords'
  _CUSTOMERCUSTOMIZERSERVICE.methods_by_name['MutateCustomerCustomizers']._options = None
  _CUSTOMERCUSTOMIZERSERVICE.methods_by_name['MutateCustomerCustomizers']._serialized_options = b'\332A\026customer_id,operations\202\323\344\223\002=\"8/v9/customers/{customer_id=*}/CustomerCustomizers:mutate:\001*'
  _MUTATECUSTOMERCUSTOMIZERSREQUEST._serialized_start=338
  _MUTATECUSTOMERCUSTOMIZERSREQUEST._serialized_end=718
  _CUSTOMERCUSTOMIZEROPERATION._serialized_start=721
  _CUSTOMERCUSTOMIZEROPERATION._serialized_end=870
  _MUTATECUSTOMERCUSTOMIZERSRESPONSE._serialized_start=873
  _MUTATECUSTOMERCUSTOMIZERSRESPONSE._serialized_end=1072
  _MUTATECUSTOMERCUSTOMIZERRESULT._serialized_start=1075
  _MUTATECUSTOMERCUSTOMIZERRESULT._serialized_end=1248
  _CUSTOMERCUSTOMIZERSERVICE._serialized_start=1251
  _CUSTOMERCUSTOMIZERSERVICE._serialized_end=1610
# @@protoc_insertion_point(module_scope)
