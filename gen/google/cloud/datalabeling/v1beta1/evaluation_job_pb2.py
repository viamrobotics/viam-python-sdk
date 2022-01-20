# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/datalabeling/v1beta1/evaluation_job.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.cloud.datalabeling.v1beta1 import dataset_pb2 as google_dot_cloud_dot_datalabeling_dot_v1beta1_dot_dataset__pb2
from google.cloud.datalabeling.v1beta1 import evaluation_pb2 as google_dot_cloud_dot_datalabeling_dot_v1beta1_dot_evaluation__pb2
from google.cloud.datalabeling.v1beta1 import human_annotation_config_pb2 as google_dot_cloud_dot_datalabeling_dot_v1beta1_dot_human__annotation__config__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n6google/cloud/datalabeling/v1beta1/evaluation_job.proto\x12!google.cloud.datalabeling.v1beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x19google/api/resource.proto\x1a/google/cloud/datalabeling/v1beta1/dataset.proto\x1a\x32google/cloud/datalabeling/v1beta1/evaluation.proto\x1a?google/cloud/datalabeling/v1beta1/human_annotation_config.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x17google/rpc/status.proto\"\xeb\x05\n\rEvaluationJob\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12 \n\x0b\x64\x65scription\x18\x02 \x01(\tR\x0b\x64\x65scription\x12L\n\x05state\x18\x03 \x01(\x0e\x32\x36.google.cloud.datalabeling.v1beta1.EvaluationJob.StateR\x05state\x12\x1a\n\x08schedule\x18\x04 \x01(\tR\x08schedule\x12#\n\rmodel_version\x18\x05 \x01(\tR\x0cmodelVersion\x12j\n\x15\x65valuation_job_config\x18\x06 \x01(\x0b\x32\x36.google.cloud.datalabeling.v1beta1.EvaluationJobConfigR\x13\x65valuationJobConfig\x12.\n\x13\x61nnotation_spec_set\x18\x07 \x01(\tR\x11\x61nnotationSpecSet\x12;\n\x1alabel_missing_ground_truth\x18\x08 \x01(\x08R\x17labelMissingGroundTruth\x12\x46\n\x08\x61ttempts\x18\t \x03(\x0b\x32*.google.cloud.datalabeling.v1beta1.AttemptR\x08\x61ttempts\x12;\n\x0b\x63reate_time\x18\n \x01(\x0b\x32\x1a.google.protobuf.TimestampR\ncreateTime\"S\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\r\n\tSCHEDULED\x10\x01\x12\x0b\n\x07RUNNING\x10\x02\x12\n\n\x06PAUSED\x10\x03\x12\x0b\n\x07STOPPED\x10\x04:b\xea\x41_\n)datalabeling.googleapis.com/EvaluationJob\x12\x32projects/{project}/evaluationJobs/{evaluation_job}\"\xee\x08\n\x13\x45valuationJobConfig\x12~\n\x1bimage_classification_config\x18\x04 \x01(\x0b\x32<.google.cloud.datalabeling.v1beta1.ImageClassificationConfigH\x00R\x19imageClassificationConfig\x12i\n\x14\x62ounding_poly_config\x18\x05 \x01(\x0b\x32\x35.google.cloud.datalabeling.v1beta1.BoundingPolyConfigH\x00R\x12\x62oundingPolyConfig\x12{\n\x1atext_classification_config\x18\x08 \x01(\x0b\x32;.google.cloud.datalabeling.v1beta1.TextClassificationConfigH\x00R\x18textClassificationConfig\x12Q\n\x0cinput_config\x18\x01 \x01(\x0b\x32..google.cloud.datalabeling.v1beta1.InputConfigR\x0binputConfig\x12`\n\x11\x65valuation_config\x18\x02 \x01(\x0b\x32\x33.google.cloud.datalabeling.v1beta1.EvaluationConfigR\x10\x65valuationConfig\x12p\n\x17human_annotation_config\x18\x03 \x01(\x0b\x32\x38.google.cloud.datalabeling.v1beta1.HumanAnnotationConfigR\x15humanAnnotationConfig\x12\x80\x01\n\x14\x62igquery_import_keys\x18\t \x03(\x0b\x32N.google.cloud.datalabeling.v1beta1.EvaluationJobConfig.BigqueryImportKeysEntryR\x12\x62igqueryImportKeys\x12#\n\rexample_count\x18\n \x01(\x05R\x0c\x65xampleCount\x12:\n\x19\x65xample_sample_percentage\x18\x0b \x01(\x01R\x17\x65xampleSamplePercentage\x12z\n\x1b\x65valuation_job_alert_config\x18\r \x01(\x0b\x32;.google.cloud.datalabeling.v1beta1.EvaluationJobAlertConfigR\x18\x65valuationJobAlertConfig\x1a\x45\n\x17\x42igqueryImportKeysEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01\x42!\n\x1fhuman_annotation_request_config\"\x82\x01\n\x18\x45valuationJobAlertConfig\x12\x14\n\x05\x65mail\x18\x01 \x01(\tR\x05\x65mail\x12P\n%min_acceptable_mean_average_precision\x18\x02 \x01(\x01R!minAcceptableMeanAveragePrecision\"\x87\x01\n\x07\x41ttempt\x12=\n\x0c\x61ttempt_time\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x0b\x61ttemptTime\x12=\n\x10partial_failures\x18\x02 \x03(\x0b\x32\x12.google.rpc.StatusR\x0fpartialFailuresB\xe7\x01\n%com.google.cloud.datalabeling.v1beta1P\x01ZMgoogle.golang.org/genproto/googleapis/cloud/datalabeling/v1beta1;datalabeling\xaa\x02!Google.Cloud.DataLabeling.V1Beta1\xca\x02!Google\\Cloud\\DataLabeling\\V1beta1\xea\x02$Google::Cloud::DataLabeling::V1beta1b\x06proto3')



