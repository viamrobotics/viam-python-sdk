# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/automl/v1beta1/model_evaluation.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.cloud.automl.v1beta1 import classification_pb2 as google_dot_cloud_dot_automl_dot_v1beta1_dot_classification__pb2
from google.cloud.automl.v1beta1 import detection_pb2 as google_dot_cloud_dot_automl_dot_v1beta1_dot_detection__pb2
from google.cloud.automl.v1beta1 import regression_pb2 as google_dot_cloud_dot_automl_dot_v1beta1_dot_regression__pb2
from google.cloud.automl.v1beta1 import tables_pb2 as google_dot_cloud_dot_automl_dot_v1beta1_dot_tables__pb2
from google.cloud.automl.v1beta1 import text_extraction_pb2 as google_dot_cloud_dot_automl_dot_v1beta1_dot_text__extraction__pb2
from google.cloud.automl.v1beta1 import text_sentiment_pb2 as google_dot_cloud_dot_automl_dot_v1beta1_dot_text__sentiment__pb2
from google.cloud.automl.v1beta1 import translation_pb2 as google_dot_cloud_dot_automl_dot_v1beta1_dot_translation__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2google/cloud/automl/v1beta1/model_evaluation.proto\x12\x1bgoogle.cloud.automl.v1beta1\x1a\x19google/api/resource.proto\x1a\x30google/cloud/automl/v1beta1/classification.proto\x1a+google/cloud/automl/v1beta1/detection.proto\x1a,google/cloud/automl/v1beta1/regression.proto\x1a(google/cloud/automl/v1beta1/tables.proto\x1a\x31google/cloud/automl/v1beta1/text_extraction.proto\x1a\x30google/cloud/automl/v1beta1/text_sentiment.proto\x1a-google/cloud/automl/v1beta1/translation.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1cgoogle/api/annotations.proto\"\xe9\n\n\x0fModelEvaluation\x12\x8a\x01\n!classification_evaluation_metrics\x18\x08 \x01(\x0b\x32<.google.cloud.automl.v1beta1.ClassificationEvaluationMetricsH\x00R\x1f\x63lassificationEvaluationMetrics\x12~\n\x1dregression_evaluation_metrics\x18\x18 \x01(\x0b\x32\x38.google.cloud.automl.v1beta1.RegressionEvaluationMetricsH\x00R\x1bregressionEvaluationMetrics\x12\x81\x01\n\x1etranslation_evaluation_metrics\x18\t \x01(\x0b\x32\x39.google.cloud.automl.v1beta1.TranslationEvaluationMetricsH\x00R\x1ctranslationEvaluationMetrics\x12\x9e\x01\n)image_object_detection_evaluation_metrics\x18\x0c \x01(\x0b\x32\x42.google.cloud.automl.v1beta1.ImageObjectDetectionEvaluationMetricsH\x00R%imageObjectDetectionEvaluationMetrics\x12\x9b\x01\n(video_object_tracking_evaluation_metrics\x18\x0e \x01(\x0b\x32\x41.google.cloud.automl.v1beta1.VideoObjectTrackingEvaluationMetricsH\x00R$videoObjectTrackingEvaluationMetrics\x12\x88\x01\n!text_sentiment_evaluation_metrics\x18\x0b \x01(\x0b\x32;.google.cloud.automl.v1beta1.TextSentimentEvaluationMetricsH\x00R\x1etextSentimentEvaluationMetrics\x12\x8b\x01\n\"text_extraction_evaluation_metrics\x18\r \x01(\x0b\x32<.google.cloud.automl.v1beta1.TextExtractionEvaluationMetricsH\x00R\x1ftextExtractionEvaluationMetrics\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12,\n\x12\x61nnotation_spec_id\x18\x02 \x01(\tR\x10\x61nnotationSpecId\x12!\n\x0c\x64isplay_name\x18\x0f \x01(\tR\x0b\x64isplayName\x12;\n\x0b\x63reate_time\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\ncreateTime\x12\x36\n\x17\x65valuated_example_count\x18\x06 \x01(\x05R\x15\x65valuatedExampleCount:\x87\x01\xea\x41\x83\x01\n%automl.googleapis.com/ModelEvaluation\x12Zprojects/{project}/locations/{location}/models/{model}/modelEvaluations/{model_evaluation}B\t\n\x07metricsB\xa5\x01\n\x1f\x63om.google.cloud.automl.v1beta1P\x01ZAgoogle.golang.org/genproto/googleapis/cloud/automl/v1beta1;automl\xca\x02\x1bGoogle\\Cloud\\AutoMl\\V1beta1\xea\x02\x1eGoogle::Cloud::AutoML::V1beta1b\x06proto3')



_MODELEVALUATION = DESCRIPTOR.message_types_by_name['ModelEvaluation']
ModelEvaluation = _reflection.GeneratedProtocolMessageType('ModelEvaluation', (_message.Message,), {
  'DESCRIPTOR' : _MODELEVALUATION,
  '__module__' : 'google.cloud.automl.v1beta1.model_evaluation_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.automl.v1beta1.ModelEvaluation)
  })
_sym_db.RegisterMessage(ModelEvaluation)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\037com.google.cloud.automl.v1beta1P\001ZAgoogle.golang.org/genproto/googleapis/cloud/automl/v1beta1;automl\312\002\033Google\\Cloud\\AutoMl\\V1beta1\352\002\036Google::Cloud::AutoML::V1beta1'
  _MODELEVALUATION._options = None
  _MODELEVALUATION._serialized_options = b'\352A\203\001\n%automl.googleapis.com/ModelEvaluation\022Zprojects/{project}/locations/{location}/models/{model}/modelEvaluations/{model_evaluation}'
  _MODELEVALUATION._serialized_start=505
  _MODELEVALUATION._serialized_end=1890
# @@protoc_insertion_point(module_scope)
