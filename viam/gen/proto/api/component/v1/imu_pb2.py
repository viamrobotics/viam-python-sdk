"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n proto/api/component/v1/imu.proto\x12\x16proto.api.component.v1\x1a\x1cgoogle/api/annotations.proto"\x80\x01\n\x0fAngularVelocity\x12#\n\x0ex_degs_per_sec\x18\x01 \x01(\x01R\x0bxDegsPerSec\x12#\n\x0ey_degs_per_sec\x18\x02 \x01(\x01R\x0byDegsPerSec\x12#\n\x0ez_degs_per_sec\x18\x03 \x01(\x01R\x0bzDegsPerSec"^\n\x0bEulerAngles\x12\x19\n\x08roll_deg\x18\x01 \x01(\x01R\x07rollDeg\x12\x1b\n\tpitch_deg\x18\x02 \x01(\x01R\x08pitchDeg\x12\x17\n\x07yaw_deg\x18\x03 \x01(\x01R\x06yawDeg"\x9b\x01\n\x0cAcceleration\x12-\n\x14x_mm_per_sec_per_sec\x18\x01 \x01(\x01R\x0fxMmPerSecPerSec\x12-\n\x14y_mm_per_sec_per_sec\x18\x02 \x01(\x01R\x0fyMmPerSecPerSec\x12-\n\x14z_mm_per_sec_per_sec\x18\x03 \x01(\x01R\x0fzMmPerSecPerSec":\n$IMUServiceReadAngularVelocityRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name"{\n%IMUServiceReadAngularVelocityResponse\x12R\n\x10angular_velocity\x18\x01 \x01(\x0b2\'.proto.api.component.v1.AngularVelocityR\x0fangularVelocity"6\n IMUServiceReadOrientationRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name"j\n!IMUServiceReadOrientationResponse\x12E\n\x0borientation\x18\x01 \x01(\x0b2#.proto.api.component.v1.EulerAnglesR\x0borientation"7\n!IMUServiceReadAccelerationRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name"n\n"IMUServiceReadAccelerationResponse\x12H\n\x0cacceleration\x18\x01 \x01(\x0b2$.proto.api.component.v1.AccelerationR\x0cacceleration2\xd2\x04\n\nIMUService\x12\xc9\x01\n\x13ReadAngularVelocity\x12<.proto.api.component.v1.IMUServiceReadAngularVelocityRequest\x1a=.proto.api.component.v1.IMUServiceReadAngularVelocityResponse"5\x82\xd3\xe4\x93\x02/\x12-/api/v1/component/imu/{name}/angular_velocity\x12\xb8\x01\n\x0fReadOrientation\x128.proto.api.component.v1.IMUServiceReadOrientationRequest\x1a9.proto.api.component.v1.IMUServiceReadOrientationResponse"0\x82\xd3\xe4\x93\x02*\x12(/api/v1/component/imu/{name}/orientation\x12\xbc\x01\n\x10ReadAcceleration\x129.proto.api.component.v1.IMUServiceReadAccelerationRequest\x1a:.proto.api.component.v1.IMUServiceReadAccelerationResponse"1\x82\xd3\xe4\x93\x02+\x12)/api/v1/component/imu/{name}/accelerationBM\n#com.viam.rdk.proto.api.component.v1Z&go.viam.com/rdk/proto/api/component/v1b\x06proto3')
_ANGULARVELOCITY = DESCRIPTOR.message_types_by_name['AngularVelocity']
_EULERANGLES = DESCRIPTOR.message_types_by_name['EulerAngles']
_ACCELERATION = DESCRIPTOR.message_types_by_name['Acceleration']
_IMUSERVICEREADANGULARVELOCITYREQUEST = DESCRIPTOR.message_types_by_name['IMUServiceReadAngularVelocityRequest']
_IMUSERVICEREADANGULARVELOCITYRESPONSE = DESCRIPTOR.message_types_by_name['IMUServiceReadAngularVelocityResponse']
_IMUSERVICEREADORIENTATIONREQUEST = DESCRIPTOR.message_types_by_name['IMUServiceReadOrientationRequest']
_IMUSERVICEREADORIENTATIONRESPONSE = DESCRIPTOR.message_types_by_name['IMUServiceReadOrientationResponse']
_IMUSERVICEREADACCELERATIONREQUEST = DESCRIPTOR.message_types_by_name['IMUServiceReadAccelerationRequest']
_IMUSERVICEREADACCELERATIONRESPONSE = DESCRIPTOR.message_types_by_name['IMUServiceReadAccelerationResponse']
AngularVelocity = _reflection.GeneratedProtocolMessageType('AngularVelocity', (_message.Message,), {'DESCRIPTOR': _ANGULARVELOCITY, '__module__': 'proto.api.component.v1.imu_pb2'})
_sym_db.RegisterMessage(AngularVelocity)
EulerAngles = _reflection.GeneratedProtocolMessageType('EulerAngles', (_message.Message,), {'DESCRIPTOR': _EULERANGLES, '__module__': 'proto.api.component.v1.imu_pb2'})
_sym_db.RegisterMessage(EulerAngles)
Acceleration = _reflection.GeneratedProtocolMessageType('Acceleration', (_message.Message,), {'DESCRIPTOR': _ACCELERATION, '__module__': 'proto.api.component.v1.imu_pb2'})
_sym_db.RegisterMessage(Acceleration)
IMUServiceReadAngularVelocityRequest = _reflection.GeneratedProtocolMessageType('IMUServiceReadAngularVelocityRequest', (_message.Message,), {'DESCRIPTOR': _IMUSERVICEREADANGULARVELOCITYREQUEST, '__module__': 'proto.api.component.v1.imu_pb2'})
_sym_db.RegisterMessage(IMUServiceReadAngularVelocityRequest)
IMUServiceReadAngularVelocityResponse = _reflection.GeneratedProtocolMessageType('IMUServiceReadAngularVelocityResponse', (_message.Message,), {'DESCRIPTOR': _IMUSERVICEREADANGULARVELOCITYRESPONSE, '__module__': 'proto.api.component.v1.imu_pb2'})
_sym_db.RegisterMessage(IMUServiceReadAngularVelocityResponse)
IMUServiceReadOrientationRequest = _reflection.GeneratedProtocolMessageType('IMUServiceReadOrientationRequest', (_message.Message,), {'DESCRIPTOR': _IMUSERVICEREADORIENTATIONREQUEST, '__module__': 'proto.api.component.v1.imu_pb2'})
_sym_db.RegisterMessage(IMUServiceReadOrientationRequest)
IMUServiceReadOrientationResponse = _reflection.GeneratedProtocolMessageType('IMUServiceReadOrientationResponse', (_message.Message,), {'DESCRIPTOR': _IMUSERVICEREADORIENTATIONRESPONSE, '__module__': 'proto.api.component.v1.imu_pb2'})
_sym_db.RegisterMessage(IMUServiceReadOrientationResponse)
IMUServiceReadAccelerationRequest = _reflection.GeneratedProtocolMessageType('IMUServiceReadAccelerationRequest', (_message.Message,), {'DESCRIPTOR': _IMUSERVICEREADACCELERATIONREQUEST, '__module__': 'proto.api.component.v1.imu_pb2'})
_sym_db.RegisterMessage(IMUServiceReadAccelerationRequest)
IMUServiceReadAccelerationResponse = _reflection.GeneratedProtocolMessageType('IMUServiceReadAccelerationResponse', (_message.Message,), {'DESCRIPTOR': _IMUSERVICEREADACCELERATIONRESPONSE, '__module__': 'proto.api.component.v1.imu_pb2'})
_sym_db.RegisterMessage(IMUServiceReadAccelerationResponse)
_IMUSERVICE = DESCRIPTOR.services_by_name['IMUService']
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n#com.viam.rdk.proto.api.component.v1Z&go.viam.com/rdk/proto/api/component/v1'
    _IMUSERVICE.methods_by_name['ReadAngularVelocity']._options = None
    _IMUSERVICE.methods_by_name['ReadAngularVelocity']._serialized_options = b'\x82\xd3\xe4\x93\x02/\x12-/api/v1/component/imu/{name}/angular_velocity'
    _IMUSERVICE.methods_by_name['ReadOrientation']._options = None
    _IMUSERVICE.methods_by_name['ReadOrientation']._serialized_options = b'\x82\xd3\xe4\x93\x02*\x12(/api/v1/component/imu/{name}/orientation'
    _IMUSERVICE.methods_by_name['ReadAcceleration']._options = None
    _IMUSERVICE.methods_by_name['ReadAcceleration']._serialized_options = b'\x82\xd3\xe4\x93\x02+\x12)/api/v1/component/imu/{name}/acceleration'
    _ANGULARVELOCITY._serialized_start = 91
    _ANGULARVELOCITY._serialized_end = 219
    _EULERANGLES._serialized_start = 221
    _EULERANGLES._serialized_end = 315
    _ACCELERATION._serialized_start = 318
    _ACCELERATION._serialized_end = 473
    _IMUSERVICEREADANGULARVELOCITYREQUEST._serialized_start = 475
    _IMUSERVICEREADANGULARVELOCITYREQUEST._serialized_end = 533
    _IMUSERVICEREADANGULARVELOCITYRESPONSE._serialized_start = 535
    _IMUSERVICEREADANGULARVELOCITYRESPONSE._serialized_end = 658
    _IMUSERVICEREADORIENTATIONREQUEST._serialized_start = 660
    _IMUSERVICEREADORIENTATIONREQUEST._serialized_end = 714
    _IMUSERVICEREADORIENTATIONRESPONSE._serialized_start = 716
    _IMUSERVICEREADORIENTATIONRESPONSE._serialized_end = 822
    _IMUSERVICEREADACCELERATIONREQUEST._serialized_start = 824
    _IMUSERVICEREADACCELERATIONREQUEST._serialized_end = 879
    _IMUSERVICEREADACCELERATIONRESPONSE._serialized_start = 881
    _IMUSERVICEREADACCELERATIONRESPONSE._serialized_end = 991
    _IMUSERVICE._serialized_start = 994
    _IMUSERVICE._serialized_end = 1588