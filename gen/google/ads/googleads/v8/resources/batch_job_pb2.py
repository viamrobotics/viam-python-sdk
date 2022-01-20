# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v8/resources/batch_job.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.googleads.v8.enums import batch_job_status_pb2 as google_dot_ads_dot_googleads_dot_v8_dot_enums_dot_batch__job__status__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1google/ads/googleads/v8/resources/batch_job.proto\x12!google.ads.googleads.v8.resources\x1a\x34google/ads/googleads/v8/enums/batch_job_status.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1cgoogle/api/annotations.proto\"\xe5\x08\n\x08\x42\x61tchJob\x12O\n\rresource_name\x18\x01 \x01(\tB*\xe2\x41\x01\x05\xfa\x41#\n!googleads.googleapis.com/BatchJobR\x0cresourceName\x12\x19\n\x02id\x18\x07 \x01(\x03\x42\x04\xe2\x41\x01\x03H\x00R\x02id\x88\x01\x01\x12@\n\x17next_add_sequence_token\x18\x08 \x01(\tB\x04\xe2\x41\x01\x03H\x01R\x14nextAddSequenceToken\x88\x01\x01\x12^\n\x08metadata\x18\x04 \x01(\x0b\x32<.google.ads.googleads.v8.resources.BatchJob.BatchJobMetadataB\x04\xe2\x41\x01\x03R\x08metadata\x12^\n\x06status\x18\x05 \x01(\x0e\x32@.google.ads.googleads.v8.enums.BatchJobStatusEnum.BatchJobStatusB\x04\xe2\x41\x01\x03R\x06status\x12?\n\x16long_running_operation\x18\t \x01(\tB\x04\xe2\x41\x01\x03H\x02R\x14longRunningOperation\x88\x01\x01\x1a\x91\x04\n\x10\x42\x61tchJobMetadata\x12\x37\n\x12\x63reation_date_time\x18\x08 \x01(\tB\x04\xe2\x41\x01\x03H\x00R\x10\x63reationDateTime\x88\x01\x01\x12\x31\n\x0fstart_date_time\x18\x07 \x01(\tB\x04\xe2\x41\x01\x03H\x01R\rstartDateTime\x88\x01\x01\x12;\n\x14\x63ompletion_date_time\x18\t \x01(\tB\x04\xe2\x41\x01\x03H\x02R\x12\x63ompletionDateTime\x88\x01\x01\x12G\n\x1a\x65stimated_completion_ratio\x18\n \x01(\x01\x42\x04\xe2\x41\x01\x03H\x03R\x18\x65stimatedCompletionRatio\x88\x01\x01\x12\x32\n\x0foperation_count\x18\x0b \x01(\x03\x42\x04\xe2\x41\x01\x03H\x04R\x0eoperationCount\x88\x01\x01\x12\x43\n\x18\x65xecuted_operation_count\x18\x0c \x01(\x03\x42\x04\xe2\x41\x01\x03H\x05R\x16\x65xecutedOperationCount\x88\x01\x01\x42\x15\n\x13_creation_date_timeB\x12\n\x10_start_date_timeB\x17\n\x15_completion_date_timeB\x1d\n\x1b_estimated_completion_ratioB\x12\n\x10_operation_countB\x1b\n\x19_executed_operation_count:X\xea\x41U\n!googleads.googleapis.com/BatchJob\x12\x30\x63ustomers/{customer_id}/batchJobs/{batch_job_id}B\x05\n\x03_idB\x1a\n\x18_next_add_sequence_tokenB\x19\n\x17_long_running_operationB\xfa\x01\n%com.google.ads.googleads.v8.resourcesB\rBatchJobProtoP\x01ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v8/resources;resources\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V8.Resources\xca\x02!Google\\Ads\\GoogleAds\\V8\\Resources\xea\x02%Google::Ads::GoogleAds::V8::Resourcesb\x06proto3')



