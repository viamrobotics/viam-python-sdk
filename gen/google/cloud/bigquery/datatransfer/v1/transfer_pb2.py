# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/bigquery/datatransfer/v1/transfer.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n4google/cloud/bigquery/datatransfer/v1/transfer.proto\x12%google.cloud.bigquery.datatransfer.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x17google/rpc/status.proto\"D\n\x10\x45mailPreferences\x12\x30\n\x14\x65nable_failure_email\x18\x01 \x01(\x08R\x12\x65nableFailureEmail\"\xbb\x01\n\x0fScheduleOptions\x12\x36\n\x17\x64isable_auto_scheduling\x18\x03 \x01(\x08R\x15\x64isableAutoScheduling\x12\x39\n\nstart_time\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\tstartTime\x12\x35\n\x08\x65nd_time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x07\x65ndTime\"/\n\x08UserInfo\x12\x19\n\x05\x65mail\x18\x01 \x01(\tH\x00R\x05\x65mail\x88\x01\x01\x42\x08\n\x06_email\"\xa2\t\n\x0eTransferConfig\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x36\n\x16\x64\x65stination_dataset_id\x18\x02 \x01(\tH\x00R\x14\x64\x65stinationDatasetId\x12!\n\x0c\x64isplay_name\x18\x03 \x01(\tR\x0b\x64isplayName\x12$\n\x0e\x64\x61ta_source_id\x18\x05 \x01(\tR\x0c\x64\x61taSourceId\x12/\n\x06params\x18\t \x01(\x0b\x32\x17.google.protobuf.StructR\x06params\x12\x1a\n\x08schedule\x18\x07 \x01(\tR\x08schedule\x12\x61\n\x10schedule_options\x18\x18 \x01(\x0b\x32\x36.google.cloud.bigquery.datatransfer.v1.ScheduleOptionsR\x0fscheduleOptions\x12\x37\n\x18\x64\x61ta_refresh_window_days\x18\x0c \x01(\x05R\x15\x64\x61taRefreshWindowDays\x12\x1a\n\x08\x64isabled\x18\r \x01(\x08R\x08\x64isabled\x12\x41\n\x0bupdate_time\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x04\xe2\x41\x01\x03R\nupdateTime\x12\x44\n\rnext_run_time\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x04\xe2\x41\x01\x03R\x0bnextRunTime\x12P\n\x05state\x18\n \x01(\x0e\x32\x34.google.cloud.bigquery.datatransfer.v1.TransferStateB\x04\xe2\x41\x01\x03R\x05state\x12\x17\n\x07user_id\x18\x0b \x01(\x03R\x06userId\x12+\n\x0e\x64\x61taset_region\x18\x0e \x01(\tB\x04\xe2\x41\x01\x03R\rdatasetRegion\x12:\n\x19notification_pubsub_topic\x18\x0f \x01(\tR\x17notificationPubsubTopic\x12\x64\n\x11\x65mail_preferences\x18\x12 \x01(\x0b\x32\x37.google.cloud.bigquery.datatransfer.v1.EmailPreferencesR\x10\x65mailPreferences\x12Y\n\nowner_info\x18\x1b \x01(\x0b\x32/.google.cloud.bigquery.datatransfer.v1.UserInfoB\x04\xe2\x41\x01\x03H\x01R\townerInfo\x88\x01\x01:\xb9\x01\xea\x41\xb5\x01\n2bigquerydatatransfer.googleapis.com/TransferConfig\x12\x34projects/{project}/transferConfigs/{transfer_config}\x12Iprojects/{project}/locations/{location}/transferConfigs/{transfer_config}B\r\n\x0b\x64\x65stinationB\r\n\x0b_owner_info\"\xbd\x08\n\x0bTransferRun\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12?\n\rschedule_time\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x0cscheduleTime\x12\x35\n\x08run_time\x18\n \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x07runTime\x12\x35\n\x0c\x65rror_status\x18\x15 \x01(\x0b\x32\x12.google.rpc.StatusR\x0b\x65rrorStatus\x12?\n\nstart_time\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x04\xe2\x41\x01\x03R\tstartTime\x12;\n\x08\x65nd_time\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x04\xe2\x41\x01\x03R\x07\x65ndTime\x12\x41\n\x0bupdate_time\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x04\xe2\x41\x01\x03R\nupdateTime\x12\x35\n\x06params\x18\t \x01(\x0b\x32\x17.google.protobuf.StructB\x04\xe2\x41\x01\x03R\x06params\x12<\n\x16\x64\x65stination_dataset_id\x18\x02 \x01(\tB\x04\xe2\x41\x01\x03H\x00R\x14\x64\x65stinationDatasetId\x12*\n\x0e\x64\x61ta_source_id\x18\x07 \x01(\tB\x04\xe2\x41\x01\x03R\x0c\x64\x61taSourceId\x12J\n\x05state\x18\x08 \x01(\x0e\x32\x34.google.cloud.bigquery.datatransfer.v1.TransferStateR\x05state\x12\x17\n\x07user_id\x18\x0b \x01(\x03R\x06userId\x12 \n\x08schedule\x18\x0c \x01(\tB\x04\xe2\x41\x01\x03R\x08schedule\x12@\n\x19notification_pubsub_topic\x18\x17 \x01(\tB\x04\xe2\x41\x01\x03R\x17notificationPubsubTopic\x12j\n\x11\x65mail_preferences\x18\x19 \x01(\x0b\x32\x37.google.cloud.bigquery.datatransfer.v1.EmailPreferencesB\x04\xe2\x41\x01\x03R\x10\x65mailPreferences:\xc4\x01\xea\x41\xc0\x01\n\'bigquerydatatransfer.googleapis.com/Run\x12?projects/{project}/transferConfigs/{transfer_config}/runs/{run}\x12Tprojects/{project}/locations/{location}/transferConfigs/{transfer_config}/runs/{run}B\r\n\x0b\x64\x65stination\"\xae\x02\n\x0fTransferMessage\x12=\n\x0cmessage_time\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x0bmessageTime\x12\x62\n\x08severity\x18\x02 \x01(\x0e\x32\x46.google.cloud.bigquery.datatransfer.v1.TransferMessage.MessageSeverityR\x08severity\x12!\n\x0cmessage_text\x18\x03 \x01(\tR\x0bmessageText\"U\n\x0fMessageSeverity\x12 \n\x1cMESSAGE_SEVERITY_UNSPECIFIED\x10\x00\x12\x08\n\x04INFO\x10\x01\x12\x0b\n\x07WARNING\x10\x02\x12\t\n\x05\x45RROR\x10\x03*K\n\x0cTransferType\x12\x1d\n\x19TRANSFER_TYPE_UNSPECIFIED\x10\x00\x12\t\n\x05\x42\x41TCH\x10\x01\x12\r\n\tSTREAMING\x10\x02\x1a\x02\x18\x01*s\n\rTransferState\x12\x1e\n\x1aTRANSFER_STATE_UNSPECIFIED\x10\x00\x12\x0b\n\x07PENDING\x10\x02\x12\x0b\n\x07RUNNING\x10\x03\x12\r\n\tSUCCEEDED\x10\x04\x12\n\n\x06\x46\x41ILED\x10\x05\x12\r\n\tCANCELLED\x10\x06\x42\x93\x02\n)com.google.cloud.bigquery.datatransfer.v1B\rTransferProtoP\x01ZQgoogle.golang.org/genproto/googleapis/cloud/bigquery/datatransfer/v1;datatransfer\xa2\x02\x05GCBDT\xaa\x02%Google.Cloud.BigQuery.DataTransfer.V1\xca\x02%Google\\Cloud\\BigQuery\\DataTransfer\\V1\xea\x02)Google::Cloud::Bigquery::DataTransfer::V1b\x06proto3')

