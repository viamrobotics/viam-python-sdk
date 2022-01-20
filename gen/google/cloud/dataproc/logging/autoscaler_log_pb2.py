# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/dataproc/logging/autoscaler_log.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2google/cloud/dataproc/logging/autoscaler_log.proto\x12\x1dgoogle.cloud.dataproc.logging\x1a\x1egoogle/protobuf/duration.proto\"u\n\x0b\x43lusterSize\x12\x30\n\x14primary_worker_count\x18\x01 \x01(\x05R\x12primaryWorkerCount\x12\x34\n\x16secondary_worker_count\x18\x02 \x01(\x05R\x14secondaryWorkerCount\"\xb9\x01\n\rAutoscalerLog\x12G\n\x06status\x18\x01 \x01(\x0b\x32/.google.cloud.dataproc.logging.AutoscalerStatusR\x06status\x12_\n\x0erecommendation\x18\x02 \x01(\x0b\x32\x37.google.cloud.dataproc.logging.AutoscalerRecommendationR\x0erecommendation\"\xc7\x01\n\x10\x41utoscalerStatus\x12\x44\n\x05state\x18\x01 \x01(\x0e\x32..google.cloud.dataproc.logging.AutoscalerStateR\x05state\x12\x18\n\x07\x64\x65tails\x18\x02 \x01(\tR\x07\x64\x65tails\x12=\n\x1bupdate_cluster_operation_id\x18\x03 \x01(\tR\x18updateClusterOperationId\x12\x14\n\x05\x65rror\x18\x04 \x01(\tR\x05\x65rror\"\xa4\t\n\x18\x41utoscalerRecommendation\x12V\n\x06inputs\x18\x01 \x01(\x0b\x32>.google.cloud.dataproc.logging.AutoscalerRecommendation.InputsR\x06inputs\x12Y\n\x07outputs\x18\x02 \x01(\x0b\x32?.google.cloud.dataproc.logging.AutoscalerRecommendation.OutputsR\x07outputs\x1a\xd6\x03\n\x06Inputs\x12{\n\x0f\x63luster_metrics\x18\x01 \x03(\x0b\x32R.google.cloud.dataproc.logging.AutoscalerRecommendation.Inputs.ClusterMetricsEntryR\x0e\x63lusterMetrics\x12\\\n\x14\x63urrent_cluster_size\x18\x02 \x01(\x0b\x32*.google.cloud.dataproc.logging.ClusterSizeR\x12\x63urrentClusterSize\x12V\n\x11min_worker_counts\x18\x03 \x01(\x0b\x32*.google.cloud.dataproc.logging.ClusterSizeR\x0fminWorkerCounts\x12V\n\x11max_worker_counts\x18\x04 \x01(\x0b\x32*.google.cloud.dataproc.logging.ClusterSizeR\x0fmaxWorkerCounts\x1a\x41\n\x13\x43lusterMetricsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01\x1a\xfb\x03\n\x07Outputs\x12N\n\x08\x64\x65\x63ision\x18\x01 \x01(\x0e\x32\x32.google.cloud.dataproc.logging.ScalingDecisionTypeR\x08\x64\x65\x63ision\x12\x64\n\x18recommended_cluster_size\x18\x02 \x01(\x0b\x32*.google.cloud.dataproc.logging.ClusterSizeR\x16recommendedClusterSize\x12]\n\x1dgraceful_decommission_timeout\x18\x03 \x01(\x0b\x32\x19.google.protobuf.DurationR\x1bgracefulDecommissionTimeout\x12\x62\n\x13\x63onstraints_reached\x18\x04 \x03(\x0e\x32\x31.google.cloud.dataproc.logging.ConstrainingFactorR\x12\x63onstraintsReached\x12J\n!additional_recommendation_details\x18\x05 \x03(\tR\x1f\x61\x64\x64itionalRecommendationDetails\x12+\n\x11recommendation_id\x18\x06 \x01(\tR\x10recommendationId*\x8b\x01\n\x0f\x41utoscalerState\x12 \n\x1c\x41UTOSCALER_STATE_UNSPECIFIED\x10\x00\x12\x0c\n\x08\x43OOLDOWN\x10\x01\x12\x10\n\x0cRECOMMENDING\x10\x06\x12\x0b\n\x07SCALING\x10\x02\x12\x0b\n\x07STOPPED\x10\x03\x12\n\n\x06\x46\x41ILED\x10\x04\x12\x10\n\x0cINITIALIZING\x10\x05*s\n\x13ScalingDecisionType\x12%\n!SCALING_DECISION_TYPE_UNSPECIFIED\x10\x00\x12\x0c\n\x08SCALE_UP\x10\x01\x12\x0e\n\nSCALE_DOWN\x10\x02\x12\x0c\n\x08NO_SCALE\x10\x03\x12\t\n\x05MIXED\x10\x04*\xa6\x01\n\x12\x43onstrainingFactor\x12#\n\x1f\x43ONSTRAINING_FACTOR_UNSPECIFIED\x10\x00\x12\'\n#SCALING_CAPPED_DUE_TO_LACK_OF_QUOTA\x10\x01\x12 \n\x1cREACHED_MAXIMUM_CLUSTER_SIZE\x10\x02\x12 \n\x1cREACHED_MINIMUM_CLUSTER_SIZE\x10\x03\x42k\n!com.google.cloud.dataproc.loggingP\x01ZDgoogle.golang.org/genproto/googleapis/cloud/dataproc/logging;loggingb\x06proto3')

