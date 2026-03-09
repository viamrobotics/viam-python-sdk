"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 7, 34, 0, '', 'google/api/field_info.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1bgoogle/api/field_info.proto\x12\ngoogle.api\x1a google/protobuf/descriptor.proto"\xda\x01\n\tFieldInfo\x124\n\x06format\x18\x01 \x01(\x0e2\x1c.google.api.FieldInfo.FormatR\x06format\x12D\n\x10referenced_types\x18\x02 \x03(\x0b2\x19.google.api.TypeReferenceR\x0freferencedTypes"Q\n\x06Format\x12\x16\n\x12FORMAT_UNSPECIFIED\x10\x00\x12\t\n\x05UUID4\x10\x01\x12\x08\n\x04IPV4\x10\x02\x12\x08\n\x04IPV6\x10\x03\x12\x10\n\x0cIPV4_OR_IPV6\x10\x04",\n\rTypeReference\x12\x1b\n\ttype_name\x18\x01 \x01(\tR\x08typeName:W\n\nfield_info\x12\x1d.google.protobuf.FieldOptions\x18\xcc\xf1\xf9\x8a\x01 \x01(\x0b2\x15.google.api.FieldInfoR\tfieldInfoBl\n\x0ecom.google.apiB\x0eFieldInfoProtoP\x01ZAgoogle.golang.org/genproto/googleapis/api/annotations;annotations\xa2\x02\x04GAPIb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.api.field_info_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x0ecom.google.apiB\x0eFieldInfoProtoP\x01ZAgoogle.golang.org/genproto/googleapis/api/annotations;annotations\xa2\x02\x04GAPI'
    _globals['_FIELDINFO']._serialized_start = 78
    _globals['_FIELDINFO']._serialized_end = 296
    _globals['_FIELDINFO_FORMAT']._serialized_start = 215
    _globals['_FIELDINFO_FORMAT']._serialized_end = 296
    _globals['_TYPEREFERENCE']._serialized_start = 298
    _globals['_TYPEREFERENCE']._serialized_end = 342