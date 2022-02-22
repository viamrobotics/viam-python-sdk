"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*proto/api/component/sensor/v1/sensor.proto\x12\x1dproto.api.component.sensor.v1\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1cgoogle/api/annotations.proto"(\n\x12GetReadingsRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name"I\n\x13GetReadingsResponse\x122\n\x08readings\x18\x01 \x03(\x0b2\x16.google.protobuf.ValueR\x08readings2\xb8\x01\n\rSensorService\x12\xa6\x01\n\x0bGetReadings\x121.proto.api.component.sensor.v1.GetReadingsRequest\x1a2.proto.api.component.sensor.v1.GetReadingsResponse"0\x82\xd3\xe4\x93\x02*\x12(/api/v1/component/sensor/{name}/readingsB[\n*com.viam.rdk.proto.api.component.sensor.v1Z-go.viam.com/rdk/proto/api/component/sensor/v1b\x06proto3')
_GETREADINGSREQUEST = DESCRIPTOR.message_types_by_name['GetReadingsRequest']
_GETREADINGSRESPONSE = DESCRIPTOR.message_types_by_name['GetReadingsResponse']
GetReadingsRequest = _reflection.GeneratedProtocolMessageType('GetReadingsRequest', (_message.Message,), {'DESCRIPTOR': _GETREADINGSREQUEST, '__module__': 'proto.api.component.sensor.v1.sensor_pb2'})
_sym_db.RegisterMessage(GetReadingsRequest)
GetReadingsResponse = _reflection.GeneratedProtocolMessageType('GetReadingsResponse', (_message.Message,), {'DESCRIPTOR': _GETREADINGSRESPONSE, '__module__': 'proto.api.component.sensor.v1.sensor_pb2'})
_sym_db.RegisterMessage(GetReadingsResponse)
_SENSORSERVICE = DESCRIPTOR.services_by_name['SensorService']
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n*com.viam.rdk.proto.api.component.sensor.v1Z-go.viam.com/rdk/proto/api/component/sensor/v1'
    _SENSORSERVICE.methods_by_name['GetReadings']._options = None
    _SENSORSERVICE.methods_by_name['GetReadings']._serialized_options = b'\x82\xd3\xe4\x93\x02*\x12(/api/v1/component/sensor/{name}/readings'
    _GETREADINGSREQUEST._serialized_start = 137
    _GETREADINGSREQUEST._serialized_end = 177
    _GETREADINGSRESPONSE._serialized_start = 179
    _GETREADINGSRESPONSE._serialized_end = 252
    _SENSORSERVICE._serialized_start = 255
    _SENSORSERVICE._serialized_end = 439