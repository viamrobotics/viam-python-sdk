# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/gaming/v1/realms.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.cloud.gaming.v1 import common_pb2 as google_dot_cloud_dot_gaming_dot_v1_dot_common__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#google/cloud/gaming/v1/realms.proto\x12\x16google.cloud.gaming.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a#google/cloud/gaming/v1/common.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1cgoogle/api/annotations.proto\"\xde\x01\n\x11ListRealmsRequest\x12\x42\n\x06parent\x18\x01 \x01(\tB*\xe2\x41\x01\x02\xfa\x41#\x12!gameservices.googleapis.com/RealmR\x06parent\x12!\n\tpage_size\x18\x02 \x01(\x05\x42\x04\xe2\x41\x01\x01R\x08pageSize\x12#\n\npage_token\x18\x03 \x01(\tB\x04\xe2\x41\x01\x01R\tpageToken\x12\x1c\n\x06\x66ilter\x18\x04 \x01(\tB\x04\xe2\x41\x01\x01R\x06\x66ilter\x12\x1f\n\x08order_by\x18\x05 \x01(\tB\x04\xe2\x41\x01\x01R\x07orderBy\"\x95\x01\n\x12ListRealmsResponse\x12\x35\n\x06realms\x18\x01 \x03(\x0b\x32\x1d.google.cloud.gaming.v1.RealmR\x06realms\x12&\n\x0fnext_page_token\x18\x02 \x01(\tR\rnextPageToken\x12 \n\x0bunreachable\x18\x03 \x03(\tR\x0bunreachable\"Q\n\x0fGetRealmRequest\x12>\n\x04name\x18\x01 \x01(\tB*\xe2\x41\x01\x02\xfa\x41#\n!gameservices.googleapis.com/RealmR\x04name\"\xb4\x01\n\x12\x43reateRealmRequest\x12\x42\n\x06parent\x18\x01 \x01(\tB*\xe2\x41\x01\x02\xfa\x41#\x12!gameservices.googleapis.com/RealmR\x06parent\x12\x1f\n\x08realm_id\x18\x02 \x01(\tB\x04\xe2\x41\x01\x02R\x07realmId\x12\x39\n\x05realm\x18\x03 \x01(\x0b\x32\x1d.google.cloud.gaming.v1.RealmB\x04\xe2\x41\x01\x02R\x05realm\"T\n\x12\x44\x65leteRealmRequest\x12>\n\x04name\x18\x01 \x01(\tB*\xe2\x41\x01\x02\xfa\x41#\n!gameservices.googleapis.com/RealmR\x04name\"\x92\x01\n\x12UpdateRealmRequest\x12\x39\n\x05realm\x18\x01 \x01(\x0b\x32\x1d.google.cloud.gaming.v1.RealmB\x04\xe2\x41\x01\x02R\x05realm\x12\x41\n\x0bupdate_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskB\x04\xe2\x41\x01\x02R\nupdateMask\"\xde\x01\n\x19PreviewRealmUpdateRequest\x12\x39\n\x05realm\x18\x01 \x01(\x0b\x32\x1d.google.cloud.gaming.v1.RealmB\x04\xe2\x41\x01\x02R\x05realm\x12\x41\n\x0bupdate_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskB\x04\xe2\x41\x01\x02R\nupdateMask\x12\x43\n\x0cpreview_time\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x04\xe2\x41\x01\x01R\x0bpreviewTime\"x\n\x1aPreviewRealmUpdateResponse\x12\x12\n\x04\x65tag\x18\x02 \x01(\tR\x04\x65tag\x12\x46\n\x0ctarget_state\x18\x03 \x01(\x0b\x32#.google.cloud.gaming.v1.TargetStateR\x0btargetState\"\xd8\x03\n\x05Realm\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x41\n\x0b\x63reate_time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x04\xe2\x41\x01\x03R\ncreateTime\x12\x41\n\x0bupdate_time\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x04\xe2\x41\x01\x03R\nupdateTime\x12\x41\n\x06labels\x18\x04 \x03(\x0b\x32).google.cloud.gaming.v1.Realm.LabelsEntryR\x06labels\x12!\n\ttime_zone\x18\x06 \x01(\tB\x04\xe2\x41\x01\x02R\x08timeZone\x12\x12\n\x04\x65tag\x18\x07 \x01(\tR\x04\x65tag\x12 \n\x0b\x64\x65scription\x18\x08 \x01(\tR\x0b\x64\x65scription\x1a\x39\n\x0bLabelsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01:^\xea\x41[\n!gameservices.googleapis.com/Realm\x12\x36projects/{project}/locations/{location}/realms/{realm}B\\\n\x1a\x63om.google.cloud.gaming.v1P\x01Z<google.golang.org/genproto/googleapis/cloud/gaming/v1;gamingb\x06proto3')