_BATCHJOB = DESCRIPTOR.message_types_by_name['BatchJob']
_BATCHJOB_BATCHJOBMETADATA = _BATCHJOB.nested_types_by_name['BatchJobMetadata']
BatchJob = _reflection.GeneratedProtocolMessageType('BatchJob', (_message.Message,), {

  'BatchJobMetadata' : _reflection.GeneratedProtocolMessageType('BatchJobMetadata', (_message.Message,), {
    'DESCRIPTOR' : _BATCHJOB_BATCHJOBMETADATA,
    '__module__' : 'google.ads.googleads.v8.resources.batch_job_pb2'
    # @@protoc_insertion_point(class_scope:google.ads.googleads.v8.resources.BatchJob.BatchJobMetadata)
    })
  ,
  'DESCRIPTOR' : _BATCHJOB,
  '__module__' : 'google.ads.googleads.v8.resources.batch_job_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v8.resources.BatchJob)
  })
_sym_db.RegisterMessage(BatchJob)
_sym_db.RegisterMessage(BatchJob.BatchJobMetadata)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n%com.google.ads.googleads.v8.resourcesB\rBatchJobProtoP\001ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v8/resources;resources\242\002\003GAA\252\002!Google.Ads.GoogleAds.V8.Resources\312\002!Google\\Ads\\GoogleAds\\V8\\Resources\352\002%Google::Ads::GoogleAds::V8::Resources'
  _BATCHJOB_BATCHJOBMETADATA.fields_by_name['creation_date_time']._options = None
  _BATCHJOB_BATCHJOBMETADATA.fields_by_name['creation_date_time']._serialized_options = b'\342A\001\003'
  _BATCHJOB_BATCHJOBMETADATA.fields_by_name['start_date_time']._options = None
  _BATCHJOB_BATCHJOBMETADATA.fields_by_name['start_date_time']._serialized_options = b'\342A\001\003'
  _BATCHJOB_BATCHJOBMETADATA.fields_by_name['completion_date_time']._options = None
  _BATCHJOB_BATCHJOBMETADATA.fields_by_name['completion_date_time']._serialized_options = b'\342A\001\003'
  _BATCHJOB_BATCHJOBMETADATA.fields_by_name['estimated_completion_ratio']._options = None
  _BATCHJOB_BATCHJOBMETADATA.fields_by_name['estimated_completion_ratio']._serialized_options = b'\342A\001\003'
  _BATCHJOB_BATCHJOBMETADATA.fields_by_name['operation_count']._options = None
  _BATCHJOB_BATCHJOBMETADATA.fields_by_name['operation_count']._serialized_options = b'\342A\001\003'
  _BATCHJOB_BATCHJOBMETADATA.fields_by_name['executed_operation_count']._options = None
  _BATCHJOB_BATCHJOBMETADATA.fields_by_name['executed_operation_count']._serialized_options = b'\342A\001\003'
  _BATCHJOB.fields_by_name['resource_name']._options = None
  _BATCHJOB.fields_by_name['resource_name']._serialized_options = b'\342A\001\005\372A#\n!googleads.googleapis.com/BatchJob'
  _BATCHJOB.fields_by_name['id']._options = None
  _BATCHJOB.fields_by_name['id']._serialized_options = b'\342A\001\003'
  _BATCHJOB.fields_by_name['next_add_sequence_token']._options = None
  _BATCHJOB.fields_by_name['next_add_sequence_token']._serialized_options = b'\342A\001\003'
  _BATCHJOB.fields_by_name['metadata']._options = None
  _BATCHJOB.fields_by_name['metadata']._serialized_options = b'\342A\001\003'
  _BATCHJOB.fields_by_name['status']._options = None
  _BATCHJOB.fields_by_name['status']._serialized_options = b'\342A\001\003'
  _BATCHJOB.fields_by_name['long_running_operation']._options = None
  _BATCHJOB.fields_by_name['long_running_operation']._serialized_options = b'\342A\001\003'
  _BATCHJOB._options = None
  _BATCHJOB._serialized_options = b'\352AU\n!googleads.googleapis.com/BatchJob\0220customers/{customer_id}/batchJobs/{batch_job_id}'
  _BATCHJOB._serialized_start=233
  _BATCHJOB._serialized_end=1358
  _BATCHJOB_BATCHJOBMETADATA._serialized_start=677
  _BATCHJOB_BATCHJOBMETADATA._serialized_end=1206
# @@protoc_insertion_point(module_scope)
