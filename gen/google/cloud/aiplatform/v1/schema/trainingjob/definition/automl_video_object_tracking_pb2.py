# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/aiplatform/v1/schema/trainingjob/definition/automl_video_object_tracking.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n[google/cloud/aiplatform/v1/schema/trainingjob/definition/automl_video_object_tracking.proto\x12\x38google.cloud.aiplatform.v1.schema.trainingjob.definition\x1a\x1cgoogle/api/annotations.proto\"\x8e\x01\n\x19\x41utoMlVideoObjectTracking\x12q\n\x06inputs\x18\x01 \x01(\x0b\x32Y.google.cloud.aiplatform.v1.schema.trainingjob.definition.AutoMlVideoObjectTrackingInputsR\x06inputs\"\xf1\x02\n\x1f\x41utoMlVideoObjectTrackingInputs\x12\x82\x01\n\nmodel_type\x18\x01 \x01(\x0e\x32\x63.google.cloud.aiplatform.v1.schema.trainingjob.definition.AutoMlVideoObjectTrackingInputs.ModelTypeR\tmodelType\"\xc8\x01\n\tModelType\x12\x1a\n\x16MODEL_TYPE_UNSPECIFIED\x10\x00\x12\t\n\x05\x43LOUD\x10\x01\x12\x16\n\x12MOBILE_VERSATILE_1\x10\x02\x12\x1c\n\x18MOBILE_CORAL_VERSATILE_1\x10\x03\x12\x1e\n\x1aMOBILE_CORAL_LOW_LATENCY_1\x10\x04\x12\x1d\n\x19MOBILE_JETSON_VERSATILE_1\x10\x05\x12\x1f\n\x1bMOBILE_JETSON_LOW_LATENCY_1\x10\x06\x42\xfb\x02\n<com.google.cloud.aiplatform.v1.schema.trainingjob.definitionB\x1e\x41utoMLVideoObjectTrackingProtoP\x01Zbgoogle.golang.org/genproto/googleapis/cloud/aiplatform/v1/schema/trainingjob/definition;definition\xaa\x02\x38Google.Cloud.AIPlatform.V1.Schema.TrainingJob.Definition\xca\x02\x38Google\\Cloud\\AIPlatform\\V1\\Schema\\TrainingJob\\Definition\xea\x02>Google::Cloud::AIPlatform::V1::Schema::TrainingJob::Definitionb\x06proto3')



_AUTOMLVIDEOOBJECTTRACKING = DESCRIPTOR.message_types_by_name['AutoMlVideoObjectTracking']
_AUTOMLVIDEOOBJECTTRACKINGINPUTS = DESCRIPTOR.message_types_by_name['AutoMlVideoObjectTrackingInputs']
_AUTOMLVIDEOOBJECTTRACKINGINPUTS_MODELTYPE = _AUTOMLVIDEOOBJECTTRACKINGINPUTS.enum_types_by_name['ModelType']
AutoMlVideoObjectTracking = _reflection.GeneratedProtocolMessageType('AutoMlVideoObjectTracking', (_message.Message,), {
  'DESCRIPTOR' : _AUTOMLVIDEOOBJECTTRACKING,
  '__module__' : 'google.cloud.aiplatform.v1.schema.trainingjob.definition.automl_video_object_tracking_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.aiplatform.v1.schema.trainingjob.definition.AutoMlVideoObjectTracking)
  })
_sym_db.RegisterMessage(AutoMlVideoObjectTracking)

AutoMlVideoObjectTrackingInputs = _reflection.GeneratedProtocolMessageType('AutoMlVideoObjectTrackingInputs', (_message.Message,), {
  'DESCRIPTOR' : _AUTOMLVIDEOOBJECTTRACKINGINPUTS,
  '__module__' : 'google.cloud.aiplatform.v1.schema.trainingjob.definition.automl_video_object_tracking_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.aiplatform.v1.schema.trainingjob.definition.AutoMlVideoObjectTrackingInputs)
  })
_sym_db.RegisterMessage(AutoMlVideoObjectTrackingInputs)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n<com.google.cloud.aiplatform.v1.schema.trainingjob.definitionB\036AutoMLVideoObjectTrackingProtoP\001Zbgoogle.golang.org/genproto/googleapis/cloud/aiplatform/v1/schema/trainingjob/definition;definition\252\0028Google.Cloud.AIPlatform.V1.Schema.TrainingJob.Definition\312\0028Google\\Cloud\\AIPlatform\\V1\\Schema\\TrainingJob\\Definition\352\002>Google::Cloud::AIPlatform::V1::Schema::TrainingJob::Definition'
  _AUTOMLVIDEOOBJECTTRACKING._serialized_start=184
  _AUTOMLVIDEOOBJECTTRACKING._serialized_end=326
  _AUTOMLVIDEOOBJECTTRACKINGINPUTS._serialized_start=329
  _AUTOMLVIDEOOBJECTTRACKINGINPUTS._serialized_end=698
  _AUTOMLVIDEOOBJECTTRACKINGINPUTS_MODELTYPE._serialized_start=498
  _AUTOMLVIDEOOBJECTTRACKINGINPUTS_MODELTYPE._serialized_end=698
# @@protoc_insertion_point(module_scope)
