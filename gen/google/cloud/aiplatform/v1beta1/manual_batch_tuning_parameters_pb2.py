# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/aiplatform/v1beta1/manual_batch_tuning_parameters.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nDgoogle/cloud/aiplatform/v1beta1/manual_batch_tuning_parameters.proto\x12\x1fgoogle.cloud.aiplatform.v1beta1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x1cgoogle/api/annotations.proto\"B\n\x1bManualBatchTuningParameters\x12#\n\nbatch_size\x18\x01 \x01(\x05\x42\x04\xe2\x41\x01\x05R\tbatchSizeB\xfd\x01\n#com.google.cloud.aiplatform.v1beta1B ManualBatchTuningParametersProtoP\x01ZIgoogle.golang.org/genproto/googleapis/cloud/aiplatform/v1beta1;aiplatform\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02\"Google::Cloud::AIPlatform::V1beta1b\x06proto3')



_MANUALBATCHTUNINGPARAMETERS = DESCRIPTOR.message_types_by_name['ManualBatchTuningParameters']
ManualBatchTuningParameters = _reflection.GeneratedProtocolMessageType('ManualBatchTuningParameters', (_message.Message,), {
  'DESCRIPTOR' : _MANUALBATCHTUNINGPARAMETERS,
  '__module__' : 'google.cloud.aiplatform.v1beta1.manual_batch_tuning_parameters_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.aiplatform.v1beta1.ManualBatchTuningParameters)
  })
_sym_db.RegisterMessage(ManualBatchTuningParameters)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n#com.google.cloud.aiplatform.v1beta1B ManualBatchTuningParametersProtoP\001ZIgoogle.golang.org/genproto/googleapis/cloud/aiplatform/v1beta1;aiplatform\252\002\037Google.Cloud.AIPlatform.V1Beta1\312\002\037Google\\Cloud\\AIPlatform\\V1beta1\352\002\"Google::Cloud::AIPlatform::V1beta1'
  _MANUALBATCHTUNINGPARAMETERS.fields_by_name['batch_size']._options = None
  _MANUALBATCHTUNINGPARAMETERS.fields_by_name['batch_size']._serialized_options = b'\342A\001\005'
  _MANUALBATCHTUNINGPARAMETERS._serialized_start=168
  _MANUALBATCHTUNINGPARAMETERS._serialized_end=234
# @@protoc_insertion_point(module_scope)
