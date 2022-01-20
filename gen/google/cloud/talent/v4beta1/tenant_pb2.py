# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/talent/v4beta1/tenant.proto
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
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(google/cloud/talent/v4beta1/tenant.proto\x12\x1bgoogle.cloud.talent.v4beta1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1cgoogle/api/annotations.proto\"\x8b\x03\n\x06Tenant\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12%\n\x0b\x65xternal_id\x18\x02 \x01(\tB\x04\xe2\x41\x01\x02R\nexternalId\x12P\n\nusage_type\x18\x03 \x01(\x0e\x32\x31.google.cloud.talent.v4beta1.Tenant.DataUsageTypeR\tusageType\x12^\n,keyword_searchable_profile_custom_attributes\x18\x04 \x03(\tR(keywordSearchableProfileCustomAttributes\"N\n\rDataUsageType\x12\x1f\n\x1b\x44\x41TA_USAGE_TYPE_UNSPECIFIED\x10\x00\x12\x0e\n\nAGGREGATED\x10\x01\x12\x0c\n\x08ISOLATED\x10\x02:D\xea\x41\x41\n\x1ajobs.googleapis.com/Tenant\x12#projects/{project}/tenants/{tenant}B\x81\x01\n\x1f\x63om.google.cloud.talent.v4beta1B\x13TenantResourceProtoP\x01ZAgoogle.golang.org/genproto/googleapis/cloud/talent/v4beta1;talent\xa2\x02\x03\x43TSb\x06proto3')



_TENANT = DESCRIPTOR.message_types_by_name['Tenant']
_TENANT_DATAUSAGETYPE = _TENANT.enum_types_by_name['DataUsageType']
Tenant = _reflection.GeneratedProtocolMessageType('Tenant', (_message.Message,), {
  'DESCRIPTOR' : _TENANT,
  '__module__' : 'google.cloud.talent.v4beta1.tenant_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.talent.v4beta1.Tenant)
  })
_sym_db.RegisterMessage(Tenant)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\037com.google.cloud.talent.v4beta1B\023TenantResourceProtoP\001ZAgoogle.golang.org/genproto/googleapis/cloud/talent/v4beta1;talent\242\002\003CTS'
  _TENANT.fields_by_name['external_id']._options = None
  _TENANT.fields_by_name['external_id']._serialized_options = b'\342A\001\002'
  _TENANT._options = None
  _TENANT._serialized_options = b'\352AA\n\032jobs.googleapis.com/Tenant\022#projects/{project}/tenants/{tenant}'
  _TENANT._serialized_start=197
  _TENANT._serialized_end=592
  _TENANT_DATAUSAGETYPE._serialized_start=444
  _TENANT_DATAUSAGETYPE._serialized_end=522
# @@protoc_insertion_point(module_scope)
