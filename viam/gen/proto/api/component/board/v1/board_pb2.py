"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......proto.api.common.v1 import common_pb2 as proto_dot_api_dot_common_dot_v1_dot_common__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(proto/api/component/board/v1/board.proto\x12\x1cproto.api.component.board.v1\x1a\x1cgoogle/api/annotations.proto\x1a proto/api/common/v1/common.proto"#\n\rStatusRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name"J\n\x0eStatusResponse\x128\n\x06status\x18\x01 \x01(\x0b2 .proto.api.common.v1.BoardStatusR\x06status"J\n\x0eSetGPIORequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x10\n\x03pin\x18\x02 \x01(\tR\x03pin\x12\x12\n\x04high\x18\x03 \x01(\x08R\x04high"\x11\n\x0fSetGPIOResponse"6\n\x0eGetGPIORequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x10\n\x03pin\x18\x02 \x01(\tR\x03pin"%\n\x0fGetGPIOResponse\x12\x12\n\x04high\x18\x01 \x01(\x08R\x04high"[\n\rSetPWMRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x10\n\x03pin\x18\x02 \x01(\tR\x03pin\x12$\n\x0eduty_cycle_pct\x18\x03 \x01(\x01R\x0cdutyCyclePct"\x10\n\x0eSetPWMResponse"\x19\n\x17SetPWMFrequencyResponse"a\n\x16SetPWMFrequencyRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x10\n\x03pin\x18\x02 \x01(\tR\x03pin\x12!\n\x0cfrequency_hz\x18\x03 \x01(\x04R\x0bfrequencyHz"f\n\x17ReadAnalogReaderRequest\x12\x1d\n\nboard_name\x18\x01 \x01(\tR\tboardName\x12,\n\x12analog_reader_name\x18\x02 \x01(\tR\x10analogReaderName"0\n\x18ReadAnalogReaderResponse\x12\x14\n\x05value\x18\x01 \x01(\x05R\x05value"v\n\x1fGetDigitalInterruptValueRequest\x12\x1d\n\nboard_name\x18\x01 \x01(\tR\tboardName\x124\n\x16digital_interrupt_name\x18\x02 \x01(\tR\x14digitalInterruptName"8\n GetDigitalInterruptValueResponse\x12\x14\n\x05value\x18\x01 \x01(\x03R\x05value2\xf8\t\n\x0cBoardService\x12\x92\x01\n\x06Status\x12+.proto.api.component.board.v1.StatusRequest\x1a,.proto.api.component.board.v1.StatusResponse"-\x82\xd3\xe4\x93\x02\'\x12%/api/v1/component/board/{name}/status\x12\x97\x01\n\x07SetGPIO\x12,.proto.api.component.board.v1.SetGPIORequest\x1a-.proto.api.component.board.v1.SetGPIOResponse"/\x82\xd3\xe4\x93\x02)\x1a\'/api/v1/component/board/{name}/set_gpio\x12\x97\x01\n\x07GetGPIO\x12,.proto.api.component.board.v1.GetGPIORequest\x1a-.proto.api.component.board.v1.GetGPIOResponse"/\x82\xd3\xe4\x93\x02)\x12\'/api/v1/component/board/{name}/get_gpio\x12\x93\x01\n\x06SetPWM\x12+.proto.api.component.board.v1.SetPWMRequest\x1a,.proto.api.component.board.v1.SetPWMResponse".\x82\xd3\xe4\x93\x02(\x1a&/api/v1/component/board/{name}/set_pwm\x12\xb3\x01\n\x0fSetPWMFrequency\x124.proto.api.component.board.v1.SetPWMFrequencyRequest\x1a5.proto.api.component.board.v1.SetPWMFrequencyResponse"3\x82\xd3\xe4\x93\x02-\x1a+/api/v1/component/board/{name}/set_pwm_freq\x12\xd7\x01\n\x10ReadAnalogReader\x125.proto.api.component.board.v1.ReadAnalogReaderRequest\x1a6.proto.api.component.board.v1.ReadAnalogReaderResponse"T\x82\xd3\xe4\x93\x02N\x12L/api/v1/component/board/{board_name}/analog_reader/{analog_reader_name}/read\x12\xf8\x01\n\x18GetDigitalInterruptValue\x12=.proto.api.component.board.v1.GetDigitalInterruptValueRequest\x1a>.proto.api.component.board.v1.GetDigitalInterruptValueResponse"]\x82\xd3\xe4\x93\x02W\x12U/api/v1/component/board/{board_name}/digital_interrupt/{digital_interrupt_name}/valueBY\n)com.viam.rdk.proto.api.component.board.v1Z,go.viam.com/rdk/proto/api/component/board/v1b\x06proto3')
_STATUSREQUEST = DESCRIPTOR.message_types_by_name['StatusRequest']
_STATUSRESPONSE = DESCRIPTOR.message_types_by_name['StatusResponse']
_SETGPIOREQUEST = DESCRIPTOR.message_types_by_name['SetGPIORequest']
_SETGPIORESPONSE = DESCRIPTOR.message_types_by_name['SetGPIOResponse']
_GETGPIOREQUEST = DESCRIPTOR.message_types_by_name['GetGPIORequest']
_GETGPIORESPONSE = DESCRIPTOR.message_types_by_name['GetGPIOResponse']
_SETPWMREQUEST = DESCRIPTOR.message_types_by_name['SetPWMRequest']
_SETPWMRESPONSE = DESCRIPTOR.message_types_by_name['SetPWMResponse']
_SETPWMFREQUENCYRESPONSE = DESCRIPTOR.message_types_by_name['SetPWMFrequencyResponse']
_SETPWMFREQUENCYREQUEST = DESCRIPTOR.message_types_by_name['SetPWMFrequencyRequest']
_READANALOGREADERREQUEST = DESCRIPTOR.message_types_by_name['ReadAnalogReaderRequest']
_READANALOGREADERRESPONSE = DESCRIPTOR.message_types_by_name['ReadAnalogReaderResponse']
_GETDIGITALINTERRUPTVALUEREQUEST = DESCRIPTOR.message_types_by_name['GetDigitalInterruptValueRequest']
_GETDIGITALINTERRUPTVALUERESPONSE = DESCRIPTOR.message_types_by_name['GetDigitalInterruptValueResponse']
StatusRequest = _reflection.GeneratedProtocolMessageType('StatusRequest', (_message.Message,), {'DESCRIPTOR': _STATUSREQUEST, '__module__': 'proto.api.component.board.v1.board_pb2'})
_sym_db.RegisterMessage(StatusRequest)
StatusResponse = _reflection.GeneratedProtocolMessageType('StatusResponse', (_message.Message,), {'DESCRIPTOR': _STATUSRESPONSE, '__module__': 'proto.api.component.board.v1.board_pb2'})
_sym_db.RegisterMessage(StatusResponse)
SetGPIORequest = _reflection.GeneratedProtocolMessageType('SetGPIORequest', (_message.Message,), {'DESCRIPTOR': _SETGPIOREQUEST, '__module__': 'proto.api.component.board.v1.board_pb2'})
_sym_db.RegisterMessage(SetGPIORequest)
SetGPIOResponse = _reflection.GeneratedProtocolMessageType('SetGPIOResponse', (_message.Message,), {'DESCRIPTOR': _SETGPIORESPONSE, '__module__': 'proto.api.component.board.v1.board_pb2'})
_sym_db.RegisterMessage(SetGPIOResponse)
GetGPIORequest = _reflection.GeneratedProtocolMessageType('GetGPIORequest', (_message.Message,), {'DESCRIPTOR': _GETGPIOREQUEST, '__module__': 'proto.api.component.board.v1.board_pb2'})
_sym_db.RegisterMessage(GetGPIORequest)
GetGPIOResponse = _reflection.GeneratedProtocolMessageType('GetGPIOResponse', (_message.Message,), {'DESCRIPTOR': _GETGPIORESPONSE, '__module__': 'proto.api.component.board.v1.board_pb2'})
_sym_db.RegisterMessage(GetGPIOResponse)
SetPWMRequest = _reflection.GeneratedProtocolMessageType('SetPWMRequest', (_message.Message,), {'DESCRIPTOR': _SETPWMREQUEST, '__module__': 'proto.api.component.board.v1.board_pb2'})
_sym_db.RegisterMessage(SetPWMRequest)
SetPWMResponse = _reflection.GeneratedProtocolMessageType('SetPWMResponse', (_message.Message,), {'DESCRIPTOR': _SETPWMRESPONSE, '__module__': 'proto.api.component.board.v1.board_pb2'})
_sym_db.RegisterMessage(SetPWMResponse)
SetPWMFrequencyResponse = _reflection.GeneratedProtocolMessageType('SetPWMFrequencyResponse', (_message.Message,), {'DESCRIPTOR': _SETPWMFREQUENCYRESPONSE, '__module__': 'proto.api.component.board.v1.board_pb2'})
_sym_db.RegisterMessage(SetPWMFrequencyResponse)
SetPWMFrequencyRequest = _reflection.GeneratedProtocolMessageType('SetPWMFrequencyRequest', (_message.Message,), {'DESCRIPTOR': _SETPWMFREQUENCYREQUEST, '__module__': 'proto.api.component.board.v1.board_pb2'})
_sym_db.RegisterMessage(SetPWMFrequencyRequest)
ReadAnalogReaderRequest = _reflection.GeneratedProtocolMessageType('ReadAnalogReaderRequest', (_message.Message,), {'DESCRIPTOR': _READANALOGREADERREQUEST, '__module__': 'proto.api.component.board.v1.board_pb2'})
_sym_db.RegisterMessage(ReadAnalogReaderRequest)
ReadAnalogReaderResponse = _reflection.GeneratedProtocolMessageType('ReadAnalogReaderResponse', (_message.Message,), {'DESCRIPTOR': _READANALOGREADERRESPONSE, '__module__': 'proto.api.component.board.v1.board_pb2'})
_sym_db.RegisterMessage(ReadAnalogReaderResponse)
GetDigitalInterruptValueRequest = _reflection.GeneratedProtocolMessageType('GetDigitalInterruptValueRequest', (_message.Message,), {'DESCRIPTOR': _GETDIGITALINTERRUPTVALUEREQUEST, '__module__': 'proto.api.component.board.v1.board_pb2'})
_sym_db.RegisterMessage(GetDigitalInterruptValueRequest)
GetDigitalInterruptValueResponse = _reflection.GeneratedProtocolMessageType('GetDigitalInterruptValueResponse', (_message.Message,), {'DESCRIPTOR': _GETDIGITALINTERRUPTVALUERESPONSE, '__module__': 'proto.api.component.board.v1.board_pb2'})
_sym_db.RegisterMessage(GetDigitalInterruptValueResponse)
_BOARDSERVICE = DESCRIPTOR.services_by_name['BoardService']
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n)com.viam.rdk.proto.api.component.board.v1Z,go.viam.com/rdk/proto/api/component/board/v1'
    _BOARDSERVICE.methods_by_name['Status']._options = None
    _BOARDSERVICE.methods_by_name['Status']._serialized_options = b"\x82\xd3\xe4\x93\x02'\x12%/api/v1/component/board/{name}/status"
    _BOARDSERVICE.methods_by_name['SetGPIO']._options = None
    _BOARDSERVICE.methods_by_name['SetGPIO']._serialized_options = b"\x82\xd3\xe4\x93\x02)\x1a'/api/v1/component/board/{name}/set_gpio"
    _BOARDSERVICE.methods_by_name['GetGPIO']._options = None
    _BOARDSERVICE.methods_by_name['GetGPIO']._serialized_options = b"\x82\xd3\xe4\x93\x02)\x12'/api/v1/component/board/{name}/get_gpio"
    _BOARDSERVICE.methods_by_name['SetPWM']._options = None
    _BOARDSERVICE.methods_by_name['SetPWM']._serialized_options = b'\x82\xd3\xe4\x93\x02(\x1a&/api/v1/component/board/{name}/set_pwm'
    _BOARDSERVICE.methods_by_name['SetPWMFrequency']._options = None
    _BOARDSERVICE.methods_by_name['SetPWMFrequency']._serialized_options = b'\x82\xd3\xe4\x93\x02-\x1a+/api/v1/component/board/{name}/set_pwm_freq'
    _BOARDSERVICE.methods_by_name['ReadAnalogReader']._options = None
    _BOARDSERVICE.methods_by_name['ReadAnalogReader']._serialized_options = b'\x82\xd3\xe4\x93\x02N\x12L/api/v1/component/board/{board_name}/analog_reader/{analog_reader_name}/read'
    _BOARDSERVICE.methods_by_name['GetDigitalInterruptValue']._options = None
    _BOARDSERVICE.methods_by_name['GetDigitalInterruptValue']._serialized_options = b'\x82\xd3\xe4\x93\x02W\x12U/api/v1/component/board/{board_name}/digital_interrupt/{digital_interrupt_name}/value'
    _STATUSREQUEST._serialized_start = 138
    _STATUSREQUEST._serialized_end = 173
    _STATUSRESPONSE._serialized_start = 175
    _STATUSRESPONSE._serialized_end = 249
    _SETGPIOREQUEST._serialized_start = 251
    _SETGPIOREQUEST._serialized_end = 325
    _SETGPIORESPONSE._serialized_start = 327
    _SETGPIORESPONSE._serialized_end = 344
    _GETGPIOREQUEST._serialized_start = 346
    _GETGPIOREQUEST._serialized_end = 400
    _GETGPIORESPONSE._serialized_start = 402
    _GETGPIORESPONSE._serialized_end = 439
    _SETPWMREQUEST._serialized_start = 441
    _SETPWMREQUEST._serialized_end = 532
    _SETPWMRESPONSE._serialized_start = 534
    _SETPWMRESPONSE._serialized_end = 550
    _SETPWMFREQUENCYRESPONSE._serialized_start = 552
    _SETPWMFREQUENCYRESPONSE._serialized_end = 577
    _SETPWMFREQUENCYREQUEST._serialized_start = 579
    _SETPWMFREQUENCYREQUEST._serialized_end = 676
    _READANALOGREADERREQUEST._serialized_start = 678
    _READANALOGREADERREQUEST._serialized_end = 780
    _READANALOGREADERRESPONSE._serialized_start = 782
    _READANALOGREADERRESPONSE._serialized_end = 830
    _GETDIGITALINTERRUPTVALUEREQUEST._serialized_start = 832
    _GETDIGITALINTERRUPTVALUEREQUEST._serialized_end = 950
    _GETDIGITALINTERRUPTVALUERESPONSE._serialized_start = 952
    _GETDIGITALINTERRUPTVALUERESPONSE._serialized_end = 1008
    _BOARDSERVICE._serialized_start = 1011
    _BOARDSERVICE._serialized_end = 2283