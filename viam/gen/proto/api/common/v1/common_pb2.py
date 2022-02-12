"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n proto/api/common/v1/common.proto\x12\x13proto.api.common.v1"\x90\x03\n\x0bBoardStatus\x12G\n\x07analogs\x18\x01 \x03(\x0b2-.proto.api.common.v1.BoardStatus.AnalogsEntryR\x07analogs\x12f\n\x12digital_interrupts\x18\x02 \x03(\x0b27.proto.api.common.v1.BoardStatus.DigitalInterruptsEntryR\x11digitalInterrupts\x1a]\n\x0cAnalogsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x127\n\x05value\x18\x02 \x01(\x0b2!.proto.api.common.v1.AnalogStatusR\x05value:\x028\x01\x1aq\n\x16DigitalInterruptsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12A\n\x05value\x18\x02 \x01(\x0b2+.proto.api.common.v1.DigitalInterruptStatusR\x05value:\x028\x01"$\n\x0cAnalogStatus\x12\x14\n\x05value\x18\x01 \x01(\x05R\x05value".\n\x16DigitalInterruptStatus\x12\x14\n\x05value\x18\x01 \x01(\x03R\x05value"y\n\x04Pose\x12\x0c\n\x01x\x18\x01 \x01(\x01R\x01x\x12\x0c\n\x01y\x18\x02 \x01(\x01R\x01y\x12\x0c\n\x01z\x18\x03 \x01(\x01R\x01z\x12\x0f\n\x03o_x\x18\x04 \x01(\x01R\x02oX\x12\x0f\n\x03o_y\x18\x05 \x01(\x01R\x02oY\x12\x0f\n\x03o_z\x18\x06 \x01(\x01R\x02oZ\x12\x14\n\x05theta\x18\x07 \x01(\x01R\x05theta"3\n\x07Vector3\x12\x0c\n\x01x\x18\x01 \x01(\x01R\x01x\x12\x0c\n\x01y\x18\x02 \x01(\x01R\x01y\x12\x0c\n\x01z\x18\x03 \x01(\x01R\x01z"`\n\x0bBoxGeometry\x12\x19\n\x08width_mm\x18\x01 \x01(\x01R\x07widthMm\x12\x1b\n\tlength_mm\x18\x02 \x01(\x01R\x08lengthMm\x12\x19\n\x08depth_mm\x18\x03 \x01(\x01R\x07depthMm"D\n\x08GeoPoint\x12\x1a\n\x08latitude\x18\x01 \x01(\x01R\x08latitude\x12\x1c\n\tlongitude\x18\x02 \x01(\x01R\tlongitudeBG\n com.viam.rdk.proto.api.common.v1Z#go.viam.com/rdk/proto/api/common/v1b\x06proto3')
_BOARDSTATUS = DESCRIPTOR.message_types_by_name['BoardStatus']
_BOARDSTATUS_ANALOGSENTRY = _BOARDSTATUS.nested_types_by_name['AnalogsEntry']
_BOARDSTATUS_DIGITALINTERRUPTSENTRY = _BOARDSTATUS.nested_types_by_name['DigitalInterruptsEntry']
_ANALOGSTATUS = DESCRIPTOR.message_types_by_name['AnalogStatus']
_DIGITALINTERRUPTSTATUS = DESCRIPTOR.message_types_by_name['DigitalInterruptStatus']
_POSE = DESCRIPTOR.message_types_by_name['Pose']
_VECTOR3 = DESCRIPTOR.message_types_by_name['Vector3']
_BOXGEOMETRY = DESCRIPTOR.message_types_by_name['BoxGeometry']
_GEOPOINT = DESCRIPTOR.message_types_by_name['GeoPoint']
BoardStatus = _reflection.GeneratedProtocolMessageType('BoardStatus', (_message.Message,), {'AnalogsEntry': _reflection.GeneratedProtocolMessageType('AnalogsEntry', (_message.Message,), {'DESCRIPTOR': _BOARDSTATUS_ANALOGSENTRY, '__module__': 'proto.api.common.v1.common_pb2'}), 'DigitalInterruptsEntry': _reflection.GeneratedProtocolMessageType('DigitalInterruptsEntry', (_message.Message,), {'DESCRIPTOR': _BOARDSTATUS_DIGITALINTERRUPTSENTRY, '__module__': 'proto.api.common.v1.common_pb2'}), 'DESCRIPTOR': _BOARDSTATUS, '__module__': 'proto.api.common.v1.common_pb2'})
_sym_db.RegisterMessage(BoardStatus)
_sym_db.RegisterMessage(BoardStatus.AnalogsEntry)
_sym_db.RegisterMessage(BoardStatus.DigitalInterruptsEntry)
AnalogStatus = _reflection.GeneratedProtocolMessageType('AnalogStatus', (_message.Message,), {'DESCRIPTOR': _ANALOGSTATUS, '__module__': 'proto.api.common.v1.common_pb2'})
_sym_db.RegisterMessage(AnalogStatus)
DigitalInterruptStatus = _reflection.GeneratedProtocolMessageType('DigitalInterruptStatus', (_message.Message,), {'DESCRIPTOR': _DIGITALINTERRUPTSTATUS, '__module__': 'proto.api.common.v1.common_pb2'})
_sym_db.RegisterMessage(DigitalInterruptStatus)
Pose = _reflection.GeneratedProtocolMessageType('Pose', (_message.Message,), {'DESCRIPTOR': _POSE, '__module__': 'proto.api.common.v1.common_pb2'})
_sym_db.RegisterMessage(Pose)
Vector3 = _reflection.GeneratedProtocolMessageType('Vector3', (_message.Message,), {'DESCRIPTOR': _VECTOR3, '__module__': 'proto.api.common.v1.common_pb2'})
_sym_db.RegisterMessage(Vector3)
BoxGeometry = _reflection.GeneratedProtocolMessageType('BoxGeometry', (_message.Message,), {'DESCRIPTOR': _BOXGEOMETRY, '__module__': 'proto.api.common.v1.common_pb2'})
_sym_db.RegisterMessage(BoxGeometry)
GeoPoint = _reflection.GeneratedProtocolMessageType('GeoPoint', (_message.Message,), {'DESCRIPTOR': _GEOPOINT, '__module__': 'proto.api.common.v1.common_pb2'})
_sym_db.RegisterMessage(GeoPoint)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n com.viam.rdk.proto.api.common.v1Z#go.viam.com/rdk/proto/api/common/v1'
    _BOARDSTATUS_ANALOGSENTRY._options = None
    _BOARDSTATUS_ANALOGSENTRY._serialized_options = b'8\x01'
    _BOARDSTATUS_DIGITALINTERRUPTSENTRY._options = None
    _BOARDSTATUS_DIGITALINTERRUPTSENTRY._serialized_options = b'8\x01'
    _BOARDSTATUS._serialized_start = 58
    _BOARDSTATUS._serialized_end = 458
    _BOARDSTATUS_ANALOGSENTRY._serialized_start = 250
    _BOARDSTATUS_ANALOGSENTRY._serialized_end = 343
    _BOARDSTATUS_DIGITALINTERRUPTSENTRY._serialized_start = 345
    _BOARDSTATUS_DIGITALINTERRUPTSENTRY._serialized_end = 458
    _ANALOGSTATUS._serialized_start = 460
    _ANALOGSTATUS._serialized_end = 496
    _DIGITALINTERRUPTSTATUS._serialized_start = 498
    _DIGITALINTERRUPTSTATUS._serialized_end = 544
    _POSE._serialized_start = 546
    _POSE._serialized_end = 667
    _VECTOR3._serialized_start = 669
    _VECTOR3._serialized_end = 720
    _BOXGEOMETRY._serialized_start = 722
    _BOXGEOMETRY._serialized_end = 818
    _GEOPOINT._serialized_start = 820
    _GEOPOINT._serialized_end = 888