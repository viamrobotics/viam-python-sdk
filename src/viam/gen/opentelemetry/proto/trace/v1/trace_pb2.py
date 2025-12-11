"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 2, '', 'opentelemetry/proto/trace/v1/trace.proto')
_sym_db = _symbol_database.Default()
from .....opentelemetry.proto.common.v1 import common_pb2 as opentelemetry_dot_proto_dot_common_dot_v1_dot_common__pb2
from .....opentelemetry.proto.resource.v1 import resource_pb2 as opentelemetry_dot_proto_dot_resource_dot_v1_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(opentelemetry/proto/trace/v1/trace.proto\x12\x1copentelemetry.proto.trace.v1\x1a*opentelemetry/proto/common/v1/common.proto\x1a.opentelemetry/proto/resource/v1/resource.proto"`\n\nTracesData\x12R\n\x0eresource_spans\x18\x01 \x03(\x0b2+.opentelemetry.proto.trace.v1.ResourceSpansR\rresourceSpans"\xc8\x01\n\rResourceSpans\x12E\n\x08resource\x18\x01 \x01(\x0b2).opentelemetry.proto.resource.v1.ResourceR\x08resource\x12I\n\x0bscope_spans\x18\x02 \x03(\x0b2(.opentelemetry.proto.trace.v1.ScopeSpansR\nscopeSpans\x12\x1d\n\nschema_url\x18\x03 \x01(\tR\tschemaUrlJ\x06\x08\xe8\x07\x10\xe9\x07"\xb0\x01\n\nScopeSpans\x12I\n\x05scope\x18\x01 \x01(\x0b23.opentelemetry.proto.common.v1.InstrumentationScopeR\x05scope\x128\n\x05spans\x18\x02 \x03(\x0b2".opentelemetry.proto.trace.v1.SpanR\x05spans\x12\x1d\n\nschema_url\x18\x03 \x01(\tR\tschemaUrl"\xc8\n\n\x04Span\x12\x19\n\x08trace_id\x18\x01 \x01(\x0cR\x07traceId\x12\x17\n\x07span_id\x18\x02 \x01(\x0cR\x06spanId\x12\x1f\n\x0btrace_state\x18\x03 \x01(\tR\ntraceState\x12$\n\x0eparent_span_id\x18\x04 \x01(\x0cR\x0cparentSpanId\x12\x14\n\x05flags\x18\x10 \x01(\x07R\x05flags\x12\x12\n\x04name\x18\x05 \x01(\tR\x04name\x12?\n\x04kind\x18\x06 \x01(\x0e2+.opentelemetry.proto.trace.v1.Span.SpanKindR\x04kind\x12/\n\x14start_time_unix_nano\x18\x07 \x01(\x06R\x11startTimeUnixNano\x12+\n\x12end_time_unix_nano\x18\x08 \x01(\x06R\x0fendTimeUnixNano\x12G\n\nattributes\x18\t \x03(\x0b2\'.opentelemetry.proto.common.v1.KeyValueR\nattributes\x128\n\x18dropped_attributes_count\x18\n \x01(\rR\x16droppedAttributesCount\x12@\n\x06events\x18\x0b \x03(\x0b2(.opentelemetry.proto.trace.v1.Span.EventR\x06events\x120\n\x14dropped_events_count\x18\x0c \x01(\rR\x12droppedEventsCount\x12=\n\x05links\x18\r \x03(\x0b2\'.opentelemetry.proto.trace.v1.Span.LinkR\x05links\x12.\n\x13dropped_links_count\x18\x0e \x01(\rR\x11droppedLinksCount\x12<\n\x06status\x18\x0f \x01(\x0b2$.opentelemetry.proto.trace.v1.StatusR\x06status\x1a\xc4\x01\n\x05Event\x12$\n\x0etime_unix_nano\x18\x01 \x01(\x06R\x0ctimeUnixNano\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12G\n\nattributes\x18\x03 \x03(\x0b2\'.opentelemetry.proto.common.v1.KeyValueR\nattributes\x128\n\x18dropped_attributes_count\x18\x04 \x01(\rR\x16droppedAttributesCount\x1a\xf4\x01\n\x04Link\x12\x19\n\x08trace_id\x18\x01 \x01(\x0cR\x07traceId\x12\x17\n\x07span_id\x18\x02 \x01(\x0cR\x06spanId\x12\x1f\n\x0btrace_state\x18\x03 \x01(\tR\ntraceState\x12G\n\nattributes\x18\x04 \x03(\x0b2\'.opentelemetry.proto.common.v1.KeyValueR\nattributes\x128\n\x18dropped_attributes_count\x18\x05 \x01(\rR\x16droppedAttributesCount\x12\x14\n\x05flags\x18\x06 \x01(\x07R\x05flags"\x99\x01\n\x08SpanKind\x12\x19\n\x15SPAN_KIND_UNSPECIFIED\x10\x00\x12\x16\n\x12SPAN_KIND_INTERNAL\x10\x01\x12\x14\n\x10SPAN_KIND_SERVER\x10\x02\x12\x14\n\x10SPAN_KIND_CLIENT\x10\x03\x12\x16\n\x12SPAN_KIND_PRODUCER\x10\x04\x12\x16\n\x12SPAN_KIND_CONSUMER\x10\x05"\xbd\x01\n\x06Status\x12\x18\n\x07message\x18\x02 \x01(\tR\x07message\x12C\n\x04code\x18\x03 \x01(\x0e2/.opentelemetry.proto.trace.v1.Status.StatusCodeR\x04code"N\n\nStatusCode\x12\x15\n\x11STATUS_CODE_UNSET\x10\x00\x12\x12\n\x0eSTATUS_CODE_OK\x10\x01\x12\x15\n\x11STATUS_CODE_ERROR\x10\x02J\x04\x08\x01\x10\x02*\x9c\x01\n\tSpanFlags\x12\x19\n\x15SPAN_FLAGS_DO_NOT_USE\x10\x00\x12 \n\x1bSPAN_FLAGS_TRACE_FLAGS_MASK\x10\xff\x01\x12*\n%SPAN_FLAGS_CONTEXT_HAS_IS_REMOTE_MASK\x10\x80\x02\x12&\n!SPAN_FLAGS_CONTEXT_IS_REMOTE_MASK\x10\x80\x04Bw\n\x1fio.opentelemetry.proto.trace.v1B\nTraceProtoP\x01Z\'go.opentelemetry.io/proto/otlp/trace/v1\xaa\x02\x1cOpenTelemetry.Proto.Trace.V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'opentelemetry.proto.trace.v1.trace_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b"\n\x1fio.opentelemetry.proto.trace.v1B\nTraceProtoP\x01Z'go.opentelemetry.io/proto/otlp/trace/v1\xaa\x02\x1cOpenTelemetry.Proto.Trace.V1"
    _globals['_SPANFLAGS']._serialized_start = 2194
    _globals['_SPANFLAGS']._serialized_end = 2350
    _globals['_TRACESDATA']._serialized_start = 166
    _globals['_TRACESDATA']._serialized_end = 262
    _globals['_RESOURCESPANS']._serialized_start = 265
    _globals['_RESOURCESPANS']._serialized_end = 465
    _globals['_SCOPESPANS']._serialized_start = 468
    _globals['_SCOPESPANS']._serialized_end = 644
    _globals['_SPAN']._serialized_start = 647
    _globals['_SPAN']._serialized_end = 1999
    _globals['_SPAN_EVENT']._serialized_start = 1400
    _globals['_SPAN_EVENT']._serialized_end = 1596
    _globals['_SPAN_LINK']._serialized_start = 1599
    _globals['_SPAN_LINK']._serialized_end = 1843
    _globals['_SPAN_SPANKIND']._serialized_start = 1846
    _globals['_SPAN_SPANKIND']._serialized_end = 1999
    _globals['_STATUS']._serialized_start = 2002
    _globals['_STATUS']._serialized_end = 2191
    _globals['_STATUS_STATUSCODE']._serialized_start = 2107
    _globals['_STATUS_STATUSCODE']._serialized_end = 2185