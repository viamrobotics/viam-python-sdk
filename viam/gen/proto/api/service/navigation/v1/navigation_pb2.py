"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......proto.api.common.v1 import common_pb2 as proto_dot_api_dot_common_dot_v1_dot_common__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0proto/api/service/navigation/v1/navigation.proto\x12\x1fproto.api.service.navigation.v1\x1a\x1cgoogle/api/annotations.proto\x1a proto/api/common/v1/common.proto"\x10\n\x0eGetModeRequest"L\n\x0fGetModeResponse\x129\n\x04mode\x18\x01 \x01(\x0e2%.proto.api.service.navigation.v1.ModeR\x04mode"K\n\x0eSetModeRequest\x129\n\x04mode\x18\x01 \x01(\x0e2%.proto.api.service.navigation.v1.ModeR\x04mode"\x11\n\x0fSetModeResponse"U\n\x08Waypoint\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x129\n\x08location\x18\x02 \x01(\x0b2\x1d.proto.api.common.v1.GeoPointR\x08location"\x14\n\x12GetLocationRequest"P\n\x13GetLocationResponse\x129\n\x08location\x18\x01 \x01(\x0b2\x1d.proto.api.common.v1.GeoPointR\x08location"\x15\n\x13GetWaypointsRequest"_\n\x14GetWaypointsResponse\x12G\n\twaypoints\x18\x01 \x03(\x0b2).proto.api.service.navigation.v1.WaypointR\twaypoints"O\n\x12AddWaypointRequest\x129\n\x08location\x18\x01 \x01(\x0b2\x1d.proto.api.common.v1.GeoPointR\x08location"\x15\n\x13AddWaypointResponse"\'\n\x15RemoveWaypointRequest\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id"\x18\n\x16RemoveWaypointResponse*@\n\x04Mode\x12\x14\n\x10MODE_UNSPECIFIED\x10\x00\x12\x0f\n\x0bMODE_MANUAL\x10\x01\x12\x11\n\rMODE_WAYPOINT\x10\x022\x95\x08\n\x11NavigationService\x12\x9a\x01\n\x07GetMode\x12/.proto.api.service.navigation.v1.GetModeRequest\x1a0.proto.api.service.navigation.v1.GetModeResponse",\x82\xd3\xe4\x93\x02&\x12$/viam/api/v1/service/navigation/mode\x12\x9a\x01\n\x07SetMode\x12/.proto.api.service.navigation.v1.SetModeRequest\x1a0.proto.api.service.navigation.v1.SetModeResponse",\x82\xd3\xe4\x93\x02&\x1a$/viam/api/v1/service/navigation/mode\x12\xaa\x01\n\x0bGetLocation\x123.proto.api.service.navigation.v1.GetLocationRequest\x1a4.proto.api.service.navigation.v1.GetLocationResponse"0\x82\xd3\xe4\x93\x02*\x12(/viam/api/v1/service/navigation/location\x12\xae\x01\n\x0cGetWaypoints\x124.proto.api.service.navigation.v1.GetWaypointsRequest\x1a5.proto.api.service.navigation.v1.GetWaypointsResponse"1\x82\xd3\xe4\x93\x02+\x12)/viam/api/v1/service/navigation/waypoints\x12\xab\x01\n\x0bAddWaypoint\x123.proto.api.service.navigation.v1.AddWaypointRequest\x1a4.proto.api.service.navigation.v1.AddWaypointResponse"1\x82\xd3\xe4\x93\x02+")/viam/api/v1/service/navigation/waypoints\x12\xb9\x01\n\x0eRemoveWaypoint\x126.proto.api.service.navigation.v1.RemoveWaypointRequest\x1a7.proto.api.service.navigation.v1.RemoveWaypointResponse"6\x82\xd3\xe4\x93\x020*./viam/api/v1/service/navigation/waypoints/{id}B_\n,com.viam.rdk.proto.api.service.navigation.v1Z/go.viam.com/rdk/proto/api/service/navigation/v1b\x06proto3')
_MODE = DESCRIPTOR.enum_types_by_name['Mode']
Mode = enum_type_wrapper.EnumTypeWrapper(_MODE)
MODE_UNSPECIFIED = 0
MODE_MANUAL = 1
MODE_WAYPOINT = 2
_GETMODEREQUEST = DESCRIPTOR.message_types_by_name['GetModeRequest']
_GETMODERESPONSE = DESCRIPTOR.message_types_by_name['GetModeResponse']
_SETMODEREQUEST = DESCRIPTOR.message_types_by_name['SetModeRequest']
_SETMODERESPONSE = DESCRIPTOR.message_types_by_name['SetModeResponse']
_WAYPOINT = DESCRIPTOR.message_types_by_name['Waypoint']
_GETLOCATIONREQUEST = DESCRIPTOR.message_types_by_name['GetLocationRequest']
_GETLOCATIONRESPONSE = DESCRIPTOR.message_types_by_name['GetLocationResponse']
_GETWAYPOINTSREQUEST = DESCRIPTOR.message_types_by_name['GetWaypointsRequest']
_GETWAYPOINTSRESPONSE = DESCRIPTOR.message_types_by_name['GetWaypointsResponse']
_ADDWAYPOINTREQUEST = DESCRIPTOR.message_types_by_name['AddWaypointRequest']
_ADDWAYPOINTRESPONSE = DESCRIPTOR.message_types_by_name['AddWaypointResponse']
_REMOVEWAYPOINTREQUEST = DESCRIPTOR.message_types_by_name['RemoveWaypointRequest']
_REMOVEWAYPOINTRESPONSE = DESCRIPTOR.message_types_by_name['RemoveWaypointResponse']
GetModeRequest = _reflection.GeneratedProtocolMessageType('GetModeRequest', (_message.Message,), {'DESCRIPTOR': _GETMODEREQUEST, '__module__': 'proto.api.service.navigation.v1.navigation_pb2'})
_sym_db.RegisterMessage(GetModeRequest)
GetModeResponse = _reflection.GeneratedProtocolMessageType('GetModeResponse', (_message.Message,), {'DESCRIPTOR': _GETMODERESPONSE, '__module__': 'proto.api.service.navigation.v1.navigation_pb2'})
_sym_db.RegisterMessage(GetModeResponse)
SetModeRequest = _reflection.GeneratedProtocolMessageType('SetModeRequest', (_message.Message,), {'DESCRIPTOR': _SETMODEREQUEST, '__module__': 'proto.api.service.navigation.v1.navigation_pb2'})
_sym_db.RegisterMessage(SetModeRequest)
SetModeResponse = _reflection.GeneratedProtocolMessageType('SetModeResponse', (_message.Message,), {'DESCRIPTOR': _SETMODERESPONSE, '__module__': 'proto.api.service.navigation.v1.navigation_pb2'})
_sym_db.RegisterMessage(SetModeResponse)
Waypoint = _reflection.GeneratedProtocolMessageType('Waypoint', (_message.Message,), {'DESCRIPTOR': _WAYPOINT, '__module__': 'proto.api.service.navigation.v1.navigation_pb2'})
_sym_db.RegisterMessage(Waypoint)
GetLocationRequest = _reflection.GeneratedProtocolMessageType('GetLocationRequest', (_message.Message,), {'DESCRIPTOR': _GETLOCATIONREQUEST, '__module__': 'proto.api.service.navigation.v1.navigation_pb2'})
_sym_db.RegisterMessage(GetLocationRequest)
GetLocationResponse = _reflection.GeneratedProtocolMessageType('GetLocationResponse', (_message.Message,), {'DESCRIPTOR': _GETLOCATIONRESPONSE, '__module__': 'proto.api.service.navigation.v1.navigation_pb2'})
_sym_db.RegisterMessage(GetLocationResponse)
GetWaypointsRequest = _reflection.GeneratedProtocolMessageType('GetWaypointsRequest', (_message.Message,), {'DESCRIPTOR': _GETWAYPOINTSREQUEST, '__module__': 'proto.api.service.navigation.v1.navigation_pb2'})
_sym_db.RegisterMessage(GetWaypointsRequest)
GetWaypointsResponse = _reflection.GeneratedProtocolMessageType('GetWaypointsResponse', (_message.Message,), {'DESCRIPTOR': _GETWAYPOINTSRESPONSE, '__module__': 'proto.api.service.navigation.v1.navigation_pb2'})
_sym_db.RegisterMessage(GetWaypointsResponse)
AddWaypointRequest = _reflection.GeneratedProtocolMessageType('AddWaypointRequest', (_message.Message,), {'DESCRIPTOR': _ADDWAYPOINTREQUEST, '__module__': 'proto.api.service.navigation.v1.navigation_pb2'})
_sym_db.RegisterMessage(AddWaypointRequest)
AddWaypointResponse = _reflection.GeneratedProtocolMessageType('AddWaypointResponse', (_message.Message,), {'DESCRIPTOR': _ADDWAYPOINTRESPONSE, '__module__': 'proto.api.service.navigation.v1.navigation_pb2'})
_sym_db.RegisterMessage(AddWaypointResponse)
RemoveWaypointRequest = _reflection.GeneratedProtocolMessageType('RemoveWaypointRequest', (_message.Message,), {'DESCRIPTOR': _REMOVEWAYPOINTREQUEST, '__module__': 'proto.api.service.navigation.v1.navigation_pb2'})
_sym_db.RegisterMessage(RemoveWaypointRequest)
RemoveWaypointResponse = _reflection.GeneratedProtocolMessageType('RemoveWaypointResponse', (_message.Message,), {'DESCRIPTOR': _REMOVEWAYPOINTRESPONSE, '__module__': 'proto.api.service.navigation.v1.navigation_pb2'})
_sym_db.RegisterMessage(RemoveWaypointResponse)
_NAVIGATIONSERVICE = DESCRIPTOR.services_by_name['NavigationService']
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n,com.viam.rdk.proto.api.service.navigation.v1Z/go.viam.com/rdk/proto/api/service/navigation/v1'
    _NAVIGATIONSERVICE.methods_by_name['GetMode']._options = None
    _NAVIGATIONSERVICE.methods_by_name['GetMode']._serialized_options = b'\x82\xd3\xe4\x93\x02&\x12$/viam/api/v1/service/navigation/mode'
    _NAVIGATIONSERVICE.methods_by_name['SetMode']._options = None
    _NAVIGATIONSERVICE.methods_by_name['SetMode']._serialized_options = b'\x82\xd3\xe4\x93\x02&\x1a$/viam/api/v1/service/navigation/mode'
    _NAVIGATIONSERVICE.methods_by_name['GetLocation']._options = None
    _NAVIGATIONSERVICE.methods_by_name['GetLocation']._serialized_options = b'\x82\xd3\xe4\x93\x02*\x12(/viam/api/v1/service/navigation/location'
    _NAVIGATIONSERVICE.methods_by_name['GetWaypoints']._options = None
    _NAVIGATIONSERVICE.methods_by_name['GetWaypoints']._serialized_options = b'\x82\xd3\xe4\x93\x02+\x12)/viam/api/v1/service/navigation/waypoints'
    _NAVIGATIONSERVICE.methods_by_name['AddWaypoint']._options = None
    _NAVIGATIONSERVICE.methods_by_name['AddWaypoint']._serialized_options = b'\x82\xd3\xe4\x93\x02+")/viam/api/v1/service/navigation/waypoints'
    _NAVIGATIONSERVICE.methods_by_name['RemoveWaypoint']._options = None
    _NAVIGATIONSERVICE.methods_by_name['RemoveWaypoint']._serialized_options = b'\x82\xd3\xe4\x93\x020*./viam/api/v1/service/navigation/waypoints/{id}'
    _MODE._serialized_start = 823
    _MODE._serialized_end = 887
    _GETMODEREQUEST._serialized_start = 149
    _GETMODEREQUEST._serialized_end = 165
    _GETMODERESPONSE._serialized_start = 167
    _GETMODERESPONSE._serialized_end = 243
    _SETMODEREQUEST._serialized_start = 245
    _SETMODEREQUEST._serialized_end = 320
    _SETMODERESPONSE._serialized_start = 322
    _SETMODERESPONSE._serialized_end = 339
    _WAYPOINT._serialized_start = 341
    _WAYPOINT._serialized_end = 426
    _GETLOCATIONREQUEST._serialized_start = 428
    _GETLOCATIONREQUEST._serialized_end = 448
    _GETLOCATIONRESPONSE._serialized_start = 450
    _GETLOCATIONRESPONSE._serialized_end = 530
    _GETWAYPOINTSREQUEST._serialized_start = 532
    _GETWAYPOINTSREQUEST._serialized_end = 553
    _GETWAYPOINTSRESPONSE._serialized_start = 555
    _GETWAYPOINTSRESPONSE._serialized_end = 650
    _ADDWAYPOINTREQUEST._serialized_start = 652
    _ADDWAYPOINTREQUEST._serialized_end = 731
    _ADDWAYPOINTRESPONSE._serialized_start = 733
    _ADDWAYPOINTRESPONSE._serialized_end = 754
    _REMOVEWAYPOINTREQUEST._serialized_start = 756
    _REMOVEWAYPOINTREQUEST._serialized_end = 795
    _REMOVEWAYPOINTRESPONSE._serialized_start = 797
    _REMOVEWAYPOINTRESPONSE._serialized_end = 821
    _NAVIGATIONSERVICE._serialized_start = 890
    _NAVIGATIONSERVICE._serialized_end = 1935