_AUTOSCALERSTATE = DESCRIPTOR.enum_types_by_name['AutoscalerState']
AutoscalerState = enum_type_wrapper.EnumTypeWrapper(_AUTOSCALERSTATE)
_SCALINGDECISIONTYPE = DESCRIPTOR.enum_types_by_name['ScalingDecisionType']
ScalingDecisionType = enum_type_wrapper.EnumTypeWrapper(_SCALINGDECISIONTYPE)
_CONSTRAININGFACTOR = DESCRIPTOR.enum_types_by_name['ConstrainingFactor']
ConstrainingFactor = enum_type_wrapper.EnumTypeWrapper(_CONSTRAININGFACTOR)
AUTOSCALER_STATE_UNSPECIFIED = 0
COOLDOWN = 1
RECOMMENDING = 6
SCALING = 2
STOPPED = 3
FAILED = 4
INITIALIZING = 5
SCALING_DECISION_TYPE_UNSPECIFIED = 0
SCALE_UP = 1
SCALE_DOWN = 2
NO_SCALE = 3
MIXED = 4
CONSTRAINING_FACTOR_UNSPECIFIED = 0
SCALING_CAPPED_DUE_TO_LACK_OF_QUOTA = 1
REACHED_MAXIMUM_CLUSTER_SIZE = 2
REACHED_MINIMUM_CLUSTER_SIZE = 3


_CLUSTERSIZE = DESCRIPTOR.message_types_by_name['ClusterSize']
_AUTOSCALERLOG = DESCRIPTOR.message_types_by_name['AutoscalerLog']
_AUTOSCALERSTATUS = DESCRIPTOR.message_types_by_name['AutoscalerStatus']
_AUTOSCALERRECOMMENDATION = DESCRIPTOR.message_types_by_name['AutoscalerRecommendation']
_AUTOSCALERRECOMMENDATION_INPUTS = _AUTOSCALERRECOMMENDATION.nested_types_by_name['Inputs']
_AUTOSCALERRECOMMENDATION_INPUTS_CLUSTERMETRICSENTRY = _AUTOSCALERRECOMMENDATION_INPUTS.nested_types_by_name['ClusterMetricsEntry']
_AUTOSCALERRECOMMENDATION_OUTPUTS = _AUTOSCALERRECOMMENDATION.nested_types_by_name['Outputs']
ClusterSize = _reflection.GeneratedProtocolMessageType('ClusterSize', (_message.Message,), {
  'DESCRIPTOR' : _CLUSTERSIZE,
  '__module__' : 'google.cloud.dataproc.logging.autoscaler_log_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.dataproc.logging.ClusterSize)
  })
_sym_db.RegisterMessage(ClusterSize)

AutoscalerLog = _reflection.GeneratedProtocolMessageType('AutoscalerLog', (_message.Message,), {
  'DESCRIPTOR' : _AUTOSCALERLOG,
  '__module__' : 'google.cloud.dataproc.logging.autoscaler_log_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.dataproc.logging.AutoscalerLog)
  })
_sym_db.RegisterMessage(AutoscalerLog)

