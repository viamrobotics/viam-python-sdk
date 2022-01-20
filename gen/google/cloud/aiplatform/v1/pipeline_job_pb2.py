# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/aiplatform/v1/pipeline_job.proto
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
from google.cloud.aiplatform.v1 import artifact_pb2 as google_dot_cloud_dot_aiplatform_dot_v1_dot_artifact__pb2
from google.cloud.aiplatform.v1 import context_pb2 as google_dot_cloud_dot_aiplatform_dot_v1_dot_context__pb2
from google.cloud.aiplatform.v1 import encryption_spec_pb2 as google_dot_cloud_dot_aiplatform_dot_v1_dot_encryption__spec__pb2
from google.cloud.aiplatform.v1 import execution_pb2 as google_dot_cloud_dot_aiplatform_dot_v1_dot_execution__pb2
from google.cloud.aiplatform.v1 import pipeline_state_pb2 as google_dot_cloud_dot_aiplatform_dot_v1_dot_pipeline__state__pb2
from google.cloud.aiplatform.v1 import value_pb2 as google_dot_cloud_dot_aiplatform_dot_v1_dot_value__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-google/cloud/aiplatform/v1/pipeline_job.proto\x12\x1agoogle.cloud.aiplatform.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a)google/cloud/aiplatform/v1/artifact.proto\x1a(google/cloud/aiplatform/v1/context.proto\x1a\x30google/cloud/aiplatform/v1/encryption_spec.proto\x1a*google/cloud/aiplatform/v1/execution.proto\x1a/google/cloud/aiplatform/v1/pipeline_state.proto\x1a&google/cloud/aiplatform/v1/value.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x17google/rpc/status.proto\x1a\x1cgoogle/api/annotations.proto\"\xdb\x0c\n\x0bPipelineJob\x12\x18\n\x04name\x18\x01 \x01(\tB\x04\xe2\x41\x01\x03R\x04name\x12!\n\x0c\x64isplay_name\x18\x02 \x01(\tR\x0b\x64isplayName\x12\x41\n\x0b\x63reate_time\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x04\xe2\x41\x01\x03R\ncreateTime\x12?\n\nstart_time\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x04\xe2\x41\x01\x03R\tstartTime\x12;\n\x08\x65nd_time\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x04\xe2\x41\x01\x03R\x07\x65ndTime\x12\x41\n\x0bupdate_time\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x04\xe2\x41\x01\x03R\nupdateTime\x12\x42\n\rpipeline_spec\x18\x07 \x01(\x0b\x32\x17.google.protobuf.StructB\x04\xe2\x41\x01\x02R\x0cpipelineSpec\x12\x45\n\x05state\x18\x08 \x01(\x0e\x32).google.cloud.aiplatform.v1.PipelineStateB\x04\xe2\x41\x01\x03R\x05state\x12R\n\njob_detail\x18\t \x01(\x0b\x32-.google.cloud.aiplatform.v1.PipelineJobDetailB\x04\xe2\x41\x01\x03R\tjobDetail\x12.\n\x05\x65rror\x18\n \x01(\x0b\x32\x12.google.rpc.StatusB\x04\xe2\x41\x01\x03R\x05\x65rror\x12K\n\x06labels\x18\x0b \x03(\x0b\x32\x33.google.cloud.aiplatform.v1.PipelineJob.LabelsEntryR\x06labels\x12\\\n\x0eruntime_config\x18\x0c \x01(\x0b\x32\x35.google.cloud.aiplatform.v1.PipelineJob.RuntimeConfigR\rruntimeConfig\x12S\n\x0f\x65ncryption_spec\x18\x10 \x01(\x0b\x32*.google.cloud.aiplatform.v1.EncryptionSpecR\x0e\x65ncryptionSpec\x12\'\n\x0fservice_account\x18\x11 \x01(\tR\x0eserviceAccount\x12=\n\x07network\x18\x12 \x01(\tB#\xfa\x41 \n\x1e\x63ompute.googleapis.com/NetworkR\x07network\x1a\xe7\x03\n\rRuntimeConfig\x12i\n\nparameters\x18\x01 \x03(\x0b\x32\x45.google.cloud.aiplatform.v1.PipelineJob.RuntimeConfig.ParametersEntryB\x02\x18\x01R\nparameters\x12\x36\n\x14gcs_output_directory\x18\x02 \x01(\tB\x04\xe2\x41\x01\x02R\x12gcsOutputDirectory\x12u\n\x10parameter_values\x18\x03 \x03(\x0b\x32J.google.cloud.aiplatform.v1.PipelineJob.RuntimeConfig.ParameterValuesEntryR\x0fparameterValues\x1a`\n\x0fParametersEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x37\n\x05value\x18\x02 \x01(\x0b\x32!.google.cloud.aiplatform.v1.ValueR\x05value:\x02\x38\x01\x1aZ\n\x14ParameterValuesEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12,\n\x05value\x18\x02 \x01(\x0b\x32\x16.google.protobuf.ValueR\x05value:\x02\x38\x01\x1a\x39\n\x0bLabelsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01:o\xea\x41l\n%aiplatform.googleapis.com/PipelineJob\x12\x43projects/{project}/locations/{location}/pipelineJobs/{pipeline_job}\"\x9f\x02\n\x11PipelineJobDetail\x12T\n\x10pipeline_context\x18\x01 \x01(\x0b\x32#.google.cloud.aiplatform.v1.ContextB\x04\xe2\x41\x01\x03R\x0fpipelineContext\x12[\n\x14pipeline_run_context\x18\x02 \x01(\x0b\x32#.google.cloud.aiplatform.v1.ContextB\x04\xe2\x41\x01\x03R\x12pipelineRunContext\x12W\n\x0ctask_details\x18\x03 \x03(\x0b\x32..google.cloud.aiplatform.v1.PipelineTaskDetailB\x04\xe2\x41\x01\x03R\x0btaskDetails\"\xf9\x0c\n\x12PipelineTaskDetail\x12\x1d\n\x07task_id\x18\x01 \x01(\x03\x42\x04\xe2\x41\x01\x03R\x06taskId\x12*\n\x0eparent_task_id\x18\x0c \x01(\x03\x42\x04\xe2\x41\x01\x03R\x0cparentTaskId\x12!\n\ttask_name\x18\x02 \x01(\tB\x04\xe2\x41\x01\x03R\x08taskName\x12\x41\n\x0b\x63reate_time\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x04\xe2\x41\x01\x03R\ncreateTime\x12?\n\nstart_time\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x04\xe2\x41\x01\x03R\tstartTime\x12;\n\x08\x65nd_time\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x04\xe2\x41\x01\x03R\x07\x65ndTime\x12\x65\n\x0f\x65xecutor_detail\x18\x06 \x01(\x0b\x32\x36.google.cloud.aiplatform.v1.PipelineTaskExecutorDetailB\x04\xe2\x41\x01\x03R\x0e\x65xecutorDetail\x12P\n\x05state\x18\x07 \x01(\x0e\x32\x34.google.cloud.aiplatform.v1.PipelineTaskDetail.StateB\x04\xe2\x41\x01\x03R\x05state\x12I\n\texecution\x18\x08 \x01(\x0b\x32%.google.cloud.aiplatform.v1.ExecutionB\x04\xe2\x41\x01\x03R\texecution\x12.\n\x05\x65rror\x18\t \x01(\x0b\x32\x12.google.rpc.StatusB\x04\xe2\x41\x01\x03R\x05\x65rror\x12y\n\x14pipeline_task_status\x18\r \x03(\x0b\x32\x41.google.cloud.aiplatform.v1.PipelineTaskDetail.PipelineTaskStatusB\x04\xe2\x41\x01\x03R\x12pipelineTaskStatus\x12X\n\x06inputs\x18\n \x03(\x0b\x32:.google.cloud.aiplatform.v1.PipelineTaskDetail.InputsEntryB\x04\xe2\x41\x01\x03R\x06inputs\x12[\n\x07outputs\x18\x0b \x03(\x0b\x32;.google.cloud.aiplatform.v1.PipelineTaskDetail.OutputsEntryB\x04\xe2\x41\x01\x03R\x07outputs\x1a\xd9\x01\n\x12PipelineTaskStatus\x12\x41\n\x0bupdate_time\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x04\xe2\x41\x01\x03R\nupdateTime\x12P\n\x05state\x18\x02 \x01(\x0e\x32\x34.google.cloud.aiplatform.v1.PipelineTaskDetail.StateB\x04\xe2\x41\x01\x03R\x05state\x12.\n\x05\x65rror\x18\x03 \x01(\x0b\x32\x12.google.rpc.StatusB\x04\xe2\x41\x01\x03R\x05\x65rror\x1aX\n\x0c\x41rtifactList\x12H\n\tartifacts\x18\x01 \x03(\x0b\x32$.google.cloud.aiplatform.v1.ArtifactB\x04\xe2\x41\x01\x03R\tartifacts\x1av\n\x0bInputsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12Q\n\x05value\x18\x02 \x01(\x0b\x32;.google.cloud.aiplatform.v1.PipelineTaskDetail.ArtifactListR\x05value:\x02\x38\x01\x1aw\n\x0cOutputsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12Q\n\x05value\x18\x02 \x01(\x0b\x32;.google.cloud.aiplatform.v1.PipelineTaskDetail.ArtifactListR\x05value:\x02\x38\x01\"\xa6\x01\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0b\n\x07PENDING\x10\x01\x12\x0b\n\x07RUNNING\x10\x02\x12\r\n\tSUCCEEDED\x10\x03\x12\x12\n\x0e\x43\x41NCEL_PENDING\x10\x04\x12\x0e\n\nCANCELLING\x10\x05\x12\r\n\tCANCELLED\x10\x06\x12\n\n\x06\x46\x41ILED\x10\x07\x12\x0b\n\x07SKIPPED\x10\x08\x12\x11\n\rNOT_TRIGGERED\x10\t\"\xb5\x04\n\x1aPipelineTaskExecutorDetail\x12y\n\x10\x63ontainer_detail\x18\x01 \x01(\x0b\x32\x46.google.cloud.aiplatform.v1.PipelineTaskExecutorDetail.ContainerDetailB\x04\xe2\x41\x01\x03H\x00R\x0f\x63ontainerDetail\x12|\n\x11\x63ustom_job_detail\x18\x02 \x01(\x0b\x32\x46.google.cloud.aiplatform.v1.PipelineTaskExecutorDetail.CustomJobDetailB\x06\x18\x01\xe2\x41\x01\x03H\x00R\x0f\x63ustomJobDetail\x1a\xbb\x01\n\x0f\x43ontainerDetail\x12G\n\x08main_job\x18\x01 \x01(\tB,\xe2\x41\x01\x03\xfa\x41%\n#aiplatform.googleapis.com/CustomJobR\x07mainJob\x12_\n\x15pre_caching_check_job\x18\x02 \x01(\tB,\xe2\x41\x01\x03\xfa\x41%\n#aiplatform.googleapis.com/CustomJobR\x12preCachingCheckJob\x1aU\n\x0f\x43ustomJobDetail\x12>\n\x03job\x18\x01 \x01(\tB,\xe2\x41\x01\x03\xfa\x41%\n#aiplatform.googleapis.com/CustomJobR\x03job:\x02\x18\x01\x42\t\n\x07\x64\x65tailsB\x9d\x02\n\x1e\x63om.google.cloud.aiplatform.v1B\x08PipelineP\x01ZDgoogle.golang.org/genproto/googleapis/cloud/aiplatform/v1;aiplatform\xaa\x02\x1aGoogle.Cloud.AIPlatform.V1\xca\x02\x1aGoogle\\Cloud\\AIPlatform\\V1\xea\x02\x1dGoogle::Cloud::AIPlatform::V1\xea\x41N\n\x1e\x63ompute.googleapis.com/Network\x12,projects/{project}/global/networks/{network}b\x06proto3')



_PIPELINEJOB = DESCRIPTOR.message_types_by_name['PipelineJob']
_PIPELINEJOB_RUNTIMECONFIG = _PIPELINEJOB.nested_types_by_name['RuntimeConfig']
_PIPELINEJOB_RUNTIMECONFIG_PARAMETERSENTRY = _PIPELINEJOB_RUNTIMECONFIG.nested_types_by_name['ParametersEntry']
_PIPELINEJOB_RUNTIMECONFIG_PARAMETERVALUESENTRY = _PIPELINEJOB_RUNTIMECONFIG.nested_types_by_name['ParameterValuesEntry']
_PIPELINEJOB_LABELSENTRY = _PIPELINEJOB.nested_types_by_name['LabelsEntry']
_PIPELINEJOBDETAIL = DESCRIPTOR.message_types_by_name['PipelineJobDetail']
_PIPELINETASKDETAIL = DESCRIPTOR.message_types_by_name['PipelineTaskDetail']
_PIPELINETASKDETAIL_PIPELINETASKSTATUS = _PIPELINETASKDETAIL.nested_types_by_name['PipelineTaskStatus']
_PIPELINETASKDETAIL_ARTIFACTLIST = _PIPELINETASKDETAIL.nested_types_by_name['ArtifactList']
_PIPELINETASKDETAIL_INPUTSENTRY = _PIPELINETASKDETAIL.nested_types_by_name['InputsEntry']
_PIPELINETASKDETAIL_OUTPUTSENTRY = _PIPELINETASKDETAIL.nested_types_by_name['OutputsEntry']
_PIPELINETASKEXECUTORDETAIL = DESCRIPTOR.message_types_by_name['PipelineTaskExecutorDetail']
_PIPELINETASKEXECUTORDETAIL_CONTAINERDETAIL = _PIPELINETASKEXECUTORDETAIL.nested_types_by_name['ContainerDetail']
_PIPELINETASKEXECUTORDETAIL_CUSTOMJOBDETAIL = _PIPELINETASKEXECUTORDETAIL.nested_types_by_name['CustomJobDetail']
_PIPELINETASKDETAIL_STATE = _PIPELINETASKDETAIL.enum_types_by_name['State']
PipelineJob = _reflection.GeneratedProtocolMessageType('PipelineJob', (_message.Message,), {

  'RuntimeConfig' : _reflection.GeneratedProtocolMessageType('RuntimeConfig', (_message.Message,), {

    'ParametersEntry' : _reflection.GeneratedProtocolMessageType('ParametersEntry', (_message.Message,), {
      'DESCRIPTOR' : _PIPELINEJOB_RUNTIMECONFIG_PARAMETERSENTRY,
      '__module__' : 'google.cloud.aiplatform.v1.pipeline_job_pb2'
      # @@protoc_insertion_point(class_scope:google.cloud.aiplatform.v1.PipelineJob.RuntimeConfig.ParametersEntry)
      })
    ,

    'ParameterValuesEntry' : _reflection.GeneratedProtocolMessageType('ParameterValuesEntry', (_message.Message,), {
      'DESCRIPTOR' : _PIPELINEJOB_RUNTIMECONFIG_PARAMETERVALUESENTRY,
      '__module__' : 'google.cloud.aiplatform.v1.pipeline_job_pb2'
      # @@protoc_insertion_point(class_scope:google.cloud.aiplatform.v1.PipelineJob.RuntimeConfig.ParameterValuesEntry)
      })
    ,
    'DESCRIPTOR' : _PIPELINEJOB_RUNTIMECONFIG,
    '__module__' : 'google.cloud.aiplatform.v1.pipeline_job_pb2'
    # @@protoc_insertion_point(class_scope:google.cloud.aiplatform.v1.PipelineJob.RuntimeConfig)
    })
  ,

  'LabelsEntry' : _reflection.GeneratedProtocolMessageType('LabelsEntry', (_message.Message,), {
    'DESCRIPTOR' : _PIPELINEJOB_LABELSENTRY,
    '__module__' : 'google.cloud.aiplatform.v1.pipeline_job_pb2'
    # @@protoc_insertion_point(class_scope:google.cloud.aiplatform.v1.PipelineJob.LabelsEntry)
    })
  ,
  'DESCRIPTOR' : _PIPELINEJOB,
  '__module__' : 'google.cloud.aiplatform.v1.pipeline_job_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.aiplatform.v1.PipelineJob)
  })
_sym_db.RegisterMessage(PipelineJob)
_sym_db.RegisterMessage(PipelineJob.RuntimeConfig)
_sym_db.RegisterMessage(PipelineJob.RuntimeConfig.ParametersEntry)
_sym_db.RegisterMessage(PipelineJob.RuntimeConfig.ParameterValuesEntry)
_sym_db.RegisterMessage(PipelineJob.LabelsEntry)

PipelineJobDetail = _reflection.GeneratedProtocolMessageType('PipelineJobDetail', (_message.Message,), {
  'DESCRIPTOR' : _PIPELINEJOBDETAIL,
  '__module__' : 'google.cloud.aiplatform.v1.pipeline_job_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.aiplatform.v1.PipelineJobDetail)
  })
_sym_db.RegisterMessage(PipelineJobDetail)

PipelineTaskDetail = _reflection.GeneratedProtocolMessageType('PipelineTaskDetail', (_message.Message,), {

  'PipelineTaskStatus' : _reflection.GeneratedProtocolMessageType('PipelineTaskStatus', (_message.Message,), {
    'DESCRIPTOR' : _PIPELINETASKDETAIL_PIPELINETASKSTATUS,
    '__module__' : 'google.cloud.aiplatform.v1.pipeline_job_pb2'
    # @@protoc_insertion_point(class_scope:google.cloud.aiplatform.v1.PipelineTaskDetail.PipelineTaskStatus)
    })
  ,

  'ArtifactList' : _reflection.GeneratedProtocolMessageType('ArtifactList', (_message.Message,), {
    'DESCRIPTOR' : _PIPELINETASKDETAIL_ARTIFACTLIST,
    '__module__' : 'google.cloud.aiplatform.v1.pipeline_job_pb2'
    # @@protoc_insertion_point(class_scope:google.cloud.aiplatform.v1.PipelineTaskDetail.ArtifactList)
    })
  ,

  'InputsEntry' : _reflection.GeneratedProtocolMessageType('InputsEntry', (_message.Message,), {
    'DESCRIPTOR' : _PIPELINETASKDETAIL_INPUTSENTRY,
    '__module__' : 'google.cloud.aiplatform.v1.pipeline_job_pb2'
    # @@protoc_insertion_point(class_scope:google.cloud.aiplatform.v1.PipelineTaskDetail.InputsEntry)
    })
  ,

  'OutputsEntry' : _reflection.GeneratedProtocolMessageType('OutputsEntry', (_message.Message,), {
    'DESCRIPTOR' : _PIPELINETASKDETAIL_OUTPUTSENTRY,
    '__module__' : 'google.cloud.aiplatform.v1.pipeline_job_pb2'
    # @@protoc_insertion_point(class_scope:google.cloud.aiplatform.v1.PipelineTaskDetail.OutputsEntry)
    })
  ,
  'DESCRIPTOR' : _PIPELINETASKDETAIL,
  '__module__' : 'google.cloud.aiplatform.v1.pipeline_job_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.aiplatform.v1.PipelineTaskDetail)
  })
_sym_db.RegisterMessage(PipelineTaskDetail)
_sym_db.RegisterMessage(PipelineTaskDetail.PipelineTaskStatus)
_sym_db.RegisterMessage(PipelineTaskDetail.ArtifactList)
_sym_db.RegisterMessage(PipelineTaskDetail.InputsEntry)
_sym_db.RegisterMessage(PipelineTaskDetail.OutputsEntry)

PipelineTaskExecutorDetail = _reflection.GeneratedProtocolMessageType('PipelineTaskExecutorDetail', (_message.Message,), {

  'ContainerDetail' : _reflection.GeneratedProtocolMessageType('ContainerDetail', (_message.Message,), {
    'DESCRIPTOR' : _PIPELINETASKEXECUTORDETAIL_CONTAINERDETAIL,
    '__module__' : 'google.cloud.aiplatform.v1.pipeline_job_pb2'
    # @@protoc_insertion_point(class_scope:google.cloud.aiplatform.v1.PipelineTaskExecutorDetail.ContainerDetail)
    })
  ,

  'CustomJobDetail' : _reflection.GeneratedProtocolMessageType('CustomJobDetail', (_message.Message,), {
    'DESCRIPTOR' : _PIPELINETASKEXECUTORDETAIL_CUSTOMJOBDETAIL,
    '__module__' : 'google.cloud.aiplatform.v1.pipeline_job_pb2'
    # @@protoc_insertion_point(class_scope:google.cloud.aiplatform.v1.PipelineTaskExecutorDetail.CustomJobDetail)
    })
  ,
  'DESCRIPTOR' : _PIPELINETASKEXECUTORDETAIL,
  '__module__' : 'google.cloud.aiplatform.v1.pipeline_job_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.aiplatform.v1.PipelineTaskExecutorDetail)
  })
_sym_db.RegisterMessage(PipelineTaskExecutorDetail)
_sym_db.RegisterMessage(PipelineTaskExecutorDetail.ContainerDetail)
_sym_db.RegisterMessage(PipelineTaskExecutorDetail.CustomJobDetail)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\036com.google.cloud.aiplatform.v1B\010PipelineP\001ZDgoogle.golang.org/genproto/googleapis/cloud/aiplatform/v1;aiplatform\252\002\032Google.Cloud.AIPlatform.V1\312\002\032Google\\Cloud\\AIPlatform\\V1\352\002\035Google::Cloud::AIPlatform::V1\352AN\n\036compute.googleapis.com/Network\022,projects/{project}/global/networks/{network}'
  _PIPELINEJOB_RUNTIMECONFIG_PARAMETERSENTRY._options = None
  _PIPELINEJOB_RUNTIMECONFIG_PARAMETERSENTRY._serialized_options = b'8\001'
  _PIPELINEJOB_RUNTIMECONFIG_PARAMETERVALUESENTRY._options = None
  _PIPELINEJOB_RUNTIMECONFIG_PARAMETERVALUESENTRY._serialized_options = b'8\001'
  _PIPELINEJOB_RUNTIMECONFIG.fields_by_name['parameters']._options = None
  _PIPELINEJOB_RUNTIMECONFIG.fields_by_name['parameters']._serialized_options = b'\030\001'
  _PIPELINEJOB_RUNTIMECONFIG.fields_by_name['gcs_output_directory']._options = None
  _PIPELINEJOB_RUNTIMECONFIG.fields_by_name['gcs_output_directory']._serialized_options = b'\342A\001\002'
  _PIPELINEJOB_LABELSENTRY._options = None
  _PIPELINEJOB_LABELSENTRY._serialized_options = b'8\001'
  _PIPELINEJOB.fields_by_name['name']._options = None
  _PIPELINEJOB.fields_by_name['name']._serialized_options = b'\342A\001\003'
  _PIPELINEJOB.fields_by_name['create_time']._options = None
  _PIPELINEJOB.fields_by_name['create_time']._serialized_options = b'\342A\001\003'
  _PIPELINEJOB.fields_by_name['start_time']._options = None
  _PIPELINEJOB.fields_by_name['start_time']._serialized_options = b'\342A\001\003'
  _PIPELINEJOB.fields_by_name['end_time']._options = None
  _PIPELINEJOB.fields_by_name['end_time']._serialized_options = b'\342A\001\003'
  _PIPELINEJOB.fields_by_name['update_time']._options = None
  _PIPELINEJOB.fields_by_name['update_time']._serialized_options = b'\342A\001\003'
  _PIPELINEJOB.fields_by_name['pipeline_spec']._options = None
  _PIPELINEJOB.fields_by_name['pipeline_spec']._serialized_options = b'\342A\001\002'
  _PIPELINEJOB.fields_by_name['state']._options = None
  _PIPELINEJOB.fields_by_name['state']._serialized_options = b'\342A\001\003'
  _PIPELINEJOB.fields_by_name['job_detail']._options = None
  _PIPELINEJOB.fields_by_name['job_detail']._serialized_options = b'\342A\001\003'
  _PIPELINEJOB.fields_by_name['error']._options = None
  _PIPELINEJOB.fields_by_name['error']._serialized_options = b'\342A\001\003'
  _PIPELINEJOB.fields_by_name['network']._options = None
  _PIPELINEJOB.fields_by_name['network']._serialized_options = b'\372A \n\036compute.googleapis.com/Network'
  _PIPELINEJOB._options = None
  _PIPELINEJOB._serialized_options = b'\352Al\n%aiplatform.googleapis.com/PipelineJob\022Cprojects/{project}/locations/{location}/pipelineJobs/{pipeline_job}'
  _PIPELINEJOBDETAIL.fields_by_name['pipeline_context']._options = None
  _PIPELINEJOBDETAIL.fields_by_name['pipeline_context']._serialized_options = b'\342A\001\003'
  _PIPELINEJOBDETAIL.fields_by_name['pipeline_run_context']._options = None
  _PIPELINEJOBDETAIL.fields_by_name['pipeline_run_context']._serialized_options = b'\342A\001\003'
  _PIPELINEJOBDETAIL.fields_by_name['task_details']._options = None
  _PIPELINEJOBDETAIL.fields_by_name['task_details']._serialized_options = b'\342A\001\003'
  _PIPELINETASKDETAIL_PIPELINETASKSTATUS.fields_by_name['update_time']._options = None
  _PIPELINETASKDETAIL_PIPELINETASKSTATUS.fields_by_name['update_time']._serialized_options = b'\342A\001\003'
  _PIPELINETASKDETAIL_PIPELINETASKSTATUS.fields_by_name['state']._options = None
  _PIPELINETASKDETAIL_PIPELINETASKSTATUS.fields_by_name['state']._serialized_options = b'\342A\001\003'
  _PIPELINETASKDETAIL_PIPELINETASKSTATUS.fields_by_name['error']._options = None
  _PIPELINETASKDETAIL_PIPELINETASKSTATUS.fields_by_name['error']._serialized_options = b'\342A\001\003'
  _PIPELINETASKDETAIL_ARTIFACTLIST.fields_by_name['artifacts']._options = None
  _PIPELINETASKDETAIL_ARTIFACTLIST.fields_by_name['artifacts']._serialized_options = b'\342A\001\003'
  _PIPELINETASKDETAIL_INPUTSENTRY._options = None
  _PIPELINETASKDETAIL_INPUTSENTRY._serialized_options = b'8\001'
  _PIPELINETASKDETAIL_OUTPUTSENTRY._options = None
  _PIPELINETASKDETAIL_OUTPUTSENTRY._serialized_options = b'8\001'
  _PIPELINETASKDETAIL.fields_by_name['task_id']._options = None
  _PIPELINETASKDETAIL.fields_by_name['task_id']._serialized_options = b'\342A\001\003'
  _PIPELINETASKDETAIL.fields_by_name['parent_task_id']._options = None
  _PIPELINETASKDETAIL.fields_by_name['parent_task_id']._serialized_options = b'\342A\001\003'
  _PIPELINETASKDETAIL.fields_by_name['task_name']._options = None
  _PIPELINETASKDETAIL.fields_by_name['task_name']._serialized_options = b'\342A\001\003'
  _PIPELINETASKDETAIL.fields_by_name['create_time']._options = None
  _PIPELINETASKDETAIL.fields_by_name['create_time']._serialized_options = b'\342A\001\003'
  _PIPELINETASKDETAIL.fields_by_name['start_time']._options = None
  _PIPELINETASKDETAIL.fields_by_name['start_time']._serialized_options = b'\342A\001\003'
  _PIPELINETASKDETAIL.fields_by_name['end_time']._options = None
  _PIPELINETASKDETAIL.fields_by_name['end_time']._serialized_options = b'\342A\001\003'
  _PIPELINETASKDETAIL.fields_by_name['executor_detail']._options = None
  _PIPELINETASKDETAIL.fields_by_name['executor_detail']._serialized_options = b'\342A\001\003'
  _PIPELINETASKDETAIL.fields_by_name['state']._options = None
  _PIPELINETASKDETAIL.fields_by_name['state']._serialized_options = b'\342A\001\003'
  _PIPELINETASKDETAIL.fields_by_name['execution']._options = None
  _PIPELINETASKDETAIL.fields_by_name['execution']._serialized_options = b'\342A\001\003'
  _PIPELINETASKDETAIL.fields_by_name['error']._options = None
  _PIPELINETASKDETAIL.fields_by_name['error']._serialized_options = b'\342A\001\003'
  _PIPELINETASKDETAIL.fields_by_name['pipeline_task_status']._options = None
  _PIPELINETASKDETAIL.fields_by_name['pipeline_task_status']._serialized_options = b'\342A\001\003'
  _PIPELINETASKDETAIL.fields_by_name['inputs']._options = None
  _PIPELINETASKDETAIL.fields_by_name['inputs']._serialized_options = b'\342A\001\003'
  _PIPELINETASKDETAIL.fields_by_name['outputs']._options = None
  _PIPELINETASKDETAIL.fields_by_name['outputs']._serialized_options = b'\342A\001\003'
  _PIPELINETASKEXECUTORDETAIL_CONTAINERDETAIL.fields_by_name['main_job']._options = None
  _PIPELINETASKEXECUTORDETAIL_CONTAINERDETAIL.fields_by_name['main_job']._serialized_options = b'\342A\001\003\372A%\n#aiplatform.googleapis.com/CustomJob'
  _PIPELINETASKEXECUTORDETAIL_CONTAINERDETAIL.fields_by_name['pre_caching_check_job']._options = None
  _PIPELINETASKEXECUTORDETAIL_CONTAINERDETAIL.fields_by_name['pre_caching_check_job']._serialized_options = b'\342A\001\003\372A%\n#aiplatform.googleapis.com/CustomJob'
  _PIPELINETASKEXECUTORDETAIL_CUSTOMJOBDETAIL.fields_by_name['job']._options = None
  _PIPELINETASKEXECUTORDETAIL_CUSTOMJOBDETAIL.fields_by_name['job']._serialized_options = b'\342A\001\003\372A%\n#aiplatform.googleapis.com/CustomJob'
  _PIPELINETASKEXECUTORDETAIL_CUSTOMJOBDETAIL._options = None
  _PIPELINETASKEXECUTORDETAIL_CUSTOMJOBDETAIL._serialized_options = b'\030\001'
  _PIPELINETASKEXECUTORDETAIL.fields_by_name['container_detail']._options = None
  _PIPELINETASKEXECUTORDETAIL.fields_by_name['container_detail']._serialized_options = b'\342A\001\003'
  _PIPELINETASKEXECUTORDETAIL.fields_by_name['custom_job_detail']._options = None
  _PIPELINETASKEXECUTORDETAIL.fields_by_name['custom_job_detail']._serialized_options = b'\030\001\342A\001\003'
  _PIPELINEJOB._serialized_start=524
  _PIPELINEJOB._serialized_end=2151
  _PIPELINEJOB_RUNTIMECONFIG._serialized_start=1492
  _PIPELINEJOB_RUNTIMECONFIG._serialized_end=1979
  _PIPELINEJOB_RUNTIMECONFIG_PARAMETERSENTRY._serialized_start=1791
  _PIPELINEJOB_RUNTIMECONFIG_PARAMETERSENTRY._serialized_end=1887
  _PIPELINEJOB_RUNTIMECONFIG_PARAMETERVALUESENTRY._serialized_start=1889
  _PIPELINEJOB_RUNTIMECONFIG_PARAMETERVALUESENTRY._serialized_end=1979
  _PIPELINEJOB_LABELSENTRY._serialized_start=1981
  _PIPELINEJOB_LABELSENTRY._serialized_end=2038
  _PIPELINEJOBDETAIL._serialized_start=2154
  _PIPELINEJOBDETAIL._serialized_end=2441
  _PIPELINETASKDETAIL._serialized_start=2444
  _PIPELINETASKDETAIL._serialized_end=4101
  _PIPELINETASKDETAIL_PIPELINETASKSTATUS._serialized_start=3384
  _PIPELINETASKDETAIL_PIPELINETASKSTATUS._serialized_end=3601
  _PIPELINETASKDETAIL_ARTIFACTLIST._serialized_start=3603
  _PIPELINETASKDETAIL_ARTIFACTLIST._serialized_end=3691
  _PIPELINETASKDETAIL_INPUTSENTRY._serialized_start=3693
  _PIPELINETASKDETAIL_INPUTSENTRY._serialized_end=3811
  _PIPELINETASKDETAIL_OUTPUTSENTRY._serialized_start=3813
  _PIPELINETASKDETAIL_OUTPUTSENTRY._serialized_end=3932
  _PIPELINETASKDETAIL_STATE._serialized_start=3935
  _PIPELINETASKDETAIL_STATE._serialized_end=4101
  _PIPELINETASKEXECUTORDETAIL._serialized_start=4104
  _PIPELINETASKEXECUTORDETAIL._serialized_end=4669
  _PIPELINETASKEXECUTORDETAIL_CONTAINERDETAIL._serialized_start=4384
  _PIPELINETASKEXECUTORDETAIL_CONTAINERDETAIL._serialized_end=4571
  _PIPELINETASKEXECUTORDETAIL_CUSTOMJOBDETAIL._serialized_start=4573
  _PIPELINETASKEXECUTORDETAIL_CUSTOMJOBDETAIL._serialized_end=4658
# @@protoc_insertion_point(module_scope)
