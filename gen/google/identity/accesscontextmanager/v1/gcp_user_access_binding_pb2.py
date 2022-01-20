# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/identity/accesscontextmanager/v1/gcp_user_access_binding.proto
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
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nEgoogle/identity/accesscontextmanager/v1/gcp_user_access_binding.proto\x12\'google.identity.accesscontextmanager.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1cgoogle/api/annotations.proto\"\xc2\x02\n\x14GcpUserAccessBinding\x12\x18\n\x04name\x18\x01 \x01(\tB\x04\xe2\x41\x01\x05R\x04name\x12\"\n\tgroup_key\x18\x02 \x01(\tB\x05\xe2\x41\x02\x02\x05R\x08groupKey\x12]\n\raccess_levels\x18\x03 \x03(\tB8\xe2\x41\x01\x02\xfa\x41\x31\n/accesscontextmanager.googleapis.com/AccessLevelR\x0c\x61\x63\x63\x65ssLevels:\x8c\x01\xea\x41\x88\x01\n8accesscontextmanager.googleapis.com/GcpUserAccessBinding\x12Lorganizations/{organization}/gcpUserAccessBindings/{gcp_user_access_binding}B\xaf\x02\n+com.google.identity.accesscontextmanager.v1B\x19GcpUserAccessBindingProtoP\x01Z[google.golang.org/genproto/googleapis/identity/accesscontextmanager/v1;accesscontextmanager\xa2\x02\x04GACM\xaa\x02\'Google.Identity.AccessContextManager.V1\xca\x02\'Google\\Identity\\AccessContextManager\\V1\xea\x02*Google::Identity::AccessContextManager::V1b\x06proto3')



_GCPUSERACCESSBINDING = DESCRIPTOR.message_types_by_name['GcpUserAccessBinding']
GcpUserAccessBinding = _reflection.GeneratedProtocolMessageType('GcpUserAccessBinding', (_message.Message,), {
  'DESCRIPTOR' : _GCPUSERACCESSBINDING,
  '__module__' : 'google.identity.accesscontextmanager.v1.gcp_user_access_binding_pb2'
  # @@protoc_insertion_point(class_scope:google.identity.accesscontextmanager.v1.GcpUserAccessBinding)
  })
_sym_db.RegisterMessage(GcpUserAccessBinding)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n+com.google.identity.accesscontextmanager.v1B\031GcpUserAccessBindingProtoP\001Z[google.golang.org/genproto/googleapis/identity/accesscontextmanager/v1;accesscontextmanager\242\002\004GACM\252\002\'Google.Identity.AccessContextManager.V1\312\002\'Google\\Identity\\AccessContextManager\\V1\352\002*Google::Identity::AccessContextManager::V1'
  _GCPUSERACCESSBINDING.fields_by_name['name']._options = None
  _GCPUSERACCESSBINDING.fields_by_name['name']._serialized_options = b'\342A\001\005'
  _GCPUSERACCESSBINDING.fields_by_name['group_key']._options = None
  _GCPUSERACCESSBINDING.fields_by_name['group_key']._serialized_options = b'\342A\002\002\005'
  _GCPUSERACCESSBINDING.fields_by_name['access_levels']._options = None
  _GCPUSERACCESSBINDING.fields_by_name['access_levels']._serialized_options = b'\342A\001\002\372A1\n/accesscontextmanager.googleapis.com/AccessLevel'
  _GCPUSERACCESSBINDING._options = None
  _GCPUSERACCESSBINDING._serialized_options = b'\352A\210\001\n8accesscontextmanager.googleapis.com/GcpUserAccessBinding\022Lorganizations/{organization}/gcpUserAccessBindings/{gcp_user_access_binding}'
  _GCPUSERACCESSBINDING._serialized_start=205
  _GCPUSERACCESSBINDING._serialized_end=527
# @@protoc_insertion_point(module_scope)
