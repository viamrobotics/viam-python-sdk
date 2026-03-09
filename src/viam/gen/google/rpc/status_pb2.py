"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 7, 34, 0, '', 'google/rpc/status.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17google/rpc/status.proto\x12\ngoogle.rpc\x1a\x19google/protobuf/any.proto"f\n\x06Status\x12\x12\n\x04code\x18\x01 \x01(\x05R\x04code\x12\x18\n\x07message\x18\x02 \x01(\tR\x07message\x12.\n\x07details\x18\x03 \x03(\x0b2\x14.google.protobuf.AnyR\x07detailsBa\n\x0ecom.google.rpcB\x0bStatusProtoP\x01Z7google.golang.org/genproto/googleapis/rpc/status;status\xf8\x01\x01\xa2\x02\x03RPCb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.rpc.status_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x0ecom.google.rpcB\x0bStatusProtoP\x01Z7google.golang.org/genproto/googleapis/rpc/status;status\xf8\x01\x01\xa2\x02\x03RPC'
    _globals['_STATUS']._serialized_start = 66
    _globals['_STATUS']._serialized_end = 168