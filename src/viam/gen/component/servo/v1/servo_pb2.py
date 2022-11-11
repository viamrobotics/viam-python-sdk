"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1ecomponent/servo/v1/servo.proto\x12\x17viam.component.servo.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x1cgoogle/protobuf/struct.proto"m\n\x0bMoveRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x1b\n\tangle_deg\x18\x02 \x01(\rR\x08angleDeg\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"\x0e\n\x0cMoveResponse"W\n\x12GetPositionRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"8\n\x13GetPositionResponse\x12!\n\x0cposition_deg\x18\x01 \x01(\rR\x0bpositionDeg"P\n\x0bStopRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"\x0e\n\x0cStopResponse"H\n\x06Status\x12!\n\x0cposition_deg\x18\x01 \x01(\rR\x0bpositionDeg\x12\x1b\n\tis_moving\x18\x02 \x01(\x08R\x08isMoving2\xbf\x03\n\x0cServoService\x12\x85\x01\n\x04Move\x12$.viam.component.servo.v1.MoveRequest\x1a%.viam.component.servo.v1.MoveResponse"0\x82\xd3\xe4\x93\x02*\x1a(/viam/api/v1/component/servo/{name}/move\x12\x9e\x01\n\x0bGetPosition\x12+.viam.component.servo.v1.GetPositionRequest\x1a,.viam.component.servo.v1.GetPositionResponse"4\x82\xd3\xe4\x93\x02.\x12,/viam/api/v1/component/servo/{name}/position\x12\x85\x01\n\x04Stop\x12$.viam.component.servo.v1.StopRequest\x1a%.viam.component.servo.v1.StopResponse"0\x82\xd3\xe4\x93\x02*"(/viam/api/v1/component/servo/{name}/stopBA\n\x1bcom.viam.component.servo.v1Z"go.viam.com/api/component/servo/v1b\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'component.servo.v1.servo_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n\x1bcom.viam.component.servo.v1Z"go.viam.com/api/component/servo/v1'
    _SERVOSERVICE.methods_by_name['Move']._options = None
    _SERVOSERVICE.methods_by_name['Move']._serialized_options = b'\x82\xd3\xe4\x93\x02*\x1a(/viam/api/v1/component/servo/{name}/move'
    _SERVOSERVICE.methods_by_name['GetPosition']._options = None
    _SERVOSERVICE.methods_by_name['GetPosition']._serialized_options = b'\x82\xd3\xe4\x93\x02.\x12,/viam/api/v1/component/servo/{name}/position'
    _SERVOSERVICE.methods_by_name['Stop']._options = None
    _SERVOSERVICE.methods_by_name['Stop']._serialized_options = b'\x82\xd3\xe4\x93\x02*"(/viam/api/v1/component/servo/{name}/stop'
    _MOVEREQUEST._serialized_start = 119
    _MOVEREQUEST._serialized_end = 228
    _MOVERESPONSE._serialized_start = 230
    _MOVERESPONSE._serialized_end = 244
    _GETPOSITIONREQUEST._serialized_start = 246
    _GETPOSITIONREQUEST._serialized_end = 333
    _GETPOSITIONRESPONSE._serialized_start = 335
    _GETPOSITIONRESPONSE._serialized_end = 391
    _STOPREQUEST._serialized_start = 393
    _STOPREQUEST._serialized_end = 473
    _STOPRESPONSE._serialized_start = 475
    _STOPRESPONSE._serialized_end = 489
    _STATUS._serialized_start = 491
    _STATUS._serialized_end = 563
    _SERVOSERVICE._serialized_start = 566
    _SERVOSERVICE._serialized_end = 1013