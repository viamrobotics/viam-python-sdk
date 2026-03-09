"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 7, 34, 0, '', 'google/api/field_behavior.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1fgoogle/api/field_behavior.proto\x12\ngoogle.api\x1a google/protobuf/descriptor.proto*\xb6\x01\n\rFieldBehavior\x12\x1e\n\x1aFIELD_BEHAVIOR_UNSPECIFIED\x10\x00\x12\x0c\n\x08OPTIONAL\x10\x01\x12\x0c\n\x08REQUIRED\x10\x02\x12\x0f\n\x0bOUTPUT_ONLY\x10\x03\x12\x0e\n\nINPUT_ONLY\x10\x04\x12\r\n\tIMMUTABLE\x10\x05\x12\x12\n\x0eUNORDERED_LIST\x10\x06\x12\x15\n\x11NON_EMPTY_DEFAULT\x10\x07\x12\x0e\n\nIDENTIFIER\x10\x08:d\n\x0efield_behavior\x12\x1d.google.protobuf.FieldOptions\x18\x9c\x08 \x03(\x0e2\x19.google.api.FieldBehaviorB\x02\x10\x00R\rfieldBehaviorBp\n\x0ecom.google.apiB\x12FieldBehaviorProtoP\x01ZAgoogle.golang.org/genproto/googleapis/api/annotations;annotations\xa2\x02\x04GAPIb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.api.field_behavior_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x0ecom.google.apiB\x12FieldBehaviorProtoP\x01ZAgoogle.golang.org/genproto/googleapis/api/annotations;annotations\xa2\x02\x04GAPI'
    _globals['field_behavior']._loaded_options = None
    _globals['field_behavior']._serialized_options = b'\x10\x00'
    _globals['_FIELDBEHAVIOR']._serialized_start = 82
    _globals['_FIELDBEHAVIOR']._serialized_end = 264