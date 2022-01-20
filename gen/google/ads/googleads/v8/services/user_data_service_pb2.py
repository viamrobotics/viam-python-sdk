# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v8/services/user_data_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.googleads.v8.common import offline_user_data_pb2 as google_dot_ads_dot_googleads_dot_v8_dot_common_dot_offline__user__data__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import client_pb2 as google_dot_api_dot_client__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n8google/ads/googleads/v8/services/user_data_service.proto\x12 google.ads.googleads.v8.services\x1a\x36google/ads/googleads/v8/common/offline_user_data.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x17google/api/client.proto\"\xb1\x02\n\x15UploadUserDataRequest\x12%\n\x0b\x63ustomer_id\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02R\ncustomerId\x12Y\n\noperations\x18\x03 \x03(\x0b\x32\x33.google.ads.googleads.v8.services.UserDataOperationB\x04\xe2\x41\x01\x02R\noperations\x12\x89\x01\n!customer_match_user_list_metadata\x18\x02 \x01(\x0b\x32=.google.ads.googleads.v8.common.CustomerMatchUserListMetadataH\x00R\x1d\x63ustomerMatchUserListMetadataB\n\n\x08metadata\"\xa8\x01\n\x11UserDataOperation\x12\x42\n\x06\x63reate\x18\x01 \x01(\x0b\x32(.google.ads.googleads.v8.common.UserDataH\x00R\x06\x63reate\x12\x42\n\x06remove\x18\x02 \x01(\x0b\x32(.google.ads.googleads.v8.common.UserDataH\x00R\x06removeB\x0b\n\toperation\"\xbb\x01\n\x16UploadUserDataResponse\x12-\n\x10upload_date_time\x18\x03 \x01(\tH\x00R\x0euploadDateTime\x88\x01\x01\x12?\n\x19received_operations_count\x18\x04 \x01(\x05H\x01R\x17receivedOperationsCount\x88\x01\x01\x42\x13\n\x11_upload_date_timeB\x1c\n\x1a_received_operations_count2\x97\x02\n\x0fUserDataService\x12\xbc\x01\n\x0eUploadUserData\x12\x37.google.ads.googleads.v8.services.UploadUserDataRequest\x1a\x38.google.ads.googleads.v8.services.UploadUserDataResponse\"7\x82\xd3\xe4\x93\x02\x31\",/v8/customers/{customer_id=*}:uploadUserData:\x01*\x1a\x45\xca\x41\x18googleads.googleapis.com\xd2\x41\'https://www.googleapis.com/auth/adwordsB\xfb\x01\n$com.google.ads.googleads.v8.servicesB\x14UserDataServiceProtoP\x01ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v8/services;services\xa2\x02\x03GAA\xaa\x02 Google.Ads.GoogleAds.V8.Services\xca\x02 Google\\Ads\\GoogleAds\\V8\\Services\xea\x02$Google::Ads::GoogleAds::V8::Servicesb\x06proto3')



_UPLOADUSERDATAREQUEST = DESCRIPTOR.message_types_by_name['UploadUserDataRequest']
_USERDATAOPERATION = DESCRIPTOR.message_types_by_name['UserDataOperation']
_UPLOADUSERDATARESPONSE = DESCRIPTOR.message_types_by_name['UploadUserDataResponse']
UploadUserDataRequest = _reflection.GeneratedProtocolMessageType('UploadUserDataRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPLOADUSERDATAREQUEST,
  '__module__' : 'google.ads.googleads.v8.services.user_data_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v8.services.UploadUserDataRequest)
  })
_sym_db.RegisterMessage(UploadUserDataRequest)

UserDataOperation = _reflection.GeneratedProtocolMessageType('UserDataOperation', (_message.Message,), {
  'DESCRIPTOR' : _USERDATAOPERATION,
  '__module__' : 'google.ads.googleads.v8.services.user_data_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v8.services.UserDataOperation)
  })
_sym_db.RegisterMessage(UserDataOperation)

UploadUserDataResponse = _reflection.GeneratedProtocolMessageType('UploadUserDataResponse', (_message.Message,), {
  'DESCRIPTOR' : _UPLOADUSERDATARESPONSE,
  '__module__' : 'google.ads.googleads.v8.services.user_data_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v8.services.UploadUserDataResponse)
  })
_sym_db.RegisterMessage(UploadUserDataResponse)

_USERDATASERVICE = DESCRIPTOR.services_by_name['UserDataService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n$com.google.ads.googleads.v8.servicesB\024UserDataServiceProtoP\001ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v8/services;services\242\002\003GAA\252\002 Google.Ads.GoogleAds.V8.Services\312\002 Google\\Ads\\GoogleAds\\V8\\Services\352\002$Google::Ads::GoogleAds::V8::Services'
  _UPLOADUSERDATAREQUEST.fields_by_name['customer_id']._options = None
  _UPLOADUSERDATAREQUEST.fields_by_name['customer_id']._serialized_options = b'\342A\001\002'
  _UPLOADUSERDATAREQUEST.fields_by_name['operations']._options = None
  _UPLOADUSERDATAREQUEST.fields_by_name['operations']._serialized_options = b'\342A\001\002'
  _USERDATASERVICE._options = None
  _USERDATASERVICE._serialized_options = b'\312A\030googleads.googleapis.com\322A\'https://www.googleapis.com/auth/adwords'
  _USERDATASERVICE.methods_by_name['UploadUserData']._options = None
  _USERDATASERVICE.methods_by_name['UploadUserData']._serialized_options = b'\202\323\344\223\0021\",/v8/customers/{customer_id=*}:uploadUserData:\001*'
  _UPLOADUSERDATAREQUEST._serialized_start=239
  _UPLOADUSERDATAREQUEST._serialized_end=544
  _USERDATAOPERATION._serialized_start=547
  _USERDATAOPERATION._serialized_end=715
  _UPLOADUSERDATARESPONSE._serialized_start=718
  _UPLOADUSERDATARESPONSE._serialized_end=905
  _USERDATASERVICE._serialized_start=908
  _USERDATASERVICE._serialized_end=1187
# @@protoc_insertion_point(module_scope)
