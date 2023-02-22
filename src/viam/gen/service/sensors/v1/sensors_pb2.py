"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....common.v1 import common_pb2 as common_dot_v1_dot_common__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n service/sensors/v1/sensors.proto\x12\x17viam.service.sensors.v1\x1a\x16common/v1/common.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1cgoogle/protobuf/struct.proto"V\n\x11GetSensorsRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"U\n\x12GetSensorsResponse\x12?\n\x0csensor_names\x18\x01 \x03(\x0b2\x1c.viam.common.v1.ResourceNameR\x0bsensorNames"\x98\x01\n\x12GetReadingsRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12?\n\x0csensor_names\x18\x02 \x03(\x0b2\x1c.viam.common.v1.ResourceNameR\x0bsensorNames\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"\xde\x01\n\x08Readings\x120\n\x04name\x18\x01 \x01(\x0b2\x1c.viam.common.v1.ResourceNameR\x04name\x12K\n\x08readings\x18\x02 \x03(\x0b2/.viam.service.sensors.v1.Readings.ReadingsEntryR\x08readings\x1aS\n\rReadingsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12,\n\x05value\x18\x02 \x01(\x0b2\x16.google.protobuf.ValueR\x05value:\x028\x01"T\n\x13GetReadingsResponse\x12=\n\x08readings\x18\x01 \x03(\x0b2!.viam.service.sensors.v1.ReadingsR\x08readings2\xd1\x03\n\x0eSensorsService\x12\x92\x01\n\nGetSensors\x12*.viam.service.sensors.v1.GetSensorsRequest\x1a+.viam.service.sensors.v1.GetSensorsResponse"+\x82\xd3\xe4\x93\x02%\x12#/viam/api/v1/service/{name}/sensors\x12\x9e\x01\n\x0bGetReadings\x12+.viam.service.sensors.v1.GetReadingsRequest\x1a,.viam.service.sensors.v1.GetReadingsResponse"4\x82\xd3\xe4\x93\x02.\x12,/viam/api/v1/service/sensors/{name}/readings\x12\x88\x01\n\tDoCommand\x12 .viam.common.v1.DoCommandRequest\x1a!.viam.common.v1.DoCommandResponse"6\x82\xd3\xe4\x93\x020"./viam/api/v1/service/sensors/{name}/do_commandBA\n\x1bcom.viam.service.sensors.v1Z"go.viam.com/api/service/sensors/v1b\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'service.sensors.v1.sensors_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n\x1bcom.viam.service.sensors.v1Z"go.viam.com/api/service/sensors/v1'
    _READINGS_READINGSENTRY._options = None
    _READINGS_READINGSENTRY._serialized_options = b'8\x01'
    _SENSORSSERVICE.methods_by_name['GetSensors']._options = None
    _SENSORSSERVICE.methods_by_name['GetSensors']._serialized_options = b'\x82\xd3\xe4\x93\x02%\x12#/viam/api/v1/service/{name}/sensors'
    _SENSORSSERVICE.methods_by_name['GetReadings']._options = None
    _SENSORSSERVICE.methods_by_name['GetReadings']._serialized_options = b'\x82\xd3\xe4\x93\x02.\x12,/viam/api/v1/service/sensors/{name}/readings'
    _SENSORSSERVICE.methods_by_name['DoCommand']._options = None
    _SENSORSSERVICE.methods_by_name['DoCommand']._serialized_options = b'\x82\xd3\xe4\x93\x020"./viam/api/v1/service/sensors/{name}/do_command'
    _GETSENSORSREQUEST._serialized_start = 145
    _GETSENSORSREQUEST._serialized_end = 231
    _GETSENSORSRESPONSE._serialized_start = 233
    _GETSENSORSRESPONSE._serialized_end = 318
    _GETREADINGSREQUEST._serialized_start = 321
    _GETREADINGSREQUEST._serialized_end = 473
    _READINGS._serialized_start = 476
    _READINGS._serialized_end = 698
    _READINGS_READINGSENTRY._serialized_start = 615
    _READINGS_READINGSENTRY._serialized_end = 698
    _GETREADINGSRESPONSE._serialized_start = 700
    _GETREADINGSRESPONSE._serialized_end = 784
    _SENSORSSERVICE._serialized_start = 787
    _SENSORSSERVICE._serialized_end = 1252