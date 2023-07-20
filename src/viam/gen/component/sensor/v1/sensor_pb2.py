"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....common.v1 import common_pb2 as common_dot_v1_dot_common__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n component/sensor/v1/sensor.proto\x12\x18viam.component.sensor.v1\x1a\x16common/v1/common.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1cgoogle/protobuf/struct.proto"W\n\x12GetReadingsRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"\xc3\x01\n\x13GetReadingsResponse\x12W\n\x08readings\x18\x01 \x03(\x0b2;.viam.component.sensor.v1.GetReadingsResponse.ReadingsEntryR\x08readings\x1aS\n\rReadingsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12,\n\x05value\x18\x02 \x01(\x0b2\x16.google.protobuf.ValueR\x05value:\x028\x012\xd7\x03\n\rSensorService\x12\xa1\x01\n\x0bGetReadings\x12,.viam.component.sensor.v1.GetReadingsRequest\x1a-.viam.component.sensor.v1.GetReadingsResponse"5\x82\xd3\xe4\x93\x02/\x12-/viam/api/v1/component/sensor/{name}/readings\x12\x89\x01\n\tDoCommand\x12 .viam.common.v1.DoCommandRequest\x1a!.viam.common.v1.DoCommandResponse"7\x82\xd3\xe4\x93\x021"//viam/api/v1/component/sensor/{name}/do_command\x12\x95\x01\n\rGetGeometries\x12$.viam.common.v1.GetGeometriesRequest\x1a%.viam.common.v1.GetGeometriesResponse"7\x82\xd3\xe4\x93\x021\x12//viam/api/v1/component/sensor/{name}/geometriesBC\n\x1ccom.viam.component.sensor.v1Z#go.viam.com/api/component/sensor/v1b\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'component.sensor.v1.sensor_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n\x1ccom.viam.component.sensor.v1Z#go.viam.com/api/component/sensor/v1'
    _GETREADINGSRESPONSE_READINGSENTRY._options = None
    _GETREADINGSRESPONSE_READINGSENTRY._serialized_options = b'8\x01'
    _SENSORSERVICE.methods_by_name['GetReadings']._options = None
    _SENSORSERVICE.methods_by_name['GetReadings']._serialized_options = b'\x82\xd3\xe4\x93\x02/\x12-/viam/api/v1/component/sensor/{name}/readings'
    _SENSORSERVICE.methods_by_name['DoCommand']._options = None
    _SENSORSERVICE.methods_by_name['DoCommand']._serialized_options = b'\x82\xd3\xe4\x93\x021"//viam/api/v1/component/sensor/{name}/do_command'
    _SENSORSERVICE.methods_by_name['GetGeometries']._options = None
    _SENSORSERVICE.methods_by_name['GetGeometries']._serialized_options = b'\x82\xd3\xe4\x93\x021\x12//viam/api/v1/component/sensor/{name}/geometries'
    _GETREADINGSREQUEST._serialized_start = 146
    _GETREADINGSREQUEST._serialized_end = 233
    _GETREADINGSRESPONSE._serialized_start = 236
    _GETREADINGSRESPONSE._serialized_end = 431
    _GETREADINGSRESPONSE_READINGSENTRY._serialized_start = 348
    _GETREADINGSRESPONSE_READINGSENTRY._serialized_end = 431
    _SENSORSERVICE._serialized_start = 434
    _SENSORSERVICE._serialized_end = 905