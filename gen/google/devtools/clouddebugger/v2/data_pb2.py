# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/devtools/clouddebugger/v2/data.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.devtools.source.v1 import source_context_pb2 as google_dot_devtools_dot_source_dot_v1_dot_source__context__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+google/devtools/clouddebugger/v2/data.proto\x12 google.devtools.clouddebugger.v2\x1a.google/devtools/source/v1/source_context.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1cgoogle/api/annotations.proto\"G\n\rFormatMessage\x12\x16\n\x06\x66ormat\x18\x01 \x01(\tR\x06\x66ormat\x12\x1e\n\nparameters\x18\x02 \x03(\tR\nparameters\"\x84\x03\n\rStatusMessage\x12\x19\n\x08is_error\x18\x01 \x01(\x08R\x07isError\x12V\n\trefers_to\x18\x02 \x01(\x0e\x32\x39.google.devtools.clouddebugger.v2.StatusMessage.ReferenceR\x08refersTo\x12Q\n\x0b\x64\x65scription\x18\x03 \x01(\x0b\x32/.google.devtools.clouddebugger.v2.FormatMessageR\x0b\x64\x65scription\"\xac\x01\n\tReference\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x1e\n\x1a\x42REAKPOINT_SOURCE_LOCATION\x10\x03\x12\x18\n\x14\x42REAKPOINT_CONDITION\x10\x04\x12\x19\n\x15\x42REAKPOINT_EXPRESSION\x10\x07\x12\x12\n\x0e\x42REAKPOINT_AGE\x10\x08\x12\x11\n\rVARIABLE_NAME\x10\x05\x12\x12\n\x0eVARIABLE_VALUE\x10\x06\"P\n\x0eSourceLocation\x12\x12\n\x04path\x18\x01 \x01(\tR\x04path\x12\x12\n\x04line\x18\x02 \x01(\x05R\x04line\x12\x16\n\x06\x63olumn\x18\x03 \x01(\x05R\x06\x63olumn\"\x9c\x02\n\x08Variable\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value\x12\x12\n\x04type\x18\x06 \x01(\tR\x04type\x12\x44\n\x07members\x18\x03 \x03(\x0b\x32*.google.devtools.clouddebugger.v2.VariableR\x07members\x12\x43\n\x0fvar_table_index\x18\x04 \x01(\x0b\x32\x1b.google.protobuf.Int32ValueR\rvarTableIndex\x12G\n\x06status\x18\x05 \x01(\x0b\x32/.google.devtools.clouddebugger.v2.StatusMessageR\x06status\"\x84\x02\n\nStackFrame\x12\x1a\n\x08\x66unction\x18\x01 \x01(\tR\x08\x66unction\x12L\n\x08location\x18\x02 \x01(\x0b\x32\x30.google.devtools.clouddebugger.v2.SourceLocationR\x08location\x12H\n\targuments\x18\x03 \x03(\x0b\x32*.google.devtools.clouddebugger.v2.VariableR\targuments\x12\x42\n\x06locals\x18\x04 \x03(\x0b\x32*.google.devtools.clouddebugger.v2.VariableR\x06locals\"\xdf\x08\n\nBreakpoint\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12K\n\x06\x61\x63tion\x18\r \x01(\x0e\x32\x33.google.devtools.clouddebugger.v2.Breakpoint.ActionR\x06\x61\x63tion\x12L\n\x08location\x18\x02 \x01(\x0b\x32\x30.google.devtools.clouddebugger.v2.SourceLocationR\x08location\x12\x1c\n\tcondition\x18\x03 \x01(\tR\tcondition\x12 \n\x0b\x65xpressions\x18\x04 \x03(\tR\x0b\x65xpressions\x12,\n\x12log_message_format\x18\x0e \x01(\tR\x10logMessageFormat\x12R\n\tlog_level\x18\x0f \x01(\x0e\x32\x35.google.devtools.clouddebugger.v2.Breakpoint.LogLevelR\x08logLevel\x12$\n\x0eis_final_state\x18\x05 \x01(\x08R\x0cisFinalState\x12;\n\x0b\x63reate_time\x18\x0b \x01(\x0b\x32\x1a.google.protobuf.TimestampR\ncreateTime\x12\x39\n\nfinal_time\x18\x0c \x01(\x0b\x32\x1a.google.protobuf.TimestampR\tfinalTime\x12\x1d\n\nuser_email\x18\x10 \x01(\tR\tuserEmail\x12G\n\x06status\x18\n \x01(\x0b\x32/.google.devtools.clouddebugger.v2.StatusMessageR\x06status\x12O\n\x0cstack_frames\x18\x07 \x03(\x0b\x32,.google.devtools.clouddebugger.v2.StackFrameR\x0bstackFrames\x12_\n\x15\x65valuated_expressions\x18\x08 \x03(\x0b\x32*.google.devtools.clouddebugger.v2.VariableR\x14\x65valuatedExpressions\x12Q\n\x0evariable_table\x18\t \x03(\x0b\x32*.google.devtools.clouddebugger.v2.VariableR\rvariableTable\x12P\n\x06labels\x18\x11 \x03(\x0b\x32\x38.google.devtools.clouddebugger.v2.Breakpoint.LabelsEntryR\x06labels\x1a\x39\n\x0bLabelsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01\"\x1e\n\x06\x41\x63tion\x12\x0b\n\x07\x43\x41PTURE\x10\x00\x12\x07\n\x03LOG\x10\x01\",\n\x08LogLevel\x12\x08\n\x04INFO\x10\x00\x12\x0b\n\x07WARNING\x10\x01\x12\t\n\x05\x45RROR\x10\x02\"\xea\x04\n\x08\x44\x65\x62uggee\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x18\n\x07project\x18\x02 \x01(\tR\x07project\x12\x1e\n\nuniquifier\x18\x03 \x01(\tR\nuniquifier\x12 \n\x0b\x64\x65scription\x18\x04 \x01(\tR\x0b\x64\x65scription\x12\x1f\n\x0bis_inactive\x18\x05 \x01(\x08R\nisInactive\x12#\n\ragent_version\x18\x06 \x01(\tR\x0c\x61gentVersion\x12\x1f\n\x0bis_disabled\x18\x07 \x01(\x08R\nisDisabled\x12G\n\x06status\x18\x08 \x01(\x0b\x32/.google.devtools.clouddebugger.v2.StatusMessageR\x06status\x12Q\n\x0fsource_contexts\x18\t \x03(\x0b\x32(.google.devtools.source.v1.SourceContextR\x0esourceContexts\x12\x64\n\x13\x65xt_source_contexts\x18\r \x03(\x0b\x32\x30.google.devtools.source.v1.ExtendedSourceContextB\x02\x18\x01R\x11\x65xtSourceContexts\x12N\n\x06labels\x18\x0b \x03(\x0b\x32\x36.google.devtools.clouddebugger.v2.Debuggee.LabelsEntryR\x06labels\x1a\x39\n\x0bLabelsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01\x42\xd9\x01\n$com.google.devtools.clouddebugger.v2B\tDataProtoP\x01ZMgoogle.golang.org/genproto/googleapis/devtools/clouddebugger/v2;clouddebugger\xf8\x01\x01\xaa\x02\x18Google.Cloud.Debugger.V2\xca\x02\x18Google\\Cloud\\Debugger\\V2\xea\x02\x1bGoogle::Cloud::Debugger::V2b\x06proto3')



