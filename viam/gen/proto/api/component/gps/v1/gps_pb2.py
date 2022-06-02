"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......proto.api.common.v1 import common_pb2 as proto_dot_api_dot_common_dot_v1_dot_common__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$proto/api/component/gps/v1/gps.proto\x12\x1aproto.api.component.gps.v1\x1a\x1cgoogle/api/annotations.proto\x1a proto/api/common/v1/common.proto")\n\x13ReadLocationRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name"U\n\x14ReadLocationResponse\x12=\n\ncoordinate\x18\x01 \x01(\x0b2\x1d.proto.api.common.v1.GeoPointR\ncoordinate")\n\x13ReadAltitudeRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name"?\n\x14ReadAltitudeResponse\x12\'\n\x0faltitude_meters\x18\x01 \x01(\x01R\x0ealtitudeMeters"&\n\x10ReadSpeedRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name"<\n\x11ReadSpeedResponse\x12\'\n\x10speed_mm_per_sec\x18\x01 \x01(\x01R\rspeedMmPerSec2\xf8\x03\n\nGPSService\x12\xa5\x01\n\x0cReadLocation\x12/.proto.api.component.gps.v1.ReadLocationRequest\x1a0.proto.api.component.gps.v1.ReadLocationResponse"2\x82\xd3\xe4\x93\x02,\x12*/viam/api/v1/component/gps/{name}/location\x12\xa5\x01\n\x0cReadAltitude\x12/.proto.api.component.gps.v1.ReadAltitudeRequest\x1a0.proto.api.component.gps.v1.ReadAltitudeResponse"2\x82\xd3\xe4\x93\x02,\x12*/viam/api/v1/component/gps/{name}/altitude\x12\x99\x01\n\tReadSpeed\x12,.proto.api.component.gps.v1.ReadSpeedRequest\x1a-.proto.api.component.gps.v1.ReadSpeedResponse"/\x82\xd3\xe4\x93\x02)\x12\'/viam/api/v1/component/gps/{name}/speedBU\n\'com.viam.rdk.proto.api.component.gps.v1Z*go.viam.com/rdk/proto/api/component/gps/v1b\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'proto.api.component.gps.v1.gps_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b"\n'com.viam.rdk.proto.api.component.gps.v1Z*go.viam.com/rdk/proto/api/component/gps/v1"
    _GPSSERVICE.methods_by_name['ReadLocation']._options = None
    _GPSSERVICE.methods_by_name['ReadLocation']._serialized_options = b'\x82\xd3\xe4\x93\x02,\x12*/viam/api/v1/component/gps/{name}/location'
    _GPSSERVICE.methods_by_name['ReadAltitude']._options = None
    _GPSSERVICE.methods_by_name['ReadAltitude']._serialized_options = b'\x82\xd3\xe4\x93\x02,\x12*/viam/api/v1/component/gps/{name}/altitude'
    _GPSSERVICE.methods_by_name['ReadSpeed']._options = None
    _GPSSERVICE.methods_by_name['ReadSpeed']._serialized_options = b"\x82\xd3\xe4\x93\x02)\x12'/viam/api/v1/component/gps/{name}/speed"
    _READLOCATIONREQUEST._serialized_start = 132
    _READLOCATIONREQUEST._serialized_end = 173
    _READLOCATIONRESPONSE._serialized_start = 175
    _READLOCATIONRESPONSE._serialized_end = 260
    _READALTITUDEREQUEST._serialized_start = 262
    _READALTITUDEREQUEST._serialized_end = 303
    _READALTITUDERESPONSE._serialized_start = 305
    _READALTITUDERESPONSE._serialized_end = 368
    _READSPEEDREQUEST._serialized_start = 370
    _READSPEEDREQUEST._serialized_end = 408
    _READSPEEDRESPONSE._serialized_start = 410
    _READSPEEDRESPONSE._serialized_end = 470
    _GPSSERVICE._serialized_start = 473
    _GPSSERVICE._serialized_end = 977