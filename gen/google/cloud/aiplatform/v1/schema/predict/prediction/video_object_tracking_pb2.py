# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/aiplatform/v1/schema/predict/prediction/video_object_tracking.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nPgoogle/cloud/aiplatform/v1/schema/predict/prediction/video_object_tracking.proto\x12\x34google.cloud.aiplatform.v1.schema.predict.prediction\x1a\x1egoogle/protobuf/duration.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1cgoogle/api/annotations.proto\"\xaa\x05\n#VideoObjectTrackingPredictionResult\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12!\n\x0c\x64isplay_name\x18\x02 \x01(\tR\x0b\x64isplayName\x12G\n\x12time_segment_start\x18\x03 \x01(\x0b\x32\x19.google.protobuf.DurationR\x10timeSegmentStart\x12\x43\n\x10time_segment_end\x18\x04 \x01(\x0b\x32\x19.google.protobuf.DurationR\x0etimeSegmentEnd\x12;\n\nconfidence\x18\x05 \x01(\x0b\x32\x1b.google.protobuf.FloatValueR\nconfidence\x12w\n\x06\x66rames\x18\x06 \x03(\x0b\x32_.google.cloud.aiplatform.v1.schema.predict.prediction.VideoObjectTrackingPredictionResult.FrameR\x06\x66rames\x1a\x8b\x02\n\x05\x46rame\x12:\n\x0btime_offset\x18\x01 \x01(\x0b\x32\x19.google.protobuf.DurationR\ntimeOffset\x12\x30\n\x05x_min\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.FloatValueR\x04xMin\x12\x30\n\x05x_max\x18\x03 \x01(\x0b\x32\x1b.google.protobuf.FloatValueR\x04xMax\x12\x30\n\x05y_min\x18\x04 \x01(\x0b\x32\x1b.google.protobuf.FloatValueR\x04yMin\x12\x30\n\x05y_max\x18\x05 \x01(\x0b\x32\x1b.google.protobuf.FloatValueR\x04yMaxB\xf1\x02\n8com.google.cloud.aiplatform.v1.schema.predict.predictionB(VideoObjectTrackingPredictionResultProtoP\x01Z^google.golang.org/genproto/googleapis/cloud/aiplatform/v1/schema/predict/prediction;prediction\xaa\x02\x34Google.Cloud.AIPlatform.V1.Schema.Predict.Prediction\xca\x02\x34Google\\Cloud\\AIPlatform\\V1\\Schema\\Predict\\Prediction\xea\x02:Google::Cloud::AIPlatform::V1::Schema::Predict::Predictionb\x06proto3')



_VIDEOOBJECTTRACKINGPREDICTIONRESULT = DESCRIPTOR.message_types_by_name['VideoObjectTrackingPredictionResult']
_VIDEOOBJECTTRACKINGPREDICTIONRESULT_FRAME = _VIDEOOBJECTTRACKINGPREDICTIONRESULT.nested_types_by_name['Frame']
VideoObjectTrackingPredictionResult = _reflection.GeneratedProtocolMessageType('VideoObjectTrackingPredictionResult', (_message.Message,), {

  'Frame' : _reflection.GeneratedProtocolMessageType('Frame', (_message.Message,), {
    'DESCRIPTOR' : _VIDEOOBJECTTRACKINGPREDICTIONRESULT_FRAME,
    '__module__' : 'google.cloud.aiplatform.v1.schema.predict.prediction.video_object_tracking_pb2'
    # @@protoc_insertion_point(class_scope:google.cloud.aiplatform.v1.schema.predict.prediction.VideoObjectTrackingPredictionResult.Frame)
    })
  ,
  'DESCRIPTOR' : _VIDEOOBJECTTRACKINGPREDICTIONRESULT,
  '__module__' : 'google.cloud.aiplatform.v1.schema.predict.prediction.video_object_tracking_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.aiplatform.v1.schema.predict.prediction.VideoObjectTrackingPredictionResult)
  })
_sym_db.RegisterMessage(VideoObjectTrackingPredictionResult)
_sym_db.RegisterMessage(VideoObjectTrackingPredictionResult.Frame)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n8com.google.cloud.aiplatform.v1.schema.predict.predictionB(VideoObjectTrackingPredictionResultProtoP\001Z^google.golang.org/genproto/googleapis/cloud/aiplatform/v1/schema/predict/prediction;prediction\252\0024Google.Cloud.AIPlatform.V1.Schema.Predict.Prediction\312\0024Google\\Cloud\\AIPlatform\\V1\\Schema\\Predict\\Prediction\352\002:Google::Cloud::AIPlatform::V1::Schema::Predict::Prediction'
  _VIDEOOBJECTTRACKINGPREDICTIONRESULT._serialized_start=233
  _VIDEOOBJECTTRACKINGPREDICTIONRESULT._serialized_end=915
  _VIDEOOBJECTTRACKINGPREDICTIONRESULT_FRAME._serialized_start=648
  _VIDEOOBJECTTRACKINGPREDICTIONRESULT_FRAME._serialized_end=915
# @@protoc_insertion_point(module_scope)
