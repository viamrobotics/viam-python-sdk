# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/integrations/v1alpha/log_entries.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.cloud.integrations.v1alpha import event_parameter_pb2 as google_dot_cloud_dot_integrations_dot_v1alpha_dot_event__parameter__pb2
from google.cloud.integrations.v1alpha import product_pb2 as google_dot_cloud_dot_integrations_dot_v1alpha_dot_product__pb2
from google.cloud.integrations.v1alpha import task_config_pb2 as google_dot_cloud_dot_integrations_dot_v1alpha_dot_task__config__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3google/cloud/integrations/v1alpha/log_entries.proto\x12!google.cloud.integrations.v1alpha\x1a\x37google/cloud/integrations/v1alpha/event_parameter.proto\x1a/google/cloud/integrations/v1alpha/product.proto\x1a\x33google/cloud/integrations/v1alpha/task_config.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xaf\t\n\rExecutionInfo\x12\x35\n\x17\x65vent_execution_info_id\x18\x01 \x01(\tR\x14\x65ventExecutionInfoId\x12 \n\x0bintegration\x18\x02 \x01(\tR\x0bintegration\x12/\n\x13integration_version\x18\x03 \x01(\tR\x12integrationVersion\x12\x1d\n\nproject_id\x18\x04 \x01(\tR\tprojectId\x12\x1d\n\ntrigger_id\x18\x05 \x01(\tR\ttriggerId\x12j\n\x0erequest_params\x18\x06 \x03(\x0b\x32\x43.google.cloud.integrations.v1alpha.ExecutionInfo.RequestParamsEntryR\rrequestParams\x12m\n\x0fresponse_params\x18\x07 \x03(\x0b\x32\x44.google.cloud.integrations.v1alpha.ExecutionInfo.ResponseParamsEntryR\x0eresponseParams\x12\\\n\x0bpost_method\x18\x08 \x01(\x0e\x32;.google.cloud.integrations.v1alpha.ExecutionInfo.PostMethodR\npostMethod\x12p\n\x17\x65vent_execution_details\x18\t \x01(\x0b\x32\x38.google.cloud.integrations.v1alpha.EventExecutionDetailsR\x15\x65ventExecutionDetails\x12\x46\n\x06\x65rrors\x18\n \x03(\x0b\x32..google.cloud.integrations.v1alpha.ErrorDetailR\x06\x65rrors\x12\x44\n\x07product\x18\x0b \x01(\x0e\x32*.google.cloud.integrations.v1alpha.ProductR\x07product\x12\x1d\n\nrequest_id\x18\x0c \x01(\tR\trequestId\x12P\n\x0ctask_configs\x18\r \x03(\x0b\x32-.google.cloud.integrations.v1alpha.TaskConfigR\x0btaskConfigs\x1as\n\x12RequestParamsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12G\n\x05value\x18\x02 \x01(\x0b\x32\x31.google.cloud.integrations.v1alpha.EventParameterR\x05value:\x02\x38\x01\x1at\n\x13ResponseParamsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12G\n\x05value\x18\x02 \x01(\x0b\x32\x31.google.cloud.integrations.v1alpha.EventParameterR\x05value:\x02\x38\x01\"A\n\nPostMethod\x12\x1b\n\x17POST_METHOD_UNSPECIFIED\x10\x00\x12\x08\n\x04POST\x10\x01\x12\x0c\n\x08SCHEDULE\x10\x02\"\x94\x05\n\x15\x45ventExecutionDetails\x12\x80\x01\n\x15\x65vent_execution_state\x18\x01 \x01(\x0e\x32L.google.cloud.integrations.v1alpha.EventExecutionDetails.EventExecutionStateR\x13\x65ventExecutionState\x12s\n\x18\x65vent_execution_snapshot\x18\x02 \x03(\x0b\x32\x39.google.cloud.integrations.v1alpha.EventExecutionSnapshotR\x16\x65ventExecutionSnapshot\x12_\n\x13\x65vent_attempt_stats\x18\x03 \x03(\x0b\x32/.google.cloud.integrations.v1alpha.AttemptStatsR\x11\x65ventAttemptStats\x12J\n\x13next_execution_time\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x11nextExecutionTime\x12.\n\x13\x65vent_retries_count\x18\x05 \x01(\x05R\x11\x65ventRetriesCount\"\xa5\x01\n\x13\x45ventExecutionState\x12%\n!EVENT_EXECUTION_STATE_UNSPECIFIED\x10\x00\x12\x0b\n\x07ON_HOLD\x10\x01\x12\x0e\n\nIN_PROCESS\x10\x02\x12\r\n\tSUCCEEDED\x10\x03\x12\n\n\x06\x46\x41ILED\x10\x04\x12\r\n\tCANCELLED\x10\x05\x12\x11\n\rRETRY_ON_HOLD\x10\x06\x12\r\n\tSUSPENDED\x10\x07\"\xf3\x08\n\x16\x45ventExecutionSnapshot\x12\x34\n\x16\x63heckpoint_task_number\x18\x01 \x01(\tR\x14\x63heckpointTaskNumber\x12?\n\rsnapshot_time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x0csnapshotTime\x12\xa3\x01\n!event_execution_snapshot_metadata\x18\x03 \x01(\x0b\x32X.google.cloud.integrations.v1alpha.EventExecutionSnapshot.EventExecutionSnapshotMetadataR\x1e\x65ventExecutionSnapshotMetadata\x12m\n\x16task_execution_details\x18\x04 \x03(\x0b\x32\x37.google.cloud.integrations.v1alpha.TaskExecutionDetailsR\x14taskExecutionDetails\x12_\n\x11\x63ondition_results\x18\x05 \x03(\x0b\x32\x32.google.cloud.integrations.v1alpha.ConditionResultR\x10\x63onditionResults\x12m\n\x0c\x65vent_params\x18\x06 \x03(\x0b\x32J.google.cloud.integrations.v1alpha.EventExecutionSnapshot.EventParamsEntryR\x0b\x65ventParams\x12j\n\x0b\x64iff_params\x18\x07 \x03(\x0b\x32I.google.cloud.integrations.v1alpha.EventExecutionSnapshot.DiffParamsEntryR\ndiffParams\x1a\xab\x01\n\x1e\x45ventExecutionSnapshotMetadata\x12\x1f\n\x0btask_number\x18\x01 \x01(\tR\ntaskNumber\x12\x12\n\x04task\x18\x02 \x01(\tR\x04task\x12*\n\x11\x65vent_attempt_num\x18\x03 \x01(\x05R\x0f\x65ventAttemptNum\x12(\n\x10task_attempt_num\x18\x04 \x01(\x05R\x0etaskAttemptNum\x1aq\n\x10\x45ventParamsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12G\n\x05value\x18\x02 \x01(\x0b\x32\x31.google.cloud.integrations.v1alpha.EventParameterR\x05value:\x02\x38\x01\x1ap\n\x0f\x44iffParamsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12G\n\x05value\x18\x02 \x01(\x0b\x32\x31.google.cloud.integrations.v1alpha.EventParameterR\x05value:\x02\x38\x01\"\x99\x04\n\x14TaskExecutionDetails\x12\x1f\n\x0btask_number\x18\x01 \x01(\tR\ntaskNumber\x12|\n\x14task_execution_state\x18\x02 \x01(\x0e\x32J.google.cloud.integrations.v1alpha.TaskExecutionDetails.TaskExecutionStateR\x12taskExecutionState\x12]\n\x12task_attempt_stats\x18\x03 \x03(\x0b\x32/.google.cloud.integrations.v1alpha.AttemptStatsR\x10taskAttemptStats\"\x82\x02\n\x12TaskExecutionState\x12$\n TASK_EXECUTION_STATE_UNSPECIFIED\x10\x00\x12\x15\n\x11PENDING_EXECUTION\x10\x01\x12\x0e\n\nIN_PROCESS\x10\x02\x12\x0b\n\x07SUCCEED\x10\x03\x12\n\n\x06\x46\x41ILED\x10\x04\x12\t\n\x05\x46\x41TAL\x10\x05\x12\x11\n\rRETRY_ON_HOLD\x10\x06\x12\x0b\n\x07SKIPPED\x10\x07\x12\r\n\tCANCELLED\x10\x08\x12\x14\n\x10PENDING_ROLLBACK\x10\t\x12\x17\n\x13ROLLBACK_IN_PROCESS\x10\n\x12\x0e\n\nROLLEDBACK\x10\x0b\x12\r\n\tSUSPENDED\x10\x0c\"\x80\x01\n\x0c\x41ttemptStats\x12\x39\n\nstart_time\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\tstartTime\x12\x35\n\x08\x65nd_time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x07\x65ndTime\"S\n\x0b\x45rrorDetail\x12#\n\rerror_message\x18\x01 \x01(\tR\x0c\x65rrorMessage\x12\x1f\n\x0btask_number\x18\x02 \x01(\x05R\ntaskNumber\"\x83\x01\n\x0f\x43onditionResult\x12.\n\x13\x63urrent_task_number\x18\x01 \x01(\tR\x11\x63urrentTaskNumber\x12(\n\x10next_task_number\x18\x02 \x01(\tR\x0enextTaskNumber\x12\x16\n\x06result\x18\x03 \x01(\x08R\x06resultB\x89\x01\n%com.google.cloud.integrations.v1alphaB\x0fLogEntriesProtoP\x01ZMgoogle.golang.org/genproto/googleapis/cloud/integrations/v1alpha;integrationsb\x06proto3')



_EXECUTIONINFO = DESCRIPTOR.message_types_by_name['ExecutionInfo']
_EXECUTIONINFO_REQUESTPARAMSENTRY = _EXECUTIONINFO.nested_types_by_name['RequestParamsEntry']
_EXECUTIONINFO_RESPONSEPARAMSENTRY = _EXECUTIONINFO.nested_types_by_name['ResponseParamsEntry']
_EVENTEXECUTIONDETAILS = DESCRIPTOR.message_types_by_name['EventExecutionDetails']
_EVENTEXECUTIONSNAPSHOT = DESCRIPTOR.message_types_by_name['EventExecutionSnapshot']
_EVENTEXECUTIONSNAPSHOT_EVENTEXECUTIONSNAPSHOTMETADATA = _EVENTEXECUTIONSNAPSHOT.nested_types_by_name['EventExecutionSnapshotMetadata']
_EVENTEXECUTIONSNAPSHOT_EVENTPARAMSENTRY = _EVENTEXECUTIONSNAPSHOT.nested_types_by_name['EventParamsEntry']
_EVENTEXECUTIONSNAPSHOT_DIFFPARAMSENTRY = _EVENTEXECUTIONSNAPSHOT.nested_types_by_name['DiffParamsEntry']
_TASKEXECUTIONDETAILS = DESCRIPTOR.message_types_by_name['TaskExecutionDetails']
_ATTEMPTSTATS = DESCRIPTOR.message_types_by_name['AttemptStats']
_ERRORDETAIL = DESCRIPTOR.message_types_by_name['ErrorDetail']
_CONDITIONRESULT = DESCRIPTOR.message_types_by_name['ConditionResult']
_EXECUTIONINFO_POSTMETHOD = _EXECUTIONINFO.enum_types_by_name['PostMethod']
_EVENTEXECUTIONDETAILS_EVENTEXECUTIONSTATE = _EVENTEXECUTIONDETAILS.enum_types_by_name['EventExecutionState']
_TASKEXECUTIONDETAILS_TASKEXECUTIONSTATE = _TASKEXECUTIONDETAILS.enum_types_by_name['TaskExecutionState']
ExecutionInfo = _reflection.GeneratedProtocolMessageType('ExecutionInfo', (_message.Message,), {

  'RequestParamsEntry' : _reflection.GeneratedProtocolMessageType('RequestParamsEntry', (_message.Message,), {
    'DESCRIPTOR' : _EXECUTIONINFO_REQUESTPARAMSENTRY,
    '__module__' : 'google.cloud.integrations.v1alpha.log_entries_pb2'
    # @@protoc_insertion_point(class_scope:google.cloud.integrations.v1alpha.ExecutionInfo.RequestParamsEntry)
    })
  ,

  'ResponseParamsEntry' : _reflection.GeneratedProtocolMessageType('ResponseParamsEntry', (_message.Message,), {
    'DESCRIPTOR' : _EXECUTIONINFO_RESPONSEPARAMSENTRY,
    '__module__' : 'google.cloud.integrations.v1alpha.log_entries_pb2'
    # @@protoc_insertion_point(class_scope:google.cloud.integrations.v1alpha.ExecutionInfo.ResponseParamsEntry)
    })
  ,
  'DESCRIPTOR' : _EXECUTIONINFO,
  '__module__' : 'google.cloud.integrations.v1alpha.log_entries_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.integrations.v1alpha.ExecutionInfo)
  })
_sym_db.RegisterMessage(ExecutionInfo)
_sym_db.RegisterMessage(ExecutionInfo.RequestParamsEntry)
_sym_db.RegisterMessage(ExecutionInfo.ResponseParamsEntry)

EventExecutionDetails = _reflection.GeneratedProtocolMessageType('EventExecutionDetails', (_message.Message,), {
  'DESCRIPTOR' : _EVENTEXECUTIONDETAILS,
  '__module__' : 'google.cloud.integrations.v1alpha.log_entries_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.integrations.v1alpha.EventExecutionDetails)
  })
_sym_db.RegisterMessage(EventExecutionDetails)

EventExecutionSnapshot = _reflection.GeneratedProtocolMessageType('EventExecutionSnapshot', (_message.Message,), {

  'EventExecutionSnapshotMetadata' : _reflection.GeneratedProtocolMessageType('EventExecutionSnapshotMetadata', (_message.Message,), {
    'DESCRIPTOR' : _EVENTEXECUTIONSNAPSHOT_EVENTEXECUTIONSNAPSHOTMETADATA,
    '__module__' : 'google.cloud.integrations.v1alpha.log_entries_pb2'
    # @@protoc_insertion_point(class_scope:google.cloud.integrations.v1alpha.EventExecutionSnapshot.EventExecutionSnapshotMetadata)
    })
  ,

  'EventParamsEntry' : _reflection.GeneratedProtocolMessageType('EventParamsEntry', (_message.Message,), {
    'DESCRIPTOR' : _EVENTEXECUTIONSNAPSHOT_EVENTPARAMSENTRY,
    '__module__' : 'google.cloud.integrations.v1alpha.log_entries_pb2'
    # @@protoc_insertion_point(class_scope:google.cloud.integrations.v1alpha.EventExecutionSnapshot.EventParamsEntry)
    })
  ,

  'DiffParamsEntry' : _reflection.GeneratedProtocolMessageType('DiffParamsEntry', (_message.Message,), {
    'DESCRIPTOR' : _EVENTEXECUTIONSNAPSHOT_DIFFPARAMSENTRY,
    '__module__' : 'google.cloud.integrations.v1alpha.log_entries_pb2'
    # @@protoc_insertion_point(class_scope:google.cloud.integrations.v1alpha.EventExecutionSnapshot.DiffParamsEntry)
    })
  ,
  'DESCRIPTOR' : _EVENTEXECUTIONSNAPSHOT,
  '__module__' : 'google.cloud.integrations.v1alpha.log_entries_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.integrations.v1alpha.EventExecutionSnapshot)
  })
_sym_db.RegisterMessage(EventExecutionSnapshot)
_sym_db.RegisterMessage(EventExecutionSnapshot.EventExecutionSnapshotMetadata)
_sym_db.RegisterMessage(EventExecutionSnapshot.EventParamsEntry)
_sym_db.RegisterMessage(EventExecutionSnapshot.DiffParamsEntry)

TaskExecutionDetails = _reflection.GeneratedProtocolMessageType('TaskExecutionDetails', (_message.Message,), {
  'DESCRIPTOR' : _TASKEXECUTIONDETAILS,
  '__module__' : 'google.cloud.integrations.v1alpha.log_entries_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.integrations.v1alpha.TaskExecutionDetails)
  })
_sym_db.RegisterMessage(TaskExecutionDetails)

AttemptStats = _reflection.GeneratedProtocolMessageType('AttemptStats', (_message.Message,), {
  'DESCRIPTOR' : _ATTEMPTSTATS,
  '__module__' : 'google.cloud.integrations.v1alpha.log_entries_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.integrations.v1alpha.AttemptStats)
  })
_sym_db.RegisterMessage(AttemptStats)

ErrorDetail = _reflection.GeneratedProtocolMessageType('ErrorDetail', (_message.Message,), {
  'DESCRIPTOR' : _ERRORDETAIL,
  '__module__' : 'google.cloud.integrations.v1alpha.log_entries_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.integrations.v1alpha.ErrorDetail)
  })
_sym_db.RegisterMessage(ErrorDetail)

ConditionResult = _reflection.GeneratedProtocolMessageType('ConditionResult', (_message.Message,), {
  'DESCRIPTOR' : _CONDITIONRESULT,
  '__module__' : 'google.cloud.integrations.v1alpha.log_entries_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.integrations.v1alpha.ConditionResult)
  })
_sym_db.RegisterMessage(ConditionResult)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n%com.google.cloud.integrations.v1alphaB\017LogEntriesProtoP\001ZMgoogle.golang.org/genproto/googleapis/cloud/integrations/v1alpha;integrations'
  _EXECUTIONINFO_REQUESTPARAMSENTRY._options = None
  _EXECUTIONINFO_REQUESTPARAMSENTRY._serialized_options = b'8\001'
  _EXECUTIONINFO_RESPONSEPARAMSENTRY._options = None
  _EXECUTIONINFO_RESPONSEPARAMSENTRY._serialized_options = b'8\001'
  _EVENTEXECUTIONSNAPSHOT_EVENTPARAMSENTRY._options = None
  _EVENTEXECUTIONSNAPSHOT_EVENTPARAMSENTRY._serialized_options = b'8\001'
  _EVENTEXECUTIONSNAPSHOT_DIFFPARAMSENTRY._options = None
  _EVENTEXECUTIONSNAPSHOT_DIFFPARAMSENTRY._serialized_options = b'8\001'
  _EXECUTIONINFO._serialized_start=283
  _EXECUTIONINFO._serialized_end=1482
  _EXECUTIONINFO_REQUESTPARAMSENTRY._serialized_start=1182
  _EXECUTIONINFO_REQUESTPARAMSENTRY._serialized_end=1297
  _EXECUTIONINFO_RESPONSEPARAMSENTRY._serialized_start=1299
  _EXECUTIONINFO_RESPONSEPARAMSENTRY._serialized_end=1415
  _EXECUTIONINFO_POSTMETHOD._serialized_start=1417
  _EXECUTIONINFO_POSTMETHOD._serialized_end=1482
  _EVENTEXECUTIONDETAILS._serialized_start=1485
  _EVENTEXECUTIONDETAILS._serialized_end=2145
  _EVENTEXECUTIONDETAILS_EVENTEXECUTIONSTATE._serialized_start=1980
  _EVENTEXECUTIONDETAILS_EVENTEXECUTIONSTATE._serialized_end=2145
  _EVENTEXECUTIONSNAPSHOT._serialized_start=2148
  _EVENTEXECUTIONSNAPSHOT._serialized_end=3287
  _EVENTEXECUTIONSNAPSHOT_EVENTEXECUTIONSNAPSHOTMETADATA._serialized_start=2887
  _EVENTEXECUTIONSNAPSHOT_EVENTEXECUTIONSNAPSHOTMETADATA._serialized_end=3058
  _EVENTEXECUTIONSNAPSHOT_EVENTPARAMSENTRY._serialized_start=3060
  _EVENTEXECUTIONSNAPSHOT_EVENTPARAMSENTRY._serialized_end=3173
  _EVENTEXECUTIONSNAPSHOT_DIFFPARAMSENTRY._serialized_start=3175
  _EVENTEXECUTIONSNAPSHOT_DIFFPARAMSENTRY._serialized_end=3287
  _TASKEXECUTIONDETAILS._serialized_start=3290
  _TASKEXECUTIONDETAILS._serialized_end=3827
  _TASKEXECUTIONDETAILS_TASKEXECUTIONSTATE._serialized_start=3569
  _TASKEXECUTIONDETAILS_TASKEXECUTIONSTATE._serialized_end=3827
  _ATTEMPTSTATS._serialized_start=3830
  _ATTEMPTSTATS._serialized_end=3958
  _ERRORDETAIL._serialized_start=3960
  _ERRORDETAIL._serialized_end=4043
  _CONDITIONRESULT._serialized_start=4046
  _CONDITIONRESULT._serialized_end=4177
# @@protoc_insertion_point(module_scope)
