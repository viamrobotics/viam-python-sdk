# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/datacatalog/v1/gcs_fileset_spec.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.cloud.datacatalog.v1 import timestamps_pb2 as google_dot_cloud_dot_datacatalog_dot_v1_dot_timestamps__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2google/cloud/datacatalog/v1/gcs_fileset_spec.proto\x12\x1bgoogle.cloud.datacatalog.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a,google/cloud/datacatalog/v1/timestamps.proto\"\x9e\x01\n\x0eGcsFilesetSpec\x12)\n\rfile_patterns\x18\x01 \x03(\tB\x04\xe2\x41\x01\x02R\x0c\x66ilePatterns\x12\x61\n\x15sample_gcs_file_specs\x18\x02 \x03(\x0b\x32(.google.cloud.datacatalog.v1.GcsFileSpecB\x04\xe2\x41\x01\x03R\x12sampleGcsFileSpecs\"\xb1\x01\n\x0bGcsFileSpec\x12!\n\tfile_path\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02R\x08\x66ilePath\x12Z\n\x0egcs_timestamps\x18\x02 \x01(\x0b\x32-.google.cloud.datacatalog.v1.SystemTimestampsB\x04\xe2\x41\x01\x03R\rgcsTimestamps\x12#\n\nsize_bytes\x18\x04 \x01(\x03\x42\x04\xe2\x41\x01\x03R\tsizeBytesB\xcb\x01\n\x1f\x63om.google.cloud.datacatalog.v1P\x01ZFgoogle.golang.org/genproto/googleapis/cloud/datacatalog/v1;datacatalog\xf8\x01\x01\xaa\x02\x1bGoogle.Cloud.DataCatalog.V1\xca\x02\x1bGoogle\\Cloud\\DataCatalog\\V1\xea\x02\x1eGoogle::Cloud::DataCatalog::V1b\x06proto3')



_GCSFILESETSPEC = DESCRIPTOR.message_types_by_name['GcsFilesetSpec']
_GCSFILESPEC = DESCRIPTOR.message_types_by_name['GcsFileSpec']
GcsFilesetSpec = _reflection.GeneratedProtocolMessageType('GcsFilesetSpec', (_message.Message,), {
  'DESCRIPTOR' : _GCSFILESETSPEC,
  '__module__' : 'google.cloud.datacatalog.v1.gcs_fileset_spec_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.datacatalog.v1.GcsFilesetSpec)
  })
_sym_db.RegisterMessage(GcsFilesetSpec)

GcsFileSpec = _reflection.GeneratedProtocolMessageType('GcsFileSpec', (_message.Message,), {
  'DESCRIPTOR' : _GCSFILESPEC,
  '__module__' : 'google.cloud.datacatalog.v1.gcs_fileset_spec_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.datacatalog.v1.GcsFileSpec)
  })
_sym_db.RegisterMessage(GcsFileSpec)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\037com.google.cloud.datacatalog.v1P\001ZFgoogle.golang.org/genproto/googleapis/cloud/datacatalog/v1;datacatalog\370\001\001\252\002\033Google.Cloud.DataCatalog.V1\312\002\033Google\\Cloud\\DataCatalog\\V1\352\002\036Google::Cloud::DataCatalog::V1'
  _GCSFILESETSPEC.fields_by_name['file_patterns']._options = None
  _GCSFILESETSPEC.fields_by_name['file_patterns']._serialized_options = b'\342A\001\002'
  _GCSFILESETSPEC.fields_by_name['sample_gcs_file_specs']._options = None
  _GCSFILESETSPEC.fields_by_name['sample_gcs_file_specs']._serialized_options = b'\342A\001\003'
  _GCSFILESPEC.fields_by_name['file_path']._options = None
  _GCSFILESPEC.fields_by_name['file_path']._serialized_options = b'\342A\001\002'
  _GCSFILESPEC.fields_by_name['gcs_timestamps']._options = None
  _GCSFILESPEC.fields_by_name['gcs_timestamps']._serialized_options = b'\342A\001\003'
  _GCSFILESPEC.fields_by_name['size_bytes']._options = None
  _GCSFILESPEC.fields_by_name['size_bytes']._serialized_options = b'\342A\001\003'
  _GCSFILESETSPEC._serialized_start=163
  _GCSFILESETSPEC._serialized_end=321
  _GCSFILESPEC._serialized_start=324
  _GCSFILESPEC._serialized_end=501
# @@protoc_insertion_point(module_scope)
