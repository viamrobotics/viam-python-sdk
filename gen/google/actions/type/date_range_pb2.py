# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/actions/type/date_range.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.type import date_pb2 as google_dot_type_dot_date__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$google/actions/type/date_range.proto\x12\x13google.actions.type\x1a\x16google/type/date.proto\"Y\n\tDateRange\x12\'\n\x05start\x18\x01 \x01(\x0b\x32\x11.google.type.DateR\x05start\x12#\n\x03\x65nd\x18\x02 \x01(\x0b\x32\x11.google.type.DateR\x03\x65ndBu\n\x17\x63om.google.actions.typeB\x0e\x44\x61teRangeProtoP\x01Z@google.golang.org/genproto/googleapis/type/date_range;date_range\xa2\x02\x05\x41OGTPb\x06proto3')



_DATERANGE = DESCRIPTOR.message_types_by_name['DateRange']
DateRange = _reflection.GeneratedProtocolMessageType('DateRange', (_message.Message,), {
  'DESCRIPTOR' : _DATERANGE,
  '__module__' : 'google.actions.type.date_range_pb2'
  # @@protoc_insertion_point(class_scope:google.actions.type.DateRange)
  })
_sym_db.RegisterMessage(DateRange)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\027com.google.actions.typeB\016DateRangeProtoP\001Z@google.golang.org/genproto/googleapis/type/date_range;date_range\242\002\005AOGTP'
  _DATERANGE._serialized_start=85
  _DATERANGE._serialized_end=174
# @@protoc_insertion_point(module_scope)
