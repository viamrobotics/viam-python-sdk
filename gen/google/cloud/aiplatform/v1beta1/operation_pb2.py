# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/aiplatform/v1beta1/operation.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/google/cloud/aiplatform/v1beta1/operation.proto\x12\x1fgoogle.cloud.aiplatform.v1beta1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x17google/rpc/status.proto\x1a\x1cgoogle/api/annotations.proto\"\xe5\x01\n\x18GenericOperationMetadata\x12\x43\n\x10partial_failures\x18\x01 \x03(\x0b\x32\x12.google.rpc.StatusB\x04\xe2\x41\x01\x03R\x0fpartialFailures\x12\x41\n\x0b\x63reate_time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x04\xe2\x41\x01\x03R\ncreateTime\x12\x41\n\x0bupdate_time\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x04\xe2\x41\x01\x03R\nupdateTime\"\x7f\n\x17\x44\x65leteOperationMetadata\x12\x64\n\x10generic_metadata\x18\x01 \x01(\x0b\x32\x39.google.cloud.aiplatform.v1beta1.GenericOperationMetadataR\x0fgenericMetadataB\xeb\x01\n#com.google.cloud.aiplatform.v1beta1B\x0eOperationProtoP\x01ZIgoogle.golang.org/genproto/googleapis/cloud/aiplatform/v1beta1;aiplatform\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02\"Google::Cloud::AIPlatform::V1beta1b\x06proto3')



_GENERICOPERATIONMETADATA = DESCRIPTOR.message_types_by_name['GenericOperationMetadata']
_DELETEOPERATIONMETADATA = DESCRIPTOR.message_types_by_name['DeleteOperationMetadata']
GenericOperationMetadata = _reflection.GeneratedProtocolMessageType('GenericOperationMetadata', (_message.Message,), {
  'DESCRIPTOR' : _GENERICOPERATIONMETADATA,
  '__module__' : 'google.cloud.aiplatform.v1beta1.operation_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.aiplatform.v1beta1.GenericOperationMetadata)
  })
_sym_db.RegisterMessage(GenericOperationMetadata)

DeleteOperationMetadata = _reflection.GeneratedProtocolMessageType('DeleteOperationMetadata', (_message.Message,), {
  'DESCRIPTOR' : _DELETEOPERATIONMETADATA,
  '__module__' : 'google.cloud.aiplatform.v1beta1.operation_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.aiplatform.v1beta1.DeleteOperationMetadata)
  })
_sym_db.RegisterMessage(DeleteOperationMetadata)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n#com.google.cloud.aiplatform.v1beta1B\016OperationProtoP\001ZIgoogle.golang.org/genproto/googleapis/cloud/aiplatform/v1beta1;aiplatform\252\002\037Google.Cloud.AIPlatform.V1Beta1\312\002\037Google\\Cloud\\AIPlatform\\V1beta1\352\002\"Google::Cloud::AIPlatform::V1beta1'
  _GENERICOPERATIONMETADATA.fields_by_name['partial_failures']._options = None
  _GENERICOPERATIONMETADATA.fields_by_name['partial_failures']._serialized_options = b'\342A\001\003'
  _GENERICOPERATIONMETADATA.fields_by_name['create_time']._options = None
  _GENERICOPERATIONMETADATA.fields_by_name['create_time']._serialized_options = b'\342A\001\003'
  _GENERICOPERATIONMETADATA.fields_by_name['update_time']._options = None
  _GENERICOPERATIONMETADATA.fields_by_name['update_time']._serialized_options = b'\342A\001\003'
  _GENERICOPERATIONMETADATA._serialized_start=206
  _GENERICOPERATIONMETADATA._serialized_end=435
  _DELETEOPERATIONMETADATA._serialized_start=437
  _DELETEOPERATIONMETADATA._serialized_end=564
# @@protoc_insertion_point(module_scope)
