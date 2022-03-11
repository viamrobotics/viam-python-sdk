"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$proto/api/component/imu/v1/imu.proto\x12\x1aproto.api.component.imu.v1\x1a\x1cgoogle/api/annotations.proto"\x80\x01\n\x0fAngularVelocity\x12#\n\x0ex_degs_per_sec\x18\x01 \x01(\x01R\x0bxDegsPerSec\x12#\n\x0ey_degs_per_sec\x18\x02 \x01(\x01R\x0byDegsPerSec\x12#\n\x0ez_degs_per_sec\x18\x03 \x01(\x01R\x0bzDegsPerSec"^\n\x0bEulerAngles\x12\x19\n\x08roll_deg\x18\x01 \x01(\x01R\x07rollDeg\x12\x1b\n\tpitch_deg\x18\x02 \x01(\x01R\x08pitchDeg\x12\x17\n\x07yaw_deg\x18\x03 \x01(\x01R\x06yawDeg"\x9b\x01\n\x0cAcceleration\x12-\n\x14x_mm_per_sec_per_sec\x18\x01 \x01(\x01R\x0fxMmPerSecPerSec\x12-\n\x14y_mm_per_sec_per_sec\x18\x02 \x01(\x01R\x0fyMmPerSecPerSec\x12-\n\x14z_mm_per_sec_per_sec\x18\x03 \x01(\x01R\x0fzMmPerSecPerSec"0\n\x1aReadAngularVelocityRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name"u\n\x1bReadAngularVelocityResponse\x12V\n\x10angular_velocity\x18\x01 \x01(\x0b2+.proto.api.component.imu.v1.AngularVelocityR\x0fangularVelocity",\n\x16ReadOrientationRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name"d\n\x17ReadOrientationResponse\x12I\n\x0borientation\x18\x01 \x01(\x0b2\'.proto.api.component.imu.v1.EulerAnglesR\x0borientation"-\n\x17ReadAccelerationRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name"h\n\x18ReadAccelerationResponse\x12L\n\x0cacceleration\x18\x01 \x01(\x0b2(.proto.api.component.imu.v1.AccelerationR\x0cacceleration2\xbd\x04\n\nIMUService\x12\xc2\x01\n\x13ReadAngularVelocity\x126.proto.api.component.imu.v1.ReadAngularVelocityRequest\x1a7.proto.api.component.imu.v1.ReadAngularVelocityResponse":\x82\xd3\xe4\x93\x024\x122/viam/api/v1/component/imu/{name}/angular_velocity\x12\xb1\x01\n\x0fReadOrientation\x122.proto.api.component.imu.v1.ReadOrientationRequest\x1a3.proto.api.component.imu.v1.ReadOrientationResponse"5\x82\xd3\xe4\x93\x02/\x12-/viam/api/v1/component/imu/{name}/orientation\x12\xb5\x01\n\x10ReadAcceleration\x123.proto.api.component.imu.v1.ReadAccelerationRequest\x1a4.proto.api.component.imu.v1.ReadAccelerationResponse"6\x82\xd3\xe4\x93\x020\x12./viam/api/v1/component/imu/{name}/accelerationBU\n\'com.viam.rdk.proto.api.component.imu.v1Z*go.viam.com/rdk/proto/api/component/imu/v1b\x06proto3')
_ANGULARVELOCITY = DESCRIPTOR.message_types_by_name['AngularVelocity']
_EULERANGLES = DESCRIPTOR.message_types_by_name['EulerAngles']
_ACCELERATION = DESCRIPTOR.message_types_by_name['Acceleration']
_READANGULARVELOCITYREQUEST = DESCRIPTOR.message_types_by_name['ReadAngularVelocityRequest']
_READANGULARVELOCITYRESPONSE = DESCRIPTOR.message_types_by_name['ReadAngularVelocityResponse']
_READORIENTATIONREQUEST = DESCRIPTOR.message_types_by_name['ReadOrientationRequest']
_READORIENTATIONRESPONSE = DESCRIPTOR.message_types_by_name['ReadOrientationResponse']
_READACCELERATIONREQUEST = DESCRIPTOR.message_types_by_name['ReadAccelerationRequest']
_READACCELERATIONRESPONSE = DESCRIPTOR.message_types_by_name['ReadAccelerationResponse']
AngularVelocity = _reflection.GeneratedProtocolMessageType('AngularVelocity', (_message.Message,), {'DESCRIPTOR': _ANGULARVELOCITY, '__module__': 'proto.api.component.imu.v1.imu_pb2'})
_sym_db.RegisterMessage(AngularVelocity)
EulerAngles = _reflection.GeneratedProtocolMessageType('EulerAngles', (_message.Message,), {'DESCRIPTOR': _EULERANGLES, '__module__': 'proto.api.component.imu.v1.imu_pb2'})
_sym_db.RegisterMessage(EulerAngles)
Acceleration = _reflection.GeneratedProtocolMessageType('Acceleration', (_message.Message,), {'DESCRIPTOR': _ACCELERATION, '__module__': 'proto.api.component.imu.v1.imu_pb2'})
_sym_db.RegisterMessage(Acceleration)
ReadAngularVelocityRequest = _reflection.GeneratedProtocolMessageType('ReadAngularVelocityRequest', (_message.Message,), {'DESCRIPTOR': _READANGULARVELOCITYREQUEST, '__module__': 'proto.api.component.imu.v1.imu_pb2'})
_sym_db.RegisterMessage(ReadAngularVelocityRequest)
ReadAngularVelocityResponse = _reflection.GeneratedProtocolMessageType('ReadAngularVelocityResponse', (_message.Message,), {'DESCRIPTOR': _READANGULARVELOCITYRESPONSE, '__module__': 'proto.api.component.imu.v1.imu_pb2'})
_sym_db.RegisterMessage(ReadAngularVelocityResponse)
ReadOrientationRequest = _reflection.GeneratedProtocolMessageType('ReadOrientationRequest', (_message.Message,), {'DESCRIPTOR': _READORIENTATIONREQUEST, '__module__': 'proto.api.component.imu.v1.imu_pb2'})
_sym_db.RegisterMessage(ReadOrientationRequest)
ReadOrientationResponse = _reflection.GeneratedProtocolMessageType('ReadOrientationResponse', (_message.Message,), {'DESCRIPTOR': _READORIENTATIONRESPONSE, '__module__': 'proto.api.component.imu.v1.imu_pb2'})
_sym_db.RegisterMessage(ReadOrientationResponse)
ReadAccelerationRequest = _reflection.GeneratedProtocolMessageType('ReadAccelerationRequest', (_message.Message,), {'DESCRIPTOR': _READACCELERATIONREQUEST, '__module__': 'proto.api.component.imu.v1.imu_pb2'})
_sym_db.RegisterMessage(ReadAccelerationRequest)
ReadAccelerationResponse = _reflection.GeneratedProtocolMessageType('ReadAccelerationResponse', (_message.Message,), {'DESCRIPTOR': _READACCELERATIONRESPONSE, '__module__': 'proto.api.component.imu.v1.imu_pb2'})
_sym_db.RegisterMessage(ReadAccelerationResponse)
_IMUSERVICE = DESCRIPTOR.services_by_name['IMUService']
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b"\n'com.viam.rdk.proto.api.component.imu.v1Z*go.viam.com/rdk/proto/api/component/imu/v1"
    _IMUSERVICE.methods_by_name['ReadAngularVelocity']._options = None
    _IMUSERVICE.methods_by_name['ReadAngularVelocity']._serialized_options = b'\x82\xd3\xe4\x93\x024\x122/viam/api/v1/component/imu/{name}/angular_velocity'
    _IMUSERVICE.methods_by_name['ReadOrientation']._options = None
    _IMUSERVICE.methods_by_name['ReadOrientation']._serialized_options = b'\x82\xd3\xe4\x93\x02/\x12-/viam/api/v1/component/imu/{name}/orientation'
    _IMUSERVICE.methods_by_name['ReadAcceleration']._options = None
    _IMUSERVICE.methods_by_name['ReadAcceleration']._serialized_options = b'\x82\xd3\xe4\x93\x020\x12./viam/api/v1/component/imu/{name}/acceleration'
    _ANGULARVELOCITY._serialized_start = 99
    _ANGULARVELOCITY._serialized_end = 227
    _EULERANGLES._serialized_start = 229
    _EULERANGLES._serialized_end = 323
    _ACCELERATION._serialized_start = 326
    _ACCELERATION._serialized_end = 481
    _READANGULARVELOCITYREQUEST._serialized_start = 483
    _READANGULARVELOCITYREQUEST._serialized_end = 531
    _READANGULARVELOCITYRESPONSE._serialized_start = 533
    _READANGULARVELOCITYRESPONSE._serialized_end = 650
    _READORIENTATIONREQUEST._serialized_start = 652
    _READORIENTATIONREQUEST._serialized_end = 696
    _READORIENTATIONRESPONSE._serialized_start = 698
    _READORIENTATIONRESPONSE._serialized_end = 798
    _READACCELERATIONREQUEST._serialized_start = 800
    _READACCELERATIONREQUEST._serialized_end = 845
    _READACCELERATIONRESPONSE._serialized_start = 847
    _READACCELERATIONRESPONSE._serialized_end = 951
    _IMUSERVICE._serialized_start = 954
    _IMUSERVICE._serialized_end = 1527