_LISTREALMSREQUEST = DESCRIPTOR.message_types_by_name['ListRealmsRequest']
_LISTREALMSRESPONSE = DESCRIPTOR.message_types_by_name['ListRealmsResponse']
_GETREALMREQUEST = DESCRIPTOR.message_types_by_name['GetRealmRequest']
_CREATEREALMREQUEST = DESCRIPTOR.message_types_by_name['CreateRealmRequest']
_DELETEREALMREQUEST = DESCRIPTOR.message_types_by_name['DeleteRealmRequest']
_UPDATEREALMREQUEST = DESCRIPTOR.message_types_by_name['UpdateRealmRequest']
_PREVIEWREALMUPDATEREQUEST = DESCRIPTOR.message_types_by_name['PreviewRealmUpdateRequest']
_PREVIEWREALMUPDATERESPONSE = DESCRIPTOR.message_types_by_name['PreviewRealmUpdateResponse']
_REALM = DESCRIPTOR.message_types_by_name['Realm']
_REALM_LABELSENTRY = _REALM.nested_types_by_name['LabelsEntry']
ListRealmsRequest = _reflection.GeneratedProtocolMessageType('ListRealmsRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTREALMSREQUEST,
  '__module__' : 'google.cloud.gaming.v1.realms_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.gaming.v1.ListRealmsRequest)
  })
_sym_db.RegisterMessage(ListRealmsRequest)

ListRealmsResponse = _reflection.GeneratedProtocolMessageType('ListRealmsResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTREALMSRESPONSE,
  '__module__' : 'google.cloud.gaming.v1.realms_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.gaming.v1.ListRealmsResponse)
  })
_sym_db.RegisterMessage(ListRealmsResponse)

GetRealmRequest = _reflection.GeneratedProtocolMessageType('GetRealmRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETREALMREQUEST,
  '__module__' : 'google.cloud.gaming.v1.realms_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.gaming.v1.GetRealmRequest)
  })
_sym_db.RegisterMessage(GetRealmRequest)

CreateRealmRequest = _reflection.GeneratedProtocolMessageType('CreateRealmRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEREALMREQUEST,
  '__module__' : 'google.cloud.gaming.v1.realms_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.gaming.v1.CreateRealmRequest)
  })
_sym_db.RegisterMessage(CreateRealmRequest)

DeleteRealmRequest = _reflection.GeneratedProtocolMessageType('DeleteRealmRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETEREALMREQUEST,
  '__module__' : 'google.cloud.gaming.v1.realms_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.gaming.v1.DeleteRealmRequest)
  })
_sym_db.RegisterMessage(DeleteRealmRequest)

UpdateRealmRequest = _reflection.GeneratedProtocolMessageType('UpdateRealmRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEREALMREQUEST,
  '__module__' : 'google.cloud.gaming.v1.realms_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.gaming.v1.UpdateRealmRequest)
  })
_sym_db.RegisterMessage(UpdateRealmRequest)

PreviewRealmUpdateRequest = _reflection.GeneratedProtocolMessageType('PreviewRealmUpdateRequest', (_message.Message,), {
  'DESCRIPTOR' : _PREVIEWREALMUPDATEREQUEST,
  '__module__' : 'google.cloud.gaming.v1.realms_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.gaming.v1.PreviewRealmUpdateRequest)
  })
_sym_db.RegisterMessage(PreviewRealmUpdateRequest)

PreviewRealmUpdateResponse = _reflection.GeneratedProtocolMessageType('PreviewRealmUpdateResponse', (_message.Message,), {
  'DESCRIPTOR' : _PREVIEWREALMUPDATERESPONSE,
  '__module__' : 'google.cloud.gaming.v1.realms_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.gaming.v1.PreviewRealmUpdateResponse)
  })
_sym_db.RegisterMessage(PreviewRealmUpdateResponse)

Realm = _reflection.GeneratedProtocolMessageType('Realm', (_message.Message,), {

  'LabelsEntry' : _reflection.GeneratedProtocolMessageType('LabelsEntry', (_message.Message,), {
    'DESCRIPTOR' : _REALM_LABELSENTRY,
    '__module__' : 'google.cloud.gaming.v1.realms_pb2'
    # @@protoc_insertion_point(class_scope:google.cloud.gaming.v1.Realm.LabelsEntry)
    })
  ,
  'DESCRIPTOR' : _REALM,
  '__module__' : 'google.cloud.gaming.v1.realms_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.gaming.v1.Realm)
  })