_TRANSFERTYPE = DESCRIPTOR.enum_types_by_name['TransferType']
TransferType = enum_type_wrapper.EnumTypeWrapper(_TRANSFERTYPE)
_TRANSFERSTATE = DESCRIPTOR.enum_types_by_name['TransferState']
TransferState = enum_type_wrapper.EnumTypeWrapper(_TRANSFERSTATE)
TRANSFER_TYPE_UNSPECIFIED = 0
BATCH = 1
STREAMING = 2
TRANSFER_STATE_UNSPECIFIED = 0
PENDING = 2
RUNNING = 3
SUCCEEDED = 4
FAILED = 5
CANCELLED = 6


_EMAILPREFERENCES = DESCRIPTOR.message_types_by_name['EmailPreferences']
_SCHEDULEOPTIONS = DESCRIPTOR.message_types_by_name['ScheduleOptions']
_USERINFO = DESCRIPTOR.message_types_by_name['UserInfo']
_TRANSFERCONFIG = DESCRIPTOR.message_types_by_name['TransferConfig']
_TRANSFERRUN = DESCRIPTOR.message_types_by_name['TransferRun']
_TRANSFERMESSAGE = DESCRIPTOR.message_types_by_name['TransferMessage']
_TRANSFERMESSAGE_MESSAGESEVERITY = _TRANSFERMESSAGE.enum_types_by_name['MessageSeverity']
EmailPreferences = _reflection.GeneratedProtocolMessageType('EmailPreferences', (_message.Message,), {
  'DESCRIPTOR' : _EMAILPREFERENCES,
  '__module__' : 'google.cloud.bigquery.datatransfer.v1.transfer_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.bigquery.datatransfer.v1.EmailPreferences)
  })
