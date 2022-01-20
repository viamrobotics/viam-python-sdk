# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/aiplatform/v1/data_labeling_job.proto
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
from google.cloud.aiplatform.v1 import accelerator_type_pb2 as google_dot_cloud_dot_aiplatform_dot_v1_dot_accelerator__type__pb2
from google.cloud.aiplatform.v1 import encryption_spec_pb2 as google_dot_cloud_dot_aiplatform_dot_v1_dot_encryption__spec__pb2
from google.cloud.aiplatform.v1 import job_state_pb2 as google_dot_cloud_dot_aiplatform_dot_v1_dot_job__state__pb2
from google.cloud.aiplatform.v1 import specialist_pool_pb2 as google_dot_cloud_dot_aiplatform_dot_v1_dot_specialist__pool__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
from google.type import money_pb2 as google_dot_type_dot_money__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2google/cloud/aiplatform/v1/data_labeling_job.proto\x12\x1agoogle.cloud.aiplatform.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x31google/cloud/aiplatform/v1/accelerator_type.proto\x1a\x30google/cloud/aiplatform/v1/encryption_spec.proto\x1a*google/cloud/aiplatform/v1/job_state.proto\x1a\x30google/cloud/aiplatform/v1/specialist_pool.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x17google/rpc/status.proto\x1a\x17google/type/money.proto\x1a\x1cgoogle/api/annotations.proto\"\xef\n\n\x0f\x44\x61taLabelingJob\x12\x18\n\x04name\x18\x01 \x01(\tB\x04\xe2\x41\x01\x03R\x04name\x12\'\n\x0c\x64isplay_name\x18\x02 \x01(\tB\x04\xe2\x41\x01\x02R\x0b\x64isplayName\x12\x46\n\x08\x64\x61tasets\x18\x03 \x03(\tB*\xe2\x41\x01\x02\xfa\x41#\n!aiplatform.googleapis.com/DatasetR\x08\x64\x61tasets\x12n\n\x11\x61nnotation_labels\x18\x0c \x03(\x0b\x32\x41.google.cloud.aiplatform.v1.DataLabelingJob.AnnotationLabelsEntryR\x10\x61nnotationLabels\x12)\n\rlabeler_count\x18\x04 \x01(\x05\x42\x04\xe2\x41\x01\x02R\x0clabelerCount\x12-\n\x0finstruction_uri\x18\x05 \x01(\tB\x04\xe2\x41\x01\x02R\x0einstructionUri\x12\x30\n\x11inputs_schema_uri\x18\x06 \x01(\tB\x04\xe2\x41\x01\x02R\x0finputsSchemaUri\x12\x34\n\x06inputs\x18\x07 \x01(\x0b\x32\x16.google.protobuf.ValueB\x04\xe2\x41\x01\x02R\x06inputs\x12@\n\x05state\x18\x08 \x01(\x0e\x32$.google.cloud.aiplatform.v1.JobStateB\x04\xe2\x41\x01\x03R\x05state\x12\x31\n\x11labeling_progress\x18\r \x01(\x05\x42\x04\xe2\x41\x01\x03R\x10labelingProgress\x12=\n\rcurrent_spend\x18\x0e \x01(\x0b\x32\x12.google.type.MoneyB\x04\xe2\x41\x01\x03R\x0c\x63urrentSpend\x12\x41\n\x0b\x63reate_time\x18\t \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x04\xe2\x41\x01\x03R\ncreateTime\x12\x41\n\x0bupdate_time\x18\n \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x04\xe2\x41\x01\x03R\nupdateTime\x12.\n\x05\x65rror\x18\x16 \x01(\x0b\x32\x12.google.rpc.StatusB\x04\xe2\x41\x01\x03R\x05\x65rror\x12O\n\x06labels\x18\x0b \x03(\x0b\x32\x37.google.cloud.aiplatform.v1.DataLabelingJob.LabelsEntryR\x06labels\x12)\n\x10specialist_pools\x18\x10 \x03(\tR\x0fspecialistPools\x12S\n\x0f\x65ncryption_spec\x18\x14 \x01(\x0b\x32*.google.cloud.aiplatform.v1.EncryptionSpecR\x0e\x65ncryptionSpec\x12\x66\n\x16\x61\x63tive_learning_config\x18\x15 \x01(\x0b\x32\x30.google.cloud.aiplatform.v1.ActiveLearningConfigR\x14\x61\x63tiveLearningConfig\x1a\x43\n\x15\x41nnotationLabelsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01\x1a\x39\n\x0bLabelsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01:|\xea\x41y\n)aiplatform.googleapis.com/DataLabelingJob\x12Lprojects/{project}/locations/{location}/dataLabelingJobs/{data_labeling_job}\"\xbf\x02\n\x14\x41\x63tiveLearningConfig\x12/\n\x13max_data_item_count\x18\x01 \x01(\x03H\x00R\x10maxDataItemCount\x12\x39\n\x18max_data_item_percentage\x18\x02 \x01(\x05H\x00R\x15maxDataItemPercentage\x12M\n\rsample_config\x18\x03 \x01(\x0b\x32(.google.cloud.aiplatform.v1.SampleConfigR\x0csampleConfig\x12S\n\x0ftraining_config\x18\x04 \x01(\x0b\x32*.google.cloud.aiplatform.v1.TrainingConfigR\x0etrainingConfigB\x17\n\x15human_labeling_budget\"\x86\x03\n\x0cSampleConfig\x12G\n\x1finitial_batch_sample_percentage\x18\x01 \x01(\x05H\x00R\x1cinitialBatchSamplePercentage\x12K\n!following_batch_sample_percentage\x18\x03 \x01(\x05H\x01R\x1e\x66ollowingBatchSamplePercentage\x12`\n\x0fsample_strategy\x18\x05 \x01(\x0e\x32\x37.google.cloud.aiplatform.v1.SampleConfig.SampleStrategyR\x0esampleStrategy\"B\n\x0eSampleStrategy\x12\x1f\n\x1bSAMPLE_STRATEGY_UNSPECIFIED\x10\x00\x12\x0f\n\x0bUNCERTAINTY\x10\x01\x42\x1b\n\x19initial_batch_sample_sizeB\x1d\n\x1b\x66ollowing_batch_sample_size\"Q\n\x0eTrainingConfig\x12?\n\x1ctimeout_training_milli_hours\x18\x01 \x01(\x03R\x19timeoutTrainingMilliHoursB\xd8\x01\n\x1e\x63om.google.cloud.aiplatform.v1B\x14\x44\x61taLabelingJobProtoP\x01ZDgoogle.golang.org/genproto/googleapis/cloud/aiplatform/v1;aiplatform\xaa\x02\x1aGoogle.Cloud.AIPlatform.V1\xca\x02\x1aGoogle\\Cloud\\AIPlatform\\V1\xea\x02\x1dGoogle::Cloud::AIPlatform::V1b\x06proto3')



