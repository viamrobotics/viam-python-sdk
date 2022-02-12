"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#proto/api/component/v1/sensor.proto\x12\x16proto.api.component.v1\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1cgoogle/api/annotations.proto"5\n\x1fSensorServiceGetReadingsRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name"V\n SensorServiceGetReadingsResponse\x122\n\x08readings\x18\x01 \x03(\x0b2\x16.google.protobuf.ValueR\x08readings2\xc4\x01\n\rSensorService\x12\xb2\x01\n\x0bGetReadings\x127.proto.api.component.v1.SensorServiceGetReadingsRequest\x1a8.proto.api.component.v1.SensorServiceGetReadingsResponse"0\x82\xd3\xe4\x93\x02*\x12(/api/v1/component/sensor/{name}/readingsBM\n#com.viam.rdk.proto.api.component.v1Z&go.viam.com/rdk/proto/api/component/v1b\x06proto3')
_SENSORSERVICEGETREADINGSREQUEST = DESCRIPTOR.message_types_by_name['SensorServiceGetReadingsRequest']
_SENSORSERVICEGETREADINGSRESPONSE = DESCRIPTOR.message_types_by_name['SensorServiceGetReadingsResponse']
SensorServiceGetReadingsRequest = _reflection.GeneratedProtocolMessageType('SensorServiceGetReadingsRequest', (_message.Message,), {'DESCRIPTOR': _SENSORSERVICEGETREADINGSREQUEST, '__module__': 'proto.api.component.v1.sensor_pb2'})
_sym_db.RegisterMessage(SensorServiceGetReadingsRequest)
SensorServiceGetReadingsResponse = _reflection.GeneratedProtocolMessageType('SensorServiceGetReadingsResponse', (_message.Message,), {'DESCRIPTOR': _SENSORSERVICEGETREADINGSRESPONSE, '__module__': 'proto.api.component.v1.sensor_pb2'})
_sym_db.RegisterMessage(SensorServiceGetReadingsResponse)
_SENSORSERVICE = DESCRIPTOR.services_by_name['SensorService']
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n#com.viam.rdk.proto.api.component.v1Z&go.viam.com/rdk/proto/api/component/v1'
    _SENSORSERVICE.methods_by_name['GetReadings']._options = None
    _SENSORSERVICE.methods_by_name['GetReadings']._serialized_options = b'\x82\xd3\xe4\x93\x02*\x12(/api/v1/component/sensor/{name}/readings'
    _SENSORSERVICEGETREADINGSREQUEST._serialized_start = 123
    _SENSORSERVICEGETREADINGSREQUEST._serialized_end = 176
    _SENSORSERVICEGETREADINGSRESPONSE._serialized_start = 178
    _SENSORSERVICEGETREADINGSRESPONSE._serialized_end = 264
    _SENSORSERVICE._serialized_start = 267
    _SENSORSERVICE._serialized_end = 463