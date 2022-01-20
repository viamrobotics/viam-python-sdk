# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v7/services/customer_client_link_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.googleads.v7.resources import customer_client_link_pb2 as google_dot_ads_dot_googleads_dot_v7_dot_resources_dot_customer__client__link__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import client_pb2 as google_dot_api_dot_client__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nCgoogle/ads/googleads/v7/services/customer_client_link_service.proto\x12 google.ads.googleads.v7.services\x1a<google/ads/googleads/v7/resources/customer_client_link.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a google/protobuf/field_mask.proto\"y\n\x1cGetCustomerClientLinkRequest\x12Y\n\rresource_name\x18\x01 \x01(\tB4\xe2\x41\x01\x02\xfa\x41-\n+googleads.googleapis.com/CustomerClientLinkR\x0cresourceName\"\xd0\x01\n\x1fMutateCustomerClientLinkRequest\x12%\n\x0b\x63ustomer_id\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02R\ncustomerId\x12\x61\n\toperation\x18\x02 \x01(\x0b\x32=.google.ads.googleads.v7.services.CustomerClientLinkOperationB\x04\xe2\x41\x01\x02R\toperation\x12#\n\rvalidate_only\x18\x03 \x01(\x08R\x0cvalidateOnly\"\x89\x02\n\x1b\x43ustomerClientLinkOperation\x12;\n\x0bupdate_mask\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\nupdateMask\x12O\n\x06\x63reate\x18\x01 \x01(\x0b\x32\x35.google.ads.googleads.v7.resources.CustomerClientLinkH\x00R\x06\x63reate\x12O\n\x06update\x18\x02 \x01(\x0b\x32\x35.google.ads.googleads.v7.resources.CustomerClientLinkH\x00R\x06updateB\x0b\n\toperation\"|\n MutateCustomerClientLinkResponse\x12X\n\x06result\x18\x01 \x01(\x0b\x32@.google.ads.googleads.v7.services.MutateCustomerClientLinkResultR\x06result\"E\n\x1eMutateCustomerClientLinkResult\x12#\n\rresource_name\x18\x01 \x01(\tR\x0cresourceName2\xc3\x04\n\x19\x43ustomerClientLinkService\x12\xdd\x01\n\x15GetCustomerClientLink\x12>.google.ads.googleads.v7.services.GetCustomerClientLinkRequest\x1a\x35.google.ads.googleads.v7.resources.CustomerClientLink\"M\xda\x41\rresource_name\x82\xd3\xe4\x93\x02\x37\x12\x35/v7/{resource_name=customers/*/customerClientLinks/*}\x12\xfe\x01\n\x18MutateCustomerClientLink\x12\x41.google.ads.googleads.v7.services.MutateCustomerClientLinkRequest\x1a\x42.google.ads.googleads.v7.services.MutateCustomerClientLinkResponse\"[\xda\x41\x15\x63ustomer_id,operation\x82\xd3\xe4\x93\x02=\"8/v7/customers/{customer_id=*}/customerClientLinks:mutate:\x01*\x1a\x45\xca\x41\x18googleads.googleapis.com\xd2\x41\'https://www.googleapis.com/auth/adwordsB\x85\x02\n$com.google.ads.googleads.v7.servicesB\x1e\x43ustomerClientLinkServiceProtoP\x01ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v7/services;services\xa2\x02\x03GAA\xaa\x02 Google.Ads.GoogleAds.V7.Services\xca\x02 Google\\Ads\\GoogleAds\\V7\\Services\xea\x02$Google::Ads::GoogleAds::V7::Servicesb\x06proto3')



_GETCUSTOMERCLIENTLINKREQUEST = DESCRIPTOR.message_types_by_name['GetCustomerClientLinkRequest']
_MUTATECUSTOMERCLIENTLINKREQUEST = DESCRIPTOR.message_types_by_name['MutateCustomerClientLinkRequest']
_CUSTOMERCLIENTLINKOPERATION = DESCRIPTOR.message_types_by_name['CustomerClientLinkOperation']
_MUTATECUSTOMERCLIENTLINKRESPONSE = DESCRIPTOR.message_types_by_name['MutateCustomerClientLinkResponse']
_MUTATECUSTOMERCLIENTLINKRESULT = DESCRIPTOR.message_types_by_name['MutateCustomerClientLinkResult']
GetCustomerClientLinkRequest = _reflection.GeneratedProtocolMessageType('GetCustomerClientLinkRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETCUSTOMERCLIENTLINKREQUEST,
  '__module__' : 'google.ads.googleads.v7.services.customer_client_link_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v7.services.GetCustomerClientLinkRequest)
  })
_sym_db.RegisterMessage(GetCustomerClientLinkRequest)

MutateCustomerClientLinkRequest = _reflection.GeneratedProtocolMessageType('MutateCustomerClientLinkRequest', (_message.Message,), {
  'DESCRIPTOR' : _MUTATECUSTOMERCLIENTLINKREQUEST,
  '__module__' : 'google.ads.googleads.v7.services.customer_client_link_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v7.services.MutateCustomerClientLinkRequest)
  })
