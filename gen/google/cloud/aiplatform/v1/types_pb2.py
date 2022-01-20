# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/aiplatform/v1/types.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&google/cloud/aiplatform/v1/types.proto\x12\x1agoogle.cloud.aiplatform.v1\x1a\x1cgoogle/api/annotations.proto\"#\n\tBoolArray\x12\x16\n\x06values\x18\x01 \x03(\x08R\x06values\"%\n\x0b\x44oubleArray\x12\x16\n\x06values\x18\x01 \x03(\x01R\x06values\"$\n\nInt64Array\x12\x16\n\x06values\x18\x01 \x03(\x03R\x06values\"%\n\x0bStringArray\x12\x16\n\x06values\x18\x01 \x03(\tR\x06valuesB\xce\x01\n\x1e\x63om.google.cloud.aiplatform.v1B\nTypesProtoP\x01ZDgoogle.golang.org/genproto/googleapis/cloud/aiplatform/v1;aiplatform\xaa\x02\x1aGoogle.Cloud.AIPlatform.V1\xca\x02\x1aGoogle\\Cloud\\AIPlatform\\V1\xea\x02\x1dGoogle::Cloud::AIPlatform::V1b\x06proto3')



_BOOLARRAY = DESCRIPTOR.message_types_by_name['BoolArray']
_DOUBLEARRAY = DESCRIPTOR.message_types_by_name['DoubleArray']
_INT64ARRAY = DESCRIPTOR.message_types_by_name['Int64Array']
_STRINGARRAY = DESCRIPTOR.message_types_by_name['StringArray']
BoolArray = _reflection.GeneratedProtocolMessageType('BoolArray', (_message.Message,), {
  'DESCRIPTOR' : _BOOLARRAY,
  '__module__' : 'google.cloud.aiplatform.v1.types_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.aiplatform.v1.BoolArray)
  })
_sym_db.RegisterMessage(BoolArray)

DoubleArray = _reflection.GeneratedProtocolMessageType('DoubleArray', (_message.Message,), {
  'DESCRIPTOR' : _DOUBLEARRAY,
  '__module__' : 'google.cloud.aiplatform.v1.types_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.aiplatform.v1.DoubleArray)
  })
_sym_db.RegisterMessage(DoubleArray)

Int64Array = _reflection.GeneratedProtocolMessageType('Int64Array', (_message.Message,), {
  'DESCRIPTOR' : _INT64ARRAY,
  '__module__' : 'google.cloud.aiplatform.v1.types_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.aiplatform.v1.Int64Array)
  })
_sym_db.RegisterMessage(Int64Array)

StringArray = _reflection.GeneratedProtocolMessageType('StringArray', (_message.Message,), {
  'DESCRIPTOR' : _STRINGARRAY,
  '__module__' : 'google.cloud.aiplatform.v1.types_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.aiplatform.v1.StringArray)
  })
_sym_db.RegisterMessage(StringArray)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\036com.google.cloud.aiplatform.v1B\nTypesProtoP\001ZDgoogle.golang.org/genproto/googleapis/cloud/aiplatform/v1;aiplatform\252\002\032Google.Cloud.AIPlatform.V1\312\002\032Google\\Cloud\\AIPlatform\\V1\352\002\035Google::Cloud::AIPlatform::V1'
  _BOOLARRAY._serialized_start=100
  _BOOLARRAY._serialized_end=135
  _DOUBLEARRAY._serialized_start=137
  _DOUBLEARRAY._serialized_end=174
  _INT64ARRAY._serialized_start=176
  _INT64ARRAY._serialized_end=212
  _STRINGARRAY._serialized_start=214
  _STRINGARRAY._serialized_end=251
# @@protoc_insertion_point(module_scope)
