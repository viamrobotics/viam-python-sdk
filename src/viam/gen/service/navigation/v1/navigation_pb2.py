"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....common.v1 import common_pb2 as common_dot_v1_dot_common__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&service/navigation/v1/navigation.proto\x12\x1aviam.service.navigation.v1\x1a\x16common/v1/common.proto\x1a\x1cgoogle/api/annotations.proto"$\n\x0eGetModeRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name"G\n\x0fGetModeResponse\x124\n\x04mode\x18\x01 \x01(\x0e2 .viam.service.navigation.v1.ModeR\x04mode"Z\n\x0eSetModeRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x124\n\x04mode\x18\x02 \x01(\x0e2 .viam.service.navigation.v1.ModeR\x04mode"\x11\n\x0fSetModeResponse"P\n\x08Waypoint\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x124\n\x08location\x18\x02 \x01(\x0b2\x18.viam.common.v1.GeoPointR\x08location"(\n\x12GetLocationRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name"K\n\x13GetLocationResponse\x124\n\x08location\x18\x01 \x01(\x0b2\x18.viam.common.v1.GeoPointR\x08location")\n\x13GetWaypointsRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name"Z\n\x14GetWaypointsResponse\x12B\n\twaypoints\x18\x01 \x03(\x0b2$.viam.service.navigation.v1.WaypointR\twaypoints"^\n\x12AddWaypointRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x124\n\x08location\x18\x02 \x01(\x0b2\x18.viam.common.v1.GeoPointR\x08location"\x15\n\x13AddWaypointResponse";\n\x15RemoveWaypointRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x0e\n\x02id\x18\x02 \x01(\tR\x02id"\x18\n\x16RemoveWaypointResponse*@\n\x04Mode\x12\x14\n\x10MODE_UNSPECIFIED\x10\x00\x12\x0f\n\x0bMODE_MANUAL\x10\x01\x12\x11\n\rMODE_WAYPOINT\x10\x022\x83\x08\n\x11NavigationService\x12\x97\x01\n\x07GetMode\x12*.viam.service.navigation.v1.GetModeRequest\x1a+.viam.service.navigation.v1.GetModeResponse"3\x82\xd3\xe4\x93\x02-\x12+/viam/api/v1/service/navigation/{name}/mode\x12\x97\x01\n\x07SetMode\x12*.viam.service.navigation.v1.SetModeRequest\x1a+.viam.service.navigation.v1.SetModeResponse"3\x82\xd3\xe4\x93\x02-\x1a+/viam/api/v1/service/navigation/{name}/mode\x12\xa7\x01\n\x0bGetLocation\x12..viam.service.navigation.v1.GetLocationRequest\x1a/.viam.service.navigation.v1.GetLocationResponse"7\x82\xd3\xe4\x93\x021\x12//viam/api/v1/service/navigation/{name}/location\x12\xab\x01\n\x0cGetWaypoints\x12/.viam.service.navigation.v1.GetWaypointsRequest\x1a0.viam.service.navigation.v1.GetWaypointsResponse"8\x82\xd3\xe4\x93\x022\x120/viam/api/v1/service/navigation/{name}/waypoints\x12\xa8\x01\n\x0bAddWaypoint\x12..viam.service.navigation.v1.AddWaypointRequest\x1a/.viam.service.navigation.v1.AddWaypointResponse"8\x82\xd3\xe4\x93\x022"0/viam/api/v1/service/navigation/{name}/waypoints\x12\xb6\x01\n\x0eRemoveWaypoint\x121.viam.service.navigation.v1.RemoveWaypointRequest\x1a2.viam.service.navigation.v1.RemoveWaypointResponse"=\x82\xd3\xe4\x93\x027*5/viam/api/v1/service/navigation/{name}/waypoints/{id}BG\n\x1ecom.viam.service.navigation.v1Z%go.viam.com/api/service/navigation/v1b\x06proto3')
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
    _MODE._serialized_start = 888
    _MODE._serialized_end = 952
    _GETMODEREQUEST._serialized_start = 124
    _GETMODEREQUEST._serialized_end = 160
    _GETMODERESPONSE._serialized_start = 162
    _GETMODERESPONSE._serialized_end = 233
    _SETMODEREQUEST._serialized_start = 235
    _SETMODEREQUEST._serialized_end = 325
    _SETMODERESPONSE._serialized_start = 327
    _SETMODERESPONSE._serialized_end = 344
    _WAYPOINT._serialized_start = 346
    _WAYPOINT._serialized_end = 426
    _GETLOCATIONREQUEST._serialized_start = 428
    _GETLOCATIONREQUEST._serialized_end = 468
    _GETLOCATIONRESPONSE._serialized_start = 470
    _GETLOCATIONRESPONSE._serialized_end = 545
    _GETWAYPOINTSREQUEST._serialized_start = 547
    _GETWAYPOINTSREQUEST._serialized_end = 588
    _GETWAYPOINTSRESPONSE._serialized_start = 590
    _GETWAYPOINTSRESPONSE._serialized_end = 680
    _ADDWAYPOINTREQUEST._serialized_start = 682
    _ADDWAYPOINTREQUEST._serialized_end = 776
    _ADDWAYPOINTRESPONSE._serialized_start = 778
    _ADDWAYPOINTRESPONSE._serialized_end = 799
    _REMOVEWAYPOINTREQUEST._serialized_start = 801
    _REMOVEWAYPOINTREQUEST._serialized_end = 860
    _REMOVEWAYPOINTRESPONSE._serialized_start = 862
    _REMOVEWAYPOINTRESPONSE._serialized_end = 886
    _NAVIGATIONSERVICE._serialized_start = 955
    _NAVIGATIONSERVICE._serialized_end = 1982