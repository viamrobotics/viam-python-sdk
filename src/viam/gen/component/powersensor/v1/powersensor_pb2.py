"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 2, '', 'component/powersensor/v1/powersensor.proto')
_sym_db = _symbol_database.Default()
from ....common.v1 import common_pb2 as common_dot_v1_dot_common__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*component/powersensor/v1/powersensor.proto\x12\x1dviam.component.powersensor.v1\x1a\x16common/v1/common.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1cgoogle/protobuf/struct.proto"V\n\x11GetVoltageRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"?\n\x12GetVoltageResponse\x12\x14\n\x05volts\x18\x01 \x01(\x01R\x05volts\x12\x13\n\x05is_ac\x18\x02 \x01(\x08R\x04isAc"V\n\x11GetCurrentRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"C\n\x12GetCurrentResponse\x12\x18\n\x07amperes\x18\x01 \x01(\x01R\x07amperes\x12\x13\n\x05is_ac\x18\x02 \x01(\x08R\x04isAc"T\n\x0fGetPowerRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"(\n\x10GetPowerResponse\x12\x14\n\x05watts\x18\x01 \x01(\x01R\x05watts2\xc4\x06\n\x12PowerSensorService\x12\xad\x01\n\nGetVoltage\x120.viam.component.powersensor.v1.GetVoltageRequest\x1a1.viam.component.powersensor.v1.GetVoltageResponse":\x82\xd3\xe4\x93\x024\x122/viam/api/v1/component/power_sensor/{name}/voltage\x12\xad\x01\n\nGetCurrent\x120.viam.component.powersensor.v1.GetCurrentRequest\x1a1.viam.component.powersensor.v1.GetCurrentResponse":\x82\xd3\xe4\x93\x024\x122/viam/api/v1/component/power_sensor/{name}/current\x12\xa5\x01\n\x08GetPower\x12..viam.component.powersensor.v1.GetPowerRequest\x1a/.viam.component.powersensor.v1.GetPowerResponse"8\x82\xd3\xe4\x93\x022\x120/viam/api/v1/component/power_sensor/{name}/power\x12\x93\x01\n\x0bGetReadings\x12".viam.common.v1.GetReadingsRequest\x1a#.viam.common.v1.GetReadingsResponse";\x82\xd3\xe4\x93\x025\x123/viam/api/v1/component/power_sensor/{name}/readings\x12\x8f\x01\n\tDoCommand\x12 .viam.common.v1.DoCommandRequest\x1a!.viam.common.v1.DoCommandResponse"=\x82\xd3\xe4\x93\x027"5/viam/api/v1/component/power_sensor/{name}/do_commandBM\n!com.viam.component.powersensor.v1Z(go.viam.com/api/component/powersensor/v1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'component.powersensor.v1.powersensor_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n!com.viam.component.powersensor.v1Z(go.viam.com/api/component/powersensor/v1'
    _globals['_POWERSENSORSERVICE'].methods_by_name['GetVoltage']._loaded_options = None
    _globals['_POWERSENSORSERVICE'].methods_by_name['GetVoltage']._serialized_options = b'\x82\xd3\xe4\x93\x024\x122/viam/api/v1/component/power_sensor/{name}/voltage'
    _globals['_POWERSENSORSERVICE'].methods_by_name['GetCurrent']._loaded_options = None
    _globals['_POWERSENSORSERVICE'].methods_by_name['GetCurrent']._serialized_options = b'\x82\xd3\xe4\x93\x024\x122/viam/api/v1/component/power_sensor/{name}/current'
    _globals['_POWERSENSORSERVICE'].methods_by_name['GetPower']._loaded_options = None
    _globals['_POWERSENSORSERVICE'].methods_by_name['GetPower']._serialized_options = b'\x82\xd3\xe4\x93\x022\x120/viam/api/v1/component/power_sensor/{name}/power'
    _globals['_POWERSENSORSERVICE'].methods_by_name['GetReadings']._loaded_options = None
    _globals['_POWERSENSORSERVICE'].methods_by_name['GetReadings']._serialized_options = b'\x82\xd3\xe4\x93\x025\x123/viam/api/v1/component/power_sensor/{name}/readings'
    _globals['_POWERSENSORSERVICE'].methods_by_name['DoCommand']._loaded_options = None
    _globals['_POWERSENSORSERVICE'].methods_by_name['DoCommand']._serialized_options = b'\x82\xd3\xe4\x93\x027"5/viam/api/v1/component/power_sensor/{name}/do_command'
    _globals['_GETVOLTAGEREQUEST']._serialized_start = 161
    _globals['_GETVOLTAGEREQUEST']._serialized_end = 247
    _globals['_GETVOLTAGERESPONSE']._serialized_start = 249
    _globals['_GETVOLTAGERESPONSE']._serialized_end = 312
    _globals['_GETCURRENTREQUEST']._serialized_start = 314
    _globals['_GETCURRENTREQUEST']._serialized_end = 400
    _globals['_GETCURRENTRESPONSE']._serialized_start = 402
    _globals['_GETCURRENTRESPONSE']._serialized_end = 469
    _globals['_GETPOWERREQUEST']._serialized_start = 471
    _globals['_GETPOWERREQUEST']._serialized_end = 555
    _globals['_GETPOWERRESPONSE']._serialized_start = 557
    _globals['_GETPOWERRESPONSE']._serialized_end = 597
    _globals['_POWERSENSORSERVICE']._serialized_start = 600
    _globals['_POWERSENSORSERVICE']._serialized_end = 1436