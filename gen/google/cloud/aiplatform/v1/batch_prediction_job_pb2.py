# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/aiplatform/v1/batch_prediction_job.proto
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
from google.cloud.aiplatform.v1 import completion_stats_pb2 as google_dot_cloud_dot_aiplatform_dot_v1_dot_completion__stats__pb2
from google.cloud.aiplatform.v1 import encryption_spec_pb2 as google_dot_cloud_dot_aiplatform_dot_v1_dot_encryption__spec__pb2
from google.cloud.aiplatform.v1 import explanation_pb2 as google_dot_cloud_dot_aiplatform_dot_v1_dot_explanation__pb2
from google.cloud.aiplatform.v1 import io_pb2 as google_dot_cloud_dot_aiplatform_dot_v1_dot_io__pb2
from google.cloud.aiplatform.v1 import job_state_pb2 as google_dot_cloud_dot_aiplatform_dot_v1_dot_job__state__pb2
from google.cloud.aiplatform.v1 import machine_resources_pb2 as google_dot_cloud_dot_aiplatform_dot_v1_dot_machine__resources__pb2
from google.cloud.aiplatform.v1 import manual_batch_tuning_parameters_pb2 as google_dot_cloud_dot_aiplatform_dot_v1_dot_manual__batch__tuning__parameters__pb2
from google.cloud.aiplatform.v1 import model_monitoring_pb2 as google_dot_cloud_dot_aiplatform_dot_v1_dot_model__monitoring__pb2
from google.cloud.aiplatform.v1 import unmanaged_container_model_pb2 as google_dot_cloud_dot_aiplatform_dot_v1_dot_unmanaged__container__model__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n5google/cloud/aiplatform/v1/batch_prediction_job.proto\x12\x1agoogle.cloud.aiplatform.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x31google/cloud/aiplatform/v1/completion_stats.proto\x1a\x30google/cloud/aiplatform/v1/encryption_spec.proto\x1a,google/cloud/aiplatform/v1/explanation.proto\x1a#google/cloud/aiplatform/v1/io.proto\x1a*google/cloud/aiplatform/v1/job_state.proto\x1a\x32google/cloud/aiplatform/v1/machine_resources.proto\x1a?google/cloud/aiplatform/v1/manual_batch_tuning_parameters.proto\x1a\x31google/cloud/aiplatform/v1/model_monitoring.proto\x1a:google/cloud/aiplatform/v1/unmanaged_container_model.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x17google/rpc/status.proto\x1a\x1cgoogle/api/annotations.proto\"\xa8\x15\n\x12\x42\x61tchPredictionJob\x12\x18\n\x04name\x18\x01 \x01(\tB\x04\xe2\x41\x01\x03R\x04name\x12\'\n\x0c\x64isplay_name\x18\x02 \x01(\tB\x04\xe2\x41\x01\x02R\x0b\x64isplayName\x12:\n\x05model\x18\x03 \x01(\tB$\xfa\x41!\n\x1f\x61iplatform.googleapis.com/ModelR\x05model\x12o\n\x19unmanaged_container_model\x18\x1c \x01(\x0b\x32\x33.google.cloud.aiplatform.v1.UnmanagedContainerModelR\x17unmanagedContainerModel\x12\x63\n\x0cinput_config\x18\x04 \x01(\x0b\x32:.google.cloud.aiplatform.v1.BatchPredictionJob.InputConfigB\x04\xe2\x41\x01\x02R\x0binputConfig\x12\x41\n\x10model_parameters\x18\x05 \x01(\x0b\x32\x16.google.protobuf.ValueR\x0fmodelParameters\x12\x66\n\routput_config\x18\x06 \x01(\x0b\x32;.google.cloud.aiplatform.v1.BatchPredictionJob.OutputConfigB\x04\xe2\x41\x01\x02R\x0coutputConfig\x12\x64\n\x13\x64\x65\x64icated_resources\x18\x07 \x01(\x0b\x32\x33.google.cloud.aiplatform.v1.BatchDedicatedResourcesR\x12\x64\x65\x64icatedResources\x12\x82\x01\n\x1emanual_batch_tuning_parameters\x18\x08 \x01(\x0b\x32\x37.google.cloud.aiplatform.v1.ManualBatchTuningParametersB\x04\xe2\x41\x01\x05R\x1bmanualBatchTuningParameters\x12\x31\n\x14generate_explanation\x18\x17 \x01(\x08R\x13generateExplanation\x12V\n\x10\x65xplanation_spec\x18\x19 \x01(\x0b\x32+.google.cloud.aiplatform.v1.ExplanationSpecR\x0f\x65xplanationSpec\x12`\n\x0boutput_info\x18\t \x01(\x0b\x32\x39.google.cloud.aiplatform.v1.BatchPredictionJob.OutputInfoB\x04\xe2\x41\x01\x03R\noutputInfo\x12@\n\x05state\x18\n \x01(\x0e\x32$.google.cloud.aiplatform.v1.JobStateB\x04\xe2\x41\x01\x03R\x05state\x12.\n\x05\x65rror\x18\x0b \x01(\x0b\x32\x12.google.rpc.StatusB\x04\xe2\x41\x01\x03R\x05\x65rror\x12\x43\n\x10partial_failures\x18\x0c \x03(\x0b\x32\x12.google.rpc.StatusB\x04\xe2\x41\x01\x03R\x0fpartialFailures\x12\x62\n\x12resources_consumed\x18\r \x01(\x0b\x32-.google.cloud.aiplatform.v1.ResourcesConsumedB\x04\xe2\x41\x01\x03R\x11resourcesConsumed\x12\\\n\x10\x63ompletion_stats\x18\x0e \x01(\x0b\x32+.google.cloud.aiplatform.v1.CompletionStatsB\x04\xe2\x41\x01\x03R\x0f\x63ompletionStats\x12\x41\n\x0b\x63reate_time\x18\x0f \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x04\xe2\x41\x01\x03R\ncreateTime\x12?\n\nstart_time\x18\x10 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x04\xe2\x41\x01\x03R\tstartTime\x12;\n\x08\x65nd_time\x18\x11 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x04\xe2\x41\x01\x03R\x07\x65ndTime\x12\x41\n\x0bupdate_time\x18\x12 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x04\xe2\x41\x01\x03R\nupdateTime\x12R\n\x06labels\x18\x13 \x03(\x0b\x32:.google.cloud.aiplatform.v1.BatchPredictionJob.LabelsEntryR\x06labels\x12S\n\x0f\x65ncryption_spec\x18\x18 \x01(\x0b\x32*.google.cloud.aiplatform.v1.EncryptionSpecR\x0e\x65ncryptionSpec\x1a\xe7\x01\n\x0bInputConfig\x12\x46\n\ngcs_source\x18\x02 \x01(\x0b\x32%.google.cloud.aiplatform.v1.GcsSourceH\x00R\tgcsSource\x12U\n\x0f\x62igquery_source\x18\x03 \x01(\x0b\x32*.google.cloud.aiplatform.v1.BigQuerySourceH\x00R\x0e\x62igquerySource\x12/\n\x10instances_format\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02R\x0finstancesFormatB\x08\n\x06source\x1a\x8f\x02\n\x0cOutputConfig\x12U\n\x0fgcs_destination\x18\x02 \x01(\x0b\x32*.google.cloud.aiplatform.v1.GcsDestinationH\x00R\x0egcsDestination\x12\x64\n\x14\x62igquery_destination\x18\x03 \x01(\x0b\x32/.google.cloud.aiplatform.v1.BigQueryDestinationH\x00R\x13\x62igqueryDestination\x12\x33\n\x12predictions_format\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02R\x11predictionsFormatB\r\n\x0b\x64\x65stination\x1a\xd3\x01\n\nOutputInfo\x12\x38\n\x14gcs_output_directory\x18\x01 \x01(\tB\x04\xe2\x41\x01\x03H\x00R\x12gcsOutputDirectory\x12>\n\x17\x62igquery_output_dataset\x18\x02 \x01(\tB\x04\xe2\x41\x01\x03H\x00R\x15\x62igqueryOutputDataset\x12\x38\n\x15\x62igquery_output_table\x18\x04 \x01(\tB\x04\xe2\x41\x01\x03R\x13\x62igqueryOutputTableB\x11\n\x0foutput_location\x1a\x39\n\x0bLabelsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01:\x86\x01\xea\x41\x82\x01\n,aiplatform.googleapis.com/BatchPredictionJob\x12Rprojects/{project}/locations/{location}/batchPredictionJobs/{batch_prediction_job}B\xdb\x01\n\x1e\x63om.google.cloud.aiplatform.v1B\x17\x42\x61tchPredictionJobProtoP\x01ZDgoogle.golang.org/genproto/googleapis/cloud/aiplatform/v1;aiplatform\xaa\x02\x1aGoogle.Cloud.AIPlatform.V1\xca\x02\x1aGoogle\\Cloud\\AIPlatform\\V1\xea\x02\x1dGoogle::Cloud::AIPlatform::V1b\x06proto3')



