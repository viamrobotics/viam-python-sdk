"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......proto.api.common.v1 import common_pb2 as proto_dot_api_dot_common_dot_v1_dot_common__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$proto/api/component/arm/v1/arm.proto\x12\x1aproto.api.component.arm.v1\x1a\x1cgoogle/api/annotations.proto\x1a proto/api/common/v1/common.proto"-\n\x11ArmJointPositions\x12\x18\n\x07degrees\x18\x01 \x03(\x01R\x07degrees"+\n\x15GetEndPositionRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name"G\n\x16GetEndPositionResponse\x12-\n\x04pose\x18\x01 \x01(\x0b2\x19.proto.api.common.v1.PoseR\x04pose".\n\x18GetJointPositionsRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name"o\n\x19GetJointPositionsResponse\x12R\n\rposition_degs\x18\x01 \x01(\x0b2-.proto.api.component.arm.v1.ArmJointPositionsR\x0cpositionDegs"\xad\x01\n\x15MoveToPositionRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12)\n\x02to\x18\x02 \x01(\x0b2\x19.proto.api.common.v1.PoseR\x02to\x12E\n\x0bworld_state\x18\x03 \x01(\x0b2\x1f.proto.api.common.v1.WorldStateH\x00R\nworldState\x88\x01\x01B\x0e\n\x0c_world_state"\x18\n\x16MoveToPositionResponse"\x85\x01\n\x1bMoveToJointPositionsRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12R\n\rposition_degs\x18\x02 \x01(\x0b2-.proto.api.component.arm.v1.ArmJointPositionsR\x0cpositionDegs"\x1e\n\x1cMoveToJointPositionsResponse2\xf9\x05\n\nArmService\x12\xae\x01\n\x0eGetEndPosition\x121.proto.api.component.arm.v1.GetEndPositionRequest\x1a2.proto.api.component.arm.v1.GetEndPositionResponse"5\x82\xd3\xe4\x93\x02/\x12-/api/v1/component/arm/{name}/current_position\x12\xae\x01\n\x0eMoveToPosition\x121.proto.api.component.arm.v1.MoveToPositionRequest\x1a2.proto.api.component.arm.v1.MoveToPositionResponse"5\x82\xd3\xe4\x93\x02/\x1a-/api/v1/component/arm/{name}/move_to_position\x12\xbe\x01\n\x11GetJointPositions\x124.proto.api.component.arm.v1.GetJointPositionsRequest\x1a5.proto.api.component.arm.v1.GetJointPositionsResponse"<\x82\xd3\xe4\x93\x026\x124/api/v1/component/arm/{name}/current_joint_positions\x12\xc7\x01\n\x14MoveToJointPositions\x127.proto.api.component.arm.v1.MoveToJointPositionsRequest\x1a8.proto.api.component.arm.v1.MoveToJointPositionsResponse"<\x82\xd3\xe4\x93\x026\x1a4/api/v1/component/arm/{name}/move_to_joint_positionsBU\n\'com.viam.rdk.proto.api.component.arm.v1Z*go.viam.com/rdk/proto/api/component/arm/v1b\x06proto3')
_ARMJOINTPOSITIONS = DESCRIPTOR.message_types_by_name['ArmJointPositions']
_GETENDPOSITIONREQUEST = DESCRIPTOR.message_types_by_name['GetEndPositionRequest']
_GETENDPOSITIONRESPONSE = DESCRIPTOR.message_types_by_name['GetEndPositionResponse']
_GETJOINTPOSITIONSREQUEST = DESCRIPTOR.message_types_by_name['GetJointPositionsRequest']
_GETJOINTPOSITIONSRESPONSE = DESCRIPTOR.message_types_by_name['GetJointPositionsResponse']
_MOVETOPOSITIONREQUEST = DESCRIPTOR.message_types_by_name['MoveToPositionRequest']
_MOVETOPOSITIONRESPONSE = DESCRIPTOR.message_types_by_name['MoveToPositionResponse']
_MOVETOJOINTPOSITIONSREQUEST = DESCRIPTOR.message_types_by_name['MoveToJointPositionsRequest']
_MOVETOJOINTPOSITIONSRESPONSE = DESCRIPTOR.message_types_by_name['MoveToJointPositionsResponse']
ArmJointPositions = _reflection.GeneratedProtocolMessageType('ArmJointPositions', (_message.Message,), {'DESCRIPTOR': _ARMJOINTPOSITIONS, '__module__': 'proto.api.component.arm.v1.arm_pb2'})
_sym_db.RegisterMessage(ArmJointPositions)
GetEndPositionRequest = _reflection.GeneratedProtocolMessageType('GetEndPositionRequest', (_message.Message,), {'DESCRIPTOR': _GETENDPOSITIONREQUEST, '__module__': 'proto.api.component.arm.v1.arm_pb2'})
_sym_db.RegisterMessage(GetEndPositionRequest)
GetEndPositionResponse = _reflection.GeneratedProtocolMessageType('GetEndPositionResponse', (_message.Message,), {'DESCRIPTOR': _GETENDPOSITIONRESPONSE, '__module__': 'proto.api.component.arm.v1.arm_pb2'})
_sym_db.RegisterMessage(GetEndPositionResponse)
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
_ARMSERVICE = DESCRIPTOR.services_by_name['ArmService']
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b"\n'com.viam.rdk.proto.api.component.arm.v1Z*go.viam.com/rdk/proto/api/component/arm/v1"
    _ARMSERVICE.methods_by_name['GetEndPosition']._options = None
    _ARMSERVICE.methods_by_name['GetEndPosition']._serialized_options = b'\x82\xd3\xe4\x93\x02/\x12-/api/v1/component/arm/{name}/current_position'
    _ARMSERVICE.methods_by_name['MoveToPosition']._options = None
    _ARMSERVICE.methods_by_name['MoveToPosition']._serialized_options = b'\x82\xd3\xe4\x93\x02/\x1a-/api/v1/component/arm/{name}/move_to_position'
    _ARMSERVICE.methods_by_name['GetJointPositions']._options = None
    _ARMSERVICE.methods_by_name['GetJointPositions']._serialized_options = b'\x82\xd3\xe4\x93\x026\x124/api/v1/component/arm/{name}/current_joint_positions'
    _ARMSERVICE.methods_by_name['MoveToJointPositions']._options = None
    _ARMSERVICE.methods_by_name['MoveToJointPositions']._serialized_options = b'\x82\xd3\xe4\x93\x026\x1a4/api/v1/component/arm/{name}/move_to_joint_positions'
    _ARMJOINTPOSITIONS._serialized_start = 132
    _ARMJOINTPOSITIONS._serialized_end = 177
    _GETENDPOSITIONREQUEST._serialized_start = 179
    _GETENDPOSITIONREQUEST._serialized_end = 222
    _GETENDPOSITIONRESPONSE._serialized_start = 224
    _GETENDPOSITIONRESPONSE._serialized_end = 295
    _GETJOINTPOSITIONSREQUEST._serialized_start = 297
    _GETJOINTPOSITIONSREQUEST._serialized_end = 343
    _GETJOINTPOSITIONSRESPONSE._serialized_start = 345
    _GETJOINTPOSITIONSRESPONSE._serialized_end = 456
    _MOVETOPOSITIONREQUEST._serialized_start = 459
    _MOVETOPOSITIONREQUEST._serialized_end = 632
    _MOVETOPOSITIONRESPONSE._serialized_start = 634
    _MOVETOPOSITIONRESPONSE._serialized_end = 658
    _MOVETOJOINTPOSITIONSREQUEST._serialized_start = 661
    _MOVETOJOINTPOSITIONSREQUEST._serialized_end = 794
    _MOVETOJOINTPOSITIONSRESPONSE._serialized_start = 796
    _MOVETOJOINTPOSITIONSRESPONSE._serialized_end = 826
    _ARMSERVICE._serialized_start = 829
    _ARMSERVICE._serialized_end = 1590