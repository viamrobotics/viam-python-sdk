# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/automl/v1beta1/classification.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.cloud.automl.v1beta1 import temporal_pb2 as google_dot_cloud_dot_automl_dot_v1beta1_dot_temporal__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0google/cloud/automl/v1beta1/classification.proto\x12\x1bgoogle.cloud.automl.v1beta1\x1a*google/cloud/automl/v1beta1/temporal.proto\x1a\x1cgoogle/api/annotations.proto\"0\n\x18\x43lassificationAnnotation\x12\x14\n\x05score\x18\x01 \x01(\x02R\x05score\"\xf4\x01\n\x1dVideoClassificationAnnotation\x12\x12\n\x04type\x18\x01 \x01(\tR\x04type\x12r\n\x19\x63lassification_annotation\x18\x02 \x01(\x0b\x32\x35.google.cloud.automl.v1beta1.ClassificationAnnotationR\x18\x63lassificationAnnotation\x12K\n\x0ctime_segment\x18\x03 \x01(\x0b\x32(.google.cloud.automl.v1beta1.TimeSegmentR\x0btimeSegment\"\x99\n\n\x1f\x43lassificationEvaluationMetrics\x12\x15\n\x06\x61u_prc\x18\x01 \x01(\x02R\x05\x61uPrc\x12\"\n\x0b\x62\x61se_au_prc\x18\x02 \x01(\x02\x42\x02\x18\x01R\tbaseAuPrc\x12\x15\n\x06\x61u_roc\x18\x06 \x01(\x02R\x05\x61uRoc\x12\x19\n\x08log_loss\x18\x07 \x01(\x02R\x07logLoss\x12\x8d\x01\n\x18\x63onfidence_metrics_entry\x18\x03 \x03(\x0b\x32S.google.cloud.automl.v1beta1.ClassificationEvaluationMetrics.ConfidenceMetricsEntryR\x16\x63onfidenceMetricsEntry\x12w\n\x10\x63onfusion_matrix\x18\x04 \x01(\x0b\x32L.google.cloud.automl.v1beta1.ClassificationEvaluationMetrics.ConfusionMatrixR\x0f\x63onfusionMatrix\x12,\n\x12\x61nnotation_spec_id\x18\x05 \x03(\tR\x10\x61nnotationSpecId\x1a\xdc\x04\n\x16\x43onfidenceMetricsEntry\x12\x31\n\x14\x63onfidence_threshold\x18\x01 \x01(\x02R\x13\x63onfidenceThreshold\x12-\n\x12position_threshold\x18\x0e \x01(\x05R\x11positionThreshold\x12\x16\n\x06recall\x18\x02 \x01(\x02R\x06recall\x12\x1c\n\tprecision\x18\x03 \x01(\x02R\tprecision\x12.\n\x13\x66\x61lse_positive_rate\x18\x08 \x01(\x02R\x11\x66\x61lsePositiveRate\x12\x19\n\x08\x66\x31_score\x18\x04 \x01(\x02R\x07\x66\x31Score\x12\x1d\n\nrecall_at1\x18\x05 \x01(\x02R\trecallAt1\x12#\n\rprecision_at1\x18\x06 \x01(\x02R\x0cprecisionAt1\x12\x35\n\x17\x66\x61lse_positive_rate_at1\x18\t \x01(\x02R\x14\x66\x61lsePositiveRateAt1\x12 \n\x0c\x66\x31_score_at1\x18\x07 \x01(\x02R\nf1ScoreAt1\x12.\n\x13true_positive_count\x18\n \x01(\x03R\x11truePositiveCount\x12\x30\n\x14\x66\x61lse_positive_count\x18\x0b \x01(\x03R\x12\x66\x61lsePositiveCount\x12\x30\n\x14\x66\x61lse_negative_count\x18\x0c \x01(\x03R\x12\x66\x61lseNegativeCount\x12.\n\x13true_negative_count\x18\r \x01(\x03R\x11trueNegativeCount\x1a\xf2\x01\n\x0f\x43onfusionMatrix\x12,\n\x12\x61nnotation_spec_id\x18\x01 \x03(\tR\x10\x61nnotationSpecId\x12!\n\x0c\x64isplay_name\x18\x03 \x03(\tR\x0b\x64isplayName\x12\x62\n\x03row\x18\x02 \x03(\x0b\x32P.google.cloud.automl.v1beta1.ClassificationEvaluationMetrics.ConfusionMatrix.RowR\x03row\x1a*\n\x03Row\x12#\n\rexample_count\x18\x01 \x03(\x05R\x0c\x65xampleCount*Y\n\x12\x43lassificationType\x12#\n\x1f\x43LASSIFICATION_TYPE_UNSPECIFIED\x10\x00\x12\x0e\n\nMULTICLASS\x10\x01\x12\x0e\n\nMULTILABEL\x10\x02\x42\xb8\x01\n\x1f\x63om.google.cloud.automl.v1beta1B\x13\x43lassificationProtoZAgoogle.golang.org/genproto/googleapis/cloud/automl/v1beta1;automl\xca\x02\x1bGoogle\\Cloud\\AutoMl\\V1beta1\xea\x02\x1eGoogle::Cloud::AutoML::V1beta1b\x06proto3')

