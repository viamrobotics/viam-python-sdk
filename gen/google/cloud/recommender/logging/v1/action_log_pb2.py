# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/recommender/logging/v1/action_log.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.cloud.recommender.v1 import insight_pb2 as google_dot_cloud_dot_recommender_dot_v1_dot_insight__pb2
from google.cloud.recommender.v1 import recommendation_pb2 as google_dot_cloud_dot_recommender_dot_v1_dot_recommendation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n4google/cloud/recommender/logging/v1/action_log.proto\x12#google.cloud.recommender.logging.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a)google/cloud/recommender/v1/insight.proto\x1a\x30google/cloud/recommender/v1/recommendation.proto\"\xd0\x02\n\tActionLog\x12\x14\n\x05\x61\x63tor\x18\x01 \x01(\tR\x05\x61\x63tor\x12P\n\x05state\x18\x02 \x01(\x0e\x32:.google.cloud.recommender.v1.RecommendationStateInfo.StateR\x05state\x12h\n\x0estate_metadata\x18\x03 \x03(\x0b\x32\x41.google.cloud.recommender.logging.v1.ActionLog.StateMetadataEntryR\rstateMetadata\x12/\n\x13recommendation_name\x18\x04 \x01(\tR\x12recommendationName\x1a@\n\x12StateMetadataEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01\"\xff\x02\n\x10InsightActionLog\x12\x1a\n\x05\x61\x63tor\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02R\x05\x61\x63tor\x12O\n\x05state\x18\x02 \x01(\x0e\x32\x33.google.cloud.recommender.v1.InsightStateInfo.StateB\x04\xe2\x41\x01\x02R\x05state\x12u\n\x0estate_metadata\x18\x03 \x03(\x0b\x32H.google.cloud.recommender.logging.v1.InsightActionLog.StateMetadataEntryB\x04\xe2\x41\x01\x01R\rstateMetadata\x12\x45\n\x07insight\x18\x04 \x01(\tB+\xe2\x41\x01\x02\xfa\x41$\n\"recommender.googleapis.com/InsightR\x07insight\x1a@\n\x12StateMetadataEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01\x42\x87\x01\n\'com.google.cloud.recommender.logging.v1B\x0e\x41\x63tionLogProtoP\x01ZJgoogle.golang.org/genproto/googleapis/cloud/recommender/logging/v1;loggingb\x06proto3')



_ACTIONLOG = DESCRIPTOR.message_types_by_name['ActionLog']
_ACTIONLOG_STATEMETADATAENTRY = _ACTIONLOG.nested_types_by_name['StateMetadataEntry']
_INSIGHTACTIONLOG = DESCRIPTOR.message_types_by_name['InsightActionLog']
_INSIGHTACTIONLOG_STATEMETADATAENTRY = _INSIGHTACTIONLOG.nested_types_by_name['StateMetadataEntry']
ActionLog = _reflection.GeneratedProtocolMessageType('ActionLog', (_message.Message,), {

  'StateMetadataEntry' : _reflection.GeneratedProtocolMessageType('StateMetadataEntry', (_message.Message,), {
    'DESCRIPTOR' : _ACTIONLOG_STATEMETADATAENTRY,
    '__module__' : 'google.cloud.recommender.logging.v1.action_log_pb2'
    # @@protoc_insertion_point(class_scope:google.cloud.recommender.logging.v1.ActionLog.StateMetadataEntry)
    })
  ,
  'DESCRIPTOR' : _ACTIONLOG,
  '__module__' : 'google.cloud.recommender.logging.v1.action_log_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.recommender.logging.v1.ActionLog)
  })
_sym_db.RegisterMessage(ActionLog)
_sym_db.RegisterMessage(ActionLog.StateMetadataEntry)

InsightActionLog = _reflection.GeneratedProtocolMessageType('InsightActionLog', (_message.Message,), {

  'StateMetadataEntry' : _reflection.GeneratedProtocolMessageType('StateMetadataEntry', (_message.Message,), {
    'DESCRIPTOR' : _INSIGHTACTIONLOG_STATEMETADATAENTRY,
    '__module__' : 'google.cloud.recommender.logging.v1.action_log_pb2'
    # @@protoc_insertion_point(class_scope:google.cloud.recommender.logging.v1.InsightActionLog.StateMetadataEntry)
    })
  ,
  'DESCRIPTOR' : _INSIGHTACTIONLOG,
  '__module__' : 'google.cloud.recommender.logging.v1.action_log_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.recommender.logging.v1.InsightActionLog)
  })
_sym_db.RegisterMessage(InsightActionLog)
_sym_db.RegisterMessage(InsightActionLog.StateMetadataEntry)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\'com.google.cloud.recommender.logging.v1B\016ActionLogProtoP\001ZJgoogle.golang.org/genproto/googleapis/cloud/recommender/logging/v1;logging'
  _ACTIONLOG_STATEMETADATAENTRY._options = None
  _ACTIONLOG_STATEMETADATAENTRY._serialized_options = b'8\001'
  _INSIGHTACTIONLOG_STATEMETADATAENTRY._options = None
  _INSIGHTACTIONLOG_STATEMETADATAENTRY._serialized_options = b'8\001'
  _INSIGHTACTIONLOG.fields_by_name['actor']._options = None
  _INSIGHTACTIONLOG.fields_by_name['actor']._serialized_options = b'\342A\001\002'
  _INSIGHTACTIONLOG.fields_by_name['state']._options = None
  _INSIGHTACTIONLOG.fields_by_name['state']._serialized_options = b'\342A\001\002'
  _INSIGHTACTIONLOG.fields_by_name['state_metadata']._options = None
  _INSIGHTACTIONLOG.fields_by_name['state_metadata']._serialized_options = b'\342A\001\001'
  _INSIGHTACTIONLOG.fields_by_name['insight']._options = None
  _INSIGHTACTIONLOG.fields_by_name['insight']._serialized_options = b'\342A\001\002\372A$\n\"recommender.googleapis.com/Insight'
  _ACTIONLOG._serialized_start=247
  _ACTIONLOG._serialized_end=583
  _ACTIONLOG_STATEMETADATAENTRY._serialized_start=519
  _ACTIONLOG_STATEMETADATAENTRY._serialized_end=583
  _INSIGHTACTIONLOG._serialized_start=586
  _INSIGHTACTIONLOG._serialized_end=969
  _INSIGHTACTIONLOG_STATEMETADATAENTRY._serialized_start=519
  _INSIGHTACTIONLOG_STATEMETADATAENTRY._serialized_end=583
# @@protoc_insertion_point(module_scope)
