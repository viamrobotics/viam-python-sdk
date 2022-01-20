# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/api/expr/v1alpha1/value.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$google/api/expr/v1alpha1/value.proto\x12\x18google.api.expr.v1alpha1\x1a\x19google/protobuf/any.proto\x1a\x1cgoogle/protobuf/struct.proto\"\xcd\x04\n\x05Value\x12;\n\nnull_value\x18\x01 \x01(\x0e\x32\x1a.google.protobuf.NullValueH\x00R\tnullValue\x12\x1f\n\nbool_value\x18\x02 \x01(\x08H\x00R\tboolValue\x12!\n\x0bint64_value\x18\x03 \x01(\x03H\x00R\nint64Value\x12#\n\x0cuint64_value\x18\x04 \x01(\x04H\x00R\x0buint64Value\x12#\n\x0c\x64ouble_value\x18\x05 \x01(\x01H\x00R\x0b\x64oubleValue\x12#\n\x0cstring_value\x18\x06 \x01(\tH\x00R\x0bstringValue\x12!\n\x0b\x62ytes_value\x18\x07 \x01(\x0cH\x00R\nbytesValue\x12\x44\n\nenum_value\x18\t \x01(\x0b\x32#.google.api.expr.v1alpha1.EnumValueH\x00R\tenumValue\x12\x39\n\x0cobject_value\x18\n \x01(\x0b\x32\x14.google.protobuf.AnyH\x00R\x0bobjectValue\x12\x41\n\tmap_value\x18\x0b \x01(\x0b\x32\".google.api.expr.v1alpha1.MapValueH\x00R\x08mapValue\x12\x44\n\nlist_value\x18\x0c \x01(\x0b\x32#.google.api.expr.v1alpha1.ListValueH\x00R\tlistValue\x12\x1f\n\ntype_value\x18\x0f \x01(\tH\x00R\ttypeValueB\x06\n\x04kind\"5\n\tEnumValue\x12\x12\n\x04type\x18\x01 \x01(\tR\x04type\x12\x14\n\x05value\x18\x02 \x01(\x05R\x05value\"D\n\tListValue\x12\x37\n\x06values\x18\x01 \x03(\x0b\x32\x1f.google.api.expr.v1alpha1.ValueR\x06values\"\xc1\x01\n\x08MapValue\x12\x42\n\x07\x65ntries\x18\x01 \x03(\x0b\x32(.google.api.expr.v1alpha1.MapValue.EntryR\x07\x65ntries\x1aq\n\x05\x45ntry\x12\x31\n\x03key\x18\x01 \x01(\x0b\x32\x1f.google.api.expr.v1alpha1.ValueR\x03key\x12\x35\n\x05value\x18\x02 \x01(\x0b\x32\x1f.google.api.expr.v1alpha1.ValueR\x05valueBm\n\x1c\x63om.google.api.expr.v1alpha1B\nValueProtoP\x01Z<google.golang.org/genproto/googleapis/api/expr/v1alpha1;expr\xf8\x01\x01\x62\x06proto3')



_VALUE = DESCRIPTOR.message_types_by_name['Value']
_ENUMVALUE = DESCRIPTOR.message_types_by_name['EnumValue']
_LISTVALUE = DESCRIPTOR.message_types_by_name['ListValue']
_MAPVALUE = DESCRIPTOR.message_types_by_name['MapValue']
_MAPVALUE_ENTRY = _MAPVALUE.nested_types_by_name['Entry']
Value = _reflection.GeneratedProtocolMessageType('Value', (_message.Message,), {
  'DESCRIPTOR' : _VALUE,
  '__module__' : 'google.api.expr.v1alpha1.value_pb2'
  # @@protoc_insertion_point(class_scope:google.api.expr.v1alpha1.Value)
  })
_sym_db.RegisterMessage(Value)

EnumValue = _reflection.GeneratedProtocolMessageType('EnumValue', (_message.Message,), {
  'DESCRIPTOR' : _ENUMVALUE,
  '__module__' : 'google.api.expr.v1alpha1.value_pb2'
  # @@protoc_insertion_point(class_scope:google.api.expr.v1alpha1.EnumValue)
  })
_sym_db.RegisterMessage(EnumValue)

ListValue = _reflection.GeneratedProtocolMessageType('ListValue', (_message.Message,), {
  'DESCRIPTOR' : _LISTVALUE,
  '__module__' : 'google.api.expr.v1alpha1.value_pb2'
  # @@protoc_insertion_point(class_scope:google.api.expr.v1alpha1.ListValue)
  })
_sym_db.RegisterMessage(ListValue)

MapValue = _reflection.GeneratedProtocolMessageType('MapValue', (_message.Message,), {

  'Entry' : _reflection.GeneratedProtocolMessageType('Entry', (_message.Message,), {
    'DESCRIPTOR' : _MAPVALUE_ENTRY,
    '__module__' : 'google.api.expr.v1alpha1.value_pb2'
    # @@protoc_insertion_point(class_scope:google.api.expr.v1alpha1.MapValue.Entry)
    })
  ,
  'DESCRIPTOR' : _MAPVALUE,
  '__module__' : 'google.api.expr.v1alpha1.value_pb2'
  # @@protoc_insertion_point(class_scope:google.api.expr.v1alpha1.MapValue)
  })
_sym_db.RegisterMessage(MapValue)
_sym_db.RegisterMessage(MapValue.Entry)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\034com.google.api.expr.v1alpha1B\nValueProtoP\001Z<google.golang.org/genproto/googleapis/api/expr/v1alpha1;expr\370\001\001'
  _VALUE._serialized_start=124
  _VALUE._serialized_end=713
  _ENUMVALUE._serialized_start=715
  _ENUMVALUE._serialized_end=768
  _LISTVALUE._serialized_start=770
  _LISTVALUE._serialized_end=838
  _MAPVALUE._serialized_start=841
  _MAPVALUE._serialized_end=1034
  _MAPVALUE_ENTRY._serialized_start=921
  _MAPVALUE_ENTRY._serialized_end=1034
# @@protoc_insertion_point(module_scope)
