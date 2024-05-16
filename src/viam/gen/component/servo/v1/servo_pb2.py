"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....common.v1 import common_pb2 as common_dot_v1_dot_common__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1ecomponent/servo/v1/servo.proto\x12\x17viam.component.servo.v1\x1a\x16common/v1/common.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1cgoogle/protobuf/struct.proto"m\n\x0bMoveRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x1b\n\tangle_deg\x18\x02 \x01(\rR\x08angleDeg\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"\x0e\n\x0cMoveResponse"W\n\x12GetPositionRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"8\n\x13GetPositionResponse\x12!\n\x0cposition_deg\x18\x01 \x01(\rR\x0bpositionDeg"P\n\x0bStopRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"\x0e\n\x0cStopResponse"H\n\x06Status\x12!\n\x0cposition_deg\x18\x01 \x01(\rR\x0bpositionDeg\x12\x1b\n\tis_moving\x18\x02 \x01(\x08R\x08isMoving"%\n\x0fIsMovingRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name"/\n\x10IsMovingResponse\x12\x1b\n\tis_moving\x18\x01 \x01(\x08R\x08isMoving2\xfe\x06\n\x0cServoService\x12\x89\x01\n\x04Move\x12$.viam.component.servo.v1.MoveRequest\x1a%.viam.component.servo.v1.MoveResponse"4\xa0\x92)\x01\x82\xd3\xe4\x93\x02*\x1a(/viam/api/v1/component/servo/{name}/move\x12\x9e\x01\n\x0bGetPosition\x12+.viam.component.servo.v1.GetPositionRequest\x1a,.viam.component.servo.v1.GetPositionResponse"4\x82\xd3\xe4\x93\x02.\x12,/viam/api/v1/component/servo/{name}/position\x12\x85\x01\n\x04Stop\x12$.viam.component.servo.v1.StopRequest\x1a%.viam.component.servo.v1.StopResponse"0\x82\xd3\xe4\x93\x02*"(/viam/api/v1/component/servo/{name}/stop\x12\x96\x01\n\x08IsMoving\x12(.viam.component.servo.v1.IsMovingRequest\x1a).viam.component.servo.v1.IsMovingResponse"5\x82\xd3\xe4\x93\x02/\x12-/viam/api/v1/component/servo/{name}/is_moving\x12\x88\x01\n\tDoCommand\x12 .viam.common.v1.DoCommandRequest\x1a!.viam.common.v1.DoCommandResponse"6\x82\xd3\xe4\x93\x020"./viam/api/v1/component/servo/{name}/do_command\x12\x94\x01\n\rGetGeometries\x12$.viam.common.v1.GetGeometriesRequest\x1a%.viam.common.v1.GetGeometriesResponse"6\x82\xd3\xe4\x93\x020\x12./viam/api/v1/component/servo/{name}/geometriesBA\n\x1bcom.viam.component.servo.v1Z"go.viam.com/api/component/servo/v1b\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'component.servo.v1.servo_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n\x1bcom.viam.component.servo.v1Z"go.viam.com/api/component/servo/v1'
    _SERVOSERVICE.methods_by_name['Move']._options = None
    _SERVOSERVICE.methods_by_name['Move']._serialized_options = b'\xa0\x92)\x01\x82\xd3\xe4\x93\x02*\x1a(/viam/api/v1/component/servo/{name}/move'
    _SERVOSERVICE.methods_by_name['GetPosition']._options = None
    _SERVOSERVICE.methods_by_name['GetPosition']._serialized_options = b'\x82\xd3\xe4\x93\x02.\x12,/viam/api/v1/component/servo/{name}/position'
    _SERVOSERVICE.methods_by_name['Stop']._options = None
    _SERVOSERVICE.methods_by_name['Stop']._serialized_options = b'\x82\xd3\xe4\x93\x02*"(/viam/api/v1/component/servo/{name}/stop'
    _SERVOSERVICE.methods_by_name['IsMoving']._options = None
    _SERVOSERVICE.methods_by_name['IsMoving']._serialized_options = b'\x82\xd3\xe4\x93\x02/\x12-/viam/api/v1/component/servo/{name}/is_moving'
    _SERVOSERVICE.methods_by_name['DoCommand']._options = None
    _SERVOSERVICE.methods_by_name['DoCommand']._serialized_options = b'\x82\xd3\xe4\x93\x020"./viam/api/v1/component/servo/{name}/do_command'
    _SERVOSERVICE.methods_by_name['GetGeometries']._options = None
    _SERVOSERVICE.methods_by_name['GetGeometries']._serialized_options = b'\x82\xd3\xe4\x93\x020\x12./viam/api/v1/component/servo/{name}/geometries'
    _MOVEREQUEST._serialized_start = 143
    _MOVEREQUEST._serialized_end = 252
    _MOVERESPONSE._serialized_start = 254
    _MOVERESPONSE._serialized_end = 268
    _GETPOSITIONREQUEST._serialized_start = 270
    _GETPOSITIONREQUEST._serialized_end = 357
    _GETPOSITIONRESPONSE._serialized_start = 359
    _GETPOSITIONRESPONSE._serialized_end = 415
    _STOPREQUEST._serialized_start = 417
    _STOPREQUEST._serialized_end = 497
    _STOPRESPONSE._serialized_start = 499
    _STOPRESPONSE._serialized_end = 513
    _STATUS._serialized_start = 515
    _STATUS._serialized_end = 587
    _ISMOVINGREQUEST._serialized_start = 589
    _ISMOVINGREQUEST._serialized_end = 626
    _ISMOVINGRESPONSE._serialized_start = 628
    _ISMOVINGRESPONSE._serialized_end = 675
    _SERVOSERVICE._serialized_start = 678
    _SERVOSERVICE._serialized_end = 1572