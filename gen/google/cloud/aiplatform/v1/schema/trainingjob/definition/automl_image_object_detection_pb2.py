# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/aiplatform/v1/schema/trainingjob/definition/automl_image_object_detection.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\\google/cloud/aiplatform/v1/schema/trainingjob/definition/automl_image_object_detection.proto\x12\x38google.cloud.aiplatform.v1.schema.trainingjob.definition\x1a\x1cgoogle/api/annotations.proto\"\x8a\x02\n\x1a\x41utoMlImageObjectDetection\x12r\n\x06inputs\x18\x01 \x01(\x0b\x32Z.google.cloud.aiplatform.v1.schema.trainingjob.definition.AutoMlImageObjectDetectionInputsR\x06inputs\x12x\n\x08metadata\x18\x02 \x01(\x0b\x32\\.google.cloud.aiplatform.v1.schema.trainingjob.definition.AutoMlImageObjectDetectionMetadataR\x08metadata\"\xca\x03\n AutoMlImageObjectDetectionInputs\x12\x83\x01\n\nmodel_type\x18\x01 \x01(\x0e\x32\x64.google.cloud.aiplatform.v1.schema.trainingjob.definition.AutoMlImageObjectDetectionInputs.ModelTypeR\tmodelType\x12\x35\n\x17\x62udget_milli_node_hours\x18\x02 \x01(\x03R\x14\x62udgetMilliNodeHours\x12\x34\n\x16\x64isable_early_stopping\x18\x03 \x01(\x08R\x14\x64isableEarlyStopping\"\xb2\x01\n\tModelType\x12\x1a\n\x16MODEL_TYPE_UNSPECIFIED\x10\x00\x12\x19\n\x15\x43LOUD_HIGH_ACCURACY_1\x10\x01\x12\x17\n\x13\x43LOUD_LOW_LATENCY_1\x10\x02\x12\x1b\n\x17MOBILE_TF_LOW_LATENCY_1\x10\x03\x12\x19\n\x15MOBILE_TF_VERSATILE_1\x10\x04\x12\x1d\n\x19MOBILE_TF_HIGH_ACCURACY_1\x10\x05\"\xea\x02\n\"AutoMlImageObjectDetectionMetadata\x12\x31\n\x15\x63ost_milli_node_hours\x18\x01 \x01(\x03R\x12\x63ostMilliNodeHours\x12\xa7\x01\n\x16successful_stop_reason\x18\x02 \x01(\x0e\x32q.google.cloud.aiplatform.v1.schema.trainingjob.definition.AutoMlImageObjectDetectionMetadata.SuccessfulStopReasonR\x14successfulStopReason\"g\n\x14SuccessfulStopReason\x12&\n\"SUCCESSFUL_STOP_REASON_UNSPECIFIED\x10\x00\x12\x12\n\x0e\x42UDGET_REACHED\x10\x01\x12\x13\n\x0fMODEL_CONVERGED\x10\x02\x42\xfc\x02\n<com.google.cloud.aiplatform.v1.schema.trainingjob.definitionB\x1f\x41utoMLImageObjectDetectionProtoP\x01Zbgoogle.golang.org/genproto/googleapis/cloud/aiplatform/v1/schema/trainingjob/definition;definition\xaa\x02\x38Google.Cloud.AIPlatform.V1.Schema.TrainingJob.Definition\xca\x02\x38Google\\Cloud\\AIPlatform\\V1\\Schema\\TrainingJob\\Definition\xea\x02>Google::Cloud::AIPlatform::V1::Schema::TrainingJob::Definitionb\x06proto3')



