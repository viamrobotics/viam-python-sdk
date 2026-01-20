"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....common.v1 import common_pb2 as common_dot_v1_dot_common__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n component/button/v1/button.proto\x12\x18viam.component.button.v1\x1a\x16common/v1/common.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1cgoogle/protobuf/struct.proto"P\n\x0bPushRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"\x0e\n\x0cPushResponse2\xa6\x02\n\rButtonService\x12\x88\x01\n\x04Push\x12%.viam.component.button.v1.PushRequest\x1a&.viam.component.button.v1.PushResponse"1\x82\xd3\xe4\x93\x02+\x1a)/viam/api/v1/component/button/{name}/push\x12\x89\x01\n\tDoCommand\x12 .viam.common.v1.DoCommandRequest\x1a!.viam.common.v1.DoCommandResponse"7\x82\xd3\xe4\x93\x021"//viam/api/v1/component/button/{name}/do_commandBC\n\x1ccom.viam.component.button.v1Z#go.viam.com/api/component/button/v1b\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'component.button.v1.button_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n\x1ccom.viam.component.button.v1Z#go.viam.com/api/component/button/v1'
    _BUTTONSERVICE.methods_by_name['Push']._options = None
    _BUTTONSERVICE.methods_by_name['Push']._serialized_options = b'\x82\xd3\xe4\x93\x02+\x1a)/viam/api/v1/component/button/{name}/push'
    _BUTTONSERVICE.methods_by_name['DoCommand']._options = None
    _BUTTONSERVICE.methods_by_name['DoCommand']._serialized_options = b'\x82\xd3\xe4\x93\x021"//viam/api/v1/component/button/{name}/do_command'
    _PUSHREQUEST._serialized_start = 146
    _PUSHREQUEST._serialized_end = 226
    _PUSHRESPONSE._serialized_start = 228
    _PUSHRESPONSE._serialized_end = 242
    _BUTTONSERVICE._serialized_start = 245
    _BUTTONSERVICE._serialized_end = 539