AutoscalerStatus = _reflection.GeneratedProtocolMessageType('AutoscalerStatus', (_message.Message,), {
  'DESCRIPTOR' : _AUTOSCALERSTATUS,
  '__module__' : 'google.cloud.dataproc.logging.autoscaler_log_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.dataproc.logging.AutoscalerStatus)
  })
_sym_db.RegisterMessage(AutoscalerStatus)

AutoscalerRecommendation = _reflection.GeneratedProtocolMessageType('AutoscalerRecommendation', (_message.Message,), {

  'Inputs' : _reflection.GeneratedProtocolMessageType('Inputs', (_message.Message,), {

    'ClusterMetricsEntry' : _reflection.GeneratedProtocolMessageType('ClusterMetricsEntry', (_message.Message,), {
      'DESCRIPTOR' : _AUTOSCALERRECOMMENDATION_INPUTS_CLUSTERMETRICSENTRY,
      '__module__' : 'google.cloud.dataproc.logging.autoscaler_log_pb2'
      # @@protoc_insertion_point(class_scope:google.cloud.dataproc.logging.AutoscalerRecommendation.Inputs.ClusterMetricsEntry)
      })
    ,
    'DESCRIPTOR' : _AUTOSCALERRECOMMENDATION_INPUTS,
    '__module__' : 'google.cloud.dataproc.logging.autoscaler_log_pb2'
    # @@protoc_insertion_point(class_scope:google.cloud.dataproc.logging.AutoscalerRecommendation.Inputs)
    })
  ,

  'Outputs' : _reflection.GeneratedProtocolMessageType('Outputs', (_message.Message,), {
    'DESCRIPTOR' : _AUTOSCALERRECOMMENDATION_OUTPUTS,
    '__module__' : 'google.cloud.dataproc.logging.autoscaler_log_pb2'
    # @@protoc_insertion_point(class_scope:google.cloud.dataproc.logging.AutoscalerRecommendation.Outputs)
    })
  ,
  'DESCRIPTOR' : _AUTOSCALERRECOMMENDATION,
  '__module__' : 'google.cloud.dataproc.logging.autoscaler_log_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.dataproc.logging.AutoscalerRecommendation)
  })
_sym_db.RegisterMessage(AutoscalerRecommendation)
_sym_db.RegisterMessage(AutoscalerRecommendation.Inputs)
_sym_db.RegisterMessage(AutoscalerRecommendation.Inputs.ClusterMetricsEntry)
_sym_db.RegisterMessage(AutoscalerRecommendation.Outputs)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n!com.google.cloud.dataproc.loggingP\001ZDgoogle.golang.org/genproto/googleapis/cloud/dataproc/logging;logging'
  _AUTOSCALERRECOMMENDATION_INPUTS_CLUSTERMETRICSENTRY._options = None
  _AUTOSCALERRECOMMENDATION_INPUTS_CLUSTERMETRICSENTRY._serialized_options = b'8\001'
  _AUTOSCALERSTATE._serialized_start=1818
  _AUTOSCALERSTATE._serialized_end=1957
  _SCALINGDECISIONTYPE._serialized_start=1959
  _SCALINGDECISIONTYPE._serialized_end=2074
  _CONSTRAININGFACTOR._serialized_start=2077
  _CONSTRAININGFACTOR._serialized_end=2243
  _CLUSTERSIZE._serialized_start=117
  _CLUSTERSIZE._serialized_end=234
  _AUTOSCALERLOG._serialized_start=237
  _AUTOSCALERLOG._serialized_end=422
  _AUTOSCALERSTATUS._serialized_start=425
  _AUTOSCALERSTATUS._serialized_end=624
  _AUTOSCALERRECOMMENDATION._serialized_start=627
  _AUTOSCALERRECOMMENDATION._serialized_end=1815
  _AUTOSCALERRECOMMENDATION_INPUTS._serialized_start=835
  _AUTOSCALERRECOMMENDATION_INPUTS._serialized_end=1305
  _AUTOSCALERRECOMMENDATION_INPUTS_CLUSTERMETRICSENTRY._serialized_start=1240
  _AUTOSCALERRECOMMENDATION_INPUTS_CLUSTERMETRICSENTRY._serialized_end=1305
  _AUTOSCALERRECOMMENDATION_OUTPUTS._serialized_start=1308
  _AUTOSCALERRECOMMENDATION_OUTPUTS._serialized_end=1815
# @@protoc_insertion_point(module_scope)
