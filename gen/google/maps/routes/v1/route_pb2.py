# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/maps/routes/v1/route.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.geo.type import viewport_pb2 as google_dot_geo_dot_type_dot_viewport__pb2
from google.maps.routes.v1 import polyline_pb2 as google_dot_maps_dot_routes_dot_v1_dot_polyline__pb2
from google.maps.routes.v1 import waypoint_pb2 as google_dot_maps_dot_routes_dot_v1_dot_waypoint__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.type import money_pb2 as google_dot_type_dot_money__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!google/maps/routes/v1/route.proto\x12\x15google.maps.routes.v1\x1a\x1egoogle/geo/type/viewport.proto\x1a$google/maps/routes/v1/polyline.proto\x1a$google/maps/routes/v1/waypoint.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x17google/type/money.proto\"\xe7\x03\n\x05Route\x12\x33\n\x04legs\x18\x01 \x03(\x0b\x32\x1f.google.maps.routes.v1.RouteLegR\x04legs\x12\'\n\x0f\x64istance_meters\x18\x02 \x01(\x05R\x0e\x64istanceMeters\x12\x35\n\x08\x64uration\x18\x03 \x01(\x0b\x32\x19.google.protobuf.DurationR\x08\x64uration\x12\x42\n\x0fstatic_duration\x18\x04 \x01(\x0b\x32\x19.google.protobuf.DurationR\x0estaticDuration\x12;\n\x08polyline\x18\x05 \x01(\x0b\x32\x1f.google.maps.routes.v1.PolylineR\x08polyline\x12 \n\x0b\x64\x65scription\x18\x06 \x01(\tR\x0b\x64\x65scription\x12\x1a\n\x08warnings\x18\x07 \x03(\tR\x08warnings\x12\x35\n\x08viewport\x18\x08 \x01(\x0b\x32\x19.google.geo.type.ViewportR\x08viewport\x12S\n\x0ftravel_advisory\x18\t \x01(\x0b\x32*.google.maps.routes.v1.RouteTravelAdvisoryR\x0etravelAdvisory\"\x94\x02\n\x13RouteTravelAdvisory\x12Z\n\x13traffic_restriction\x18\x01 \x01(\x0b\x32).google.maps.routes.v1.TrafficRestrictionR\x12trafficRestriction\x12<\n\ttoll_info\x18\x02 \x01(\x0b\x32\x1f.google.maps.routes.v1.TollInfoR\x08tollInfo\x12\x63\n\x17speed_reading_intervals\x18\x03 \x03(\x0b\x32+.google.maps.routes.v1.SpeedReadingIntervalR\x15speedReadingIntervals\"\xbb\x01\n\x16RouteLegTravelAdvisory\x12<\n\ttoll_info\x18\x01 \x01(\x0b\x32\x1f.google.maps.routes.v1.TollInfoR\x08tollInfo\x12\x63\n\x17speed_reading_intervals\x18\x02 \x03(\x0b\x32+.google.maps.routes.v1.SpeedReadingIntervalR\x15speedReadingIntervals\"\x81\x01\n\x1aRouteLegStepTravelAdvisory\x12\x63\n\x17speed_reading_intervals\x18\x01 \x03(\x0b\x32+.google.maps.routes.v1.SpeedReadingIntervalR\x15speedReadingIntervals\"\xaa\x01\n\x12TrafficRestriction\x12\x93\x01\n(license_plate_last_character_restriction\x18\x01 \x01(\x0b\x32;.google.maps.routes.v1.LicensePlateLastCharacterRestrictionR$licensePlateLastCharacterRestriction\"^\n$LicensePlateLastCharacterRestriction\x12\x36\n\x17\x61llowed_last_characters\x18\x01 \x03(\tR\x15\x61llowedLastCharacters\"\x8a\x04\n\x08RouteLeg\x12\'\n\x0f\x64istance_meters\x18\x01 \x01(\x05R\x0e\x64istanceMeters\x12\x35\n\x08\x64uration\x18\x02 \x01(\x0b\x32\x19.google.protobuf.DurationR\x08\x64uration\x12\x42\n\x0fstatic_duration\x18\x03 \x01(\x0b\x32\x19.google.protobuf.DurationR\x0estaticDuration\x12;\n\x08polyline\x18\x04 \x01(\x0b\x32\x1f.google.maps.routes.v1.PolylineR\x08polyline\x12\x46\n\x0estart_location\x18\x05 \x01(\x0b\x32\x1f.google.maps.routes.v1.LocationR\rstartLocation\x12\x42\n\x0c\x65nd_location\x18\x06 \x01(\x0b\x32\x1f.google.maps.routes.v1.LocationR\x0b\x65ndLocation\x12\x39\n\x05steps\x18\x07 \x03(\x0b\x32#.google.maps.routes.v1.RouteLegStepR\x05steps\x12V\n\x0ftravel_advisory\x18\x08 \x01(\x0b\x32-.google.maps.routes.v1.RouteLegTravelAdvisoryR\x0etravelAdvisory\"G\n\x08TollInfo\x12;\n\x0f\x65stimated_price\x18\x01 \x03(\x0b\x32\x12.google.type.MoneyR\x0e\x65stimatedPrice\"\x85\x04\n\x0cRouteLegStep\x12\'\n\x0f\x64istance_meters\x18\x01 \x01(\x05R\x0e\x64istanceMeters\x12\x42\n\x0fstatic_duration\x18\x02 \x01(\x0b\x32\x19.google.protobuf.DurationR\x0estaticDuration\x12;\n\x08polyline\x18\x03 \x01(\x0b\x32\x1f.google.maps.routes.v1.PolylineR\x08polyline\x12\x46\n\x0estart_location\x18\x04 \x01(\x0b\x32\x1f.google.maps.routes.v1.LocationR\rstartLocation\x12\x42\n\x0c\x65nd_location\x18\x05 \x01(\x0b\x32\x1f.google.maps.routes.v1.LocationR\x0b\x65ndLocation\x12\x63\n\x16navigation_instruction\x18\x06 \x01(\x0b\x32,.google.maps.routes.v1.NavigationInstructionR\x15navigationInstruction\x12Z\n\x0ftravel_advisory\x18\x07 \x01(\x0b\x32\x31.google.maps.routes.v1.RouteLegStepTravelAdvisoryR\x0etravelAdvisory\"x\n\x15NavigationInstruction\x12;\n\x08maneuver\x18\x01 \x01(\x0e\x32\x1f.google.maps.routes.v1.ManeuverR\x08maneuver\x12\"\n\x0cinstructions\x18\x02 \x01(\tR\x0cinstructions\"\x9c\x02\n\x14SpeedReadingInterval\x12;\n\x1astart_polyline_point_index\x18\x01 \x01(\x05R\x17startPolylinePointIndex\x12\x37\n\x18\x65nd_polyline_point_index\x18\x02 \x01(\x05R\x15\x65ndPolylinePointIndex\x12G\n\x05speed\x18\x03 \x01(\x0e\x32\x31.google.maps.routes.v1.SpeedReadingInterval.SpeedR\x05speed\"E\n\x05Speed\x12\x15\n\x11SPEED_UNSPECIFIED\x10\x00\x12\n\n\x06NORMAL\x10\x01\x12\x08\n\x04SLOW\x10\x02\x12\x0f\n\x0bTRAFFIC_JAM\x10\x03*\xda\x02\n\x08Maneuver\x12\x18\n\x14MANEUVER_UNSPECIFIED\x10\x00\x12\x14\n\x10TURN_SLIGHT_LEFT\x10\x01\x12\x13\n\x0fTURN_SHARP_LEFT\x10\x02\x12\x0e\n\nUTURN_LEFT\x10\x03\x12\r\n\tTURN_LEFT\x10\x04\x12\x15\n\x11TURN_SLIGHT_RIGHT\x10\x05\x12\x14\n\x10TURN_SHARP_RIGHT\x10\x06\x12\x0f\n\x0bUTURN_RIGHT\x10\x07\x12\x0e\n\nTURN_RIGHT\x10\x08\x12\x0c\n\x08STRAIGHT\x10\t\x12\r\n\tRAMP_LEFT\x10\n\x12\x0e\n\nRAMP_RIGHT\x10\x0b\x12\t\n\x05MERGE\x10\x0c\x12\r\n\tFORK_LEFT\x10\r\x12\x0e\n\nFORK_RIGHT\x10\x0e\x12\t\n\x05\x46\x45RRY\x10\x0f\x12\x0f\n\x0b\x46\x45RRY_TRAIN\x10\x10\x12\x13\n\x0fROUNDABOUT_LEFT\x10\x11\x12\x14\n\x10ROUNDABOUT_RIGHT\x10\x12\x42\xa0\x01\n\x19\x63om.google.maps.routes.v1B\nRouteProtoP\x01Z;google.golang.org/genproto/googleapis/maps/routes/v1;routes\xf8\x01\x01\xa2\x02\x04GMRS\xaa\x02\x15Google.Maps.Routes.V1\xca\x02\x15Google\\Maps\\Routes\\V1b\x06proto3')

