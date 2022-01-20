# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/devtools/cloudtrace/v1/trace.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import client_pb2 as google_dot_api_dot_client__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)google/devtools/cloudtrace/v1/trace.proto\x12\x1dgoogle.devtools.cloudtrace.v1\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1cgoogle/api/annotations.proto\"\x81\x01\n\x05Trace\x12\x1d\n\nproject_id\x18\x01 \x01(\tR\tprojectId\x12\x19\n\x08trace_id\x18\x02 \x01(\tR\x07traceId\x12>\n\x05spans\x18\x03 \x03(\x0b\x32(.google.devtools.cloudtrace.v1.TraceSpanR\x05spans\"F\n\x06Traces\x12<\n\x06traces\x18\x01 \x03(\x0b\x32$.google.devtools.cloudtrace.v1.TraceR\x06traces\"\xed\x03\n\tTraceSpan\x12\x17\n\x07span_id\x18\x01 \x01(\x06R\x06spanId\x12\x45\n\x04kind\x18\x02 \x01(\x0e\x32\x31.google.devtools.cloudtrace.v1.TraceSpan.SpanKindR\x04kind\x12\x12\n\x04name\x18\x03 \x01(\tR\x04name\x12\x39\n\nstart_time\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\tstartTime\x12\x35\n\x08\x65nd_time\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x07\x65ndTime\x12*\n\x0eparent_span_id\x18\x06 \x01(\x06\x42\x04\xe2\x41\x01\x01R\x0cparentSpanId\x12L\n\x06labels\x18\x07 \x03(\x0b\x32\x34.google.devtools.cloudtrace.v1.TraceSpan.LabelsEntryR\x06labels\x1a\x39\n\x0bLabelsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01\"E\n\x08SpanKind\x12\x19\n\x15SPAN_KIND_UNSPECIFIED\x10\x00\x12\x0e\n\nRPC_SERVER\x10\x01\x12\x0e\n\nRPC_CLIENT\x10\x02\"\xd0\x03\n\x11ListTracesRequest\x12#\n\nproject_id\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02R\tprojectId\x12S\n\x04view\x18\x02 \x01(\x0e\x32\x39.google.devtools.cloudtrace.v1.ListTracesRequest.ViewTypeB\x04\xe2\x41\x01\x01R\x04view\x12!\n\tpage_size\x18\x03 \x01(\x05\x42\x04\xe2\x41\x01\x01R\x08pageSize\x12\x1d\n\npage_token\x18\x04 \x01(\tR\tpageToken\x12\x39\n\nstart_time\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\tstartTime\x12\x35\n\x08\x65nd_time\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x07\x65ndTime\x12\x1c\n\x06\x66ilter\x18\x07 \x01(\tB\x04\xe2\x41\x01\x01R\x06\x66ilter\x12\x1f\n\x08order_by\x18\x08 \x01(\tB\x04\xe2\x41\x01\x01R\x07orderBy\"N\n\x08ViewType\x12\x19\n\x15VIEW_TYPE_UNSPECIFIED\x10\x00\x12\x0b\n\x07MINIMAL\x10\x01\x12\x0c\n\x08ROOTSPAN\x10\x02\x12\x0c\n\x08\x43OMPLETE\x10\x03\"z\n\x12ListTracesResponse\x12<\n\x06traces\x18\x01 \x03(\x0b\x32$.google.devtools.cloudtrace.v1.TraceR\x06traces\x12&\n\x0fnext_page_token\x18\x02 \x01(\tR\rnextPageToken\"W\n\x0fGetTraceRequest\x12#\n\nproject_id\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02R\tprojectId\x12\x1f\n\x08trace_id\x18\x02 \x01(\tB\x04\xe2\x41\x01\x02R\x07traceId\"~\n\x12PatchTracesRequest\x12#\n\nproject_id\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02R\tprojectId\x12\x43\n\x06traces\x18\x02 \x01(\x0b\x32%.google.devtools.cloudtrace.v1.TracesB\x04\xe2\x41\x01\x02R\x06traces2\xb5\x05\n\x0cTraceService\x12\xa8\x01\n\nListTraces\x12\x30.google.devtools.cloudtrace.v1.ListTracesRequest\x1a\x31.google.devtools.cloudtrace.v1.ListTracesResponse\"5\xda\x41\nproject_id\x82\xd3\xe4\x93\x02\"\x12 /v1/projects/{project_id}/traces\x12\xab\x01\n\x08GetTrace\x12..google.devtools.cloudtrace.v1.GetTraceRequest\x1a$.google.devtools.cloudtrace.v1.Trace\"I\xda\x41\x13project_id,trace_id\x82\xd3\xe4\x93\x02-\x12+/v1/projects/{project_id}/traces/{trace_id}\x12\x9e\x01\n\x0bPatchTraces\x12\x31.google.devtools.cloudtrace.v1.PatchTracesRequest\x1a\x16.google.protobuf.Empty\"D\xda\x41\x11project_id,traces\x82\xd3\xe4\x93\x02*2 /v1/projects/{project_id}/traces:\x06traces\x1a\xaa\x01\xca\x41\x19\x63loudtrace.googleapis.com\xd2\x41\x8a\x01https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/trace.append,https://www.googleapis.com/auth/trace.readonlyB\xc5\x01\n!com.google.devtools.cloudtrace.v1B\nTraceProtoP\x01ZGgoogle.golang.org/genproto/googleapis/devtools/cloudtrace/v1;cloudtrace\xaa\x02\x15Google.Cloud.Trace.V1\xca\x02\x15Google\\Cloud\\Trace\\V1\xea\x02\x18Google::Cloud::Trace::V1b\x06proto3')



