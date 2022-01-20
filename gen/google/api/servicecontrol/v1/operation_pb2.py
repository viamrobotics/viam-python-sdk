# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/api/servicecontrol/v1/operation.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api.servicecontrol.v1 import log_entry_pb2 as google_dot_api_dot_servicecontrol_dot_v1_dot_log__entry__pb2
from google.api.servicecontrol.v1 import metric_value_pb2 as google_dot_api_dot_servicecontrol_dot_v1_dot_metric__value__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,google/api/servicecontrol/v1/operation.proto\x12\x1cgoogle.api.servicecontrol.v1\x1a,google/api/servicecontrol/v1/log_entry.proto\x1a/google/api/servicecontrol/v1/metric_value.proto\x1a\x19google/protobuf/any.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xbe\x05\n\tOperation\x12!\n\x0coperation_id\x18\x01 \x01(\tR\x0boperationId\x12%\n\x0eoperation_name\x18\x02 \x01(\tR\roperationName\x12\x1f\n\x0b\x63onsumer_id\x18\x03 \x01(\tR\nconsumerId\x12\x39\n\nstart_time\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\tstartTime\x12\x35\n\x08\x65nd_time\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x07\x65ndTime\x12K\n\x06labels\x18\x06 \x03(\x0b\x32\x33.google.api.servicecontrol.v1.Operation.LabelsEntryR\x06labels\x12X\n\x11metric_value_sets\x18\x07 \x03(\x0b\x32,.google.api.servicecontrol.v1.MetricValueSetR\x0fmetricValueSets\x12G\n\x0blog_entries\x18\x08 \x03(\x0b\x32&.google.api.servicecontrol.v1.LogEntryR\nlogEntries\x12R\n\nimportance\x18\x0b \x01(\x0e\x32\x32.google.api.servicecontrol.v1.Operation.ImportanceR\nimportance\x12\x34\n\nextensions\x18\x10 \x03(\x0b\x32\x14.google.protobuf.AnyR\nextensions\x1a\x39\n\x0bLabelsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01\"\x1f\n\nImportance\x12\x07\n\x03LOW\x10\x00\x12\x08\n\x04HIGH\x10\x01\x42\xe9\x01\n com.google.api.servicecontrol.v1B\x0eOperationProtoP\x01ZJgoogle.golang.org/genproto/googleapis/api/servicecontrol/v1;servicecontrol\xf8\x01\x01\xaa\x02\x1eGoogle.Cloud.ServiceControl.V1\xca\x02\x1eGoogle\\Cloud\\ServiceControl\\V1\xea\x02!Google::Cloud::ServiceControl::V1b\x06proto3')



_OPERATION = DESCRIPTOR.message_types_by_name['Operation']
_OPERATION_LABELSENTRY = _OPERATION.nested_types_by_name['LabelsEntry']
_OPERATION_IMPORTANCE = _OPERATION.enum_types_by_name['Importance']
Operation = _reflection.GeneratedProtocolMessageType('Operation', (_message.Message,), {

  'LabelsEntry' : _reflection.GeneratedProtocolMessageType('LabelsEntry', (_message.Message,), {
    'DESCRIPTOR' : _OPERATION_LABELSENTRY,
    '__module__' : 'google.api.servicecontrol.v1.operation_pb2'
    # @@protoc_insertion_point(class_scope:google.api.servicecontrol.v1.Operation.LabelsEntry)
    })
  ,
  'DESCRIPTOR' : _OPERATION,
  '__module__' : 'google.api.servicecontrol.v1.operation_pb2'
  # @@protoc_insertion_point(class_scope:google.api.servicecontrol.v1.Operation)
  })
_sym_db.RegisterMessage(Operation)
_sym_db.RegisterMessage(Operation.LabelsEntry)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n com.google.api.servicecontrol.v1B\016OperationProtoP\001ZJgoogle.golang.org/genproto/googleapis/api/servicecontrol/v1;servicecontrol\370\001\001\252\002\036Google.Cloud.ServiceControl.V1\312\002\036Google\\Cloud\\ServiceControl\\V1\352\002!Google::Cloud::ServiceControl::V1'
  _OPERATION_LABELSENTRY._options = None
  _OPERATION_LABELSENTRY._serialized_options = b'8\001'
  _OPERATION._serialized_start=234
  _OPERATION._serialized_end=936
  _OPERATION_LABELSENTRY._serialized_start=846
  _OPERATION_LABELSENTRY._serialized_end=903
  _OPERATION_IMPORTANCE._serialized_start=905
  _OPERATION_IMPORTANCE._serialized_end=936
# @@protoc_insertion_point(module_scope)