_BATCHPREDICTIONJOB = DESCRIPTOR.message_types_by_name['BatchPredictionJob']
_BATCHPREDICTIONJOB_INPUTCONFIG = _BATCHPREDICTIONJOB.nested_types_by_name['InputConfig']
_BATCHPREDICTIONJOB_OUTPUTCONFIG = _BATCHPREDICTIONJOB.nested_types_by_name['OutputConfig']
_BATCHPREDICTIONJOB_OUTPUTINFO = _BATCHPREDICTIONJOB.nested_types_by_name['OutputInfo']
_BATCHPREDICTIONJOB_LABELSENTRY = _BATCHPREDICTIONJOB.nested_types_by_name['LabelsEntry']
BatchPredictionJob = _reflection.GeneratedProtocolMessageType('BatchPredictionJob', (_message.Message,), {

  'InputConfig' : _reflection.GeneratedProtocolMessageType('InputConfig', (_message.Message,), {
    'DESCRIPTOR' : _BATCHPREDICTIONJOB_INPUTCONFIG,
    '__module__' : 'google.cloud.aiplatform.v1.batch_prediction_job_pb2'
    # @@protoc_insertion_point(class_scope:google.cloud.aiplatform.v1.BatchPredictionJob.InputConfig)
    })
  ,

  'OutputConfig' : _reflection.GeneratedProtocolMessageType('OutputConfig', (_message.Message,), {
    'DESCRIPTOR' : _BATCHPREDICTIONJOB_OUTPUTCONFIG,
    '__module__' : 'google.cloud.aiplatform.v1.batch_prediction_job_pb2'
    # @@protoc_insertion_point(class_scope:google.cloud.aiplatform.v1.BatchPredictionJob.OutputConfig)
    })
  ,

  'OutputInfo' : _reflection.GeneratedProtocolMessageType('OutputInfo', (_message.Message,), {
    'DESCRIPTOR' : _BATCHPREDICTIONJOB_OUTPUTINFO,
    '__module__' : 'google.cloud.aiplatform.v1.batch_prediction_job_pb2'
    # @@protoc_insertion_point(class_scope:google.cloud.aiplatform.v1.BatchPredictionJob.OutputInfo)
    })
  ,

  'LabelsEntry' : _reflection.GeneratedProtocolMessageType('LabelsEntry', (_message.Message,), {
    'DESCRIPTOR' : _BATCHPREDICTIONJOB_LABELSENTRY,
    '__module__' : 'google.cloud.aiplatform.v1.batch_prediction_job_pb2'
    # @@protoc_insertion_point(class_scope:google.cloud.aiplatform.v1.BatchPredictionJob.LabelsEntry)
    })
  ,
  'DESCRIPTOR' : _BATCHPREDICTIONJOB,
  '__module__' : 'google.cloud.aiplatform.v1.batch_prediction_job_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.aiplatform.v1.BatchPredictionJob)
  })
