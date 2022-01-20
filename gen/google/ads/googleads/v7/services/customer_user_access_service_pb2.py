# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v7/services/customer_user_access_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.googleads.v7.resources import customer_user_access_pb2 as google_dot_ads_dot_googleads_dot_v7_dot_resources_dot_customer__user__access__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import client_pb2 as google_dot_api_dot_client__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nCgoogle/ads/googleads/v7/services/customer_user_access_service.proto\x12 google.ads.googleads.v7.services\x1a<google/ads/googleads/v7/resources/customer_user_access.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a google/protobuf/field_mask.proto\"y\n\x1cGetCustomerUserAccessRequest\x12Y\n\rresource_name\x18\x01 \x01(\tB4\xe2\x41\x01\x02\xfa\x41-\n+googleads.googleapis.com/CustomerUserAccessR\x0cresourceName\"\xab\x01\n\x1fMutateCustomerUserAccessRequest\x12%\n\x0b\x63ustomer_id\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02R\ncustomerId\x12\x61\n\toperation\x18\x02 \x01(\x0b\x32=.google.ads.googleads.v7.services.CustomerUserAccessOperationB\x04\xe2\x41\x01\x02R\toperation\"\xd2\x01\n\x1b\x43ustomerUserAccessOperation\x12;\n\x0bupdate_mask\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\nupdateMask\x12O\n\x06update\x18\x01 \x01(\x0b\x32\x35.google.ads.googleads.v7.resources.CustomerUserAccessH\x00R\x06update\x12\x18\n\x06remove\x18\x02 \x01(\tH\x00R\x06removeB\x0b\n\toperation\"|\n MutateCustomerUserAccessResponse\x12X\n\x06result\x18\x01 \x01(\x0b\x32@.google.ads.googleads.v7.services.MutateCustomerUserAccessResultR\x06result\"E\n\x1eMutateCustomerUserAccessResult\x12#\n\rresource_name\x18\x01 \x01(\tR\x0cresourceName2\xc5\x04\n\x19\x43ustomerUserAccessService\x12\xde\x01\n\x15GetCustomerUserAccess\x12>.google.ads.googleads.v7.services.GetCustomerUserAccessRequest\x1a\x35.google.ads.googleads.v7.resources.CustomerUserAccess\"N\xda\x41\rresource_name\x82\xd3\xe4\x93\x02\x38\x12\x36/v7/{resource_name=customers/*/customerUserAccesses/*}\x12\xff\x01\n\x18MutateCustomerUserAccess\x12\x41.google.ads.googleads.v7.services.MutateCustomerUserAccessRequest\x1a\x42.google.ads.googleads.v7.services.MutateCustomerUserAccessResponse\"\\\xda\x41\x15\x63ustomer_id,operation\x82\xd3\xe4\x93\x02>\"9/v7/customers/{customer_id=*}/customerUserAccesses:mutate:\x01*\x1a\x45\xca\x41\x18googleads.googleapis.com\xd2\x41\'https://www.googleapis.com/auth/adwordsB\x85\x02\n$com.google.ads.googleads.v7.servicesB\x1e\x43ustomerUserAccessServiceProtoP\x01ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v7/services;services\xa2\x02\x03GAA\xaa\x02 Google.Ads.GoogleAds.V7.Services\xca\x02 Google\\Ads\\GoogleAds\\V7\\Services\xea\x02$Google::Ads::GoogleAds::V7::Servicesb\x06proto3')



_GETCUSTOMERUSERACCESSREQUEST = DESCRIPTOR.message_types_by_name['GetCustomerUserAccessRequest']
_MUTATECUSTOMERUSERACCESSREQUEST = DESCRIPTOR.message_types_by_name['MutateCustomerUserAccessRequest']
_CUSTOMERUSERACCESSOPERATION = DESCRIPTOR.message_types_by_name['CustomerUserAccessOperation']
_MUTATECUSTOMERUSERACCESSRESPONSE = DESCRIPTOR.message_types_by_name['MutateCustomerUserAccessResponse']
_MUTATECUSTOMERUSERACCESSRESULT = DESCRIPTOR.message_types_by_name['MutateCustomerUserAccessResult']
GetCustomerUserAccessRequest = _reflection.GeneratedProtocolMessageType('GetCustomerUserAccessRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETCUSTOMERUSERACCESSREQUEST,
  '__module__' : 'google.ads.googleads.v7.services.customer_user_access_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v7.services.GetCustomerUserAccessRequest)
  })
_sym_db.RegisterMessage(GetCustomerUserAccessRequest)

MutateCustomerUserAccessRequest = _reflection.GeneratedProtocolMessageType('MutateCustomerUserAccessRequest', (_message.Message,), {
  'DESCRIPTOR' : _MUTATECUSTOMERUSERACCESSREQUEST,
  '__module__' : 'google.ads.googleads.v7.services.customer_user_access_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v7.services.MutateCustomerUserAccessRequest)
  })
