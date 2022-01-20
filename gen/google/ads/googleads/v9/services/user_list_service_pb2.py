# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v9/services/user_list_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.googleads.v9.resources import user_list_pb2 as google_dot_ads_dot_googleads_dot_v9_dot_resources_dot_user__list__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import client_pb2 as google_dot_api_dot_client__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n8google/ads/googleads/v9/services/user_list_service.proto\x12 google.ads.googleads.v9.services\x1a\x31google/ads/googleads/v9/resources/user_list.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a google/protobuf/field_mask.proto\x1a\x17google/rpc/status.proto\"e\n\x12GetUserListRequest\x12O\n\rresource_name\x18\x01 \x01(\tB*\xe2\x41\x01\x02\xfa\x41#\n!googleads.googleapis.com/UserListR\x0cresourceName\"\xe8\x01\n\x16MutateUserListsRequest\x12%\n\x0b\x63ustomer_id\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02R\ncustomerId\x12Y\n\noperations\x18\x02 \x03(\x0b\x32\x33.google.ads.googleads.v9.services.UserListOperationB\x04\xe2\x41\x01\x02R\noperations\x12\'\n\x0fpartial_failure\x18\x03 \x01(\x08R\x0epartialFailure\x12#\n\rvalidate_only\x18\x04 \x01(\x08R\x0cvalidateOnly\"\x85\x02\n\x11UserListOperation\x12;\n\x0bupdate_mask\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\nupdateMask\x12\x45\n\x06\x63reate\x18\x01 \x01(\x0b\x32+.google.ads.googleads.v9.resources.UserListH\x00R\x06\x63reate\x12\x45\n\x06update\x18\x02 \x01(\x0b\x32+.google.ads.googleads.v9.resources.UserListH\x00R\x06update\x12\x18\n\x06remove\x18\x03 \x01(\tH\x00R\x06removeB\x0b\n\toperation\"\xb3\x01\n\x17MutateUserListsResponse\x12\x46\n\x15partial_failure_error\x18\x03 \x01(\x0b\x32\x12.google.rpc.StatusR\x13partialFailureError\x12P\n\x07results\x18\x02 \x03(\x0b\x32\x36.google.ads.googleads.v9.services.MutateUserListResultR\x07results\";\n\x14MutateUserListResult\x12#\n\rresource_name\x18\x01 \x01(\tR\x0cresourceName2\xed\x03\n\x0fUserListService\x12\xb5\x01\n\x0bGetUserList\x12\x34.google.ads.googleads.v9.services.GetUserListRequest\x1a+.google.ads.googleads.v9.resources.UserList\"C\xda\x41\rresource_name\x82\xd3\xe4\x93\x02-\x12+/v9/{resource_name=customers/*/userLists/*}\x12\xda\x01\n\x0fMutateUserLists\x12\x38.google.ads.googleads.v9.services.MutateUserListsRequest\x1a\x39.google.ads.googleads.v9.services.MutateUserListsResponse\"R\xda\x41\x16\x63ustomer_id,operations\x82\xd3\xe4\x93\x02\x33\"./v9/customers/{customer_id=*}/userLists:mutate:\x01*\x1a\x45\xca\x41\x18googleads.googleapis.com\xd2\x41\'https://www.googleapis.com/auth/adwordsB\xfb\x01\n$com.google.ads.googleads.v9.servicesB\x14UserListServiceProtoP\x01ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v9/services;services\xa2\x02\x03GAA\xaa\x02 Google.Ads.GoogleAds.V9.Services\xca\x02 Google\\Ads\\GoogleAds\\V9\\Services\xea\x02$Google::Ads::GoogleAds::V9::Servicesb\x06proto3')



_GETUSERLISTREQUEST = DESCRIPTOR.message_types_by_name['GetUserListRequest']
_MUTATEUSERLISTSREQUEST = DESCRIPTOR.message_types_by_name['MutateUserListsRequest']
_USERLISTOPERATION = DESCRIPTOR.message_types_by_name['UserListOperation']
_MUTATEUSERLISTSRESPONSE = DESCRIPTOR.message_types_by_name['MutateUserListsResponse']
_MUTATEUSERLISTRESULT = DESCRIPTOR.message_types_by_name['MutateUserListResult']
GetUserListRequest = _reflection.GeneratedProtocolMessageType('GetUserListRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETUSERLISTREQUEST,
  '__module__' : 'google.ads.googleads.v9.services.user_list_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v9.services.GetUserListRequest)
  })
