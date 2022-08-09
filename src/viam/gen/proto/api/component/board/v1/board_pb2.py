"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from ......proto.api.common.v1 import common_pb2 as proto_dot_api_dot_common_dot_v1_dot_common__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(proto/api/component/board/v1/board.proto\x12\x1cproto.api.component.board.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a proto/api/common/v1/common.proto"R\n\rStatusRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"J\n\x0eStatusResponse\x128\n\x06status\x18\x01 \x01(\x0b2 .proto.api.common.v1.BoardStatusR\x06status"y\n\x0eSetGPIORequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x10\n\x03pin\x18\x02 \x01(\tR\x03pin\x12\x12\n\x04high\x18\x03 \x01(\x08R\x04high\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"\x11\n\x0fSetGPIOResponse"e\n\x0eGetGPIORequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x10\n\x03pin\x18\x02 \x01(\tR\x03pin\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"%\n\x0fGetGPIOResponse\x12\x12\n\x04high\x18\x01 \x01(\x08R\x04high"a\n\nPWMRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x10\n\x03pin\x18\x02 \x01(\tR\x03pin\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"3\n\x0bPWMResponse\x12$\n\x0eduty_cycle_pct\x18\x01 \x01(\x01R\x0cdutyCyclePct"\x8a\x01\n\rSetPWMRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x10\n\x03pin\x18\x02 \x01(\tR\x03pin\x12$\n\x0eduty_cycle_pct\x18\x03 \x01(\x01R\x0cdutyCyclePct\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"\x10\n\x0eSetPWMResponse"j\n\x13PWMFrequencyRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x10\n\x03pin\x18\x02 \x01(\tR\x03pin\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"9\n\x14PWMFrequencyResponse\x12!\n\x0cfrequency_hz\x18\x01 \x01(\x04R\x0bfrequencyHz"\x90\x01\n\x16SetPWMFrequencyRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x10\n\x03pin\x18\x02 \x01(\tR\x03pin\x12!\n\x0cfrequency_hz\x18\x03 \x01(\x04R\x0bfrequencyHz\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"\x19\n\x17SetPWMFrequencyResponse"\x95\x01\n\x17ReadAnalogReaderRequest\x12\x1d\n\nboard_name\x18\x01 \x01(\tR\tboardName\x12,\n\x12analog_reader_name\x18\x02 \x01(\tR\x10analogReaderName\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"0\n\x18ReadAnalogReaderResponse\x12\x14\n\x05value\x18\x01 \x01(\x05R\x05value"\xa5\x01\n\x1fGetDigitalInterruptValueRequest\x12\x1d\n\nboard_name\x18\x01 \x01(\tR\tboardName\x124\n\x16digital_interrupt_name\x18\x02 \x01(\tR\x14digitalInterruptName\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"8\n GetDigitalInterruptValueResponse\x12\x14\n\x05value\x18\x01 \x01(\x03R\x05value2\xc7\x0c\n\x0cBoardService\x12\x97\x01\n\x06Status\x12+.proto.api.component.board.v1.StatusRequest\x1a,.proto.api.component.board.v1.StatusResponse"2\x82\xd3\xe4\x93\x02,\x12*/viam/api/v1/component/board/{name}/status\x12\x98\x01\n\x07SetGPIO\x12,.proto.api.component.board.v1.SetGPIORequest\x1a-.proto.api.component.board.v1.SetGPIOResponse"0\x82\xd3\xe4\x93\x02*\x1a(/viam/api/v1/component/board/{name}/gpio\x12\x98\x01\n\x07GetGPIO\x12,.proto.api.component.board.v1.GetGPIORequest\x1a-.proto.api.component.board.v1.GetGPIOResponse"0\x82\xd3\xe4\x93\x02*\x12(/viam/api/v1/component/board/{name}/gpio\x12\x8b\x01\n\x03PWM\x12(.proto.api.component.board.v1.PWMRequest\x1a).proto.api.component.board.v1.PWMResponse"/\x82\xd3\xe4\x93\x02)\x12\'/viam/api/v1/component/board/{name}/pwm\x12\x94\x01\n\x06SetPWM\x12+.proto.api.component.board.v1.SetPWMRequest\x1a,.proto.api.component.board.v1.SetPWMResponse"/\x82\xd3\xe4\x93\x02)\x1a\'/viam/api/v1/component/board/{name}/pwm\x12\xab\x01\n\x0cPWMFrequency\x121.proto.api.component.board.v1.PWMFrequencyRequest\x1a2.proto.api.component.board.v1.PWMFrequencyResponse"4\x82\xd3\xe4\x93\x02.\x12,/viam/api/v1/component/board/{name}/pwm_freq\x12\xb4\x01\n\x0fSetPWMFrequency\x124.proto.api.component.board.v1.SetPWMFrequencyRequest\x1a5.proto.api.component.board.v1.SetPWMFrequencyResponse"4\x82\xd3\xe4\x93\x02.\x1a,/viam/api/v1/component/board/{name}/pwm_freq\x12\xdc\x01\n\x10ReadAnalogReader\x125.proto.api.component.board.v1.ReadAnalogReaderRequest\x1a6.proto.api.component.board.v1.ReadAnalogReaderResponse"Y\x82\xd3\xe4\x93\x02S\x12Q/viam/api/v1/component/board/{board_name}/analog_reader/{analog_reader_name}/read\x12\xfd\x01\n\x18GetDigitalInterruptValue\x12=.proto.api.component.board.v1.GetDigitalInterruptValueRequest\x1a>.proto.api.component.board.v1.GetDigitalInterruptValueResponse"b\x82\xd3\xe4\x93\x02\\\x12Z/viam/api/v1/component/board/{board_name}/digital_interrupt/{digital_interrupt_name}/valueBY\n)com.viam.rdk.proto.api.component.board.v1Z,go.viam.com/rdk/proto/api/component/board/v1b\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'proto.api.component.board.v1.board_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n)com.viam.rdk.proto.api.component.board.v1Z,go.viam.com/rdk/proto/api/component/board/v1'
    _BOARDSERVICE.methods_by_name['Status']._options = None
    _BOARDSERVICE.methods_by_name['Status']._serialized_options = b'\x82\xd3\xe4\x93\x02,\x12*/viam/api/v1/component/board/{name}/status'
    _BOARDSERVICE.methods_by_name['SetGPIO']._options = None
    _BOARDSERVICE.methods_by_name['SetGPIO']._serialized_options = b'\x82\xd3\xe4\x93\x02*\x1a(/viam/api/v1/component/board/{name}/gpio'
    _BOARDSERVICE.methods_by_name['GetGPIO']._options = None
    _BOARDSERVICE.methods_by_name['GetGPIO']._serialized_options = b'\x82\xd3\xe4\x93\x02*\x12(/viam/api/v1/component/board/{name}/gpio'
    _BOARDSERVICE.methods_by_name['PWM']._options = None
    _BOARDSERVICE.methods_by_name['PWM']._serialized_options = b"\x82\xd3\xe4\x93\x02)\x12'/viam/api/v1/component/board/{name}/pwm"
    _BOARDSERVICE.methods_by_name['SetPWM']._options = None
    _BOARDSERVICE.methods_by_name['SetPWM']._serialized_options = b"\x82\xd3\xe4\x93\x02)\x1a'/viam/api/v1/component/board/{name}/pwm"
    _BOARDSERVICE.methods_by_name['PWMFrequency']._options = None
    _BOARDSERVICE.methods_by_name['PWMFrequency']._serialized_options = b'\x82\xd3\xe4\x93\x02.\x12,/viam/api/v1/component/board/{name}/pwm_freq'
    _BOARDSERVICE.methods_by_name['SetPWMFrequency']._options = None
    _BOARDSERVICE.methods_by_name['SetPWMFrequency']._serialized_options = b'\x82\xd3\xe4\x93\x02.\x1a,/viam/api/v1/component/board/{name}/pwm_freq'
    _BOARDSERVICE.methods_by_name['ReadAnalogReader']._options = None
    _BOARDSERVICE.methods_by_name['ReadAnalogReader']._serialized_options = b'\x82\xd3\xe4\x93\x02S\x12Q/viam/api/v1/component/board/{board_name}/analog_reader/{analog_reader_name}/read'
    _BOARDSERVICE.methods_by_name['GetDigitalInterruptValue']._options = None
    _BOARDSERVICE.methods_by_name['GetDigitalInterruptValue']._serialized_options = b'\x82\xd3\xe4\x93\x02\\\x12Z/viam/api/v1/component/board/{board_name}/digital_interrupt/{digital_interrupt_name}/value'
    _STATUSREQUEST._serialized_start = 168
    _STATUSREQUEST._serialized_end = 250
    _STATUSRESPONSE._serialized_start = 252
    _STATUSRESPONSE._serialized_end = 326
    _SETGPIOREQUEST._serialized_start = 328
    _SETGPIOREQUEST._serialized_end = 449
    _SETGPIORESPONSE._serialized_start = 451
    _SETGPIORESPONSE._serialized_end = 468
    _GETGPIOREQUEST._serialized_start = 470
    _GETGPIOREQUEST._serialized_end = 571
    _GETGPIORESPONSE._serialized_start = 573
    _GETGPIORESPONSE._serialized_end = 610
    _PWMREQUEST._serialized_start = 612
    _PWMREQUEST._serialized_end = 709
    _PWMRESPONSE._serialized_start = 711
    _PWMRESPONSE._serialized_end = 762
    _SETPWMREQUEST._serialized_start = 765
    _SETPWMREQUEST._serialized_end = 903
    _SETPWMRESPONSE._serialized_start = 905
    _SETPWMRESPONSE._serialized_end = 921
    _PWMFREQUENCYREQUEST._serialized_start = 923
    _PWMFREQUENCYREQUEST._serialized_end = 1029
    _PWMFREQUENCYRESPONSE._serialized_start = 1031
    _PWMFREQUENCYRESPONSE._serialized_end = 1088
    _SETPWMFREQUENCYREQUEST._serialized_start = 1091
    _SETPWMFREQUENCYREQUEST._serialized_end = 1235
    _SETPWMFREQUENCYRESPONSE._serialized_start = 1237
    _SETPWMFREQUENCYRESPONSE._serialized_end = 1262
    _READANALOGREADERREQUEST._serialized_start = 1265
    _READANALOGREADERREQUEST._serialized_end = 1414
    _READANALOGREADERRESPONSE._serialized_start = 1416
    _READANALOGREADERRESPONSE._serialized_end = 1464
    _GETDIGITALINTERRUPTVALUEREQUEST._serialized_start = 1467
    _GETDIGITALINTERRUPTVALUEREQUEST._serialized_end = 1632
    _GETDIGITALINTERRUPTVALUERESPONSE._serialized_start = 1634
    _GETDIGITALINTERRUPTVALUERESPONSE._serialized_end = 1690
    _BOARDSERVICE._serialized_start = 1693
    _BOARDSERVICE._serialized_end = 3300