"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....proto.api.common.v1 import common_pb2 as proto_dot_api_dot_common_dot_v1_dot_common__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n proto/api/component/v1/gps.proto\x12\x16proto.api.component.v1\x1a\x1cgoogle/api/annotations.proto\x1a proto/api/common/v1/common.proto"3\n\x1dGPSServiceReadLocationRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name"_\n\x1eGPSServiceReadLocationResponse\x12=\n\ncoordinate\x18\x01 \x01(\x0b2\x1d.proto.api.common.v1.GeoPointR\ncoordinate"3\n\x1dGPSServiceReadAltitudeRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name"I\n\x1eGPSServiceReadAltitudeResponse\x12\'\n\x0faltitude_meters\x18\x01 \x01(\x01R\x0ealtitudeMeters"0\n\x1aGPSServiceReadSpeedRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name"F\n\x1bGPSServiceReadSpeedResponse\x12\'\n\x10speed_mm_per_sec\x18\x01 \x01(\x01R\rspeedMmPerSec2\x8d\x04\n\nGPSService\x12\xac\x01\n\x0cReadLocation\x125.proto.api.component.v1.GPSServiceReadLocationRequest\x1a6.proto.api.component.v1.GPSServiceReadLocationResponse"-\x82\xd3\xe4\x93\x02\'\x12%/api/v1/component/gps/{name}/location\x12\xac\x01\n\x0cReadAltitude\x125.proto.api.component.v1.GPSServiceReadAltitudeRequest\x1a6.proto.api.component.v1.GPSServiceReadAltitudeResponse"-\x82\xd3\xe4\x93\x02\'\x12%/api/v1/component/gps/{name}/altitude\x12\xa0\x01\n\tReadSpeed\x122.proto.api.component.v1.GPSServiceReadSpeedRequest\x1a3.proto.api.component.v1.GPSServiceReadSpeedResponse"*\x82\xd3\xe4\x93\x02$\x12"/api/v1/component/gps/{name}/speedBM\n#com.viam.rdk.proto.api.component.v1Z&go.viam.com/rdk/proto/api/component/v1b\x06proto3')
_GPSSERVICEREADLOCATIONREQUEST = DESCRIPTOR.message_types_by_name['GPSServiceReadLocationRequest']
_GPSSERVICEREADLOCATIONRESPONSE = DESCRIPTOR.message_types_by_name['GPSServiceReadLocationResponse']
_GPSSERVICEREADALTITUDEREQUEST = DESCRIPTOR.message_types_by_name['GPSServiceReadAltitudeRequest']
_GPSSERVICEREADALTITUDERESPONSE = DESCRIPTOR.message_types_by_name['GPSServiceReadAltitudeResponse']
_GPSSERVICEREADSPEEDREQUEST = DESCRIPTOR.message_types_by_name['GPSServiceReadSpeedRequest']
_GPSSERVICEREADSPEEDRESPONSE = DESCRIPTOR.message_types_by_name['GPSServiceReadSpeedResponse']
GPSServiceReadLocationRequest = _reflection.GeneratedProtocolMessageType('GPSServiceReadLocationRequest', (_message.Message,), {'DESCRIPTOR': _GPSSERVICEREADLOCATIONREQUEST, '__module__': 'proto.api.component.v1.gps_pb2'})
_sym_db.RegisterMessage(GPSServiceReadLocationRequest)
GPSServiceReadLocationResponse = _reflection.GeneratedProtocolMessageType('GPSServiceReadLocationResponse', (_message.Message,), {'DESCRIPTOR': _GPSSERVICEREADLOCATIONRESPONSE, '__module__': 'proto.api.component.v1.gps_pb2'})
_sym_db.RegisterMessage(GPSServiceReadLocationResponse)
GPSServiceReadAltitudeRequest = _reflection.GeneratedProtocolMessageType('GPSServiceReadAltitudeRequest', (_message.Message,), {'DESCRIPTOR': _GPSSERVICEREADALTITUDEREQUEST, '__module__': 'proto.api.component.v1.gps_pb2'})
_sym_db.RegisterMessage(GPSServiceReadAltitudeRequest)
GPSServiceReadAltitudeResponse = _reflection.GeneratedProtocolMessageType('GPSServiceReadAltitudeResponse', (_message.Message,), {'DESCRIPTOR': _GPSSERVICEREADALTITUDERESPONSE, '__module__': 'proto.api.component.v1.gps_pb2'})
_sym_db.RegisterMessage(GPSServiceReadAltitudeResponse)
GPSServiceReadSpeedRequest = _reflection.GeneratedProtocolMessageType('GPSServiceReadSpeedRequest', (_message.Message,), {'DESCRIPTOR': _GPSSERVICEREADSPEEDREQUEST, '__module__': 'proto.api.component.v1.gps_pb2'})
_sym_db.RegisterMessage(GPSServiceReadSpeedRequest)
GPSServiceReadSpeedResponse = _reflection.GeneratedProtocolMessageType('GPSServiceReadSpeedResponse', (_message.Message,), {'DESCRIPTOR': _GPSSERVICEREADSPEEDRESPONSE, '__module__': 'proto.api.component.v1.gps_pb2'})
_sym_db.RegisterMessage(GPSServiceReadSpeedResponse)
_GPSSERVICE = DESCRIPTOR.services_by_name['GPSService']
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n#com.viam.rdk.proto.api.component.v1Z&go.viam.com/rdk/proto/api/component/v1'
    _GPSSERVICE.methods_by_name['ReadLocation']._options = None
    _GPSSERVICE.methods_by_name['ReadLocation']._serialized_options = b"\x82\xd3\xe4\x93\x02'\x12%/api/v1/component/gps/{name}/location"
    _GPSSERVICE.methods_by_name['ReadAltitude']._options = None
    _GPSSERVICE.methods_by_name['ReadAltitude']._serialized_options = b"\x82\xd3\xe4\x93\x02'\x12%/api/v1/component/gps/{name}/altitude"
    _GPSSERVICE.methods_by_name['ReadSpeed']._options = None
    _GPSSERVICE.methods_by_name['ReadSpeed']._serialized_options = b'\x82\xd3\xe4\x93\x02$\x12"/api/v1/component/gps/{name}/speed'
    _GPSSERVICEREADLOCATIONREQUEST._serialized_start = 124
    _GPSSERVICEREADLOCATIONREQUEST._serialized_end = 175
    _GPSSERVICEREADLOCATIONRESPONSE._serialized_start = 177
    _GPSSERVICEREADLOCATIONRESPONSE._serialized_end = 272
    _GPSSERVICEREADALTITUDEREQUEST._serialized_start = 274
    _GPSSERVICEREADALTITUDEREQUEST._serialized_end = 325
    _GPSSERVICEREADALTITUDERESPONSE._serialized_start = 327
    _GPSSERVICEREADALTITUDERESPONSE._serialized_end = 400
    _GPSSERVICEREADSPEEDREQUEST._serialized_start = 402
    _GPSSERVICEREADSPEEDREQUEST._serialized_end = 450
    _GPSSERVICEREADSPEEDRESPONSE._serialized_start = 452
    _GPSSERVICEREADSPEEDRESPONSE._serialized_end = 522
    _GPSSERVICE._serialized_start = 525
    _GPSSERVICE._serialized_end = 1050