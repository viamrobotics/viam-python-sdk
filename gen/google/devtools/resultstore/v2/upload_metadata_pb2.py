# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/devtools/resultstore/v2/upload_metadata.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import resource_pb2 as google_dot_api_dot_resource__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n4google/devtools/resultstore/v2/upload_metadata.proto\x12\x1egoogle.devtools.resultstore.v2\x1a\x19google/api/resource.proto\"\xc7\x01\n\x0eUploadMetadata\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12!\n\x0cresume_token\x18\x02 \x01(\tR\x0bresumeToken\x12%\n\x0euploader_state\x18\x03 \x01(\x0cR\ruploaderState:W\xea\x41T\n)resultstore.googleapis.com/UploadMetadata\x12\'invocations/{invocation}/uploadMetadataB\x86\x01\n\"com.google.devtools.resultstore.v2B\x13UploadMetadataProtoP\x01ZIgoogle.golang.org/genproto/googleapis/devtools/resultstore/v2;resultstoreb\x06proto3')



_UPLOADMETADATA = DESCRIPTOR.message_types_by_name['UploadMetadata']
UploadMetadata = _reflection.GeneratedProtocolMessageType('UploadMetadata', (_message.Message,), {
  'DESCRIPTOR' : _UPLOADMETADATA,
  '__module__' : 'google.devtools.resultstore.v2.upload_metadata_pb2'
  # @@protoc_insertion_point(class_scope:google.devtools.resultstore.v2.UploadMetadata)
  })
_sym_db.RegisterMessage(UploadMetadata)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\"com.google.devtools.resultstore.v2B\023UploadMetadataProtoP\001ZIgoogle.golang.org/genproto/googleapis/devtools/resultstore/v2;resultstore'
  _UPLOADMETADATA._options = None
  _UPLOADMETADATA._serialized_options = b'\352AT\n)resultstore.googleapis.com/UploadMetadata\022\'invocations/{invocation}/uploadMetadata'
  _UPLOADMETADATA._serialized_start=116
  _UPLOADMETADATA._serialized_end=315
# @@protoc_insertion_point(module_scope)