_TRACE = DESCRIPTOR.message_types_by_name['Trace']
_TRACES = DESCRIPTOR.message_types_by_name['Traces']
_TRACESPAN = DESCRIPTOR.message_types_by_name['TraceSpan']
_TRACESPAN_LABELSENTRY = _TRACESPAN.nested_types_by_name['LabelsEntry']
_LISTTRACESREQUEST = DESCRIPTOR.message_types_by_name['ListTracesRequest']
_LISTTRACESRESPONSE = DESCRIPTOR.message_types_by_name['ListTracesResponse']
_GETTRACEREQUEST = DESCRIPTOR.message_types_by_name['GetTraceRequest']
_PATCHTRACESREQUEST = DESCRIPTOR.message_types_by_name['PatchTracesRequest']
_TRACESPAN_SPANKIND = _TRACESPAN.enum_types_by_name['SpanKind']
_LISTTRACESREQUEST_VIEWTYPE = _LISTTRACESREQUEST.enum_types_by_name['ViewType']
Trace = _reflection.GeneratedProtocolMessageType('Trace', (_message.Message,), {
  'DESCRIPTOR' : _TRACE,
  '__module__' : 'google.devtools.cloudtrace.v1.trace_pb2'
  # @@protoc_insertion_point(class_scope:google.devtools.cloudtrace.v1.Trace)
  })
_sym_db.RegisterMessage(Trace)

Traces = _reflection.GeneratedProtocolMessageType('Traces', (_message.Message,), {
  'DESCRIPTOR' : _TRACES,
  '__module__' : 'google.devtools.cloudtrace.v1.trace_pb2'
  # @@protoc_insertion_point(class_scope:google.devtools.cloudtrace.v1.Traces)
  })
_sym_db.RegisterMessage(Traces)

TraceSpan = _reflection.GeneratedProtocolMessageType('TraceSpan', (_message.Message,), {

  'LabelsEntry' : _reflection.GeneratedProtocolMessageType('LabelsEntry', (_message.Message,), {
    'DESCRIPTOR' : _TRACESPAN_LABELSENTRY,
    '__module__' : 'google.devtools.cloudtrace.v1.trace_pb2'
    # @@protoc_insertion_point(class_scope:google.devtools.cloudtrace.v1.TraceSpan.LabelsEntry)
    })
  ,
  'DESCRIPTOR' : _TRACESPAN,
  '__module__' : 'google.devtools.cloudtrace.v1.trace_pb2'
  # @@protoc_insertion_point(class_scope:google.devtools.cloudtrace.v1.TraceSpan)
  })
_sym_db.RegisterMessage(TraceSpan)
_sym_db.RegisterMessage(TraceSpan.LabelsEntry)

ListTracesRequest = _reflection.GeneratedProtocolMessageType('ListTracesRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTTRACESREQUEST,
  '__module__' : 'google.devtools.cloudtrace.v1.trace_pb2'
  # @@protoc_insertion_point(class_scope:google.devtools.cloudtrace.v1.ListTracesRequest)
  })
_sym_db.RegisterMessage(ListTracesRequest)

ListTracesResponse = _reflection.GeneratedProtocolMessageType('ListTracesResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTTRACESRESPONSE,
  '__module__' : 'google.devtools.cloudtrace.v1.trace_pb2'
  # @@protoc_insertion_point(class_scope:google.devtools.cloudtrace.v1.ListTracesResponse)
  })
_sym_db.RegisterMessage(ListTracesResponse)

GetTraceRequest = _reflection.GeneratedProtocolMessageType('GetTraceRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETTRACEREQUEST,
  '__module__' : 'google.devtools.cloudtrace.v1.trace_pb2'
  # @@protoc_insertion_point(class_scope:google.devtools.cloudtrace.v1.GetTraceRequest)
  })
_sym_db.RegisterMessage(GetTraceRequest)

PatchTracesRequest = _reflection.GeneratedProtocolMessageType('PatchTracesRequest', (_message.Message,), {
  'DESCRIPTOR' : _PATCHTRACESREQUEST,
  '__module__' : 'google.devtools.cloudtrace.v1.trace_pb2'
  # @@protoc_insertion_point(class_scope:google.devtools.cloudtrace.v1.PatchTracesRequest)
  })
