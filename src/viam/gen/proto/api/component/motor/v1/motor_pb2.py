"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(proto/api/component/motor/v1/motor.proto\x12\x1cproto.api.component.motor.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x1cgoogle/protobuf/struct.proto"q\n\x0fSetPowerRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x1b\n\tpower_pct\x18\x02 \x01(\x01R\x08powerPct\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"\x12\n\x10SetPowerResponse"\x85\x01\n\x0cGoForRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x10\n\x03rpm\x18\x02 \x01(\x01R\x03rpm\x12 \n\x0brevolutions\x18\x03 \x01(\x01R\x0brevolutions\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"\x0f\n\rGoForResponse"\x95\x01\n\x0bGoToRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x10\n\x03rpm\x18\x02 \x01(\x01R\x03rpm\x121\n\x14position_revolutions\x18\x03 \x01(\x01R\x13positionRevolutions\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"\x0e\n\x0cGoToResponse"u\n\x18ResetZeroPositionRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x16\n\x06offset\x18\x02 \x01(\x01R\x06offset\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"\x1b\n\x19ResetZeroPositionResponse"W\n\x12GetPositionRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"1\n\x13GetPositionResponse\x12\x1a\n\x08position\x18\x01 \x01(\x01R\x08position"P\n\x0bStopRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"\x0e\n\x0cStopResponse"U\n\x10IsPoweredRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"(\n\x11IsPoweredResponse\x12\x13\n\x05is_on\x18\x01 \x01(\x08R\x04isOn"Y\n\x14GetPropertiesRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"F\n\x15GetPropertiesResponse\x12-\n\x12position_reporting\x18\x01 \x01(\x08R\x11positionReporting"\x8f\x01\n\x06Status\x12\x1d\n\nis_powered\x18\x01 \x01(\x08R\tisPowered\x12-\n\x12position_reporting\x18\x02 \x01(\x08R\x11positionReporting\x12\x1a\n\x08position\x18\x03 \x01(\x01R\x08position\x12\x1b\n\tis_moving\x18\x04 \x01(\x08R\x08isMoving2\xa2\n\n\x0cMotorService\x12\x9c\x01\n\x08SetPower\x12-.proto.api.component.motor.v1.SetPowerRequest\x1a..proto.api.component.motor.v1.SetPowerResponse"1\x82\xd3\xe4\x93\x02+\x1a)/viam/api/v1/component/motor/{name}/power\x12\x94\x01\n\x05GoFor\x12*.proto.api.component.motor.v1.GoForRequest\x1a+.proto.api.component.motor.v1.GoForResponse"2\x82\xd3\xe4\x93\x02,\x1a*/viam/api/v1/component/motor/{name}/go_for\x12\x90\x01\n\x04GoTo\x12).proto.api.component.motor.v1.GoToRequest\x1a*.proto.api.component.motor.v1.GoToResponse"1\x82\xd3\xe4\x93\x02+\x1a)/viam/api/v1/component/motor/{name}/go_to\x12\xb6\x01\n\x11ResetZeroPosition\x126.proto.api.component.motor.v1.ResetZeroPositionRequest\x1a7.proto.api.component.motor.v1.ResetZeroPositionResponse"0\x82\xd3\xe4\x93\x02*\x1a(/viam/api/v1/component/motor/{name}/zero\x12\xa8\x01\n\x0bGetPosition\x120.proto.api.component.motor.v1.GetPositionRequest\x1a1.proto.api.component.motor.v1.GetPositionResponse"4\x82\xd3\xe4\x93\x02.\x12,/viam/api/v1/component/motor/{name}/position\x12\xae\x01\n\rGetProperties\x122.proto.api.component.motor.v1.GetPropertiesRequest\x1a3.proto.api.component.motor.v1.GetPropertiesResponse"4\x82\xd3\xe4\x93\x02.\x12,/viam/api/v1/component/motor/{name}/features\x12\x8f\x01\n\x04Stop\x12).proto.api.component.motor.v1.StopRequest\x1a*.proto.api.component.motor.v1.StopResponse"0\x82\xd3\xe4\x93\x02*\x1a(/viam/api/v1/component/motor/{name}/stop\x12\xa1\x01\n\tIsPowered\x12..proto.api.component.motor.v1.IsPoweredRequest\x1a/.proto.api.component.motor.v1.IsPoweredResponse"3\x82\xd3\xe4\x93\x02-\x12+/viam/api/v1/component/motor/{name}/poweredBY\n)com.viam.rdk.proto.api.component.motor.v1Z,go.viam.com/rdk/proto/api/component/motor/v1b\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'proto.api.component.motor.v1.motor_pb2', globals())
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
    _MOTORSERVICE.methods_by_name['GetProperties']._options = None
    _MOTORSERVICE.methods_by_name['GetProperties']._serialized_options = b'\x82\xd3\xe4\x93\x02.\x12,/viam/api/v1/component/motor/{name}/features'
    _MOTORSERVICE.methods_by_name['Stop']._options = None
    _MOTORSERVICE.methods_by_name['Stop']._serialized_options = b'\x82\xd3\xe4\x93\x02*\x1a(/viam/api/v1/component/motor/{name}/stop'
    _MOTORSERVICE.methods_by_name['IsPowered']._options = None
    _MOTORSERVICE.methods_by_name['IsPowered']._serialized_options = b'\x82\xd3\xe4\x93\x02-\x12+/viam/api/v1/component/motor/{name}/powered'
    _SETPOWERREQUEST._serialized_start = 134
    _SETPOWERREQUEST._serialized_end = 247
    _SETPOWERRESPONSE._serialized_start = 249
    _SETPOWERRESPONSE._serialized_end = 267
    _GOFORREQUEST._serialized_start = 270
    _GOFORREQUEST._serialized_end = 403
    _GOFORRESPONSE._serialized_start = 405
    _GOFORRESPONSE._serialized_end = 420
    _GOTOREQUEST._serialized_start = 423
    _GOTOREQUEST._serialized_end = 572
    _GOTORESPONSE._serialized_start = 574
    _GOTORESPONSE._serialized_end = 588
    _RESETZEROPOSITIONREQUEST._serialized_start = 590
    _RESETZEROPOSITIONREQUEST._serialized_end = 707
    _RESETZEROPOSITIONRESPONSE._serialized_start = 709
    _RESETZEROPOSITIONRESPONSE._serialized_end = 736
    _GETPOSITIONREQUEST._serialized_start = 738
    _GETPOSITIONREQUEST._serialized_end = 825
    _GETPOSITIONRESPONSE._serialized_start = 827
    _GETPOSITIONRESPONSE._serialized_end = 876
    _STOPREQUEST._serialized_start = 878
    _STOPREQUEST._serialized_end = 958
    _STOPRESPONSE._serialized_start = 960
    _STOPRESPONSE._serialized_end = 974
    _ISPOWEREDREQUEST._serialized_start = 976
    _ISPOWEREDREQUEST._serialized_end = 1061
    _ISPOWEREDRESPONSE._serialized_start = 1063
    _ISPOWEREDRESPONSE._serialized_end = 1103
    _GETPROPERTIESREQUEST._serialized_start = 1105
    _GETPROPERTIESREQUEST._serialized_end = 1194
    _GETPROPERTIESRESPONSE._serialized_start = 1196
    _GETPROPERTIESRESPONSE._serialized_end = 1266
    _STATUS._serialized_start = 1269
    _STATUS._serialized_end = 1412
    _MOTORSERVICE._serialized_start = 1415
    _MOTORSERVICE._serialized_end = 2729