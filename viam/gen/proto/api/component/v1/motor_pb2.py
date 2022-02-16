"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n"proto/api/component/v1/motor.proto\x12\x16proto.api.component.v1\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1cgoogle/api/annotations.proto"N\n\x1bMotorServiceSetPowerRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x1b\n\tpower_pct\x18\x02 \x01(\x01R\x08powerPct"\x1e\n\x1cMotorServiceSetPowerResponse"b\n\x18MotorServiceGoForRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x10\n\x03rpm\x18\x02 \x01(\x01R\x03rpm\x12 \n\x0brevolutions\x18\x03 \x01(\x01R\x0brevolutions"\x1b\n\x19MotorServiceGoForResponse"r\n\x17MotorServiceGoToRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x10\n\x03rpm\x18\x02 \x01(\x01R\x03rpm\x121\n\x14position_revolutions\x18\x03 \x01(\x01R\x13positionRevolutions"\x1a\n\x18MotorServiceGoToResponse"R\n$MotorServiceResetZeroPositionRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x16\n\x06offset\x18\x02 \x01(\x01R\x06offset"\'\n%MotorServiceResetZeroPositionResponse"4\n\x1eMotorServiceGetPositionRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name"=\n\x1fMotorServiceGetPositionResponse\x12\x1a\n\x08position\x18\x01 \x01(\x01R\x08position"-\n\x17MotorServiceStopRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name"\x1a\n\x18MotorServiceStopResponse"2\n\x1cMotorServiceIsPoweredRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name"4\n\x1dMotorServiceIsPoweredResponse\x12\x13\n\x05is_on\x18\x01 \x01(\x08R\x04isOn"4\n\x1eMotorServiceGetFeaturesRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name"P\n\x1fMotorServiceGetFeaturesResponse\x12-\n\x12position_reporting\x18\x01 \x01(\x08R\x11positionReporting2\xd4\n\n\x0cMotorService\x12\xa3\x01\n\x08SetPower\x123.proto.api.component.v1.MotorServiceSetPowerRequest\x1a4.proto.api.component.v1.MotorServiceSetPowerResponse",\x82\xd3\xe4\x93\x02&\x1a$/api/v1/component/motor/{name}/power\x12\x9b\x01\n\x05GoFor\x120.proto.api.component.v1.MotorServiceGoForRequest\x1a1.proto.api.component.v1.MotorServiceGoForResponse"-\x82\xd3\xe4\x93\x02\'\x1a%/api/v1/component/motor/{name}/go_for\x12\x97\x01\n\x04GoTo\x12/.proto.api.component.v1.MotorServiceGoToRequest\x1a0.proto.api.component.v1.MotorServiceGoToResponse",\x82\xd3\xe4\x93\x02&\x1a$/api/v1/component/motor/{name}/go_to\x12\xbd\x01\n\x11ResetZeroPosition\x12<.proto.api.component.v1.MotorServiceResetZeroPositionRequest\x1a=.proto.api.component.v1.MotorServiceResetZeroPositionResponse"+\x82\xd3\xe4\x93\x02%\x1a#/api/v1/component/motor/{name}/zero\x12\xaf\x01\n\x0bGetPosition\x126.proto.api.component.v1.MotorServiceGetPositionRequest\x1a7.proto.api.component.v1.MotorServiceGetPositionResponse"/\x82\xd3\xe4\x93\x02)\x12\'/api/v1/component/motor/{name}/position\x12\xaf\x01\n\x0bGetFeatures\x126.proto.api.component.v1.MotorServiceGetFeaturesRequest\x1a7.proto.api.component.v1.MotorServiceGetFeaturesResponse"/\x82\xd3\xe4\x93\x02)\x12\'/api/v1/component/motor/{name}/features\x12\x96\x01\n\x04Stop\x12/.proto.api.component.v1.MotorServiceStopRequest\x1a0.proto.api.component.v1.MotorServiceStopResponse"+\x82\xd3\xe4\x93\x02%\x1a#/api/v1/component/motor/{name}/stop\x12\xa8\x01\n\tIsPowered\x124.proto.api.component.v1.MotorServiceIsPoweredRequest\x1a5.proto.api.component.v1.MotorServiceIsPoweredResponse".\x82\xd3\xe4\x93\x02(\x12&/api/v1/component/motor/{name}/poweredBM\n#com.viam.rdk.proto.api.component.v1Z&go.viam.com/rdk/proto/api/component/v1b\x06proto3')
_MOTORSERVICESETPOWERREQUEST = DESCRIPTOR.message_types_by_name['MotorServiceSetPowerRequest']
_MOTORSERVICESETPOWERRESPONSE = DESCRIPTOR.message_types_by_name['MotorServiceSetPowerResponse']
_MOTORSERVICEGOFORREQUEST = DESCRIPTOR.message_types_by_name['MotorServiceGoForRequest']
_MOTORSERVICEGOFORRESPONSE = DESCRIPTOR.message_types_by_name['MotorServiceGoForResponse']
_MOTORSERVICEGOTOREQUEST = DESCRIPTOR.message_types_by_name['MotorServiceGoToRequest']
_MOTORSERVICEGOTORESPONSE = DESCRIPTOR.message_types_by_name['MotorServiceGoToResponse']
_MOTORSERVICERESETZEROPOSITIONREQUEST = DESCRIPTOR.message_types_by_name['MotorServiceResetZeroPositionRequest']
_MOTORSERVICERESETZEROPOSITIONRESPONSE = DESCRIPTOR.message_types_by_name['MotorServiceResetZeroPositionResponse']
_MOTORSERVICEGETPOSITIONREQUEST = DESCRIPTOR.message_types_by_name['MotorServiceGetPositionRequest']
_MOTORSERVICEGETPOSITIONRESPONSE = DESCRIPTOR.message_types_by_name['MotorServiceGetPositionResponse']
_MOTORSERVICESTOPREQUEST = DESCRIPTOR.message_types_by_name['MotorServiceStopRequest']
_MOTORSERVICESTOPRESPONSE = DESCRIPTOR.message_types_by_name['MotorServiceStopResponse']
_MOTORSERVICEISPOWEREDREQUEST = DESCRIPTOR.message_types_by_name['MotorServiceIsPoweredRequest']
_MOTORSERVICEISPOWEREDRESPONSE = DESCRIPTOR.message_types_by_name['MotorServiceIsPoweredResponse']
_MOTORSERVICEGETFEATURESREQUEST = DESCRIPTOR.message_types_by_name['MotorServiceGetFeaturesRequest']
_MOTORSERVICEGETFEATURESRESPONSE = DESCRIPTOR.message_types_by_name['MotorServiceGetFeaturesResponse']
MotorServiceSetPowerRequest = _reflection.GeneratedProtocolMessageType('MotorServiceSetPowerRequest', (_message.Message,), {'DESCRIPTOR': _MOTORSERVICESETPOWERREQUEST, '__module__': 'proto.api.component.v1.motor_pb2'})
_sym_db.RegisterMessage(MotorServiceSetPowerRequest)
MotorServiceSetPowerResponse = _reflection.GeneratedProtocolMessageType('MotorServiceSetPowerResponse', (_message.Message,), {'DESCRIPTOR': _MOTORSERVICESETPOWERRESPONSE, '__module__': 'proto.api.component.v1.motor_pb2'})
_sym_db.RegisterMessage(MotorServiceSetPowerResponse)
MotorServiceGoForRequest = _reflection.GeneratedProtocolMessageType('MotorServiceGoForRequest', (_message.Message,), {'DESCRIPTOR': _MOTORSERVICEGOFORREQUEST, '__module__': 'proto.api.component.v1.motor_pb2'})
_sym_db.RegisterMessage(MotorServiceGoForRequest)
MotorServiceGoForResponse = _reflection.GeneratedProtocolMessageType('MotorServiceGoForResponse', (_message.Message,), {'DESCRIPTOR': _MOTORSERVICEGOFORRESPONSE, '__module__': 'proto.api.component.v1.motor_pb2'})
_sym_db.RegisterMessage(MotorServiceGoForResponse)
MotorServiceGoToRequest = _reflection.GeneratedProtocolMessageType('MotorServiceGoToRequest', (_message.Message,), {'DESCRIPTOR': _MOTORSERVICEGOTOREQUEST, '__module__': 'proto.api.component.v1.motor_pb2'})
_sym_db.RegisterMessage(MotorServiceGoToRequest)
MotorServiceGoToResponse = _reflection.GeneratedProtocolMessageType('MotorServiceGoToResponse', (_message.Message,), {'DESCRIPTOR': _MOTORSERVICEGOTORESPONSE, '__module__': 'proto.api.component.v1.motor_pb2'})
_sym_db.RegisterMessage(MotorServiceGoToResponse)
MotorServiceResetZeroPositionRequest = _reflection.GeneratedProtocolMessageType('MotorServiceResetZeroPositionRequest', (_message.Message,), {'DESCRIPTOR': _MOTORSERVICERESETZEROPOSITIONREQUEST, '__module__': 'proto.api.component.v1.motor_pb2'})
_sym_db.RegisterMessage(MotorServiceResetZeroPositionRequest)
MotorServiceResetZeroPositionResponse = _reflection.GeneratedProtocolMessageType('MotorServiceResetZeroPositionResponse', (_message.Message,), {'DESCRIPTOR': _MOTORSERVICERESETZEROPOSITIONRESPONSE, '__module__': 'proto.api.component.v1.motor_pb2'})
_sym_db.RegisterMessage(MotorServiceResetZeroPositionResponse)
MotorServiceGetPositionRequest = _reflection.GeneratedProtocolMessageType('MotorServiceGetPositionRequest', (_message.Message,), {'DESCRIPTOR': _MOTORSERVICEGETPOSITIONREQUEST, '__module__': 'proto.api.component.v1.motor_pb2'})
_sym_db.RegisterMessage(MotorServiceGetPositionRequest)
MotorServiceGetPositionResponse = _reflection.GeneratedProtocolMessageType('MotorServiceGetPositionResponse', (_message.Message,), {'DESCRIPTOR': _MOTORSERVICEGETPOSITIONRESPONSE, '__module__': 'proto.api.component.v1.motor_pb2'})
_sym_db.RegisterMessage(MotorServiceGetPositionResponse)
MotorServiceStopRequest = _reflection.GeneratedProtocolMessageType('MotorServiceStopRequest', (_message.Message,), {'DESCRIPTOR': _MOTORSERVICESTOPREQUEST, '__module__': 'proto.api.component.v1.motor_pb2'})
_sym_db.RegisterMessage(MotorServiceStopRequest)
MotorServiceStopResponse = _reflection.GeneratedProtocolMessageType('MotorServiceStopResponse', (_message.Message,), {'DESCRIPTOR': _MOTORSERVICESTOPRESPONSE, '__module__': 'proto.api.component.v1.motor_pb2'})
_sym_db.RegisterMessage(MotorServiceStopResponse)
MotorServiceIsPoweredRequest = _reflection.GeneratedProtocolMessageType('MotorServiceIsPoweredRequest', (_message.Message,), {'DESCRIPTOR': _MOTORSERVICEISPOWEREDREQUEST, '__module__': 'proto.api.component.v1.motor_pb2'})
_sym_db.RegisterMessage(MotorServiceIsPoweredRequest)
MotorServiceIsPoweredResponse = _reflection.GeneratedProtocolMessageType('MotorServiceIsPoweredResponse', (_message.Message,), {'DESCRIPTOR': _MOTORSERVICEISPOWEREDRESPONSE, '__module__': 'proto.api.component.v1.motor_pb2'})
_sym_db.RegisterMessage(MotorServiceIsPoweredResponse)
MotorServiceGetFeaturesRequest = _reflection.GeneratedProtocolMessageType('MotorServiceGetFeaturesRequest', (_message.Message,), {'DESCRIPTOR': _MOTORSERVICEGETFEATURESREQUEST, '__module__': 'proto.api.component.v1.motor_pb2'})
_sym_db.RegisterMessage(MotorServiceGetFeaturesRequest)
MotorServiceGetFeaturesResponse = _reflection.GeneratedProtocolMessageType('MotorServiceGetFeaturesResponse', (_message.Message,), {'DESCRIPTOR': _MOTORSERVICEGETFEATURESRESPONSE, '__module__': 'proto.api.component.v1.motor_pb2'})
_sym_db.RegisterMessage(MotorServiceGetFeaturesResponse)
_MOTORSERVICE = DESCRIPTOR.services_by_name['MotorService']
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n#com.viam.rdk.proto.api.component.v1Z&go.viam.com/rdk/proto/api/component/v1'
    _MOTORSERVICE.methods_by_name['SetPower']._options = None
    _MOTORSERVICE.methods_by_name['SetPower']._serialized_options = b'\x82\xd3\xe4\x93\x02&\x1a$/api/v1/component/motor/{name}/power'
    _MOTORSERVICE.methods_by_name['GoFor']._options = None
    _MOTORSERVICE.methods_by_name['GoFor']._serialized_options = b"\x82\xd3\xe4\x93\x02'\x1a%/api/v1/component/motor/{name}/go_for"
    _MOTORSERVICE.methods_by_name['GoTo']._options = None
    _MOTORSERVICE.methods_by_name['GoTo']._serialized_options = b'\x82\xd3\xe4\x93\x02&\x1a$/api/v1/component/motor/{name}/go_to'
    _MOTORSERVICE.methods_by_name['ResetZeroPosition']._options = None
    _MOTORSERVICE.methods_by_name['ResetZeroPosition']._serialized_options = b'\x82\xd3\xe4\x93\x02%\x1a#/api/v1/component/motor/{name}/zero'
    _MOTORSERVICE.methods_by_name['GetPosition']._options = None
    _MOTORSERVICE.methods_by_name['GetPosition']._serialized_options = b"\x82\xd3\xe4\x93\x02)\x12'/api/v1/component/motor/{name}/position"
    _MOTORSERVICE.methods_by_name['GetFeatures']._options = None
    _MOTORSERVICE.methods_by_name['GetFeatures']._serialized_options = b"\x82\xd3\xe4\x93\x02)\x12'/api/v1/component/motor/{name}/features"
    _MOTORSERVICE.methods_by_name['Stop']._options = None
    _MOTORSERVICE.methods_by_name['Stop']._serialized_options = b'\x82\xd3\xe4\x93\x02%\x1a#/api/v1/component/motor/{name}/stop'
    _MOTORSERVICE.methods_by_name['IsPowered']._options = None
    _MOTORSERVICE.methods_by_name['IsPowered']._serialized_options = b'\x82\xd3\xe4\x93\x02(\x12&/api/v1/component/motor/{name}/powered'
    _MOTORSERVICESETPOWERREQUEST._serialized_start = 122
    _MOTORSERVICESETPOWERREQUEST._serialized_end = 200
    _MOTORSERVICESETPOWERRESPONSE._serialized_start = 202
    _MOTORSERVICESETPOWERRESPONSE._serialized_end = 232
    _MOTORSERVICEGOFORREQUEST._serialized_start = 234
    _MOTORSERVICEGOFORREQUEST._serialized_end = 332
    _MOTORSERVICEGOFORRESPONSE._serialized_start = 334
    _MOTORSERVICEGOFORRESPONSE._serialized_end = 361
    _MOTORSERVICEGOTOREQUEST._serialized_start = 363
    _MOTORSERVICEGOTOREQUEST._serialized_end = 477
    _MOTORSERVICEGOTORESPONSE._serialized_start = 479
    _MOTORSERVICEGOTORESPONSE._serialized_end = 505
    _MOTORSERVICERESETZEROPOSITIONREQUEST._serialized_start = 507
    _MOTORSERVICERESETZEROPOSITIONREQUEST._serialized_end = 589
    _MOTORSERVICERESETZEROPOSITIONRESPONSE._serialized_start = 591
    _MOTORSERVICERESETZEROPOSITIONRESPONSE._serialized_end = 630
    _MOTORSERVICEGETPOSITIONREQUEST._serialized_start = 632
    _MOTORSERVICEGETPOSITIONREQUEST._serialized_end = 684
    _MOTORSERVICEGETPOSITIONRESPONSE._serialized_start = 686
    _MOTORSERVICEGETPOSITIONRESPONSE._serialized_end = 747
    _MOTORSERVICESTOPREQUEST._serialized_start = 749
    _MOTORSERVICESTOPREQUEST._serialized_end = 794
    _MOTORSERVICESTOPRESPONSE._serialized_start = 796
    _MOTORSERVICESTOPRESPONSE._serialized_end = 822
    _MOTORSERVICEISPOWEREDREQUEST._serialized_start = 824
    _MOTORSERVICEISPOWEREDREQUEST._serialized_end = 874
    _MOTORSERVICEISPOWEREDRESPONSE._serialized_start = 876
    _MOTORSERVICEISPOWEREDRESPONSE._serialized_end = 928
    _MOTORSERVICEGETFEATURESREQUEST._serialized_start = 930
    _MOTORSERVICEGETFEATURESREQUEST._serialized_end = 982
    _MOTORSERVICEGETFEATURESRESPONSE._serialized_start = 984
    _MOTORSERVICEGETFEATURESRESPONSE._serialized_end = 1064
    _MOTORSERVICE._serialized_start = 1067
    _MOTORSERVICE._serialized_end = 2431