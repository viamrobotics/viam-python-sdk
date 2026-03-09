"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 7, 34, 0, '', 'google/api/expr/v1alpha1/value.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$google/api/expr/v1alpha1/value.proto\x12\x18google.api.expr.v1alpha1\x1a\x19google/protobuf/any.proto\x1a\x1cgoogle/protobuf/struct.proto"\xcd\x04\n\x05Value\x12;\n\nnull_value\x18\x01 \x01(\x0e2\x1a.google.protobuf.NullValueH\x00R\tnullValue\x12\x1f\n\nbool_value\x18\x02 \x01(\x08H\x00R\tboolValue\x12!\n\x0bint64_value\x18\x03 \x01(\x03H\x00R\nint64Value\x12#\n\x0cuint64_value\x18\x04 \x01(\x04H\x00R\x0buint64Value\x12#\n\x0cdouble_value\x18\x05 \x01(\x01H\x00R\x0bdoubleValue\x12#\n\x0cstring_value\x18\x06 \x01(\tH\x00R\x0bstringValue\x12!\n\x0bbytes_value\x18\x07 \x01(\x0cH\x00R\nbytesValue\x12D\n\nenum_value\x18\t \x01(\x0b2#.google.api.expr.v1alpha1.EnumValueH\x00R\tenumValue\x129\n\x0cobject_value\x18\n \x01(\x0b2\x14.google.protobuf.AnyH\x00R\x0bobjectValue\x12A\n\tmap_value\x18\x0b \x01(\x0b2".google.api.expr.v1alpha1.MapValueH\x00R\x08mapValue\x12D\n\nlist_value\x18\x0c \x01(\x0b2#.google.api.expr.v1alpha1.ListValueH\x00R\tlistValue\x12\x1f\n\ntype_value\x18\x0f \x01(\tH\x00R\ttypeValueB\x06\n\x04kind"5\n\tEnumValue\x12\x12\n\x04type\x18\x01 \x01(\tR\x04type\x12\x14\n\x05value\x18\x02 \x01(\x05R\x05value"D\n\tListValue\x127\n\x06values\x18\x01 \x03(\x0b2\x1f.google.api.expr.v1alpha1.ValueR\x06values"\xc1\x01\n\x08MapValue\x12B\n\x07entries\x18\x01 \x03(\x0b2(.google.api.expr.v1alpha1.MapValue.EntryR\x07entries\x1aq\n\x05Entry\x121\n\x03key\x18\x01 \x01(\x0b2\x1f.google.api.expr.v1alpha1.ValueR\x03key\x125\n\x05value\x18\x02 \x01(\x0b2\x1f.google.api.expr.v1alpha1.ValueR\x05valueBm\n\x1ccom.google.api.expr.v1alpha1B\nValueProtoP\x01Z<google.golang.org/genproto/googleapis/api/expr/v1alpha1;expr\xf8\x01\x01b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.api.expr.v1alpha1.value_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ccom.google.api.expr.v1alpha1B\nValueProtoP\x01Z<google.golang.org/genproto/googleapis/api/expr/v1alpha1;expr\xf8\x01\x01'
    _globals['_VALUE']._serialized_start = 124
    _globals['_VALUE']._serialized_end = 713
    _globals['_ENUMVALUE']._serialized_start = 715
    _globals['_ENUMVALUE']._serialized_end = 768
    _globals['_LISTVALUE']._serialized_start = 770
    _globals['_LISTVALUE']._serialized_end = 838
    _globals['_MAPVALUE']._serialized_start = 841
    _globals['_MAPVALUE']._serialized_end = 1034
    _globals['_MAPVALUE_ENTRY']._serialized_start = 921
    _globals['_MAPVALUE_ENTRY']._serialized_end = 1034