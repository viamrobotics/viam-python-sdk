"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......proto.api.common.v1 import common_pb2 as proto_dot_api_dot_common_dot_v1_dot_common__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$proto/api/service/slam/v1/slam.proto\x12\x19proto.api.service.slam.v1\x1a\x1cgoogle/api/annotations.proto\x1a proto/api/common/v1/common.proto"(\n\x12GetPositionRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name"K\n\x13GetPositionResponse\x124\n\x04pose\x18\x01 \x01(\x0b2 .proto.api.common.v1.PoseInFrameR\x04pose"\xcf\x01\n\rGetMapRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x1b\n\tmime_type\x18\x02 \x01(\tR\x08mimeType\x12G\n\x0fcamera_position\x18\x03 \x01(\x0b2\x19.proto.api.common.v1.PoseH\x00R\x0ecameraPosition\x88\x01\x01\x120\n\x14include_robot_marker\x18\x04 \x01(\x08R\x12includeRobotMarkerB\x12\n\x10_camera_position"\x96\x01\n\x0eGetMapResponse\x12H\n\x0bpoint_cloud\x18\x01 \x01(\x0b2%.proto.api.common.v1.PointCloudObjectH\x00R\npointCloud\x12\x16\n\x05image\x18\x02 \x01(\x0cH\x00R\x05image\x12\x1b\n\tmime_type\x18\x03 \x01(\tR\x08mimeTypeB\x05\n\x03map2\xbd\x02\n\x0bSLAMService\x12\x9f\x01\n\x0bGetPosition\x12-.proto.api.service.slam.v1.GetPositionRequest\x1a..proto.api.service.slam.v1.GetPositionResponse"1\x82\xd3\xe4\x93\x02+\x12)/viam/api/v1/service/slam/{name}/position\x12\x8b\x01\n\x06GetMap\x12(.proto.api.service.slam.v1.GetMapRequest\x1a).proto.api.service.slam.v1.GetMapResponse",\x82\xd3\xe4\x93\x02&\x12$/viam/api/v1/service/slam/{name}/mapBS\n&com.viam.rdk.proto.api.service.slam.v1Z)go.viam.com/rdk/proto/api/service/slam/v1b\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'proto.api.service.slam.v1.slam_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n&com.viam.rdk.proto.api.service.slam.v1Z)go.viam.com/rdk/proto/api/service/slam/v1'
    _SLAMSERVICE.methods_by_name['GetPosition']._options = None
    _SLAMSERVICE.methods_by_name['GetPosition']._serialized_options = b'\x82\xd3\xe4\x93\x02+\x12)/viam/api/v1/service/slam/{name}/position'
    _SLAMSERVICE.methods_by_name['GetMap']._options = None
    _SLAMSERVICE.methods_by_name['GetMap']._serialized_options = b'\x82\xd3\xe4\x93\x02&\x12$/viam/api/v1/service/slam/{name}/map'
    _GETPOSITIONREQUEST._serialized_start = 131
    _GETPOSITIONREQUEST._serialized_end = 171
    _GETPOSITIONRESPONSE._serialized_start = 173
    _GETPOSITIONRESPONSE._serialized_end = 248
    _GETMAPREQUEST._serialized_start = 251
    _GETMAPREQUEST._serialized_end = 458
    _GETMAPRESPONSE._serialized_start = 461
    _GETMAPRESPONSE._serialized_end = 611
    _SLAMSERVICE._serialized_start = 614
    _SLAMSERVICE._serialized_end = 931