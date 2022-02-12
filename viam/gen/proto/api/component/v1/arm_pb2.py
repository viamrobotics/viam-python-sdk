"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....proto.api.common.v1 import common_pb2 as proto_dot_api_dot_common_dot_v1_dot_common__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n proto/api/component/v1/arm.proto\x12\x16proto.api.component.v1\x1a\x1cgoogle/api/annotations.proto\x1a proto/api/common/v1/common.proto"-\n\x11ArmJointPositions\x12\x18\n\x07degrees\x18\x01 \x03(\x01R\x07degrees"5\n\x1fArmServiceGetEndPositionRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name"Q\n ArmServiceGetEndPositionResponse\x12-\n\x04pose\x18\x01 \x01(\x0b2\x19.proto.api.common.v1.PoseR\x04pose"8\n"ArmServiceGetJointPositionsRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name"u\n#ArmServiceGetJointPositionsResponse\x12N\n\rposition_degs\x18\x01 \x01(\x0b2).proto.api.component.v1.ArmJointPositionsR\x0cpositionDegs"d\n\x1fArmServiceMoveToPositionRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12-\n\x04pose\x18\x02 \x01(\x0b2\x19.proto.api.common.v1.PoseR\x04pose""\n ArmServiceMoveToPositionResponse"\x8b\x01\n%ArmServiceMoveToJointPositionsRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12N\n\rposition_degs\x18\x02 \x01(\x0b2).proto.api.component.v1.ArmJointPositionsR\x0cpositionDegs"(\n&ArmServiceMoveToJointPositionsResponse2\xa9\x06\n\nArmService\x12\xba\x01\n\x0eGetEndPosition\x127.proto.api.component.v1.ArmServiceGetEndPositionRequest\x1a8.proto.api.component.v1.ArmServiceGetEndPositionResponse"5\x82\xd3\xe4\x93\x02/\x12-/api/v1/component/arm/{name}/current_position\x12\xba\x01\n\x0eMoveToPosition\x127.proto.api.component.v1.ArmServiceMoveToPositionRequest\x1a8.proto.api.component.v1.ArmServiceMoveToPositionResponse"5\x82\xd3\xe4\x93\x02/\x1a-/api/v1/component/arm/{name}/move_to_position\x12\xca\x01\n\x11GetJointPositions\x12:.proto.api.component.v1.ArmServiceGetJointPositionsRequest\x1a;.proto.api.component.v1.ArmServiceGetJointPositionsResponse"<\x82\xd3\xe4\x93\x026\x124/api/v1/component/arm/{name}/current_joint_positions\x12\xd3\x01\n\x14MoveToJointPositions\x12=.proto.api.component.v1.ArmServiceMoveToJointPositionsRequest\x1a>.proto.api.component.v1.ArmServiceMoveToJointPositionsResponse"<\x82\xd3\xe4\x93\x026\x1a4/api/v1/component/arm/{name}/move_to_joint_positionsBM\n#com.viam.rdk.proto.api.component.v1Z&go.viam.com/rdk/proto/api/component/v1b\x06proto3')
_ARMJOINTPOSITIONS = DESCRIPTOR.message_types_by_name['ArmJointPositions']
_ARMSERVICEGETENDPOSITIONREQUEST = DESCRIPTOR.message_types_by_name['ArmServiceGetEndPositionRequest']
_ARMSERVICEGETENDPOSITIONRESPONSE = DESCRIPTOR.message_types_by_name['ArmServiceGetEndPositionResponse']
_ARMSERVICEGETJOINTPOSITIONSREQUEST = DESCRIPTOR.message_types_by_name['ArmServiceGetJointPositionsRequest']
_ARMSERVICEGETJOINTPOSITIONSRESPONSE = DESCRIPTOR.message_types_by_name['ArmServiceGetJointPositionsResponse']
_ARMSERVICEMOVETOPOSITIONREQUEST = DESCRIPTOR.message_types_by_name['ArmServiceMoveToPositionRequest']
_ARMSERVICEMOVETOPOSITIONRESPONSE = DESCRIPTOR.message_types_by_name['ArmServiceMoveToPositionResponse']
_ARMSERVICEMOVETOJOINTPOSITIONSREQUEST = DESCRIPTOR.message_types_by_name['ArmServiceMoveToJointPositionsRequest']
_ARMSERVICEMOVETOJOINTPOSITIONSRESPONSE = DESCRIPTOR.message_types_by_name['ArmServiceMoveToJointPositionsResponse']
ArmJointPositions = _reflection.GeneratedProtocolMessageType('ArmJointPositions', (_message.Message,), {'DESCRIPTOR': _ARMJOINTPOSITIONS, '__module__': 'proto.api.component.v1.arm_pb2'})
_sym_db.RegisterMessage(ArmJointPositions)
ArmServiceGetEndPositionRequest = _reflection.GeneratedProtocolMessageType('ArmServiceGetEndPositionRequest', (_message.Message,), {'DESCRIPTOR': _ARMSERVICEGETENDPOSITIONREQUEST, '__module__': 'proto.api.component.v1.arm_pb2'})
_sym_db.RegisterMessage(ArmServiceGetEndPositionRequest)
ArmServiceGetEndPositionResponse = _reflection.GeneratedProtocolMessageType('ArmServiceGetEndPositionResponse', (_message.Message,), {'DESCRIPTOR': _ARMSERVICEGETENDPOSITIONRESPONSE, '__module__': 'proto.api.component.v1.arm_pb2'})
_sym_db.RegisterMessage(ArmServiceGetEndPositionResponse)
ArmServiceGetJointPositionsRequest = _reflection.GeneratedProtocolMessageType('ArmServiceGetJointPositionsRequest', (_message.Message,), {'DESCRIPTOR': _ARMSERVICEGETJOINTPOSITIONSREQUEST, '__module__': 'proto.api.component.v1.arm_pb2'})
_sym_db.RegisterMessage(ArmServiceGetJointPositionsRequest)
ArmServiceGetJointPositionsResponse = _reflection.GeneratedProtocolMessageType('ArmServiceGetJointPositionsResponse', (_message.Message,), {'DESCRIPTOR': _ARMSERVICEGETJOINTPOSITIONSRESPONSE, '__module__': 'proto.api.component.v1.arm_pb2'})
_sym_db.RegisterMessage(ArmServiceGetJointPositionsResponse)
ArmServiceMoveToPositionRequest = _reflection.GeneratedProtocolMessageType('ArmServiceMoveToPositionRequest', (_message.Message,), {'DESCRIPTOR': _ARMSERVICEMOVETOPOSITIONREQUEST, '__module__': 'proto.api.component.v1.arm_pb2'})
_sym_db.RegisterMessage(ArmServiceMoveToPositionRequest)
ArmServiceMoveToPositionResponse = _reflection.GeneratedProtocolMessageType('ArmServiceMoveToPositionResponse', (_message.Message,), {'DESCRIPTOR': _ARMSERVICEMOVETOPOSITIONRESPONSE, '__module__': 'proto.api.component.v1.arm_pb2'})
_sym_db.RegisterMessage(ArmServiceMoveToPositionResponse)
ArmServiceMoveToJointPositionsRequest = _reflection.GeneratedProtocolMessageType('ArmServiceMoveToJointPositionsRequest', (_message.Message,), {'DESCRIPTOR': _ARMSERVICEMOVETOJOINTPOSITIONSREQUEST, '__module__': 'proto.api.component.v1.arm_pb2'})
_sym_db.RegisterMessage(ArmServiceMoveToJointPositionsRequest)
ArmServiceMoveToJointPositionsResponse = _reflection.GeneratedProtocolMessageType('ArmServiceMoveToJointPositionsResponse', (_message.Message,), {'DESCRIPTOR': _ARMSERVICEMOVETOJOINTPOSITIONSRESPONSE, '__module__': 'proto.api.component.v1.arm_pb2'})
_sym_db.RegisterMessage(ArmServiceMoveToJointPositionsResponse)
_ARMSERVICE = DESCRIPTOR.services_by_name['ArmService']
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n#com.viam.rdk.proto.api.component.v1Z&go.viam.com/rdk/proto/api/component/v1'
    _ARMSERVICE.methods_by_name['GetEndPosition']._options = None
    _ARMSERVICE.methods_by_name['GetEndPosition']._serialized_options = b'\x82\xd3\xe4\x93\x02/\x12-/api/v1/component/arm/{name}/current_position'
    _ARMSERVICE.methods_by_name['MoveToPosition']._options = None
    _ARMSERVICE.methods_by_name['MoveToPosition']._serialized_options = b'\x82\xd3\xe4\x93\x02/\x1a-/api/v1/component/arm/{name}/move_to_position'
    _ARMSERVICE.methods_by_name['GetJointPositions']._options = None
    _ARMSERVICE.methods_by_name['GetJointPositions']._serialized_options = b'\x82\xd3\xe4\x93\x026\x124/api/v1/component/arm/{name}/current_joint_positions'
    _ARMSERVICE.methods_by_name['MoveToJointPositions']._options = None
    _ARMSERVICE.methods_by_name['MoveToJointPositions']._serialized_options = b'\x82\xd3\xe4\x93\x026\x1a4/api/v1/component/arm/{name}/move_to_joint_positions'
    _ARMJOINTPOSITIONS._serialized_start = 124
    _ARMJOINTPOSITIONS._serialized_end = 169
    _ARMSERVICEGETENDPOSITIONREQUEST._serialized_start = 171
    _ARMSERVICEGETENDPOSITIONREQUEST._serialized_end = 224
    _ARMSERVICEGETENDPOSITIONRESPONSE._serialized_start = 226
    _ARMSERVICEGETENDPOSITIONRESPONSE._serialized_end = 307
    _ARMSERVICEGETJOINTPOSITIONSREQUEST._serialized_start = 309
    _ARMSERVICEGETJOINTPOSITIONSREQUEST._serialized_end = 365
    _ARMSERVICEGETJOINTPOSITIONSRESPONSE._serialized_start = 367
    _ARMSERVICEGETJOINTPOSITIONSRESPONSE._serialized_end = 484
    _ARMSERVICEMOVETOPOSITIONREQUEST._serialized_start = 486
    _ARMSERVICEMOVETOPOSITIONREQUEST._serialized_end = 586
    _ARMSERVICEMOVETOPOSITIONRESPONSE._serialized_start = 588
    _ARMSERVICEMOVETOPOSITIONRESPONSE._serialized_end = 622
    _ARMSERVICEMOVETOJOINTPOSITIONSREQUEST._serialized_start = 625
    _ARMSERVICEMOVETOJOINTPOSITIONSREQUEST._serialized_end = 764
    _ARMSERVICEMOVETOJOINTPOSITIONSRESPONSE._serialized_start = 766
    _ARMSERVICEMOVETOJOINTPOSITIONSRESPONSE._serialized_end = 806
    _ARMSERVICE._serialized_start = 809
    _ARMSERVICE._serialized_end = 1618