_sym_db.RegisterMessage(EmailPreferences)

ScheduleOptions = _reflection.GeneratedProtocolMessageType('ScheduleOptions', (_message.Message,), {
  'DESCRIPTOR' : _SCHEDULEOPTIONS,
  '__module__' : 'google.cloud.bigquery.datatransfer.v1.transfer_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.bigquery.datatransfer.v1.ScheduleOptions)
  })
_sym_db.RegisterMessage(ScheduleOptions)

UserInfo = _reflection.GeneratedProtocolMessageType('UserInfo', (_message.Message,), {
  'DESCRIPTOR' : _USERINFO,
  '__module__' : 'google.cloud.bigquery.datatransfer.v1.transfer_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.bigquery.datatransfer.v1.UserInfo)
  })
_sym_db.RegisterMessage(UserInfo)

TransferConfig = _reflection.GeneratedProtocolMessageType('TransferConfig', (_message.Message,), {
  'DESCRIPTOR' : _TRANSFERCONFIG,
  '__module__' : 'google.cloud.bigquery.datatransfer.v1.transfer_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.bigquery.datatransfer.v1.TransferConfig)
  })
_sym_db.RegisterMessage(TransferConfig)

TransferRun = _reflection.GeneratedProtocolMessageType('TransferRun', (_message.Message,), {
  'DESCRIPTOR' : _TRANSFERRUN,
  '__module__' : 'google.cloud.bigquery.datatransfer.v1.transfer_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.bigquery.datatransfer.v1.TransferRun)
  })
_sym_db.RegisterMessage(TransferRun)

TransferMessage = _reflection.GeneratedProtocolMessageType('TransferMessage', (_message.Message,), {
  'DESCRIPTOR' : _TRANSFERMESSAGE,
  '__module__' : 'google.cloud.bigquery.datatransfer.v1.transfer_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.bigquery.datatransfer.v1.TransferMessage)
  })
