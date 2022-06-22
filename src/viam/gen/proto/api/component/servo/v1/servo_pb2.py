"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(proto/api/component/servo/v1/servo.proto\x12\x1cproto.api.component.servo.v1\x1a\x1cgoogle/api/annotations.proto">\n\x0bMoveRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x1b\n\tangle_deg\x18\x02 \x01(\rR\x08angleDeg"\x0e\n\x0cMoveResponse"(\n\x12GetPositionRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name"8\n\x13GetPositionResponse\x12!\n\x0cposition_deg\x18\x01 \x01(\rR\x0bpositionDeg"!\n\x0bStopRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name"\x0e\n\x0cStopResponse"H\n\x06Status\x12!\n\x0cposition_deg\x18\x01 \x01(\rR\x0bpositionDeg\x12\x1b\n\tis_moving\x18\x02 \x01(\x08R\x08isMoving2\xdd\x03\n\x0cServoService\x12\x8f\x01\n\x04Move\x12).proto.api.component.servo.v1.MoveRequest\x1a*.proto.api.component.servo.v1.MoveResponse"0\x82\xd3\xe4\x93\x02*\x1a(/viam/api/v1/component/servo/{name}/move\x12\xa8\x01\n\x0bGetPosition\x120.proto.api.component.servo.v1.GetPositionRequest\x1a1.proto.api.component.servo.v1.GetPositionResponse"4\x82\xd3\xe4\x93\x02.\x12,/viam/api/v1/component/servo/{name}/position\x12\x8f\x01\n\x04Stop\x12).proto.api.component.servo.v1.StopRequest\x1a*.proto.api.component.servo.v1.StopResponse"0\x82\xd3\xe4\x93\x02*"(/viam/api/v1/component/servo/{name}/stopBY\n)com.viam.rdk.proto.api.component.servo.v1Z,go.viam.com/rdk/proto/api/component/servo/v1b\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'proto.api.component.servo.v1.servo_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n)com.viam.rdk.proto.api.component.servo.v1Z,go.viam.com/rdk/proto/api/component/servo/v1'
    _SERVOSERVICE.methods_by_name['Move']._options = None
    _SERVOSERVICE.methods_by_name['Move']._serialized_options = b'\x82\xd3\xe4\x93\x02*\x1a(/viam/api/v1/component/servo/{name}/move'
    _SERVOSERVICE.methods_by_name['GetPosition']._options = None
    _SERVOSERVICE.methods_by_name['GetPosition']._serialized_options = b'\x82\xd3\xe4\x93\x02.\x12,/viam/api/v1/component/servo/{name}/position'
    _SERVOSERVICE.methods_by_name['Stop']._options = None
    _SERVOSERVICE.methods_by_name['Stop']._serialized_options = b'\x82\xd3\xe4\x93\x02*"(/viam/api/v1/component/servo/{name}/stop'
    _MOVEREQUEST._serialized_start = 104
    _MOVEREQUEST._serialized_end = 166
    _MOVERESPONSE._serialized_start = 168
    _MOVERESPONSE._serialized_end = 182
    _GETPOSITIONREQUEST._serialized_start = 184
    _GETPOSITIONREQUEST._serialized_end = 224
    _GETPOSITIONRESPONSE._serialized_start = 226
    _GETPOSITIONRESPONSE._serialized_end = 282
    _STOPREQUEST._serialized_start = 284
    _STOPREQUEST._serialized_end = 317
    _STOPRESPONSE._serialized_start = 319
    _STOPRESPONSE._serialized_end = 333
    _STATUS._serialized_start = 335
    _STATUS._serialized_end = 407
    _SERVOSERVICE._serialized_start = 410
    _SERVOSERVICE._serialized_end = 887