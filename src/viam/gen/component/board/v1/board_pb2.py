"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....common.v1 import common_pb2 as common_dot_v1_dot_common__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1ecomponent/board/v1/board.proto\x12\x17viam.component.board.v1\x1a\x16common/v1/common.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1cgoogle/protobuf/struct.proto"\xb9\x02\n\x06Status\x12F\n\x07analogs\x18\x01 \x03(\x0b2,.viam.component.board.v1.Status.AnalogsEntryR\x07analogs\x12e\n\x12digital_interrupts\x18\x02 \x03(\x0b26.viam.component.board.v1.Status.DigitalInterruptsEntryR\x11digitalInterrupts\x1a:\n\x0cAnalogsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\x05R\x05value:\x028\x01\x1aD\n\x16DigitalInterruptsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\x03R\x05value:\x028\x01"y\n\x0eSetGPIORequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x10\n\x03pin\x18\x02 \x01(\tR\x03pin\x12\x12\n\x04high\x18\x03 \x01(\x08R\x04high\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"\x11\n\x0fSetGPIOResponse"e\n\x0eGetGPIORequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x10\n\x03pin\x18\x02 \x01(\tR\x03pin\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"%\n\x0fGetGPIOResponse\x12\x12\n\x04high\x18\x01 \x01(\x08R\x04high"a\n\nPWMRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x10\n\x03pin\x18\x02 \x01(\tR\x03pin\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"3\n\x0bPWMResponse\x12$\n\x0eduty_cycle_pct\x18\x01 \x01(\x01R\x0cdutyCyclePct"\x8a\x01\n\rSetPWMRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x10\n\x03pin\x18\x02 \x01(\tR\x03pin\x12$\n\x0eduty_cycle_pct\x18\x03 \x01(\x01R\x0cdutyCyclePct\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"\x10\n\x0eSetPWMResponse"j\n\x13PWMFrequencyRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x10\n\x03pin\x18\x02 \x01(\tR\x03pin\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"9\n\x14PWMFrequencyResponse\x12!\n\x0cfrequency_hz\x18\x01 \x01(\x04R\x0bfrequencyHz"\x90\x01\n\x16SetPWMFrequencyRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x10\n\x03pin\x18\x02 \x01(\tR\x03pin\x12!\n\x0cfrequency_hz\x18\x03 \x01(\x04R\x0bfrequencyHz\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"\x19\n\x17SetPWMFrequencyResponse"\x95\x01\n\x17ReadAnalogReaderRequest\x12\x1d\n\nboard_name\x18\x01 \x01(\tR\tboardName\x12,\n\x12analog_reader_name\x18\x02 \x01(\tR\x10analogReaderName\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"\x87\x01\n\x18ReadAnalogReaderResponse\x12\x14\n\x05value\x18\x01 \x01(\x05R\x05value\x12\x1b\n\tmin_range\x18\x02 \x01(\x02R\x08minRange\x12\x1b\n\tmax_range\x18\x03 \x01(\x02R\x08maxRange\x12\x1b\n\tstep_size\x18\x04 \x01(\x02R\x08stepSize"\x7f\n\x12WriteAnalogRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x10\n\x03pin\x18\x02 \x01(\tR\x03pin\x12\x14\n\x05value\x18\x03 \x01(\x05R\x05value\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"\x15\n\x13WriteAnalogResponse"\xa5\x01\n\x1fGetDigitalInterruptValueRequest\x12\x1d\n\nboard_name\x18\x01 \x01(\tR\tboardName\x124\n\x16digital_interrupt_name\x18\x02 \x01(\tR\x14digitalInterruptName\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"8\n GetDigitalInterruptValueResponse\x12\x14\n\x05value\x18\x01 \x01(\x03R\x05value"t\n\x12StreamTicksRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x1b\n\tpin_names\x18\x02 \x03(\tR\x08pinNames\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"X\n\x13StreamTicksResponse\x12\x19\n\x08pin_name\x18\x01 \x01(\tR\x07pinName\x12\x12\n\x04time\x18\x02 \x01(\x04R\x04time\x12\x12\n\x04high\x18\x03 \x01(\x08R\x04high"\xe4\x01\n\x13SetPowerModeRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12A\n\npower_mode\x18\x02 \x01(\x0e2".viam.component.board.v1.PowerModeR\tpowerMode\x12:\n\x08duration\x18\x03 \x01(\x0b2\x19.google.protobuf.DurationH\x00R\x08duration\x88\x01\x01\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extraB\x0b\n\t_duration"\x16\n\x14SetPowerModeResponse*[\n\tPowerMode\x12\x1a\n\x16POWER_MODE_UNSPECIFIED\x10\x00\x12\x15\n\x11POWER_MODE_NORMAL\x10\x01\x12\x1b\n\x17POWER_MODE_OFFLINE_DEEP\x10\x022\xf0\x10\n\x0cBoardService\x12\x8e\x01\n\x07SetGPIO\x12\'.viam.component.board.v1.SetGPIORequest\x1a(.viam.component.board.v1.SetGPIOResponse"0\x82\xd3\xe4\x93\x02*\x1a(/viam/api/v1/component/board/{name}/gpio\x12\x8e\x01\n\x07GetGPIO\x12\'.viam.component.board.v1.GetGPIORequest\x1a(.viam.component.board.v1.GetGPIOResponse"0\x82\xd3\xe4\x93\x02*\x12(/viam/api/v1/component/board/{name}/gpio\x12\x81\x01\n\x03PWM\x12#.viam.component.board.v1.PWMRequest\x1a$.viam.component.board.v1.PWMResponse"/\x82\xd3\xe4\x93\x02)\x12\'/viam/api/v1/component/board/{name}/pwm\x12\x8a\x01\n\x06SetPWM\x12&.viam.component.board.v1.SetPWMRequest\x1a\'.viam.component.board.v1.SetPWMResponse"/\x82\xd3\xe4\x93\x02)\x1a\'/viam/api/v1/component/board/{name}/pwm\x12\xa1\x01\n\x0cPWMFrequency\x12,.viam.component.board.v1.PWMFrequencyRequest\x1a-.viam.component.board.v1.PWMFrequencyResponse"4\x82\xd3\xe4\x93\x02.\x12,/viam/api/v1/component/board/{name}/pwm_freq\x12\xaa\x01\n\x0fSetPWMFrequency\x12/.viam.component.board.v1.SetPWMFrequencyRequest\x1a0.viam.component.board.v1.SetPWMFrequencyResponse"4\x82\xd3\xe4\x93\x02.\x1a,/viam/api/v1/component/board/{name}/pwm_freq\x12\x88\x01\n\tDoCommand\x12 .viam.common.v1.DoCommandRequest\x1a!.viam.common.v1.DoCommandResponse"6\x82\xd3\xe4\x93\x020"./viam/api/v1/component/board/{name}/do_command\x12\xd2\x01\n\x10ReadAnalogReader\x120.viam.component.board.v1.ReadAnalogReaderRequest\x1a1.viam.component.board.v1.ReadAnalogReaderResponse"Y\x82\xd3\xe4\x93\x02S\x12Q/viam/api/v1/component/board/{board_name}/analog_reader/{analog_reader_name}/read\x12\xa2\x01\n\x0bWriteAnalog\x12+.viam.component.board.v1.WriteAnalogRequest\x1a,.viam.component.board.v1.WriteAnalogResponse"8\x82\xd3\xe4\x93\x022\x1a0/viam/api/v1/component/board/{name}/analog_write\x12\xf3\x01\n\x18GetDigitalInterruptValue\x128.viam.component.board.v1.GetDigitalInterruptValueRequest\x1a9.viam.component.board.v1.GetDigitalInterruptValueResponse"b\x82\xd3\xe4\x93\x02\\\x12Z/viam/api/v1/component/board/{board_name}/digital_interrupt/{digital_interrupt_name}/value\x12\xa3\x01\n\x0bStreamTicks\x12+.viam.component.board.v1.StreamTicksRequest\x1a,.viam.component.board.v1.StreamTicksResponse"7\x82\xd3\xe4\x93\x021\x12//viam/api/v1/component/board/{name}/tick_stream0\x01\x12\xa3\x01\n\x0cSetPowerMode\x12,.viam.component.board.v1.SetPowerModeRequest\x1a-.viam.component.board.v1.SetPowerModeResponse"6\x82\xd3\xe4\x93\x020\x1a./viam/api/v1/component/board/{name}/power_mode\x12\x94\x01\n\rGetGeometries\x12$.viam.common.v1.GetGeometriesRequest\x1a%.viam.common.v1.GetGeometriesResponse"6\x82\xd3\xe4\x93\x020\x12./viam/api/v1/component/board/{name}/geometriesBA\n\x1bcom.viam.component.board.v1Z"go.viam.com/api/component/board/v1b\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'component.board.v1.board_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n\x1bcom.viam.component.board.v1Z"go.viam.com/api/component/board/v1'
    _STATUS_ANALOGSENTRY._options = None
    _STATUS_ANALOGSENTRY._serialized_options = b'8\x01'
    _STATUS_DIGITALINTERRUPTSENTRY._options = None
    _STATUS_DIGITALINTERRUPTSENTRY._serialized_options = b'8\x01'
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
    _BOARDSERVICE.methods_by_name['DoCommand']._options = None
    _BOARDSERVICE.methods_by_name['DoCommand']._serialized_options = b'\x82\xd3\xe4\x93\x020"./viam/api/v1/component/board/{name}/do_command'
    _BOARDSERVICE.methods_by_name['ReadAnalogReader']._options = None
    _BOARDSERVICE.methods_by_name['ReadAnalogReader']._serialized_options = b'\x82\xd3\xe4\x93\x02S\x12Q/viam/api/v1/component/board/{board_name}/analog_reader/{analog_reader_name}/read'
    _BOARDSERVICE.methods_by_name['WriteAnalog']._options = None
    _BOARDSERVICE.methods_by_name['WriteAnalog']._serialized_options = b'\x82\xd3\xe4\x93\x022\x1a0/viam/api/v1/component/board/{name}/analog_write'
    _BOARDSERVICE.methods_by_name['GetDigitalInterruptValue']._options = None
    _BOARDSERVICE.methods_by_name['GetDigitalInterruptValue']._serialized_options = b'\x82\xd3\xe4\x93\x02\\\x12Z/viam/api/v1/component/board/{board_name}/digital_interrupt/{digital_interrupt_name}/value'
    _BOARDSERVICE.methods_by_name['StreamTicks']._options = None
    _BOARDSERVICE.methods_by_name['StreamTicks']._serialized_options = b'\x82\xd3\xe4\x93\x021\x12//viam/api/v1/component/board/{name}/tick_stream'
    _BOARDSERVICE.methods_by_name['SetPowerMode']._options = None
    _BOARDSERVICE.methods_by_name['SetPowerMode']._serialized_options = b'\x82\xd3\xe4\x93\x020\x1a./viam/api/v1/component/board/{name}/power_mode'
    _BOARDSERVICE.methods_by_name['GetGeometries']._options = None
    _BOARDSERVICE.methods_by_name['GetGeometries']._serialized_options = b'\x82\xd3\xe4\x93\x020\x12./viam/api/v1/component/board/{name}/geometries'
    _POWERMODE._serialized_start = 2558
    _POWERMODE._serialized_end = 2649
    _STATUS._serialized_start = 176
    _STATUS._serialized_end = 489
    _STATUS_ANALOGSENTRY._serialized_start = 361
    _STATUS_ANALOGSENTRY._serialized_end = 419
    _STATUS_DIGITALINTERRUPTSENTRY._serialized_start = 421
    _STATUS_DIGITALINTERRUPTSENTRY._serialized_end = 489
    _SETGPIOREQUEST._serialized_start = 491
    _SETGPIOREQUEST._serialized_end = 612
    _SETGPIORESPONSE._serialized_start = 614
    _SETGPIORESPONSE._serialized_end = 631
    _GETGPIOREQUEST._serialized_start = 633
    _GETGPIOREQUEST._serialized_end = 734
    _GETGPIORESPONSE._serialized_start = 736
    _GETGPIORESPONSE._serialized_end = 773
    _PWMREQUEST._serialized_start = 775
    _PWMREQUEST._serialized_end = 872
    _PWMRESPONSE._serialized_start = 874
    _PWMRESPONSE._serialized_end = 925
    _SETPWMREQUEST._serialized_start = 928
    _SETPWMREQUEST._serialized_end = 1066
    _SETPWMRESPONSE._serialized_start = 1068
    _SETPWMRESPONSE._serialized_end = 1084
    _PWMFREQUENCYREQUEST._serialized_start = 1086
    _PWMFREQUENCYREQUEST._serialized_end = 1192
    _PWMFREQUENCYRESPONSE._serialized_start = 1194
    _PWMFREQUENCYRESPONSE._serialized_end = 1251
    _SETPWMFREQUENCYREQUEST._serialized_start = 1254
    _SETPWMFREQUENCYREQUEST._serialized_end = 1398
    _SETPWMFREQUENCYRESPONSE._serialized_start = 1400
    _SETPWMFREQUENCYRESPONSE._serialized_end = 1425
    _READANALOGREADERREQUEST._serialized_start = 1428
    _READANALOGREADERREQUEST._serialized_end = 1577
    _READANALOGREADERRESPONSE._serialized_start = 1580
    _READANALOGREADERRESPONSE._serialized_end = 1715
    _WRITEANALOGREQUEST._serialized_start = 1717
    _WRITEANALOGREQUEST._serialized_end = 1844
    _WRITEANALOGRESPONSE._serialized_start = 1846
    _WRITEANALOGRESPONSE._serialized_end = 1867
    _GETDIGITALINTERRUPTVALUEREQUEST._serialized_start = 1870
    _GETDIGITALINTERRUPTVALUEREQUEST._serialized_end = 2035
    _GETDIGITALINTERRUPTVALUERESPONSE._serialized_start = 2037
    _GETDIGITALINTERRUPTVALUERESPONSE._serialized_end = 2093
    _STREAMTICKSREQUEST._serialized_start = 2095
    _STREAMTICKSREQUEST._serialized_end = 2211
    _STREAMTICKSRESPONSE._serialized_start = 2213
    _STREAMTICKSRESPONSE._serialized_end = 2301
    _SETPOWERMODEREQUEST._serialized_start = 2304
    _SETPOWERMODEREQUEST._serialized_end = 2532
    _SETPOWERMODERESPONSE._serialized_start = 2534
    _SETPOWERMODERESPONSE._serialized_end = 2556
    _BOARDSERVICE._serialized_start = 2652
    _BOARDSERVICE._serialized_end = 4812