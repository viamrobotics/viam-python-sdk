"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 7, 34, 0, '', 'google/api/visibility.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1bgoogle/api/visibility.proto\x12\ngoogle.api\x1a google/protobuf/descriptor.proto">\n\nVisibility\x120\n\x05rules\x18\x01 \x03(\x0b2\x1a.google.api.VisibilityRuleR\x05rules"N\n\x0eVisibilityRule\x12\x1a\n\x08selector\x18\x01 \x01(\tR\x08selector\x12 \n\x0brestriction\x18\x02 \x01(\tR\x0brestriction:d\n\x0fenum_visibility\x12\x1c.google.protobuf.EnumOptions\x18\xaf\xca\xbc" \x01(\x0b2\x1a.google.api.VisibilityRuleR\x0eenumVisibility:k\n\x10value_visibility\x12!.google.protobuf.EnumValueOptions\x18\xaf\xca\xbc" \x01(\x0b2\x1a.google.api.VisibilityRuleR\x0fvalueVisibility:g\n\x10field_visibility\x12\x1d.google.protobuf.FieldOptions\x18\xaf\xca\xbc" \x01(\x0b2\x1a.google.api.VisibilityRuleR\x0ffieldVisibility:m\n\x12message_visibility\x12\x1f.google.protobuf.MessageOptions\x18\xaf\xca\xbc" \x01(\x0b2\x1a.google.api.VisibilityRuleR\x11messageVisibility:j\n\x11method_visibility\x12\x1e.google.protobuf.MethodOptions\x18\xaf\xca\xbc" \x01(\x0b2\x1a.google.api.VisibilityRuleR\x10methodVisibility:e\n\x0eapi_visibility\x12\x1f.google.protobuf.ServiceOptions\x18\xaf\xca\xbc" \x01(\x0b2\x1a.google.api.VisibilityRuleR\rapiVisibilityBk\n\x0ecom.google.apiB\x0fVisibilityProtoP\x01Z?google.golang.org/genproto/googleapis/api/visibility;visibility\xa2\x02\x04GAPIb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.api.visibility_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x0ecom.google.apiB\x0fVisibilityProtoP\x01Z?google.golang.org/genproto/googleapis/api/visibility;visibility\xa2\x02\x04GAPI'
    _globals['_VISIBILITY']._serialized_start = 77
    _globals['_VISIBILITY']._serialized_end = 139
    _globals['_VISIBILITYRULE']._serialized_start = 141
    _globals['_VISIBILITYRULE']._serialized_end = 219