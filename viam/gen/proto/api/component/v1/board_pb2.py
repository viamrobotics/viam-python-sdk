"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....proto.api.common.v1 import common_pb2 as proto_dot_api_dot_common_dot_v1_dot_common__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n"proto/api/component/v1/board.proto\x12\x16proto.api.component.v1\x1a\x1cgoogle/api/annotations.proto\x1a proto/api/common/v1/common.proto"/\n\x19BoardServiceStatusRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name"V\n\x1aBoardServiceStatusResponse\x128\n\x06status\x18\x01 \x01(\x0b2 .proto.api.common.v1.BoardStatusR\x06status"V\n\x1aBoardServiceSetGPIORequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x10\n\x03pin\x18\x02 \x01(\tR\x03pin\x12\x12\n\x04high\x18\x03 \x01(\x08R\x04high"\x1d\n\x1bBoardServiceSetGPIOResponse"B\n\x1aBoardServiceGetGPIORequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x10\n\x03pin\x18\x02 \x01(\tR\x03pin"1\n\x1bBoardServiceGetGPIOResponse\x12\x12\n\x04high\x18\x01 \x01(\x08R\x04high"g\n\x19BoardServiceSetPWMRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x10\n\x03pin\x18\x02 \x01(\tR\x03pin\x12$\n\x0eduty_cycle_pct\x18\x03 \x01(\x01R\x0cdutyCyclePct"\x1c\n\x1aBoardServiceSetPWMResponse"%\n#BoardServiceSetPWMFrequencyResponse"m\n"BoardServiceSetPWMFrequencyRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x10\n\x03pin\x18\x02 \x01(\tR\x03pin\x12!\n\x0cfrequency_hz\x18\x03 \x01(\x04R\x0bfrequencyHz"r\n#BoardServiceReadAnalogReaderRequest\x12\x1d\n\nboard_name\x18\x01 \x01(\tR\tboardName\x12,\n\x12analog_reader_name\x18\x02 \x01(\tR\x10analogReaderName"<\n$BoardServiceReadAnalogReaderResponse\x12\x14\n\x05value\x18\x01 \x01(\x05R\x05value"\x82\x01\n+BoardServiceGetDigitalInterruptValueRequest\x12\x1d\n\nboard_name\x18\x01 \x01(\tR\tboardName\x124\n\x16digital_interrupt_name\x18\x02 \x01(\tR\x14digitalInterruptName"D\n,BoardServiceGetDigitalInterruptValueResponse\x12\x14\n\x05value\x18\x01 \x01(\x03R\x05value2\xcc\n\n\x0cBoardService\x12\x9e\x01\n\x06Status\x121.proto.api.component.v1.BoardServiceStatusRequest\x1a2.proto.api.component.v1.BoardServiceStatusResponse"-\x82\xd3\xe4\x93\x02\'\x12%/api/v1/component/board/{name}/status\x12\xa3\x01\n\x07SetGPIO\x122.proto.api.component.v1.BoardServiceSetGPIORequest\x1a3.proto.api.component.v1.BoardServiceSetGPIOResponse"/\x82\xd3\xe4\x93\x02)\x1a\'/api/v1/component/board/{name}/set_gpio\x12\xa3\x01\n\x07GetGPIO\x122.proto.api.component.v1.BoardServiceGetGPIORequest\x1a3.proto.api.component.v1.BoardServiceGetGPIOResponse"/\x82\xd3\xe4\x93\x02)\x12\'/api/v1/component/board/{name}/get_gpio\x12\x9f\x01\n\x06SetPWM\x121.proto.api.component.v1.BoardServiceSetPWMRequest\x1a2.proto.api.component.v1.BoardServiceSetPWMResponse".\x82\xd3\xe4\x93\x02(\x1a&/api/v1/component/board/{name}/set_pwm\x12\xbf\x01\n\x0fSetPWMFrequency\x12:.proto.api.component.v1.BoardServiceSetPWMFrequencyRequest\x1a;.proto.api.component.v1.BoardServiceSetPWMFrequencyResponse"3\x82\xd3\xe4\x93\x02-\x1a+/api/v1/component/board/{name}/set_pwm_freq\x12\xe3\x01\n\x10ReadAnalogReader\x12;.proto.api.component.v1.BoardServiceReadAnalogReaderRequest\x1a<.proto.api.component.v1.BoardServiceReadAnalogReaderResponse"T\x82\xd3\xe4\x93\x02N\x12L/api/v1/component/board/{board_name}/analog_reader/{analog_reader_name}/read\x12\x84\x02\n\x18GetDigitalInterruptValue\x12C.proto.api.component.v1.BoardServiceGetDigitalInterruptValueRequest\x1aD.proto.api.component.v1.BoardServiceGetDigitalInterruptValueResponse"]\x82\xd3\xe4\x93\x02W\x12U/api/v1/component/board/{board_name}/digital_interrupt/{digital_interrupt_name}/valueBM\n#com.viam.rdk.proto.api.component.v1Z&go.viam.com/rdk/proto/api/component/v1b\x06proto3')
_BOARDSERVICESTATUSREQUEST = DESCRIPTOR.message_types_by_name['BoardServiceStatusRequest']
_BOARDSERVICESTATUSRESPONSE = DESCRIPTOR.message_types_by_name['BoardServiceStatusResponse']
_BOARDSERVICESETGPIOREQUEST = DESCRIPTOR.message_types_by_name['BoardServiceSetGPIORequest']
_BOARDSERVICESETGPIORESPONSE = DESCRIPTOR.message_types_by_name['BoardServiceSetGPIOResponse']
_BOARDSERVICEGETGPIOREQUEST = DESCRIPTOR.message_types_by_name['BoardServiceGetGPIORequest']
_BOARDSERVICEGETGPIORESPONSE = DESCRIPTOR.message_types_by_name['BoardServiceGetGPIOResponse']
_BOARDSERVICESETPWMREQUEST = DESCRIPTOR.message_types_by_name['BoardServiceSetPWMRequest']
_BOARDSERVICESETPWMRESPONSE = DESCRIPTOR.message_types_by_name['BoardServiceSetPWMResponse']
_BOARDSERVICESETPWMFREQUENCYRESPONSE = DESCRIPTOR.message_types_by_name['BoardServiceSetPWMFrequencyResponse']
_BOARDSERVICESETPWMFREQUENCYREQUEST = DESCRIPTOR.message_types_by_name['BoardServiceSetPWMFrequencyRequest']
_BOARDSERVICEREADANALOGREADERREQUEST = DESCRIPTOR.message_types_by_name['BoardServiceReadAnalogReaderRequest']
_BOARDSERVICEREADANALOGREADERRESPONSE = DESCRIPTOR.message_types_by_name['BoardServiceReadAnalogReaderResponse']
_BOARDSERVICEGETDIGITALINTERRUPTVALUEREQUEST = DESCRIPTOR.message_types_by_name['BoardServiceGetDigitalInterruptValueRequest']
_BOARDSERVICEGETDIGITALINTERRUPTVALUERESPONSE = DESCRIPTOR.message_types_by_name['BoardServiceGetDigitalInterruptValueResponse']
BoardServiceStatusRequest = _reflection.GeneratedProtocolMessageType('BoardServiceStatusRequest', (_message.Message,), {'DESCRIPTOR': _BOARDSERVICESTATUSREQUEST, '__module__': 'proto.api.component.v1.board_pb2'})
_sym_db.RegisterMessage(BoardServiceStatusRequest)
BoardServiceStatusResponse = _reflection.GeneratedProtocolMessageType('BoardServiceStatusResponse', (_message.Message,), {'DESCRIPTOR': _BOARDSERVICESTATUSRESPONSE, '__module__': 'proto.api.component.v1.board_pb2'})
_sym_db.RegisterMessage(BoardServiceStatusResponse)
BoardServiceSetGPIORequest = _reflection.GeneratedProtocolMessageType('BoardServiceSetGPIORequest', (_message.Message,), {'DESCRIPTOR': _BOARDSERVICESETGPIOREQUEST, '__module__': 'proto.api.component.v1.board_pb2'})
_sym_db.RegisterMessage(BoardServiceSetGPIORequest)
BoardServiceSetGPIOResponse = _reflection.GeneratedProtocolMessageType('BoardServiceSetGPIOResponse', (_message.Message,), {'DESCRIPTOR': _BOARDSERVICESETGPIORESPONSE, '__module__': 'proto.api.component.v1.board_pb2'})
_sym_db.RegisterMessage(BoardServiceSetGPIOResponse)
BoardServiceGetGPIORequest = _reflection.GeneratedProtocolMessageType('BoardServiceGetGPIORequest', (_message.Message,), {'DESCRIPTOR': _BOARDSERVICEGETGPIOREQUEST, '__module__': 'proto.api.component.v1.board_pb2'})
_sym_db.RegisterMessage(BoardServiceGetGPIORequest)
BoardServiceGetGPIOResponse = _reflection.GeneratedProtocolMessageType('BoardServiceGetGPIOResponse', (_message.Message,), {'DESCRIPTOR': _BOARDSERVICEGETGPIORESPONSE, '__module__': 'proto.api.component.v1.board_pb2'})
_sym_db.RegisterMessage(BoardServiceGetGPIOResponse)
BoardServiceSetPWMRequest = _reflection.GeneratedProtocolMessageType('BoardServiceSetPWMRequest', (_message.Message,), {'DESCRIPTOR': _BOARDSERVICESETPWMREQUEST, '__module__': 'proto.api.component.v1.board_pb2'})
_sym_db.RegisterMessage(BoardServiceSetPWMRequest)
BoardServiceSetPWMResponse = _reflection.GeneratedProtocolMessageType('BoardServiceSetPWMResponse', (_message.Message,), {'DESCRIPTOR': _BOARDSERVICESETPWMRESPONSE, '__module__': 'proto.api.component.v1.board_pb2'})
_sym_db.RegisterMessage(BoardServiceSetPWMResponse)
BoardServiceSetPWMFrequencyResponse = _reflection.GeneratedProtocolMessageType('BoardServiceSetPWMFrequencyResponse', (_message.Message,), {'DESCRIPTOR': _BOARDSERVICESETPWMFREQUENCYRESPONSE, '__module__': 'proto.api.component.v1.board_pb2'})
_sym_db.RegisterMessage(BoardServiceSetPWMFrequencyResponse)
BoardServiceSetPWMFrequencyRequest = _reflection.GeneratedProtocolMessageType('BoardServiceSetPWMFrequencyRequest', (_message.Message,), {'DESCRIPTOR': _BOARDSERVICESETPWMFREQUENCYREQUEST, '__module__': 'proto.api.component.v1.board_pb2'})
_sym_db.RegisterMessage(BoardServiceSetPWMFrequencyRequest)
BoardServiceReadAnalogReaderRequest = _reflection.GeneratedProtocolMessageType('BoardServiceReadAnalogReaderRequest', (_message.Message,), {'DESCRIPTOR': _BOARDSERVICEREADANALOGREADERREQUEST, '__module__': 'proto.api.component.v1.board_pb2'})
_sym_db.RegisterMessage(BoardServiceReadAnalogReaderRequest)
BoardServiceReadAnalogReaderResponse = _reflection.GeneratedProtocolMessageType('BoardServiceReadAnalogReaderResponse', (_message.Message,), {'DESCRIPTOR': _BOARDSERVICEREADANALOGREADERRESPONSE, '__module__': 'proto.api.component.v1.board_pb2'})
_sym_db.RegisterMessage(BoardServiceReadAnalogReaderResponse)
BoardServiceGetDigitalInterruptValueRequest = _reflection.GeneratedProtocolMessageType('BoardServiceGetDigitalInterruptValueRequest', (_message.Message,), {'DESCRIPTOR': _BOARDSERVICEGETDIGITALINTERRUPTVALUEREQUEST, '__module__': 'proto.api.component.v1.board_pb2'})
_sym_db.RegisterMessage(BoardServiceGetDigitalInterruptValueRequest)
BoardServiceGetDigitalInterruptValueResponse = _reflection.GeneratedProtocolMessageType('BoardServiceGetDigitalInterruptValueResponse', (_message.Message,), {'DESCRIPTOR': _BOARDSERVICEGETDIGITALINTERRUPTVALUERESPONSE, '__module__': 'proto.api.component.v1.board_pb2'})
_sym_db.RegisterMessage(BoardServiceGetDigitalInterruptValueResponse)
_BOARDSERVICE = DESCRIPTOR.services_by_name['BoardService']
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n#com.viam.rdk.proto.api.component.v1Z&go.viam.com/rdk/proto/api/component/v1'
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
    _BOARDSERVICESTATUSREQUEST._serialized_start = 126
    _BOARDSERVICESTATUSREQUEST._serialized_end = 173
    _BOARDSERVICESTATUSRESPONSE._serialized_start = 175
    _BOARDSERVICESTATUSRESPONSE._serialized_end = 261
    _BOARDSERVICESETGPIOREQUEST._serialized_start = 263
    _BOARDSERVICESETGPIOREQUEST._serialized_end = 349
    _BOARDSERVICESETGPIORESPONSE._serialized_start = 351
    _BOARDSERVICESETGPIORESPONSE._serialized_end = 380
    _BOARDSERVICEGETGPIOREQUEST._serialized_start = 382
    _BOARDSERVICEGETGPIOREQUEST._serialized_end = 448
    _BOARDSERVICEGETGPIORESPONSE._serialized_start = 450
    _BOARDSERVICEGETGPIORESPONSE._serialized_end = 499
    _BOARDSERVICESETPWMREQUEST._serialized_start = 501
    _BOARDSERVICESETPWMREQUEST._serialized_end = 604
    _BOARDSERVICESETPWMRESPONSE._serialized_start = 606
    _BOARDSERVICESETPWMRESPONSE._serialized_end = 634
    _BOARDSERVICESETPWMFREQUENCYRESPONSE._serialized_start = 636
    _BOARDSERVICESETPWMFREQUENCYRESPONSE._serialized_end = 673
    _BOARDSERVICESETPWMFREQUENCYREQUEST._serialized_start = 675
    _BOARDSERVICESETPWMFREQUENCYREQUEST._serialized_end = 784
    _BOARDSERVICEREADANALOGREADERREQUEST._serialized_start = 786
    _BOARDSERVICEREADANALOGREADERREQUEST._serialized_end = 900
    _BOARDSERVICEREADANALOGREADERRESPONSE._serialized_start = 902
    _BOARDSERVICEREADANALOGREADERRESPONSE._serialized_end = 962
    _BOARDSERVICEGETDIGITALINTERRUPTVALUEREQUEST._serialized_start = 965
    _BOARDSERVICEGETDIGITALINTERRUPTVALUEREQUEST._serialized_end = 1095
    _BOARDSERVICEGETDIGITALINTERRUPTVALUERESPONSE._serialized_start = 1097
    _BOARDSERVICEGETDIGITALINTERRUPTVALUERESPONSE._serialized_end = 1165
    _BOARDSERVICE._serialized_start = 1168
    _BOARDSERVICE._serialized_end = 2524