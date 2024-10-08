"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....common.v1 import common_pb2 as common_dot_v1_dot_common__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*component/powersensor/v1/powersensor.proto\x12\x1dviam.component.powersensor.v1\x1a\x16common/v1/common.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1cgoogle/protobuf/struct.proto"V\n\x11GetVoltageRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"?\n\x12GetVoltageResponse\x12\x14\n\x05volts\x18\x01 \x01(\x01R\x05volts\x12\x13\n\x05is_ac\x18\x02 \x01(\x08R\x04isAc"V\n\x11GetCurrentRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"C\n\x12GetCurrentResponse\x12\x18\n\x07amperes\x18\x01 \x01(\x01R\x07amperes\x12\x13\n\x05is_ac\x18\x02 \x01(\x08R\x04isAc"T\n\x0fGetPowerRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"(\n\x10GetPowerResponse\x12\x14\n\x05watts\x18\x01 \x01(\x01R\x05watts2\xc4\x06\n\x12PowerSensorService\x12\xad\x01\n\nGetVoltage\x120.viam.component.powersensor.v1.GetVoltageRequest\x1a1.viam.component.powersensor.v1.GetVoltageResponse":\x82\xd3\xe4\x93\x024\x122/viam/api/v1/component/power_sensor/{name}/voltage\x12\xad\x01\n\nGetCurrent\x120.viam.component.powersensor.v1.GetCurrentRequest\x1a1.viam.component.powersensor.v1.GetCurrentResponse":\x82\xd3\xe4\x93\x024\x122/viam/api/v1/component/power_sensor/{name}/current\x12\xa5\x01\n\x08GetPower\x12..viam.component.powersensor.v1.GetPowerRequest\x1a/.viam.component.powersensor.v1.GetPowerResponse"8\x82\xd3\xe4\x93\x022\x120/viam/api/v1/component/power_sensor/{name}/power\x12\x93\x01\n\x0bGetReadings\x12".viam.common.v1.GetReadingsRequest\x1a#.viam.common.v1.GetReadingsResponse";\x82\xd3\xe4\x93\x025\x123/viam/api/v1/component/power_sensor/{name}/readings\x12\x8f\x01\n\tDoCommand\x12 .viam.common.v1.DoCommandRequest\x1a!.viam.common.v1.DoCommandResponse"=\x82\xd3\xe4\x93\x027"5/viam/api/v1/component/power_sensor/{name}/do_commandBM\n!com.viam.component.powersensor.v1Z(go.viam.com/api/component/powersensor/v1b\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'component.powersensor.v1.powersensor_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n!com.viam.component.powersensor.v1Z(go.viam.com/api/component/powersensor/v1'
    _POWERSENSORSERVICE.methods_by_name['GetVoltage']._options = None
    _POWERSENSORSERVICE.methods_by_name['GetVoltage']._serialized_options = b'\x82\xd3\xe4\x93\x024\x122/viam/api/v1/component/power_sensor/{name}/voltage'
    _POWERSENSORSERVICE.methods_by_name['GetCurrent']._options = None
    _POWERSENSORSERVICE.methods_by_name['GetCurrent']._serialized_options = b'\x82\xd3\xe4\x93\x024\x122/viam/api/v1/component/power_sensor/{name}/current'
    _POWERSENSORSERVICE.methods_by_name['GetPower']._options = None
    _POWERSENSORSERVICE.methods_by_name['GetPower']._serialized_options = b'\x82\xd3\xe4\x93\x022\x120/viam/api/v1/component/power_sensor/{name}/power'
    _POWERSENSORSERVICE.methods_by_name['GetReadings']._options = None
    _POWERSENSORSERVICE.methods_by_name['GetReadings']._serialized_options = b'\x82\xd3\xe4\x93\x025\x123/viam/api/v1/component/power_sensor/{name}/readings'
    _POWERSENSORSERVICE.methods_by_name['DoCommand']._options = None
    _POWERSENSORSERVICE.methods_by_name['DoCommand']._serialized_options = b'\x82\xd3\xe4\x93\x027"5/viam/api/v1/component/power_sensor/{name}/do_command'
    _GETVOLTAGEREQUEST._serialized_start = 161
    _GETVOLTAGEREQUEST._serialized_end = 247
    _GETVOLTAGERESPONSE._serialized_start = 249
    _GETVOLTAGERESPONSE._serialized_end = 312
    _GETCURRENTREQUEST._serialized_start = 314
    _GETCURRENTREQUEST._serialized_end = 400
    _GETCURRENTRESPONSE._serialized_start = 402
    _GETCURRENTRESPONSE._serialized_end = 469
    _GETPOWERREQUEST._serialized_start = 471
    _GETPOWERREQUEST._serialized_end = 555
    _GETPOWERRESPONSE._serialized_start = 557
    _GETPOWERRESPONSE._serialized_end = 597
    _POWERSENSORSERVICE._serialized_start = 600
    _POWERSENSORSERVICE._serialized_end = 1436