_DATALABELINGJOB = DESCRIPTOR.message_types_by_name['DataLabelingJob']
_DATALABELINGJOB_ANNOTATIONLABELSENTRY = _DATALABELINGJOB.nested_types_by_name['AnnotationLabelsEntry']
_DATALABELINGJOB_LABELSENTRY = _DATALABELINGJOB.nested_types_by_name['LabelsEntry']
_ACTIVELEARNINGCONFIG = DESCRIPTOR.message_types_by_name['ActiveLearningConfig']
_SAMPLECONFIG = DESCRIPTOR.message_types_by_name['SampleConfig']
_TRAININGCONFIG = DESCRIPTOR.message_types_by_name['TrainingConfig']
_SAMPLECONFIG_SAMPLESTRATEGY = _SAMPLECONFIG.enum_types_by_name['SampleStrategy']
DataLabelingJob = _reflection.GeneratedProtocolMessageType('DataLabelingJob', (_message.Message,), {

  'AnnotationLabelsEntry' : _reflection.GeneratedProtocolMessageType('AnnotationLabelsEntry', (_message.Message,), {
    'DESCRIPTOR' : _DATALABELINGJOB_ANNOTATIONLABELSENTRY,
    '__module__' : 'google.cloud.aiplatform.v1.data_labeling_job_pb2'
    # @@protoc_insertion_point(class_scope:google.cloud.aiplatform.v1.DataLabelingJob.AnnotationLabelsEntry)
    })
  ,

  'LabelsEntry' : _reflection.GeneratedProtocolMessageType('LabelsEntry', (_message.Message,), {
    'DESCRIPTOR' : _DATALABELINGJOB_LABELSENTRY,
    '__module__' : 'google.cloud.aiplatform.v1.data_labeling_job_pb2'
    # @@protoc_insertion_point(class_scope:google.cloud.aiplatform.v1.DataLabelingJob.LabelsEntry)
    })
  ,
  'DESCRIPTOR' : _DATALABELINGJOB,
  '__module__' : 'google.cloud.aiplatform.v1.data_labeling_job_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.aiplatform.v1.DataLabelingJob)
  })
_sym_db.RegisterMessage(DataLabelingJob)
_sym_db.RegisterMessage(DataLabelingJob.AnnotationLabelsEntry)
_sym_db.RegisterMessage(DataLabelingJob.LabelsEntry)

ActiveLearningConfig = _reflection.GeneratedProtocolMessageType('ActiveLearningConfig', (_message.Message,), {
  'DESCRIPTOR' : _ACTIVELEARNINGCONFIG,
  '__module__' : 'google.cloud.aiplatform.v1.data_labeling_job_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.aiplatform.v1.ActiveLearningConfig)
  })
_sym_db.RegisterMessage(ActiveLearningConfig)

SampleConfig = _reflection.GeneratedProtocolMessageType('SampleConfig', (_message.Message,), {
  'DESCRIPTOR' : _SAMPLECONFIG,
  '__module__' : 'google.cloud.aiplatform.v1.data_labeling_job_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.aiplatform.v1.SampleConfig)
  })
