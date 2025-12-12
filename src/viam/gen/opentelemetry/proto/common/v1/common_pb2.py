"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 2, '', 'opentelemetry/proto/common/v1/common.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*opentelemetry/proto/common/v1/common.proto\x12\x1dopentelemetry.proto.common.v1"\xe0\x02\n\x08AnyValue\x12#\n\x0cstring_value\x18\x01 \x01(\tH\x00R\x0bstringValue\x12\x1f\n\nbool_value\x18\x02 \x01(\x08H\x00R\tboolValue\x12\x1d\n\tint_value\x18\x03 \x01(\x03H\x00R\x08intValue\x12#\n\x0cdouble_value\x18\x04 \x01(\x01H\x00R\x0bdoubleValue\x12L\n\x0barray_value\x18\x05 \x01(\x0b2).opentelemetry.proto.common.v1.ArrayValueH\x00R\narrayValue\x12P\n\x0ckvlist_value\x18\x06 \x01(\x0b2+.opentelemetry.proto.common.v1.KeyValueListH\x00R\x0bkvlistValue\x12!\n\x0bbytes_value\x18\x07 \x01(\x0cH\x00R\nbytesValueB\x07\n\x05value"M\n\nArrayValue\x12?\n\x06values\x18\x01 \x03(\x0b2\'.opentelemetry.proto.common.v1.AnyValueR\x06values"O\n\x0cKeyValueList\x12?\n\x06values\x18\x01 \x03(\x0b2\'.opentelemetry.proto.common.v1.KeyValueR\x06values"[\n\x08KeyValue\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12=\n\x05value\x18\x02 \x01(\x0b2\'.opentelemetry.proto.common.v1.AnyValueR\x05value"\xc7\x01\n\x14InstrumentationScope\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x18\n\x07version\x18\x02 \x01(\tR\x07version\x12G\n\nattributes\x18\x03 \x03(\x0b2\'.opentelemetry.proto.common.v1.KeyValueR\nattributes\x128\n\x18dropped_attributes_count\x18\x04 \x01(\rR\x16droppedAttributesCount"\x82\x01\n\tEntityRef\x12\x1d\n\nschema_url\x18\x01 \x01(\tR\tschemaUrl\x12\x12\n\x04type\x18\x02 \x01(\tR\x04type\x12\x17\n\x07id_keys\x18\x03 \x03(\tR\x06idKeys\x12)\n\x10description_keys\x18\x04 \x03(\tR\x0fdescriptionKeysB{\n io.opentelemetry.proto.common.v1B\x0bCommonProtoP\x01Z(go.opentelemetry.io/proto/otlp/common/v1\xaa\x02\x1dOpenTelemetry.Proto.Common.V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'opentelemetry.proto.common.v1.common_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n io.opentelemetry.proto.common.v1B\x0bCommonProtoP\x01Z(go.opentelemetry.io/proto/otlp/common/v1\xaa\x02\x1dOpenTelemetry.Proto.Common.V1'
    _globals['_ANYVALUE']._serialized_start = 78
    _globals['_ANYVALUE']._serialized_end = 430
    _globals['_ARRAYVALUE']._serialized_start = 432
    _globals['_ARRAYVALUE']._serialized_end = 509
    _globals['_KEYVALUELIST']._serialized_start = 511
    _globals['_KEYVALUELIST']._serialized_end = 590
    _globals['_KEYVALUE']._serialized_start = 592
    _globals['_KEYVALUE']._serialized_end = 683
    _globals['_INSTRUMENTATIONSCOPE']._serialized_start = 686
    _globals['_INSTRUMENTATIONSCOPE']._serialized_end = 885
    _globals['_ENTITYREF']._serialized_start = 888
    _globals['_ENTITYREF']._serialized_end = 1018