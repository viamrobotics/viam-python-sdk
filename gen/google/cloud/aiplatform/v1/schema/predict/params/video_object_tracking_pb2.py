# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/aiplatform/v1/schema/predict/params/video_object_tracking.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nLgoogle/cloud/aiplatform/v1/schema/predict/params/video_object_tracking.proto\x12\x30google.cloud.aiplatform.v1.schema.predict.params\x1a\x1cgoogle/api/annotations.proto\"\xb4\x01\n#VideoObjectTrackingPredictionParams\x12\x31\n\x14\x63onfidence_threshold\x18\x01 \x01(\x02R\x13\x63onfidenceThreshold\x12\'\n\x0fmax_predictions\x18\x02 \x01(\x05R\x0emaxPredictions\x12\x31\n\x15min_bounding_box_size\x18\x03 \x01(\x02R\x12minBoundingBoxSizeB\xd9\x02\n4com.google.cloud.aiplatform.v1.schema.predict.paramsB(VideoObjectTrackingPredictionParamsProtoP\x01ZVgoogle.golang.org/genproto/googleapis/cloud/aiplatform/v1/schema/predict/params;params\xaa\x02\x30Google.Cloud.AIPlatform.V1.Schema.Predict.Params\xca\x02\x30Google\\Cloud\\AIPlatform\\V1\\Schema\\Predict\\Params\xea\x02\x36Google::Cloud::AIPlatform::V1::Schema::Predict::Paramsb\x06proto3')



_VIDEOOBJECTTRACKINGPREDICTIONPARAMS = DESCRIPTOR.message_types_by_name['VideoObjectTrackingPredictionParams']
VideoObjectTrackingPredictionParams = _reflection.GeneratedProtocolMessageType('VideoObjectTrackingPredictionParams', (_message.Message,), {
  'DESCRIPTOR' : _VIDEOOBJECTTRACKINGPREDICTIONPARAMS,
  '__module__' : 'google.cloud.aiplatform.v1.schema.predict.params.video_object_tracking_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.aiplatform.v1.schema.predict.params.VideoObjectTrackingPredictionParams)
  })
_sym_db.RegisterMessage(VideoObjectTrackingPredictionParams)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n4com.google.cloud.aiplatform.v1.schema.predict.paramsB(VideoObjectTrackingPredictionParamsProtoP\001ZVgoogle.golang.org/genproto/googleapis/cloud/aiplatform/v1/schema/predict/params;params\252\0020Google.Cloud.AIPlatform.V1.Schema.Predict.Params\312\0020Google\\Cloud\\AIPlatform\\V1\\Schema\\Predict\\Params\352\0026Google::Cloud::AIPlatform::V1::Schema::Predict::Params'
  _VIDEOOBJECTTRACKINGPREDICTIONPARAMS._serialized_start=161
  _VIDEOOBJECTTRACKINGPREDICTIONPARAMS._serialized_end=341
# @@protoc_insertion_point(module_scope)
