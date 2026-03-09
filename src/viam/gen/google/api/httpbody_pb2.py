"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 7, 34, 0, '', 'google/api/httpbody.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19google/api/httpbody.proto\x12\ngoogle.api\x1a\x19google/protobuf/any.proto"w\n\x08HttpBody\x12!\n\x0ccontent_type\x18\x01 \x01(\tR\x0bcontentType\x12\x12\n\x04data\x18\x02 \x01(\x0cR\x04data\x124\n\nextensions\x18\x03 \x03(\x0b2\x14.google.protobuf.AnyR\nextensionsBe\n\x0ecom.google.apiB\rHttpBodyProtoP\x01Z;google.golang.org/genproto/googleapis/api/httpbody;httpbody\xa2\x02\x04GAPIb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.api.httpbody_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x0ecom.google.apiB\rHttpBodyProtoP\x01Z;google.golang.org/genproto/googleapis/api/httpbody;httpbody\xa2\x02\x04GAPI'
    _globals['_HTTPBODY']._serialized_start = 68
    _globals['_HTTPBODY']._serialized_end = 187