_sym_db.RegisterMessage(Realm)
_sym_db.RegisterMessage(Realm.LabelsEntry)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\032com.google.cloud.gaming.v1P\001Z<google.golang.org/genproto/googleapis/cloud/gaming/v1;gaming'
  _LISTREALMSREQUEST.fields_by_name['parent']._options = None
  _LISTREALMSREQUEST.fields_by_name['parent']._serialized_options = b'\342A\001\002\372A#\022!gameservices.googleapis.com/Realm'
  _LISTREALMSREQUEST.fields_by_name['page_size']._options = None
  _LISTREALMSREQUEST.fields_by_name['page_size']._serialized_options = b'\342A\001\001'
  _LISTREALMSREQUEST.fields_by_name['page_token']._options = None
  _LISTREALMSREQUEST.fields_by_name['page_token']._serialized_options = b'\342A\001\001'
  _LISTREALMSREQUEST.fields_by_name['filter']._options = None
  _LISTREALMSREQUEST.fields_by_name['filter']._serialized_options = b'\342A\001\001'
  _LISTREALMSREQUEST.fields_by_name['order_by']._options = None
  _LISTREALMSREQUEST.fields_by_name['order_by']._serialized_options = b'\342A\001\001'
  _GETREALMREQUEST.fields_by_name['name']._options = None
  _GETREALMREQUEST.fields_by_name['name']._serialized_options = b'\342A\001\002\372A#\n!gameservices.googleapis.com/Realm'
  _CREATEREALMREQUEST.fields_by_name['parent']._options = None
  _CREATEREALMREQUEST.fields_by_name['parent']._serialized_options = b'\342A\001\002\372A#\022!gameservices.googleapis.com/Realm'
  _CREATEREALMREQUEST.fields_by_name['realm_id']._options = None
  _CREATEREALMREQUEST.fields_by_name['realm_id']._serialized_options = b'\342A\001\002'
  _CREATEREALMREQUEST.fields_by_name['realm']._options = None
  _CREATEREALMREQUEST.fields_by_name['realm']._serialized_options = b'\342A\001\002'
  _DELETEREALMREQUEST.fields_by_name['name']._options = None
  _DELETEREALMREQUEST.fields_by_name['name']._serialized_options = b'\342A\001\002\372A#\n!gameservices.googleapis.com/Realm'
  _UPDATEREALMREQUEST.fields_by_name['realm']._options = None
  _UPDATEREALMREQUEST.fields_by_name['realm']._serialized_options = b'\342A\001\002'
  _UPDATEREALMREQUEST.fields_by_name['update_mask']._options = None
  _UPDATEREALMREQUEST.fields_by_name['update_mask']._serialized_options = b'\342A\001\002'
  _PREVIEWREALMUPDATEREQUEST.fields_by_name['realm']._options = None
  _PREVIEWREALMUPDATEREQUEST.fields_by_name['realm']._serialized_options = b'\342A\001\002'
  _PREVIEWREALMUPDATEREQUEST.fields_by_name['update_mask']._options = None
  _PREVIEWREALMUPDATEREQUEST.fields_by_name['update_mask']._serialized_options = b'\342A\001\002'
  _PREVIEWREALMUPDATEREQUEST.fields_by_name['preview_time']._options = None
  _PREVIEWREALMUPDATEREQUEST.fields_by_name['preview_time']._serialized_options = b'\342A\001\001'
  _REALM_LABELSENTRY._options = None
  _REALM_LABELSENTRY._serialized_options = b'8\001'
  _REALM.fields_by_name['create_time']._options = None
  _REALM.fields_by_name['create_time']._serialized_options = b'\342A\001\003'
  _REALM.fields_by_name['update_time']._options = None
  _REALM.fields_by_name['update_time']._serialized_options = b'\342A\001\003'
  _REALM.fields_by_name['time_zone']._options = None
  _REALM.fields_by_name['time_zone']._serialized_options = b'\342A\001\002'
  _REALM._options = None
  _REALM._serialized_options = b'\352A[\n!gameservices.googleapis.com/Realm\0226projects/{project}/locations/{location}/realms/{realm}'
  _LISTREALMSREQUEST._serialized_start=258
  _LISTREALMSREQUEST._serialized_end=480
  _LISTREALMSRESPONSE._serialized_start=483
  _LISTREALMSRESPONSE._serialized_end=632
  _GETREALMREQUEST._serialized_start=634
  _GETREALMREQUEST._serialized_end=715
  _CREATEREALMREQUEST._serialized_start=718
  _CREATEREALMREQUEST._serialized_end=898
  _DELETEREALMREQUEST._serialized_start=900
  _DELETEREALMREQUEST._serialized_end=984
  _UPDATEREALMREQUEST._serialized_start=987
  _UPDATEREALMREQUEST._serialized_end=1133
  _PREVIEWREALMUPDATEREQUEST._serialized_start=1136
  _PREVIEWREALMUPDATEREQUEST._serialized_end=1358
  _PREVIEWREALMUPDATERESPONSE._serialized_start=1360
  _PREVIEWREALMUPDATERESPONSE._serialized_end=1480
  _REALM._serialized_start=1483
  _REALM._serialized_end=1955
  _REALM_LABELSENTRY._serialized_start=1802
  _REALM_LABELSENTRY._serialized_end=1859
# @@protoc_insertion_point(module_scope)
