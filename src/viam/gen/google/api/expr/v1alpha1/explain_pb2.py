"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 7, 34, 0, '', 'google/api/expr/v1alpha1/explain.proto')
_sym_db = _symbol_database.Default()
from .....google.api.expr.v1alpha1 import value_pb2 as google_dot_api_dot_expr_dot_v1alpha1_dot_value__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&google/api/expr/v1alpha1/explain.proto\x12\x18google.api.expr.v1alpha1\x1a$google/api/expr/v1alpha1/value.proto"\xce\x01\n\x07Explain\x127\n\x06values\x18\x01 \x03(\x0b2\x1f.google.api.expr.v1alpha1.ValueR\x06values\x12I\n\nexpr_steps\x18\x02 \x03(\x0b2*.google.api.expr.v1alpha1.Explain.ExprStepR\texprSteps\x1a;\n\x08ExprStep\x12\x0e\n\x02id\x18\x01 \x01(\x03R\x02id\x12\x1f\n\x0bvalue_index\x18\x02 \x01(\x05R\nvalueIndex:\x02\x18\x01Bo\n\x1ccom.google.api.expr.v1alpha1B\x0cExplainProtoP\x01Z<google.golang.org/genproto/googleapis/api/expr/v1alpha1;expr\xf8\x01\x01b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.api.expr.v1alpha1.explain_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ccom.google.api.expr.v1alpha1B\x0cExplainProtoP\x01Z<google.golang.org/genproto/googleapis/api/expr/v1alpha1;expr\xf8\x01\x01'
    _globals['_EXPLAIN']._loaded_options = None
    _globals['_EXPLAIN']._serialized_options = b'\x18\x01'
    _globals['_EXPLAIN']._serialized_start = 107
    _globals['_EXPLAIN']._serialized_end = 313
    _globals['_EXPLAIN_EXPRSTEP']._serialized_start = 250
    _globals['_EXPLAIN_EXPRSTEP']._serialized_end = 309