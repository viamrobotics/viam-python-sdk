"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......proto.api.common.v1 import common_pb2 as proto_dot_api_dot_common_dot_v1_dot_common__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0proto/api/service/navigation/v1/navigation.proto\x12\x1fproto.api.service.navigation.v1\x1a\x1cgoogle/api/annotations.proto\x1a proto/api/common/v1/common.proto"$\n\x0eGetModeRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name"L\n\x0fGetModeResponse\x129\n\x04mode\x18\x01 \x01(\x0e2%.proto.api.service.navigation.v1.ModeR\x04mode"_\n\x0eSetModeRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x129\n\x04mode\x18\x02 \x01(\x0e2%.proto.api.service.navigation.v1.ModeR\x04mode"\x11\n\x0fSetModeResponse"U\n\x08Waypoint\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x129\n\x08location\x18\x02 \x01(\x0b2\x1d.proto.api.common.v1.GeoPointR\x08location"(\n\x12GetLocationRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name"P\n\x13GetLocationResponse\x129\n\x08location\x18\x01 \x01(\x0b2\x1d.proto.api.common.v1.GeoPointR\x08location")\n\x13GetWaypointsRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name"_\n\x14GetWaypointsResponse\x12G\n\twaypoints\x18\x01 \x03(\x0b2).proto.api.service.navigation.v1.WaypointR\twaypoints"c\n\x12AddWaypointRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x129\n\x08location\x18\x02 \x01(\x0b2\x1d.proto.api.common.v1.GeoPointR\x08location"\x15\n\x13AddWaypointResponse";\n\x15RemoveWaypointRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x0e\n\x02id\x18\x02 \x01(\tR\x02id"\x18\n\x16RemoveWaypointResponse*@\n\x04Mode\x12\x14\n\x10MODE_UNSPECIFIED\x10\x00\x12\x0f\n\x0bMODE_MANUAL\x10\x01\x12\x11\n\rMODE_WAYPOINT\x10\x022\xbf\x08\n\x11NavigationService\x12\xa1\x01\n\x07GetMode\x12/.proto.api.service.navigation.v1.GetModeRequest\x1a0.proto.api.service.navigation.v1.GetModeResponse"3\x82\xd3\xe4\x93\x02-\x12+/viam/api/v1/service/navigation/{name}/mode\x12\xa1\x01\n\x07SetMode\x12/.proto.api.service.navigation.v1.SetModeRequest\x1a0.proto.api.service.navigation.v1.SetModeResponse"3\x82\xd3\xe4\x93\x02-\x1a+/viam/api/v1/service/navigation/{name}/mode\x12\xb1\x01\n\x0bGetLocation\x123.proto.api.service.navigation.v1.GetLocationRequest\x1a4.proto.api.service.navigation.v1.GetLocationResponse"7\x82\xd3\xe4\x93\x021\x12//viam/api/v1/service/navigation/{name}/location\x12\xb5\x01\n\x0cGetWaypoints\x124.proto.api.service.navigation.v1.GetWaypointsRequest\x1a5.proto.api.service.navigation.v1.GetWaypointsResponse"8\x82\xd3\xe4\x93\x022\x120/viam/api/v1/service/navigation/{name}/waypoints\x12\xb2\x01\n\x0bAddWaypoint\x123.proto.api.service.navigation.v1.AddWaypointRequest\x1a4.proto.api.service.navigation.v1.AddWaypointResponse"8\x82\xd3\xe4\x93\x022"0/viam/api/v1/service/navigation/{name}/waypoints\x12\xc0\x01\n\x0eRemoveWaypoint\x126.proto.api.service.navigation.v1.RemoveWaypointRequest\x1a7.proto.api.service.navigation.v1.RemoveWaypointResponse"=\x82\xd3\xe4\x93\x027*5/viam/api/v1/service/navigation/{name}/waypoints/{id}B_\n,com.viam.rdk.proto.api.service.navigation.v1Z/go.viam.com/rdk/proto/api/service/navigation/v1b\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'proto.api.service.navigation.v1.navigation_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n,com.viam.rdk.proto.api.service.navigation.v1Z/go.viam.com/rdk/proto/api/service/navigation/v1'
    _NAVIGATIONSERVICE.methods_by_name['GetMode']._options = None
    _NAVIGATIONSERVICE.methods_by_name['GetMode']._serialized_options = b'\x82\xd3\xe4\x93\x02-\x12+/viam/api/v1/service/navigation/{name}/mode'
    _NAVIGATIONSERVICE.methods_by_name['SetMode']._options = None
    _NAVIGATIONSERVICE.methods_by_name['SetMode']._serialized_options = b'\x82\xd3\xe4\x93\x02-\x1a+/viam/api/v1/service/navigation/{name}/mode'
    _NAVIGATIONSERVICE.methods_by_name['GetLocation']._options = None
    _NAVIGATIONSERVICE.methods_by_name['GetLocation']._serialized_options = b'\x82\xd3\xe4\x93\x021\x12//viam/api/v1/service/navigation/{name}/location'
    _NAVIGATIONSERVICE.methods_by_name['GetWaypoints']._options = None
    _NAVIGATIONSERVICE.methods_by_name['GetWaypoints']._serialized_options = b'\x82\xd3\xe4\x93\x022\x120/viam/api/v1/service/navigation/{name}/waypoints'
    _NAVIGATIONSERVICE.methods_by_name['AddWaypoint']._options = None
    _NAVIGATIONSERVICE.methods_by_name['AddWaypoint']._serialized_options = b'\x82\xd3\xe4\x93\x022"0/viam/api/v1/service/navigation/{name}/waypoints'
    _NAVIGATIONSERVICE.methods_by_name['RemoveWaypoint']._options = None
    _NAVIGATIONSERVICE.methods_by_name['RemoveWaypoint']._serialized_options = b'\x82\xd3\xe4\x93\x027*5/viam/api/v1/service/navigation/{name}/waypoints/{id}'
    _MODE._serialized_start = 943
    _MODE._serialized_end = 1007
    _GETMODEREQUEST._serialized_start = 149
    _GETMODEREQUEST._serialized_end = 185
    _GETMODERESPONSE._serialized_start = 187
    _GETMODERESPONSE._serialized_end = 263
    _SETMODEREQUEST._serialized_start = 265
    _SETMODEREQUEST._serialized_end = 360
    _SETMODERESPONSE._serialized_start = 362
    _SETMODERESPONSE._serialized_end = 379
    _WAYPOINT._serialized_start = 381
    _WAYPOINT._serialized_end = 466
    _GETLOCATIONREQUEST._serialized_start = 468
    _GETLOCATIONREQUEST._serialized_end = 508
    _GETLOCATIONRESPONSE._serialized_start = 510
    _GETLOCATIONRESPONSE._serialized_end = 590
    _GETWAYPOINTSREQUEST._serialized_start = 592
    _GETWAYPOINTSREQUEST._serialized_end = 633
    _GETWAYPOINTSRESPONSE._serialized_start = 635
    _GETWAYPOINTSRESPONSE._serialized_end = 730
    _ADDWAYPOINTREQUEST._serialized_start = 732
    _ADDWAYPOINTREQUEST._serialized_end = 831
    _ADDWAYPOINTRESPONSE._serialized_start = 833
    _ADDWAYPOINTRESPONSE._serialized_end = 854
    _REMOVEWAYPOINTREQUEST._serialized_start = 856
    _REMOVEWAYPOINTREQUEST._serialized_end = 915
    _REMOVEWAYPOINTRESPONSE._serialized_start = 917
    _REMOVEWAYPOINTRESPONSE._serialized_end = 941
    _NAVIGATIONSERVICE._serialized_start = 1010
    _NAVIGATIONSERVICE._serialized_end = 2097