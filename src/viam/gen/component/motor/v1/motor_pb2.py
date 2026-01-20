"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....common.v1 import common_pb2 as common_dot_v1_dot_common__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1ecomponent/motor/v1/motor.proto\x12\x17viam.component.motor.v1\x1a\x16common/v1/common.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1cgoogle/protobuf/struct.proto"q\n\x0fSetPowerRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x1b\n\tpower_pct\x18\x02 \x01(\x01R\x08powerPct\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"\x12\n\x10SetPowerResponse"\x85\x01\n\x0cGoForRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x10\n\x03rpm\x18\x02 \x01(\x01R\x03rpm\x12 \n\x0brevolutions\x18\x03 \x01(\x01R\x0brevolutions\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"\x0f\n\rGoForResponse"\x95\x01\n\x0bGoToRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x10\n\x03rpm\x18\x02 \x01(\x01R\x03rpm\x121\n\x14position_revolutions\x18\x03 \x01(\x01R\x13positionRevolutions\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"\x0e\n\x0cGoToResponse"d\n\rSetRPMRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x10\n\x03rpm\x18\x02 \x01(\x01R\x03rpm\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"\x10\n\x0eSetRPMResponse"u\n\x18ResetZeroPositionRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x16\n\x06offset\x18\x02 \x01(\x01R\x06offset\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"\x1b\n\x19ResetZeroPositionResponse"W\n\x12GetPositionRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"1\n\x13GetPositionResponse\x12\x1a\n\x08position\x18\x01 \x01(\x01R\x08position"P\n\x0bStopRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"\x0e\n\x0cStopResponse"U\n\x10IsPoweredRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"E\n\x11IsPoweredResponse\x12\x13\n\x05is_on\x18\x01 \x01(\x08R\x04isOn\x12\x1b\n\tpower_pct\x18\x02 \x01(\x01R\x08powerPct"Y\n\x14GetPropertiesRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"F\n\x15GetPropertiesResponse\x12-\n\x12position_reporting\x18\x01 \x01(\x08R\x11positionReporting"`\n\x06Status\x12\x1d\n\nis_powered\x18\x01 \x01(\x08R\tisPowered\x12\x1a\n\x08position\x18\x03 \x01(\x01R\x08position\x12\x1b\n\tis_moving\x18\x04 \x01(\x08R\x08isMoving"%\n\x0fIsMovingRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name"/\n\x10IsMovingResponse\x12\x1b\n\tis_moving\x18\x01 \x01(\x08R\x08isMoving2\xae\x0e\n\x0cMotorService\x12\x96\x01\n\x08SetPower\x12(.viam.component.motor.v1.SetPowerRequest\x1a).viam.component.motor.v1.SetPowerResponse"5\xa0\x92)\x01\x82\xd3\xe4\x93\x02+\x1a)/viam/api/v1/component/motor/{name}/power\x12\x8e\x01\n\x05GoFor\x12%.viam.component.motor.v1.GoForRequest\x1a&.viam.component.motor.v1.GoForResponse"6\xa0\x92)\x01\x82\xd3\xe4\x93\x02,\x1a*/viam/api/v1/component/motor/{name}/go_for\x12\x8a\x01\n\x04GoTo\x12$.viam.component.motor.v1.GoToRequest\x1a%.viam.component.motor.v1.GoToResponse"5\xa0\x92)\x01\x82\xd3\xe4\x93\x02+\x1a)/viam/api/v1/component/motor/{name}/go_to\x12\x92\x01\n\x06SetRPM\x12&.viam.component.motor.v1.SetRPMRequest\x1a\'.viam.component.motor.v1.SetRPMResponse"7\xa0\x92)\x01\x82\xd3\xe4\x93\x02-\x1a+/viam/api/v1/component/motor/{name}/set_rpm\x12\xac\x01\n\x11ResetZeroPosition\x121.viam.component.motor.v1.ResetZeroPositionRequest\x1a2.viam.component.motor.v1.ResetZeroPositionResponse"0\x82\xd3\xe4\x93\x02*\x1a(/viam/api/v1/component/motor/{name}/zero\x12\x9e\x01\n\x0bGetPosition\x12+.viam.component.motor.v1.GetPositionRequest\x1a,.viam.component.motor.v1.GetPositionResponse"4\x82\xd3\xe4\x93\x02.\x12,/viam/api/v1/component/motor/{name}/position\x12\xa4\x01\n\rGetProperties\x12-.viam.component.motor.v1.GetPropertiesRequest\x1a..viam.component.motor.v1.GetPropertiesResponse"4\x82\xd3\xe4\x93\x02.\x12,/viam/api/v1/component/motor/{name}/features\x12\x85\x01\n\x04Stop\x12$.viam.component.motor.v1.StopRequest\x1a%.viam.component.motor.v1.StopResponse"0\x82\xd3\xe4\x93\x02*\x1a(/viam/api/v1/component/motor/{name}/stop\x12\x97\x01\n\tIsPowered\x12).viam.component.motor.v1.IsPoweredRequest\x1a*.viam.component.motor.v1.IsPoweredResponse"3\x82\xd3\xe4\x93\x02-\x12+/viam/api/v1/component/motor/{name}/powered\x12\x96\x01\n\x08IsMoving\x12(.viam.component.motor.v1.IsMovingRequest\x1a).viam.component.motor.v1.IsMovingResponse"5\x82\xd3\xe4\x93\x02/\x12-/viam/api/v1/component/motor/{name}/is_moving\x12\x88\x01\n\tDoCommand\x12 .viam.common.v1.DoCommandRequest\x1a!.viam.common.v1.DoCommandResponse"6\x82\xd3\xe4\x93\x020"./viam/api/v1/component/motor/{name}/do_command\x12\x94\x01\n\rGetGeometries\x12$.viam.common.v1.GetGeometriesRequest\x1a%.viam.common.v1.GetGeometriesResponse"6\x82\xd3\xe4\x93\x020\x12./viam/api/v1/component/motor/{name}/geometriesBA\n\x1bcom.viam.component.motor.v1Z"go.viam.com/api/component/motor/v1b\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'component.motor.v1.motor_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n\x1bcom.viam.component.motor.v1Z"go.viam.com/api/component/motor/v1'
    _MOTORSERVICE.methods_by_name['SetPower']._options = None
    _MOTORSERVICE.methods_by_name['SetPower']._serialized_options = b'\xa0\x92)\x01\x82\xd3\xe4\x93\x02+\x1a)/viam/api/v1/component/motor/{name}/power'
    _MOTORSERVICE.methods_by_name['GoFor']._options = None
    _MOTORSERVICE.methods_by_name['GoFor']._serialized_options = b'\xa0\x92)\x01\x82\xd3\xe4\x93\x02,\x1a*/viam/api/v1/component/motor/{name}/go_for'
    _MOTORSERVICE.methods_by_name['GoTo']._options = None
    _MOTORSERVICE.methods_by_name['GoTo']._serialized_options = b'\xa0\x92)\x01\x82\xd3\xe4\x93\x02+\x1a)/viam/api/v1/component/motor/{name}/go_to'
    _MOTORSERVICE.methods_by_name['SetRPM']._options = None
    _MOTORSERVICE.methods_by_name['SetRPM']._serialized_options = b'\xa0\x92)\x01\x82\xd3\xe4\x93\x02-\x1a+/viam/api/v1/component/motor/{name}/set_rpm'
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
    _MOTORSERVICE.methods_by_name['IsMoving']._options = None
    _MOTORSERVICE.methods_by_name['IsMoving']._serialized_options = b'\x82\xd3\xe4\x93\x02/\x12-/viam/api/v1/component/motor/{name}/is_moving'
    _MOTORSERVICE.methods_by_name['DoCommand']._options = None
    _MOTORSERVICE.methods_by_name['DoCommand']._serialized_options = b'\x82\xd3\xe4\x93\x020"./viam/api/v1/component/motor/{name}/do_command'
    _MOTORSERVICE.methods_by_name['GetGeometries']._options = None
    _MOTORSERVICE.methods_by_name['GetGeometries']._serialized_options = b'\x82\xd3\xe4\x93\x020\x12./viam/api/v1/component/motor/{name}/geometries'
    _SETPOWERREQUEST._serialized_start = 143
    _SETPOWERREQUEST._serialized_end = 256
    _SETPOWERRESPONSE._serialized_start = 258
    _SETPOWERRESPONSE._serialized_end = 276
    _GOFORREQUEST._serialized_start = 279
    _GOFORREQUEST._serialized_end = 412
    _GOFORRESPONSE._serialized_start = 414
    _GOFORRESPONSE._serialized_end = 429
    _GOTOREQUEST._serialized_start = 432
    _GOTOREQUEST._serialized_end = 581
    _GOTORESPONSE._serialized_start = 583
    _GOTORESPONSE._serialized_end = 597
    _SETRPMREQUEST._serialized_start = 599
    _SETRPMREQUEST._serialized_end = 699
    _SETRPMRESPONSE._serialized_start = 701
    _SETRPMRESPONSE._serialized_end = 717
    _RESETZEROPOSITIONREQUEST._serialized_start = 719
    _RESETZEROPOSITIONREQUEST._serialized_end = 836
    _RESETZEROPOSITIONRESPONSE._serialized_start = 838
    _RESETZEROPOSITIONRESPONSE._serialized_end = 865
    _GETPOSITIONREQUEST._serialized_start = 867
    _GETPOSITIONREQUEST._serialized_end = 954
    _GETPOSITIONRESPONSE._serialized_start = 956
    _GETPOSITIONRESPONSE._serialized_end = 1005
    _STOPREQUEST._serialized_start = 1007
    _STOPREQUEST._serialized_end = 1087
    _STOPRESPONSE._serialized_start = 1089
    _STOPRESPONSE._serialized_end = 1103
    _ISPOWEREDREQUEST._serialized_start = 1105
    _ISPOWEREDREQUEST._serialized_end = 1190
    _ISPOWEREDRESPONSE._serialized_start = 1192
    _ISPOWEREDRESPONSE._serialized_end = 1261
    _GETPROPERTIESREQUEST._serialized_start = 1263
    _GETPROPERTIESREQUEST._serialized_end = 1352
    _GETPROPERTIESRESPONSE._serialized_start = 1354
    _GETPROPERTIESRESPONSE._serialized_end = 1424
    _STATUS._serialized_start = 1426
    _STATUS._serialized_end = 1522
    _ISMOVINGREQUEST._serialized_start = 1524
    _ISMOVINGREQUEST._serialized_end = 1561
    _ISMOVINGRESPONSE._serialized_start = 1563
    _ISMOVINGRESPONSE._serialized_end = 1610
    _MOTORSERVICE._serialized_start = 1613
    _MOTORSERVICE._serialized_end = 3451