# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/aiplatform/v1beta1/schema/predict/params/image_segmentation.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nNgoogle/cloud/aiplatform/v1beta1/schema/predict/params/image_segmentation.proto\x12\x35google.cloud.aiplatform.v1beta1.schema.predict.params\x1a\x1cgoogle/api/annotations.proto\"V\n!ImageSegmentationPredictionParams\x12\x31\n\x14\x63onfidence_threshold\x18\x01 \x01(\x02R\x13\x63onfidenceThresholdB\xc2\x01\n9com.google.cloud.aiplatform.v1beta1.schema.predict.paramsB&ImageSegmentationPredictionParamsProtoP\x01Z[google.golang.org/genproto/googleapis/cloud/aiplatform/v1beta1/schema/predict/params;paramsb\x06proto3')



_IMAGESEGMENTATIONPREDICTIONPARAMS = DESCRIPTOR.message_types_by_name['ImageSegmentationPredictionParams']
ImageSegmentationPredictionParams = _reflection.GeneratedProtocolMessageType('ImageSegmentationPredictionParams', (_message.Message,), {
  'DESCRIPTOR' : _IMAGESEGMENTATIONPREDICTIONPARAMS,
  '__module__' : 'google.cloud.aiplatform.v1beta1.schema.predict.params.image_segmentation_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.aiplatform.v1beta1.schema.predict.params.ImageSegmentationPredictionParams)
  })
_sym_db.RegisterMessage(ImageSegmentationPredictionParams)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n9com.google.cloud.aiplatform.v1beta1.schema.predict.paramsB&ImageSegmentationPredictionParamsProtoP\001Z[google.golang.org/genproto/googleapis/cloud/aiplatform/v1beta1/schema/predict/params;params'
  _IMAGESEGMENTATIONPREDICTIONPARAMS._serialized_start=167
  _IMAGESEGMENTATIONPREDICTIONPARAMS._serialized_end=253
# @@protoc_insertion_point(module_scope)
