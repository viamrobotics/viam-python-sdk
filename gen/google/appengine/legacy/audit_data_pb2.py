# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/appengine/legacy/audit_data.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(google/appengine/legacy/audit_data.proto\x12\x17google.appengine.legacy\x1a\x1cgoogle/api/annotations.proto\"\xc0\x01\n\tAuditData\x12#\n\revent_message\x18\x01 \x01(\tR\x0c\x65ventMessage\x12P\n\nevent_data\x18\x02 \x03(\x0b\x32\x31.google.appengine.legacy.AuditData.EventDataEntryR\teventData\x1a<\n\x0e\x45ventDataEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01\x42n\n\x1b\x63om.google.appengine.legacyB\x0e\x41uditDataProtoP\x01Z=google.golang.org/genproto/googleapis/appengine/legacy;legacyb\x06proto3')



_AUDITDATA = DESCRIPTOR.message_types_by_name['AuditData']
_AUDITDATA_EVENTDATAENTRY = _AUDITDATA.nested_types_by_name['EventDataEntry']
AuditData = _reflection.GeneratedProtocolMessageType('AuditData', (_message.Message,), {

  'EventDataEntry' : _reflection.GeneratedProtocolMessageType('EventDataEntry', (_message.Message,), {
    'DESCRIPTOR' : _AUDITDATA_EVENTDATAENTRY,
    '__module__' : 'google.appengine.legacy.audit_data_pb2'
    # @@protoc_insertion_point(class_scope:google.appengine.legacy.AuditData.EventDataEntry)
    })
  ,
  'DESCRIPTOR' : _AUDITDATA,
  '__module__' : 'google.appengine.legacy.audit_data_pb2'
  # @@protoc_insertion_point(class_scope:google.appengine.legacy.AuditData)
  })
_sym_db.RegisterMessage(AuditData)
_sym_db.RegisterMessage(AuditData.EventDataEntry)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\033com.google.appengine.legacyB\016AuditDataProtoP\001Z=google.golang.org/genproto/googleapis/appengine/legacy;legacy'
  _AUDITDATA_EVENTDATAENTRY._options = None
  _AUDITDATA_EVENTDATAENTRY._serialized_options = b'8\001'
  _AUDITDATA._serialized_start=100
  _AUDITDATA._serialized_end=292
  _AUDITDATA_EVENTDATAENTRY._serialized_start=232
  _AUDITDATA_EVENTDATAENTRY._serialized_end=292
# @@protoc_insertion_point(module_scope)