_CLASSIFICATIONTYPE = DESCRIPTOR.enum_types_by_name['ClassificationType']
ClassificationType = enum_type_wrapper.EnumTypeWrapper(_CLASSIFICATIONTYPE)
CLASSIFICATION_TYPE_UNSPECIFIED = 0
MULTICLASS = 1
MULTILABEL = 2


_CLASSIFICATIONANNOTATION = DESCRIPTOR.message_types_by_name['ClassificationAnnotation']
_VIDEOCLASSIFICATIONANNOTATION = DESCRIPTOR.message_types_by_name['VideoClassificationAnnotation']
_CLASSIFICATIONEVALUATIONMETRICS = DESCRIPTOR.message_types_by_name['ClassificationEvaluationMetrics']
_CLASSIFICATIONEVALUATIONMETRICS_CONFIDENCEMETRICSENTRY = _CLASSIFICATIONEVALUATIONMETRICS.nested_types_by_name['ConfidenceMetricsEntry']
_CLASSIFICATIONEVALUATIONMETRICS_CONFUSIONMATRIX = _CLASSIFICATIONEVALUATIONMETRICS.nested_types_by_name['ConfusionMatrix']
_CLASSIFICATIONEVALUATIONMETRICS_CONFUSIONMATRIX_ROW = _CLASSIFICATIONEVALUATIONMETRICS_CONFUSIONMATRIX.nested_types_by_name['Row']
ClassificationAnnotation = _reflection.GeneratedProtocolMessageType('ClassificationAnnotation', (_message.Message,), {
  'DESCRIPTOR' : _CLASSIFICATIONANNOTATION,
  '__module__' : 'google.cloud.automl.v1beta1.classification_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.automl.v1beta1.ClassificationAnnotation)
  })
_sym_db.RegisterMessage(ClassificationAnnotation)

VideoClassificationAnnotation = _reflection.GeneratedProtocolMessageType('VideoClassificationAnnotation', (_message.Message,), {
  'DESCRIPTOR' : _VIDEOCLASSIFICATIONANNOTATION,
  '__module__' : 'google.cloud.automl.v1beta1.classification_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.automl.v1beta1.VideoClassificationAnnotation)
  })
_sym_db.RegisterMessage(VideoClassificationAnnotation)