_sym_db.RegisterMessage(BatchPredictionJob)
_sym_db.RegisterMessage(BatchPredictionJob.InputConfig)
_sym_db.RegisterMessage(BatchPredictionJob.OutputConfig)
_sym_db.RegisterMessage(BatchPredictionJob.OutputInfo)
_sym_db.RegisterMessage(BatchPredictionJob.LabelsEntry)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\036com.google.cloud.aiplatform.v1B\027BatchPredictionJobProtoP\001ZDgoogle.golang.org/genproto/googleapis/cloud/aiplatform/v1;aiplatform\252\002\032Google.Cloud.AIPlatform.V1\312\002\032Google\\Cloud\\AIPlatform\\V1\352\002\035Google::Cloud::AIPlatform::V1'
  _BATCHPREDICTIONJOB_INPUTCONFIG.fields_by_name['instances_format']._options = None
  _BATCHPREDICTIONJOB_INPUTCONFIG.fields_by_name['instances_format']._serialized_options = b'\342A\001\002'
  _BATCHPREDICTIONJOB_OUTPUTCONFIG.fields_by_name['predictions_format']._options = None
  _BATCHPREDICTIONJOB_OUTPUTCONFIG.fields_by_name['predictions_format']._serialized_options = b'\342A\001\002'
  _BATCHPREDICTIONJOB_OUTPUTINFO.fields_by_name['gcs_output_directory']._options = None
  _BATCHPREDICTIONJOB_OUTPUTINFO.fields_by_name['gcs_output_directory']._serialized_options = b'\342A\001\003'
  _BATCHPREDICTIONJOB_OUTPUTINFO.fields_by_name['bigquery_output_dataset']._options = None
  _BATCHPREDICTIONJOB_OUTPUTINFO.fields_by_name['bigquery_output_dataset']._serialized_options = b'\342A\001\003'
  _BATCHPREDICTIONJOB_OUTPUTINFO.fields_by_name['bigquery_output_table']._options = None
  _BATCHPREDICTIONJOB_OUTPUTINFO.fields_by_name['bigquery_output_table']._serialized_options = b'\342A\001\003'
  _BATCHPREDICTIONJOB_LABELSENTRY._options = None
  _BATCHPREDICTIONJOB_LABELSENTRY._serialized_options = b'8\001'
  _BATCHPREDICTIONJOB.fields_by_name['name']._options = None
  _BATCHPREDICTIONJOB.fields_by_name['name']._serialized_options = b'\342A\001\003'
  _BATCHPREDICTIONJOB.fields_by_name['display_name']._options = None
  _BATCHPREDICTIONJOB.fields_by_name['display_name']._serialized_options = b'\342A\001\002'
  _BATCHPREDICTIONJOB.fields_by_name['model']._options = None
  _BATCHPREDICTIONJOB.fields_by_name['model']._serialized_options = b'\372A!\n\037aiplatform.googleapis.com/Model'
  _BATCHPREDICTIONJOB.fields_by_name['input_config']._options = None
  _BATCHPREDICTIONJOB.fields_by_name['input_config']._serialized_options = b'\342A\001\002'
  _BATCHPREDICTIONJOB.fields_by_name['output_config']._options = None
  _BATCHPREDICTIONJOB.fields_by_name['output_config']._serialized_options = b'\342A\001\002'
  _BATCHPREDICTIONJOB.fields_by_name['manual_batch_tuning_parameters']._options = None
  _BATCHPREDICTIONJOB.fields_by_name['manual_batch_tuning_parameters']._serialized_options = b'\342A\001\005'
  _BATCHPREDICTIONJOB.fields_by_name['output_info']._options = None
  _BATCHPREDICTIONJOB.fields_by_name['output_info']._serialized_options = b'\342A\001\003'
  _BATCHPREDICTIONJOB.fields_by_name['state']._options = None
  _BATCHPREDICTIONJOB.fields_by_name['state']._serialized_options = b'\342A\001\003'
  _BATCHPREDICTIONJOB.fields_by_name['error']._options = None
  _BATCHPREDICTIONJOB.fields_by_name['error']._serialized_options = b'\342A\001\003'
  _BATCHPREDICTIONJOB.fields_by_name['partial_failures']._options = None
  _BATCHPREDICTIONJOB.fields_by_name['partial_failures']._serialized_options = b'\342A\001\003'
  _BATCHPREDICTIONJOB.fields_by_name['resources_consumed']._options = None
  _BATCHPREDICTIONJOB.fields_by_name['resources_consumed']._serialized_options = b'\342A\001\003'
  _BATCHPREDICTIONJOB.fields_by_name['completion_stats']._options = None
  _BATCHPREDICTIONJOB.fields_by_name['completion_stats']._serialized_options = b'\342A\001\003'
  _BATCHPREDICTIONJOB.fields_by_name['create_time']._options = None
  _BATCHPREDICTIONJOB.fields_by_name['create_time']._serialized_options = b'\342A\001\003'
  _BATCHPREDICTIONJOB.fields_by_name['start_time']._options = None
  _BATCHPREDICTIONJOB.fields_by_name['start_time']._serialized_options = b'\342A\001\003'
  _BATCHPREDICTIONJOB.fields_by_name['end_time']._options = None
  _BATCHPREDICTIONJOB.fields_by_name['end_time']._serialized_options = b'\342A\001\003'
  _BATCHPREDICTIONJOB.fields_by_name['update_time']._options = None
  _BATCHPREDICTIONJOB.fields_by_name['update_time']._serialized_options = b'\342A\001\003'
  _BATCHPREDICTIONJOB._options = None
  _BATCHPREDICTIONJOB._serialized_options = b'\352A\202\001\n,aiplatform.googleapis.com/BatchPredictionJob\022Rprojects/{project}/locations/{location}/batchPredictionJobs/{batch_prediction_job}'
  _BATCHPREDICTIONJOB._serialized_start=720
  _BATCHPREDICTIONJOB._serialized_end=3448
  _BATCHPREDICTIONJOB_INPUTCONFIG._serialized_start=2533
  _BATCHPREDICTIONJOB_INPUTCONFIG._serialized_end=2764
  _BATCHPREDICTIONJOB_OUTPUTCONFIG._serialized_start=2767
  _BATCHPREDICTIONJOB_OUTPUTCONFIG._serialized_end=3038
  _BATCHPREDICTIONJOB_OUTPUTINFO._serialized_start=3041
  _BATCHPREDICTIONJOB_OUTPUTINFO._serialized_end=3252
  _BATCHPREDICTIONJOB_LABELSENTRY._serialized_start=3254
  _BATCHPREDICTIONJOB_LABELSENTRY._serialized_end=3311
# @@protoc_insertion_point(module_scope)