_FORMATMESSAGE = DESCRIPTOR.message_types_by_name['FormatMessage']
_STATUSMESSAGE = DESCRIPTOR.message_types_by_name['StatusMessage']
_SOURCELOCATION = DESCRIPTOR.message_types_by_name['SourceLocation']
_VARIABLE = DESCRIPTOR.message_types_by_name['Variable']
_STACKFRAME = DESCRIPTOR.message_types_by_name['StackFrame']
_BREAKPOINT = DESCRIPTOR.message_types_by_name['Breakpoint']
_BREAKPOINT_LABELSENTRY = _BREAKPOINT.nested_types_by_name['LabelsEntry']
_DEBUGGEE = DESCRIPTOR.message_types_by_name['Debuggee']
_DEBUGGEE_LABELSENTRY = _DEBUGGEE.nested_types_by_name['LabelsEntry']
_STATUSMESSAGE_REFERENCE = _STATUSMESSAGE.enum_types_by_name['Reference']
_BREAKPOINT_ACTION = _BREAKPOINT.enum_types_by_name['Action']
_BREAKPOINT_LOGLEVEL = _BREAKPOINT.enum_types_by_name['LogLevel']
FormatMessage = _reflection.GeneratedProtocolMessageType('FormatMessage', (_message.Message,), {
  'DESCRIPTOR' : _FORMATMESSAGE,
  '__module__' : 'google.devtools.clouddebugger.v2.data_pb2'
  # @@protoc_insertion_point(class_scope:google.devtools.clouddebugger.v2.FormatMessage)
  })
_sym_db.RegisterMessage(FormatMessage)

StatusMessage = _reflection.GeneratedProtocolMessageType('StatusMessage', (_message.Message,), {
  'DESCRIPTOR' : _STATUSMESSAGE,
  '__module__' : 'google.devtools.clouddebugger.v2.data_pb2'
  # @@protoc_insertion_point(class_scope:google.devtools.clouddebugger.v2.StatusMessage)
  })
_sym_db.RegisterMessage(StatusMessage)

SourceLocation = _reflection.GeneratedProtocolMessageType('SourceLocation', (_message.Message,), {
  'DESCRIPTOR' : _SOURCELOCATION,
  '__module__' : 'google.devtools.clouddebugger.v2.data_pb2'
  # @@protoc_insertion_point(class_scope:google.devtools.clouddebugger.v2.SourceLocation)
  })
