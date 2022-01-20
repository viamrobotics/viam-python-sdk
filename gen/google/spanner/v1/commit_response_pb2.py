# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/spanner/v1/commit_response.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'google/spanner/v1/commit_response.proto\x12\x11google.spanner.v1\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1cgoogle/api/annotations.proto\"\xdf\x01\n\x0e\x43ommitResponse\x12\x45\n\x10\x63ommit_timestamp\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x0f\x63ommitTimestamp\x12P\n\x0c\x63ommit_stats\x18\x02 \x01(\x0b\x32-.google.spanner.v1.CommitResponse.CommitStatsR\x0b\x63ommitStats\x1a\x34\n\x0b\x43ommitStats\x12%\n\x0emutation_count\x18\x01 \x01(\x03R\rmutationCountB\xb9\x01\n\x15\x63om.google.spanner.v1B\x13\x43ommitResponseProtoP\x01Z8google.golang.org/genproto/googleapis/spanner/v1;spanner\xaa\x02\x17Google.Cloud.Spanner.V1\xca\x02\x17Google\\Cloud\\Spanner\\V1\xea\x02\x1aGoogle::Cloud::Spanner::V1b\x06proto3')



_COMMITRESPONSE = DESCRIPTOR.message_types_by_name['CommitResponse']
_COMMITRESPONSE_COMMITSTATS = _COMMITRESPONSE.nested_types_by_name['CommitStats']
CommitResponse = _reflection.GeneratedProtocolMessageType('CommitResponse', (_message.Message,), {

  'CommitStats' : _reflection.GeneratedProtocolMessageType('CommitStats', (_message.Message,), {
    'DESCRIPTOR' : _COMMITRESPONSE_COMMITSTATS,
    '__module__' : 'google.spanner.v1.commit_response_pb2'
    # @@protoc_insertion_point(class_scope:google.spanner.v1.CommitResponse.CommitStats)
    })
  ,
  'DESCRIPTOR' : _COMMITRESPONSE,
  '__module__' : 'google.spanner.v1.commit_response_pb2'
  # @@protoc_insertion_point(class_scope:google.spanner.v1.CommitResponse)
  })
_sym_db.RegisterMessage(CommitResponse)
_sym_db.RegisterMessage(CommitResponse.CommitStats)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\025com.google.spanner.v1B\023CommitResponseProtoP\001Z8google.golang.org/genproto/googleapis/spanner/v1;spanner\252\002\027Google.Cloud.Spanner.V1\312\002\027Google\\Cloud\\Spanner\\V1\352\002\032Google::Cloud::Spanner::V1'
  _COMMITRESPONSE._serialized_start=158
  _COMMITRESPONSE._serialized_end=381
  _COMMITRESPONSE_COMMITSTATS._serialized_start=329
  _COMMITRESPONSE_COMMITSTATS._serialized_end=381
# @@protoc_insertion_point(module_scope)
