"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from .....proto.api.common.v1 import common_pb2 as proto_dot_api_dot_common_dot_v1_dot_common__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1eproto/api/robot/v1/robot.proto\x12\x12proto.api.robot.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a proto/api/common/v1/common.proto"\x99\x01\n\x11FrameSystemConfig\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12Q\n\x14pose_in_parent_frame\x18\x02 \x01(\x0b2 .proto.api.common.v1.PoseInFrameR\x11poseInParentFrame\x12\x1d\n\nmodel_json\x18\x03 \x01(\x0cR\tmodelJson"s\n\x18FrameSystemConfigRequest\x12W\n\x17supplemental_transforms\x18\x01 \x03(\x0b2\x1e.proto.api.common.v1.TransformR\x16supplementalTransforms"t\n\x19FrameSystemConfigResponse\x12W\n\x14frame_system_configs\x18\x01 \x03(\x0b2%.proto.api.robot.v1.FrameSystemConfigR\x12frameSystemConfigs"\xcb\x01\n\x14TransformPoseRequest\x128\n\x06source\x18\x01 \x01(\x0b2 .proto.api.common.v1.PoseInFrameR\x06source\x12 \n\x0bdestination\x18\x02 \x01(\tR\x0bdestination\x12W\n\x17supplemental_transforms\x18\x03 \x03(\x0b2\x1e.proto.api.common.v1.TransformR\x16supplementalTransforms"M\n\x15TransformPoseResponse\x124\n\x04pose\x18\x01 \x01(\x0b2 .proto.api.common.v1.PoseInFrameR\x04pose"\x16\n\x14ResourceNamesRequest"X\n\x15ResourceNamesResponse\x12?\n\tresources\x18\x01 \x03(\x0b2!.proto.api.common.v1.ResourceNameR\tresources"\xa0\x01\n\tOperation\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x16\n\x06method\x18\x02 \x01(\tR\x06method\x125\n\targuments\x18\x03 \x01(\x0b2\x17.google.protobuf.StructR\targuments\x124\n\x07started\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampR\x07started"\x16\n\x14GetOperationsRequest"V\n\x15GetOperationsResponse\x12=\n\noperations\x18\x01 \x03(\x0b2\x1d.proto.api.robot.v1.OperationR\noperations"(\n\x16CancelOperationRequest\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id"\x19\n\x17CancelOperationResponse"*\n\x18BlockForOperationRequest\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id"\x1b\n\x19BlockForOperationResponse"@\n\x0eDiscoveryQuery\x12\x18\n\x07subtype\x18\x01 \x01(\tR\x07subtype\x12\x14\n\x05model\x18\x02 \x01(\tR\x05model"x\n\tDiscovery\x128\n\x05query\x18\x01 \x01(\x0b2".proto.api.robot.v1.DiscoveryQueryR\x05query\x121\n\x07results\x18\x02 \x01(\x0b2\x17.google.protobuf.StructR\x07results"Y\n\x19DiscoverComponentsRequest\x12<\n\x07queries\x18\x01 \x03(\x0b2".proto.api.robot.v1.DiscoveryQueryR\x07queries"Y\n\x1aDiscoverComponentsResponse\x12;\n\tdiscovery\x18\x01 \x03(\x0b2\x1d.proto.api.robot.v1.DiscoveryR\tdiscovery"p\n\x06Status\x125\n\x04name\x18\x01 \x01(\x0b2!.proto.api.common.v1.ResourceNameR\x04name\x12/\n\x06status\x18\x02 \x01(\x0b2\x17.google.protobuf.StructR\x06status"\\\n\x10GetStatusRequest\x12H\n\x0eresource_names\x18\x01 \x03(\x0b2!.proto.api.common.v1.ResourceNameR\rresourceNames"G\n\x11GetStatusResponse\x122\n\x06status\x18\x01 \x03(\x0b2\x1a.proto.api.robot.v1.StatusR\x06status"\x90\x01\n\x13StreamStatusRequest\x12H\n\x0eresource_names\x18\x01 \x03(\x0b2!.proto.api.common.v1.ResourceNameR\rresourceNames\x12/\n\x05every\x18\x02 \x01(\x0b2\x19.google.protobuf.DurationR\x05every"J\n\x14StreamStatusResponse\x122\n\x06status\x18\x01 \x03(\x0b2\x1a.proto.api.robot.v1.StatusR\x06status2\xae\n\n\x0cRobotService\x12\x8a\x01\n\rGetOperations\x12(.proto.api.robot.v1.GetOperationsRequest\x1a).proto.api.robot.v1.GetOperationsResponse"$\x82\xd3\xe4\x93\x02\x1e\x12\x1c/viam/api/v1/operations/list\x12\x89\x01\n\rResourceNames\x12(.proto.api.robot.v1.ResourceNamesRequest\x1a).proto.api.robot.v1.ResourceNamesResponse"#\x82\xd3\xe4\x93\x02\x1d\x12\x1b/viam/api/v1/resources/list\x12\x92\x01\n\x0fCancelOperation\x12*.proto.api.robot.v1.CancelOperationRequest\x1a+.proto.api.robot.v1.CancelOperationResponse"&\x82\xd3\xe4\x93\x02 "\x1e/viam/api/v1/operations/cancel\x12\x97\x01\n\x11BlockForOperation\x12,.proto.api.robot.v1.BlockForOperationRequest\x1a-.proto.api.robot.v1.BlockForOperationResponse"%\x82\xd3\xe4\x93\x02\x1f"\x1d/viam/api/v1/operations/block\x12\x9e\x01\n\x12DiscoverComponents\x12-.proto.api.robot.v1.DiscoverComponentsRequest\x1a..proto.api.robot.v1.DiscoverComponentsResponse")\x82\xd3\xe4\x93\x02#\x12!/viam/api/v1/discovery/components\x12\x9a\x01\n\x11FrameSystemConfig\x12,.proto.api.robot.v1.FrameSystemConfigRequest\x1a-.proto.api.robot.v1.FrameSystemConfigResponse"(\x82\xd3\xe4\x93\x02"\x12 /viam/api/v1/frame_system/config\x12\x96\x01\n\rTransformPose\x12(.proto.api.robot.v1.TransformPoseRequest\x1a).proto.api.robot.v1.TransformPoseResponse"0\x82\xd3\xe4\x93\x02*\x12(/viam/api/v1/frame_system/transform_pose\x12u\n\tGetStatus\x12$.proto.api.robot.v1.GetStatusRequest\x1a%.proto.api.robot.v1.GetStatusResponse"\x1b\x82\xd3\xe4\x93\x02\x15\x12\x13/viam/api/v1/status\x12\x87\x01\n\x0cStreamStatus\x12\'.proto.api.robot.v1.StreamStatusRequest\x1a(.proto.api.robot.v1.StreamStatusResponse""\x82\xd3\xe4\x93\x02\x1c\x12\x1a/viam/api/v1/status/stream0\x01BE\n\x1fcom.viam.rdk.proto.api.robot.v1Z"go.viam.com/rdk/proto/api/robot/v1b\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'proto.api.robot.v1.robot_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n\x1fcom.viam.rdk.proto.api.robot.v1Z"go.viam.com/rdk/proto/api/robot/v1'
    _ROBOTSERVICE.methods_by_name['GetOperations']._options = None
    _ROBOTSERVICE.methods_by_name['GetOperations']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1e\x12\x1c/viam/api/v1/operations/list'
    _ROBOTSERVICE.methods_by_name['ResourceNames']._options = None
    _ROBOTSERVICE.methods_by_name['ResourceNames']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1d\x12\x1b/viam/api/v1/resources/list'
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
    _FRAMESYSTEMCONFIG._serialized_start = 214
    _FRAMESYSTEMCONFIG._serialized_end = 367
    _FRAMESYSTEMCONFIGREQUEST._serialized_start = 369
    _FRAMESYSTEMCONFIGREQUEST._serialized_end = 484
    _FRAMESYSTEMCONFIGRESPONSE._serialized_start = 486
    _FRAMESYSTEMCONFIGRESPONSE._serialized_end = 602
    _TRANSFORMPOSEREQUEST._serialized_start = 605
    _TRANSFORMPOSEREQUEST._serialized_end = 808
    _TRANSFORMPOSERESPONSE._serialized_start = 810
    _TRANSFORMPOSERESPONSE._serialized_end = 887
    _RESOURCENAMESREQUEST._serialized_start = 889
    _RESOURCENAMESREQUEST._serialized_end = 911
    _RESOURCENAMESRESPONSE._serialized_start = 913
    _RESOURCENAMESRESPONSE._serialized_end = 1001
    _OPERATION._serialized_start = 1004
    _OPERATION._serialized_end = 1164
    _GETOPERATIONSREQUEST._serialized_start = 1166
    _GETOPERATIONSREQUEST._serialized_end = 1188
    _GETOPERATIONSRESPONSE._serialized_start = 1190
    _GETOPERATIONSRESPONSE._serialized_end = 1276
    _CANCELOPERATIONREQUEST._serialized_start = 1278
    _CANCELOPERATIONREQUEST._serialized_end = 1318
    _CANCELOPERATIONRESPONSE._serialized_start = 1320
    _CANCELOPERATIONRESPONSE._serialized_end = 1345
    _BLOCKFOROPERATIONREQUEST._serialized_start = 1347
    _BLOCKFOROPERATIONREQUEST._serialized_end = 1389
    _BLOCKFOROPERATIONRESPONSE._serialized_start = 1391
    _BLOCKFOROPERATIONRESPONSE._serialized_end = 1418
    _DISCOVERYQUERY._serialized_start = 1420
    _DISCOVERYQUERY._serialized_end = 1484
    _DISCOVERY._serialized_start = 1486
    _DISCOVERY._serialized_end = 1606
    _DISCOVERCOMPONENTSREQUEST._serialized_start = 1608
    _DISCOVERCOMPONENTSREQUEST._serialized_end = 1697
    _DISCOVERCOMPONENTSRESPONSE._serialized_start = 1699
    _DISCOVERCOMPONENTSRESPONSE._serialized_end = 1788
    _STATUS._serialized_start = 1790
    _STATUS._serialized_end = 1902
    _GETSTATUSREQUEST._serialized_start = 1904
    _GETSTATUSREQUEST._serialized_end = 1996
    _GETSTATUSRESPONSE._serialized_start = 1998
    _GETSTATUSRESPONSE._serialized_end = 2069
    _STREAMSTATUSREQUEST._serialized_start = 2072
    _STREAMSTATUSREQUEST._serialized_end = 2216
    _STREAMSTATUSRESPONSE._serialized_start = 2218
    _STREAMSTATUSRESPONSE._serialized_end = 2292
    _ROBOTSERVICE._serialized_start = 2295
    _ROBOTSERVICE._serialized_end = 3621