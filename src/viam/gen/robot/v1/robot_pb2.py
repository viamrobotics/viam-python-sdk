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
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14robot/v1/robot.proto\x12\rviam.robot.v1\x1a\x16common/v1/common.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\x94\x01\n\x11FrameSystemConfig\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12L\n\x14pose_in_parent_frame\x18\x02 \x01(\x0b2\x1b.viam.common.v1.PoseInFrameR\x11poseInParentFrame\x12\x1d\n\nmodel_json\x18\x03 \x01(\x0cR\tmodelJson"n\n\x18FrameSystemConfigRequest\x12R\n\x17supplemental_transforms\x18\x01 \x03(\x0b2\x19.viam.common.v1.TransformR\x16supplementalTransforms"o\n\x19FrameSystemConfigResponse\x12R\n\x14frame_system_configs\x18\x01 \x03(\x0b2 .viam.robot.v1.FrameSystemConfigR\x12frameSystemConfigs"\xc1\x01\n\x14TransformPoseRequest\x123\n\x06source\x18\x01 \x01(\x0b2\x1b.viam.common.v1.PoseInFrameR\x06source\x12 \n\x0bdestination\x18\x02 \x01(\tR\x0bdestination\x12R\n\x17supplemental_transforms\x18\x03 \x03(\x0b2\x19.viam.common.v1.TransformR\x16supplementalTransforms"H\n\x15TransformPoseResponse\x12/\n\x04pose\x18\x01 \x01(\x0b2\x1b.viam.common.v1.PoseInFrameR\x04pose"\x16\n\x14ResourceNamesRequest"S\n\x15ResourceNamesResponse\x12:\n\tresources\x18\x01 \x03(\x0b2\x1c.viam.common.v1.ResourceNameR\tresources"q\n\x12ResourceRPCSubtype\x126\n\x07subtype\x18\x01 \x01(\x0b2\x1c.viam.common.v1.ResourceNameR\x07subtype\x12#\n\rproto_service\x18\x02 \x01(\tR\x0cprotoService"\x1c\n\x1aResourceRPCSubtypesRequest"t\n\x1bResourceRPCSubtypesResponse\x12U\n\x15resource_rpc_subtypes\x18\x01 \x03(\x0b2!.viam.robot.v1.ResourceRPCSubtypeR\x13resourceRpcSubtypes"\xa0\x01\n\tOperation\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x16\n\x06method\x18\x02 \x01(\tR\x06method\x125\n\targuments\x18\x03 \x01(\x0b2\x17.google.protobuf.StructR\targuments\x124\n\x07started\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampR\x07started"\x16\n\x14GetOperationsRequest"Q\n\x15GetOperationsResponse\x128\n\noperations\x18\x01 \x03(\x0b2\x18.viam.robot.v1.OperationR\noperations"(\n\x16CancelOperationRequest\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id"\x19\n\x17CancelOperationResponse"*\n\x18BlockForOperationRequest\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id"\x1b\n\x19BlockForOperationResponse"@\n\x0eDiscoveryQuery\x12\x18\n\x07subtype\x18\x01 \x01(\tR\x07subtype\x12\x14\n\x05model\x18\x02 \x01(\tR\x05model"s\n\tDiscovery\x123\n\x05query\x18\x01 \x01(\x0b2\x1d.viam.robot.v1.DiscoveryQueryR\x05query\x121\n\x07results\x18\x02 \x01(\x0b2\x17.google.protobuf.StructR\x07results"T\n\x19DiscoverComponentsRequest\x127\n\x07queries\x18\x01 \x03(\x0b2\x1d.viam.robot.v1.DiscoveryQueryR\x07queries"T\n\x1aDiscoverComponentsResponse\x126\n\tdiscovery\x18\x01 \x03(\x0b2\x18.viam.robot.v1.DiscoveryR\tdiscovery"k\n\x06Status\x120\n\x04name\x18\x01 \x01(\x0b2\x1c.viam.common.v1.ResourceNameR\x04name\x12/\n\x06status\x18\x02 \x01(\x0b2\x17.google.protobuf.StructR\x06status"W\n\x10GetStatusRequest\x12C\n\x0eresource_names\x18\x01 \x03(\x0b2\x1c.viam.common.v1.ResourceNameR\rresourceNames"B\n\x11GetStatusResponse\x12-\n\x06status\x18\x01 \x03(\x0b2\x15.viam.robot.v1.StatusR\x06status"\x8b\x01\n\x13StreamStatusRequest\x12C\n\x0eresource_names\x18\x01 \x03(\x0b2\x1c.viam.common.v1.ResourceNameR\rresourceNames\x12/\n\x05every\x18\x02 \x01(\x0b2\x19.google.protobuf.DurationR\x05every"E\n\x14StreamStatusResponse\x12-\n\x06status\x18\x01 \x03(\x0b2\x15.viam.robot.v1.StatusR\x06status"x\n\x13StopExtraParameters\x120\n\x04name\x18\x01 \x01(\x0b2\x1c.viam.common.v1.ResourceNameR\x04name\x12/\n\x06params\x18\x02 \x01(\x0b2\x17.google.protobuf.StructR\x06params"J\n\x0eStopAllRequest\x128\n\x05extra\x18c \x03(\x0b2".viam.robot.v1.StopExtraParametersR\x05extra"\x11\n\x0fStopAllResponse2\xdb\x0b\n\x0cRobotService\x12\x80\x01\n\rGetOperations\x12#.viam.robot.v1.GetOperationsRequest\x1a$.viam.robot.v1.GetOperationsResponse"$\x82\xd3\xe4\x93\x02\x1e\x12\x1c/viam/api/v1/operations/list\x12\x7f\n\rResourceNames\x12#.viam.robot.v1.ResourceNamesRequest\x1a$.viam.robot.v1.ResourceNamesResponse"#\x82\xd3\xe4\x93\x02\x1d\x12\x1b/viam/api/v1/resources/list\x12\x9d\x01\n\x13ResourceRPCSubtypes\x12).viam.robot.v1.ResourceRPCSubtypesRequest\x1a*.viam.robot.v1.ResourceRPCSubtypesResponse"/\x82\xd3\xe4\x93\x02)\x12\'/viam/api/v1/resource_rpc_subtypes/list\x12\x88\x01\n\x0fCancelOperation\x12%.viam.robot.v1.CancelOperationRequest\x1a&.viam.robot.v1.CancelOperationResponse"&\x82\xd3\xe4\x93\x02 "\x1e/viam/api/v1/operations/cancel\x12\x8d\x01\n\x11BlockForOperation\x12\'.viam.robot.v1.BlockForOperationRequest\x1a(.viam.robot.v1.BlockForOperationResponse"%\x82\xd3\xe4\x93\x02\x1f"\x1d/viam/api/v1/operations/block\x12\x94\x01\n\x12DiscoverComponents\x12(.viam.robot.v1.DiscoverComponentsRequest\x1a).viam.robot.v1.DiscoverComponentsResponse")\x82\xd3\xe4\x93\x02#\x12!/viam/api/v1/discovery/components\x12\x90\x01\n\x11FrameSystemConfig\x12\'.viam.robot.v1.FrameSystemConfigRequest\x1a(.viam.robot.v1.FrameSystemConfigResponse"(\x82\xd3\xe4\x93\x02"\x12 /viam/api/v1/frame_system/config\x12\x8c\x01\n\rTransformPose\x12#.viam.robot.v1.TransformPoseRequest\x1a$.viam.robot.v1.TransformPoseResponse"0\x82\xd3\xe4\x93\x02*\x12(/viam/api/v1/frame_system/transform_pose\x12k\n\tGetStatus\x12\x1f.viam.robot.v1.GetStatusRequest\x1a .viam.robot.v1.GetStatusResponse"\x1b\x82\xd3\xe4\x93\x02\x15\x12\x13/viam/api/v1/status\x12}\n\x0cStreamStatus\x12".viam.robot.v1.StreamStatusRequest\x1a#.viam.robot.v1.StreamStatusResponse""\x82\xd3\xe4\x93\x02\x1c\x12\x1a/viam/api/v1/status/stream0\x01\x12g\n\x07StopAll\x12\x1d.viam.robot.v1.StopAllRequest\x1a\x1e.viam.robot.v1.StopAllResponse"\x1d\x82\xd3\xe4\x93\x02\x17\x12\x15/viam/api/v1/stop_allB-\n\x11com.viam.robot.v1Z\x18go.viam.com/api/robot/v1b\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'robot.v1.robot_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n\x11com.viam.robot.v1Z\x18go.viam.com/api/robot/v1'
    _ROBOTSERVICE.methods_by_name['GetOperations']._options = None
    _ROBOTSERVICE.methods_by_name['GetOperations']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1e\x12\x1c/viam/api/v1/operations/list'
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
    _ROBOTSERVICE.methods_by_name['GetStatus']._options = None
    _ROBOTSERVICE.methods_by_name['GetStatus']._serialized_options = b'\x82\xd3\xe4\x93\x02\x15\x12\x13/viam/api/v1/status'
    _ROBOTSERVICE.methods_by_name['StreamStatus']._options = None
    _ROBOTSERVICE.methods_by_name['StreamStatus']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1c\x12\x1a/viam/api/v1/status/stream'
    _ROBOTSERVICE.methods_by_name['StopAll']._options = None
    _ROBOTSERVICE.methods_by_name['StopAll']._serialized_options = b'\x82\xd3\xe4\x93\x02\x17\x12\x15/viam/api/v1/stop_all'
    _FRAMESYSTEMCONFIG._serialized_start = 189
    _FRAMESYSTEMCONFIG._serialized_end = 337
    _FRAMESYSTEMCONFIGREQUEST._serialized_start = 339
    _FRAMESYSTEMCONFIGREQUEST._serialized_end = 449
    _FRAMESYSTEMCONFIGRESPONSE._serialized_start = 451
    _FRAMESYSTEMCONFIGRESPONSE._serialized_end = 562
    _TRANSFORMPOSEREQUEST._serialized_start = 565
    _TRANSFORMPOSEREQUEST._serialized_end = 758
    _TRANSFORMPOSERESPONSE._serialized_start = 760
    _TRANSFORMPOSERESPONSE._serialized_end = 832
    _RESOURCENAMESREQUEST._serialized_start = 834
    _RESOURCENAMESREQUEST._serialized_end = 856
    _RESOURCENAMESRESPONSE._serialized_start = 858
    _RESOURCENAMESRESPONSE._serialized_end = 941
    _RESOURCERPCSUBTYPE._serialized_start = 943
    _RESOURCERPCSUBTYPE._serialized_end = 1056
    _RESOURCERPCSUBTYPESREQUEST._serialized_start = 1058
    _RESOURCERPCSUBTYPESREQUEST._serialized_end = 1086
    _RESOURCERPCSUBTYPESRESPONSE._serialized_start = 1088
    _RESOURCERPCSUBTYPESRESPONSE._serialized_end = 1204
    _OPERATION._serialized_start = 1207
    _OPERATION._serialized_end = 1367
    _GETOPERATIONSREQUEST._serialized_start = 1369
    _GETOPERATIONSREQUEST._serialized_end = 1391
    _GETOPERATIONSRESPONSE._serialized_start = 1393
    _GETOPERATIONSRESPONSE._serialized_end = 1474
    _CANCELOPERATIONREQUEST._serialized_start = 1476
    _CANCELOPERATIONREQUEST._serialized_end = 1516
    _CANCELOPERATIONRESPONSE._serialized_start = 1518
    _CANCELOPERATIONRESPONSE._serialized_end = 1543
    _BLOCKFOROPERATIONREQUEST._serialized_start = 1545
    _BLOCKFOROPERATIONREQUEST._serialized_end = 1587
    _BLOCKFOROPERATIONRESPONSE._serialized_start = 1589
    _BLOCKFOROPERATIONRESPONSE._serialized_end = 1616
    _DISCOVERYQUERY._serialized_start = 1618
    _DISCOVERYQUERY._serialized_end = 1682
    _DISCOVERY._serialized_start = 1684
    _DISCOVERY._serialized_end = 1799
    _DISCOVERCOMPONENTSREQUEST._serialized_start = 1801
    _DISCOVERCOMPONENTSREQUEST._serialized_end = 1885
    _DISCOVERCOMPONENTSRESPONSE._serialized_start = 1887
    _DISCOVERCOMPONENTSRESPONSE._serialized_end = 1971
    _STATUS._serialized_start = 1973
    _STATUS._serialized_end = 2080
    _GETSTATUSREQUEST._serialized_start = 2082
    _GETSTATUSREQUEST._serialized_end = 2169
    _GETSTATUSRESPONSE._serialized_start = 2171
    _GETSTATUSRESPONSE._serialized_end = 2237
    _STREAMSTATUSREQUEST._serialized_start = 2240
    _STREAMSTATUSREQUEST._serialized_end = 2379
    _STREAMSTATUSRESPONSE._serialized_start = 2381
    _STREAMSTATUSRESPONSE._serialized_end = 2450
    _STOPEXTRAPARAMETERS._serialized_start = 2452
    _STOPEXTRAPARAMETERS._serialized_end = 2572
    _STOPALLREQUEST._serialized_start = 2574
    _STOPALLREQUEST._serialized_end = 2648
    _STOPALLRESPONSE._serialized_start = 2650
    _STOPALLRESPONSE._serialized_end = 2667
    _ROBOTSERVICE._serialized_start = 2670
    _ROBOTSERVICE._serialized_end = 4169