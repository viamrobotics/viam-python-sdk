# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/integrations/v1alpha/event_parameter.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.cloud.integrations.v1alpha import value_type_pb2 as google_dot_cloud_dot_integrations_dot_v1alpha_dot_value__type__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n7google/cloud/integrations/v1alpha/event_parameter.proto\x12!google.cloud.integrations.v1alpha\x1a\x32google/cloud/integrations/v1alpha/value_type.proto\"f\n\x0e\x45ventParameter\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x42\n\x05value\x18\x02 \x01(\x0b\x32,.google.cloud.integrations.v1alpha.ValueTypeR\x05valueB\x8d\x01\n%com.google.cloud.integrations.v1alphaB\x13\x45ventParameterProtoP\x01ZMgoogle.golang.org/genproto/googleapis/cloud/integrations/v1alpha;integrationsb\x06proto3')



_EVENTPARAMETER = DESCRIPTOR.message_types_by_name['EventParameter']
EventParameter = _reflection.GeneratedProtocolMessageType('EventParameter', (_message.Message,), {
  'DESCRIPTOR' : _EVENTPARAMETER,
  '__module__' : 'google.cloud.integrations.v1alpha.event_parameter_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.integrations.v1alpha.EventParameter)
  })
_sym_db.RegisterMessage(EventParameter)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n%com.google.cloud.integrations.v1alphaB\023EventParameterProtoP\001ZMgoogle.golang.org/genproto/googleapis/cloud/integrations/v1alpha;integrations'
  _EVENTPARAMETER._serialized_start=146
  _EVENTPARAMETER._serialized_end=248
# @@protoc_insertion_point(module_scope)
