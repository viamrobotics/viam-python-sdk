# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/datacatalog/v1/schema.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(google/cloud/datacatalog/v1/schema.proto\x12\x1bgoogle.cloud.datacatalog.v1\x1a\x1fgoogle/api/field_behavior.proto\"M\n\x06Schema\x12\x43\n\x07\x63olumns\x18\x02 \x03(\x0b\x32).google.cloud.datacatalog.v1.ColumnSchemaR\x07\x63olumns\"\xd9\x01\n\x0c\x43olumnSchema\x12\x1c\n\x06\x63olumn\x18\x06 \x01(\tB\x04\xe2\x41\x01\x02R\x06\x63olumn\x12\x18\n\x04type\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02R\x04type\x12&\n\x0b\x64\x65scription\x18\x02 \x01(\tB\x04\xe2\x41\x01\x01R\x0b\x64\x65scription\x12\x18\n\x04mode\x18\x03 \x01(\tB\x04\xe2\x41\x01\x01R\x04mode\x12O\n\nsubcolumns\x18\x07 \x03(\x0b\x32).google.cloud.datacatalog.v1.ColumnSchemaB\x04\xe2\x41\x01\x01R\nsubcolumnsB\xcb\x01\n\x1f\x63om.google.cloud.datacatalog.v1P\x01ZFgoogle.golang.org/genproto/googleapis/cloud/datacatalog/v1;datacatalog\xf8\x01\x01\xaa\x02\x1bGoogle.Cloud.DataCatalog.V1\xca\x02\x1bGoogle\\Cloud\\DataCatalog\\V1\xea\x02\x1eGoogle::Cloud::DataCatalog::V1b\x06proto3')



_SCHEMA = DESCRIPTOR.message_types_by_name['Schema']
_COLUMNSCHEMA = DESCRIPTOR.message_types_by_name['ColumnSchema']
Schema = _reflection.GeneratedProtocolMessageType('Schema', (_message.Message,), {
  'DESCRIPTOR' : _SCHEMA,
  '__module__' : 'google.cloud.datacatalog.v1.schema_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.datacatalog.v1.Schema)
  })
_sym_db.RegisterMessage(Schema)

ColumnSchema = _reflection.GeneratedProtocolMessageType('ColumnSchema', (_message.Message,), {
  'DESCRIPTOR' : _COLUMNSCHEMA,
  '__module__' : 'google.cloud.datacatalog.v1.schema_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.datacatalog.v1.ColumnSchema)
  })
_sym_db.RegisterMessage(ColumnSchema)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\037com.google.cloud.datacatalog.v1P\001ZFgoogle.golang.org/genproto/googleapis/cloud/datacatalog/v1;datacatalog\370\001\001\252\002\033Google.Cloud.DataCatalog.V1\312\002\033Google\\Cloud\\DataCatalog\\V1\352\002\036Google::Cloud::DataCatalog::V1'
  _COLUMNSCHEMA.fields_by_name['column']._options = None
  _COLUMNSCHEMA.fields_by_name['column']._serialized_options = b'\342A\001\002'
  _COLUMNSCHEMA.fields_by_name['type']._options = None
  _COLUMNSCHEMA.fields_by_name['type']._serialized_options = b'\342A\001\002'
  _COLUMNSCHEMA.fields_by_name['description']._options = None
  _COLUMNSCHEMA.fields_by_name['description']._serialized_options = b'\342A\001\001'
  _COLUMNSCHEMA.fields_by_name['mode']._options = None
  _COLUMNSCHEMA.fields_by_name['mode']._serialized_options = b'\342A\001\001'
  _COLUMNSCHEMA.fields_by_name['subcolumns']._options = None
  _COLUMNSCHEMA.fields_by_name['subcolumns']._serialized_options = b'\342A\001\001'
  _SCHEMA._serialized_start=106
  _SCHEMA._serialized_end=183
  _COLUMNSCHEMA._serialized_start=186
  _COLUMNSCHEMA._serialized_end=403
# @@protoc_insertion_point(module_scope)
