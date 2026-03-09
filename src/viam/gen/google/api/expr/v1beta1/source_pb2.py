"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 7, 34, 0, '', 'google/api/expr/v1beta1/source.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$google/api/expr/v1beta1/source.proto\x12\x17google.api.expr.v1beta1"\xdb\x01\n\nSourceInfo\x12\x1a\n\x08location\x18\x02 \x01(\tR\x08location\x12!\n\x0cline_offsets\x18\x03 \x03(\x05R\x0blineOffsets\x12P\n\tpositions\x18\x04 \x03(\x0b22.google.api.expr.v1beta1.SourceInfo.PositionsEntryR\tpositions\x1a<\n\x0ePositionsEntry\x12\x10\n\x03key\x18\x01 \x01(\x05R\x03key\x12\x14\n\x05value\x18\x02 \x01(\x05R\x05value:\x028\x01"p\n\x0eSourcePosition\x12\x1a\n\x08location\x18\x01 \x01(\tR\x08location\x12\x16\n\x06offset\x18\x02 \x01(\x05R\x06offset\x12\x12\n\x04line\x18\x03 \x01(\x05R\x04line\x12\x16\n\x06column\x18\x04 \x01(\x05R\x06columnBl\n\x1bcom.google.api.expr.v1beta1B\x0bSourceProtoP\x01Z;google.golang.org/genproto/googleapis/api/expr/v1beta1;expr\xf8\x01\x01b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.api.expr.v1beta1.source_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1bcom.google.api.expr.v1beta1B\x0bSourceProtoP\x01Z;google.golang.org/genproto/googleapis/api/expr/v1beta1;expr\xf8\x01\x01'
    _globals['_SOURCEINFO_POSITIONSENTRY']._loaded_options = None
    _globals['_SOURCEINFO_POSITIONSENTRY']._serialized_options = b'8\x01'
    _globals['_SOURCEINFO']._serialized_start = 66
    _globals['_SOURCEINFO']._serialized_end = 285
    _globals['_SOURCEINFO_POSITIONSENTRY']._serialized_start = 225
    _globals['_SOURCEINFO_POSITIONSENTRY']._serialized_end = 285
    _globals['_SOURCEPOSITION']._serialized_start = 287
    _globals['_SOURCEPOSITION']._serialized_end = 399