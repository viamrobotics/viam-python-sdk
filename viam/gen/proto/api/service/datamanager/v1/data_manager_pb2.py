"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3proto/api/service/datamanager/v1/data_manager.proto\x12 proto.api.service.datamanager.v1\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\x94\x01\n\x0eSensorMetadata\x12A\n\x0etime_requested\x18\x01 \x01(\x0b2\x1a.google.protobuf.TimestampR\rtimeRequested\x12?\n\rtime_received\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampR\x0ctimeReceived"\x87\x01\n\nSensorData\x12L\n\x08metadata\x18\x01 \x01(\x0b20.proto.api.service.datamanager.v1.SensorMetadataR\x08metadata\x12+\n\x04data\x18\x02 \x01(\x0b2\x17.google.protobuf.StructR\x04dataB2Z0go.viam.com/rdk/proto/api/service/datamanager/v1b\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'proto.api.service.datamanager.v1.data_manager_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z0go.viam.com/rdk/proto/api/service/datamanager/v1'
    _SENSORMETADATA._serialized_start = 153
    _SENSORMETADATA._serialized_end = 301
    _SENSORDATA._serialized_start = 304
    _SENSORDATA._serialized_end = 439