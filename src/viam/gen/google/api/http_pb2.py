"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 7, 34, 0, '', 'google/api/http.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15google/api/http.proto\x12\ngoogle.api"y\n\x04Http\x12*\n\x05rules\x18\x01 \x03(\x0b2\x14.google.api.HttpRuleR\x05rules\x12E\n\x1ffully_decode_reserved_expansion\x18\x02 \x01(\x08R\x1cfullyDecodeReservedExpansion"\xda\x02\n\x08HttpRule\x12\x1a\n\x08selector\x18\x01 \x01(\tR\x08selector\x12\x12\n\x03get\x18\x02 \x01(\tH\x00R\x03get\x12\x12\n\x03put\x18\x03 \x01(\tH\x00R\x03put\x12\x14\n\x04post\x18\x04 \x01(\tH\x00R\x04post\x12\x18\n\x06delete\x18\x05 \x01(\tH\x00R\x06delete\x12\x16\n\x05patch\x18\x06 \x01(\tH\x00R\x05patch\x127\n\x06custom\x18\x08 \x01(\x0b2\x1d.google.api.CustomHttpPatternH\x00R\x06custom\x12\x12\n\x04body\x18\x07 \x01(\tR\x04body\x12#\n\rresponse_body\x18\x0c \x01(\tR\x0cresponseBody\x12E\n\x13additional_bindings\x18\x0b \x03(\x0b2\x14.google.api.HttpRuleR\x12additionalBindingsB\t\n\x07pattern";\n\x11CustomHttpPattern\x12\x12\n\x04kind\x18\x01 \x01(\tR\x04kind\x12\x12\n\x04path\x18\x02 \x01(\tR\x04pathBg\n\x0ecom.google.apiB\tHttpProtoP\x01ZAgoogle.golang.org/genproto/googleapis/api/annotations;annotations\xa2\x02\x04GAPIb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.api.http_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x0ecom.google.apiB\tHttpProtoP\x01ZAgoogle.golang.org/genproto/googleapis/api/annotations;annotations\xa2\x02\x04GAPI'
    _globals['_HTTP']._serialized_start = 37
    _globals['_HTTP']._serialized_end = 158
    _globals['_HTTPRULE']._serialized_start = 161
    _globals['_HTTPRULE']._serialized_end = 507
    _globals['_CUSTOMHTTPPATTERN']._serialized_start = 509
    _globals['_CUSTOMHTTPPATTERN']._serialized_end = 568