_AUTOMLIMAGEOBJECTDETECTION = DESCRIPTOR.message_types_by_name['AutoMlImageObjectDetection']
_AUTOMLIMAGEOBJECTDETECTIONINPUTS = DESCRIPTOR.message_types_by_name['AutoMlImageObjectDetectionInputs']
_AUTOMLIMAGEOBJECTDETECTIONMETADATA = DESCRIPTOR.message_types_by_name['AutoMlImageObjectDetectionMetadata']
_AUTOMLIMAGEOBJECTDETECTIONINPUTS_MODELTYPE = _AUTOMLIMAGEOBJECTDETECTIONINPUTS.enum_types_by_name['ModelType']
_AUTOMLIMAGEOBJECTDETECTIONMETADATA_SUCCESSFULSTOPREASON = _AUTOMLIMAGEOBJECTDETECTIONMETADATA.enum_types_by_name['SuccessfulStopReason']
AutoMlImageObjectDetection = _reflection.GeneratedProtocolMessageType('AutoMlImageObjectDetection', (_message.Message,), {
  'DESCRIPTOR' : _AUTOMLIMAGEOBJECTDETECTION,
  '__module__' : 'google.cloud.aiplatform.v1.schema.trainingjob.definition.automl_image_object_detection_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.aiplatform.v1.schema.trainingjob.definition.AutoMlImageObjectDetection)
  })
_sym_db.RegisterMessage(AutoMlImageObjectDetection)

AutoMlImageObjectDetectionInputs = _reflection.GeneratedProtocolMessageType('AutoMlImageObjectDetectionInputs', (_message.Message,), {
  'DESCRIPTOR' : _AUTOMLIMAGEOBJECTDETECTIONINPUTS,
  '__module__' : 'google.cloud.aiplatform.v1.schema.trainingjob.definition.automl_image_object_detection_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.aiplatform.v1.schema.trainingjob.definition.AutoMlImageObjectDetectionInputs)
  })
_sym_db.RegisterMessage(AutoMlImageObjectDetectionInputs)

AutoMlImageObjectDetectionMetadata = _reflection.GeneratedProtocolMessageType('AutoMlImageObjectDetectionMetadata', (_message.Message,), {
  'DESCRIPTOR' : _AUTOMLIMAGEOBJECTDETECTIONMETADATA,
  '__module__' : 'google.cloud.aiplatform.v1.schema.trainingjob.definition.automl_image_object_detection_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.aiplatform.v1.schema.trainingjob.definition.AutoMlImageObjectDetectionMetadata)
  })
_sym_db.RegisterMessage(AutoMlImageObjectDetectionMetadata)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n<com.google.cloud.aiplatform.v1.schema.trainingjob.definitionB\037AutoMLImageObjectDetectionProtoP\001Zbgoogle.golang.org/genproto/googleapis/cloud/aiplatform/v1/schema/trainingjob/definition;definition\252\0028Google.Cloud.AIPlatform.V1.Schema.TrainingJob.Definition\312\0028Google\\Cloud\\AIPlatform\\V1\\Schema\\TrainingJob\\Definition\352\002>Google::Cloud::AIPlatform::V1::Schema::TrainingJob::Definition'
  _AUTOMLIMAGEOBJECTDETECTION._serialized_start=185
  _AUTOMLIMAGEOBJECTDETECTION._serialized_end=451
  _AUTOMLIMAGEOBJECTDETECTIONINPUTS._serialized_start=454
  _AUTOMLIMAGEOBJECTDETECTIONINPUTS._serialized_end=912
  _AUTOMLIMAGEOBJECTDETECTIONINPUTS_MODELTYPE._serialized_start=734
  _AUTOMLIMAGEOBJECTDETECTIONINPUTS_MODELTYPE._serialized_end=912
  _AUTOMLIMAGEOBJECTDETECTIONMETADATA._serialized_start=915
  _AUTOMLIMAGEOBJECTDETECTIONMETADATA._serialized_end=1277
  _AUTOMLIMAGEOBJECTDETECTIONMETADATA_SUCCESSFULSTOPREASON._serialized_start=1174
  _AUTOMLIMAGEOBJECTDETECTIONMETADATA_SUCCESSFULSTOPREASON._serialized_end=1277
# @@protoc_insertion_point(module_scope)
