# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/automl/v1/detection.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.cloud.automl.v1 import geometry_pb2 as google_dot_cloud_dot_automl_dot_v1_dot_geometry__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&google/cloud/automl/v1/detection.proto\x12\x16google.cloud.automl.v1\x1a\x1cgoogle/api/annotations.proto\x1a%google/cloud/automl/v1/geometry.proto\x1a\x1egoogle/protobuf/duration.proto\"\x7f\n\x1eImageObjectDetectionAnnotation\x12G\n\x0c\x62ounding_box\x18\x01 \x01(\x0b\x32$.google.cloud.automl.v1.BoundingPolyR\x0b\x62oundingBox\x12\x14\n\x05score\x18\x02 \x01(\x02R\x05score\"\x9a\x03\n\x17\x42oundingBoxMetricsEntry\x12#\n\riou_threshold\x18\x01 \x01(\x02R\x0ciouThreshold\x12\x34\n\x16mean_average_precision\x18\x02 \x01(\x02R\x14meanAveragePrecision\x12\x84\x01\n\x1a\x63onfidence_metrics_entries\x18\x03 \x03(\x0b\x32\x46.google.cloud.automl.v1.BoundingBoxMetricsEntry.ConfidenceMetricsEntryR\x18\x63onfidenceMetricsEntries\x1a\x9c\x01\n\x16\x43onfidenceMetricsEntry\x12\x31\n\x14\x63onfidence_threshold\x18\x01 \x01(\x02R\x13\x63onfidenceThreshold\x12\x16\n\x06recall\x18\x02 \x01(\x02R\x06recall\x12\x1c\n\tprecision\x18\x03 \x01(\x02R\tprecision\x12\x19\n\x08\x66\x31_score\x18\x04 \x01(\x02R\x07\x66\x31Score\"\xa8\x02\n%ImageObjectDetectionEvaluationMetrics\x12?\n\x1c\x65valuated_bounding_box_count\x18\x01 \x01(\x05R\x19\x65valuatedBoundingBoxCount\x12p\n\x1c\x62ounding_box_metrics_entries\x18\x02 \x03(\x0b\x32/.google.cloud.automl.v1.BoundingBoxMetricsEntryR\x19\x62oundingBoxMetricsEntries\x12L\n#bounding_box_mean_average_precision\x18\x03 \x01(\x02R\x1f\x62oundingBoxMeanAveragePrecisionB\xaa\x01\n\x1a\x63om.google.cloud.automl.v1P\x01Z<google.golang.org/genproto/googleapis/cloud/automl/v1;automl\xaa\x02\x16Google.Cloud.AutoML.V1\xca\x02\x16Google\\Cloud\\AutoMl\\V1\xea\x02\x19Google::Cloud::AutoML::V1b\x06proto3')



_IMAGEOBJECTDETECTIONANNOTATION = DESCRIPTOR.message_types_by_name['ImageObjectDetectionAnnotation']
_BOUNDINGBOXMETRICSENTRY = DESCRIPTOR.message_types_by_name['BoundingBoxMetricsEntry']
_BOUNDINGBOXMETRICSENTRY_CONFIDENCEMETRICSENTRY = _BOUNDINGBOXMETRICSENTRY.nested_types_by_name['ConfidenceMetricsEntry']
_IMAGEOBJECTDETECTIONEVALUATIONMETRICS = DESCRIPTOR.message_types_by_name['ImageObjectDetectionEvaluationMetrics']
ImageObjectDetectionAnnotation = _reflection.GeneratedProtocolMessageType('ImageObjectDetectionAnnotation', (_message.Message,), {
  'DESCRIPTOR' : _IMAGEOBJECTDETECTIONANNOTATION,
  '__module__' : 'google.cloud.automl.v1.detection_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.automl.v1.ImageObjectDetectionAnnotation)
  })
_sym_db.RegisterMessage(ImageObjectDetectionAnnotation)

BoundingBoxMetricsEntry = _reflection.GeneratedProtocolMessageType('BoundingBoxMetricsEntry', (_message.Message,), {

  'ConfidenceMetricsEntry' : _reflection.GeneratedProtocolMessageType('ConfidenceMetricsEntry', (_message.Message,), {
    'DESCRIPTOR' : _BOUNDINGBOXMETRICSENTRY_CONFIDENCEMETRICSENTRY,
    '__module__' : 'google.cloud.automl.v1.detection_pb2'
    # @@protoc_insertion_point(class_scope:google.cloud.automl.v1.BoundingBoxMetricsEntry.ConfidenceMetricsEntry)
    })
  ,
  'DESCRIPTOR' : _BOUNDINGBOXMETRICSENTRY,
  '__module__' : 'google.cloud.automl.v1.detection_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.automl.v1.BoundingBoxMetricsEntry)
  })
_sym_db.RegisterMessage(BoundingBoxMetricsEntry)
_sym_db.RegisterMessage(BoundingBoxMetricsEntry.ConfidenceMetricsEntry)

ImageObjectDetectionEvaluationMetrics = _reflection.GeneratedProtocolMessageType('ImageObjectDetectionEvaluationMetrics', (_message.Message,), {
  'DESCRIPTOR' : _IMAGEOBJECTDETECTIONEVALUATIONMETRICS,
  '__module__' : 'google.cloud.automl.v1.detection_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.automl.v1.ImageObjectDetectionEvaluationMetrics)
  })
_sym_db.RegisterMessage(ImageObjectDetectionEvaluationMetrics)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\032com.google.cloud.automl.v1P\001Z<google.golang.org/genproto/googleapis/cloud/automl/v1;automl\252\002\026Google.Cloud.AutoML.V1\312\002\026Google\\Cloud\\AutoMl\\V1\352\002\031Google::Cloud::AutoML::V1'
  _IMAGEOBJECTDETECTIONANNOTATION._serialized_start=167
  _IMAGEOBJECTDETECTIONANNOTATION._serialized_end=294
  _BOUNDINGBOXMETRICSENTRY._serialized_start=297
  _BOUNDINGBOXMETRICSENTRY._serialized_end=707
  _BOUNDINGBOXMETRICSENTRY_CONFIDENCEMETRICSENTRY._serialized_start=551
  _BOUNDINGBOXMETRICSENTRY_CONFIDENCEMETRICSENTRY._serialized_end=707
  _IMAGEOBJECTDETECTIONEVALUATIONMETRICS._serialized_start=710
  _IMAGEOBJECTDETECTIONEVALUATIONMETRICS._serialized_end=1006
# @@protoc_insertion_point(module_scope)
