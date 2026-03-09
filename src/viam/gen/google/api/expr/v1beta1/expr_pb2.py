"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 7, 34, 0, '', 'google/api/expr/v1beta1/expr.proto')
_sym_db = _symbol_database.Default()
from .....google.api.expr.v1beta1 import source_pb2 as google_dot_api_dot_expr_dot_v1beta1_dot_source__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n"google/api/expr/v1beta1/expr.proto\x12\x17google.api.expr.v1beta1\x1a$google/api/expr/v1beta1/source.proto\x1a\x1cgoogle/protobuf/struct.proto"\xac\x01\n\nParsedExpr\x121\n\x04expr\x18\x02 \x01(\x0b2\x1d.google.api.expr.v1beta1.ExprR\x04expr\x12D\n\x0bsource_info\x18\x03 \x01(\x0b2#.google.api.expr.v1beta1.SourceInfoR\nsourceInfo\x12%\n\x0esyntax_version\x18\x04 \x01(\tR\rsyntaxVersion"\xbd\x0c\n\x04Expr\x12\x0e\n\x02id\x18\x02 \x01(\x05R\x02id\x12E\n\x0cliteral_expr\x18\x03 \x01(\x0b2 .google.api.expr.v1beta1.LiteralH\x00R\x0bliteralExpr\x12D\n\nident_expr\x18\x04 \x01(\x0b2#.google.api.expr.v1beta1.Expr.IdentH\x00R\tidentExpr\x12G\n\x0bselect_expr\x18\x05 \x01(\x0b2$.google.api.expr.v1beta1.Expr.SelectH\x00R\nselectExpr\x12A\n\tcall_expr\x18\x06 \x01(\x0b2".google.api.expr.v1beta1.Expr.CallH\x00R\x08callExpr\x12G\n\tlist_expr\x18\x07 \x01(\x0b2(.google.api.expr.v1beta1.Expr.CreateListH\x00R\x08listExpr\x12M\n\x0bstruct_expr\x18\x08 \x01(\x0b2*.google.api.expr.v1beta1.Expr.CreateStructH\x00R\nstructExpr\x12\\\n\x12comprehension_expr\x18\t \x01(\x0b2+.google.api.expr.v1beta1.Expr.ComprehensionH\x00R\x11comprehensionExpr\x1a\x1b\n\x05Ident\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x1at\n\x06Select\x127\n\x07operand\x18\x01 \x01(\x0b2\x1d.google.api.expr.v1beta1.ExprR\x07operand\x12\x14\n\x05field\x18\x02 \x01(\tR\x05field\x12\x1b\n\ttest_only\x18\x03 \x01(\x08R\x08testOnly\x1a\x8c\x01\n\x04Call\x125\n\x06target\x18\x01 \x01(\x0b2\x1d.google.api.expr.v1beta1.ExprR\x06target\x12\x1a\n\x08function\x18\x02 \x01(\tR\x08function\x121\n\x04args\x18\x03 \x03(\x0b2\x1d.google.api.expr.v1beta1.ExprR\x04args\x1aG\n\nCreateList\x129\n\x08elements\x18\x01 \x03(\x0b2\x1d.google.api.expr.v1beta1.ExprR\x08elements\x1a\xa2\x02\n\x0cCreateStruct\x12\x12\n\x04type\x18\x01 \x01(\tR\x04type\x12J\n\x07entries\x18\x02 \x03(\x0b20.google.api.expr.v1beta1.Expr.CreateStruct.EntryR\x07entries\x1a\xb1\x01\n\x05Entry\x12\x0e\n\x02id\x18\x01 \x01(\x05R\x02id\x12\x1d\n\tfield_key\x18\x02 \x01(\tH\x00R\x08fieldKey\x128\n\x07map_key\x18\x03 \x01(\x0b2\x1d.google.api.expr.v1beta1.ExprH\x00R\x06mapKey\x123\n\x05value\x18\x04 \x01(\x0b2\x1d.google.api.expr.v1beta1.ExprR\x05valueB\n\n\x08key_kind\x1a\xf8\x02\n\rComprehension\x12\x19\n\x08iter_var\x18\x01 \x01(\tR\x07iterVar\x12<\n\niter_range\x18\x02 \x01(\x0b2\x1d.google.api.expr.v1beta1.ExprR\titerRange\x12\x19\n\x08accu_var\x18\x03 \x01(\tR\x07accuVar\x12:\n\taccu_init\x18\x04 \x01(\x0b2\x1d.google.api.expr.v1beta1.ExprR\x08accuInit\x12D\n\x0eloop_condition\x18\x05 \x01(\x0b2\x1d.google.api.expr.v1beta1.ExprR\rloopCondition\x12:\n\tloop_step\x18\x06 \x01(\x0b2\x1d.google.api.expr.v1beta1.ExprR\x08loopStep\x125\n\x06result\x18\x07 \x01(\x0b2\x1d.google.api.expr.v1beta1.ExprR\x06resultB\x0b\n\texpr_kind"\xad\x02\n\x07Literal\x12;\n\nnull_value\x18\x01 \x01(\x0e2\x1a.google.protobuf.NullValueH\x00R\tnullValue\x12\x1f\n\nbool_value\x18\x02 \x01(\x08H\x00R\tboolValue\x12!\n\x0bint64_value\x18\x03 \x01(\x03H\x00R\nint64Value\x12#\n\x0cuint64_value\x18\x04 \x01(\x04H\x00R\x0buint64Value\x12#\n\x0cdouble_value\x18\x05 \x01(\x01H\x00R\x0bdoubleValue\x12#\n\x0cstring_value\x18\x06 \x01(\tH\x00R\x0bstringValue\x12!\n\x0bbytes_value\x18\x07 \x01(\x0cH\x00R\nbytesValueB\x0f\n\rconstant_kindBj\n\x1bcom.google.api.expr.v1beta1B\tExprProtoP\x01Z;google.golang.org/genproto/googleapis/api/expr/v1beta1;expr\xf8\x01\x01b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.api.expr.v1beta1.expr_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1bcom.google.api.expr.v1beta1B\tExprProtoP\x01Z;google.golang.org/genproto/googleapis/api/expr/v1beta1;expr\xf8\x01\x01'
    _globals['_PARSEDEXPR']._serialized_start = 132
    _globals['_PARSEDEXPR']._serialized_end = 304
    _globals['_EXPR']._serialized_start = 307
    _globals['_EXPR']._serialized_end = 1904
    _globals['_EXPR_IDENT']._serialized_start = 858
    _globals['_EXPR_IDENT']._serialized_end = 885
    _globals['_EXPR_SELECT']._serialized_start = 887
    _globals['_EXPR_SELECT']._serialized_end = 1003
    _globals['_EXPR_CALL']._serialized_start = 1006
    _globals['_EXPR_CALL']._serialized_end = 1146
    _globals['_EXPR_CREATELIST']._serialized_start = 1148
    _globals['_EXPR_CREATELIST']._serialized_end = 1219
    _globals['_EXPR_CREATESTRUCT']._serialized_start = 1222
    _globals['_EXPR_CREATESTRUCT']._serialized_end = 1512
    _globals['_EXPR_CREATESTRUCT_ENTRY']._serialized_start = 1335
    _globals['_EXPR_CREATESTRUCT_ENTRY']._serialized_end = 1512
    _globals['_EXPR_COMPREHENSION']._serialized_start = 1515
    _globals['_EXPR_COMPREHENSION']._serialized_end = 1891
    _globals['_LITERAL']._serialized_start = 1907
    _globals['_LITERAL']._serialized_end = 2208