"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 2, '', 'opentelemetry/proto/resource/v1/resource.proto')
_sym_db = _symbol_database.Default()
from .....opentelemetry.proto.common.v1 import common_pb2 as opentelemetry_dot_proto_dot_common_dot_v1_dot_common__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.opentelemetry/proto/resource/v1/resource.proto\x12\x1fopentelemetry.proto.resource.v1\x1a*opentelemetry/proto/common/v1/common.proto"\xd8\x01\n\x08Resource\x12G\n\nattributes\x18\x01 \x03(\x0b2\'.opentelemetry.proto.common.v1.KeyValueR\nattributes\x128\n\x18dropped_attributes_count\x18\x02 \x01(\rR\x16droppedAttributesCount\x12I\n\x0bentity_refs\x18\x03 \x03(\x0b2(.opentelemetry.proto.common.v1.EntityRefR\nentityRefsB\x83\x01\n"io.opentelemetry.proto.resource.v1B\rResourceProtoP\x01Z*go.opentelemetry.io/proto/otlp/resource/v1\xaa\x02\x1fOpenTelemetry.Proto.Resource.V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'opentelemetry.proto.resource.v1.resource_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n"io.opentelemetry.proto.resource.v1B\rResourceProtoP\x01Z*go.opentelemetry.io/proto/otlp/resource/v1\xaa\x02\x1fOpenTelemetry.Proto.Resource.V1'
    _globals['_RESOURCE']._serialized_start = 128
    _globals['_RESOURCE']._serialized_end = 344