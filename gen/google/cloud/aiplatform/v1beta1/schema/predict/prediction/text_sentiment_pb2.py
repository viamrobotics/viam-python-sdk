# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/aiplatform/v1beta1/schema/predict/prediction/text_sentiment.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nNgoogle/cloud/aiplatform/v1beta1/schema/predict/prediction/text_sentiment.proto\x12\x39google.cloud.aiplatform.v1beta1.schema.predict.prediction\x1a\x1cgoogle/api/annotations.proto\"=\n\x1dTextSentimentPredictionResult\x12\x1c\n\tsentiment\x18\x01 \x01(\x05R\tsentimentB\xca\x01\n=com.google.cloud.aiplatform.v1beta1.schema.predict.predictionB\"TextSentimentPredictionResultProtoP\x01Zcgoogle.golang.org/genproto/googleapis/cloud/aiplatform/v1beta1/schema/predict/prediction;predictionb\x06proto3')



_TEXTSENTIMENTPREDICTIONRESULT = DESCRIPTOR.message_types_by_name['TextSentimentPredictionResult']
TextSentimentPredictionResult = _reflection.GeneratedProtocolMessageType('TextSentimentPredictionResult', (_message.Message,), {
  'DESCRIPTOR' : _TEXTSENTIMENTPREDICTIONRESULT,
  '__module__' : 'google.cloud.aiplatform.v1beta1.schema.predict.prediction.text_sentiment_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.aiplatform.v1beta1.schema.predict.prediction.TextSentimentPredictionResult)
  })
_sym_db.RegisterMessage(TextSentimentPredictionResult)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n=com.google.cloud.aiplatform.v1beta1.schema.predict.predictionB\"TextSentimentPredictionResultProtoP\001Zcgoogle.golang.org/genproto/googleapis/cloud/aiplatform/v1beta1/schema/predict/prediction;prediction'
  _TEXTSENTIMENTPREDICTIONRESULT._serialized_start=171
  _TEXTSENTIMENTPREDICTIONRESULT._serialized_end=232
# @@protoc_insertion_point(module_scope)
