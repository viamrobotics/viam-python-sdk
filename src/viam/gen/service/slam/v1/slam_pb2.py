"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....common.v1 import common_pb2 as common_dot_v1_dot_common__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1aservice/slam/v1/slam.proto\x12\x14viam.service.slam.v1\x1a\x16common/v1/common.proto\x1a\x1cgoogle/api/annotations.proto"(\n\x12GetPositionRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name"F\n\x13GetPositionResponse\x12/\n\x04pose\x18\x01 \x01(\x0b2\x1b.viam.common.v1.PoseInFrameR\x04pose"\xca\x01\n\rGetMapRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x1b\n\tmime_type\x18\x02 \x01(\tR\x08mimeType\x12B\n\x0fcamera_position\x18\x03 \x01(\x0b2\x14.viam.common.v1.PoseH\x00R\x0ecameraPosition\x88\x01\x01\x120\n\x14include_robot_marker\x18\x04 \x01(\x08R\x12includeRobotMarkerB\x12\n\x10_camera_position"\x91\x01\n\x0eGetMapResponse\x12C\n\x0bpoint_cloud\x18\x01 \x01(\x0b2 .viam.common.v1.PointCloudObjectH\x00R\npointCloud\x12\x16\n\x05image\x18\x02 \x01(\x0cH\x00R\x05image\x12\x1b\n\tmime_type\x18\x03 \x01(\tR\x08mimeTypeB\x05\n\x03map2\xa9\x02\n\x0bSLAMService\x12\x95\x01\n\x0bGetPosition\x12(.viam.service.slam.v1.GetPositionRequest\x1a).viam.service.slam.v1.GetPositionResponse"1\x82\xd3\xe4\x93\x02+\x12)/viam/api/v1/service/slam/{name}/position\x12\x81\x01\n\x06GetMap\x12#.viam.service.slam.v1.GetMapRequest\x1a$.viam.service.slam.v1.GetMapResponse",\x82\xd3\xe4\x93\x02&\x12$/viam/api/v1/service/slam/{name}/mapB;\n\x18com.viam.service.slam.v1Z\x1fgo.viam.com/api/service/slam/v1b\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'service.slam.v1.slam_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n\x18com.viam.service.slam.v1Z\x1fgo.viam.com/api/service/slam/v1'
    _SLAMSERVICE.methods_by_name['GetPosition']._options = None
    _SLAMSERVICE.methods_by_name['GetPosition']._serialized_options = b'\x82\xd3\xe4\x93\x02+\x12)/viam/api/v1/service/slam/{name}/position'
    _SLAMSERVICE.methods_by_name['GetMap']._options = None
    _SLAMSERVICE.methods_by_name['GetMap']._serialized_options = b'\x82\xd3\xe4\x93\x02&\x12$/viam/api/v1/service/slam/{name}/map'
    _GETPOSITIONREQUEST._serialized_start = 106
    _GETPOSITIONREQUEST._serialized_end = 146
    _GETPOSITIONRESPONSE._serialized_start = 148
    _GETPOSITIONRESPONSE._serialized_end = 218
    _GETMAPREQUEST._serialized_start = 221
    _GETMAPREQUEST._serialized_end = 423
    _GETMAPRESPONSE._serialized_start = 426
    _GETMAPRESPONSE._serialized_end = 571
    _SLAMSERVICE._serialized_start = 574
    _SLAMSERVICE._serialized_end = 871