"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ...common.v1 import common_pb2 as common_dot_v1_dot_common__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14robot/v1/robot.proto\x12\rviam.robot.v1\x1a\x16common/v1/common.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto"}\n\x11FrameSystemConfig\x12/\n\x05frame\x18\x01 \x01(\x0b2\x19.viam.common.v1.TransformR\x05frame\x127\n\nkinematics\x18\x02 \x01(\x0b2\x17.google.protobuf.StructR\nkinematics"n\n\x18FrameSystemConfigRequest\x12R\n\x17supplemental_transforms\x18\x01 \x03(\x0b2\x19.viam.common.v1.TransformR\x16supplementalTransforms"o\n\x19FrameSystemConfigResponse\x12R\n\x14frame_system_configs\x18\x01 \x03(\x0b2 .viam.robot.v1.FrameSystemConfigR\x12frameSystemConfigs"\xc1\x01\n\x14TransformPoseRequest\x123\n\x06source\x18\x01 \x01(\x0b2\x1b.viam.common.v1.PoseInFrameR\x06source\x12 \n\x0bdestination\x18\x02 \x01(\tR\x0bdestination\x12R\n\x17supplemental_transforms\x18\x03 \x03(\x0b2\x19.viam.common.v1.TransformR\x16supplementalTransforms"H\n\x15TransformPoseResponse\x12/\n\x04pose\x18\x01 \x01(\x0b2\x1b.viam.common.v1.PoseInFrameR\x04pose"w\n\x13TransformPCDRequest\x12&\n\x0fpoint_cloud_pcd\x18\x01 \x01(\x0cR\rpointCloudPcd\x12\x16\n\x06source\x18\x02 \x01(\tR\x06source\x12 \n\x0bdestination\x18\x03 \x01(\tR\x0bdestination">\n\x14TransformPCDResponse\x12&\n\x0fpoint_cloud_pcd\x18\x01 \x01(\x0cR\rpointCloudPcd"\x16\n\x14ResourceNamesRequest"S\n\x15ResourceNamesResponse\x12:\n\tresources\x18\x01 \x03(\x0b2\x1c.viam.common.v1.ResourceNameR\tresources"q\n\x12ResourceRPCSubtype\x126\n\x07subtype\x18\x01 \x01(\x0b2\x1c.viam.common.v1.ResourceNameR\x07subtype\x12#\n\rproto_service\x18\x02 \x01(\tR\x0cprotoService"\x1c\n\x1aResourceRPCSubtypesRequest"t\n\x1bResourceRPCSubtypesResponse\x12U\n\x15resource_rpc_subtypes\x18\x01 \x03(\x0b2!.viam.robot.v1.ResourceRPCSubtypeR\x13resourceRpcSubtypes"\xd3\x01\n\tOperation\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x16\n\x06method\x18\x02 \x01(\tR\x06method\x125\n\targuments\x18\x03 \x01(\x0b2\x17.google.protobuf.StructR\targuments\x124\n\x07started\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampR\x07started\x12"\n\nsession_id\x18\x05 \x01(\tH\x00R\tsessionId\x88\x01\x01B\r\n\x0b_session_id"\x16\n\x14GetOperationsRequest"Q\n\x15GetOperationsResponse\x128\n\noperations\x18\x01 \x03(\x0b2\x18.viam.robot.v1.OperationR\noperations"(\n\x16CancelOperationRequest\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id"\x19\n\x17CancelOperationResponse"*\n\x18BlockForOperationRequest\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id"\x1b\n\x19BlockForOperationResponse"\xc6\x01\n\x12PeerConnectionInfo\x125\n\x04type\x18\x01 \x01(\x0e2!.viam.robot.v1.PeerConnectionTypeR\x04type\x12*\n\x0eremote_address\x18\x02 \x01(\tH\x00R\rremoteAddress\x88\x01\x01\x12(\n\rlocal_address\x18\x03 \x01(\tH\x01R\x0clocalAddress\x88\x01\x01B\x11\n\x0f_remote_addressB\x10\n\x0e_local_address"\x8c\x01\n\x07Session\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12X\n\x14peer_connection_info\x18\x02 \x01(\x0b2!.viam.robot.v1.PeerConnectionInfoH\x00R\x12peerConnectionInfo\x88\x01\x01B\x17\n\x15_peer_connection_info"\x14\n\x12GetSessionsRequest"I\n\x13GetSessionsResponse\x122\n\x08sessions\x18\x01 \x03(\x0b2\x16.viam.robot.v1.SessionR\x08sessions"@\n\x0eDiscoveryQuery\x12\x18\n\x07subtype\x18\x01 \x01(\tR\x07subtype\x12\x14\n\x05model\x18\x02 \x01(\tR\x05model"s\n\tDiscovery\x123\n\x05query\x18\x01 \x01(\x0b2\x1d.viam.robot.v1.DiscoveryQueryR\x05query\x121\n\x07results\x18\x02 \x01(\x0b2\x17.google.protobuf.StructR\x07results"T\n\x19DiscoverComponentsRequest\x127\n\x07queries\x18\x01 \x03(\x0b2\x1d.viam.robot.v1.DiscoveryQueryR\x07queries"T\n\x1aDiscoverComponentsResponse\x126\n\tdiscovery\x18\x01 \x03(\x0b2\x18.viam.robot.v1.DiscoveryR\tdiscovery"k\n\x06Status\x120\n\x04name\x18\x01 \x01(\x0b2\x1c.viam.common.v1.ResourceNameR\x04name\x12/\n\x06status\x18\x02 \x01(\x0b2\x17.google.protobuf.StructR\x06status"W\n\x10GetStatusRequest\x12C\n\x0eresource_names\x18\x01 \x03(\x0b2\x1c.viam.common.v1.ResourceNameR\rresourceNames"B\n\x11GetStatusResponse\x12-\n\x06status\x18\x01 \x03(\x0b2\x15.viam.robot.v1.StatusR\x06status"\x8b\x01\n\x13StreamStatusRequest\x12C\n\x0eresource_names\x18\x01 \x03(\x0b2\x1c.viam.common.v1.ResourceNameR\rresourceNames\x12/\n\x05every\x18\x02 \x01(\x0b2\x19.google.protobuf.DurationR\x05every"E\n\x14StreamStatusResponse\x12-\n\x06status\x18\x01 \x03(\x0b2\x15.viam.robot.v1.StatusR\x06status"x\n\x13StopExtraParameters\x120\n\x04name\x18\x01 \x01(\x0b2\x1c.viam.common.v1.ResourceNameR\x04name\x12/\n\x06params\x18\x02 \x01(\x0b2\x17.google.protobuf.StructR\x06params"J\n\x0eStopAllRequest\x128\n\x05extra\x18c \x03(\x0b2".viam.robot.v1.StopExtraParametersR\x05extra"\x11\n\x0fStopAllResponse"-\n\x13StartSessionRequest\x12\x16\n\x06resume\x18\x01 \x01(\tR\x06resume"l\n\x14StartSessionResponse\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12D\n\x10heartbeat_window\x18\x02 \x01(\x0b2\x19.google.protobuf.DurationR\x0fheartbeatWindow"-\n\x1bSendSessionHeartbeatRequest\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id"\x1e\n\x1cSendSessionHeartbeatResponse*z\n\x12PeerConnectionType\x12$\n PEER_CONNECTION_TYPE_UNSPECIFIED\x10\x00\x12\x1d\n\x19PEER_CONNECTION_TYPE_GRPC\x10\x01\x12\x1f\n\x1bPEER_CONNECTION_TYPE_WEBRTC\x10\x022\xf8\x0f\n\x0cRobotService\x12\x80\x01\n\rGetOperations\x12#.viam.robot.v1.GetOperationsRequest\x1a$.viam.robot.v1.GetOperationsResponse"$\x82\xd3\xe4\x93\x02\x1e\x12\x1c/viam/api/v1/operations/list\x12x\n\x0bGetSessions\x12!.viam.robot.v1.GetSessionsRequest\x1a".viam.robot.v1.GetSessionsResponse""\x82\xd3\xe4\x93\x02\x1c\x12\x1a/viam/api/v1/sessions/list\x12\x7f\n\rResourceNames\x12#.viam.robot.v1.ResourceNamesRequest\x1a$.viam.robot.v1.ResourceNamesResponse"#\x82\xd3\xe4\x93\x02\x1d\x12\x1b/viam/api/v1/resources/list\x12\x9d\x01\n\x13ResourceRPCSubtypes\x12).viam.robot.v1.ResourceRPCSubtypesRequest\x1a*.viam.robot.v1.ResourceRPCSubtypesResponse"/\x82\xd3\xe4\x93\x02)\x12\'/viam/api/v1/resource_rpc_subtypes/list\x12\x88\x01\n\x0fCancelOperation\x12%.viam.robot.v1.CancelOperationRequest\x1a&.viam.robot.v1.CancelOperationResponse"&\x82\xd3\xe4\x93\x02 "\x1e/viam/api/v1/operations/cancel\x12\x8d\x01\n\x11BlockForOperation\x12\'.viam.robot.v1.BlockForOperationRequest\x1a(.viam.robot.v1.BlockForOperationResponse"%\x82\xd3\xe4\x93\x02\x1f"\x1d/viam/api/v1/operations/block\x12\x94\x01\n\x12DiscoverComponents\x12(.viam.robot.v1.DiscoverComponentsRequest\x1a).viam.robot.v1.DiscoverComponentsResponse")\x82\xd3\xe4\x93\x02#\x12!/viam/api/v1/discovery/components\x12\x90\x01\n\x11FrameSystemConfig\x12\'.viam.robot.v1.FrameSystemConfigRequest\x1a(.viam.robot.v1.FrameSystemConfigResponse"(\x82\xd3\xe4\x93\x02"\x12 /viam/api/v1/frame_system/config\x12\x8c\x01\n\rTransformPose\x12#.viam.robot.v1.TransformPoseRequest\x1a$.viam.robot.v1.TransformPoseResponse"0\x82\xd3\xe4\x93\x02*\x12(/viam/api/v1/frame_system/transform_pose\x12\x88\x01\n\x0cTransformPCD\x12".viam.robot.v1.TransformPCDRequest\x1a#.viam.robot.v1.TransformPCDResponse"/\x82\xd3\xe4\x93\x02)\x12\'/viam/api/v1/frame_system/transform_pcd\x12k\n\tGetStatus\x12\x1f.viam.robot.v1.GetStatusRequest\x1a .viam.robot.v1.GetStatusResponse"\x1b\x82\xd3\xe4\x93\x02\x15\x12\x13/viam/api/v1/status\x12}\n\x0cStreamStatus\x12".viam.robot.v1.StreamStatusRequest\x1a#.viam.robot.v1.StreamStatusResponse""\x82\xd3\xe4\x93\x02\x1c\x12\x1a/viam/api/v1/status/stream0\x01\x12g\n\x07StopAll\x12\x1d.viam.robot.v1.StopAllRequest\x1a\x1e.viam.robot.v1.StopAllResponse"\x1d\x82\xd3\xe4\x93\x02\x17\x12\x15/viam/api/v1/stop_all\x12v\n\x0cStartSession\x12".viam.robot.v1.StartSessionRequest\x1a#.viam.robot.v1.StartSessionResponse"\x1d\x82\xd3\xe4\x93\x02\x17"\x15/viam/api/v1/sessions\x12\x9d\x01\n\x14SendSessionHeartbeat\x12*.viam.robot.v1.SendSessionHeartbeatRequest\x1a+.viam.robot.v1.SendSessionHeartbeatResponse",\x82\xd3\xe4\x93\x02&"$/viam/api/v1/sessions/{id}/heartbeatB-\n\x11com.viam.robot.v1Z\x18go.viam.com/api/robot/v1b\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'robot.v1.robot_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n\x11com.viam.robot.v1Z\x18go.viam.com/api/robot/v1'
    _ROBOTSERVICE.methods_by_name['GetOperations']._options = None
    _ROBOTSERVICE.methods_by_name['GetOperations']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1e\x12\x1c/viam/api/v1/operations/list'
    _ROBOTSERVICE.methods_by_name['GetSessions']._options = None
    _ROBOTSERVICE.methods_by_name['GetSessions']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1c\x12\x1a/viam/api/v1/sessions/list'
    _ROBOTSERVICE.methods_by_name['ResourceNames']._options = None
    _ROBOTSERVICE.methods_by_name['ResourceNames']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1d\x12\x1b/viam/api/v1/resources/list'
    _ROBOTSERVICE.methods_by_name['ResourceRPCSubtypes']._options = None
    _ROBOTSERVICE.methods_by_name['ResourceRPCSubtypes']._serialized_options = b"\x82\xd3\xe4\x93\x02)\x12'/viam/api/v1/resource_rpc_subtypes/list"
    _ROBOTSERVICE.methods_by_name['CancelOperation']._options = None
    _ROBOTSERVICE.methods_by_name['CancelOperation']._serialized_options = b'\x82\xd3\xe4\x93\x02 "\x1e/viam/api/v1/operations/cancel'
    _ROBOTSERVICE.methods_by_name['BlockForOperation']._options = None
    _ROBOTSERVICE.methods_by_name['BlockForOperation']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1f"\x1d/viam/api/v1/operations/block'
    _ROBOTSERVICE.methods_by_name['DiscoverComponents']._options = None
    _ROBOTSERVICE.methods_by_name['DiscoverComponents']._serialized_options = b'\x82\xd3\xe4\x93\x02#\x12!/viam/api/v1/discovery/components'
    _ROBOTSERVICE.methods_by_name['FrameSystemConfig']._options = None
    _ROBOTSERVICE.methods_by_name['FrameSystemConfig']._serialized_options = b'\x82\xd3\xe4\x93\x02"\x12 /viam/api/v1/frame_system/config'
    _ROBOTSERVICE.methods_by_name['TransformPose']._options = None
    _ROBOTSERVICE.methods_by_name['TransformPose']._serialized_options = b'\x82\xd3\xe4\x93\x02*\x12(/viam/api/v1/frame_system/transform_pose'
    _ROBOTSERVICE.methods_by_name['TransformPCD']._options = None
    _ROBOTSERVICE.methods_by_name['TransformPCD']._serialized_options = b"\x82\xd3\xe4\x93\x02)\x12'/viam/api/v1/frame_system/transform_pcd"
    _ROBOTSERVICE.methods_by_name['GetStatus']._options = None
    _ROBOTSERVICE.methods_by_name['GetStatus']._serialized_options = b'\x82\xd3\xe4\x93\x02\x15\x12\x13/viam/api/v1/status'
    _ROBOTSERVICE.methods_by_name['StreamStatus']._options = None
    _ROBOTSERVICE.methods_by_name['StreamStatus']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1c\x12\x1a/viam/api/v1/status/stream'
    _ROBOTSERVICE.methods_by_name['StopAll']._options = None
    _ROBOTSERVICE.methods_by_name['StopAll']._serialized_options = b'\x82\xd3\xe4\x93\x02\x17\x12\x15/viam/api/v1/stop_all'
    _ROBOTSERVICE.methods_by_name['StartSession']._options = None
    _ROBOTSERVICE.methods_by_name['StartSession']._serialized_options = b'\x82\xd3\xe4\x93\x02\x17"\x15/viam/api/v1/sessions'
    _ROBOTSERVICE.methods_by_name['SendSessionHeartbeat']._options = None
    _ROBOTSERVICE.methods_by_name['SendSessionHeartbeat']._serialized_options = b'\x82\xd3\xe4\x93\x02&"$/viam/api/v1/sessions/{id}/heartbeat'
    _PEERCONNECTIONTYPE._serialized_start = 3558
    _PEERCONNECTIONTYPE._serialized_end = 3680
    _FRAMESYSTEMCONFIG._serialized_start = 188
    _FRAMESYSTEMCONFIG._serialized_end = 313
    _FRAMESYSTEMCONFIGREQUEST._serialized_start = 315
    _FRAMESYSTEMCONFIGREQUEST._serialized_end = 425
    _FRAMESYSTEMCONFIGRESPONSE._serialized_start = 427
    _FRAMESYSTEMCONFIGRESPONSE._serialized_end = 538
    _TRANSFORMPOSEREQUEST._serialized_start = 541
    _TRANSFORMPOSEREQUEST._serialized_end = 734
    _TRANSFORMPOSERESPONSE._serialized_start = 736
    _TRANSFORMPOSERESPONSE._serialized_end = 808
    _TRANSFORMPCDREQUEST._serialized_start = 810
    _TRANSFORMPCDREQUEST._serialized_end = 929
    _TRANSFORMPCDRESPONSE._serialized_start = 931
    _TRANSFORMPCDRESPONSE._serialized_end = 993
    _RESOURCENAMESREQUEST._serialized_start = 995
    _RESOURCENAMESREQUEST._serialized_end = 1017
    _RESOURCENAMESRESPONSE._serialized_start = 1019
    _RESOURCENAMESRESPONSE._serialized_end = 1102
    _RESOURCERPCSUBTYPE._serialized_start = 1104
    _RESOURCERPCSUBTYPE._serialized_end = 1217
    _RESOURCERPCSUBTYPESREQUEST._serialized_start = 1219
    _RESOURCERPCSUBTYPESREQUEST._serialized_end = 1247
    _RESOURCERPCSUBTYPESRESPONSE._serialized_start = 1249
    _RESOURCERPCSUBTYPESRESPONSE._serialized_end = 1365
    _OPERATION._serialized_start = 1368
    _OPERATION._serialized_end = 1579
    _GETOPERATIONSREQUEST._serialized_start = 1581
    _GETOPERATIONSREQUEST._serialized_end = 1603
    _GETOPERATIONSRESPONSE._serialized_start = 1605
    _GETOPERATIONSRESPONSE._serialized_end = 1686
    _CANCELOPERATIONREQUEST._serialized_start = 1688
    _CANCELOPERATIONREQUEST._serialized_end = 1728
    _CANCELOPERATIONRESPONSE._serialized_start = 1730
    _CANCELOPERATIONRESPONSE._serialized_end = 1755
    _BLOCKFOROPERATIONREQUEST._serialized_start = 1757
    _BLOCKFOROPERATIONREQUEST._serialized_end = 1799
    _BLOCKFOROPERATIONRESPONSE._serialized_start = 1801
    _BLOCKFOROPERATIONRESPONSE._serialized_end = 1828
    _PEERCONNECTIONINFO._serialized_start = 1831
    _PEERCONNECTIONINFO._serialized_end = 2029
    _SESSION._serialized_start = 2032
    _SESSION._serialized_end = 2172
    _GETSESSIONSREQUEST._serialized_start = 2174
    _GETSESSIONSREQUEST._serialized_end = 2194
    _GETSESSIONSRESPONSE._serialized_start = 2196
    _GETSESSIONSRESPONSE._serialized_end = 2269
    _DISCOVERYQUERY._serialized_start = 2271
    _DISCOVERYQUERY._serialized_end = 2335
    _DISCOVERY._serialized_start = 2337
    _DISCOVERY._serialized_end = 2452
    _DISCOVERCOMPONENTSREQUEST._serialized_start = 2454
    _DISCOVERCOMPONENTSREQUEST._serialized_end = 2538
    _DISCOVERCOMPONENTSRESPONSE._serialized_start = 2540
    _DISCOVERCOMPONENTSRESPONSE._serialized_end = 2624
    _STATUS._serialized_start = 2626
    _STATUS._serialized_end = 2733
    _GETSTATUSREQUEST._serialized_start = 2735
    _GETSTATUSREQUEST._serialized_end = 2822
    _GETSTATUSRESPONSE._serialized_start = 2824
    _GETSTATUSRESPONSE._serialized_end = 2890
    _STREAMSTATUSREQUEST._serialized_start = 2893
    _STREAMSTATUSREQUEST._serialized_end = 3032
    _STREAMSTATUSRESPONSE._serialized_start = 3034
    _STREAMSTATUSRESPONSE._serialized_end = 3103
    _STOPEXTRAPARAMETERS._serialized_start = 3105
    _STOPEXTRAPARAMETERS._serialized_end = 3225
    _STOPALLREQUEST._serialized_start = 3227
    _STOPALLREQUEST._serialized_end = 3301
    _STOPALLRESPONSE._serialized_start = 3303
    _STOPALLRESPONSE._serialized_end = 3320
    _STARTSESSIONREQUEST._serialized_start = 3322
    _STARTSESSIONREQUEST._serialized_end = 3367
    _STARTSESSIONRESPONSE._serialized_start = 3369
    _STARTSESSIONRESPONSE._serialized_end = 3477
    _SENDSESSIONHEARTBEATREQUEST._serialized_start = 3479
    _SENDSESSIONHEARTBEATREQUEST._serialized_end = 3524
    _SENDSESSIONHEARTBEATRESPONSE._serialized_start = 3526
    _SENDSESSIONHEARTBEATRESPONSE._serialized_end = 3556
    _ROBOTSERVICE._serialized_start = 3683
    _ROBOTSERVICE._serialized_end = 5723