_sym_db.RegisterMessage(MutateCustomerUserAccessRequest)

CustomerUserAccessOperation = _reflection.GeneratedProtocolMessageType('CustomerUserAccessOperation', (_message.Message,), {
  'DESCRIPTOR' : _CUSTOMERUSERACCESSOPERATION,
  '__module__' : 'google.ads.googleads.v7.services.customer_user_access_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v7.services.CustomerUserAccessOperation)
  })
_sym_db.RegisterMessage(CustomerUserAccessOperation)

MutateCustomerUserAccessResponse = _reflection.GeneratedProtocolMessageType('MutateCustomerUserAccessResponse', (_message.Message,), {
  'DESCRIPTOR' : _MUTATECUSTOMERUSERACCESSRESPONSE,
  '__module__' : 'google.ads.googleads.v7.services.customer_user_access_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v7.services.MutateCustomerUserAccessResponse)
  })
_sym_db.RegisterMessage(MutateCustomerUserAccessResponse)

MutateCustomerUserAccessResult = _reflection.GeneratedProtocolMessageType('MutateCustomerUserAccessResult', (_message.Message,), {
  'DESCRIPTOR' : _MUTATECUSTOMERUSERACCESSRESULT,
  '__module__' : 'google.ads.googleads.v7.services.customer_user_access_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v7.services.MutateCustomerUserAccessResult)
  })
_sym_db.RegisterMessage(MutateCustomerUserAccessResult)

_CUSTOMERUSERACCESSSERVICE = DESCRIPTOR.services_by_name['CustomerUserAccessService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n$com.google.ads.googleads.v7.servicesB\036CustomerUserAccessServiceProtoP\001ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v7/services;services\242\002\003GAA\252\002 Google.Ads.GoogleAds.V7.Services\312\002 Google\\Ads\\GoogleAds\\V7\\Services\352\002$Google::Ads::GoogleAds::V7::Services'
  _GETCUSTOMERUSERACCESSREQUEST.fields_by_name['resource_name']._options = None
  _GETCUSTOMERUSERACCESSREQUEST.fields_by_name['resource_name']._serialized_options = b'\342A\001\002\372A-\n+googleads.googleapis.com/CustomerUserAccess'
  _MUTATECUSTOMERUSERACCESSREQUEST.fields_by_name['customer_id']._options = None
  _MUTATECUSTOMERUSERACCESSREQUEST.fields_by_name['customer_id']._serialized_options = b'\342A\001\002'
  _MUTATECUSTOMERUSERACCESSREQUEST.fields_by_name['operation']._options = None
  _MUTATECUSTOMERUSERACCESSREQUEST.fields_by_name['operation']._serialized_options = b'\342A\001\002'
  _CUSTOMERUSERACCESSSERVICE._options = None
  _CUSTOMERUSERACCESSSERVICE._serialized_options = b'\312A\030googleads.googleapis.com\322A\'https://www.googleapis.com/auth/adwords'
  _CUSTOMERUSERACCESSSERVICE.methods_by_name['GetCustomerUserAccess']._options = None
  _CUSTOMERUSERACCESSSERVICE.methods_by_name['GetCustomerUserAccess']._serialized_options = b'\332A\rresource_name\202\323\344\223\0028\0226/v7/{resource_name=customers/*/customerUserAccesses/*}'
  _CUSTOMERUSERACCESSSERVICE.methods_by_name['MutateCustomerUserAccess']._options = None
  _CUSTOMERUSERACCESSSERVICE.methods_by_name['MutateCustomerUserAccess']._serialized_options = b'\332A\025customer_id,operation\202\323\344\223\002>\"9/v7/customers/{customer_id=*}/customerUserAccesses:mutate:\001*'
  _GETCUSTOMERUSERACCESSREQUEST._serialized_start=316
  _GETCUSTOMERUSERACCESSREQUEST._serialized_end=437
  _MUTATECUSTOMERUSERACCESSREQUEST._serialized_start=440
  _MUTATECUSTOMERUSERACCESSREQUEST._serialized_end=611
  _CUSTOMERUSERACCESSOPERATION._serialized_start=614
  _CUSTOMERUSERACCESSOPERATION._serialized_end=824
  _MUTATECUSTOMERUSERACCESSRESPONSE._serialized_start=826
  _MUTATECUSTOMERUSERACCESSRESPONSE._serialized_end=950
  _MUTATECUSTOMERUSERACCESSRESULT._serialized_start=952
  _MUTATECUSTOMERUSERACCESSRESULT._serialized_end=1021
  _CUSTOMERUSERACCESSSERVICE._serialized_start=1024
  _CUSTOMERUSERACCESSSERVICE._serialized_end=1605
# @@protoc_insertion_point(module_scope)
