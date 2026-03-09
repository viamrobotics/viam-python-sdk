"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 7, 34, 0, '', 'google/api/expr/v1beta1/decl.proto')
_sym_db = _symbol_database.Default()
from .....google.api.expr.v1beta1 import expr_pb2 as google_dot_api_dot_expr_dot_v1beta1_dot_expr__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n"google/api/expr/v1beta1/decl.proto\x12\x17google.api.expr.v1beta1\x1a"google/api/expr/v1beta1/expr.proto"\xc5\x01\n\x04Decl\x12\x0e\n\x02id\x18\x01 \x01(\x05R\x02id\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12\x10\n\x03doc\x18\x03 \x01(\tR\x03doc\x12:\n\x05ident\x18\x04 \x01(\x0b2".google.api.expr.v1beta1.IdentDeclH\x00R\x05ident\x12C\n\x08function\x18\x05 \x01(\x0b2%.google.api.expr.v1beta1.FunctionDeclH\x00R\x08functionB\x06\n\x04kind"r\n\x08DeclType\x12\x0e\n\x02id\x18\x01 \x01(\x05R\x02id\x12\x12\n\x04type\x18\x02 \x01(\tR\x04type\x12B\n\x0btype_params\x18\x04 \x03(\x0b2!.google.api.expr.v1beta1.DeclTypeR\ntypeParams"w\n\tIdentDecl\x125\n\x04type\x18\x03 \x01(\x0b2!.google.api.expr.v1beta1.DeclTypeR\x04type\x123\n\x05value\x18\x04 \x01(\x0b2\x1d.google.api.expr.v1beta1.ExprR\x05value"\xb7\x01\n\x0cFunctionDecl\x126\n\x04args\x18\x01 \x03(\x0b2".google.api.expr.v1beta1.IdentDeclR\x04args\x12B\n\x0breturn_type\x18\x02 \x01(\x0b2!.google.api.expr.v1beta1.DeclTypeR\nreturnType\x12+\n\x11receiver_function\x18\x03 \x01(\x08R\x10receiverFunctionBj\n\x1bcom.google.api.expr.v1beta1B\tDeclProtoP\x01Z;google.golang.org/genproto/googleapis/api/expr/v1beta1;expr\xf8\x01\x01b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.api.expr.v1beta1.decl_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1bcom.google.api.expr.v1beta1B\tDeclProtoP\x01Z;google.golang.org/genproto/googleapis/api/expr/v1beta1;expr\xf8\x01\x01'
    _globals['_DECL']._serialized_start = 100
    _globals['_DECL']._serialized_end = 297
    _globals['_DECLTYPE']._serialized_start = 299
    _globals['_DECLTYPE']._serialized_end = 413
    _globals['_IDENTDECL']._serialized_start = 415
    _globals['_IDENTDECL']._serialized_end = 534
    _globals['_FUNCTIONDECL']._serialized_start = 537
    _globals['_FUNCTIONDECL']._serialized_end = 720