_sym_db.RegisterMessage(TransferMessage)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n)com.google.cloud.bigquery.datatransfer.v1B\rTransferProtoP\001ZQgoogle.golang.org/genproto/googleapis/cloud/bigquery/datatransfer/v1;datatransfer\242\002\005GCBDT\252\002%Google.Cloud.BigQuery.DataTransfer.V1\312\002%Google\\Cloud\\BigQuery\\DataTransfer\\V1\352\002)Google::Cloud::Bigquery::DataTransfer::V1'
  _TRANSFERTYPE._options = None
  _TRANSFERTYPE._serialized_options = b'\030\001'
  _TRANSFERCONFIG.fields_by_name['update_time']._options = None
  _TRANSFERCONFIG.fields_by_name['update_time']._serialized_options = b'\342A\001\003'
  _TRANSFERCONFIG.fields_by_name['next_run_time']._options = None
  _TRANSFERCONFIG.fields_by_name['next_run_time']._serialized_options = b'\342A\001\003'
  _TRANSFERCONFIG.fields_by_name['state']._options = None
  _TRANSFERCONFIG.fields_by_name['state']._serialized_options = b'\342A\001\003'
  _TRANSFERCONFIG.fields_by_name['dataset_region']._options = None
  _TRANSFERCONFIG.fields_by_name['dataset_region']._serialized_options = b'\342A\001\003'
  _TRANSFERCONFIG.fields_by_name['owner_info']._options = None
  _TRANSFERCONFIG.fields_by_name['owner_info']._serialized_options = b'\342A\001\003'
  _TRANSFERCONFIG._options = None
  _TRANSFERCONFIG._serialized_options = b'\352A\265\001\n2bigquerydatatransfer.googleapis.com/TransferConfig\0224projects/{project}/transferConfigs/{transfer_config}\022Iprojects/{project}/locations/{location}/transferConfigs/{transfer_config}'
  _TRANSFERRUN.fields_by_name['start_time']._options = None
  _TRANSFERRUN.fields_by_name['start_time']._serialized_options = b'\342A\001\003'
  _TRANSFERRUN.fields_by_name['end_time']._options = None
  _TRANSFERRUN.fields_by_name['end_time']._serialized_options = b'\342A\001\003'
  _TRANSFERRUN.fields_by_name['update_time']._options = None
  _TRANSFERRUN.fields_by_name['update_time']._serialized_options = b'\342A\001\003'
  _TRANSFERRUN.fields_by_name['params']._options = None
  _TRANSFERRUN.fields_by_name['params']._serialized_options = b'\342A\001\003'
  _TRANSFERRUN.fields_by_name['destination_dataset_id']._options = None
  _TRANSFERRUN.fields_by_name['destination_dataset_id']._serialized_options = b'\342A\001\003'
  _TRANSFERRUN.fields_by_name['data_source_id']._options = None
  _TRANSFERRUN.fields_by_name['data_source_id']._serialized_options = b'\342A\001\003'
  _TRANSFERRUN.fields_by_name['schedule']._options = None
  _TRANSFERRUN.fields_by_name['schedule']._serialized_options = b'\342A\001\003'
  _TRANSFERRUN.fields_by_name['notification_pubsub_topic']._options = None
  _TRANSFERRUN.fields_by_name['notification_pubsub_topic']._serialized_options = b'\342A\001\003'
  _TRANSFERRUN.fields_by_name['email_preferences']._options = None
  _TRANSFERRUN.fields_by_name['email_preferences']._serialized_options = b'\342A\001\003'
  _TRANSFERRUN._options = None
  _TRANSFERRUN._serialized_options = b'\352A\300\001\n\'bigquerydatatransfer.googleapis.com/Run\022?projects/{project}/transferConfigs/{transfer_config}/runs/{run}\022Tprojects/{project}/locations/{location}/transferConfigs/{transfer_config}/runs/{run}'
  _TRANSFERTYPE._serialized_start=3166
  _TRANSFERTYPE._serialized_end=3241
  _TRANSFERSTATE._serialized_start=3243
  _TRANSFERSTATE._serialized_end=3358
  _EMAILPREFERENCES._serialized_start=275
  _EMAILPREFERENCES._serialized_end=343
  _SCHEDULEOPTIONS._serialized_start=346
  _SCHEDULEOPTIONS._serialized_end=533
  _USERINFO._serialized_start=535
  _USERINFO._serialized_end=582
  _TRANSFERCONFIG._serialized_start=585
  _TRANSFERCONFIG._serialized_end=1771
  _TRANSFERRUN._serialized_start=1774
  _TRANSFERRUN._serialized_end=2859
  _TRANSFERMESSAGE._serialized_start=2862
  _TRANSFERMESSAGE._serialized_end=3164
  _TRANSFERMESSAGE_MESSAGESEVERITY._serialized_start=3079
  _TRANSFERMESSAGE_MESSAGESEVERITY._serialized_end=3164
# @@protoc_insertion_point(module_scope)
