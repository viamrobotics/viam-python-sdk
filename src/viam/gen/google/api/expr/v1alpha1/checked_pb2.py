"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 7, 34, 0, '', 'google/api/expr/v1alpha1/checked.proto')
_sym_db = _symbol_database.Default()
from .....google.api.expr.v1alpha1 import syntax_pb2 as google_dot_api_dot_expr_dot_v1alpha1_dot_syntax__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&google/api/expr/v1alpha1/checked.proto\x12\x18google.api.expr.v1alpha1\x1a%google/api/expr/v1alpha1/syntax.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1cgoogle/protobuf/struct.proto"\x9a\x04\n\x0bCheckedExpr\x12\\\n\rreference_map\x18\x02 \x03(\x0b27.google.api.expr.v1alpha1.CheckedExpr.ReferenceMapEntryR\x0creferenceMap\x12M\n\x08type_map\x18\x03 \x03(\x0b22.google.api.expr.v1alpha1.CheckedExpr.TypeMapEntryR\x07typeMap\x12E\n\x0bsource_info\x18\x05 \x01(\x0b2$.google.api.expr.v1alpha1.SourceInfoR\nsourceInfo\x12!\n\x0cexpr_version\x18\x06 \x01(\tR\x0bexprVersion\x122\n\x04expr\x18\x04 \x01(\x0b2\x1e.google.api.expr.v1alpha1.ExprR\x04expr\x1ad\n\x11ReferenceMapEntry\x12\x10\n\x03key\x18\x01 \x01(\x03R\x03key\x129\n\x05value\x18\x02 \x01(\x0b2#.google.api.expr.v1alpha1.ReferenceR\x05value:\x028\x01\x1aZ\n\x0cTypeMapEntry\x12\x10\n\x03key\x18\x01 \x01(\x03R\x03key\x124\n\x05value\x18\x02 \x01(\x0b2\x1e.google.api.expr.v1alpha1.TypeR\x05value:\x028\x01"\xc8\x0b\n\x04Type\x12*\n\x03dyn\x18\x01 \x01(\x0b2\x16.google.protobuf.EmptyH\x00R\x03dyn\x120\n\x04null\x18\x02 \x01(\x0e2\x1a.google.protobuf.NullValueH\x00R\x04null\x12L\n\tprimitive\x18\x03 \x01(\x0e2,.google.api.expr.v1alpha1.Type.PrimitiveTypeH\x00R\tprimitive\x12H\n\x07wrapper\x18\x04 \x01(\x0e2,.google.api.expr.v1alpha1.Type.PrimitiveTypeH\x00R\x07wrapper\x12M\n\nwell_known\x18\x05 \x01(\x0e2,.google.api.expr.v1alpha1.Type.WellKnownTypeH\x00R\twellKnown\x12F\n\tlist_type\x18\x06 \x01(\x0b2\'.google.api.expr.v1alpha1.Type.ListTypeH\x00R\x08listType\x12C\n\x08map_type\x18\x07 \x01(\x0b2&.google.api.expr.v1alpha1.Type.MapTypeH\x00R\x07mapType\x12I\n\x08function\x18\x08 \x01(\x0b2+.google.api.expr.v1alpha1.Type.FunctionTypeH\x00R\x08function\x12#\n\x0cmessage_type\x18\t \x01(\tH\x00R\x0bmessageType\x12\x1f\n\ntype_param\x18\n \x01(\tH\x00R\ttypeParam\x124\n\x04type\x18\x0b \x01(\x0b2\x1e.google.api.expr.v1alpha1.TypeH\x00R\x04type\x12.\n\x05error\x18\x0c \x01(\x0b2\x16.google.protobuf.EmptyH\x00R\x05error\x12R\n\rabstract_type\x18\x0e \x01(\x0b2+.google.api.expr.v1alpha1.Type.AbstractTypeH\x00R\x0cabstractType\x1aG\n\x08ListType\x12;\n\telem_type\x18\x01 \x01(\x0b2\x1e.google.api.expr.v1alpha1.TypeR\x08elemType\x1a\x83\x01\n\x07MapType\x129\n\x08key_type\x18\x01 \x01(\x0b2\x1e.google.api.expr.v1alpha1.TypeR\x07keyType\x12=\n\nvalue_type\x18\x02 \x01(\x0b2\x1e.google.api.expr.v1alpha1.TypeR\tvalueType\x1a\x8c\x01\n\x0cFunctionType\x12?\n\x0bresult_type\x18\x01 \x01(\x0b2\x1e.google.api.expr.v1alpha1.TypeR\nresultType\x12;\n\targ_types\x18\x02 \x03(\x0b2\x1e.google.api.expr.v1alpha1.TypeR\x08argTypes\x1ak\n\x0cAbstractType\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12G\n\x0fparameter_types\x18\x02 \x03(\x0b2\x1e.google.api.expr.v1alpha1.TypeR\x0eparameterTypes"s\n\rPrimitiveType\x12\x1e\n\x1aPRIMITIVE_TYPE_UNSPECIFIED\x10\x00\x12\x08\n\x04BOOL\x10\x01\x12\t\n\x05INT64\x10\x02\x12\n\n\x06UINT64\x10\x03\x12\n\n\x06DOUBLE\x10\x04\x12\n\n\x06STRING\x10\x05\x12\t\n\x05BYTES\x10\x06"V\n\rWellKnownType\x12\x1f\n\x1bWELL_KNOWN_TYPE_UNSPECIFIED\x10\x00\x12\x07\n\x03ANY\x10\x01\x12\r\n\tTIMESTAMP\x10\x02\x12\x0c\n\x08DURATION\x10\x03B\x0b\n\ttype_kind"\xb3\x05\n\x04Decl\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12@\n\x05ident\x18\x02 \x01(\x0b2(.google.api.expr.v1alpha1.Decl.IdentDeclH\x00R\x05ident\x12I\n\x08function\x18\x03 \x01(\x0b2+.google.api.expr.v1alpha1.Decl.FunctionDeclH\x00R\x08function\x1a\x8b\x01\n\tIdentDecl\x122\n\x04type\x18\x01 \x01(\x0b2\x1e.google.api.expr.v1alpha1.TypeR\x04type\x128\n\x05value\x18\x02 \x01(\x0b2".google.api.expr.v1alpha1.ConstantR\x05value\x12\x10\n\x03doc\x18\x03 \x01(\tR\x03doc\x1a\xee\x02\n\x0cFunctionDecl\x12R\n\toverloads\x18\x01 \x03(\x0b24.google.api.expr.v1alpha1.Decl.FunctionDecl.OverloadR\toverloads\x1a\x89\x02\n\x08Overload\x12\x1f\n\x0boverload_id\x18\x01 \x01(\tR\noverloadId\x126\n\x06params\x18\x02 \x03(\x0b2\x1e.google.api.expr.v1alpha1.TypeR\x06params\x12\x1f\n\x0btype_params\x18\x03 \x03(\tR\ntypeParams\x12?\n\x0bresult_type\x18\x04 \x01(\x0b2\x1e.google.api.expr.v1alpha1.TypeR\nresultType\x120\n\x14is_instance_function\x18\x05 \x01(\x08R\x12isInstanceFunction\x12\x10\n\x03doc\x18\x06 \x01(\tR\x03docB\x0b\n\tdecl_kind"z\n\tReference\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x1f\n\x0boverload_id\x18\x03 \x03(\tR\noverloadId\x128\n\x05value\x18\x04 \x01(\x0b2".google.api.expr.v1alpha1.ConstantR\x05valueBl\n\x1ccom.google.api.expr.v1alpha1B\tDeclProtoP\x01Z<google.golang.org/genproto/googleapis/api/expr/v1alpha1;expr\xf8\x01\x01b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.api.expr.v1alpha1.checked_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ccom.google.api.expr.v1alpha1B\tDeclProtoP\x01Z<google.golang.org/genproto/googleapis/api/expr/v1alpha1;expr\xf8\x01\x01'
    _globals['_CHECKEDEXPR_REFERENCEMAPENTRY']._loaded_options = None
    _globals['_CHECKEDEXPR_REFERENCEMAPENTRY']._serialized_options = b'8\x01'
    _globals['_CHECKEDEXPR_TYPEMAPENTRY']._loaded_options = None
    _globals['_CHECKEDEXPR_TYPEMAPENTRY']._serialized_options = b'8\x01'
    _globals['_CHECKEDEXPR']._serialized_start = 167
    _globals['_CHECKEDEXPR']._serialized_end = 705
    _globals['_CHECKEDEXPR_REFERENCEMAPENTRY']._serialized_start = 513
    _globals['_CHECKEDEXPR_REFERENCEMAPENTRY']._serialized_end = 613
    _globals['_CHECKEDEXPR_TYPEMAPENTRY']._serialized_start = 615
    _globals['_CHECKEDEXPR_TYPEMAPENTRY']._serialized_end = 705
    _globals['_TYPE']._serialized_start = 708
    _globals['_TYPE']._serialized_end = 2188
    _globals['_TYPE_LISTTYPE']._serialized_start = 1513
    _globals['_TYPE_LISTTYPE']._serialized_end = 1584
    _globals['_TYPE_MAPTYPE']._serialized_start = 1587
    _globals['_TYPE_MAPTYPE']._serialized_end = 1718
    _globals['_TYPE_FUNCTIONTYPE']._serialized_start = 1721
    _globals['_TYPE_FUNCTIONTYPE']._serialized_end = 1861
    _globals['_TYPE_ABSTRACTTYPE']._serialized_start = 1863
    _globals['_TYPE_ABSTRACTTYPE']._serialized_end = 1970
    _globals['_TYPE_PRIMITIVETYPE']._serialized_start = 1972
    _globals['_TYPE_PRIMITIVETYPE']._serialized_end = 2087
    _globals['_TYPE_WELLKNOWNTYPE']._serialized_start = 2089
    _globals['_TYPE_WELLKNOWNTYPE']._serialized_end = 2175
    _globals['_DECL']._serialized_start = 2191
    _globals['_DECL']._serialized_end = 2882
    _globals['_DECL_IDENTDECL']._serialized_start = 2361
    _globals['_DECL_IDENTDECL']._serialized_end = 2500
    _globals['_DECL_FUNCTIONDECL']._serialized_start = 2503
    _globals['_DECL_FUNCTIONDECL']._serialized_end = 2869
    _globals['_DECL_FUNCTIONDECL_OVERLOAD']._serialized_start = 2604
    _globals['_DECL_FUNCTIONDECL_OVERLOAD']._serialized_end = 2869
    _globals['_REFERENCE']._serialized_start = 2884
    _globals['_REFERENCE']._serialized_end = 3006