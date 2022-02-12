"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n"proto/api/component/v1/motor.proto\x12\x16proto.api.component.v1\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1cgoogle/api/annotations.proto"N\n\x1bMotorServiceSetPowerRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x1b\n\tpower_pct\x18\x02 \x01(\x01R\x08powerPct"\x1e\n\x1cMotorServiceSetPowerResponse"H\n\x15MotorServiceGoRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x1b\n\tpower_pct\x18\x02 \x01(\x01R\x08powerPct"\x18\n\x16MotorServiceGoResponse"b\n\x18MotorServiceGoForRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x10\n\x03rpm\x18\x02 \x01(\x01R\x03rpm\x12 \n\x0brevolutions\x18\x03 \x01(\x01R\x0brevolutions"\x1b\n\x19MotorServiceGoForResponse"[\n\x17MotorServiceGoToRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x10\n\x03rpm\x18\x02 \x01(\x01R\x03rpm\x12\x1a\n\x08position\x18\x03 \x01(\x01R\x08position"\x1a\n\x18MotorServiceGoToResponse"E\n\x1dMotorServiceGoTillStopRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x10\n\x03rpm\x18\x02 \x01(\x01R\x03rpm" \n\x1eMotorServiceGoTillStopResponse"R\n$MotorServiceResetZeroPositionRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x16\n\x06offset\x18\x02 \x01(\x01R\x06offset"\'\n%MotorServiceResetZeroPositionResponse"1\n\x1bMotorServicePositionRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name":\n\x1cMotorServicePositionResponse\x12\x1a\n\x08position\x18\x01 \x01(\x01R\x08position":\n$MotorServicePositionSupportedRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name"E\n%MotorServicePositionSupportedResponse\x12\x1c\n\tsupported\x18\x01 \x01(\x08R\tsupported"-\n\x17MotorServiceStopRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name"\x1a\n\x18MotorServiceStopResponse"-\n\x17MotorServiceIsOnRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name"/\n\x18MotorServiceIsOnResponse\x12\x13\n\x05is_on\x18\x01 \x01(\x08R\x04isOn2\xb5\x0c\n\x0cMotorService\x12\x99\x01\n\x08SetPower\x123.proto.api.component.v1.MotorServiceSetPowerRequest\x1a4.proto.api.component.v1.MotorServiceSetPowerResponse""\x82\xd3\xe4\x93\x02\x1c\x1a\x1a/api/v1/motor/{name}/power\x12\x84\x01\n\x02Go\x12-.proto.api.component.v1.MotorServiceGoRequest\x1a..proto.api.component.v1.MotorServiceGoResponse"\x1f\x82\xd3\xe4\x93\x02\x19\x1a\x17/api/v1/motor/{name}/go\x12\x91\x01\n\x05GoFor\x120.proto.api.component.v1.MotorServiceGoForRequest\x1a1.proto.api.component.v1.MotorServiceGoForResponse"#\x82\xd3\xe4\x93\x02\x1d\x1a\x1b/api/v1/motor/{name}/go_for\x12\x8d\x01\n\x04GoTo\x12/.proto.api.component.v1.MotorServiceGoToRequest\x1a0.proto.api.component.v1.MotorServiceGoToResponse""\x82\xd3\xe4\x93\x02\x1c\x1a\x1a/api/v1/motor/{name}/go_to\x12\xa6\x01\n\nGoTillStop\x125.proto.api.component.v1.MotorServiceGoTillStopRequest\x1a6.proto.api.component.v1.MotorServiceGoTillStopResponse")\x82\xd3\xe4\x93\x02#\x1a!/api/v1/motor/{name}/go_till_stop\x12\xb3\x01\n\x11ResetZeroPosition\x12<.proto.api.component.v1.MotorServiceResetZeroPositionRequest\x1a=.proto.api.component.v1.MotorServiceResetZeroPositionResponse"!\x82\xd3\xe4\x93\x02\x1b\x1a\x19/api/v1/motor/{name}/zero\x12\x9c\x01\n\x08Position\x123.proto.api.component.v1.MotorServicePositionRequest\x1a4.proto.api.component.v1.MotorServicePositionResponse"%\x82\xd3\xe4\x93\x02\x1f\x12\x1d/api/v1/motor/{name}/position\x12\xc1\x01\n\x11PositionSupported\x12<.proto.api.component.v1.MotorServicePositionSupportedRequest\x1a=.proto.api.component.v1.MotorServicePositionSupportedResponse"/\x82\xd3\xe4\x93\x02)\x12\'/api/v1/motor/{name}/position_supported\x12\x8b\x01\n\x04Stop\x12/.proto.api.component.v1.MotorServiceStopRequest\x1a0.proto.api.component.v1.MotorServiceStopResponse" \x82\xd3\xe4\x93\x02\x1a\x1a\x18/api/v1/motor/{name}/off\x12\x8d\x01\n\x04IsOn\x12/.proto.api.component.v1.MotorServiceIsOnRequest\x1a0.proto.api.component.v1.MotorServiceIsOnResponse""\x82\xd3\xe4\x93\x02\x1c\x12\x1a/api/v1/motor/{name}/is_onBM\n#com.viam.rdk.proto.api.component.v1Z&go.viam.com/rdk/proto/api/component/v1b\x06proto3')
_MOTORSERVICESETPOWERREQUEST = DESCRIPTOR.message_types_by_name['MotorServiceSetPowerRequest']
_MOTORSERVICESETPOWERRESPONSE = DESCRIPTOR.message_types_by_name['MotorServiceSetPowerResponse']
_MOTORSERVICEGOREQUEST = DESCRIPTOR.message_types_by_name['MotorServiceGoRequest']
_MOTORSERVICEGORESPONSE = DESCRIPTOR.message_types_by_name['MotorServiceGoResponse']
_MOTORSERVICEGOFORREQUEST = DESCRIPTOR.message_types_by_name['MotorServiceGoForRequest']
_MOTORSERVICEGOFORRESPONSE = DESCRIPTOR.message_types_by_name['MotorServiceGoForResponse']
_MOTORSERVICEGOTOREQUEST = DESCRIPTOR.message_types_by_name['MotorServiceGoToRequest']
_MOTORSERVICEGOTORESPONSE = DESCRIPTOR.message_types_by_name['MotorServiceGoToResponse']
_MOTORSERVICEGOTILLSTOPREQUEST = DESCRIPTOR.message_types_by_name['MotorServiceGoTillStopRequest']
_MOTORSERVICEGOTILLSTOPRESPONSE = DESCRIPTOR.message_types_by_name['MotorServiceGoTillStopResponse']
_MOTORSERVICERESETZEROPOSITIONREQUEST = DESCRIPTOR.message_types_by_name['MotorServiceResetZeroPositionRequest']
_MOTORSERVICERESETZEROPOSITIONRESPONSE = DESCRIPTOR.message_types_by_name['MotorServiceResetZeroPositionResponse']
_MOTORSERVICEPOSITIONREQUEST = DESCRIPTOR.message_types_by_name['MotorServicePositionRequest']
_MOTORSERVICEPOSITIONRESPONSE = DESCRIPTOR.message_types_by_name['MotorServicePositionResponse']
_MOTORSERVICEPOSITIONSUPPORTEDREQUEST = DESCRIPTOR.message_types_by_name['MotorServicePositionSupportedRequest']
_MOTORSERVICEPOSITIONSUPPORTEDRESPONSE = DESCRIPTOR.message_types_by_name['MotorServicePositionSupportedResponse']
_MOTORSERVICESTOPREQUEST = DESCRIPTOR.message_types_by_name['MotorServiceStopRequest']
_MOTORSERVICESTOPRESPONSE = DESCRIPTOR.message_types_by_name['MotorServiceStopResponse']
_MOTORSERVICEISONREQUEST = DESCRIPTOR.message_types_by_name['MotorServiceIsOnRequest']
_MOTORSERVICEISONRESPONSE = DESCRIPTOR.message_types_by_name['MotorServiceIsOnResponse']
MotorServiceSetPowerRequest = _reflection.GeneratedProtocolMessageType('MotorServiceSetPowerRequest', (_message.Message,), {'DESCRIPTOR': _MOTORSERVICESETPOWERREQUEST, '__module__': 'proto.api.component.v1.motor_pb2'})
_sym_db.RegisterMessage(MotorServiceSetPowerRequest)
MotorServiceSetPowerResponse = _reflection.GeneratedProtocolMessageType('MotorServiceSetPowerResponse', (_message.Message,), {'DESCRIPTOR': _MOTORSERVICESETPOWERRESPONSE, '__module__': 'proto.api.component.v1.motor_pb2'})
_sym_db.RegisterMessage(MotorServiceSetPowerResponse)
MotorServiceGoRequest = _reflection.GeneratedProtocolMessageType('MotorServiceGoRequest', (_message.Message,), {'DESCRIPTOR': _MOTORSERVICEGOREQUEST, '__module__': 'proto.api.component.v1.motor_pb2'})
_sym_db.RegisterMessage(MotorServiceGoRequest)
MotorServiceGoResponse = _reflection.GeneratedProtocolMessageType('MotorServiceGoResponse', (_message.Message,), {'DESCRIPTOR': _MOTORSERVICEGORESPONSE, '__module__': 'proto.api.component.v1.motor_pb2'})
_sym_db.RegisterMessage(MotorServiceGoResponse)
MotorServiceGoForRequest = _reflection.GeneratedProtocolMessageType('MotorServiceGoForRequest', (_message.Message,), {'DESCRIPTOR': _MOTORSERVICEGOFORREQUEST, '__module__': 'proto.api.component.v1.motor_pb2'})
_sym_db.RegisterMessage(MotorServiceGoForRequest)
MotorServiceGoForResponse = _reflection.GeneratedProtocolMessageType('MotorServiceGoForResponse', (_message.Message,), {'DESCRIPTOR': _MOTORSERVICEGOFORRESPONSE, '__module__': 'proto.api.component.v1.motor_pb2'})
_sym_db.RegisterMessage(MotorServiceGoForResponse)
MotorServiceGoToRequest = _reflection.GeneratedProtocolMessageType('MotorServiceGoToRequest', (_message.Message,), {'DESCRIPTOR': _MOTORSERVICEGOTOREQUEST, '__module__': 'proto.api.component.v1.motor_pb2'})
_sym_db.RegisterMessage(MotorServiceGoToRequest)
MotorServiceGoToResponse = _reflection.GeneratedProtocolMessageType('MotorServiceGoToResponse', (_message.Message,), {'DESCRIPTOR': _MOTORSERVICEGOTORESPONSE, '__module__': 'proto.api.component.v1.motor_pb2'})
_sym_db.RegisterMessage(MotorServiceGoToResponse)
MotorServiceGoTillStopRequest = _reflection.GeneratedProtocolMessageType('MotorServiceGoTillStopRequest', (_message.Message,), {'DESCRIPTOR': _MOTORSERVICEGOTILLSTOPREQUEST, '__module__': 'proto.api.component.v1.motor_pb2'})
_sym_db.RegisterMessage(MotorServiceGoTillStopRequest)
MotorServiceGoTillStopResponse = _reflection.GeneratedProtocolMessageType('MotorServiceGoTillStopResponse', (_message.Message,), {'DESCRIPTOR': _MOTORSERVICEGOTILLSTOPRESPONSE, '__module__': 'proto.api.component.v1.motor_pb2'})
_sym_db.RegisterMessage(MotorServiceGoTillStopResponse)
MotorServiceResetZeroPositionRequest = _reflection.GeneratedProtocolMessageType('MotorServiceResetZeroPositionRequest', (_message.Message,), {'DESCRIPTOR': _MOTORSERVICERESETZEROPOSITIONREQUEST, '__module__': 'proto.api.component.v1.motor_pb2'})
_sym_db.RegisterMessage(MotorServiceResetZeroPositionRequest)
MotorServiceResetZeroPositionResponse = _reflection.GeneratedProtocolMessageType('MotorServiceResetZeroPositionResponse', (_message.Message,), {'DESCRIPTOR': _MOTORSERVICERESETZEROPOSITIONRESPONSE, '__module__': 'proto.api.component.v1.motor_pb2'})
_sym_db.RegisterMessage(MotorServiceResetZeroPositionResponse)
MotorServicePositionRequest = _reflection.GeneratedProtocolMessageType('MotorServicePositionRequest', (_message.Message,), {'DESCRIPTOR': _MOTORSERVICEPOSITIONREQUEST, '__module__': 'proto.api.component.v1.motor_pb2'})
_sym_db.RegisterMessage(MotorServicePositionRequest)
MotorServicePositionResponse = _reflection.GeneratedProtocolMessageType('MotorServicePositionResponse', (_message.Message,), {'DESCRIPTOR': _MOTORSERVICEPOSITIONRESPONSE, '__module__': 'proto.api.component.v1.motor_pb2'})
_sym_db.RegisterMessage(MotorServicePositionResponse)
MotorServicePositionSupportedRequest = _reflection.GeneratedProtocolMessageType('MotorServicePositionSupportedRequest', (_message.Message,), {'DESCRIPTOR': _MOTORSERVICEPOSITIONSUPPORTEDREQUEST, '__module__': 'proto.api.component.v1.motor_pb2'})
_sym_db.RegisterMessage(MotorServicePositionSupportedRequest)
MotorServicePositionSupportedResponse = _reflection.GeneratedProtocolMessageType('MotorServicePositionSupportedResponse', (_message.Message,), {'DESCRIPTOR': _MOTORSERVICEPOSITIONSUPPORTEDRESPONSE, '__module__': 'proto.api.component.v1.motor_pb2'})
_sym_db.RegisterMessage(MotorServicePositionSupportedResponse)
MotorServiceStopRequest = _reflection.GeneratedProtocolMessageType('MotorServiceStopRequest', (_message.Message,), {'DESCRIPTOR': _MOTORSERVICESTOPREQUEST, '__module__': 'proto.api.component.v1.motor_pb2'})
_sym_db.RegisterMessage(MotorServiceStopRequest)
MotorServiceStopResponse = _reflection.GeneratedProtocolMessageType('MotorServiceStopResponse', (_message.Message,), {'DESCRIPTOR': _MOTORSERVICESTOPRESPONSE, '__module__': 'proto.api.component.v1.motor_pb2'})
_sym_db.RegisterMessage(MotorServiceStopResponse)
MotorServiceIsOnRequest = _reflection.GeneratedProtocolMessageType('MotorServiceIsOnRequest', (_message.Message,), {'DESCRIPTOR': _MOTORSERVICEISONREQUEST, '__module__': 'proto.api.component.v1.motor_pb2'})
_sym_db.RegisterMessage(MotorServiceIsOnRequest)
MotorServiceIsOnResponse = _reflection.GeneratedProtocolMessageType('MotorServiceIsOnResponse', (_message.Message,), {'DESCRIPTOR': _MOTORSERVICEISONRESPONSE, '__module__': 'proto.api.component.v1.motor_pb2'})
_sym_db.RegisterMessage(MotorServiceIsOnResponse)
_MOTORSERVICE = DESCRIPTOR.services_by_name['MotorService']
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n#com.viam.rdk.proto.api.component.v1Z&go.viam.com/rdk/proto/api/component/v1'
    _MOTORSERVICE.methods_by_name['SetPower']._options = None
    _MOTORSERVICE.methods_by_name['SetPower']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1c\x1a\x1a/api/v1/motor/{name}/power'
    _MOTORSERVICE.methods_by_name['Go']._options = None
    _MOTORSERVICE.methods_by_name['Go']._serialized_options = b'\x82\xd3\xe4\x93\x02\x19\x1a\x17/api/v1/motor/{name}/go'
    _MOTORSERVICE.methods_by_name['GoFor']._options = None
    _MOTORSERVICE.methods_by_name['GoFor']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1d\x1a\x1b/api/v1/motor/{name}/go_for'
    _MOTORSERVICE.methods_by_name['GoTo']._options = None
    _MOTORSERVICE.methods_by_name['GoTo']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1c\x1a\x1a/api/v1/motor/{name}/go_to'
    _MOTORSERVICE.methods_by_name['GoTillStop']._options = None
    _MOTORSERVICE.methods_by_name['GoTillStop']._serialized_options = b'\x82\xd3\xe4\x93\x02#\x1a!/api/v1/motor/{name}/go_till_stop'
    _MOTORSERVICE.methods_by_name['ResetZeroPosition']._options = None
    _MOTORSERVICE.methods_by_name['ResetZeroPosition']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1b\x1a\x19/api/v1/motor/{name}/zero'
    _MOTORSERVICE.methods_by_name['Position']._options = None
    _MOTORSERVICE.methods_by_name['Position']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1f\x12\x1d/api/v1/motor/{name}/position'
    _MOTORSERVICE.methods_by_name['PositionSupported']._options = None
    _MOTORSERVICE.methods_by_name['PositionSupported']._serialized_options = b"\x82\xd3\xe4\x93\x02)\x12'/api/v1/motor/{name}/position_supported"
    _MOTORSERVICE.methods_by_name['Stop']._options = None
    _MOTORSERVICE.methods_by_name['Stop']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1a\x1a\x18/api/v1/motor/{name}/off'
    _MOTORSERVICE.methods_by_name['IsOn']._options = None
    _MOTORSERVICE.methods_by_name['IsOn']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1c\x12\x1a/api/v1/motor/{name}/is_on'
    _MOTORSERVICESETPOWERREQUEST._serialized_start = 122
    _MOTORSERVICESETPOWERREQUEST._serialized_end = 200
    _MOTORSERVICESETPOWERRESPONSE._serialized_start = 202
    _MOTORSERVICESETPOWERRESPONSE._serialized_end = 232
    _MOTORSERVICEGOREQUEST._serialized_start = 234
    _MOTORSERVICEGOREQUEST._serialized_end = 306
    _MOTORSERVICEGORESPONSE._serialized_start = 308
    _MOTORSERVICEGORESPONSE._serialized_end = 332
    _MOTORSERVICEGOFORREQUEST._serialized_start = 334
    _MOTORSERVICEGOFORREQUEST._serialized_end = 432
    _MOTORSERVICEGOFORRESPONSE._serialized_start = 434
    _MOTORSERVICEGOFORRESPONSE._serialized_end = 461
    _MOTORSERVICEGOTOREQUEST._serialized_start = 463
    _MOTORSERVICEGOTOREQUEST._serialized_end = 554
    _MOTORSERVICEGOTORESPONSE._serialized_start = 556
    _MOTORSERVICEGOTORESPONSE._serialized_end = 582
    _MOTORSERVICEGOTILLSTOPREQUEST._serialized_start = 584
    _MOTORSERVICEGOTILLSTOPREQUEST._serialized_end = 653
    _MOTORSERVICEGOTILLSTOPRESPONSE._serialized_start = 655
    _MOTORSERVICEGOTILLSTOPRESPONSE._serialized_end = 687
    _MOTORSERVICERESETZEROPOSITIONREQUEST._serialized_start = 689
    _MOTORSERVICERESETZEROPOSITIONREQUEST._serialized_end = 771
    _MOTORSERVICERESETZEROPOSITIONRESPONSE._serialized_start = 773
    _MOTORSERVICERESETZEROPOSITIONRESPONSE._serialized_end = 812
    _MOTORSERVICEPOSITIONREQUEST._serialized_start = 814
    _MOTORSERVICEPOSITIONREQUEST._serialized_end = 863
    _MOTORSERVICEPOSITIONRESPONSE._serialized_start = 865
    _MOTORSERVICEPOSITIONRESPONSE._serialized_end = 923
    _MOTORSERVICEPOSITIONSUPPORTEDREQUEST._serialized_start = 925
    _MOTORSERVICEPOSITIONSUPPORTEDREQUEST._serialized_end = 983
    _MOTORSERVICEPOSITIONSUPPORTEDRESPONSE._serialized_start = 985
    _MOTORSERVICEPOSITIONSUPPORTEDRESPONSE._serialized_end = 1054
    _MOTORSERVICESTOPREQUEST._serialized_start = 1056
    _MOTORSERVICESTOPREQUEST._serialized_end = 1101
    _MOTORSERVICESTOPRESPONSE._serialized_start = 1103
    _MOTORSERVICESTOPRESPONSE._serialized_end = 1129
    _MOTORSERVICEISONREQUEST._serialized_start = 1131
    _MOTORSERVICEISONREQUEST._serialized_end = 1176
    _MOTORSERVICEISONRESPONSE._serialized_start = 1178
    _MOTORSERVICEISONRESPONSE._serialized_end = 1225
    _MOTORSERVICE._serialized_start = 1228
    _MOTORSERVICE._serialized_end = 2817