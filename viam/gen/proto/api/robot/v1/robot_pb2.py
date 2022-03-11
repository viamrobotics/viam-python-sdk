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
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1eproto/api/robot/v1/robot.proto\x12\x12proto.api.robot.v1\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1cgoogle/api/annotations.proto\x1a proto/api/common/v1/common.proto"\x7f\n\x0fComponentConfig\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x12\n\x04type\x18\x02 \x01(\tR\x04type\x12\x16\n\x06parent\x18\x03 \x01(\tR\x06parent\x12,\n\x04pose\x18\x04 \x01(\x0b2\x18.proto.api.robot.v1.PoseR\x04pose"\x0f\n\rConfigRequest"U\n\x0eConfigResponse\x12C\n\ncomponents\x18\x01 \x03(\x0b2#.proto.api.robot.v1.ComponentConfigR\ncomponents"%\n\x0fDoActionRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name"\x12\n\x10DoActionResponse"y\n\x04Pose\x12\x0c\n\x01x\x18\x01 \x01(\x01R\x01x\x12\x0c\n\x01y\x18\x02 \x01(\x01R\x01y\x12\x0c\n\x01z\x18\x03 \x01(\x01R\x01z\x12\x0f\n\x03o_x\x18\x04 \x01(\x01R\x02oX\x12\x0f\n\x03o_y\x18\x05 \x01(\x01R\x02oY\x12\x0f\n\x03o_z\x18\x06 \x01(\x01R\x02oZ\x12\x14\n\x05theta\x18\x07 \x01(\x01R\x05theta",\n\x16ExecuteFunctionRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name"}\n\x17ExecuteFunctionResponse\x120\n\x07results\x18\x01 \x03(\x0b2\x16.google.protobuf.ValueR\x07results\x12\x17\n\x07std_out\x18\x02 \x01(\tR\x06stdOut\x12\x17\n\x07std_err\x18\x03 \x01(\tR\x06stdErr"F\n\x14ExecuteSourceRequest\x12\x16\n\x06source\x18\x01 \x01(\tR\x06source\x12\x16\n\x06engine\x18\x02 \x01(\tR\x06engine"{\n\x15ExecuteSourceResponse\x120\n\x07results\x18\x01 \x03(\x0b2\x16.google.protobuf.ValueR\x07results\x12\x17\n\x07std_out\x18\x02 \x01(\tR\x06stdOut\x12\x17\n\x07std_err\x18\x03 \x01(\tR\x06stdErr"\x90\x01\n\x19ResourceRunCommandRequest\x12#\n\rresource_name\x18\x01 \x01(\tR\x0cresourceName\x12!\n\x0ccommand_name\x18\x02 \x01(\tR\x0bcommandName\x12+\n\x04args\x18\x03 \x01(\x0b2\x17.google.protobuf.StructR\x04args"M\n\x1aResourceRunCommandResponse\x12/\n\x06result\x18\x01 \x01(\x0b2\x17.google.protobuf.StructR\x06result2\xdc\x05\n\x0cRobotService\x12l\n\x06Config\x12!.proto.api.robot.v1.ConfigRequest\x1a".proto.api.robot.v1.ConfigResponse"\x1b\x82\xd3\xe4\x93\x02\x15\x12\x13/viam/api/v1/config\x12u\n\x08DoAction\x12#.proto.api.robot.v1.DoActionRequest\x1a$.proto.api.robot.v1.DoActionResponse"\x1e\x82\xd3\xe4\x93\x02\x18"\x16/viam/api/v1/do_action\x12\xa1\x01\n\x0fExecuteFunction\x12*.proto.api.robot.v1.ExecuteFunctionRequest\x1a+.proto.api.robot.v1.ExecuteFunctionResponse"5\x82\xd3\xe4\x93\x02/"-/viam/api/v1/functions/by_name/{name}/execute\x12\x91\x01\n\rExecuteSource\x12(.proto.api.robot.v1.ExecuteSourceRequest\x1a).proto.api.robot.v1.ExecuteSourceResponse"+\x82\xd3\xe4\x93\x02%"#/viam/api/v1/functions/execute_code\x12\xae\x01\n\x12ResourceRunCommand\x12-.proto.api.robot.v1.ResourceRunCommandRequest\x1a..proto.api.robot.v1.ResourceRunCommandResponse"9\x82\xd3\xe4\x93\x023"1/viam/api/v1/resource/{resource_name}/run_commandBE\n\x1fcom.viam.rdk.proto.api.robot.v1Z"go.viam.com/rdk/proto/api/robot/v1b\x06proto3')
_COMPONENTCONFIG = DESCRIPTOR.message_types_by_name['ComponentConfig']
_CONFIGREQUEST = DESCRIPTOR.message_types_by_name['ConfigRequest']
_CONFIGRESPONSE = DESCRIPTOR.message_types_by_name['ConfigResponse']
_DOACTIONREQUEST = DESCRIPTOR.message_types_by_name['DoActionRequest']
_DOACTIONRESPONSE = DESCRIPTOR.message_types_by_name['DoActionResponse']
_POSE = DESCRIPTOR.message_types_by_name['Pose']
_EXECUTEFUNCTIONREQUEST = DESCRIPTOR.message_types_by_name['ExecuteFunctionRequest']
_EXECUTEFUNCTIONRESPONSE = DESCRIPTOR.message_types_by_name['ExecuteFunctionResponse']
_EXECUTESOURCEREQUEST = DESCRIPTOR.message_types_by_name['ExecuteSourceRequest']
_EXECUTESOURCERESPONSE = DESCRIPTOR.message_types_by_name['ExecuteSourceResponse']
_RESOURCERUNCOMMANDREQUEST = DESCRIPTOR.message_types_by_name['ResourceRunCommandRequest']
_RESOURCERUNCOMMANDRESPONSE = DESCRIPTOR.message_types_by_name['ResourceRunCommandResponse']
ComponentConfig = _reflection.GeneratedProtocolMessageType('ComponentConfig', (_message.Message,), {'DESCRIPTOR': _COMPONENTCONFIG, '__module__': 'proto.api.robot.v1.robot_pb2'})
_sym_db.RegisterMessage(ComponentConfig)
ConfigRequest = _reflection.GeneratedProtocolMessageType('ConfigRequest', (_message.Message,), {'DESCRIPTOR': _CONFIGREQUEST, '__module__': 'proto.api.robot.v1.robot_pb2'})
_sym_db.RegisterMessage(ConfigRequest)
ConfigResponse = _reflection.GeneratedProtocolMessageType('ConfigResponse', (_message.Message,), {'DESCRIPTOR': _CONFIGRESPONSE, '__module__': 'proto.api.robot.v1.robot_pb2'})
_sym_db.RegisterMessage(ConfigResponse)
DoActionRequest = _reflection.GeneratedProtocolMessageType('DoActionRequest', (_message.Message,), {'DESCRIPTOR': _DOACTIONREQUEST, '__module__': 'proto.api.robot.v1.robot_pb2'})
_sym_db.RegisterMessage(DoActionRequest)
DoActionResponse = _reflection.GeneratedProtocolMessageType('DoActionResponse', (_message.Message,), {'DESCRIPTOR': _DOACTIONRESPONSE, '__module__': 'proto.api.robot.v1.robot_pb2'})
_sym_db.RegisterMessage(DoActionResponse)
Pose = _reflection.GeneratedProtocolMessageType('Pose', (_message.Message,), {'DESCRIPTOR': _POSE, '__module__': 'proto.api.robot.v1.robot_pb2'})
_sym_db.RegisterMessage(Pose)
ExecuteFunctionRequest = _reflection.GeneratedProtocolMessageType('ExecuteFunctionRequest', (_message.Message,), {'DESCRIPTOR': _EXECUTEFUNCTIONREQUEST, '__module__': 'proto.api.robot.v1.robot_pb2'})
_sym_db.RegisterMessage(ExecuteFunctionRequest)
ExecuteFunctionResponse = _reflection.GeneratedProtocolMessageType('ExecuteFunctionResponse', (_message.Message,), {'DESCRIPTOR': _EXECUTEFUNCTIONRESPONSE, '__module__': 'proto.api.robot.v1.robot_pb2'})
_sym_db.RegisterMessage(ExecuteFunctionResponse)
ExecuteSourceRequest = _reflection.GeneratedProtocolMessageType('ExecuteSourceRequest', (_message.Message,), {'DESCRIPTOR': _EXECUTESOURCEREQUEST, '__module__': 'proto.api.robot.v1.robot_pb2'})
_sym_db.RegisterMessage(ExecuteSourceRequest)
ExecuteSourceResponse = _reflection.GeneratedProtocolMessageType('ExecuteSourceResponse', (_message.Message,), {'DESCRIPTOR': _EXECUTESOURCERESPONSE, '__module__': 'proto.api.robot.v1.robot_pb2'})
_sym_db.RegisterMessage(ExecuteSourceResponse)
ResourceRunCommandRequest = _reflection.GeneratedProtocolMessageType('ResourceRunCommandRequest', (_message.Message,), {'DESCRIPTOR': _RESOURCERUNCOMMANDREQUEST, '__module__': 'proto.api.robot.v1.robot_pb2'})
_sym_db.RegisterMessage(ResourceRunCommandRequest)
ResourceRunCommandResponse = _reflection.GeneratedProtocolMessageType('ResourceRunCommandResponse', (_message.Message,), {'DESCRIPTOR': _RESOURCERUNCOMMANDRESPONSE, '__module__': 'proto.api.robot.v1.robot_pb2'})
_sym_db.RegisterMessage(ResourceRunCommandResponse)
_ROBOTSERVICE = DESCRIPTOR.services_by_name['RobotService']
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n\x1fcom.viam.rdk.proto.api.robot.v1Z"go.viam.com/rdk/proto/api/robot/v1'
    _ROBOTSERVICE.methods_by_name['Config']._options = None
    _ROBOTSERVICE.methods_by_name['Config']._serialized_options = b'\x82\xd3\xe4\x93\x02\x15\x12\x13/viam/api/v1/config'
    _ROBOTSERVICE.methods_by_name['DoAction']._options = None
    _ROBOTSERVICE.methods_by_name['DoAction']._serialized_options = b'\x82\xd3\xe4\x93\x02\x18"\x16/viam/api/v1/do_action'
    _ROBOTSERVICE.methods_by_name['ExecuteFunction']._options = None
    _ROBOTSERVICE.methods_by_name['ExecuteFunction']._serialized_options = b'\x82\xd3\xe4\x93\x02/"-/viam/api/v1/functions/by_name/{name}/execute'
    _ROBOTSERVICE.methods_by_name['ExecuteSource']._options = None
    _ROBOTSERVICE.methods_by_name['ExecuteSource']._serialized_options = b'\x82\xd3\xe4\x93\x02%"#/viam/api/v1/functions/execute_code'
    _ROBOTSERVICE.methods_by_name['ResourceRunCommand']._options = None
    _ROBOTSERVICE.methods_by_name['ResourceRunCommand']._serialized_options = b'\x82\xd3\xe4\x93\x023"1/viam/api/v1/resource/{resource_name}/run_command'
    _COMPONENTCONFIG._serialized_start = 148
    _COMPONENTCONFIG._serialized_end = 275
    _CONFIGREQUEST._serialized_start = 277
    _CONFIGREQUEST._serialized_end = 292
    _CONFIGRESPONSE._serialized_start = 294
    _CONFIGRESPONSE._serialized_end = 379
    _DOACTIONREQUEST._serialized_start = 381
    _DOACTIONREQUEST._serialized_end = 418
    _DOACTIONRESPONSE._serialized_start = 420
    _DOACTIONRESPONSE._serialized_end = 438
    _POSE._serialized_start = 440
    _POSE._serialized_end = 561
    _EXECUTEFUNCTIONREQUEST._serialized_start = 563
    _EXECUTEFUNCTIONREQUEST._serialized_end = 607
    _EXECUTEFUNCTIONRESPONSE._serialized_start = 609
    _EXECUTEFUNCTIONRESPONSE._serialized_end = 734
    _EXECUTESOURCEREQUEST._serialized_start = 736
    _EXECUTESOURCEREQUEST._serialized_end = 806
    _EXECUTESOURCERESPONSE._serialized_start = 808
    _EXECUTESOURCERESPONSE._serialized_end = 931
    _RESOURCERUNCOMMANDREQUEST._serialized_start = 934
    _RESOURCERUNCOMMANDREQUEST._serialized_end = 1078
    _RESOURCERUNCOMMANDRESPONSE._serialized_start = 1080
    _RESOURCERUNCOMMANDRESPONSE._serialized_end = 1157
    _ROBOTSERVICE._serialized_start = 1160
    _ROBOTSERVICE._serialized_end = 1892