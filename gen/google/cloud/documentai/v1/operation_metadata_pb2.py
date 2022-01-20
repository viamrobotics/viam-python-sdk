# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/documentai/v1/operation_metadata.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3google/cloud/documentai/v1/operation_metadata.proto\x12\x1agoogle.cloud.documentai.v1\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1cgoogle/api/annotations.proto\"\xf0\x02\n\x17\x43ommonOperationMetadata\x12O\n\x05state\x18\x01 \x01(\x0e\x32\x39.google.cloud.documentai.v1.CommonOperationMetadata.StateR\x05state\x12#\n\rstate_message\x18\x02 \x01(\tR\x0cstateMessage\x12;\n\x0b\x63reate_time\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\ncreateTime\x12;\n\x0bupdate_time\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\nupdateTime\"e\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0b\n\x07RUNNING\x10\x01\x12\x0e\n\nCANCELLING\x10\x02\x12\r\n\tSUCCEEDED\x10\x03\x12\n\n\x06\x46\x41ILED\x10\x04\x12\r\n\tCANCELLED\x10\x05\x42\xda\x01\n\x1e\x63om.google.cloud.documentai.v1B\x16OperationMetadataProtoP\x01ZDgoogle.golang.org/genproto/googleapis/cloud/documentai/v1;documentai\xaa\x02\x1aGoogle.Cloud.DocumentAI.V1\xca\x02\x1aGoogle\\Cloud\\DocumentAI\\V1\xea\x02\x1dGoogle::Cloud::DocumentAI::V1b\x06proto3')



_COMMONOPERATIONMETADATA = DESCRIPTOR.message_types_by_name['CommonOperationMetadata']
_COMMONOPERATIONMETADATA_STATE = _COMMONOPERATIONMETADATA.enum_types_by_name['State']
CommonOperationMetadata = _reflection.GeneratedProtocolMessageType('CommonOperationMetadata', (_message.Message,), {
  'DESCRIPTOR' : _COMMONOPERATIONMETADATA,
  '__module__' : 'google.cloud.documentai.v1.operation_metadata_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.documentai.v1.CommonOperationMetadata)
  })
_sym_db.RegisterMessage(CommonOperationMetadata)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\036com.google.cloud.documentai.v1B\026OperationMetadataProtoP\001ZDgoogle.golang.org/genproto/googleapis/cloud/documentai/v1;documentai\252\002\032Google.Cloud.DocumentAI.V1\312\002\032Google\\Cloud\\DocumentAI\\V1\352\002\035Google::Cloud::DocumentAI::V1'
  _COMMONOPERATIONMETADATA._serialized_start=147
  _COMMONOPERATIONMETADATA._serialized_end=515
  _COMMONOPERATIONMETADATA_STATE._serialized_start=414
  _COMMONOPERATIONMETADATA_STATE._serialized_end=515
# @@protoc_insertion_point(module_scope)
