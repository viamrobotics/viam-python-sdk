"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......proto.api.common.v1 import common_pb2 as proto_dot_api_dot_common_dot_v1_dot_common__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$proto/api/component/arm/v1/arm.proto\x12\x1aproto.api.component.arm.v1\x1a\x1cgoogle/api/annotations.proto\x1a proto/api/common/v1/common.proto"+\n\x15GetEndPositionRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name"G\n\x16GetEndPositionResponse\x12-\n\x04pose\x18\x01 \x01(\x0b2\x19.proto.api.common.v1.PoseR\x04pose"*\n\x0eJointPositions\x12\x18\n\x07degrees\x18\x01 \x03(\x01R\x07degrees".\n\x18GetJointPositionsRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name"l\n\x19GetJointPositionsResponse\x12O\n\rposition_degs\x18\x01 \x01(\x0b2*.proto.api.component.arm.v1.JointPositionsR\x0cpositionDegs"\xad\x01\n\x15MoveToPositionRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12)\n\x02to\x18\x02 \x01(\x0b2\x19.proto.api.common.v1.PoseR\x02to\x12E\n\x0bworld_state\x18\x03 \x01(\x0b2\x1f.proto.api.common.v1.WorldStateH\x00R\nworldState\x88\x01\x01B\x0e\n\x0c_world_state"\x18\n\x16MoveToPositionResponse"\x82\x01\n\x1bMoveToJointPositionsRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12O\n\rposition_degs\x18\x02 \x01(\x0b2*.proto.api.component.arm.v1.JointPositionsR\x0cpositionDegs"\x1e\n\x1cMoveToJointPositionsResponse"!\n\x0bStopRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name"\x0e\n\x0cStopResponse"\x9b\x01\n\x06Status\x12<\n\x0cend_position\x18\x01 \x01(\x0b2\x19.proto.api.common.v1.PoseR\x0bendPosition\x12S\n\x0fjoint_positions\x18\x02 \x01(\x0b2*.proto.api.component.arm.v1.JointPositionsR\x0ejointPositions2\xf9\x06\n\nArmService\x12\xab\x01\n\x0eGetEndPosition\x121.proto.api.component.arm.v1.GetEndPositionRequest\x1a2.proto.api.component.arm.v1.GetEndPositionResponse"2\x82\xd3\xe4\x93\x02,\x12*/viam/api/v1/component/arm/{name}/position\x12\xab\x01\n\x0eMoveToPosition\x121.proto.api.component.arm.v1.MoveToPositionRequest\x1a2.proto.api.component.arm.v1.MoveToPositionResponse"2\x82\xd3\xe4\x93\x02,\x1a*/viam/api/v1/component/arm/{name}/position\x12\xbb\x01\n\x11GetJointPositions\x124.proto.api.component.arm.v1.GetJointPositionsRequest\x1a5.proto.api.component.arm.v1.GetJointPositionsResponse"9\x82\xd3\xe4\x93\x023\x121/viam/api/v1/component/arm/{name}/joint_positions\x12\xc4\x01\n\x14MoveToJointPositions\x127.proto.api.component.arm.v1.MoveToJointPositionsRequest\x1a8.proto.api.component.arm.v1.MoveToJointPositionsResponse"9\x82\xd3\xe4\x93\x023\x1a1/viam/api/v1/component/arm/{name}/joint_positions\x12\x89\x01\n\x04Stop\x12\'.proto.api.component.arm.v1.StopRequest\x1a(.proto.api.component.arm.v1.StopResponse".\x82\xd3\xe4\x93\x02("&/viam/api/v1/component/arm/{name}/stopBU\n\'com.viam.rdk.proto.api.component.arm.v1Z*go.viam.com/rdk/proto/api/component/arm/v1b\x06proto3')
_GETENDPOSITIONREQUEST = DESCRIPTOR.message_types_by_name['GetEndPositionRequest']
_GETENDPOSITIONRESPONSE = DESCRIPTOR.message_types_by_name['GetEndPositionResponse']
_JOINTPOSITIONS = DESCRIPTOR.message_types_by_name['JointPositions']
_GETJOINTPOSITIONSREQUEST = DESCRIPTOR.message_types_by_name['GetJointPositionsRequest']
_GETJOINTPOSITIONSRESPONSE = DESCRIPTOR.message_types_by_name['GetJointPositionsResponse']
_MOVETOPOSITIONREQUEST = DESCRIPTOR.message_types_by_name['MoveToPositionRequest']
_MOVETOPOSITIONRESPONSE = DESCRIPTOR.message_types_by_name['MoveToPositionResponse']
_MOVETOJOINTPOSITIONSREQUEST = DESCRIPTOR.message_types_by_name['MoveToJointPositionsRequest']
_MOVETOJOINTPOSITIONSRESPONSE = DESCRIPTOR.message_types_by_name['MoveToJointPositionsResponse']
_STOPREQUEST = DESCRIPTOR.message_types_by_name['StopRequest']
_STOPRESPONSE = DESCRIPTOR.message_types_by_name['StopResponse']
_STATUS = DESCRIPTOR.message_types_by_name['Status']
GetEndPositionRequest = _reflection.GeneratedProtocolMessageType('GetEndPositionRequest', (_message.Message,), {'DESCRIPTOR': _GETENDPOSITIONREQUEST, '__module__': 'proto.api.component.arm.v1.arm_pb2'})
_sym_db.RegisterMessage(GetEndPositionRequest)
GetEndPositionResponse = _reflection.GeneratedProtocolMessageType('GetEndPositionResponse', (_message.Message,), {'DESCRIPTOR': _GETENDPOSITIONRESPONSE, '__module__': 'proto.api.component.arm.v1.arm_pb2'})
_sym_db.RegisterMessage(GetEndPositionResponse)
JointPositions = _reflection.GeneratedProtocolMessageType('JointPositions', (_message.Message,), {'DESCRIPTOR': _JOINTPOSITIONS, '__module__': 'proto.api.component.arm.v1.arm_pb2'})
_sym_db.RegisterMessage(JointPositions)
GetJointPositionsRequest = _reflection.GeneratedProtocolMessageType('GetJointPositionsRequest', (_message.Message,), {'DESCRIPTOR': _GETJOINTPOSITIONSREQUEST, '__module__': 'proto.api.component.arm.v1.arm_pb2'})
_sym_db.RegisterMessage(GetJointPositionsRequest)
GetJointPositionsResponse = _reflection.GeneratedProtocolMessageType('GetJointPositionsResponse', (_message.Message,), {'DESCRIPTOR': _GETJOINTPOSITIONSRESPONSE, '__module__': 'proto.api.component.arm.v1.arm_pb2'})
_sym_db.RegisterMessage(GetJointPositionsResponse)
MoveToPositionRequest = _reflection.GeneratedProtocolMessageType('MoveToPositionRequest', (_message.Message,), {'DESCRIPTOR': _MOVETOPOSITIONREQUEST, '__module__': 'proto.api.component.arm.v1.arm_pb2'})
_sym_db.RegisterMessage(MoveToPositionRequest)
MoveToPositionResponse = _reflection.GeneratedProtocolMessageType('MoveToPositionResponse', (_message.Message,), {'DESCRIPTOR': _MOVETOPOSITIONRESPONSE, '__module__': 'proto.api.component.arm.v1.arm_pb2'})
_sym_db.RegisterMessage(MoveToPositionResponse)
MoveToJointPositionsRequest = _reflection.GeneratedProtocolMessageType('MoveToJointPositionsRequest', (_message.Message,), {'DESCRIPTOR': _MOVETOJOINTPOSITIONSREQUEST, '__module__': 'proto.api.component.arm.v1.arm_pb2'})
_sym_db.RegisterMessage(MoveToJointPositionsRequest)
MoveToJointPositionsResponse = _reflection.GeneratedProtocolMessageType('MoveToJointPositionsResponse', (_message.Message,), {'DESCRIPTOR': _MOVETOJOINTPOSITIONSRESPONSE, '__module__': 'proto.api.component.arm.v1.arm_pb2'})
_sym_db.RegisterMessage(MoveToJointPositionsResponse)
StopRequest = _reflection.GeneratedProtocolMessageType('StopRequest', (_message.Message,), {'DESCRIPTOR': _STOPREQUEST, '__module__': 'proto.api.component.arm.v1.arm_pb2'})
_sym_db.RegisterMessage(StopRequest)
StopResponse = _reflection.GeneratedProtocolMessageType('StopResponse', (_message.Message,), {'DESCRIPTOR': _STOPRESPONSE, '__module__': 'proto.api.component.arm.v1.arm_pb2'})
_sym_db.RegisterMessage(StopResponse)
Status = _reflection.GeneratedProtocolMessageType('Status', (_message.Message,), {'DESCRIPTOR': _STATUS, '__module__': 'proto.api.component.arm.v1.arm_pb2'})
_sym_db.RegisterMessage(Status)
_ARMSERVICE = DESCRIPTOR.services_by_name['ArmService']
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b"\n'com.viam.rdk.proto.api.component.arm.v1Z*go.viam.com/rdk/proto/api/component/arm/v1"
    _ARMSERVICE.methods_by_name['GetEndPosition']._options = None
    _ARMSERVICE.methods_by_name['GetEndPosition']._serialized_options = b'\x82\xd3\xe4\x93\x02,\x12*/viam/api/v1/component/arm/{name}/position'
    _ARMSERVICE.methods_by_name['MoveToPosition']._options = None
    _ARMSERVICE.methods_by_name['MoveToPosition']._serialized_options = b'\x82\xd3\xe4\x93\x02,\x1a*/viam/api/v1/component/arm/{name}/position'
    _ARMSERVICE.methods_by_name['GetJointPositions']._options = None
    _ARMSERVICE.methods_by_name['GetJointPositions']._serialized_options = b'\x82\xd3\xe4\x93\x023\x121/viam/api/v1/component/arm/{name}/joint_positions'
    _ARMSERVICE.methods_by_name['MoveToJointPositions']._options = None
    _ARMSERVICE.methods_by_name['MoveToJointPositions']._serialized_options = b'\x82\xd3\xe4\x93\x023\x1a1/viam/api/v1/component/arm/{name}/joint_positions'
    _ARMSERVICE.methods_by_name['Stop']._options = None
    _ARMSERVICE.methods_by_name['Stop']._serialized_options = b'\x82\xd3\xe4\x93\x02("&/viam/api/v1/component/arm/{name}/stop'
    _GETENDPOSITIONREQUEST._serialized_start = 132
    _GETENDPOSITIONREQUEST._serialized_end = 175
    _GETENDPOSITIONRESPONSE._serialized_start = 177
    _GETENDPOSITIONRESPONSE._serialized_end = 248
    _JOINTPOSITIONS._serialized_start = 250
    _JOINTPOSITIONS._serialized_end = 292
    _GETJOINTPOSITIONSREQUEST._serialized_start = 294
    _GETJOINTPOSITIONSREQUEST._serialized_end = 340
    _GETJOINTPOSITIONSRESPONSE._serialized_start = 342
    _GETJOINTPOSITIONSRESPONSE._serialized_end = 450
    _MOVETOPOSITIONREQUEST._serialized_start = 453
    _MOVETOPOSITIONREQUEST._serialized_end = 626
    _MOVETOPOSITIONRESPONSE._serialized_start = 628
    _MOVETOPOSITIONRESPONSE._serialized_end = 652
    _MOVETOJOINTPOSITIONSREQUEST._serialized_start = 655
    _MOVETOJOINTPOSITIONSREQUEST._serialized_end = 785
    _MOVETOJOINTPOSITIONSRESPONSE._serialized_start = 787
    _MOVETOJOINTPOSITIONSRESPONSE._serialized_end = 817
    _STOPREQUEST._serialized_start = 819
    _STOPREQUEST._serialized_end = 852
    _STOPRESPONSE._serialized_start = 854
    _STOPRESPONSE._serialized_end = 868
    _STATUS._serialized_start = 871
    _STATUS._serialized_end = 1026
    _ARMSERVICE._serialized_start = 1029
    _ARMSERVICE._serialized_end = 1918