_sym_db.RegisterMessage(MutateCustomerClientLinkRequest)

CustomerClientLinkOperation = _reflection.GeneratedProtocolMessageType('CustomerClientLinkOperation', (_message.Message,), {
  'DESCRIPTOR' : _CUSTOMERCLIENTLINKOPERATION,
  '__module__' : 'google.ads.googleads.v7.services.customer_client_link_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v7.services.CustomerClientLinkOperation)
  })
_sym_db.RegisterMessage(CustomerClientLinkOperation)

MutateCustomerClientLinkResponse = _reflection.GeneratedProtocolMessageType('MutateCustomerClientLinkResponse', (_message.Message,), {
  'DESCRIPTOR' : _MUTATECUSTOMERCLIENTLINKRESPONSE,
  '__module__' : 'google.ads.googleads.v7.services.customer_client_link_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v7.services.MutateCustomerClientLinkResponse)
  })
_sym_db.RegisterMessage(MutateCustomerClientLinkResponse)

MutateCustomerClientLinkResult = _reflection.GeneratedProtocolMessageType('MutateCustomerClientLinkResult', (_message.Message,), {
  'DESCRIPTOR' : _MUTATECUSTOMERCLIENTLINKRESULT,
  '__module__' : 'google.ads.googleads.v7.services.customer_client_link_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v7.services.MutateCustomerClientLinkResult)
  })
_sym_db.RegisterMessage(MutateCustomerClientLinkResult)

_CUSTOMERCLIENTLINKSERVICE = DESCRIPTOR.services_by_name['CustomerClientLinkService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n$com.google.ads.googleads.v7.servicesB\036CustomerClientLinkServiceProtoP\001ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v7/services;services\242\002\003GAA\252\002 Google.Ads.GoogleAds.V7.Services\312\002 Google\\Ads\\GoogleAds\\V7\\Services\352\002$Google::Ads::GoogleAds::V7::Services'
  _GETCUSTOMERCLIENTLINKREQUEST.fields_by_name['resource_name']._options = None
  _GETCUSTOMERCLIENTLINKREQUEST.fields_by_name['resource_name']._serialized_options = b'\342A\001\002\372A-\n+googleads.googleapis.com/CustomerClientLink'
  _MUTATECUSTOMERCLIENTLINKREQUEST.fields_by_name['customer_id']._options = None
  _MUTATECUSTOMERCLIENTLINKREQUEST.fields_by_name['customer_id']._serialized_options = b'\342A\001\002'
  _MUTATECUSTOMERCLIENTLINKREQUEST.fields_by_name['operation']._options = None
  _MUTATECUSTOMERCLIENTLINKREQUEST.fields_by_name['operation']._serialized_options = b'\342A\001\002'
  _CUSTOMERCLIENTLINKSERVICE._options = None
  _CUSTOMERCLIENTLINKSERVICE._serialized_options = b'\312A\030googleads.googleapis.com\322A\'https://www.googleapis.com/auth/adwords'
  _CUSTOMERCLIENTLINKSERVICE.methods_by_name['GetCustomerClientLink']._options = None
  _CUSTOMERCLIENTLINKSERVICE.methods_by_name['GetCustomerClientLink']._serialized_options = b'\332A\rresource_name\202\323\344\223\0027\0225/v7/{resource_name=customers/*/customerClientLinks/*}'
  _CUSTOMERCLIENTLINKSERVICE.methods_by_name['MutateCustomerClientLink']._options = None
  _CUSTOMERCLIENTLINKSERVICE.methods_by_name['MutateCustomerClientLink']._serialized_options = b'\332A\025customer_id,operation\202\323\344\223\002=\"8/v7/customers/{customer_id=*}/customerClientLinks:mutate:\001*'
  _GETCUSTOMERCLIENTLINKREQUEST._serialized_start=316
  _GETCUSTOMERCLIENTLINKREQUEST._serialized_end=437
  _MUTATECUSTOMERCLIENTLINKREQUEST._serialized_start=440
  _MUTATECUSTOMERCLIENTLINKREQUEST._serialized_end=648
  _CUSTOMERCLIENTLINKOPERATION._serialized_start=651
  _CUSTOMERCLIENTLINKOPERATION._serialized_end=916
  _MUTATECUSTOMERCLIENTLINKRESPONSE._serialized_start=918
  _MUTATECUSTOMERCLIENTLINKRESPONSE._serialized_end=1042
  _MUTATECUSTOMERCLIENTLINKRESULT._serialized_start=1044
  _MUTATECUSTOMERCLIENTLINKRESULT._serialized_end=1113
  _CUSTOMERCLIENTLINKSERVICE._serialized_start=1116
  _CUSTOMERCLIENTLINKSERVICE._serialized_end=1695
# @@protoc_insertion_point(module_scope)