_EVALUATIONJOB = DESCRIPTOR.message_types_by_name['EvaluationJob']
_EVALUATIONJOBCONFIG = DESCRIPTOR.message_types_by_name['EvaluationJobConfig']
_EVALUATIONJOBCONFIG_BIGQUERYIMPORTKEYSENTRY = _EVALUATIONJOBCONFIG.nested_types_by_name['BigqueryImportKeysEntry']
_EVALUATIONJOBALERTCONFIG = DESCRIPTOR.message_types_by_name['EvaluationJobAlertConfig']
_ATTEMPT = DESCRIPTOR.message_types_by_name['Attempt']
_EVALUATIONJOB_STATE = _EVALUATIONJOB.enum_types_by_name['State']
EvaluationJob = _reflection.GeneratedProtocolMessageType('EvaluationJob', (_message.Message,), {
  'DESCRIPTOR' : _EVALUATIONJOB,
  '__module__' : 'google.cloud.datalabeling.v1beta1.evaluation_job_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.datalabeling.v1beta1.EvaluationJob)
  })
_sym_db.RegisterMessage(EvaluationJob)

EvaluationJobConfig = _reflection.GeneratedProtocolMessageType('EvaluationJobConfig', (_message.Message,), {

  'BigqueryImportKeysEntry' : _reflection.GeneratedProtocolMessageType('BigqueryImportKeysEntry', (_message.Message,), {
    'DESCRIPTOR' : _EVALUATIONJOBCONFIG_BIGQUERYIMPORTKEYSENTRY,
    '__module__' : 'google.cloud.datalabeling.v1beta1.evaluation_job_pb2'
    # @@protoc_insertion_point(class_scope:google.cloud.datalabeling.v1beta1.EvaluationJobConfig.BigqueryImportKeysEntry)
    })
  ,
  'DESCRIPTOR' : _EVALUATIONJOBCONFIG,
  '__module__' : 'google.cloud.datalabeling.v1beta1.evaluation_job_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.datalabeling.v1beta1.EvaluationJobConfig)
  })
_sym_db.RegisterMessage(EvaluationJobConfig)
_sym_db.RegisterMessage(EvaluationJobConfig.BigqueryImportKeysEntry)

EvaluationJobAlertConfig = _reflection.GeneratedProtocolMessageType('EvaluationJobAlertConfig', (_message.Message,), {
  'DESCRIPTOR' : _EVALUATIONJOBALERTCONFIG,
  '__module__' : 'google.cloud.datalabeling.v1beta1.evaluation_job_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.datalabeling.v1beta1.EvaluationJobAlertConfig)
  })
_sym_db.RegisterMessage(EvaluationJobAlertConfig)

Attempt = _reflection.GeneratedProtocolMessageType('Attempt', (_message.Message,), {
  'DESCRIPTOR' : _ATTEMPT,
  '__module__' : 'google.cloud.datalabeling.v1beta1.evaluation_job_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.datalabeling.v1beta1.Attempt)
  })
_sym_db.RegisterMessage(Attempt)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n%com.google.cloud.datalabeling.v1beta1P\001ZMgoogle.golang.org/genproto/googleapis/cloud/datalabeling/v1beta1;datalabeling\252\002!Google.Cloud.DataLabeling.V1Beta1\312\002!Google\\Cloud\\DataLabeling\\V1beta1\352\002$Google::Cloud::DataLabeling::V1beta1'
  _EVALUATIONJOB._options = None
  _EVALUATIONJOB._serialized_options = b'\352A_\n)datalabeling.googleapis.com/EvaluationJob\0222projects/{project}/evaluationJobs/{evaluation_job}'
  _EVALUATIONJOBCONFIG_BIGQUERYIMPORTKEYSENTRY._options = None
  _EVALUATIONJOBCONFIG_BIGQUERYIMPORTKEYSENTRY._serialized_options = b'8\001'
  _EVALUATIONJOB._serialized_start=375
  _EVALUATIONJOB._serialized_end=1122
  _EVALUATIONJOB_STATE._serialized_start=939
  _EVALUATIONJOB_STATE._serialized_end=1022
  _EVALUATIONJOBCONFIG._serialized_start=1125
  _EVALUATIONJOBCONFIG._serialized_end=2259
  _EVALUATIONJOBCONFIG_BIGQUERYIMPORTKEYSENTRY._serialized_start=2155
  _EVALUATIONJOBCONFIG_BIGQUERYIMPORTKEYSENTRY._serialized_end=2224
  _EVALUATIONJOBALERTCONFIG._serialized_start=2262
  _EVALUATIONJOBALERTCONFIG._serialized_end=2392
  _ATTEMPT._serialized_start=2395
  _ATTEMPT._serialized_end=2530
# @@protoc_insertion_point(module_scope)
