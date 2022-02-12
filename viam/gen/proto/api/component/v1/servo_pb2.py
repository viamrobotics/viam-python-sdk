"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n"proto/api/component/v1/servo.proto\x12\x16proto.api.component.v1\x1a\x1cgoogle/api/annotations.proto"J\n\x17ServoServiceMoveRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x1b\n\tangle_deg\x18\x02 \x01(\rR\x08angleDeg"\x1a\n\x18ServoServiceMoveResponse"4\n\x1eServoServiceGetPositionRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name"D\n\x1fServoServiceGetPositionResponse\x12!\n\x0cposition_deg\x18\x01 \x01(\rR\x0bpositionDeg2\xd9\x02\n\x0cServoService\x12\x96\x01\n\x04Move\x12/.proto.api.component.v1.ServoServiceMoveRequest\x1a0.proto.api.component.v1.ServoServiceMoveResponse"+\x82\xd3\xe4\x93\x02%\x1a#/api/v1/component/servo/{name}/move\x12\xaf\x01\n\x0bGetPosition\x126.proto.api.component.v1.ServoServiceGetPositionRequest\x1a7.proto.api.component.v1.ServoServiceGetPositionResponse"/\x82\xd3\xe4\x93\x02)\x12\'/api/v1/component/servo/{name}/positionBM\n#com.viam.rdk.proto.api.component.v1Z&go.viam.com/rdk/proto/api/component/v1b\x06proto3')
_SERVOSERVICEMOVEREQUEST = DESCRIPTOR.message_types_by_name['ServoServiceMoveRequest']
_SERVOSERVICEMOVERESPONSE = DESCRIPTOR.message_types_by_name['ServoServiceMoveResponse']
_SERVOSERVICEGETPOSITIONREQUEST = DESCRIPTOR.message_types_by_name['ServoServiceGetPositionRequest']
_SERVOSERVICEGETPOSITIONRESPONSE = DESCRIPTOR.message_types_by_name['ServoServiceGetPositionResponse']
ServoServiceMoveRequest = _reflection.GeneratedProtocolMessageType('ServoServiceMoveRequest', (_message.Message,), {'DESCRIPTOR': _SERVOSERVICEMOVEREQUEST, '__module__': 'proto.api.component.v1.servo_pb2'})
_sym_db.RegisterMessage(ServoServiceMoveRequest)
ServoServiceMoveResponse = _reflection.GeneratedProtocolMessageType('ServoServiceMoveResponse', (_message.Message,), {'DESCRIPTOR': _SERVOSERVICEMOVERESPONSE, '__module__': 'proto.api.component.v1.servo_pb2'})
_sym_db.RegisterMessage(ServoServiceMoveResponse)
ServoServiceGetPositionRequest = _reflection.GeneratedProtocolMessageType('ServoServiceGetPositionRequest', (_message.Message,), {'DESCRIPTOR': _SERVOSERVICEGETPOSITIONREQUEST, '__module__': 'proto.api.component.v1.servo_pb2'})
_sym_db.RegisterMessage(ServoServiceGetPositionRequest)
ServoServiceGetPositionResponse = _reflection.GeneratedProtocolMessageType('ServoServiceGetPositionResponse', (_message.Message,), {'DESCRIPTOR': _SERVOSERVICEGETPOSITIONRESPONSE, '__module__': 'proto.api.component.v1.servo_pb2'})
_sym_db.RegisterMessage(ServoServiceGetPositionResponse)
_SERVOSERVICE = DESCRIPTOR.services_by_name['ServoService']
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n#com.viam.rdk.proto.api.component.v1Z&go.viam.com/rdk/proto/api/component/v1'
    _SERVOSERVICE.methods_by_name['Move']._options = None
    _SERVOSERVICE.methods_by_name['Move']._serialized_options = b'\x82\xd3\xe4\x93\x02%\x1a#/api/v1/component/servo/{name}/move'
    _SERVOSERVICE.methods_by_name['GetPosition']._options = None
    _SERVOSERVICE.methods_by_name['GetPosition']._serialized_options = b"\x82\xd3\xe4\x93\x02)\x12'/api/v1/component/servo/{name}/position"
    _SERVOSERVICEMOVEREQUEST._serialized_start = 92
    _SERVOSERVICEMOVEREQUEST._serialized_end = 166
    _SERVOSERVICEMOVERESPONSE._serialized_start = 168
    _SERVOSERVICEMOVERESPONSE._serialized_end = 194
    _SERVOSERVICEGETPOSITIONREQUEST._serialized_start = 196
    _SERVOSERVICEGETPOSITIONREQUEST._serialized_end = 248
    _SERVOSERVICEGETPOSITIONRESPONSE._serialized_start = 250
    _SERVOSERVICEGETPOSITIONRESPONSE._serialized_end = 318
    _SERVOSERVICE._serialized_start = 321
    _SERVOSERVICE._serialized_end = 666