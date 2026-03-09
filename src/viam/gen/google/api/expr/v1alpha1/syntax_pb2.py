"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 7, 34, 0, '', 'google/api/expr/v1alpha1/syntax.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%google/api/expr/v1alpha1/syntax.proto\x12\x18google.api.expr.v1alpha1\x1a\x1egoogle/protobuf/duration.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\x87\x01\n\nParsedExpr\x122\n\x04expr\x18\x02 \x01(\x0b2\x1e.google.api.expr.v1alpha1.ExprR\x04expr\x12E\n\x0bsource_info\x18\x03 \x01(\x0b2$.google.api.expr.v1alpha1.SourceInfoR\nsourceInfo"\xcb\r\n\x04Expr\x12\x0e\n\x02id\x18\x02 \x01(\x03R\x02id\x12C\n\nconst_expr\x18\x03 \x01(\x0b2".google.api.expr.v1alpha1.ConstantH\x00R\tconstExpr\x12E\n\nident_expr\x18\x04 \x01(\x0b2$.google.api.expr.v1alpha1.Expr.IdentH\x00R\tidentExpr\x12H\n\x0bselect_expr\x18\x05 \x01(\x0b2%.google.api.expr.v1alpha1.Expr.SelectH\x00R\nselectExpr\x12B\n\tcall_expr\x18\x06 \x01(\x0b2#.google.api.expr.v1alpha1.Expr.CallH\x00R\x08callExpr\x12H\n\tlist_expr\x18\x07 \x01(\x0b2).google.api.expr.v1alpha1.Expr.CreateListH\x00R\x08listExpr\x12N\n\x0bstruct_expr\x18\x08 \x01(\x0b2+.google.api.expr.v1alpha1.Expr.CreateStructH\x00R\nstructExpr\x12]\n\x12comprehension_expr\x18\t \x01(\x0b2,.google.api.expr.v1alpha1.Expr.ComprehensionH\x00R\x11comprehensionExpr\x1a\x1b\n\x05Ident\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x1au\n\x06Select\x128\n\x07operand\x18\x01 \x01(\x0b2\x1e.google.api.expr.v1alpha1.ExprR\x07operand\x12\x14\n\x05field\x18\x02 \x01(\tR\x05field\x12\x1b\n\ttest_only\x18\x03 \x01(\x08R\x08testOnly\x1a\x8e\x01\n\x04Call\x126\n\x06target\x18\x01 \x01(\x0b2\x1e.google.api.expr.v1alpha1.ExprR\x06target\x12\x1a\n\x08function\x18\x02 \x01(\tR\x08function\x122\n\x04args\x18\x03 \x03(\x0b2\x1e.google.api.expr.v1alpha1.ExprR\x04args\x1as\n\nCreateList\x12:\n\x08elements\x18\x01 \x03(\x0b2\x1e.google.api.expr.v1alpha1.ExprR\x08elements\x12)\n\x10optional_indices\x18\x02 \x03(\x05R\x0foptionalIndices\x1a\xdb\x02\n\x0cCreateStruct\x12!\n\x0cmessage_name\x18\x01 \x01(\tR\x0bmessageName\x12K\n\x07entries\x18\x02 \x03(\x0b21.google.api.expr.v1alpha1.Expr.CreateStruct.EntryR\x07entries\x1a\xda\x01\n\x05Entry\x12\x0e\n\x02id\x18\x01 \x01(\x03R\x02id\x12\x1d\n\tfield_key\x18\x02 \x01(\tH\x00R\x08fieldKey\x129\n\x07map_key\x18\x03 \x01(\x0b2\x1e.google.api.expr.v1alpha1.ExprH\x00R\x06mapKey\x124\n\x05value\x18\x04 \x01(\x0b2\x1e.google.api.expr.v1alpha1.ExprR\x05value\x12%\n\x0eoptional_entry\x18\x05 \x01(\x08R\roptionalEntryB\n\n\x08key_kind\x1a\x9a\x03\n\rComprehension\x12\x19\n\x08iter_var\x18\x01 \x01(\tR\x07iterVar\x12\x1b\n\titer_var2\x18\x08 \x01(\tR\x08iterVar2\x12=\n\niter_range\x18\x02 \x01(\x0b2\x1e.google.api.expr.v1alpha1.ExprR\titerRange\x12\x19\n\x08accu_var\x18\x03 \x01(\tR\x07accuVar\x12;\n\taccu_init\x18\x04 \x01(\x0b2\x1e.google.api.expr.v1alpha1.ExprR\x08accuInit\x12E\n\x0eloop_condition\x18\x05 \x01(\x0b2\x1e.google.api.expr.v1alpha1.ExprR\rloopCondition\x12;\n\tloop_step\x18\x06 \x01(\x0b2\x1e.google.api.expr.v1alpha1.ExprR\x08loopStep\x126\n\x06result\x18\x07 \x01(\x0b2\x1e.google.api.expr.v1alpha1.ExprR\x06resultB\x0b\n\texpr_kind"\xc1\x03\n\x08Constant\x12;\n\nnull_value\x18\x01 \x01(\x0e2\x1a.google.protobuf.NullValueH\x00R\tnullValue\x12\x1f\n\nbool_value\x18\x02 \x01(\x08H\x00R\tboolValue\x12!\n\x0bint64_value\x18\x03 \x01(\x03H\x00R\nint64Value\x12#\n\x0cuint64_value\x18\x04 \x01(\x04H\x00R\x0buint64Value\x12#\n\x0cdouble_value\x18\x05 \x01(\x01H\x00R\x0bdoubleValue\x12#\n\x0cstring_value\x18\x06 \x01(\tH\x00R\x0bstringValue\x12!\n\x0bbytes_value\x18\x07 \x01(\x0cH\x00R\nbytesValue\x12F\n\x0eduration_value\x18\x08 \x01(\x0b2\x19.google.protobuf.DurationB\x02\x18\x01H\x00R\rdurationValue\x12I\n\x0ftimestamp_value\x18\t \x01(\x0b2\x1a.google.protobuf.TimestampB\x02\x18\x01H\x00R\x0etimestampValueB\x0f\n\rconstant_kind"\x8c\x07\n\nSourceInfo\x12%\n\x0esyntax_version\x18\x01 \x01(\tR\rsyntaxVersion\x12\x1a\n\x08location\x18\x02 \x01(\tR\x08location\x12!\n\x0cline_offsets\x18\x03 \x03(\x05R\x0blineOffsets\x12Q\n\tpositions\x18\x04 \x03(\x0b23.google.api.expr.v1alpha1.SourceInfo.PositionsEntryR\tpositions\x12U\n\x0bmacro_calls\x18\x05 \x03(\x0b24.google.api.expr.v1alpha1.SourceInfo.MacroCallsEntryR\nmacroCalls\x12N\n\nextensions\x18\x06 \x03(\x0b2..google.api.expr.v1alpha1.SourceInfo.ExtensionR\nextensions\x1a\x80\x03\n\tExtension\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12i\n\x13affected_components\x18\x02 \x03(\x0e28.google.api.expr.v1alpha1.SourceInfo.Extension.ComponentR\x12affectedComponents\x12P\n\x07version\x18\x03 \x01(\x0b26.google.api.expr.v1alpha1.SourceInfo.Extension.VersionR\x07version\x1a5\n\x07Version\x12\x14\n\x05major\x18\x01 \x01(\x03R\x05major\x12\x14\n\x05minor\x18\x02 \x01(\x03R\x05minor"o\n\tComponent\x12\x19\n\x15COMPONENT_UNSPECIFIED\x10\x00\x12\x14\n\x10COMPONENT_PARSER\x10\x01\x12\x1a\n\x16COMPONENT_TYPE_CHECKER\x10\x02\x12\x15\n\x11COMPONENT_RUNTIME\x10\x03\x1a<\n\x0ePositionsEntry\x12\x10\n\x03key\x18\x01 \x01(\x03R\x03key\x12\x14\n\x05value\x18\x02 \x01(\x05R\x05value:\x028\x01\x1a]\n\x0fMacroCallsEntry\x12\x10\n\x03key\x18\x01 \x01(\x03R\x03key\x124\n\x05value\x18\x02 \x01(\x0b2\x1e.google.api.expr.v1alpha1.ExprR\x05value:\x028\x01"p\n\x0eSourcePosition\x12\x1a\n\x08location\x18\x01 \x01(\tR\x08location\x12\x16\n\x06offset\x18\x02 \x01(\x05R\x06offset\x12\x12\n\x04line\x18\x03 \x01(\x05R\x04line\x12\x16\n\x06column\x18\x04 \x01(\x05R\x06columnBn\n\x1ccom.google.api.expr.v1alpha1B\x0bSyntaxProtoP\x01Z<google.golang.org/genproto/googleapis/api/expr/v1alpha1;expr\xf8\x01\x01b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.api.expr.v1alpha1.syntax_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ccom.google.api.expr.v1alpha1B\x0bSyntaxProtoP\x01Z<google.golang.org/genproto/googleapis/api/expr/v1alpha1;expr\xf8\x01\x01'
    _globals['_CONSTANT'].fields_by_name['duration_value']._loaded_options = None
    _globals['_CONSTANT'].fields_by_name['duration_value']._serialized_options = b'\x18\x01'
    _globals['_CONSTANT'].fields_by_name['timestamp_value']._loaded_options = None
    _globals['_CONSTANT'].fields_by_name['timestamp_value']._serialized_options = b'\x18\x01'
    _globals['_SOURCEINFO_POSITIONSENTRY']._loaded_options = None
    _globals['_SOURCEINFO_POSITIONSENTRY']._serialized_options = b'8\x01'
    _globals['_SOURCEINFO_MACROCALLSENTRY']._loaded_options = None
    _globals['_SOURCEINFO_MACROCALLSENTRY']._serialized_options = b'8\x01'
    _globals['_PARSEDEXPR']._serialized_start = 163
    _globals['_PARSEDEXPR']._serialized_end = 298
    _globals['_EXPR']._serialized_start = 301
    _globals['_EXPR']._serialized_end = 2040
    _globals['_EXPR_IDENT']._serialized_start = 856
    _globals['_EXPR_IDENT']._serialized_end = 883
    _globals['_EXPR_SELECT']._serialized_start = 885
    _globals['_EXPR_SELECT']._serialized_end = 1002
    _globals['_EXPR_CALL']._serialized_start = 1005
    _globals['_EXPR_CALL']._serialized_end = 1147
    _globals['_EXPR_CREATELIST']._serialized_start = 1149
    _globals['_EXPR_CREATELIST']._serialized_end = 1264
    _globals['_EXPR_CREATESTRUCT']._serialized_start = 1267
    _globals['_EXPR_CREATESTRUCT']._serialized_end = 1614
    _globals['_EXPR_CREATESTRUCT_ENTRY']._serialized_start = 1396
    _globals['_EXPR_CREATESTRUCT_ENTRY']._serialized_end = 1614
    _globals['_EXPR_COMPREHENSION']._serialized_start = 1617
    _globals['_EXPR_COMPREHENSION']._serialized_end = 2027
    _globals['_CONSTANT']._serialized_start = 2043
    _globals['_CONSTANT']._serialized_end = 2492
    _globals['_SOURCEINFO']._serialized_start = 2495
    _globals['_SOURCEINFO']._serialized_end = 3403
    _globals['_SOURCEINFO_EXTENSION']._serialized_start = 2862
    _globals['_SOURCEINFO_EXTENSION']._serialized_end = 3246
    _globals['_SOURCEINFO_EXTENSION_VERSION']._serialized_start = 3080
    _globals['_SOURCEINFO_EXTENSION_VERSION']._serialized_end = 3133
    _globals['_SOURCEINFO_EXTENSION_COMPONENT']._serialized_start = 3135
    _globals['_SOURCEINFO_EXTENSION_COMPONENT']._serialized_end = 3246
    _globals['_SOURCEINFO_POSITIONSENTRY']._serialized_start = 3248
    _globals['_SOURCEINFO_POSITIONSENTRY']._serialized_end = 3308
    _globals['_SOURCEINFO_MACROCALLSENTRY']._serialized_start = 3310
    _globals['_SOURCEINFO_MACROCALLSENTRY']._serialized_end = 3403
    _globals['_SOURCEPOSITION']._serialized_start = 3405
    _globals['_SOURCEPOSITION']._serialized_end = 3517