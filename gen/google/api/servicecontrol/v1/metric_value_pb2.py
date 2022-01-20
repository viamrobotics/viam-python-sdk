# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/api/servicecontrol/v1/metric_value.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api.servicecontrol.v1 import distribution_pb2 as google_dot_api_dot_servicecontrol_dot_v1_dot_distribution__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/google/api/servicecontrol/v1/metric_value.proto\x12\x1cgoogle.api.servicecontrol.v1\x1a/google/api/servicecontrol/v1/distribution.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xfd\x03\n\x0bMetricValue\x12M\n\x06labels\x18\x01 \x03(\x0b\x32\x35.google.api.servicecontrol.v1.MetricValue.LabelsEntryR\x06labels\x12\x39\n\nstart_time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\tstartTime\x12\x35\n\x08\x65nd_time\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x07\x65ndTime\x12\x1f\n\nbool_value\x18\x04 \x01(\x08H\x00R\tboolValue\x12!\n\x0bint64_value\x18\x05 \x01(\x03H\x00R\nint64Value\x12#\n\x0c\x64ouble_value\x18\x06 \x01(\x01H\x00R\x0b\x64oubleValue\x12#\n\x0cstring_value\x18\x07 \x01(\tH\x00R\x0bstringValue\x12[\n\x12\x64istribution_value\x18\x08 \x01(\x0b\x32*.google.api.servicecontrol.v1.DistributionH\x00R\x11\x64istributionValue\x1a\x39\n\x0bLabelsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01\x42\x07\n\x05value\"\x81\x01\n\x0eMetricValueSet\x12\x1f\n\x0bmetric_name\x18\x01 \x01(\tR\nmetricName\x12N\n\rmetric_values\x18\x02 \x03(\x0b\x32).google.api.servicecontrol.v1.MetricValueR\x0cmetricValuesB\xee\x01\n com.google.api.servicecontrol.v1B\x13MetricValueSetProtoP\x01ZJgoogle.golang.org/genproto/googleapis/api/servicecontrol/v1;servicecontrol\xf8\x01\x01\xaa\x02\x1eGoogle.Cloud.ServiceControl.V1\xca\x02\x1eGoogle\\Cloud\\ServiceControl\\V1\xea\x02!Google::Cloud::ServiceControl::V1b\x06proto3')



_METRICVALUE = DESCRIPTOR.message_types_by_name['MetricValue']
_METRICVALUE_LABELSENTRY = _METRICVALUE.nested_types_by_name['LabelsEntry']
_METRICVALUESET = DESCRIPTOR.message_types_by_name['MetricValueSet']
MetricValue = _reflection.GeneratedProtocolMessageType('MetricValue', (_message.Message,), {

  'LabelsEntry' : _reflection.GeneratedProtocolMessageType('LabelsEntry', (_message.Message,), {
    'DESCRIPTOR' : _METRICVALUE_LABELSENTRY,
    '__module__' : 'google.api.servicecontrol.v1.metric_value_pb2'
    # @@protoc_insertion_point(class_scope:google.api.servicecontrol.v1.MetricValue.LabelsEntry)
    })
  ,
  'DESCRIPTOR' : _METRICVALUE,
  '__module__' : 'google.api.servicecontrol.v1.metric_value_pb2'
  # @@protoc_insertion_point(class_scope:google.api.servicecontrol.v1.MetricValue)
  })
_sym_db.RegisterMessage(MetricValue)
_sym_db.RegisterMessage(MetricValue.LabelsEntry)

MetricValueSet = _reflection.GeneratedProtocolMessageType('MetricValueSet', (_message.Message,), {
  'DESCRIPTOR' : _METRICVALUESET,
  '__module__' : 'google.api.servicecontrol.v1.metric_value_pb2'
  # @@protoc_insertion_point(class_scope:google.api.servicecontrol.v1.MetricValueSet)
  })
_sym_db.RegisterMessage(MetricValueSet)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n com.google.api.servicecontrol.v1B\023MetricValueSetProtoP\001ZJgoogle.golang.org/genproto/googleapis/api/servicecontrol/v1;servicecontrol\370\001\001\252\002\036Google.Cloud.ServiceControl.V1\312\002\036Google\\Cloud\\ServiceControl\\V1\352\002!Google::Cloud::ServiceControl::V1'
  _METRICVALUE_LABELSENTRY._options = None
  _METRICVALUE_LABELSENTRY._serialized_options = b'8\001'
  _METRICVALUE._serialized_start=164
  _METRICVALUE._serialized_end=673
  _METRICVALUE_LABELSENTRY._serialized_start=607
  _METRICVALUE_LABELSENTRY._serialized_end=664
  _METRICVALUESET._serialized_start=676
  _METRICVALUESET._serialized_end=805
# @@protoc_insertion_point(module_scope)