ClassificationEvaluationMetrics = _reflection.GeneratedProtocolMessageType('ClassificationEvaluationMetrics', (_message.Message,), {

  'ConfidenceMetricsEntry' : _reflection.GeneratedProtocolMessageType('ConfidenceMetricsEntry', (_message.Message,), {
    'DESCRIPTOR' : _CLASSIFICATIONEVALUATIONMETRICS_CONFIDENCEMETRICSENTRY,
    '__module__' : 'google.cloud.automl.v1beta1.classification_pb2'
    # @@protoc_insertion_point(class_scope:google.cloud.automl.v1beta1.ClassificationEvaluationMetrics.ConfidenceMetricsEntry)
    })
  ,

  'ConfusionMatrix' : _reflection.GeneratedProtocolMessageType('ConfusionMatrix', (_message.Message,), {

    'Row' : _reflection.GeneratedProtocolMessageType('Row', (_message.Message,), {
      'DESCRIPTOR' : _CLASSIFICATIONEVALUATIONMETRICS_CONFUSIONMATRIX_ROW,
      '__module__' : 'google.cloud.automl.v1beta1.classification_pb2'
      # @@protoc_insertion_point(class_scope:google.cloud.automl.v1beta1.ClassificationEvaluationMetrics.ConfusionMatrix.Row)
      })
    ,
    'DESCRIPTOR' : _CLASSIFICATIONEVALUATIONMETRICS_CONFUSIONMATRIX,
    '__module__' : 'google.cloud.automl.v1beta1.classification_pb2'
    # @@protoc_insertion_point(class_scope:google.cloud.automl.v1beta1.ClassificationEvaluationMetrics.ConfusionMatrix)
    })
  ,
  'DESCRIPTOR' : _CLASSIFICATIONEVALUATIONMETRICS,
  '__module__' : 'google.cloud.automl.v1beta1.classification_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.automl.v1beta1.ClassificationEvaluationMetrics)
  })
_sym_db.RegisterMessage(ClassificationEvaluationMetrics)
_sym_db.RegisterMessage(ClassificationEvaluationMetrics.ConfidenceMetricsEntry)
_sym_db.RegisterMessage(ClassificationEvaluationMetrics.ConfusionMatrix)
_sym_db.RegisterMessage(ClassificationEvaluationMetrics.ConfusionMatrix.Row)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\037com.google.cloud.automl.v1beta1B\023ClassificationProtoZAgoogle.golang.org/genproto/googleapis/cloud/automl/v1beta1;automl\312\002\033Google\\Cloud\\AutoMl\\V1beta1\352\002\036Google::Cloud::AutoML::V1beta1'
  _CLASSIFICATIONEVALUATIONMETRICS.fields_by_name['base_au_prc']._options = None
  _CLASSIFICATIONEVALUATIONMETRICS.fields_by_name['base_au_prc']._serialized_options = b'\030\001'
  _CLASSIFICATIONTYPE._serialized_start=1760
  _CLASSIFICATIONTYPE._serialized_end=1849
  _CLASSIFICATIONANNOTATION._serialized_start=155
  _CLASSIFICATIONANNOTATION._serialized_end=203
  _VIDEOCLASSIFICATIONANNOTATION._serialized_start=206
  _VIDEOCLASSIFICATIONANNOTATION._serialized_end=450
  _CLASSIFICATIONEVALUATIONMETRICS._serialized_start=453
  _CLASSIFICATIONEVALUATIONMETRICS._serialized_end=1758
  _CLASSIFICATIONEVALUATIONMETRICS_CONFIDENCEMETRICSENTRY._serialized_start=909
  _CLASSIFICATIONEVALUATIONMETRICS_CONFIDENCEMETRICSENTRY._serialized_end=1513
  _CLASSIFICATIONEVALUATIONMETRICS_CONFUSIONMATRIX._serialized_start=1516
  _CLASSIFICATIONEVALUATIONMETRICS_CONFUSIONMATRIX._serialized_end=1758
  _CLASSIFICATIONEVALUATIONMETRICS_CONFUSIONMATRIX_ROW._serialized_start=1716
  _CLASSIFICATIONEVALUATIONMETRICS_CONFUSIONMATRIX_ROW._serialized_end=1758
# @@protoc_insertion_point(module_scope)