_sym_db.RegisterMessage(SourceLocation)

Variable = _reflection.GeneratedProtocolMessageType('Variable', (_message.Message,), {
  'DESCRIPTOR' : _VARIABLE,
  '__module__' : 'google.devtools.clouddebugger.v2.data_pb2'
  # @@protoc_insertion_point(class_scope:google.devtools.clouddebugger.v2.Variable)
  })
_sym_db.RegisterMessage(Variable)

StackFrame = _reflection.GeneratedProtocolMessageType('StackFrame', (_message.Message,), {
  'DESCRIPTOR' : _STACKFRAME,
  '__module__' : 'google.devtools.clouddebugger.v2.data_pb2'
  # @@protoc_insertion_point(class_scope:google.devtools.clouddebugger.v2.StackFrame)
  })
_sym_db.RegisterMessage(StackFrame)

Breakpoint = _reflection.GeneratedProtocolMessageType('Breakpoint', (_message.Message,), {

  'LabelsEntry' : _reflection.GeneratedProtocolMessageType('LabelsEntry', (_message.Message,), {
    'DESCRIPTOR' : _BREAKPOINT_LABELSENTRY,
    '__module__' : 'google.devtools.clouddebugger.v2.data_pb2'
    # @@protoc_insertion_point(class_scope:google.devtools.clouddebugger.v2.Breakpoint.LabelsEntry)
    })
  ,
  'DESCRIPTOR' : _BREAKPOINT,
  '__module__' : 'google.devtools.clouddebugger.v2.data_pb2'
  # @@protoc_insertion_point(class_scope:google.devtools.clouddebugger.v2.Breakpoint)
  })
_sym_db.RegisterMessage(Breakpoint)
_sym_db.RegisterMessage(Breakpoint.LabelsEntry)

Debuggee = _reflection.GeneratedProtocolMessageType('Debuggee', (_message.Message,), {

  'LabelsEntry' : _reflection.GeneratedProtocolMessageType('LabelsEntry', (_message.Message,), {
    'DESCRIPTOR' : _DEBUGGEE_LABELSENTRY,
    '__module__' : 'google.devtools.clouddebugger.v2.data_pb2'
    # @@protoc_insertion_point(class_scope:google.devtools.clouddebugger.v2.Debuggee.LabelsEntry)
    })
  ,
  'DESCRIPTOR' : _DEBUGGEE,
  '__module__' : 'google.devtools.clouddebugger.v2.data_pb2'
  # @@protoc_insertion_point(class_scope:google.devtools.clouddebugger.v2.Debuggee)
  })
_sym_db.RegisterMessage(Debuggee)
_sym_db.RegisterMessage(Debuggee.LabelsEntry)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n$com.google.devtools.clouddebugger.v2B\tDataProtoP\001ZMgoogle.golang.org/genproto/googleapis/devtools/clouddebugger/v2;clouddebugger\370\001\001\252\002\030Google.Cloud.Debugger.V2\312\002\030Google\\Cloud\\Debugger\\V2\352\002\033Google::Cloud::Debugger::V2'
  _BREAKPOINT_LABELSENTRY._options = None
  _BREAKPOINT_LABELSENTRY._serialized_options = b'8\001'
  _DEBUGGEE_LABELSENTRY._options = None
  _DEBUGGEE_LABELSENTRY._serialized_options = b'8\001'
  _DEBUGGEE.fields_by_name['ext_source_contexts']._options = None
  _DEBUGGEE.fields_by_name['ext_source_contexts']._serialized_options = b'\030\001'
  _FORMATMESSAGE._serialized_start=224
  _FORMATMESSAGE._serialized_end=295
  _STATUSMESSAGE._serialized_start=298
  _STATUSMESSAGE._serialized_end=686
  _STATUSMESSAGE_REFERENCE._serialized_start=514
  _STATUSMESSAGE_REFERENCE._serialized_end=686
  _SOURCELOCATION._serialized_start=688
  _SOURCELOCATION._serialized_end=768
  _VARIABLE._serialized_start=771
  _VARIABLE._serialized_end=1055
  _STACKFRAME._serialized_start=1058
  _STACKFRAME._serialized_end=1318
  _BREAKPOINT._serialized_start=1321
  _BREAKPOINT._serialized_end=2440
  _BREAKPOINT_LABELSENTRY._serialized_start=2305
  _BREAKPOINT_LABELSENTRY._serialized_end=2362
  _BREAKPOINT_ACTION._serialized_start=2364
  _BREAKPOINT_ACTION._serialized_end=2394
  _BREAKPOINT_LOGLEVEL._serialized_start=2396
  _BREAKPOINT_LOGLEVEL._serialized_end=2440
  _DEBUGGEE._serialized_start=2443
  _DEBUGGEE._serialized_end=3061
  _DEBUGGEE_LABELSENTRY._serialized_start=2305
  _DEBUGGEE_LABELSENTRY._serialized_end=2362
# @@protoc_insertion_point(module_scope)