_MANEUVER = DESCRIPTOR.enum_types_by_name['Maneuver']
Maneuver = enum_type_wrapper.EnumTypeWrapper(_MANEUVER)
MANEUVER_UNSPECIFIED = 0
TURN_SLIGHT_LEFT = 1
TURN_SHARP_LEFT = 2
UTURN_LEFT = 3
TURN_LEFT = 4
TURN_SLIGHT_RIGHT = 5
TURN_SHARP_RIGHT = 6
UTURN_RIGHT = 7
TURN_RIGHT = 8
STRAIGHT = 9
RAMP_LEFT = 10
RAMP_RIGHT = 11
MERGE = 12
FORK_LEFT = 13
FORK_RIGHT = 14
FERRY = 15
FERRY_TRAIN = 16
ROUNDABOUT_LEFT = 17
ROUNDABOUT_RIGHT = 18


_ROUTE = DESCRIPTOR.message_types_by_name['Route']
_ROUTETRAVELADVISORY = DESCRIPTOR.message_types_by_name['RouteTravelAdvisory']
_ROUTELEGTRAVELADVISORY = DESCRIPTOR.message_types_by_name['RouteLegTravelAdvisory']
_ROUTELEGSTEPTRAVELADVISORY = DESCRIPTOR.message_types_by_name['RouteLegStepTravelAdvisory']
_TRAFFICRESTRICTION = DESCRIPTOR.message_types_by_name['TrafficRestriction']
_LICENSEPLATELASTCHARACTERRESTRICTION = DESCRIPTOR.message_types_by_name['LicensePlateLastCharacterRestriction']
_ROUTELEG = DESCRIPTOR.message_types_by_name['RouteLeg']
_TOLLINFO = DESCRIPTOR.message_types_by_name['TollInfo']
_ROUTELEGSTEP = DESCRIPTOR.message_types_by_name['RouteLegStep']
_NAVIGATIONINSTRUCTION = DESCRIPTOR.message_types_by_name['NavigationInstruction']
_SPEEDREADINGINTERVAL = DESCRIPTOR.message_types_by_name['SpeedReadingInterval']
_SPEEDREADINGINTERVAL_SPEED = _SPEEDREADINGINTERVAL.enum_types_by_name['Speed']
Route = _reflection.GeneratedProtocolMessageType('Route', (_message.Message,), {
  'DESCRIPTOR' : _ROUTE,
  '__module__' : 'google.maps.routes.v1.route_pb2'
  # @@protoc_insertion_point(class_scope:google.maps.routes.v1.Route)
  })
