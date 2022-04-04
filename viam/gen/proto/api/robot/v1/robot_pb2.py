"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....proto.api.common.v1 import common_pb2 as proto_dot_api_dot_common_dot_v1_dot_common__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1eproto/api/robot/v1/robot.proto\x12\x12proto.api.robot.v1\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1cgoogle/api/annotations.proto\x1a proto/api/common/v1/common.proto"%\n\x0fDoActionRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name"\x12\n\x10DoActionResponse"\x90\x01\n\x19ResourceRunCommandRequest\x12#\n\rresource_name\x18\x01 \x01(\tR\x0cresourceName\x12!\n\x0ccommand_name\x18\x02 \x01(\tR\x0bcommandName\x12+\n\x04args\x18\x03 \x01(\x0b2\x17.google.protobuf.StructR\x04args"M\n\x1aResourceRunCommandResponse\x12/\n\x06result\x18\x01 \x01(\x0b2\x17.google.protobuf.StructR\x06result2\xb6\x02\n\x0cRobotService\x12u\n\x08DoAction\x12#.proto.api.robot.v1.DoActionRequest\x1a$.proto.api.robot.v1.DoActionResponse"\x1e\x82\xd3\xe4\x93\x02\x18"\x16/viam/api/v1/do_action\x12\xae\x01\n\x12ResourceRunCommand\x12-.proto.api.robot.v1.ResourceRunCommandRequest\x1a..proto.api.robot.v1.ResourceRunCommandResponse"9\x82\xd3\xe4\x93\x023"1/viam/api/v1/resource/{resource_name}/run_commandBE\n\x1fcom.viam.rdk.proto.api.robot.v1Z"go.viam.com/rdk/proto/api/robot/v1b\x06proto3')
_DOACTIONREQUEST = DESCRIPTOR.message_types_by_name['DoActionRequest']
_DOACTIONRESPONSE = DESCRIPTOR.message_types_by_name['DoActionResponse']
_RESOURCERUNCOMMANDREQUEST = DESCRIPTOR.message_types_by_name['ResourceRunCommandRequest']
_RESOURCERUNCOMMANDRESPONSE = DESCRIPTOR.message_types_by_name['ResourceRunCommandResponse']
DoActionRequest = _reflection.GeneratedProtocolMessageType('DoActionRequest', (_message.Message,), {'DESCRIPTOR': _DOACTIONREQUEST, '__module__': 'proto.api.robot.v1.robot_pb2'})
_sym_db.RegisterMessage(DoActionRequest)
DoActionResponse = _reflection.GeneratedProtocolMessageType('DoActionResponse', (_message.Message,), {'DESCRIPTOR': _DOACTIONRESPONSE, '__module__': 'proto.api.robot.v1.robot_pb2'})
_sym_db.RegisterMessage(DoActionResponse)
ResourceRunCommandRequest = _reflection.GeneratedProtocolMessageType('ResourceRunCommandRequest', (_message.Message,), {'DESCRIPTOR': _RESOURCERUNCOMMANDREQUEST, '__module__': 'proto.api.robot.v1.robot_pb2', '__doc__': 'Attributes:\n      resource_name:\n          Note(erd): okay in v1 because names are unique. v2 should be a\n          VRN\n  '})
_sym_db.RegisterMessage(ResourceRunCommandRequest)
ResourceRunCommandResponse = _reflection.GeneratedProtocolMessageType('ResourceRunCommandResponse', (_message.Message,), {'DESCRIPTOR': _RESOURCERUNCOMMANDRESPONSE, '__module__': 'proto.api.robot.v1.robot_pb2'})
_sym_db.RegisterMessage(ResourceRunCommandResponse)
_ROBOTSERVICE = DESCRIPTOR.services_by_name['RobotService']
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n\x1fcom.viam.rdk.proto.api.robot.v1Z"go.viam.com/rdk/proto/api/robot/v1'
    _ROBOTSERVICE.methods_by_name['DoAction']._options = None
    _ROBOTSERVICE.methods_by_name['DoAction']._serialized_options = b'\x82\xd3\xe4\x93\x02\x18"\x16/viam/api/v1/do_action'
    _ROBOTSERVICE.methods_by_name['ResourceRunCommand']._options = None
    _ROBOTSERVICE.methods_by_name['ResourceRunCommand']._serialized_options = b'\x82\xd3\xe4\x93\x023"1/viam/api/v1/resource/{resource_name}/run_command'
    _DOACTIONREQUEST._serialized_start = 148
    _DOACTIONREQUEST._serialized_end = 185
    _DOACTIONRESPONSE._serialized_start = 187
    _DOACTIONRESPONSE._serialized_end = 205
    _RESOURCERUNCOMMANDREQUEST._serialized_start = 208
    _RESOURCERUNCOMMANDREQUEST._serialized_end = 352
    _RESOURCERUNCOMMANDRESPONSE._serialized_start = 354
    _RESOURCERUNCOMMANDRESPONSE._serialized_end = 431
    _ROBOTSERVICE._serialized_start = 434
    _ROBOTSERVICE._serialized_end = 744