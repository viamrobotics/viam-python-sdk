# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/aiplatform/v1beta1/schema/trainingjob/definition/automl_video_classification.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n_google/cloud/aiplatform/v1beta1/schema/trainingjob/definition/automl_video_classification.proto\x12=google.cloud.aiplatform.v1beta1.schema.trainingjob.definition\x1a\x1cgoogle/api/annotations.proto\"\x93\x01\n\x19\x41utoMlVideoClassification\x12v\n\x06inputs\x18\x01 \x01(\x0b\x32^.google.cloud.aiplatform.v1beta1.schema.trainingjob.definition.AutoMlVideoClassificationInputsR\x06inputs\"\x96\x02\n\x1f\x41utoMlVideoClassificationInputs\x12\x87\x01\n\nmodel_type\x18\x01 \x01(\x0e\x32h.google.cloud.aiplatform.v1beta1.schema.trainingjob.definition.AutoMlVideoClassificationInputs.ModelTypeR\tmodelType\"i\n\tModelType\x12\x1a\n\x16MODEL_TYPE_UNSPECIFIED\x10\x00\x12\t\n\x05\x43LOUD\x10\x01\x12\x16\n\x12MOBILE_VERSATILE_1\x10\x02\x12\x1d\n\x19MOBILE_JETSON_VERSATILE_1\x10\x03\x42\xce\x01\nAcom.google.cloud.aiplatform.v1beta1.schema.trainingjob.definitionB\x1e\x41utoMLVideoClassificationProtoP\x01Zggoogle.golang.org/genproto/googleapis/cloud/aiplatform/v1beta1/schema/trainingjob/definition;definitionb\x06proto3')



_AUTOMLVIDEOCLASSIFICATION = DESCRIPTOR.message_types_by_name['AutoMlVideoClassification']
_AUTOMLVIDEOCLASSIFICATIONINPUTS = DESCRIPTOR.message_types_by_name['AutoMlVideoClassificationInputs']
_AUTOMLVIDEOCLASSIFICATIONINPUTS_MODELTYPE = _AUTOMLVIDEOCLASSIFICATIONINPUTS.enum_types_by_name['ModelType']
AutoMlVideoClassification = _reflection.GeneratedProtocolMessageType('AutoMlVideoClassification', (_message.Message,), {
  'DESCRIPTOR' : _AUTOMLVIDEOCLASSIFICATION,
  '__module__' : 'google.cloud.aiplatform.v1beta1.schema.trainingjob.definition.automl_video_classification_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.aiplatform.v1beta1.schema.trainingjob.definition.AutoMlVideoClassification)
  })
_sym_db.RegisterMessage(AutoMlVideoClassification)

AutoMlVideoClassificationInputs = _reflection.GeneratedProtocolMessageType('AutoMlVideoClassificationInputs', (_message.Message,), {
  'DESCRIPTOR' : _AUTOMLVIDEOCLASSIFICATIONINPUTS,
  '__module__' : 'google.cloud.aiplatform.v1beta1.schema.trainingjob.definition.automl_video_classification_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.aiplatform.v1beta1.schema.trainingjob.definition.AutoMlVideoClassificationInputs)
  })
_sym_db.RegisterMessage(AutoMlVideoClassificationInputs)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\nAcom.google.cloud.aiplatform.v1beta1.schema.trainingjob.definitionB\036AutoMLVideoClassificationProtoP\001Zggoogle.golang.org/genproto/googleapis/cloud/aiplatform/v1beta1/schema/trainingjob/definition;definition'
  _AUTOMLVIDEOCLASSIFICATION._serialized_start=193
  _AUTOMLVIDEOCLASSIFICATION._serialized_end=340
  _AUTOMLVIDEOCLASSIFICATIONINPUTS._serialized_start=343
  _AUTOMLVIDEOCLASSIFICATIONINPUTS._serialized_end=621
  _AUTOMLVIDEOCLASSIFICATIONINPUTS_MODELTYPE._serialized_start=516
  _AUTOMLVIDEOCLASSIFICATIONINPUTS_MODELTYPE._serialized_end=621
# @@protoc_insertion_point(module_scope)
