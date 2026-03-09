"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 7, 34, 0, '', 'google/api/expr/v1alpha1/eval.proto')
_sym_db = _symbol_database.Default()
from .....google.api.expr.v1alpha1 import value_pb2 as google_dot_api_dot_expr_dot_v1alpha1_dot_value__pb2
from .....google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#google/api/expr/v1alpha1/eval.proto\x12\x18google.api.expr.v1alpha1\x1a$google/api/expr/v1alpha1/value.proto\x1a\x17google/rpc/status.proto"\xc2\x01\n\tEvalState\x12;\n\x06values\x18\x01 \x03(\x0b2#.google.api.expr.v1alpha1.ExprValueR\x06values\x12D\n\x07results\x18\x03 \x03(\x0b2*.google.api.expr.v1alpha1.EvalState.ResultR\x07results\x1a2\n\x06Result\x12\x12\n\x04expr\x18\x01 \x01(\x03R\x04expr\x12\x14\n\x05value\x18\x02 \x01(\x03R\x05value"\xca\x01\n\tExprValue\x127\n\x05value\x18\x01 \x01(\x0b2\x1f.google.api.expr.v1alpha1.ValueH\x00R\x05value\x12:\n\x05error\x18\x02 \x01(\x0b2".google.api.expr.v1alpha1.ErrorSetH\x00R\x05error\x12@\n\x07unknown\x18\x03 \x01(\x0b2$.google.api.expr.v1alpha1.UnknownSetH\x00R\x07unknownB\x06\n\x04kind"6\n\x08ErrorSet\x12*\n\x06errors\x18\x01 \x03(\x0b2\x12.google.rpc.StatusR\x06errors""\n\nUnknownSet\x12\x14\n\x05exprs\x18\x01 \x03(\x03R\x05exprsBl\n\x1ccom.google.api.expr.v1alpha1B\tEvalProtoP\x01Z<google.golang.org/genproto/googleapis/api/expr/v1alpha1;expr\xf8\x01\x01b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.api.expr.v1alpha1.eval_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ccom.google.api.expr.v1alpha1B\tEvalProtoP\x01Z<google.golang.org/genproto/googleapis/api/expr/v1alpha1;expr\xf8\x01\x01'
    _globals['_EVALSTATE']._serialized_start = 129
    _globals['_EVALSTATE']._serialized_end = 323
    _globals['_EVALSTATE_RESULT']._serialized_start = 273
    _globals['_EVALSTATE_RESULT']._serialized_end = 323
    _globals['_EXPRVALUE']._serialized_start = 326
    _globals['_EXPRVALUE']._serialized_end = 528
    _globals['_ERRORSET']._serialized_start = 530
    _globals['_ERRORSET']._serialized_end = 584
    _globals['_UNKNOWNSET']._serialized_start = 586
    _globals['_UNKNOWNSET']._serialized_end = 620