_sym_db.RegisterMessage(Route)

RouteTravelAdvisory = _reflection.GeneratedProtocolMessageType('RouteTravelAdvisory', (_message.Message,), {
  'DESCRIPTOR' : _ROUTETRAVELADVISORY,
  '__module__' : 'google.maps.routes.v1.route_pb2'
  # @@protoc_insertion_point(class_scope:google.maps.routes.v1.RouteTravelAdvisory)
  })
_sym_db.RegisterMessage(RouteTravelAdvisory)

RouteLegTravelAdvisory = _reflection.GeneratedProtocolMessageType('RouteLegTravelAdvisory', (_message.Message,), {
  'DESCRIPTOR' : _ROUTELEGTRAVELADVISORY,
  '__module__' : 'google.maps.routes.v1.route_pb2'
  # @@protoc_insertion_point(class_scope:google.maps.routes.v1.RouteLegTravelAdvisory)
  })
_sym_db.RegisterMessage(RouteLegTravelAdvisory)

RouteLegStepTravelAdvisory = _reflection.GeneratedProtocolMessageType('RouteLegStepTravelAdvisory', (_message.Message,), {
  'DESCRIPTOR' : _ROUTELEGSTEPTRAVELADVISORY,
  '__module__' : 'google.maps.routes.v1.route_pb2'
  # @@protoc_insertion_point(class_scope:google.maps.routes.v1.RouteLegStepTravelAdvisory)
  })
_sym_db.RegisterMessage(RouteLegStepTravelAdvisory)

TrafficRestriction = _reflection.GeneratedProtocolMessageType('TrafficRestriction', (_message.Message,), {
  'DESCRIPTOR' : _TRAFFICRESTRICTION,
  '__module__' : 'google.maps.routes.v1.route_pb2'
  # @@protoc_insertion_point(class_scope:google.maps.routes.v1.TrafficRestriction)
  })
_sym_db.RegisterMessage(TrafficRestriction)

