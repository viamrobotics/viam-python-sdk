"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 2, '', 'service/sensors/v1/sensors.proto')
_sym_db = _symbol_database.Default()
from ....common.v1 import common_pb2 as common_dot_v1_dot_common__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n service/sensors/v1/sensors.proto\x12\x17viam.service.sensors.v1\x1a\x16common/v1/common.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1cgoogle/protobuf/struct.proto"b\n\x11GetSensorsRequest\x12\x16\n\x04name\x18\x01 \x01(\tB\x02\x18\x01R\x04name\x121\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructB\x02\x18\x01R\x05extra:\x02\x18\x01"]\n\x12GetSensorsResponse\x12C\n\x0csensor_names\x18\x01 \x03(\x0b2\x1c.viam.common.v1.ResourceNameB\x02\x18\x01R\x0bsensorNames:\x02\x18\x01"\xa8\x01\n\x12GetReadingsRequest\x12\x16\n\x04name\x18\x01 \x01(\tB\x02\x18\x01R\x04name\x12C\n\x0csensor_names\x18\x02 \x03(\x0b2\x1c.viam.common.v1.ResourceNameB\x02\x18\x01R\x0bsensorNames\x121\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructB\x02\x18\x01R\x05extra:\x02\x18\x01"\xea\x01\n\x08Readings\x124\n\x04name\x18\x01 \x01(\x0b2\x1c.viam.common.v1.ResourceNameB\x02\x18\x01R\x04name\x12O\n\x08readings\x18\x02 \x03(\x0b2/.viam.service.sensors.v1.Readings.ReadingsEntryB\x02\x18\x01R\x08readings\x1aS\n\rReadingsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12,\n\x05value\x18\x02 \x01(\x0b2\x16.google.protobuf.ValueR\x05value:\x028\x01:\x02\x18\x01"\\\n\x13GetReadingsResponse\x12A\n\x08readings\x18\x01 \x03(\x0b2!.viam.service.sensors.v1.ReadingsB\x02\x18\x01R\x08readings:\x02\x18\x012\xda\x03\n\x0eSensorsService\x12\x95\x01\n\nGetSensors\x12*.viam.service.sensors.v1.GetSensorsRequest\x1a+.viam.service.sensors.v1.GetSensorsResponse".\x88\x02\x01\x82\xd3\xe4\x93\x02%\x12#/viam/api/v1/service/{name}/sensors\x12\xa1\x01\n\x0bGetReadings\x12+.viam.service.sensors.v1.GetReadingsRequest\x1a,.viam.service.sensors.v1.GetReadingsResponse"7\x88\x02\x01\x82\xd3\xe4\x93\x02.\x12,/viam/api/v1/service/sensors/{name}/readings\x12\x8b\x01\n\tDoCommand\x12 .viam.common.v1.DoCommandRequest\x1a!.viam.common.v1.DoCommandResponse"9\x88\x02\x01\x82\xd3\xe4\x93\x020"./viam/api/v1/service/sensors/{name}/do_commandBD\n\x1bcom.viam.service.sensors.v1Z"go.viam.com/api/service/sensors/v1\xb8\x01\x01b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'service.sensors.v1.sensors_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1bcom.viam.service.sensors.v1Z"go.viam.com/api/service/sensors/v1\xb8\x01\x01'
    _globals['_GETSENSORSREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETSENSORSREQUEST'].fields_by_name['name']._serialized_options = b'\x18\x01'
    _globals['_GETSENSORSREQUEST'].fields_by_name['extra']._loaded_options = None
    _globals['_GETSENSORSREQUEST'].fields_by_name['extra']._serialized_options = b'\x18\x01'
    _globals['_GETSENSORSREQUEST']._loaded_options = None
    _globals['_GETSENSORSREQUEST']._serialized_options = b'\x18\x01'
    _globals['_GETSENSORSRESPONSE'].fields_by_name['sensor_names']._loaded_options = None
    _globals['_GETSENSORSRESPONSE'].fields_by_name['sensor_names']._serialized_options = b'\x18\x01'
    _globals['_GETSENSORSRESPONSE']._loaded_options = None
    _globals['_GETSENSORSRESPONSE']._serialized_options = b'\x18\x01'
    _globals['_GETREADINGSREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETREADINGSREQUEST'].fields_by_name['name']._serialized_options = b'\x18\x01'
    _globals['_GETREADINGSREQUEST'].fields_by_name['sensor_names']._loaded_options = None
    _globals['_GETREADINGSREQUEST'].fields_by_name['sensor_names']._serialized_options = b'\x18\x01'
    _globals['_GETREADINGSREQUEST'].fields_by_name['extra']._loaded_options = None
    _globals['_GETREADINGSREQUEST'].fields_by_name['extra']._serialized_options = b'\x18\x01'
    _globals['_GETREADINGSREQUEST']._loaded_options = None
    _globals['_GETREADINGSREQUEST']._serialized_options = b'\x18\x01'
    _globals['_READINGS_READINGSENTRY']._loaded_options = None
    _globals['_READINGS_READINGSENTRY']._serialized_options = b'8\x01'
    _globals['_READINGS'].fields_by_name['name']._loaded_options = None
    _globals['_READINGS'].fields_by_name['name']._serialized_options = b'\x18\x01'
    _globals['_READINGS'].fields_by_name['readings']._loaded_options = None
    _globals['_READINGS'].fields_by_name['readings']._serialized_options = b'\x18\x01'
    _globals['_READINGS']._loaded_options = None
    _globals['_READINGS']._serialized_options = b'\x18\x01'
    _globals['_GETREADINGSRESPONSE'].fields_by_name['readings']._loaded_options = None
    _globals['_GETREADINGSRESPONSE'].fields_by_name['readings']._serialized_options = b'\x18\x01'
    _globals['_GETREADINGSRESPONSE']._loaded_options = None
    _globals['_GETREADINGSRESPONSE']._serialized_options = b'\x18\x01'
    _globals['_SENSORSSERVICE'].methods_by_name['GetSensors']._loaded_options = None
    _globals['_SENSORSSERVICE'].methods_by_name['GetSensors']._serialized_options = b'\x88\x02\x01\x82\xd3\xe4\x93\x02%\x12#/viam/api/v1/service/{name}/sensors'
    _globals['_SENSORSSERVICE'].methods_by_name['GetReadings']._loaded_options = None
    _globals['_SENSORSSERVICE'].methods_by_name['GetReadings']._serialized_options = b'\x88\x02\x01\x82\xd3\xe4\x93\x02.\x12,/viam/api/v1/service/sensors/{name}/readings'
    _globals['_SENSORSSERVICE'].methods_by_name['DoCommand']._loaded_options = None
    _globals['_SENSORSSERVICE'].methods_by_name['DoCommand']._serialized_options = b'\x88\x02\x01\x82\xd3\xe4\x93\x020"./viam/api/v1/service/sensors/{name}/do_command'
    _globals['_GETSENSORSREQUEST']._serialized_start = 145
    _globals['_GETSENSORSREQUEST']._serialized_end = 243
    _globals['_GETSENSORSRESPONSE']._serialized_start = 245
    _globals['_GETSENSORSRESPONSE']._serialized_end = 338
    _globals['_GETREADINGSREQUEST']._serialized_start = 341
    _globals['_GETREADINGSREQUEST']._serialized_end = 509
    _globals['_READINGS']._serialized_start = 512
    _globals['_READINGS']._serialized_end = 746
    _globals['_READINGS_READINGSENTRY']._serialized_start = 659
    _globals['_READINGS_READINGSENTRY']._serialized_end = 742
    _globals['_GETREADINGSRESPONSE']._serialized_start = 748
    _globals['_GETREADINGSRESPONSE']._serialized_end = 840
    _globals['_SENSORSSERVICE']._serialized_start = 843
    _globals['_SENSORSSERVICE']._serialized_end = 1317