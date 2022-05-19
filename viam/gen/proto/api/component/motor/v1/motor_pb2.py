"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(proto/api/component/motor/v1/motor.proto\x12\x1cproto.api.component.motor.v1\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1cgoogle/api/annotations.proto"B\n\x0fSetPowerRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x1b\n\tpower_pct\x18\x02 \x01(\x01R\x08powerPct"\x12\n\x10SetPowerResponse"V\n\x0cGoForRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x10\n\x03rpm\x18\x02 \x01(\x01R\x03rpm\x12 \n\x0brevolutions\x18\x03 \x01(\x01R\x0brevolutions"\x0f\n\rGoForResponse"f\n\x0bGoToRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x10\n\x03rpm\x18\x02 \x01(\x01R\x03rpm\x121\n\x14position_revolutions\x18\x03 \x01(\x01R\x13positionRevolutions"\x0e\n\x0cGoToResponse"F\n\x18ResetZeroPositionRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x16\n\x06offset\x18\x02 \x01(\x01R\x06offset"\x1b\n\x19ResetZeroPositionResponse"(\n\x12GetPositionRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name"1\n\x13GetPositionResponse\x12\x1a\n\x08position\x18\x01 \x01(\x01R\x08position"!\n\x0bStopRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name"\x0e\n\x0cStopResponse"&\n\x10IsPoweredRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name"(\n\x11IsPoweredResponse\x12\x13\n\x05is_on\x18\x01 \x01(\x08R\x04isOn"(\n\x12GetFeaturesRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name"D\n\x13GetFeaturesResponse\x12-\n\x12position_reporting\x18\x01 \x01(\x08R\x11positionReporting"h\n\x06Status\x12\x13\n\x05is_on\x18\x01 \x01(\x08R\x04isOn\x12-\n\x12position_reporting\x18\x02 \x01(\x08R\x11positionReporting\x12\x1a\n\x08position\x18\x03 \x01(\x01R\x08position2\x9c\n\n\x0cMotorService\x12\x9c\x01\n\x08SetPower\x12-.proto.api.component.motor.v1.SetPowerRequest\x1a..proto.api.component.motor.v1.SetPowerResponse"1\x82\xd3\xe4\x93\x02+\x1a)/viam/api/v1/component/motor/{name}/power\x12\x94\x01\n\x05GoFor\x12*.proto.api.component.motor.v1.GoForRequest\x1a+.proto.api.component.motor.v1.GoForResponse"2\x82\xd3\xe4\x93\x02,\x1a*/viam/api/v1/component/motor/{name}/go_for\x12\x90\x01\n\x04GoTo\x12).proto.api.component.motor.v1.GoToRequest\x1a*.proto.api.component.motor.v1.GoToResponse"1\x82\xd3\xe4\x93\x02+\x1a)/viam/api/v1/component/motor/{name}/go_to\x12\xb6\x01\n\x11ResetZeroPosition\x126.proto.api.component.motor.v1.ResetZeroPositionRequest\x1a7.proto.api.component.motor.v1.ResetZeroPositionResponse"0\x82\xd3\xe4\x93\x02*\x1a(/viam/api/v1/component/motor/{name}/zero\x12\xa8\x01\n\x0bGetPosition\x120.proto.api.component.motor.v1.GetPositionRequest\x1a1.proto.api.component.motor.v1.GetPositionResponse"4\x82\xd3\xe4\x93\x02.\x12,/viam/api/v1/component/motor/{name}/position\x12\xa8\x01\n\x0bGetFeatures\x120.proto.api.component.motor.v1.GetFeaturesRequest\x1a1.proto.api.component.motor.v1.GetFeaturesResponse"4\x82\xd3\xe4\x93\x02.\x12,/viam/api/v1/component/motor/{name}/features\x12\x8f\x01\n\x04Stop\x12).proto.api.component.motor.v1.StopRequest\x1a*.proto.api.component.motor.v1.StopResponse"0\x82\xd3\xe4\x93\x02*\x1a(/viam/api/v1/component/motor/{name}/stop\x12\xa1\x01\n\tIsPowered\x12..proto.api.component.motor.v1.IsPoweredRequest\x1a/.proto.api.component.motor.v1.IsPoweredResponse"3\x82\xd3\xe4\x93\x02-\x12+/viam/api/v1/component/motor/{name}/poweredBY\n)com.viam.rdk.proto.api.component.motor.v1Z,go.viam.com/rdk/proto/api/component/motor/v1b\x06proto3')
_SETPOWERREQUEST = DESCRIPTOR.message_types_by_name['SetPowerRequest']
_SETPOWERRESPONSE = DESCRIPTOR.message_types_by_name['SetPowerResponse']
_GOFORREQUEST = DESCRIPTOR.message_types_by_name['GoForRequest']
_GOFORRESPONSE = DESCRIPTOR.message_types_by_name['GoForResponse']
_GOTOREQUEST = DESCRIPTOR.message_types_by_name['GoToRequest']
_GOTORESPONSE = DESCRIPTOR.message_types_by_name['GoToResponse']
_RESETZEROPOSITIONREQUEST = DESCRIPTOR.message_types_by_name['ResetZeroPositionRequest']
_RESETZEROPOSITIONRESPONSE = DESCRIPTOR.message_types_by_name['ResetZeroPositionResponse']
_GETPOSITIONREQUEST = DESCRIPTOR.message_types_by_name['GetPositionRequest']
_GETPOSITIONRESPONSE = DESCRIPTOR.message_types_by_name['GetPositionResponse']
_STOPREQUEST = DESCRIPTOR.message_types_by_name['StopRequest']
_STOPRESPONSE = DESCRIPTOR.message_types_by_name['StopResponse']
_ISPOWEREDREQUEST = DESCRIPTOR.message_types_by_name['IsPoweredRequest']
_ISPOWEREDRESPONSE = DESCRIPTOR.message_types_by_name['IsPoweredResponse']
_GETFEATURESREQUEST = DESCRIPTOR.message_types_by_name['GetFeaturesRequest']
_GETFEATURESRESPONSE = DESCRIPTOR.message_types_by_name['GetFeaturesResponse']
_STATUS = DESCRIPTOR.message_types_by_name['Status']
SetPowerRequest = _reflection.GeneratedProtocolMessageType('SetPowerRequest', (_message.Message,), {'DESCRIPTOR': _SETPOWERREQUEST, '__module__': 'proto.api.component.motor.v1.motor_pb2', '__doc__': 'Attributes:\n      name:\n          Name of a motor\n      power_pct:\n          Percentage of motor’s power, between -1 and 1\n  '})
_sym_db.RegisterMessage(SetPowerRequest)
SetPowerResponse = _reflection.GeneratedProtocolMessageType('SetPowerResponse', (_message.Message,), {'DESCRIPTOR': _SETPOWERRESPONSE, '__module__': 'proto.api.component.motor.v1.motor_pb2'})
_sym_db.RegisterMessage(SetPowerResponse)
GoForRequest = _reflection.GeneratedProtocolMessageType('GoForRequest', (_message.Message,), {'DESCRIPTOR': _GOFORREQUEST, '__module__': 'proto.api.component.motor.v1.motor_pb2', '__doc__': 'Attributes:\n      name:\n          Name of a motor\n      rpm:\n          Speed of motor travel in rotations per minute\n      revolutions:\n          Number of revolutions relative to motor’s start position\n  '})
_sym_db.RegisterMessage(GoForRequest)
GoForResponse = _reflection.GeneratedProtocolMessageType('GoForResponse', (_message.Message,), {'DESCRIPTOR': _GOFORRESPONSE, '__module__': 'proto.api.component.motor.v1.motor_pb2'})
_sym_db.RegisterMessage(GoForResponse)
GoToRequest = _reflection.GeneratedProtocolMessageType('GoToRequest', (_message.Message,), {'DESCRIPTOR': _GOTOREQUEST, '__module__': 'proto.api.component.motor.v1.motor_pb2', '__doc__': 'Attributes:\n      name:\n          Name of a motor\n      rpm:\n          Speed of motor travel in rotations per minute\n      position_revolutions:\n          Number of revolutions relative to motor’s home home/zero\n  '})
_sym_db.RegisterMessage(GoToRequest)
GoToResponse = _reflection.GeneratedProtocolMessageType('GoToResponse', (_message.Message,), {'DESCRIPTOR': _GOTORESPONSE, '__module__': 'proto.api.component.motor.v1.motor_pb2'})
_sym_db.RegisterMessage(GoToResponse)
ResetZeroPositionRequest = _reflection.GeneratedProtocolMessageType('ResetZeroPositionRequest', (_message.Message,), {'DESCRIPTOR': _RESETZEROPOSITIONREQUEST, '__module__': 'proto.api.component.motor.v1.motor_pb2', '__doc__': 'Attributes:\n      name:\n          Name of a motor\n      offset:\n          Motor position\n  '})
_sym_db.RegisterMessage(ResetZeroPositionRequest)
ResetZeroPositionResponse = _reflection.GeneratedProtocolMessageType('ResetZeroPositionResponse', (_message.Message,), {'DESCRIPTOR': _RESETZEROPOSITIONRESPONSE, '__module__': 'proto.api.component.motor.v1.motor_pb2'})
_sym_db.RegisterMessage(ResetZeroPositionResponse)
GetPositionRequest = _reflection.GeneratedProtocolMessageType('GetPositionRequest', (_message.Message,), {'DESCRIPTOR': _GETPOSITIONREQUEST, '__module__': 'proto.api.component.motor.v1.motor_pb2', '__doc__': 'Attributes:\n      name:\n          Name of a motor\n  '})
_sym_db.RegisterMessage(GetPositionRequest)
GetPositionResponse = _reflection.GeneratedProtocolMessageType('GetPositionResponse', (_message.Message,), {'DESCRIPTOR': _GETPOSITIONRESPONSE, '__module__': 'proto.api.component.motor.v1.motor_pb2', '__doc__': 'Attributes:\n      position:\n          Current position of the motor relative to its home\n  '})
_sym_db.RegisterMessage(GetPositionResponse)
StopRequest = _reflection.GeneratedProtocolMessageType('StopRequest', (_message.Message,), {'DESCRIPTOR': _STOPREQUEST, '__module__': 'proto.api.component.motor.v1.motor_pb2', '__doc__': 'Attributes:\n      name:\n          Name of a motor\n  '})
_sym_db.RegisterMessage(StopRequest)
StopResponse = _reflection.GeneratedProtocolMessageType('StopResponse', (_message.Message,), {'DESCRIPTOR': _STOPRESPONSE, '__module__': 'proto.api.component.motor.v1.motor_pb2'})
_sym_db.RegisterMessage(StopResponse)
IsPoweredRequest = _reflection.GeneratedProtocolMessageType('IsPoweredRequest', (_message.Message,), {'DESCRIPTOR': _ISPOWEREDREQUEST, '__module__': 'proto.api.component.motor.v1.motor_pb2', '__doc__': 'Attributes:\n      name:\n          Name of a motor\n  '})
_sym_db.RegisterMessage(IsPoweredRequest)
IsPoweredResponse = _reflection.GeneratedProtocolMessageType('IsPoweredResponse', (_message.Message,), {'DESCRIPTOR': _ISPOWEREDRESPONSE, '__module__': 'proto.api.component.motor.v1.motor_pb2', '__doc__': 'Attributes:\n      is_on:\n          Returns true if the motor is on\n  '})
_sym_db.RegisterMessage(IsPoweredResponse)
GetFeaturesRequest = _reflection.GeneratedProtocolMessageType('GetFeaturesRequest', (_message.Message,), {'DESCRIPTOR': _GETFEATURESREQUEST, '__module__': 'proto.api.component.motor.v1.motor_pb2', '__doc__': 'Attributes:\n      name:\n          Name of a motor\n  '})
_sym_db.RegisterMessage(GetFeaturesRequest)
GetFeaturesResponse = _reflection.GeneratedProtocolMessageType('GetFeaturesResponse', (_message.Message,), {'DESCRIPTOR': _GETFEATURESRESPONSE, '__module__': 'proto.api.component.motor.v1.motor_pb2', '__doc__': 'Attributes:\n      position_reporting:\n          Returns true if the motor supports reporting its position\n  '})
_sym_db.RegisterMessage(GetFeaturesResponse)
Status = _reflection.GeneratedProtocolMessageType('Status', (_message.Message,), {'DESCRIPTOR': _STATUS, '__module__': 'proto.api.component.motor.v1.motor_pb2', '__doc__': 'Attributes:\n      is_on:\n          To D0 (FA): Delete this field\n      position_reporting:\n          Returns true if the motor has position support\n      position:\n          Returns current position of the motor relative to its home\n  '})
_sym_db.RegisterMessage(Status)
_MOTORSERVICE = DESCRIPTOR.services_by_name['MotorService']
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n)com.viam.rdk.proto.api.component.motor.v1Z,go.viam.com/rdk/proto/api/component/motor/v1'
    _MOTORSERVICE.methods_by_name['SetPower']._options = None
    _MOTORSERVICE.methods_by_name['SetPower']._serialized_options = b'\x82\xd3\xe4\x93\x02+\x1a)/viam/api/v1/component/motor/{name}/power'
    _MOTORSERVICE.methods_by_name['GoFor']._options = None
    _MOTORSERVICE.methods_by_name['GoFor']._serialized_options = b'\x82\xd3\xe4\x93\x02,\x1a*/viam/api/v1/component/motor/{name}/go_for'
    _MOTORSERVICE.methods_by_name['GoTo']._options = None
    _MOTORSERVICE.methods_by_name['GoTo']._serialized_options = b'\x82\xd3\xe4\x93\x02+\x1a)/viam/api/v1/component/motor/{name}/go_to'
    _MOTORSERVICE.methods_by_name['ResetZeroPosition']._options = None
    _MOTORSERVICE.methods_by_name['ResetZeroPosition']._serialized_options = b'\x82\xd3\xe4\x93\x02*\x1a(/viam/api/v1/component/motor/{name}/zero'
    _MOTORSERVICE.methods_by_name['GetPosition']._options = None
    _MOTORSERVICE.methods_by_name['GetPosition']._serialized_options = b'\x82\xd3\xe4\x93\x02.\x12,/viam/api/v1/component/motor/{name}/position'
    _MOTORSERVICE.methods_by_name['GetFeatures']._options = None
    _MOTORSERVICE.methods_by_name['GetFeatures']._serialized_options = b'\x82\xd3\xe4\x93\x02.\x12,/viam/api/v1/component/motor/{name}/features'
    _MOTORSERVICE.methods_by_name['Stop']._options = None
    _MOTORSERVICE.methods_by_name['Stop']._serialized_options = b'\x82\xd3\xe4\x93\x02*\x1a(/viam/api/v1/component/motor/{name}/stop'
    _MOTORSERVICE.methods_by_name['IsPowered']._options = None
    _MOTORSERVICE.methods_by_name['IsPowered']._serialized_options = b'\x82\xd3\xe4\x93\x02-\x12+/viam/api/v1/component/motor/{name}/powered'
    _SETPOWERREQUEST._serialized_start = 134
    _SETPOWERREQUEST._serialized_end = 200
    _SETPOWERRESPONSE._serialized_start = 202
    _SETPOWERRESPONSE._serialized_end = 220
    _GOFORREQUEST._serialized_start = 222
    _GOFORREQUEST._serialized_end = 308
    _GOFORRESPONSE._serialized_start = 310
    _GOFORRESPONSE._serialized_end = 325
    _GOTOREQUEST._serialized_start = 327
    _GOTOREQUEST._serialized_end = 429
    _GOTORESPONSE._serialized_start = 431
    _GOTORESPONSE._serialized_end = 445
    _RESETZEROPOSITIONREQUEST._serialized_start = 447
    _RESETZEROPOSITIONREQUEST._serialized_end = 517
    _RESETZEROPOSITIONRESPONSE._serialized_start = 519
    _RESETZEROPOSITIONRESPONSE._serialized_end = 546
    _GETPOSITIONREQUEST._serialized_start = 548
    _GETPOSITIONREQUEST._serialized_end = 588
    _GETPOSITIONRESPONSE._serialized_start = 590
    _GETPOSITIONRESPONSE._serialized_end = 639
    _STOPREQUEST._serialized_start = 641
    _STOPREQUEST._serialized_end = 674
    _STOPRESPONSE._serialized_start = 676
    _STOPRESPONSE._serialized_end = 690
    _ISPOWEREDREQUEST._serialized_start = 692
    _ISPOWEREDREQUEST._serialized_end = 730
    _ISPOWEREDRESPONSE._serialized_start = 732
    _ISPOWEREDRESPONSE._serialized_end = 772
    _GETFEATURESREQUEST._serialized_start = 774
    _GETFEATURESREQUEST._serialized_end = 814
    _GETFEATURESRESPONSE._serialized_start = 816
    _GETFEATURESRESPONSE._serialized_end = 884
    _STATUS._serialized_start = 886
    _STATUS._serialized_end = 990
    _MOTORSERVICE._serialized_start = 993
    _MOTORSERVICE._serialized_end = 2301