# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/api/routing.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18google/api/routing.proto\x12\ngoogle.api\x1a google/protobuf/descriptor.proto\"Z\n\x0bRoutingRule\x12K\n\x12routing_parameters\x18\x02 \x03(\x0b\x32\x1c.google.api.RoutingParameterR\x11routingParameters\"M\n\x10RoutingParameter\x12\x14\n\x05\x66ield\x18\x01 \x01(\tR\x05\x66ield\x12#\n\rpath_template\x18\x02 \x01(\tR\x0cpathTemplate:T\n\x07routing\x12\x1e.google.protobuf.MethodOptions\x18\xb1\xca\xbc\" \x01(\x0b\x32\x17.google.api.RoutingRuleR\x07routingBj\n\x0e\x63om.google.apiB\x0cRoutingProtoP\x01ZAgoogle.golang.org/genproto/googleapis/api/annotations;annotations\xa2\x02\x04GAPIb\x06proto3')


ROUTING_FIELD_NUMBER = 72295729
routing = DESCRIPTOR.extensions_by_name['routing']

_ROUTINGRULE = DESCRIPTOR.message_types_by_name['RoutingRule']
_ROUTINGPARAMETER = DESCRIPTOR.message_types_by_name['RoutingParameter']
RoutingRule = _reflection.GeneratedProtocolMessageType('RoutingRule', (_message.Message,), {
  'DESCRIPTOR' : _ROUTINGRULE,
  '__module__' : 'google.api.routing_pb2'
  # @@protoc_insertion_point(class_scope:google.api.RoutingRule)
  })
_sym_db.RegisterMessage(RoutingRule)

RoutingParameter = _reflection.GeneratedProtocolMessageType('RoutingParameter', (_message.Message,), {
  'DESCRIPTOR' : _ROUTINGPARAMETER,
  '__module__' : 'google.api.routing_pb2'
  # @@protoc_insertion_point(class_scope:google.api.RoutingParameter)
  })
_sym_db.RegisterMessage(RoutingParameter)

if _descriptor._USE_C_DESCRIPTORS == False:
  google_dot_protobuf_dot_descriptor__pb2.MethodOptions.RegisterExtension(routing)

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\016com.google.apiB\014RoutingProtoP\001ZAgoogle.golang.org/genproto/googleapis/api/annotations;annotations\242\002\004GAPI'
  _ROUTINGRULE._serialized_start=74
  _ROUTINGRULE._serialized_end=164
  _ROUTINGPARAMETER._serialized_start=166
  _ROUTINGPARAMETER._serialized_end=243
# @@protoc_insertion_point(module_scope)
