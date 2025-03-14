"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 2, '', 'robot/v1/robot.proto')
_sym_db = _symbol_database.Default()
from ...common.v1 import common_pb2 as common_dot_v1_dot_common__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14robot/v1/robot.proto\x12\rviam.robot.v1\x1a\x16common/v1/common.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto"N\n\rTunnelRequest\x12)\n\x10destination_port\x18\x01 \x01(\rR\x0fdestinationPort\x12\x12\n\x04data\x18\x02 \x01(\x0cR\x04data"$\n\x0eTunnelResponse\x12\x12\n\x04data\x18\x01 \x01(\x0cR\x04data"\x14\n\x12ListTunnelsRequest"F\n\x13ListTunnelsResponse\x12/\n\x07tunnels\x18\x01 \x03(\x0b2\x15.viam.robot.v1.TunnelR\x07tunnels"f\n\x06Tunnel\x12\x12\n\x04port\x18\x01 \x01(\rR\x04port\x12H\n\x12connection_timeout\x18\x02 \x01(\x0b2\x19.google.protobuf.DurationR\x11connectionTimeout"}\n\x11FrameSystemConfig\x12/\n\x05frame\x18\x01 \x01(\x0b2\x19.viam.common.v1.TransformR\x05frame\x127\n\nkinematics\x18\x02 \x01(\x0b2\x17.google.protobuf.StructR\nkinematics"n\n\x18FrameSystemConfigRequest\x12R\n\x17supplemental_transforms\x18\x01 \x03(\x0b2\x19.viam.common.v1.TransformR\x16supplementalTransforms"o\n\x19FrameSystemConfigResponse\x12R\n\x14frame_system_configs\x18\x01 \x03(\x0b2 .viam.robot.v1.FrameSystemConfigR\x12frameSystemConfigs"\xc1\x01\n\x14TransformPoseRequest\x123\n\x06source\x18\x01 \x01(\x0b2\x1b.viam.common.v1.PoseInFrameR\x06source\x12 \n\x0bdestination\x18\x02 \x01(\tR\x0bdestination\x12R\n\x17supplemental_transforms\x18\x03 \x03(\x0b2\x19.viam.common.v1.TransformR\x16supplementalTransforms"H\n\x15TransformPoseResponse\x12/\n\x04pose\x18\x01 \x01(\x0b2\x1b.viam.common.v1.PoseInFrameR\x04pose"w\n\x13TransformPCDRequest\x12&\n\x0fpoint_cloud_pcd\x18\x01 \x01(\x0cR\rpointCloudPcd\x12\x16\n\x06source\x18\x02 \x01(\tR\x06source\x12 \n\x0bdestination\x18\x03 \x01(\tR\x0bdestination">\n\x14TransformPCDResponse\x12&\n\x0fpoint_cloud_pcd\x18\x01 \x01(\x0cR\rpointCloudPcd"\x16\n\x14ResourceNamesRequest"S\n\x15ResourceNamesResponse\x12:\n\tresources\x18\x01 \x03(\x0b2\x1c.viam.common.v1.ResourceNameR\tresources"q\n\x12ResourceRPCSubtype\x126\n\x07subtype\x18\x01 \x01(\x0b2\x1c.viam.common.v1.ResourceNameR\x07subtype\x12#\n\rproto_service\x18\x02 \x01(\tR\x0cprotoService"\x1c\n\x1aResourceRPCSubtypesRequest"t\n\x1bResourceRPCSubtypesResponse\x12U\n\x15resource_rpc_subtypes\x18\x01 \x03(\x0b2!.viam.robot.v1.ResourceRPCSubtypeR\x13resourceRpcSubtypes"\xd3\x01\n\tOperation\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x16\n\x06method\x18\x02 \x01(\tR\x06method\x125\n\targuments\x18\x03 \x01(\x0b2\x17.google.protobuf.StructR\targuments\x124\n\x07started\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampR\x07started\x12"\n\nsession_id\x18\x05 \x01(\tH\x00R\tsessionId\x88\x01\x01B\r\n\x0b_session_id"\x16\n\x14GetOperationsRequest"Q\n\x15GetOperationsResponse\x128\n\noperations\x18\x01 \x03(\x0b2\x18.viam.robot.v1.OperationR\noperations"(\n\x16CancelOperationRequest\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id"\x19\n\x17CancelOperationResponse"*\n\x18BlockForOperationRequest\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id"\x1b\n\x19BlockForOperationResponse"\xc6\x01\n\x12PeerConnectionInfo\x125\n\x04type\x18\x01 \x01(\x0e2!.viam.robot.v1.PeerConnectionTypeR\x04type\x12*\n\x0eremote_address\x18\x02 \x01(\tH\x00R\rremoteAddress\x88\x01\x01\x12(\n\rlocal_address\x18\x03 \x01(\tH\x01R\x0clocalAddress\x88\x01\x01B\x11\n\x0f_remote_addressB\x10\n\x0e_local_address"\x8c\x01\n\x07Session\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12X\n\x14peer_connection_info\x18\x02 \x01(\x0b2!.viam.robot.v1.PeerConnectionInfoH\x00R\x12peerConnectionInfo\x88\x01\x01B\x17\n\x15_peer_connection_info"\x14\n\x12GetSessionsRequest"I\n\x13GetSessionsResponse\x122\n\x08sessions\x18\x01 \x03(\x0b2\x16.viam.robot.v1.SessionR\x08sessions"\x82\x01\n\x0bModuleModel\x12\x1f\n\x0bmodule_name\x18\x01 \x01(\tR\nmoduleName\x12\x14\n\x05model\x18\x02 \x01(\tR\x05model\x12\x10\n\x03api\x18\x03 \x01(\tR\x03api\x12*\n\x11from_local_module\x18\x04 \x01(\x08R\x0ffromLocalModule"\x1d\n\x1bGetModelsFromModulesRequest"R\n\x1cGetModelsFromModulesResponse\x122\n\x06models\x18\x01 \x03(\x0b2\x1a.viam.robot.v1.ModuleModelR\x06models"\xb4\x01\n\x06Status\x120\n\x04name\x18\x01 \x01(\x0b2\x1c.viam.common.v1.ResourceNameR\x04name\x12/\n\x06status\x18\x02 \x01(\x0b2\x17.google.protobuf.StructR\x06status\x12G\n\x11last_reconfigured\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampR\x10lastReconfigured"W\n\x10GetStatusRequest\x12C\n\x0eresource_names\x18\x01 \x03(\x0b2\x1c.viam.common.v1.ResourceNameR\rresourceNames"B\n\x11GetStatusResponse\x12-\n\x06status\x18\x01 \x03(\x0b2\x15.viam.robot.v1.StatusR\x06status"\x8b\x01\n\x13StreamStatusRequest\x12C\n\x0eresource_names\x18\x01 \x03(\x0b2\x1c.viam.common.v1.ResourceNameR\rresourceNames\x12/\n\x05every\x18\x02 \x01(\x0b2\x19.google.protobuf.DurationR\x05every"E\n\x14StreamStatusResponse\x12-\n\x06status\x18\x01 \x03(\x0b2\x15.viam.robot.v1.StatusR\x06status"x\n\x13StopExtraParameters\x120\n\x04name\x18\x01 \x01(\x0b2\x1c.viam.common.v1.ResourceNameR\x04name\x12/\n\x06params\x18\x02 \x01(\x0b2\x17.google.protobuf.StructR\x06params"J\n\x0eStopAllRequest\x128\n\x05extra\x18c \x03(\x0b2".viam.robot.v1.StopExtraParametersR\x05extra"\x11\n\x0fStopAllResponse"-\n\x13StartSessionRequest\x12\x16\n\x06resume\x18\x01 \x01(\tR\x06resume"l\n\x14StartSessionResponse\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12D\n\x10heartbeat_window\x18\x02 \x01(\x0b2\x19.google.protobuf.DurationR\x0fheartbeatWindow"-\n\x1bSendSessionHeartbeatRequest\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id"\x1e\n\x1cSendSessionHeartbeatResponse":\n\nLogRequest\x12,\n\x04logs\x18\x01 \x03(\x0b2\x18.viam.common.v1.LogEntryR\x04logs"\r\n\x0bLogResponse"\x19\n\x17GetCloudMetadataRequest"\xd0\x01\n\x18GetCloudMetadataResponse\x12&\n\rrobot_part_id\x18\x01 \x01(\tB\x02\x18\x01R\x0brobotPartId\x12$\n\x0eprimary_org_id\x18\x02 \x01(\tR\x0cprimaryOrgId\x12\x1f\n\x0blocation_id\x18\x03 \x01(\tR\nlocationId\x12\x1d\n\nmachine_id\x18\x04 \x01(\tR\tmachineId\x12&\n\x0fmachine_part_id\x18\x05 \x01(\tR\rmachinePartId"f\n\x14RestartModuleRequest\x12\x1d\n\tmodule_id\x18\x01 \x01(\tH\x00R\x08moduleId\x12!\n\x0bmodule_name\x18\x02 \x01(\tH\x00R\nmoduleNameB\x0c\n\nid_or_name"\x17\n\x15RestartModuleResponse"\x11\n\x0fShutdownRequest"\x12\n\x10ShutdownResponse"\x19\n\x17GetMachineStatusRequest"\x9c\x02\n\x18GetMachineStatusResponse\x12;\n\tresources\x18\x01 \x03(\x0b2\x1d.viam.robot.v1.ResourceStatusR\tresources\x123\n\x06config\x18\x02 \x01(\x0b2\x1b.viam.robot.v1.ConfigStatusR\x06config\x12C\n\x05state\x18\x03 \x01(\x0e2-.viam.robot.v1.GetMachineStatusResponse.StateR\x05state"I\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x16\n\x12STATE_INITIALIZING\x10\x01\x12\x11\n\rSTATE_RUNNING\x10\x02"\xe0\x03\n\x0eResourceStatus\x120\n\x04name\x18\x01 \x01(\x0b2\x1c.viam.common.v1.ResourceNameR\x04name\x129\n\x05state\x18\x02 \x01(\x0e2#.viam.robot.v1.ResourceStatus.StateR\x05state\x12=\n\x0clast_updated\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampR\x0blastUpdated\x12\x1a\n\x08revision\x18\x04 \x01(\tR\x08revision\x12\x14\n\x05error\x18\x05 \x01(\tR\x05error\x12S\n\x0ecloud_metadata\x18\x06 \x01(\x0b2\'.viam.robot.v1.GetCloudMetadataResponseH\x00R\rcloudMetadata\x88\x01\x01"\x87\x01\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x16\n\x12STATE_UNCONFIGURED\x10\x01\x12\x15\n\x11STATE_CONFIGURING\x10\x02\x12\x0f\n\x0bSTATE_READY\x10\x03\x12\x12\n\x0eSTATE_REMOVING\x10\x04\x12\x13\n\x0fSTATE_UNHEALTHY\x10\x05B\x11\n\x0f_cloud_metadata"i\n\x0cConfigStatus\x12\x1a\n\x08revision\x18\x01 \x01(\tR\x08revision\x12=\n\x0clast_updated\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampR\x0blastUpdated"\x13\n\x11GetVersionRequest"k\n\x12GetVersionResponse\x12\x1a\n\x08platform\x18\x01 \x01(\tR\x08platform\x12\x18\n\x07version\x18\x02 \x01(\tR\x07version\x12\x1f\n\x0bapi_version\x18\x03 \x01(\tR\napiVersion*z\n\x12PeerConnectionType\x12$\n PEER_CONNECTION_TYPE_UNSPECIFIED\x10\x00\x12\x1d\n\x19PEER_CONNECTION_TYPE_GRPC\x10\x01\x12\x1f\n\x1bPEER_CONNECTION_TYPE_WEBRTC\x10\x022\x8e\x17\n\x0cRobotService\x12\x80\x01\n\rGetOperations\x12#.viam.robot.v1.GetOperationsRequest\x1a$.viam.robot.v1.GetOperationsResponse"$\x82\xd3\xe4\x93\x02\x1e\x12\x1c/viam/api/v1/operations/list\x12x\n\x0bGetSessions\x12!.viam.robot.v1.GetSessionsRequest\x1a".viam.robot.v1.GetSessionsResponse""\x82\xd3\xe4\x93\x02\x1c\x12\x1a/viam/api/v1/sessions/list\x12\x7f\n\rResourceNames\x12#.viam.robot.v1.ResourceNamesRequest\x1a$.viam.robot.v1.ResourceNamesResponse"#\x82\xd3\xe4\x93\x02\x1d\x12\x1b/viam/api/v1/resources/list\x12\x9d\x01\n\x13ResourceRPCSubtypes\x12).viam.robot.v1.ResourceRPCSubtypesRequest\x1a*.viam.robot.v1.ResourceRPCSubtypesResponse"/\x82\xd3\xe4\x93\x02)\x12\'/viam/api/v1/resource_rpc_subtypes/list\x12\x88\x01\n\x0fCancelOperation\x12%.viam.robot.v1.CancelOperationRequest\x1a&.viam.robot.v1.CancelOperationResponse"&\x82\xd3\xe4\x93\x02 "\x1e/viam/api/v1/operations/cancel\x12\x8d\x01\n\x11BlockForOperation\x12\'.viam.robot.v1.BlockForOperationRequest\x1a(.viam.robot.v1.BlockForOperationResponse"%\x82\xd3\xe4\x93\x02\x1f"\x1d/viam/api/v1/operations/block\x12\x93\x01\n\x14GetModelsFromModules\x12*.viam.robot.v1.GetModelsFromModulesRequest\x1a+.viam.robot.v1.GetModelsFromModulesResponse""\x82\xd3\xe4\x93\x02\x1c\x12\x1a/viam/api/v1/module_models\x12\x90\x01\n\x11FrameSystemConfig\x12\'.viam.robot.v1.FrameSystemConfigRequest\x1a(.viam.robot.v1.FrameSystemConfigResponse"(\x82\xd3\xe4\x93\x02"\x12 /viam/api/v1/frame_system/config\x12\x8c\x01\n\rTransformPose\x12#.viam.robot.v1.TransformPoseRequest\x1a$.viam.robot.v1.TransformPoseResponse"0\x82\xd3\xe4\x93\x02*\x12(/viam/api/v1/frame_system/transform_pose\x12\x88\x01\n\x0cTransformPCD\x12".viam.robot.v1.TransformPCDRequest\x1a#.viam.robot.v1.TransformPCDResponse"/\x82\xd3\xe4\x93\x02)\x12\'/viam/api/v1/frame_system/transform_pcd\x12n\n\tGetStatus\x12\x1f.viam.robot.v1.GetStatusRequest\x1a .viam.robot.v1.GetStatusResponse"\x1e\x88\x02\x01\x82\xd3\xe4\x93\x02\x15\x12\x13/viam/api/v1/status\x12\x80\x01\n\x0cStreamStatus\x12".viam.robot.v1.StreamStatusRequest\x1a#.viam.robot.v1.StreamStatusResponse"%\x88\x02\x01\x82\xd3\xe4\x93\x02\x1c\x12\x1a/viam/api/v1/status/stream0\x01\x12g\n\x07StopAll\x12\x1d.viam.robot.v1.StopAllRequest\x1a\x1e.viam.robot.v1.StopAllResponse"\x1d\x82\xd3\xe4\x93\x02\x17\x12\x15/viam/api/v1/stop_all\x12v\n\x0cStartSession\x12".viam.robot.v1.StartSessionRequest\x1a#.viam.robot.v1.StartSessionResponse"\x1d\x82\xd3\xe4\x93\x02\x17"\x15/viam/api/v1/sessions\x12\x9d\x01\n\x14SendSessionHeartbeat\x12*.viam.robot.v1.SendSessionHeartbeatRequest\x1a+.viam.robot.v1.SendSessionHeartbeatResponse",\x82\xd3\xe4\x93\x02&"$/viam/api/v1/sessions/{id}/heartbeat\x12V\n\x03Log\x12\x19.viam.robot.v1.LogRequest\x1a\x1a.viam.robot.v1.LogResponse"\x18\x82\xd3\xe4\x93\x02\x12"\x10/viam/api/v1/log\x12\x88\x01\n\x10GetCloudMetadata\x12&.viam.robot.v1.GetCloudMetadataRequest\x1a\'.viam.robot.v1.GetCloudMetadataResponse"#\x82\xd3\xe4\x93\x02\x1d\x12\x1b/viam/api/v1/cloud_metadata\x12\x7f\n\rRestartModule\x12#.viam.robot.v1.RestartModuleRequest\x1a$.viam.robot.v1.RestartModuleResponse"#\x82\xd3\xe4\x93\x02\x1d"\x1b/viam/api/v1/restart_module\x12j\n\x08Shutdown\x12\x1e.viam.robot.v1.ShutdownRequest\x1a\x1f.viam.robot.v1.ShutdownResponse"\x1d\x82\xd3\xe4\x93\x02\x17"\x15/viam/api/v1/shutdown\x12\x88\x01\n\x10GetMachineStatus\x12&.viam.robot.v1.GetMachineStatusRequest\x1a\'.viam.robot.v1.GetMachineStatusResponse"#\x82\xd3\xe4\x93\x02\x1d\x12\x1b/viam/api/v1/machine_status\x12o\n\nGetVersion\x12 .viam.robot.v1.GetVersionRequest\x1a!.viam.robot.v1.GetVersionResponse"\x1c\x82\xd3\xe4\x93\x02\x16\x12\x14/viam/api/v1/version\x12I\n\x06Tunnel\x12\x1c.viam.robot.v1.TunnelRequest\x1a\x1d.viam.robot.v1.TunnelResponse(\x010\x01\x12w\n\x0bListTunnels\x12!.viam.robot.v1.ListTunnelsRequest\x1a".viam.robot.v1.ListTunnelsResponse"!\x82\xd3\xe4\x93\x02\x1b\x12\x19/viam/api/v1/list_tunnelsB-\n\x11com.viam.robot.v1Z\x18go.viam.com/api/robot/v1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'robot.v1.robot_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x11com.viam.robot.v1Z\x18go.viam.com/api/robot/v1'
    _globals['_GETCLOUDMETADATARESPONSE'].fields_by_name['robot_part_id']._loaded_options = None
    _globals['_GETCLOUDMETADATARESPONSE'].fields_by_name['robot_part_id']._serialized_options = b'\x18\x01'
    _globals['_ROBOTSERVICE'].methods_by_name['GetOperations']._loaded_options = None
    _globals['_ROBOTSERVICE'].methods_by_name['GetOperations']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1e\x12\x1c/viam/api/v1/operations/list'
    _globals['_ROBOTSERVICE'].methods_by_name['GetSessions']._loaded_options = None
    _globals['_ROBOTSERVICE'].methods_by_name['GetSessions']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1c\x12\x1a/viam/api/v1/sessions/list'
    _globals['_ROBOTSERVICE'].methods_by_name['ResourceNames']._loaded_options = None
    _globals['_ROBOTSERVICE'].methods_by_name['ResourceNames']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1d\x12\x1b/viam/api/v1/resources/list'
    _globals['_ROBOTSERVICE'].methods_by_name['ResourceRPCSubtypes']._loaded_options = None
    _globals['_ROBOTSERVICE'].methods_by_name['ResourceRPCSubtypes']._serialized_options = b"\x82\xd3\xe4\x93\x02)\x12'/viam/api/v1/resource_rpc_subtypes/list"
    _globals['_ROBOTSERVICE'].methods_by_name['CancelOperation']._loaded_options = None
    _globals['_ROBOTSERVICE'].methods_by_name['CancelOperation']._serialized_options = b'\x82\xd3\xe4\x93\x02 "\x1e/viam/api/v1/operations/cancel'
    _globals['_ROBOTSERVICE'].methods_by_name['BlockForOperation']._loaded_options = None
    _globals['_ROBOTSERVICE'].methods_by_name['BlockForOperation']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1f"\x1d/viam/api/v1/operations/block'
    _globals['_ROBOTSERVICE'].methods_by_name['GetModelsFromModules']._loaded_options = None
    _globals['_ROBOTSERVICE'].methods_by_name['GetModelsFromModules']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1c\x12\x1a/viam/api/v1/module_models'
    _globals['_ROBOTSERVICE'].methods_by_name['FrameSystemConfig']._loaded_options = None
    _globals['_ROBOTSERVICE'].methods_by_name['FrameSystemConfig']._serialized_options = b'\x82\xd3\xe4\x93\x02"\x12 /viam/api/v1/frame_system/config'
    _globals['_ROBOTSERVICE'].methods_by_name['TransformPose']._loaded_options = None
    _globals['_ROBOTSERVICE'].methods_by_name['TransformPose']._serialized_options = b'\x82\xd3\xe4\x93\x02*\x12(/viam/api/v1/frame_system/transform_pose'
    _globals['_ROBOTSERVICE'].methods_by_name['TransformPCD']._loaded_options = None
    _globals['_ROBOTSERVICE'].methods_by_name['TransformPCD']._serialized_options = b"\x82\xd3\xe4\x93\x02)\x12'/viam/api/v1/frame_system/transform_pcd"
    _globals['_ROBOTSERVICE'].methods_by_name['GetStatus']._loaded_options = None
    _globals['_ROBOTSERVICE'].methods_by_name['GetStatus']._serialized_options = b'\x88\x02\x01\x82\xd3\xe4\x93\x02\x15\x12\x13/viam/api/v1/status'
    _globals['_ROBOTSERVICE'].methods_by_name['StreamStatus']._loaded_options = None
    _globals['_ROBOTSERVICE'].methods_by_name['StreamStatus']._serialized_options = b'\x88\x02\x01\x82\xd3\xe4\x93\x02\x1c\x12\x1a/viam/api/v1/status/stream'
    _globals['_ROBOTSERVICE'].methods_by_name['StopAll']._loaded_options = None
    _globals['_ROBOTSERVICE'].methods_by_name['StopAll']._serialized_options = b'\x82\xd3\xe4\x93\x02\x17\x12\x15/viam/api/v1/stop_all'
    _globals['_ROBOTSERVICE'].methods_by_name['StartSession']._loaded_options = None
    _globals['_ROBOTSERVICE'].methods_by_name['StartSession']._serialized_options = b'\x82\xd3\xe4\x93\x02\x17"\x15/viam/api/v1/sessions'
    _globals['_ROBOTSERVICE'].methods_by_name['SendSessionHeartbeat']._loaded_options = None
    _globals['_ROBOTSERVICE'].methods_by_name['SendSessionHeartbeat']._serialized_options = b'\x82\xd3\xe4\x93\x02&"$/viam/api/v1/sessions/{id}/heartbeat'
    _globals['_ROBOTSERVICE'].methods_by_name['Log']._loaded_options = None
    _globals['_ROBOTSERVICE'].methods_by_name['Log']._serialized_options = b'\x82\xd3\xe4\x93\x02\x12"\x10/viam/api/v1/log'
    _globals['_ROBOTSERVICE'].methods_by_name['GetCloudMetadata']._loaded_options = None
    _globals['_ROBOTSERVICE'].methods_by_name['GetCloudMetadata']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1d\x12\x1b/viam/api/v1/cloud_metadata'
    _globals['_ROBOTSERVICE'].methods_by_name['RestartModule']._loaded_options = None
    _globals['_ROBOTSERVICE'].methods_by_name['RestartModule']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1d"\x1b/viam/api/v1/restart_module'
    _globals['_ROBOTSERVICE'].methods_by_name['Shutdown']._loaded_options = None
    _globals['_ROBOTSERVICE'].methods_by_name['Shutdown']._serialized_options = b'\x82\xd3\xe4\x93\x02\x17"\x15/viam/api/v1/shutdown'
    _globals['_ROBOTSERVICE'].methods_by_name['GetMachineStatus']._loaded_options = None
    _globals['_ROBOTSERVICE'].methods_by_name['GetMachineStatus']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1d\x12\x1b/viam/api/v1/machine_status'
    _globals['_ROBOTSERVICE'].methods_by_name['GetVersion']._loaded_options = None
    _globals['_ROBOTSERVICE'].methods_by_name['GetVersion']._serialized_options = b'\x82\xd3\xe4\x93\x02\x16\x12\x14/viam/api/v1/version'
    _globals['_ROBOTSERVICE'].methods_by_name['ListTunnels']._loaded_options = None
    _globals['_ROBOTSERVICE'].methods_by_name['ListTunnels']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1b\x12\x19/viam/api/v1/list_tunnels'
    _globals['_PEERCONNECTIONTYPE']._serialized_start = 5356
    _globals['_PEERCONNECTIONTYPE']._serialized_end = 5478
    _globals['_TUNNELREQUEST']._serialized_start = 188
    _globals['_TUNNELREQUEST']._serialized_end = 266
    _globals['_TUNNELRESPONSE']._serialized_start = 268
    _globals['_TUNNELRESPONSE']._serialized_end = 304
    _globals['_LISTTUNNELSREQUEST']._serialized_start = 306
    _globals['_LISTTUNNELSREQUEST']._serialized_end = 326
    _globals['_LISTTUNNELSRESPONSE']._serialized_start = 328
    _globals['_LISTTUNNELSRESPONSE']._serialized_end = 398
    _globals['_TUNNEL']._serialized_start = 400
    _globals['_TUNNEL']._serialized_end = 502
    _globals['_FRAMESYSTEMCONFIG']._serialized_start = 504
    _globals['_FRAMESYSTEMCONFIG']._serialized_end = 629
    _globals['_FRAMESYSTEMCONFIGREQUEST']._serialized_start = 631
    _globals['_FRAMESYSTEMCONFIGREQUEST']._serialized_end = 741
    _globals['_FRAMESYSTEMCONFIGRESPONSE']._serialized_start = 743
    _globals['_FRAMESYSTEMCONFIGRESPONSE']._serialized_end = 854
    _globals['_TRANSFORMPOSEREQUEST']._serialized_start = 857
    _globals['_TRANSFORMPOSEREQUEST']._serialized_end = 1050
    _globals['_TRANSFORMPOSERESPONSE']._serialized_start = 1052
    _globals['_TRANSFORMPOSERESPONSE']._serialized_end = 1124
    _globals['_TRANSFORMPCDREQUEST']._serialized_start = 1126
    _globals['_TRANSFORMPCDREQUEST']._serialized_end = 1245
    _globals['_TRANSFORMPCDRESPONSE']._serialized_start = 1247
    _globals['_TRANSFORMPCDRESPONSE']._serialized_end = 1309
    _globals['_RESOURCENAMESREQUEST']._serialized_start = 1311
    _globals['_RESOURCENAMESREQUEST']._serialized_end = 1333
    _globals['_RESOURCENAMESRESPONSE']._serialized_start = 1335
    _globals['_RESOURCENAMESRESPONSE']._serialized_end = 1418
    _globals['_RESOURCERPCSUBTYPE']._serialized_start = 1420
    _globals['_RESOURCERPCSUBTYPE']._serialized_end = 1533
    _globals['_RESOURCERPCSUBTYPESREQUEST']._serialized_start = 1535
    _globals['_RESOURCERPCSUBTYPESREQUEST']._serialized_end = 1563
    _globals['_RESOURCERPCSUBTYPESRESPONSE']._serialized_start = 1565
    _globals['_RESOURCERPCSUBTYPESRESPONSE']._serialized_end = 1681
    _globals['_OPERATION']._serialized_start = 1684
    _globals['_OPERATION']._serialized_end = 1895
    _globals['_GETOPERATIONSREQUEST']._serialized_start = 1897
    _globals['_GETOPERATIONSREQUEST']._serialized_end = 1919
    _globals['_GETOPERATIONSRESPONSE']._serialized_start = 1921
    _globals['_GETOPERATIONSRESPONSE']._serialized_end = 2002
    _globals['_CANCELOPERATIONREQUEST']._serialized_start = 2004
    _globals['_CANCELOPERATIONREQUEST']._serialized_end = 2044
    _globals['_CANCELOPERATIONRESPONSE']._serialized_start = 2046
    _globals['_CANCELOPERATIONRESPONSE']._serialized_end = 2071
    _globals['_BLOCKFOROPERATIONREQUEST']._serialized_start = 2073
    _globals['_BLOCKFOROPERATIONREQUEST']._serialized_end = 2115
    _globals['_BLOCKFOROPERATIONRESPONSE']._serialized_start = 2117
    _globals['_BLOCKFOROPERATIONRESPONSE']._serialized_end = 2144
    _globals['_PEERCONNECTIONINFO']._serialized_start = 2147
    _globals['_PEERCONNECTIONINFO']._serialized_end = 2345
    _globals['_SESSION']._serialized_start = 2348
    _globals['_SESSION']._serialized_end = 2488
    _globals['_GETSESSIONSREQUEST']._serialized_start = 2490
    _globals['_GETSESSIONSREQUEST']._serialized_end = 2510
    _globals['_GETSESSIONSRESPONSE']._serialized_start = 2512
    _globals['_GETSESSIONSRESPONSE']._serialized_end = 2585
    _globals['_MODULEMODEL']._serialized_start = 2588
    _globals['_MODULEMODEL']._serialized_end = 2718
    _globals['_GETMODELSFROMMODULESREQUEST']._serialized_start = 2720
    _globals['_GETMODELSFROMMODULESREQUEST']._serialized_end = 2749
    _globals['_GETMODELSFROMMODULESRESPONSE']._serialized_start = 2751
    _globals['_GETMODELSFROMMODULESRESPONSE']._serialized_end = 2833
    _globals['_STATUS']._serialized_start = 2836
    _globals['_STATUS']._serialized_end = 3016
    _globals['_GETSTATUSREQUEST']._serialized_start = 3018
    _globals['_GETSTATUSREQUEST']._serialized_end = 3105
    _globals['_GETSTATUSRESPONSE']._serialized_start = 3107
    _globals['_GETSTATUSRESPONSE']._serialized_end = 3173
    _globals['_STREAMSTATUSREQUEST']._serialized_start = 3176
    _globals['_STREAMSTATUSREQUEST']._serialized_end = 3315
    _globals['_STREAMSTATUSRESPONSE']._serialized_start = 3317
    _globals['_STREAMSTATUSRESPONSE']._serialized_end = 3386
    _globals['_STOPEXTRAPARAMETERS']._serialized_start = 3388
    _globals['_STOPEXTRAPARAMETERS']._serialized_end = 3508
    _globals['_STOPALLREQUEST']._serialized_start = 3510
    _globals['_STOPALLREQUEST']._serialized_end = 3584
    _globals['_STOPALLRESPONSE']._serialized_start = 3586
    _globals['_STOPALLRESPONSE']._serialized_end = 3603
    _globals['_STARTSESSIONREQUEST']._serialized_start = 3605
    _globals['_STARTSESSIONREQUEST']._serialized_end = 3650
    _globals['_STARTSESSIONRESPONSE']._serialized_start = 3652
    _globals['_STARTSESSIONRESPONSE']._serialized_end = 3760
    _globals['_SENDSESSIONHEARTBEATREQUEST']._serialized_start = 3762
    _globals['_SENDSESSIONHEARTBEATREQUEST']._serialized_end = 3807
    _globals['_SENDSESSIONHEARTBEATRESPONSE']._serialized_start = 3809
    _globals['_SENDSESSIONHEARTBEATRESPONSE']._serialized_end = 3839
    _globals['_LOGREQUEST']._serialized_start = 3841
    _globals['_LOGREQUEST']._serialized_end = 3899
    _globals['_LOGRESPONSE']._serialized_start = 3901
    _globals['_LOGRESPONSE']._serialized_end = 3914
    _globals['_GETCLOUDMETADATAREQUEST']._serialized_start = 3916
    _globals['_GETCLOUDMETADATAREQUEST']._serialized_end = 3941
    _globals['_GETCLOUDMETADATARESPONSE']._serialized_start = 3944
    _globals['_GETCLOUDMETADATARESPONSE']._serialized_end = 4152
    _globals['_RESTARTMODULEREQUEST']._serialized_start = 4154
    _globals['_RESTARTMODULEREQUEST']._serialized_end = 4256
    _globals['_RESTARTMODULERESPONSE']._serialized_start = 4258
    _globals['_RESTARTMODULERESPONSE']._serialized_end = 4281
    _globals['_SHUTDOWNREQUEST']._serialized_start = 4283
    _globals['_SHUTDOWNREQUEST']._serialized_end = 4300
    _globals['_SHUTDOWNRESPONSE']._serialized_start = 4302
    _globals['_SHUTDOWNRESPONSE']._serialized_end = 4320
    _globals['_GETMACHINESTATUSREQUEST']._serialized_start = 4322
    _globals['_GETMACHINESTATUSREQUEST']._serialized_end = 4347
    _globals['_GETMACHINESTATUSRESPONSE']._serialized_start = 4350
    _globals['_GETMACHINESTATUSRESPONSE']._serialized_end = 4634
    _globals['_GETMACHINESTATUSRESPONSE_STATE']._serialized_start = 4561
    _globals['_GETMACHINESTATUSRESPONSE_STATE']._serialized_end = 4634
    _globals['_RESOURCESTATUS']._serialized_start = 4637
    _globals['_RESOURCESTATUS']._serialized_end = 5117
    _globals['_RESOURCESTATUS_STATE']._serialized_start = 4963
    _globals['_RESOURCESTATUS_STATE']._serialized_end = 5098
    _globals['_CONFIGSTATUS']._serialized_start = 5119
    _globals['_CONFIGSTATUS']._serialized_end = 5224
    _globals['_GETVERSIONREQUEST']._serialized_start = 5226
    _globals['_GETVERSIONREQUEST']._serialized_end = 5245
    _globals['_GETVERSIONRESPONSE']._serialized_start = 5247
    _globals['_GETVERSIONRESPONSE']._serialized_end = 5354
    _globals['_ROBOTSERVICE']._serialized_start = 5481
    _globals['_ROBOTSERVICE']._serialized_end = 8439