_sym_db.RegisterMessage(PatchTracesRequest)

_TRACESERVICE = DESCRIPTOR.services_by_name['TraceService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n!com.google.devtools.cloudtrace.v1B\nTraceProtoP\001ZGgoogle.golang.org/genproto/googleapis/devtools/cloudtrace/v1;cloudtrace\252\002\025Google.Cloud.Trace.V1\312\002\025Google\\Cloud\\Trace\\V1\352\002\030Google::Cloud::Trace::V1'
  _TRACESPAN_LABELSENTRY._options = None
  _TRACESPAN_LABELSENTRY._serialized_options = b'8\001'
  _TRACESPAN.fields_by_name['parent_span_id']._options = None
  _TRACESPAN.fields_by_name['parent_span_id']._serialized_options = b'\342A\001\001'
  _LISTTRACESREQUEST.fields_by_name['project_id']._options = None
  _LISTTRACESREQUEST.fields_by_name['project_id']._serialized_options = b'\342A\001\002'
  _LISTTRACESREQUEST.fields_by_name['view']._options = None
  _LISTTRACESREQUEST.fields_by_name['view']._serialized_options = b'\342A\001\001'
  _LISTTRACESREQUEST.fields_by_name['page_size']._options = None
  _LISTTRACESREQUEST.fields_by_name['page_size']._serialized_options = b'\342A\001\001'
  _LISTTRACESREQUEST.fields_by_name['filter']._options = None
  _LISTTRACESREQUEST.fields_by_name['filter']._serialized_options = b'\342A\001\001'
  _LISTTRACESREQUEST.fields_by_name['order_by']._options = None
  _LISTTRACESREQUEST.fields_by_name['order_by']._serialized_options = b'\342A\001\001'
  _GETTRACEREQUEST.fields_by_name['project_id']._options = None
  _GETTRACEREQUEST.fields_by_name['project_id']._serialized_options = b'\342A\001\002'
  _GETTRACEREQUEST.fields_by_name['trace_id']._options = None
  _GETTRACEREQUEST.fields_by_name['trace_id']._serialized_options = b'\342A\001\002'
  _PATCHTRACESREQUEST.fields_by_name['project_id']._options = None
  _PATCHTRACESREQUEST.fields_by_name['project_id']._serialized_options = b'\342A\001\002'
  _PATCHTRACESREQUEST.fields_by_name['traces']._options = None
  _PATCHTRACESREQUEST.fields_by_name['traces']._serialized_options = b'\342A\001\002'
  _TRACESERVICE._options = None
  _TRACESERVICE._serialized_options = b'\312A\031cloudtrace.googleapis.com\322A\212\001https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/trace.append,https://www.googleapis.com/auth/trace.readonly'
  _TRACESERVICE.methods_by_name['ListTraces']._options = None
  _TRACESERVICE.methods_by_name['ListTraces']._serialized_options = b'\332A\nproject_id\202\323\344\223\002\"\022 /v1/projects/{project_id}/traces'
  _TRACESERVICE.methods_by_name['GetTrace']._options = None
  _TRACESERVICE.methods_by_name['GetTrace']._serialized_options = b'\332A\023project_id,trace_id\202\323\344\223\002-\022+/v1/projects/{project_id}/traces/{trace_id}'
  _TRACESERVICE.methods_by_name['PatchTraces']._options = None
  _TRACESERVICE.methods_by_name['PatchTraces']._serialized_options = b'\332A\021project_id,traces\202\323\344\223\002*2 /v1/projects/{project_id}/traces:\006traces'
  _TRACE._serialized_start=254
  _TRACE._serialized_end=383
  _TRACES._serialized_start=385
  _TRACES._serialized_end=455
  _TRACESPAN._serialized_start=458
  _TRACESPAN._serialized_end=951
  _TRACESPAN_LABELSENTRY._serialized_start=823
  _TRACESPAN_LABELSENTRY._serialized_end=880
  _TRACESPAN_SPANKIND._serialized_start=882
  _TRACESPAN_SPANKIND._serialized_end=951
  _LISTTRACESREQUEST._serialized_start=954
  _LISTTRACESREQUEST._serialized_end=1418
  _LISTTRACESREQUEST_VIEWTYPE._serialized_start=1340
  _LISTTRACESREQUEST_VIEWTYPE._serialized_end=1418
  _LISTTRACESRESPONSE._serialized_start=1420
  _LISTTRACESRESPONSE._serialized_end=1542
  _GETTRACEREQUEST._serialized_start=1544
  _GETTRACEREQUEST._serialized_end=1631
  _PATCHTRACESREQUEST._serialized_start=1633
  _PATCHTRACESREQUEST._serialized_end=1759
  _TRACESERVICE._serialized_start=1762
  _TRACESERVICE._serialized_end=2455
# @@protoc_insertion_point(module_scope)
