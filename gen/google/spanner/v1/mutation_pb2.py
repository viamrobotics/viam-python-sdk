# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/spanner/v1/mutation.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.spanner.v1 import keys_pb2 as google_dot_spanner_dot_v1_dot_keys__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n google/spanner/v1/mutation.proto\x12\x11google.spanner.v1\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1cgoogle/spanner/v1/keys.proto\x1a\x1cgoogle/api/annotations.proto\"\x9e\x04\n\x08Mutation\x12;\n\x06insert\x18\x01 \x01(\x0b\x32!.google.spanner.v1.Mutation.WriteH\x00R\x06insert\x12;\n\x06update\x18\x02 \x01(\x0b\x32!.google.spanner.v1.Mutation.WriteH\x00R\x06update\x12M\n\x10insert_or_update\x18\x03 \x01(\x0b\x32!.google.spanner.v1.Mutation.WriteH\x00R\x0einsertOrUpdate\x12=\n\x07replace\x18\x04 \x01(\x0b\x32!.google.spanner.v1.Mutation.WriteH\x00R\x07replace\x12<\n\x06\x64\x65lete\x18\x05 \x01(\x0b\x32\".google.spanner.v1.Mutation.DeleteH\x00R\x06\x64\x65lete\x1ak\n\x05Write\x12\x14\n\x05table\x18\x01 \x01(\tR\x05table\x12\x18\n\x07\x63olumns\x18\x02 \x03(\tR\x07\x63olumns\x12\x32\n\x06values\x18\x03 \x03(\x0b\x32\x1a.google.protobuf.ListValueR\x06values\x1aR\n\x06\x44\x65lete\x12\x14\n\x05table\x18\x01 \x01(\tR\x05table\x12\x32\n\x07key_set\x18\x02 \x01(\x0b\x32\x19.google.spanner.v1.KeySetR\x06keySetB\x0b\n\toperationB\xb3\x01\n\x15\x63om.google.spanner.v1B\rMutationProtoP\x01Z8google.golang.org/genproto/googleapis/spanner/v1;spanner\xaa\x02\x17Google.Cloud.Spanner.V1\xca\x02\x17Google\\Cloud\\Spanner\\V1\xea\x02\x1aGoogle::Cloud::Spanner::V1b\x06proto3')



_MUTATION = DESCRIPTOR.message_types_by_name['Mutation']
_MUTATION_WRITE = _MUTATION.nested_types_by_name['Write']
_MUTATION_DELETE = _MUTATION.nested_types_by_name['Delete']
Mutation = _reflection.GeneratedProtocolMessageType('Mutation', (_message.Message,), {

  'Write' : _reflection.GeneratedProtocolMessageType('Write', (_message.Message,), {
    'DESCRIPTOR' : _MUTATION_WRITE,
    '__module__' : 'google.spanner.v1.mutation_pb2'
    # @@protoc_insertion_point(class_scope:google.spanner.v1.Mutation.Write)
    })
  ,

  'Delete' : _reflection.GeneratedProtocolMessageType('Delete', (_message.Message,), {
    'DESCRIPTOR' : _MUTATION_DELETE,
    '__module__' : 'google.spanner.v1.mutation_pb2'
    # @@protoc_insertion_point(class_scope:google.spanner.v1.Mutation.Delete)
    })
  ,
  'DESCRIPTOR' : _MUTATION,
  '__module__' : 'google.spanner.v1.mutation_pb2'
  # @@protoc_insertion_point(class_scope:google.spanner.v1.Mutation)
  })
_sym_db.RegisterMessage(Mutation)
_sym_db.RegisterMessage(Mutation.Write)
_sym_db.RegisterMessage(Mutation.Delete)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\025com.google.spanner.v1B\rMutationProtoP\001Z8google.golang.org/genproto/googleapis/spanner/v1;spanner\252\002\027Google.Cloud.Spanner.V1\312\002\027Google\\Cloud\\Spanner\\V1\352\002\032Google::Cloud::Spanner::V1'
  _MUTATION._serialized_start=146
  _MUTATION._serialized_end=688
  _MUTATION_WRITE._serialized_start=484
  _MUTATION_WRITE._serialized_end=591
  _MUTATION_DELETE._serialized_start=593
  _MUTATION_DELETE._serialized_end=675
# @@protoc_insertion_point(module_scope)
