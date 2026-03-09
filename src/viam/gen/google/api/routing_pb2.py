"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 7, 34, 0, '', 'google/api/routing.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18google/api/routing.proto\x12\ngoogle.api\x1a google/protobuf/descriptor.proto"Z\n\x0bRoutingRule\x12K\n\x12routing_parameters\x18\x02 \x03(\x0b2\x1c.google.api.RoutingParameterR\x11routingParameters"M\n\x10RoutingParameter\x12\x14\n\x05field\x18\x01 \x01(\tR\x05field\x12#\n\rpath_template\x18\x02 \x01(\tR\x0cpathTemplate:T\n\x07routing\x12\x1e.google.protobuf.MethodOptions\x18\xb1\xca\xbc" \x01(\x0b2\x17.google.api.RoutingRuleR\x07routingBj\n\x0ecom.google.apiB\x0cRoutingProtoP\x01ZAgoogle.golang.org/genproto/googleapis/api/annotations;annotations\xa2\x02\x04GAPIb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.api.routing_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x0ecom.google.apiB\x0cRoutingProtoP\x01ZAgoogle.golang.org/genproto/googleapis/api/annotations;annotations\xa2\x02\x04GAPI'
    _globals['_ROUTINGRULE']._serialized_start = 74
    _globals['_ROUTINGRULE']._serialized_end = 164
    _globals['_ROUTINGPARAMETER']._serialized_start = 166
    _globals['_ROUTINGPARAMETER']._serialized_end = 243