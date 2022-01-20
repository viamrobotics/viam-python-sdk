# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/aiplatform/v1beta1/deployed_model_ref.proto
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
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n8google/cloud/aiplatform/v1beta1/deployed_model_ref.proto\x12\x1fgoogle.cloud.aiplatform.v1beta1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1cgoogle/api/annotations.proto\"\x8d\x01\n\x10\x44\x65ployedModelRef\x12G\n\x08\x65ndpoint\x18\x01 \x01(\tB+\xe2\x41\x01\x05\xfa\x41$\n\"aiplatform.googleapis.com/EndpointR\x08\x65ndpoint\x12\x30\n\x11\x64\x65ployed_model_id\x18\x02 \x01(\tB\x04\xe2\x41\x01\x05R\x0f\x64\x65ployedModelIdB\xf3\x01\n#com.google.cloud.aiplatform.v1beta1B\x16\x44\x65ployedModelNameProtoP\x01ZIgoogle.golang.org/genproto/googleapis/cloud/aiplatform/v1beta1;aiplatform\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02\"Google::Cloud::AIPlatform::V1beta1b\x06proto3')



_DEPLOYEDMODELREF = DESCRIPTOR.message_types_by_name['DeployedModelRef']
DeployedModelRef = _reflection.GeneratedProtocolMessageType('DeployedModelRef', (_message.Message,), {
  'DESCRIPTOR' : _DEPLOYEDMODELREF,
  '__module__' : 'google.cloud.aiplatform.v1beta1.deployed_model_ref_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.aiplatform.v1beta1.DeployedModelRef)
  })
_sym_db.RegisterMessage(DeployedModelRef)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n#com.google.cloud.aiplatform.v1beta1B\026DeployedModelNameProtoP\001ZIgoogle.golang.org/genproto/googleapis/cloud/aiplatform/v1beta1;aiplatform\252\002\037Google.Cloud.AIPlatform.V1Beta1\312\002\037Google\\Cloud\\AIPlatform\\V1beta1\352\002\"Google::Cloud::AIPlatform::V1beta1'
  _DEPLOYEDMODELREF.fields_by_name['endpoint']._options = None
  _DEPLOYEDMODELREF.fields_by_name['endpoint']._serialized_options = b'\342A\001\005\372A$\n\"aiplatform.googleapis.com/Endpoint'
  _DEPLOYEDMODELREF.fields_by_name['deployed_model_id']._options = None
  _DEPLOYEDMODELREF.fields_by_name['deployed_model_id']._serialized_options = b'\342A\001\005'
  _DEPLOYEDMODELREF._serialized_start=184
  _DEPLOYEDMODELREF._serialized_end=325
# @@protoc_insertion_point(module_scope)
