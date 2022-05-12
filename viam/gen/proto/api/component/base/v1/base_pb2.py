"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&proto/api/component/base/v1/base.proto\x12\x1bproto.api.component.base.v1\x1a\x1cgoogle/api/annotations.proto"h\n\x13MoveStraightRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x1f\n\x0bdistance_mm\x18\x02 \x01(\x03R\ndistanceMm\x12\x1c\n\nmm_per_sec\x18\x03 \x01(\x01R\x08mmPerSec"\x16\n\x14MoveStraightResponse"\x80\x01\n\x0eMoveArcRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x1f\n\x0bdistance_mm\x18\x02 \x01(\x03R\ndistanceMm\x12\x1c\n\nmm_per_sec\x18\x03 \x01(\x01R\x08mmPerSec\x12\x1b\n\tangle_deg\x18\x04 \x01(\x01R\x08angleDeg"\x11\n\x0fMoveArcResponse"`\n\x0bSpinRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x1b\n\tangle_deg\x18\x02 \x01(\x01R\x08angleDeg\x12 \n\x0cdegs_per_sec\x18\x03 \x01(\x01R\ndegsPerSec"\x0e\n\x0cSpinResponse"!\n\x0bStopRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name"\x0e\n\x0cStopResponse2\xf7\x04\n\x0bBaseService\x12\xad\x01\n\x0cMoveStraight\x120.proto.api.component.base.v1.MoveStraightRequest\x1a1.proto.api.component.base.v1.MoveStraightResponse"8\x82\xd3\xe4\x93\x022"0/viam/api/v1/component/base/{name}/move_straight\x12\x99\x01\n\x07MoveArc\x12+.proto.api.component.base.v1.MoveArcRequest\x1a,.proto.api.component.base.v1.MoveArcResponse"3\x82\xd3\xe4\x93\x02-"+/viam/api/v1/component/base/{name}/move_arc\x12\x8c\x01\n\x04Spin\x12(.proto.api.component.base.v1.SpinRequest\x1a).proto.api.component.base.v1.SpinResponse"/\x82\xd3\xe4\x93\x02)"\'/viam/api/v1/component/base/{name}/spin\x12\x8c\x01\n\x04Stop\x12(.proto.api.component.base.v1.StopRequest\x1a).proto.api.component.base.v1.StopResponse"/\x82\xd3\xe4\x93\x02)"\'/viam/api/v1/component/base/{name}/stopBW\n(com.viam.rdk.proto.api.component.base.v1Z+go.viam.com/rdk/proto/api/component/base/v1b\x06proto3')
_MOVESTRAIGHTREQUEST = DESCRIPTOR.message_types_by_name['MoveStraightRequest']
_MOVESTRAIGHTRESPONSE = DESCRIPTOR.message_types_by_name['MoveStraightResponse']
_MOVEARCREQUEST = DESCRIPTOR.message_types_by_name['MoveArcRequest']
_MOVEARCRESPONSE = DESCRIPTOR.message_types_by_name['MoveArcResponse']
_SPINREQUEST = DESCRIPTOR.message_types_by_name['SpinRequest']
_SPINRESPONSE = DESCRIPTOR.message_types_by_name['SpinResponse']
_STOPREQUEST = DESCRIPTOR.message_types_by_name['StopRequest']
_STOPRESPONSE = DESCRIPTOR.message_types_by_name['StopResponse']
MoveStraightRequest = _reflection.GeneratedProtocolMessageType('MoveStraightRequest', (_message.Message,), {'DESCRIPTOR': _MOVESTRAIGHTREQUEST, '__module__': 'proto.api.component.base.v1.base_pb2', '__doc__': 'Attributes:\n      name:\n          Name of a base\n      distance_mm:\n          Desired travel distance in millimeters\n      mm_per_sec:\n          Desired travel velocity in millimeters/second\n  '})
_sym_db.RegisterMessage(MoveStraightRequest)
MoveStraightResponse = _reflection.GeneratedProtocolMessageType('MoveStraightResponse', (_message.Message,), {'DESCRIPTOR': _MOVESTRAIGHTRESPONSE, '__module__': 'proto.api.component.base.v1.base_pb2'})
_sym_db.RegisterMessage(MoveStraightResponse)
MoveArcRequest = _reflection.GeneratedProtocolMessageType('MoveArcRequest', (_message.Message,), {'DESCRIPTOR': _MOVEARCREQUEST, '__module__': 'proto.api.component.base.v1.base_pb2', '__doc__': 'Attributes:\n      name:\n          Name of a base\n      distance_mm:\n          Desired travel distance in millimeters\n      mm_per_sec:\n          Desired speed in millimeters per second\n      angle_deg:\n          Desired angle in degrees\n  '})
_sym_db.RegisterMessage(MoveArcRequest)
MoveArcResponse = _reflection.GeneratedProtocolMessageType('MoveArcResponse', (_message.Message,), {'DESCRIPTOR': _MOVEARCRESPONSE, '__module__': 'proto.api.component.base.v1.base_pb2'})
_sym_db.RegisterMessage(MoveArcResponse)
SpinRequest = _reflection.GeneratedProtocolMessageType('SpinRequest', (_message.Message,), {'DESCRIPTOR': _SPINREQUEST, '__module__': 'proto.api.component.base.v1.base_pb2', '__doc__': 'Attributes:\n      name:\n          Name of a base\n      angle_deg:\n          Desired angle\n      degs_per_sec:\n          Desired angular velocity\n  '})
_sym_db.RegisterMessage(SpinRequest)
SpinResponse = _reflection.GeneratedProtocolMessageType('SpinResponse', (_message.Message,), {'DESCRIPTOR': _SPINRESPONSE, '__module__': 'proto.api.component.base.v1.base_pb2'})
_sym_db.RegisterMessage(SpinResponse)
StopRequest = _reflection.GeneratedProtocolMessageType('StopRequest', (_message.Message,), {'DESCRIPTOR': _STOPREQUEST, '__module__': 'proto.api.component.base.v1.base_pb2', '__doc__': 'Attributes:\n      name:\n          Name of a base\n  '})
_sym_db.RegisterMessage(StopRequest)
StopResponse = _reflection.GeneratedProtocolMessageType('StopResponse', (_message.Message,), {'DESCRIPTOR': _STOPRESPONSE, '__module__': 'proto.api.component.base.v1.base_pb2'})
_sym_db.RegisterMessage(StopResponse)
_BASESERVICE = DESCRIPTOR.services_by_name['BaseService']
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n(com.viam.rdk.proto.api.component.base.v1Z+go.viam.com/rdk/proto/api/component/base/v1'
    _BASESERVICE.methods_by_name['MoveStraight']._options = None
    _BASESERVICE.methods_by_name['MoveStraight']._serialized_options = b'\x82\xd3\xe4\x93\x022"0/viam/api/v1/component/base/{name}/move_straight'
    _BASESERVICE.methods_by_name['MoveArc']._options = None
    _BASESERVICE.methods_by_name['MoveArc']._serialized_options = b'\x82\xd3\xe4\x93\x02-"+/viam/api/v1/component/base/{name}/move_arc'
    _BASESERVICE.methods_by_name['Spin']._options = None
    _BASESERVICE.methods_by_name['Spin']._serialized_options = b'\x82\xd3\xe4\x93\x02)"\'/viam/api/v1/component/base/{name}/spin'
    _BASESERVICE.methods_by_name['Stop']._options = None
    _BASESERVICE.methods_by_name['Stop']._serialized_options = b'\x82\xd3\xe4\x93\x02)"\'/viam/api/v1/component/base/{name}/stop'
    _MOVESTRAIGHTREQUEST._serialized_start = 101
    _MOVESTRAIGHTREQUEST._serialized_end = 205
    _MOVESTRAIGHTRESPONSE._serialized_start = 207
    _MOVESTRAIGHTRESPONSE._serialized_end = 229
    _MOVEARCREQUEST._serialized_start = 232
    _MOVEARCREQUEST._serialized_end = 360
    _MOVEARCRESPONSE._serialized_start = 362
    _MOVEARCRESPONSE._serialized_end = 379
    _SPINREQUEST._serialized_start = 381
    _SPINREQUEST._serialized_end = 477
    _SPINRESPONSE._serialized_start = 479
    _SPINRESPONSE._serialized_end = 493
    _STOPREQUEST._serialized_start = 495
    _STOPREQUEST._serialized_end = 528
    _STOPRESPONSE._serialized_start = 530
    _STOPRESPONSE._serialized_end = 544
    _BASESERVICE._serialized_start = 547
    _BASESERVICE._serialized_end = 1178