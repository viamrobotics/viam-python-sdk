"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(proto/api/component/servo/v1/servo.proto\x12\x1cproto.api.component.servo.v1\x1a\x1cgoogle/api/annotations.proto">\n\x0bMoveRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x1b\n\tangle_deg\x18\x02 \x01(\rR\x08angleDeg"\x0e\n\x0cMoveResponse"(\n\x12GetPositionRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name"8\n\x13GetPositionResponse\x12!\n\x0cposition_deg\x18\x01 \x01(\rR\x0bpositionDeg2\xc1\x02\n\x0cServoService\x12\x8a\x01\n\x04Move\x12).proto.api.component.servo.v1.MoveRequest\x1a*.proto.api.component.servo.v1.MoveResponse"+\x82\xd3\xe4\x93\x02%\x1a#/api/v1/component/servo/{name}/move\x12\xa3\x01\n\x0bGetPosition\x120.proto.api.component.servo.v1.GetPositionRequest\x1a1.proto.api.component.servo.v1.GetPositionResponse"/\x82\xd3\xe4\x93\x02)\x12\'/api/v1/component/servo/{name}/positionBY\n)com.viam.rdk.proto.api.component.servo.v1Z,go.viam.com/rdk/proto/api/component/servo/v1b\x06proto3')
_MOVEREQUEST = DESCRIPTOR.message_types_by_name['MoveRequest']
_MOVERESPONSE = DESCRIPTOR.message_types_by_name['MoveResponse']
_GETPOSITIONREQUEST = DESCRIPTOR.message_types_by_name['GetPositionRequest']
_GETPOSITIONRESPONSE = DESCRIPTOR.message_types_by_name['GetPositionResponse']
MoveRequest = _reflection.GeneratedProtocolMessageType('MoveRequest', (_message.Message,), {'DESCRIPTOR': _MOVEREQUEST, '__module__': 'proto.api.component.servo.v1.servo_pb2'})
_sym_db.RegisterMessage(MoveRequest)
MoveResponse = _reflection.GeneratedProtocolMessageType('MoveResponse', (_message.Message,), {'DESCRIPTOR': _MOVERESPONSE, '__module__': 'proto.api.component.servo.v1.servo_pb2'})
_sym_db.RegisterMessage(MoveResponse)
GetPositionRequest = _reflection.GeneratedProtocolMessageType('GetPositionRequest', (_message.Message,), {'DESCRIPTOR': _GETPOSITIONREQUEST, '__module__': 'proto.api.component.servo.v1.servo_pb2'})
_sym_db.RegisterMessage(GetPositionRequest)
GetPositionResponse = _reflection.GeneratedProtocolMessageType('GetPositionResponse', (_message.Message,), {'DESCRIPTOR': _GETPOSITIONRESPONSE, '__module__': 'proto.api.component.servo.v1.servo_pb2'})
_sym_db.RegisterMessage(GetPositionResponse)
_SERVOSERVICE = DESCRIPTOR.services_by_name['ServoService']
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n)com.viam.rdk.proto.api.component.servo.v1Z,go.viam.com/rdk/proto/api/component/servo/v1'
    _SERVOSERVICE.methods_by_name['Move']._options = None
    _SERVOSERVICE.methods_by_name['Move']._serialized_options = b'\x82\xd3\xe4\x93\x02%\x1a#/api/v1/component/servo/{name}/move'
    _SERVOSERVICE.methods_by_name['GetPosition']._options = None
    _SERVOSERVICE.methods_by_name['GetPosition']._serialized_options = b"\x82\xd3\xe4\x93\x02)\x12'/api/v1/component/servo/{name}/position"
    _MOVEREQUEST._serialized_start = 104
    _MOVEREQUEST._serialized_end = 166
    _MOVERESPONSE._serialized_start = 168
    _MOVERESPONSE._serialized_end = 182
    _GETPOSITIONREQUEST._serialized_start = 184
    _GETPOSITIONREQUEST._serialized_end = 224
    _GETPOSITIONRESPONSE._serialized_start = 226
    _GETPOSITIONRESPONSE._serialized_end = 282
    _SERVOSERVICE._serialized_start = 285
    _SERVOSERVICE._serialized_end = 606