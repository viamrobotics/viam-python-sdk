"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ....proto.api.common.v1 import common_pb2 as proto_dot_api_dot_common_dot_v1_dot_common__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18proto/api/v1/robot.proto\x12\x0cproto.api.v1\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1cgoogle/api/annotations.proto\x1a proto/api/common/v1/common.proto"\x0f\n\rStatusRequest"F\n\x13StatusStreamRequest\x12/\n\x05every\x18\x01 \x01(\x0b2\x19.google.protobuf.DurationR\x05every">\n\x0eStatusResponse\x12,\n\x06status\x18\x01 \x01(\x0b2\x14.proto.api.v1.StatusR\x06status"D\n\x14StatusStreamResponse\x12,\n\x06status\x18\x01 \x01(\x0b2\x14.proto.api.v1.StatusR\x06status"\x9b\r\n\x06Status\x122\n\x04arms\x18\x01 \x03(\x0b2\x1e.proto.api.v1.Status.ArmsEntryR\x04arms\x125\n\x05bases\x18\x02 \x03(\x0b2\x1f.proto.api.v1.Status.BasesEntryR\x05bases\x12>\n\x08grippers\x18\x03 \x03(\x0b2".proto.api.v1.Status.GrippersEntryR\x08grippers\x128\n\x06boards\x18\x04 \x03(\x0b2 .proto.api.v1.Status.BoardsEntryR\x06boards\x12;\n\x07cameras\x18\x05 \x03(\x0b2!.proto.api.v1.Status.CamerasEntryR\x07cameras\x12;\n\x07sensors\x18\x06 \x03(\x0b2!.proto.api.v1.Status.SensorsEntryR\x07sensors\x12A\n\tfunctions\x18\x07 \x03(\x0b2#.proto.api.v1.Status.FunctionsEntryR\tfunctions\x128\n\x06servos\x18\x08 \x03(\x0b2 .proto.api.v1.Status.ServosEntryR\x06servos\x128\n\x06motors\x18\t \x03(\x0b2 .proto.api.v1.Status.MotorsEntryR\x06motors\x12>\n\x08services\x18\n \x03(\x0b2".proto.api.v1.Status.ServicesEntryR\x08services\x12W\n\x11input_controllers\x18\x0b \x03(\x0b2*.proto.api.v1.Status.InputControllersEntryR\x10inputControllers\x12>\n\x08gantries\x18\x0c \x03(\x0b2".proto.api.v1.Status.GantriesEntryR\x08gantries\x1aP\n\tArmsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12-\n\x05value\x18\x02 \x01(\x0b2\x17.proto.api.v1.ArmStatusR\x05value:\x028\x01\x1a8\n\nBasesEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\x08R\x05value:\x028\x01\x1a;\n\rGrippersEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\x08R\x05value:\x028\x01\x1a[\n\x0bBoardsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x126\n\x05value\x18\x02 \x01(\x0b2 .proto.api.common.v1.BoardStatusR\x05value:\x028\x01\x1a:\n\x0cCamerasEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\x08R\x05value:\x028\x01\x1aV\n\x0cSensorsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x120\n\x05value\x18\x02 \x01(\x0b2\x1a.proto.api.v1.SensorStatusR\x05value:\x028\x01\x1a<\n\x0eFunctionsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\x08R\x05value:\x028\x01\x1aT\n\x0bServosEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12/\n\x05value\x18\x02 \x01(\x0b2\x19.proto.api.v1.ServoStatusR\x05value:\x028\x01\x1aT\n\x0bMotorsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12/\n\x05value\x18\x02 \x01(\x0b2\x19.proto.api.v1.MotorStatusR\x05value:\x028\x01\x1a;\n\rServicesEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\x08R\x05value:\x028\x01\x1ah\n\x15InputControllersEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x129\n\x05value\x18\x02 \x01(\x0b2#.proto.api.v1.InputControllerStatusR\x05value:\x028\x01\x1aW\n\rGantriesEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x120\n\x05value\x18\x02 \x01(\x0b2\x1a.proto.api.v1.GantryStatusR\x05value:\x028\x01"y\n\x0fComponentConfig\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x12\n\x04type\x18\x02 \x01(\tR\x04type\x12\x16\n\x06parent\x18\x03 \x01(\tR\x06parent\x12&\n\x04pose\x18\x04 \x01(\x0b2\x12.proto.api.v1.PoseR\x04pose"\x0f\n\rConfigRequest"O\n\x0eConfigResponse\x12=\n\ncomponents\x18\x01 \x03(\x0b2\x1d.proto.api.v1.ComponentConfigR\ncomponents"%\n\x0fDoActionRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name"\x12\n\x10DoActionResponse"F\n\x0cGantryStatus\x12\x1c\n\tpositions\x18\x01 \x03(\x01R\tpositions\x12\x18\n\x07lengths\x18\x02 \x03(\x01R\x07lengths"\x8b\x01\n\tArmStatus\x127\n\rgrid_position\x18\x01 \x01(\x0b2\x12.proto.api.v1.PoseR\x0cgridPosition\x12E\n\x0fjoint_positions\x18\x02 \x01(\x0b2\x1c.proto.api.v1.JointPositionsR\x0ejointPositions"y\n\x04Pose\x12\x0c\n\x01x\x18\x01 \x01(\x01R\x01x\x12\x0c\n\x01y\x18\x02 \x01(\x01R\x01y\x12\x0c\n\x01z\x18\x03 \x01(\x01R\x01z\x12\x0f\n\x03o_x\x18\x04 \x01(\x01R\x02oX\x12\x0f\n\x03o_y\x18\x05 \x01(\x01R\x02oY\x12\x0f\n\x03o_z\x18\x06 \x01(\x01R\x02oZ\x12\x14\n\x05theta\x18\x07 \x01(\x01R\x05theta"*\n\x0eJointPositions\x12\x18\n\x07degrees\x18\x01 \x03(\x01R\x07degrees""\n\x0cSensorStatus\x12\x12\n\x04type\x18\x01 \x01(\tR\x04type"+\n\x15SensorReadingsRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name"L\n\x16SensorReadingsResponse\x122\n\x08readings\x18\x01 \x03(\x0b2\x16.google.protobuf.ValueR\x08readings",\n\x16ExecuteFunctionRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name"}\n\x17ExecuteFunctionResponse\x120\n\x07results\x18\x01 \x03(\x0b2\x16.google.protobuf.ValueR\x07results\x12\x17\n\x07std_out\x18\x02 \x01(\tR\x06stdOut\x12\x17\n\x07std_err\x18\x03 \x01(\tR\x06stdErr"F\n\x14ExecuteSourceRequest\x12\x16\n\x06source\x18\x01 \x01(\tR\x06source\x12\x16\n\x06engine\x18\x02 \x01(\tR\x06engine"{\n\x15ExecuteSourceResponse\x120\n\x07results\x18\x01 \x03(\x0b2\x16.google.protobuf.ValueR\x07results\x12\x17\n\x07std_out\x18\x02 \x01(\tR\x06stdOut\x12\x17\n\x07std_err\x18\x03 \x01(\tR\x06stdErr"\xb4\x01\n\x0bMotorStatus\x12\x0e\n\x02on\x18\x01 \x01(\x08R\x02on\x12-\n\x12position_supported\x18\x02 \x01(\x08R\x11positionSupported\x12\x1a\n\x08position\x18\x03 \x01(\x01R\x08position\x12;\n\npid_config\x18\x04 \x01(\x0b2\x17.google.protobuf.StructH\x00R\tpidConfig\x88\x01\x01B\r\n\x0b_pid_config"#\n\x0bServoStatus\x12\x14\n\x05angle\x18\x01 \x01(\rR\x05angle"\x90\x01\n\x19ResourceRunCommandRequest\x12#\n\rresource_name\x18\x01 \x01(\tR\x0cresourceName\x12!\n\x0ccommand_name\x18\x02 \x01(\tR\x0bcommandName\x12+\n\x04args\x18\x03 \x01(\x0b2\x17.google.protobuf.StructR\x04args"M\n\x1aResourceRunCommandResponse\x12/\n\x06result\x18\x01 \x01(\x0b2\x17.google.protobuf.StructR\x06result"\x1e\n\x1cNavigationServiceModeRequest"X\n\x1dNavigationServiceModeResponse\x127\n\x04mode\x18\x01 \x01(\x0e2#.proto.api.v1.NavigationServiceModeR\x04mode"Z\n\x1fNavigationServiceSetModeRequest\x127\n\x04mode\x18\x01 \x01(\x0e2#.proto.api.v1.NavigationServiceModeR\x04mode""\n NavigationServiceSetModeResponse"f\n\x19NavigationServiceWaypoint\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x129\n\x08location\x18\x02 \x01(\x0b2\x1d.proto.api.common.v1.GeoPointR\x08location""\n NavigationServiceLocationRequest"^\n!NavigationServiceLocationResponse\x129\n\x08location\x18\x01 \x01(\x0b2\x1d.proto.api.common.v1.GeoPointR\x08location"#\n!NavigationServiceWaypointsRequest"k\n"NavigationServiceWaypointsResponse\x12E\n\twaypoints\x18\x01 \x03(\x0b2\'.proto.api.v1.NavigationServiceWaypointR\twaypoints"`\n#NavigationServiceAddWaypointRequest\x129\n\x08location\x18\x01 \x01(\x0b2\x1d.proto.api.common.v1.GeoPointR\x08location"&\n$NavigationServiceAddWaypointResponse"8\n&NavigationServiceRemoveWaypointRequest\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id")\n\'NavigationServiceRemoveWaypointResponse"\x8c\x01\n\x14InputControllerEvent\x12.\n\x04time\x18\x01 \x01(\x0b2\x1a.google.protobuf.TimestampR\x04time\x12\x14\n\x05event\x18\x02 \x01(\tR\x05event\x12\x18\n\x07control\x18\x03 \x01(\tR\x07control\x12\x14\n\x05value\x18\x04 \x01(\x01R\x05value"S\n\x15InputControllerStatus\x12:\n\x06events\x18\x01 \x03(\x0b2".proto.api.v1.InputControllerEventR\x06events*\x8a\x01\n\x15NavigationServiceMode\x12\'\n#NAVIGATION_SERVICE_MODE_UNSPECIFIED\x10\x00\x12"\n\x1eNAVIGATION_SERVICE_MODE_MANUAL\x10\x01\x12$\n NAVIGATION_SERVICE_MODE_WAYPOINT\x10\x022\x87\x10\n\x0cRobotService\x12[\n\x06Status\x12\x1b.proto.api.v1.StatusRequest\x1a\x1c.proto.api.v1.StatusResponse"\x16\x82\xd3\xe4\x93\x02\x10\x12\x0e/api/v1/status\x12v\n\x0cStatusStream\x12!.proto.api.v1.StatusStreamRequest\x1a".proto.api.v1.StatusStreamResponse"\x1d\x82\xd3\xe4\x93\x02\x17\x12\x15/api/v1/status_stream0\x01\x12[\n\x06Config\x12\x1b.proto.api.v1.ConfigRequest\x1a\x1c.proto.api.v1.ConfigResponse"\x16\x82\xd3\xe4\x93\x02\x10\x12\x0e/api/v1/config\x12d\n\x08DoAction\x12\x1d.proto.api.v1.DoActionRequest\x1a\x1e.proto.api.v1.DoActionResponse"\x19\x82\xd3\xe4\x93\x02\x13"\x11/api/v1/do_action\x12\x8b\x01\n\x0eSensorReadings\x12#.proto.api.v1.SensorReadingsRequest\x1a$.proto.api.v1.SensorReadingsResponse".\x82\xd3\xe4\x93\x02(\x12&/api/v1/sensors/sensor/{name}/readings\x12\x90\x01\n\x0fExecuteFunction\x12$.proto.api.v1.ExecuteFunctionRequest\x1a%.proto.api.v1.ExecuteFunctionResponse"0\x82\xd3\xe4\x93\x02*"(/api/v1/functions/by_name/{name}/execute\x12\x80\x01\n\rExecuteSource\x12".proto.api.v1.ExecuteSourceRequest\x1a#.proto.api.v1.ExecuteSourceResponse"&\x82\xd3\xe4\x93\x02 "\x1e/api/v1/functions/execute_code\x12\x9d\x01\n\x12ResourceRunCommand\x12\'.proto.api.v1.ResourceRunCommandRequest\x1a(.proto.api.v1.ResourceRunCommandResponse"4\x82\xd3\xe4\x93\x02.",/api/v1/resource/{resource_name}/run_command\x12\x9a\x01\n\x15NavigationServiceMode\x12*.proto.api.v1.NavigationServiceModeRequest\x1a+.proto.api.v1.NavigationServiceModeResponse"(\x82\xd3\xe4\x93\x02"\x12 /api/v1/services/navigation/mode\x12\xa3\x01\n\x18NavigationServiceSetMode\x12-.proto.api.v1.NavigationServiceSetModeRequest\x1a..proto.api.v1.NavigationServiceSetModeResponse"(\x82\xd3\xe4\x93\x02"\x1a /api/v1/services/navigation/mode\x12\xaa\x01\n\x19NavigationServiceLocation\x12..proto.api.v1.NavigationServiceLocationRequest\x1a/.proto.api.v1.NavigationServiceLocationResponse",\x82\xd3\xe4\x93\x02&\x12$/api/v1/services/navigation/location\x12\xae\x01\n\x1aNavigationServiceWaypoints\x12/.proto.api.v1.NavigationServiceWaypointsRequest\x1a0.proto.api.v1.NavigationServiceWaypointsResponse"-\x82\xd3\xe4\x93\x02\'\x12%/api/v1/services/navigation/waypoints\x12\xb4\x01\n\x1cNavigationServiceAddWaypoint\x121.proto.api.v1.NavigationServiceAddWaypointRequest\x1a2.proto.api.v1.NavigationServiceAddWaypointResponse"-\x82\xd3\xe4\x93\x02\'"%/api/v1/services/navigation/waypoints\x12\xc2\x01\n\x1fNavigationServiceRemoveWaypoint\x124.proto.api.v1.NavigationServiceRemoveWaypointRequest\x1a5.proto.api.v1.NavigationServiceRemoveWaypointResponse"2\x82\xd3\xe4\x93\x02,**/api/v1/services/navigation/waypoints/{id}B9\n\x19com.viam.rdk.proto.api.v1Z\x1cgo.viam.com/rdk/proto/api/v1b\x06proto3')
_NAVIGATIONSERVICEMODE = DESCRIPTOR.enum_types_by_name['NavigationServiceMode']
NavigationServiceMode = enum_type_wrapper.EnumTypeWrapper(_NAVIGATIONSERVICEMODE)
NAVIGATION_SERVICE_MODE_UNSPECIFIED = 0
NAVIGATION_SERVICE_MODE_MANUAL = 1
NAVIGATION_SERVICE_MODE_WAYPOINT = 2
_STATUSREQUEST = DESCRIPTOR.message_types_by_name['StatusRequest']
_STATUSSTREAMREQUEST = DESCRIPTOR.message_types_by_name['StatusStreamRequest']
_STATUSRESPONSE = DESCRIPTOR.message_types_by_name['StatusResponse']
_STATUSSTREAMRESPONSE = DESCRIPTOR.message_types_by_name['StatusStreamResponse']
_STATUS = DESCRIPTOR.message_types_by_name['Status']
_STATUS_ARMSENTRY = _STATUS.nested_types_by_name['ArmsEntry']
_STATUS_BASESENTRY = _STATUS.nested_types_by_name['BasesEntry']
_STATUS_GRIPPERSENTRY = _STATUS.nested_types_by_name['GrippersEntry']
_STATUS_BOARDSENTRY = _STATUS.nested_types_by_name['BoardsEntry']
_STATUS_CAMERASENTRY = _STATUS.nested_types_by_name['CamerasEntry']
_STATUS_SENSORSENTRY = _STATUS.nested_types_by_name['SensorsEntry']
_STATUS_FUNCTIONSENTRY = _STATUS.nested_types_by_name['FunctionsEntry']
_STATUS_SERVOSENTRY = _STATUS.nested_types_by_name['ServosEntry']
_STATUS_MOTORSENTRY = _STATUS.nested_types_by_name['MotorsEntry']
_STATUS_SERVICESENTRY = _STATUS.nested_types_by_name['ServicesEntry']
_STATUS_INPUTCONTROLLERSENTRY = _STATUS.nested_types_by_name['InputControllersEntry']
_STATUS_GANTRIESENTRY = _STATUS.nested_types_by_name['GantriesEntry']
_COMPONENTCONFIG = DESCRIPTOR.message_types_by_name['ComponentConfig']
_CONFIGREQUEST = DESCRIPTOR.message_types_by_name['ConfigRequest']
_CONFIGRESPONSE = DESCRIPTOR.message_types_by_name['ConfigResponse']
_DOACTIONREQUEST = DESCRIPTOR.message_types_by_name['DoActionRequest']
_DOACTIONRESPONSE = DESCRIPTOR.message_types_by_name['DoActionResponse']
_GANTRYSTATUS = DESCRIPTOR.message_types_by_name['GantryStatus']
_ARMSTATUS = DESCRIPTOR.message_types_by_name['ArmStatus']
_POSE = DESCRIPTOR.message_types_by_name['Pose']
_JOINTPOSITIONS = DESCRIPTOR.message_types_by_name['JointPositions']
_SENSORSTATUS = DESCRIPTOR.message_types_by_name['SensorStatus']
_SENSORREADINGSREQUEST = DESCRIPTOR.message_types_by_name['SensorReadingsRequest']
_SENSORREADINGSRESPONSE = DESCRIPTOR.message_types_by_name['SensorReadingsResponse']
_EXECUTEFUNCTIONREQUEST = DESCRIPTOR.message_types_by_name['ExecuteFunctionRequest']
_EXECUTEFUNCTIONRESPONSE = DESCRIPTOR.message_types_by_name['ExecuteFunctionResponse']
_EXECUTESOURCEREQUEST = DESCRIPTOR.message_types_by_name['ExecuteSourceRequest']
_EXECUTESOURCERESPONSE = DESCRIPTOR.message_types_by_name['ExecuteSourceResponse']
_MOTORSTATUS = DESCRIPTOR.message_types_by_name['MotorStatus']
_SERVOSTATUS = DESCRIPTOR.message_types_by_name['ServoStatus']
_RESOURCERUNCOMMANDREQUEST = DESCRIPTOR.message_types_by_name['ResourceRunCommandRequest']
_RESOURCERUNCOMMANDRESPONSE = DESCRIPTOR.message_types_by_name['ResourceRunCommandResponse']
_NAVIGATIONSERVICEMODEREQUEST = DESCRIPTOR.message_types_by_name['NavigationServiceModeRequest']
_NAVIGATIONSERVICEMODERESPONSE = DESCRIPTOR.message_types_by_name['NavigationServiceModeResponse']
_NAVIGATIONSERVICESETMODEREQUEST = DESCRIPTOR.message_types_by_name['NavigationServiceSetModeRequest']
_NAVIGATIONSERVICESETMODERESPONSE = DESCRIPTOR.message_types_by_name['NavigationServiceSetModeResponse']
_NAVIGATIONSERVICEWAYPOINT = DESCRIPTOR.message_types_by_name['NavigationServiceWaypoint']
_NAVIGATIONSERVICELOCATIONREQUEST = DESCRIPTOR.message_types_by_name['NavigationServiceLocationRequest']
_NAVIGATIONSERVICELOCATIONRESPONSE = DESCRIPTOR.message_types_by_name['NavigationServiceLocationResponse']
_NAVIGATIONSERVICEWAYPOINTSREQUEST = DESCRIPTOR.message_types_by_name['NavigationServiceWaypointsRequest']
_NAVIGATIONSERVICEWAYPOINTSRESPONSE = DESCRIPTOR.message_types_by_name['NavigationServiceWaypointsResponse']
_NAVIGATIONSERVICEADDWAYPOINTREQUEST = DESCRIPTOR.message_types_by_name['NavigationServiceAddWaypointRequest']
_NAVIGATIONSERVICEADDWAYPOINTRESPONSE = DESCRIPTOR.message_types_by_name['NavigationServiceAddWaypointResponse']
_NAVIGATIONSERVICEREMOVEWAYPOINTREQUEST = DESCRIPTOR.message_types_by_name['NavigationServiceRemoveWaypointRequest']
_NAVIGATIONSERVICEREMOVEWAYPOINTRESPONSE = DESCRIPTOR.message_types_by_name['NavigationServiceRemoveWaypointResponse']
_INPUTCONTROLLEREVENT = DESCRIPTOR.message_types_by_name['InputControllerEvent']
_INPUTCONTROLLERSTATUS = DESCRIPTOR.message_types_by_name['InputControllerStatus']
StatusRequest = _reflection.GeneratedProtocolMessageType('StatusRequest', (_message.Message,), {'DESCRIPTOR': _STATUSREQUEST, '__module__': 'proto.api.v1.robot_pb2'})
_sym_db.RegisterMessage(StatusRequest)
StatusStreamRequest = _reflection.GeneratedProtocolMessageType('StatusStreamRequest', (_message.Message,), {'DESCRIPTOR': _STATUSSTREAMREQUEST, '__module__': 'proto.api.v1.robot_pb2'})
_sym_db.RegisterMessage(StatusStreamRequest)
StatusResponse = _reflection.GeneratedProtocolMessageType('StatusResponse', (_message.Message,), {'DESCRIPTOR': _STATUSRESPONSE, '__module__': 'proto.api.v1.robot_pb2'})
_sym_db.RegisterMessage(StatusResponse)
StatusStreamResponse = _reflection.GeneratedProtocolMessageType('StatusStreamResponse', (_message.Message,), {'DESCRIPTOR': _STATUSSTREAMRESPONSE, '__module__': 'proto.api.v1.robot_pb2'})
_sym_db.RegisterMessage(StatusStreamResponse)
Status = _reflection.GeneratedProtocolMessageType('Status', (_message.Message,), {'ArmsEntry': _reflection.GeneratedProtocolMessageType('ArmsEntry', (_message.Message,), {'DESCRIPTOR': _STATUS_ARMSENTRY, '__module__': 'proto.api.v1.robot_pb2'}), 'BasesEntry': _reflection.GeneratedProtocolMessageType('BasesEntry', (_message.Message,), {'DESCRIPTOR': _STATUS_BASESENTRY, '__module__': 'proto.api.v1.robot_pb2'}), 'GrippersEntry': _reflection.GeneratedProtocolMessageType('GrippersEntry', (_message.Message,), {'DESCRIPTOR': _STATUS_GRIPPERSENTRY, '__module__': 'proto.api.v1.robot_pb2'}), 'BoardsEntry': _reflection.GeneratedProtocolMessageType('BoardsEntry', (_message.Message,), {'DESCRIPTOR': _STATUS_BOARDSENTRY, '__module__': 'proto.api.v1.robot_pb2'}), 'CamerasEntry': _reflection.GeneratedProtocolMessageType('CamerasEntry', (_message.Message,), {'DESCRIPTOR': _STATUS_CAMERASENTRY, '__module__': 'proto.api.v1.robot_pb2'}), 'SensorsEntry': _reflection.GeneratedProtocolMessageType('SensorsEntry', (_message.Message,), {'DESCRIPTOR': _STATUS_SENSORSENTRY, '__module__': 'proto.api.v1.robot_pb2'}), 'FunctionsEntry': _reflection.GeneratedProtocolMessageType('FunctionsEntry', (_message.Message,), {'DESCRIPTOR': _STATUS_FUNCTIONSENTRY, '__module__': 'proto.api.v1.robot_pb2'}), 'ServosEntry': _reflection.GeneratedProtocolMessageType('ServosEntry', (_message.Message,), {'DESCRIPTOR': _STATUS_SERVOSENTRY, '__module__': 'proto.api.v1.robot_pb2'}), 'MotorsEntry': _reflection.GeneratedProtocolMessageType('MotorsEntry', (_message.Message,), {'DESCRIPTOR': _STATUS_MOTORSENTRY, '__module__': 'proto.api.v1.robot_pb2'}), 'ServicesEntry': _reflection.GeneratedProtocolMessageType('ServicesEntry', (_message.Message,), {'DESCRIPTOR': _STATUS_SERVICESENTRY, '__module__': 'proto.api.v1.robot_pb2'}), 'InputControllersEntry': _reflection.GeneratedProtocolMessageType('InputControllersEntry', (_message.Message,), {'DESCRIPTOR': _STATUS_INPUTCONTROLLERSENTRY, '__module__': 'proto.api.v1.robot_pb2'}), 'GantriesEntry': _reflection.GeneratedProtocolMessageType('GantriesEntry', (_message.Message,), {'DESCRIPTOR': _STATUS_GANTRIESENTRY, '__module__': 'proto.api.v1.robot_pb2'}), 'DESCRIPTOR': _STATUS, '__module__': 'proto.api.v1.robot_pb2'})
_sym_db.RegisterMessage(Status)
_sym_db.RegisterMessage(Status.ArmsEntry)
_sym_db.RegisterMessage(Status.BasesEntry)
_sym_db.RegisterMessage(Status.GrippersEntry)
_sym_db.RegisterMessage(Status.BoardsEntry)
_sym_db.RegisterMessage(Status.CamerasEntry)
_sym_db.RegisterMessage(Status.SensorsEntry)
_sym_db.RegisterMessage(Status.FunctionsEntry)
_sym_db.RegisterMessage(Status.ServosEntry)
_sym_db.RegisterMessage(Status.MotorsEntry)
_sym_db.RegisterMessage(Status.ServicesEntry)
_sym_db.RegisterMessage(Status.InputControllersEntry)
_sym_db.RegisterMessage(Status.GantriesEntry)
ComponentConfig = _reflection.GeneratedProtocolMessageType('ComponentConfig', (_message.Message,), {'DESCRIPTOR': _COMPONENTCONFIG, '__module__': 'proto.api.v1.robot_pb2'})
_sym_db.RegisterMessage(ComponentConfig)
ConfigRequest = _reflection.GeneratedProtocolMessageType('ConfigRequest', (_message.Message,), {'DESCRIPTOR': _CONFIGREQUEST, '__module__': 'proto.api.v1.robot_pb2'})
_sym_db.RegisterMessage(ConfigRequest)
ConfigResponse = _reflection.GeneratedProtocolMessageType('ConfigResponse', (_message.Message,), {'DESCRIPTOR': _CONFIGRESPONSE, '__module__': 'proto.api.v1.robot_pb2'})
_sym_db.RegisterMessage(ConfigResponse)
DoActionRequest = _reflection.GeneratedProtocolMessageType('DoActionRequest', (_message.Message,), {'DESCRIPTOR': _DOACTIONREQUEST, '__module__': 'proto.api.v1.robot_pb2'})
_sym_db.RegisterMessage(DoActionRequest)
DoActionResponse = _reflection.GeneratedProtocolMessageType('DoActionResponse', (_message.Message,), {'DESCRIPTOR': _DOACTIONRESPONSE, '__module__': 'proto.api.v1.robot_pb2'})
_sym_db.RegisterMessage(DoActionResponse)
GantryStatus = _reflection.GeneratedProtocolMessageType('GantryStatus', (_message.Message,), {'DESCRIPTOR': _GANTRYSTATUS, '__module__': 'proto.api.v1.robot_pb2'})
_sym_db.RegisterMessage(GantryStatus)
ArmStatus = _reflection.GeneratedProtocolMessageType('ArmStatus', (_message.Message,), {'DESCRIPTOR': _ARMSTATUS, '__module__': 'proto.api.v1.robot_pb2'})
_sym_db.RegisterMessage(ArmStatus)
Pose = _reflection.GeneratedProtocolMessageType('Pose', (_message.Message,), {'DESCRIPTOR': _POSE, '__module__': 'proto.api.v1.robot_pb2'})
_sym_db.RegisterMessage(Pose)
JointPositions = _reflection.GeneratedProtocolMessageType('JointPositions', (_message.Message,), {'DESCRIPTOR': _JOINTPOSITIONS, '__module__': 'proto.api.v1.robot_pb2'})
_sym_db.RegisterMessage(JointPositions)
SensorStatus = _reflection.GeneratedProtocolMessageType('SensorStatus', (_message.Message,), {'DESCRIPTOR': _SENSORSTATUS, '__module__': 'proto.api.v1.robot_pb2'})
_sym_db.RegisterMessage(SensorStatus)
SensorReadingsRequest = _reflection.GeneratedProtocolMessageType('SensorReadingsRequest', (_message.Message,), {'DESCRIPTOR': _SENSORREADINGSREQUEST, '__module__': 'proto.api.v1.robot_pb2'})
_sym_db.RegisterMessage(SensorReadingsRequest)
SensorReadingsResponse = _reflection.GeneratedProtocolMessageType('SensorReadingsResponse', (_message.Message,), {'DESCRIPTOR': _SENSORREADINGSRESPONSE, '__module__': 'proto.api.v1.robot_pb2'})
_sym_db.RegisterMessage(SensorReadingsResponse)
ExecuteFunctionRequest = _reflection.GeneratedProtocolMessageType('ExecuteFunctionRequest', (_message.Message,), {'DESCRIPTOR': _EXECUTEFUNCTIONREQUEST, '__module__': 'proto.api.v1.robot_pb2'})
_sym_db.RegisterMessage(ExecuteFunctionRequest)
ExecuteFunctionResponse = _reflection.GeneratedProtocolMessageType('ExecuteFunctionResponse', (_message.Message,), {'DESCRIPTOR': _EXECUTEFUNCTIONRESPONSE, '__module__': 'proto.api.v1.robot_pb2'})
_sym_db.RegisterMessage(ExecuteFunctionResponse)
ExecuteSourceRequest = _reflection.GeneratedProtocolMessageType('ExecuteSourceRequest', (_message.Message,), {'DESCRIPTOR': _EXECUTESOURCEREQUEST, '__module__': 'proto.api.v1.robot_pb2'})
_sym_db.RegisterMessage(ExecuteSourceRequest)
ExecuteSourceResponse = _reflection.GeneratedProtocolMessageType('ExecuteSourceResponse', (_message.Message,), {'DESCRIPTOR': _EXECUTESOURCERESPONSE, '__module__': 'proto.api.v1.robot_pb2'})
_sym_db.RegisterMessage(ExecuteSourceResponse)
MotorStatus = _reflection.GeneratedProtocolMessageType('MotorStatus', (_message.Message,), {'DESCRIPTOR': _MOTORSTATUS, '__module__': 'proto.api.v1.robot_pb2'})
_sym_db.RegisterMessage(MotorStatus)
ServoStatus = _reflection.GeneratedProtocolMessageType('ServoStatus', (_message.Message,), {'DESCRIPTOR': _SERVOSTATUS, '__module__': 'proto.api.v1.robot_pb2'})
_sym_db.RegisterMessage(ServoStatus)
ResourceRunCommandRequest = _reflection.GeneratedProtocolMessageType('ResourceRunCommandRequest', (_message.Message,), {'DESCRIPTOR': _RESOURCERUNCOMMANDREQUEST, '__module__': 'proto.api.v1.robot_pb2'})
_sym_db.RegisterMessage(ResourceRunCommandRequest)
ResourceRunCommandResponse = _reflection.GeneratedProtocolMessageType('ResourceRunCommandResponse', (_message.Message,), {'DESCRIPTOR': _RESOURCERUNCOMMANDRESPONSE, '__module__': 'proto.api.v1.robot_pb2'})
_sym_db.RegisterMessage(ResourceRunCommandResponse)
NavigationServiceModeRequest = _reflection.GeneratedProtocolMessageType('NavigationServiceModeRequest', (_message.Message,), {'DESCRIPTOR': _NAVIGATIONSERVICEMODEREQUEST, '__module__': 'proto.api.v1.robot_pb2'})
_sym_db.RegisterMessage(NavigationServiceModeRequest)
NavigationServiceModeResponse = _reflection.GeneratedProtocolMessageType('NavigationServiceModeResponse', (_message.Message,), {'DESCRIPTOR': _NAVIGATIONSERVICEMODERESPONSE, '__module__': 'proto.api.v1.robot_pb2'})
_sym_db.RegisterMessage(NavigationServiceModeResponse)
NavigationServiceSetModeRequest = _reflection.GeneratedProtocolMessageType('NavigationServiceSetModeRequest', (_message.Message,), {'DESCRIPTOR': _NAVIGATIONSERVICESETMODEREQUEST, '__module__': 'proto.api.v1.robot_pb2'})
_sym_db.RegisterMessage(NavigationServiceSetModeRequest)
NavigationServiceSetModeResponse = _reflection.GeneratedProtocolMessageType('NavigationServiceSetModeResponse', (_message.Message,), {'DESCRIPTOR': _NAVIGATIONSERVICESETMODERESPONSE, '__module__': 'proto.api.v1.robot_pb2'})
_sym_db.RegisterMessage(NavigationServiceSetModeResponse)
NavigationServiceWaypoint = _reflection.GeneratedProtocolMessageType('NavigationServiceWaypoint', (_message.Message,), {'DESCRIPTOR': _NAVIGATIONSERVICEWAYPOINT, '__module__': 'proto.api.v1.robot_pb2'})
_sym_db.RegisterMessage(NavigationServiceWaypoint)
NavigationServiceLocationRequest = _reflection.GeneratedProtocolMessageType('NavigationServiceLocationRequest', (_message.Message,), {'DESCRIPTOR': _NAVIGATIONSERVICELOCATIONREQUEST, '__module__': 'proto.api.v1.robot_pb2'})
_sym_db.RegisterMessage(NavigationServiceLocationRequest)
NavigationServiceLocationResponse = _reflection.GeneratedProtocolMessageType('NavigationServiceLocationResponse', (_message.Message,), {'DESCRIPTOR': _NAVIGATIONSERVICELOCATIONRESPONSE, '__module__': 'proto.api.v1.robot_pb2'})
_sym_db.RegisterMessage(NavigationServiceLocationResponse)
NavigationServiceWaypointsRequest = _reflection.GeneratedProtocolMessageType('NavigationServiceWaypointsRequest', (_message.Message,), {'DESCRIPTOR': _NAVIGATIONSERVICEWAYPOINTSREQUEST, '__module__': 'proto.api.v1.robot_pb2'})
_sym_db.RegisterMessage(NavigationServiceWaypointsRequest)
NavigationServiceWaypointsResponse = _reflection.GeneratedProtocolMessageType('NavigationServiceWaypointsResponse', (_message.Message,), {'DESCRIPTOR': _NAVIGATIONSERVICEWAYPOINTSRESPONSE, '__module__': 'proto.api.v1.robot_pb2'})
_sym_db.RegisterMessage(NavigationServiceWaypointsResponse)
NavigationServiceAddWaypointRequest = _reflection.GeneratedProtocolMessageType('NavigationServiceAddWaypointRequest', (_message.Message,), {'DESCRIPTOR': _NAVIGATIONSERVICEADDWAYPOINTREQUEST, '__module__': 'proto.api.v1.robot_pb2'})
_sym_db.RegisterMessage(NavigationServiceAddWaypointRequest)
NavigationServiceAddWaypointResponse = _reflection.GeneratedProtocolMessageType('NavigationServiceAddWaypointResponse', (_message.Message,), {'DESCRIPTOR': _NAVIGATIONSERVICEADDWAYPOINTRESPONSE, '__module__': 'proto.api.v1.robot_pb2'})
_sym_db.RegisterMessage(NavigationServiceAddWaypointResponse)
NavigationServiceRemoveWaypointRequest = _reflection.GeneratedProtocolMessageType('NavigationServiceRemoveWaypointRequest', (_message.Message,), {'DESCRIPTOR': _NAVIGATIONSERVICEREMOVEWAYPOINTREQUEST, '__module__': 'proto.api.v1.robot_pb2'})
_sym_db.RegisterMessage(NavigationServiceRemoveWaypointRequest)
NavigationServiceRemoveWaypointResponse = _reflection.GeneratedProtocolMessageType('NavigationServiceRemoveWaypointResponse', (_message.Message,), {'DESCRIPTOR': _NAVIGATIONSERVICEREMOVEWAYPOINTRESPONSE, '__module__': 'proto.api.v1.robot_pb2'})
_sym_db.RegisterMessage(NavigationServiceRemoveWaypointResponse)
InputControllerEvent = _reflection.GeneratedProtocolMessageType('InputControllerEvent', (_message.Message,), {'DESCRIPTOR': _INPUTCONTROLLEREVENT, '__module__': 'proto.api.v1.robot_pb2'})
_sym_db.RegisterMessage(InputControllerEvent)
InputControllerStatus = _reflection.GeneratedProtocolMessageType('InputControllerStatus', (_message.Message,), {'DESCRIPTOR': _INPUTCONTROLLERSTATUS, '__module__': 'proto.api.v1.robot_pb2'})
_sym_db.RegisterMessage(InputControllerStatus)
_ROBOTSERVICE = DESCRIPTOR.services_by_name['RobotService']
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n\x19com.viam.rdk.proto.api.v1Z\x1cgo.viam.com/rdk/proto/api/v1'
    _STATUS_ARMSENTRY._options = None
    _STATUS_ARMSENTRY._serialized_options = b'8\x01'
    _STATUS_BASESENTRY._options = None
    _STATUS_BASESENTRY._serialized_options = b'8\x01'
    _STATUS_GRIPPERSENTRY._options = None
    _STATUS_GRIPPERSENTRY._serialized_options = b'8\x01'
    _STATUS_BOARDSENTRY._options = None
    _STATUS_BOARDSENTRY._serialized_options = b'8\x01'
    _STATUS_CAMERASENTRY._options = None
    _STATUS_CAMERASENTRY._serialized_options = b'8\x01'
    _STATUS_SENSORSENTRY._options = None
    _STATUS_SENSORSENTRY._serialized_options = b'8\x01'
    _STATUS_FUNCTIONSENTRY._options = None
    _STATUS_FUNCTIONSENTRY._serialized_options = b'8\x01'
    _STATUS_SERVOSENTRY._options = None
    _STATUS_SERVOSENTRY._serialized_options = b'8\x01'
    _STATUS_MOTORSENTRY._options = None
    _STATUS_MOTORSENTRY._serialized_options = b'8\x01'
    _STATUS_SERVICESENTRY._options = None
    _STATUS_SERVICESENTRY._serialized_options = b'8\x01'
    _STATUS_INPUTCONTROLLERSENTRY._options = None
    _STATUS_INPUTCONTROLLERSENTRY._serialized_options = b'8\x01'
    _STATUS_GANTRIESENTRY._options = None
    _STATUS_GANTRIESENTRY._serialized_options = b'8\x01'
    _ROBOTSERVICE.methods_by_name['Status']._options = None
    _ROBOTSERVICE.methods_by_name['Status']._serialized_options = b'\x82\xd3\xe4\x93\x02\x10\x12\x0e/api/v1/status'
    _ROBOTSERVICE.methods_by_name['StatusStream']._options = None
    _ROBOTSERVICE.methods_by_name['StatusStream']._serialized_options = b'\x82\xd3\xe4\x93\x02\x17\x12\x15/api/v1/status_stream'
    _ROBOTSERVICE.methods_by_name['Config']._options = None
    _ROBOTSERVICE.methods_by_name['Config']._serialized_options = b'\x82\xd3\xe4\x93\x02\x10\x12\x0e/api/v1/config'
    _ROBOTSERVICE.methods_by_name['DoAction']._options = None
    _ROBOTSERVICE.methods_by_name['DoAction']._serialized_options = b'\x82\xd3\xe4\x93\x02\x13"\x11/api/v1/do_action'
    _ROBOTSERVICE.methods_by_name['SensorReadings']._options = None
    _ROBOTSERVICE.methods_by_name['SensorReadings']._serialized_options = b'\x82\xd3\xe4\x93\x02(\x12&/api/v1/sensors/sensor/{name}/readings'
    _ROBOTSERVICE.methods_by_name['ExecuteFunction']._options = None
    _ROBOTSERVICE.methods_by_name['ExecuteFunction']._serialized_options = b'\x82\xd3\xe4\x93\x02*"(/api/v1/functions/by_name/{name}/execute'
    _ROBOTSERVICE.methods_by_name['ExecuteSource']._options = None
    _ROBOTSERVICE.methods_by_name['ExecuteSource']._serialized_options = b'\x82\xd3\xe4\x93\x02 "\x1e/api/v1/functions/execute_code'
    _ROBOTSERVICE.methods_by_name['ResourceRunCommand']._options = None
    _ROBOTSERVICE.methods_by_name['ResourceRunCommand']._serialized_options = b'\x82\xd3\xe4\x93\x02.",/api/v1/resource/{resource_name}/run_command'
    _ROBOTSERVICE.methods_by_name['NavigationServiceMode']._options = None
    _ROBOTSERVICE.methods_by_name['NavigationServiceMode']._serialized_options = b'\x82\xd3\xe4\x93\x02"\x12 /api/v1/services/navigation/mode'
    _ROBOTSERVICE.methods_by_name['NavigationServiceSetMode']._options = None
    _ROBOTSERVICE.methods_by_name['NavigationServiceSetMode']._serialized_options = b'\x82\xd3\xe4\x93\x02"\x1a /api/v1/services/navigation/mode'
    _ROBOTSERVICE.methods_by_name['NavigationServiceLocation']._options = None
    _ROBOTSERVICE.methods_by_name['NavigationServiceLocation']._serialized_options = b'\x82\xd3\xe4\x93\x02&\x12$/api/v1/services/navigation/location'
    _ROBOTSERVICE.methods_by_name['NavigationServiceWaypoints']._options = None
    _ROBOTSERVICE.methods_by_name['NavigationServiceWaypoints']._serialized_options = b"\x82\xd3\xe4\x93\x02'\x12%/api/v1/services/navigation/waypoints"
    _ROBOTSERVICE.methods_by_name['NavigationServiceAddWaypoint']._options = None
    _ROBOTSERVICE.methods_by_name['NavigationServiceAddWaypoint']._serialized_options = b'\x82\xd3\xe4\x93\x02\'"%/api/v1/services/navigation/waypoints'
    _ROBOTSERVICE.methods_by_name['NavigationServiceRemoveWaypoint']._options = None
    _ROBOTSERVICE.methods_by_name['NavigationServiceRemoveWaypoint']._serialized_options = b'\x82\xd3\xe4\x93\x02,**/api/v1/services/navigation/waypoints/{id}'
    _NAVIGATIONSERVICEMODE._serialized_start = 4854
    _NAVIGATIONSERVICEMODE._serialized_end = 4992
    _STATUSREQUEST._serialized_start = 201
    _STATUSREQUEST._serialized_end = 216
    _STATUSSTREAMREQUEST._serialized_start = 218
    _STATUSSTREAMREQUEST._serialized_end = 288
    _STATUSRESPONSE._serialized_start = 290
    _STATUSRESPONSE._serialized_end = 352
    _STATUSSTREAMRESPONSE._serialized_start = 354
    _STATUSSTREAMRESPONSE._serialized_end = 422
    _STATUS._serialized_start = 425
    _STATUS._serialized_end = 2116
    _STATUS_ARMSENTRY._serialized_start = 1186
    _STATUS_ARMSENTRY._serialized_end = 1266
    _STATUS_BASESENTRY._serialized_start = 1268
    _STATUS_BASESENTRY._serialized_end = 1324
    _STATUS_GRIPPERSENTRY._serialized_start = 1326
    _STATUS_GRIPPERSENTRY._serialized_end = 1385
    _STATUS_BOARDSENTRY._serialized_start = 1387
    _STATUS_BOARDSENTRY._serialized_end = 1478
    _STATUS_CAMERASENTRY._serialized_start = 1480
    _STATUS_CAMERASENTRY._serialized_end = 1538
    _STATUS_SENSORSENTRY._serialized_start = 1540
    _STATUS_SENSORSENTRY._serialized_end = 1626
    _STATUS_FUNCTIONSENTRY._serialized_start = 1628
    _STATUS_FUNCTIONSENTRY._serialized_end = 1688
    _STATUS_SERVOSENTRY._serialized_start = 1690
    _STATUS_SERVOSENTRY._serialized_end = 1774
    _STATUS_MOTORSENTRY._serialized_start = 1776
    _STATUS_MOTORSENTRY._serialized_end = 1860
    _STATUS_SERVICESENTRY._serialized_start = 1862
    _STATUS_SERVICESENTRY._serialized_end = 1921
    _STATUS_INPUTCONTROLLERSENTRY._serialized_start = 1923
    _STATUS_INPUTCONTROLLERSENTRY._serialized_end = 2027
    _STATUS_GANTRIESENTRY._serialized_start = 2029
    _STATUS_GANTRIESENTRY._serialized_end = 2116
    _COMPONENTCONFIG._serialized_start = 2118
    _COMPONENTCONFIG._serialized_end = 2239
    _CONFIGREQUEST._serialized_start = 2241
    _CONFIGREQUEST._serialized_end = 2256
    _CONFIGRESPONSE._serialized_start = 2258
    _CONFIGRESPONSE._serialized_end = 2337
    _DOACTIONREQUEST._serialized_start = 2339
    _DOACTIONREQUEST._serialized_end = 2376
    _DOACTIONRESPONSE._serialized_start = 2378
    _DOACTIONRESPONSE._serialized_end = 2396
    _GANTRYSTATUS._serialized_start = 2398
    _GANTRYSTATUS._serialized_end = 2468
    _ARMSTATUS._serialized_start = 2471
    _ARMSTATUS._serialized_end = 2610
    _POSE._serialized_start = 2612
    _POSE._serialized_end = 2733
    _JOINTPOSITIONS._serialized_start = 2735
    _JOINTPOSITIONS._serialized_end = 2777
    _SENSORSTATUS._serialized_start = 2779
    _SENSORSTATUS._serialized_end = 2813
    _SENSORREADINGSREQUEST._serialized_start = 2815
    _SENSORREADINGSREQUEST._serialized_end = 2858
    _SENSORREADINGSRESPONSE._serialized_start = 2860
    _SENSORREADINGSRESPONSE._serialized_end = 2936
    _EXECUTEFUNCTIONREQUEST._serialized_start = 2938
    _EXECUTEFUNCTIONREQUEST._serialized_end = 2982
    _EXECUTEFUNCTIONRESPONSE._serialized_start = 2984
    _EXECUTEFUNCTIONRESPONSE._serialized_end = 3109
    _EXECUTESOURCEREQUEST._serialized_start = 3111
    _EXECUTESOURCEREQUEST._serialized_end = 3181
    _EXECUTESOURCERESPONSE._serialized_start = 3183
    _EXECUTESOURCERESPONSE._serialized_end = 3306
    _MOTORSTATUS._serialized_start = 3309
    _MOTORSTATUS._serialized_end = 3489
    _SERVOSTATUS._serialized_start = 3491
    _SERVOSTATUS._serialized_end = 3526
    _RESOURCERUNCOMMANDREQUEST._serialized_start = 3529
    _RESOURCERUNCOMMANDREQUEST._serialized_end = 3673
    _RESOURCERUNCOMMANDRESPONSE._serialized_start = 3675
    _RESOURCERUNCOMMANDRESPONSE._serialized_end = 3752
    _NAVIGATIONSERVICEMODEREQUEST._serialized_start = 3754
    _NAVIGATIONSERVICEMODEREQUEST._serialized_end = 3784
    _NAVIGATIONSERVICEMODERESPONSE._serialized_start = 3786
    _NAVIGATIONSERVICEMODERESPONSE._serialized_end = 3874
    _NAVIGATIONSERVICESETMODEREQUEST._serialized_start = 3876
    _NAVIGATIONSERVICESETMODEREQUEST._serialized_end = 3966
    _NAVIGATIONSERVICESETMODERESPONSE._serialized_start = 3968
    _NAVIGATIONSERVICESETMODERESPONSE._serialized_end = 4002
    _NAVIGATIONSERVICEWAYPOINT._serialized_start = 4004
    _NAVIGATIONSERVICEWAYPOINT._serialized_end = 4106
    _NAVIGATIONSERVICELOCATIONREQUEST._serialized_start = 4108
    _NAVIGATIONSERVICELOCATIONREQUEST._serialized_end = 4142
    _NAVIGATIONSERVICELOCATIONRESPONSE._serialized_start = 4144
    _NAVIGATIONSERVICELOCATIONRESPONSE._serialized_end = 4238
    _NAVIGATIONSERVICEWAYPOINTSREQUEST._serialized_start = 4240
    _NAVIGATIONSERVICEWAYPOINTSREQUEST._serialized_end = 4275
    _NAVIGATIONSERVICEWAYPOINTSRESPONSE._serialized_start = 4277
    _NAVIGATIONSERVICEWAYPOINTSRESPONSE._serialized_end = 4384
    _NAVIGATIONSERVICEADDWAYPOINTREQUEST._serialized_start = 4386
    _NAVIGATIONSERVICEADDWAYPOINTREQUEST._serialized_end = 4482
    _NAVIGATIONSERVICEADDWAYPOINTRESPONSE._serialized_start = 4484
    _NAVIGATIONSERVICEADDWAYPOINTRESPONSE._serialized_end = 4522
    _NAVIGATIONSERVICEREMOVEWAYPOINTREQUEST._serialized_start = 4524
    _NAVIGATIONSERVICEREMOVEWAYPOINTREQUEST._serialized_end = 4580
    _NAVIGATIONSERVICEREMOVEWAYPOINTRESPONSE._serialized_start = 4582
    _NAVIGATIONSERVICEREMOVEWAYPOINTRESPONSE._serialized_end = 4623
    _INPUTCONTROLLEREVENT._serialized_start = 4626
    _INPUTCONTROLLEREVENT._serialized_end = 4766
    _INPUTCONTROLLERSTATUS._serialized_start = 4768
    _INPUTCONTROLLERSTATUS._serialized_end = 4851
    _ROBOTSERVICE._serialized_start = 4995
    _ROBOTSERVICE._serialized_end = 7050