_sym_db.RegisterMessage(SampleConfig)

TrainingConfig = _reflection.GeneratedProtocolMessageType('TrainingConfig', (_message.Message,), {
  'DESCRIPTOR' : _TRAININGCONFIG,
  '__module__' : 'google.cloud.aiplatform.v1.data_labeling_job_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.aiplatform.v1.TrainingConfig)
  })
_sym_db.RegisterMessage(TrainingConfig)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\036com.google.cloud.aiplatform.v1B\024DataLabelingJobProtoP\001ZDgoogle.golang.org/genproto/googleapis/cloud/aiplatform/v1;aiplatform\252\002\032Google.Cloud.AIPlatform.V1\312\002\032Google\\Cloud\\AIPlatform\\V1\352\002\035Google::Cloud::AIPlatform::V1'
  _DATALABELINGJOB_ANNOTATIONLABELSENTRY._options = None
  _DATALABELINGJOB_ANNOTATIONLABELSENTRY._serialized_options = b'8\001'
  _DATALABELINGJOB_LABELSENTRY._options = None
  _DATALABELINGJOB_LABELSENTRY._serialized_options = b'8\001'
  _DATALABELINGJOB.fields_by_name['name']._options = None
  _DATALABELINGJOB.fields_by_name['name']._serialized_options = b'\342A\001\003'
  _DATALABELINGJOB.fields_by_name['display_name']._options = None
  _DATALABELINGJOB.fields_by_name['display_name']._serialized_options = b'\342A\001\002'
  _DATALABELINGJOB.fields_by_name['datasets']._options = None
  _DATALABELINGJOB.fields_by_name['datasets']._serialized_options = b'\342A\001\002\372A#\n!aiplatform.googleapis.com/Dataset'
  _DATALABELINGJOB.fields_by_name['labeler_count']._options = None
  _DATALABELINGJOB.fields_by_name['labeler_count']._serialized_options = b'\342A\001\002'
  _DATALABELINGJOB.fields_by_name['instruction_uri']._options = None
  _DATALABELINGJOB.fields_by_name['instruction_uri']._serialized_options = b'\342A\001\002'
  _DATALABELINGJOB.fields_by_name['inputs_schema_uri']._options = None
  _DATALABELINGJOB.fields_by_name['inputs_schema_uri']._serialized_options = b'\342A\001\002'
  _DATALABELINGJOB.fields_by_name['inputs']._options = None
  _DATALABELINGJOB.fields_by_name['inputs']._serialized_options = b'\342A\001\002'
  _DATALABELINGJOB.fields_by_name['state']._options = None
  _DATALABELINGJOB.fields_by_name['state']._serialized_options = b'\342A\001\003'
  _DATALABELINGJOB.fields_by_name['labeling_progress']._options = None
  _DATALABELINGJOB.fields_by_name['labeling_progress']._serialized_options = b'\342A\001\003'
  _DATALABELINGJOB.fields_by_name['current_spend']._options = None
  _DATALABELINGJOB.fields_by_name['current_spend']._serialized_options = b'\342A\001\003'
  _DATALABELINGJOB.fields_by_name['create_time']._options = None
  _DATALABELINGJOB.fields_by_name['create_time']._serialized_options = b'\342A\001\003'
  _DATALABELINGJOB.fields_by_name['update_time']._options = None
  _DATALABELINGJOB.fields_by_name['update_time']._serialized_options = b'\342A\001\003'
  _DATALABELINGJOB.fields_by_name['error']._options = None
  _DATALABELINGJOB.fields_by_name['error']._serialized_options = b'\342A\001\003'
  _DATALABELINGJOB._options = None
  _DATALABELINGJOB._serialized_options = b'\352Ay\n)aiplatform.googleapis.com/DataLabelingJob\022Lprojects/{project}/locations/{location}/dataLabelingJobs/{data_labeling_job}'
  _DATALABELINGJOB._serialized_start=481
  _DATALABELINGJOB._serialized_end=1872
  _DATALABELINGJOB_ANNOTATIONLABELSENTRY._serialized_start=1620
  _DATALABELINGJOB_ANNOTATIONLABELSENTRY._serialized_end=1687
  _DATALABELINGJOB_LABELSENTRY._serialized_start=1689
  _DATALABELINGJOB_LABELSENTRY._serialized_end=1746
  _ACTIVELEARNINGCONFIG._serialized_start=1875
  _ACTIVELEARNINGCONFIG._serialized_end=2194
  _SAMPLECONFIG._serialized_start=2197
  _SAMPLECONFIG._serialized_end=2587
  _SAMPLECONFIG_SAMPLESTRATEGY._serialized_start=2461
  _SAMPLECONFIG_SAMPLESTRATEGY._serialized_end=2527
  _TRAININGCONFIG._serialized_start=2589
  _TRAININGCONFIG._serialized_end=2670
# @@protoc_insertion_point(module_scope)