LicensePlateLastCharacterRestriction = _reflection.GeneratedProtocolMessageType('LicensePlateLastCharacterRestriction', (_message.Message,), {
  'DESCRIPTOR' : _LICENSEPLATELASTCHARACTERRESTRICTION,
  '__module__' : 'google.maps.routes.v1.route_pb2'
  # @@protoc_insertion_point(class_scope:google.maps.routes.v1.LicensePlateLastCharacterRestriction)
  })
_sym_db.RegisterMessage(LicensePlateLastCharacterRestriction)

RouteLeg = _reflection.GeneratedProtocolMessageType('RouteLeg', (_message.Message,), {
  'DESCRIPTOR' : _ROUTELEG,
  '__module__' : 'google.maps.routes.v1.route_pb2'
  # @@protoc_insertion_point(class_scope:google.maps.routes.v1.RouteLeg)
  })
_sym_db.RegisterMessage(RouteLeg)

TollInfo = _reflection.GeneratedProtocolMessageType('TollInfo', (_message.Message,), {
  'DESCRIPTOR' : _TOLLINFO,
  '__module__' : 'google.maps.routes.v1.route_pb2'
  # @@protoc_insertion_point(class_scope:google.maps.routes.v1.TollInfo)
  })
_sym_db.RegisterMessage(TollInfo)

RouteLegStep = _reflection.GeneratedProtocolMessageType('RouteLegStep', (_message.Message,), {
  'DESCRIPTOR' : _ROUTELEGSTEP,
  '__module__' : 'google.maps.routes.v1.route_pb2'
  # @@protoc_insertion_point(class_scope:google.maps.routes.v1.RouteLegStep)
  })
_sym_db.RegisterMessage(RouteLegStep)

NavigationInstruction = _reflection.GeneratedProtocolMessageType('NavigationInstruction', (_message.Message,), {
  'DESCRIPTOR' : _NAVIGATIONINSTRUCTION,
  '__module__' : 'google.maps.routes.v1.route_pb2'
  # @@protoc_insertion_point(class_scope:google.maps.routes.v1.NavigationInstruction)
  })
_sym_db.RegisterMessage(NavigationInstruction)

SpeedReadingInterval = _reflection.GeneratedProtocolMessageType('SpeedReadingInterval', (_message.Message,), {
  'DESCRIPTOR' : _SPEEDREADINGINTERVAL,
  '__module__' : 'google.maps.routes.v1.route_pb2'
  # @@protoc_insertion_point(class_scope:google.maps.routes.v1.SpeedReadingInterval)
  })
_sym_db.RegisterMessage(SpeedReadingInterval)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031com.google.maps.routes.v1B\nRouteProtoP\001Z;google.golang.org/genproto/googleapis/maps/routes/v1;routes\370\001\001\242\002\004GMRS\252\002\025Google.Maps.Routes.V1\312\002\025Google\\Maps\\Routes\\V1'
  _MANEUVER._serialized_start=3113
  _MANEUVER._serialized_end=3459
  _ROUTE._serialized_start=226
  _ROUTE._serialized_end=713
  _ROUTETRAVELADVISORY._serialized_start=716
  _ROUTETRAVELADVISORY._serialized_end=992
  _ROUTELEGTRAVELADVISORY._serialized_start=995
  _ROUTELEGTRAVELADVISORY._serialized_end=1182
  _ROUTELEGSTEPTRAVELADVISORY._serialized_start=1185
  _ROUTELEGSTEPTRAVELADVISORY._serialized_end=1314
  _TRAFFICRESTRICTION._serialized_start=1317
  _TRAFFICRESTRICTION._serialized_end=1487
  _LICENSEPLATELASTCHARACTERRESTRICTION._serialized_start=1489
  _LICENSEPLATELASTCHARACTERRESTRICTION._serialized_end=1583
  _ROUTELEG._serialized_start=1586
  _ROUTELEG._serialized_end=2108
  _TOLLINFO._serialized_start=2110
  _TOLLINFO._serialized_end=2181
  _ROUTELEGSTEP._serialized_start=2184
  _ROUTELEGSTEP._serialized_end=2701
  _NAVIGATIONINSTRUCTION._serialized_start=2703
  _NAVIGATIONINSTRUCTION._serialized_end=2823
  _SPEEDREADINGINTERVAL._serialized_start=2826
  _SPEEDREADINGINTERVAL._serialized_end=3110
  _SPEEDREADINGINTERVAL_SPEED._serialized_start=3041
  _SPEEDREADINGINTERVAL_SPEED._serialized_end=3110
# @@protoc_insertion_point(module_scope)
