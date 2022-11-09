"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1cservice/shell/v1/shell.proto\x12\x15viam.service.shell.v1\x1a\x1cgoogle/protobuf/struct.proto"j\n\x0cShellRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x17\n\x07data_in\x18\x02 \x01(\tR\x06dataIn\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"W\n\rShellResponse\x12\x19\n\x08data_out\x18\x01 \x01(\tR\x07dataOut\x12\x19\n\x08data_err\x18\x02 \x01(\tR\x07dataErr\x12\x10\n\x03eof\x18\x03 \x01(\x08R\x03eof2f\n\x0cShellService\x12V\n\x05Shell\x12#.viam.service.shell.v1.ShellRequest\x1a$.viam.service.shell.v1.ShellResponse(\x010\x01B=\n\x19com.viam.service.shell.v1Z go.viam.com/api/service/shell/v1b\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'service.shell.v1.shell_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n\x19com.viam.service.shell.v1Z go.viam.com/api/service/shell/v1'
    _SHELLREQUEST._serialized_start = 85
    _SHELLREQUEST._serialized_end = 191
    _SHELLRESPONSE._serialized_start = 193
    _SHELLRESPONSE._serialized_end = 280
    _SHELLSERVICE._serialized_start = 282
    _SHELLSERVICE._serialized_end = 384