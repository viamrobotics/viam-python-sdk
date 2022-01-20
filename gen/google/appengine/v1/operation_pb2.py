# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/appengine/v1/operation.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#google/appengine/v1/operation.proto\x12\x13google.appengine.v1\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1cgoogle/api/annotations.proto\"\x8f\x03\n\x13OperationMetadataV1\x12\x16\n\x06method\x18\x01 \x01(\tR\x06method\x12;\n\x0binsert_time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\ninsertTime\x12\x35\n\x08\x65nd_time\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x07\x65ndTime\x12\x12\n\x04user\x18\x04 \x01(\tR\x04user\x12\x16\n\x06target\x18\x05 \x01(\tR\x06target\x12+\n\x11\x65phemeral_message\x18\x06 \x01(\tR\x10\x65phemeralMessage\x12\x18\n\x07warning\x18\x07 \x03(\tR\x07warning\x12\x66\n\x17\x63reate_version_metadata\x18\x08 \x01(\x0b\x32,.google.appengine.v1.CreateVersionMetadataV1H\x00R\x15\x63reateVersionMetadataB\x11\n\x0fmethod_metadata\"?\n\x17\x43reateVersionMetadataV1\x12$\n\x0e\x63loud_build_id\x18\x01 \x01(\tR\x0c\x63loudBuildIdB\xc0\x01\n\x17\x63om.google.appengine.v1B\x0eOperationProtoP\x01Z<google.golang.org/genproto/googleapis/appengine/v1;appengine\xaa\x02\x19Google.Cloud.AppEngine.V1\xca\x02\x19Google\\Cloud\\AppEngine\\V1\xea\x02\x1cGoogle::Cloud::AppEngine::V1b\x06proto3')



_OPERATIONMETADATAV1 = DESCRIPTOR.message_types_by_name['OperationMetadataV1']
_CREATEVERSIONMETADATAV1 = DESCRIPTOR.message_types_by_name['CreateVersionMetadataV1']
OperationMetadataV1 = _reflection.GeneratedProtocolMessageType('OperationMetadataV1', (_message.Message,), {
  'DESCRIPTOR' : _OPERATIONMETADATAV1,
  '__module__' : 'google.appengine.v1.operation_pb2'
  # @@protoc_insertion_point(class_scope:google.appengine.v1.OperationMetadataV1)
  })
_sym_db.RegisterMessage(OperationMetadataV1)

CreateVersionMetadataV1 = _reflection.GeneratedProtocolMessageType('CreateVersionMetadataV1', (_message.Message,), {
  'DESCRIPTOR' : _CREATEVERSIONMETADATAV1,
  '__module__' : 'google.appengine.v1.operation_pb2'
  # @@protoc_insertion_point(class_scope:google.appengine.v1.CreateVersionMetadataV1)
  })
_sym_db.RegisterMessage(CreateVersionMetadataV1)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\027com.google.appengine.v1B\016OperationProtoP\001Z<google.golang.org/genproto/googleapis/appengine/v1;appengine\252\002\031Google.Cloud.AppEngine.V1\312\002\031Google\\Cloud\\AppEngine\\V1\352\002\034Google::Cloud::AppEngine::V1'
  _OPERATIONMETADATAV1._serialized_start=156
  _OPERATIONMETADATAV1._serialized_end=555
  _CREATEVERSIONMETADATAV1._serialized_start=557
  _CREATEVERSIONMETADATAV1._serialized_end=620
# @@protoc_insertion_point(module_scope)
