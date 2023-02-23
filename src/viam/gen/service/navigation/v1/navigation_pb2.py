"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....common.v1 import common_pb2 as common_dot_v1_dot_common__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&service/navigation/v1/navigation.proto\x12\x1aviam.service.navigation.v1\x1a\x16common/v1/common.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1cgoogle/protobuf/struct.proto"S\n\x0eGetModeRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"G\n\x0fGetModeResponse\x124\n\x04mode\x18\x01 \x01(\x0e2 .viam.service.navigation.v1.ModeR\x04mode"\x89\x01\n\x0eSetModeRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x124\n\x04mode\x18\x02 \x01(\x0e2 .viam.service.navigation.v1.ModeR\x04mode\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"\x11\n\x0fSetModeResponse"P\n\x08Waypoint\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x124\n\x08location\x18\x02 \x01(\x0b2\x18.viam.common.v1.GeoPointR\x08location"W\n\x12GetLocationRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"K\n\x13GetLocationResponse\x124\n\x08location\x18\x01 \x01(\x0b2\x18.viam.common.v1.GeoPointR\x08location"X\n\x13GetWaypointsRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"Z\n\x14GetWaypointsResponse\x12B\n\twaypoints\x18\x01 \x03(\x0b2$.viam.service.navigation.v1.WaypointR\twaypoints"\x8d\x01\n\x12AddWaypointRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x124\n\x08location\x18\x02 \x01(\x0b2\x18.viam.common.v1.GeoPointR\x08location\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"\x15\n\x13AddWaypointResponse"j\n\x15RemoveWaypointRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x0e\n\x02id\x18\x02 \x01(\tR\x02id\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"\x18\n\x16RemoveWaypointResponse*@\n\x04Mode\x12\x14\n\x10MODE_UNSPECIFIED\x10\x00\x12\x0f\n\x0bMODE_MANUAL\x10\x01\x12\x11\n\rMODE_WAYPOINT\x10\x022\x91\t\n\x11NavigationService\x12\x97\x01\n\x07GetMode\x12*.viam.service.navigation.v1.GetModeRequest\x1a+.viam.service.navigation.v1.GetModeResponse"3\x82\xd3\xe4\x93\x02-\x12+/viam/api/v1/service/navigation/{name}/mode\x12\x97\x01\n\x07SetMode\x12*.viam.service.navigation.v1.SetModeRequest\x1a+.viam.service.navigation.v1.SetModeResponse"3\x82\xd3\xe4\x93\x02-\x1a+/viam/api/v1/service/navigation/{name}/mode\x12\xa7\x01\n\x0bGetLocation\x12..viam.service.navigation.v1.GetLocationRequest\x1a/.viam.service.navigation.v1.GetLocationResponse"7\x82\xd3\xe4\x93\x021\x12//viam/api/v1/service/navigation/{name}/location\x12\xab\x01\n\x0cGetWaypoints\x12/.viam.service.navigation.v1.GetWaypointsRequest\x1a0.viam.service.navigation.v1.GetWaypointsResponse"8\x82\xd3\xe4\x93\x022\x120/viam/api/v1/service/navigation/{name}/waypoints\x12\xa8\x01\n\x0bAddWaypoint\x12..viam.service.navigation.v1.AddWaypointRequest\x1a/.viam.service.navigation.v1.AddWaypointResponse"8\x82\xd3\xe4\x93\x022"0/viam/api/v1/service/navigation/{name}/waypoints\x12\xb6\x01\n\x0eRemoveWaypoint\x121.viam.service.navigation.v1.RemoveWaypointRequest\x1a2.viam.service.navigation.v1.RemoveWaypointResponse"=\x82\xd3\xe4\x93\x027*5/viam/api/v1/service/navigation/{name}/waypoints/{id}\x12\x8b\x01\n\tDoCommand\x12 .viam.common.v1.DoCommandRequest\x1a!.viam.common.v1.DoCommandResponse"9\x82\xd3\xe4\x93\x023"1/viam/api/v1/service/navigation/{name}/do_commandBG\n\x1ecom.viam.service.navigation.v1Z%go.viam.com/api/service/navigation/v1b\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'service.navigation.v1.navigation_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n\x1ecom.viam.service.navigation.v1Z%go.viam.com/api/service/navigation/v1'
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
    _NAVIGATIONSERVICE.methods_by_name['DoCommand']._options = None
    _NAVIGATIONSERVICE.methods_by_name['DoCommand']._serialized_options = b'\x82\xd3\xe4\x93\x023"1/viam/api/v1/service/navigation/{name}/do_command'
    _MODE._serialized_start = 1202
    _MODE._serialized_end = 1266
    _GETMODEREQUEST._serialized_start = 154
    _GETMODEREQUEST._serialized_end = 237
    _GETMODERESPONSE._serialized_start = 239
    _GETMODERESPONSE._serialized_end = 310
    _SETMODEREQUEST._serialized_start = 313
    _SETMODEREQUEST._serialized_end = 450
    _SETMODERESPONSE._serialized_start = 452
    _SETMODERESPONSE._serialized_end = 469
    _WAYPOINT._serialized_start = 471
    _WAYPOINT._serialized_end = 551
    _GETLOCATIONREQUEST._serialized_start = 553
    _GETLOCATIONREQUEST._serialized_end = 640
    _GETLOCATIONRESPONSE._serialized_start = 642
    _GETLOCATIONRESPONSE._serialized_end = 717
    _GETWAYPOINTSREQUEST._serialized_start = 719
    _GETWAYPOINTSREQUEST._serialized_end = 807
    _GETWAYPOINTSRESPONSE._serialized_start = 809
    _GETWAYPOINTSRESPONSE._serialized_end = 899
    _ADDWAYPOINTREQUEST._serialized_start = 902
    _ADDWAYPOINTREQUEST._serialized_end = 1043
    _ADDWAYPOINTRESPONSE._serialized_start = 1045
    _ADDWAYPOINTRESPONSE._serialized_end = 1066
    _REMOVEWAYPOINTREQUEST._serialized_start = 1068
    _REMOVEWAYPOINTREQUEST._serialized_end = 1174
    _REMOVEWAYPOINTRESPONSE._serialized_start = 1176
    _REMOVEWAYPOINTRESPONSE._serialized_end = 1200
    _NAVIGATIONSERVICE._serialized_start = 1269
    _NAVIGATIONSERVICE._serialized_end = 2438