_sym_db.RegisterMessage(GetUserListRequest)

MutateUserListsRequest = _reflection.GeneratedProtocolMessageType('MutateUserListsRequest', (_message.Message,), {
  'DESCRIPTOR' : _MUTATEUSERLISTSREQUEST,
  '__module__' : 'google.ads.googleads.v9.services.user_list_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v9.services.MutateUserListsRequest)
  })
_sym_db.RegisterMessage(MutateUserListsRequest)

UserListOperation = _reflection.GeneratedProtocolMessageType('UserListOperation', (_message.Message,), {
  'DESCRIPTOR' : _USERLISTOPERATION,
  '__module__' : 'google.ads.googleads.v9.services.user_list_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v9.services.UserListOperation)
  })
_sym_db.RegisterMessage(UserListOperation)

MutateUserListsResponse = _reflection.GeneratedProtocolMessageType('MutateUserListsResponse', (_message.Message,), {
  'DESCRIPTOR' : _MUTATEUSERLISTSRESPONSE,
  '__module__' : 'google.ads.googleads.v9.services.user_list_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v9.services.MutateUserListsResponse)
  })
_sym_db.RegisterMessage(MutateUserListsResponse)

MutateUserListResult = _reflection.GeneratedProtocolMessageType('MutateUserListResult', (_message.Message,), {
  'DESCRIPTOR' : _MUTATEUSERLISTRESULT,
  '__module__' : 'google.ads.googleads.v9.services.user_list_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v9.services.MutateUserListResult)
  })
_sym_db.RegisterMessage(MutateUserListResult)

_USERLISTSERVICE = DESCRIPTOR.services_by_name['UserListService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n$com.google.ads.googleads.v9.servicesB\024UserListServiceProtoP\001ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v9/services;services\242\002\003GAA\252\002 Google.Ads.GoogleAds.V9.Services\312\002 Google\\Ads\\GoogleAds\\V9\\Services\352\002$Google::Ads::GoogleAds::V9::Services'
  _GETUSERLISTREQUEST.fields_by_name['resource_name']._options = None
  _GETUSERLISTREQUEST.fields_by_name['resource_name']._serialized_options = b'\342A\001\002\372A#\n!googleads.googleapis.com/UserList'
  _MUTATEUSERLISTSREQUEST.fields_by_name['customer_id']._options = None
  _MUTATEUSERLISTSREQUEST.fields_by_name['customer_id']._serialized_options = b'\342A\001\002'
  _MUTATEUSERLISTSREQUEST.fields_by_name['operations']._options = None
  _MUTATEUSERLISTSREQUEST.fields_by_name['operations']._serialized_options = b'\342A\001\002'
  _USERLISTSERVICE._options = None
  _USERLISTSERVICE._serialized_options = b'\312A\030googleads.googleapis.com\322A\'https://www.googleapis.com/auth/adwords'
  _USERLISTSERVICE.methods_by_name['GetUserList']._options = None
  _USERLISTSERVICE.methods_by_name['GetUserList']._serialized_options = b'\332A\rresource_name\202\323\344\223\002-\022+/v9/{resource_name=customers/*/userLists/*}'
  _USERLISTSERVICE.methods_by_name['MutateUserLists']._options = None
  _USERLISTSERVICE.methods_by_name['MutateUserLists']._serialized_options = b'\332A\026customer_id,operations\202\323\344\223\0023\"./v9/customers/{customer_id=*}/userLists:mutate:\001*'
  _GETUSERLISTREQUEST._serialized_start=319
  _GETUSERLISTREQUEST._serialized_end=420
  _MUTATEUSERLISTSREQUEST._serialized_start=423
  _MUTATEUSERLISTSREQUEST._serialized_end=655
  _USERLISTOPERATION._serialized_start=658
  _USERLISTOPERATION._serialized_end=919
  _MUTATEUSERLISTSRESPONSE._serialized_start=922
  _MUTATEUSERLISTSRESPONSE._serialized_end=1101
  _MUTATEUSERLISTRESULT._serialized_start=1103
  _MUTATEUSERLISTRESULT._serialized_end=1162
  _USERLISTSERVICE._serialized_start=1165
  _USERLISTSERVICE._serialized_end=1658
# @@protoc_insertion_point(module_scope)
