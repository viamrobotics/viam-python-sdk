"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....common.v1 import common_pb2 as common_dot_v1_dot_common__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1aservice/slam/v1/slam.proto\x12\x14viam.service.slam.v1\x1a\x16common/v1/common.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1cgoogle/protobuf/struct.proto"[\n\x12GetPositionRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra:\x02\x18\x01"y\n\x13GetPositionResponse\x12/\n\x04pose\x18\x01 \x01(\x0b2\x1b.viam.common.v1.PoseInFrameR\x04pose\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra:\x02\x18\x01"\xfd\x01\n\rGetMapRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x1b\n\tmime_type\x18\x02 \x01(\tR\x08mimeType\x12B\n\x0fcamera_position\x18\x03 \x01(\x0b2\x14.viam.common.v1.PoseH\x00R\x0ecameraPosition\x88\x01\x01\x120\n\x14include_robot_marker\x18\x04 \x01(\x08R\x12includeRobotMarker\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra:\x02\x18\x01B\x12\n\x10_camera_position"\x95\x01\n\x0eGetMapResponse\x12C\n\x0bpoint_cloud\x18\x01 \x01(\x0b2 .viam.common.v1.PointCloudObjectH\x00R\npointCloud\x12\x16\n\x05image\x18\x02 \x01(\x0cH\x00R\x05image\x12\x1b\n\tmime_type\x18\x03 \x01(\tR\x08mimeType:\x02\x18\x01B\x05\n\x03map"+\n\x15GetPositionNewRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name"\xa2\x01\n\x16GetPositionNewResponse\x12(\n\x04pose\x18\x01 \x01(\x0b2\x14.viam.common.v1.PoseR\x04pose\x12/\n\x13component_reference\x18\x02 \x01(\tR\x12componentReference\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"1\n\x17GetPointCloudMapRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name:\x02\x18\x01"F\n\x18GetPointCloudMapResponse\x12&\n\x0fpoint_cloud_pcd\x18\x01 \x01(\x0cR\rpointCloudPcd:\x02\x18\x01"1\n\x17GetInternalStateRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name:\x02\x18\x01"E\n\x18GetInternalStateResponse\x12%\n\x0einternal_state\x18\x01 \x01(\x0cR\rinternalState:\x02\x18\x01"3\n\x1dGetPointCloudMapStreamRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name"S\n\x1eGetPointCloudMapStreamResponse\x121\n\x15point_cloud_pcd_chunk\x18\x01 \x01(\x0cR\x12pointCloudPcdChunk"3\n\x1dGetInternalStateStreamRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name"R\n\x1eGetInternalStateStreamResponse\x120\n\x14internal_state_chunk\x18\x01 \x01(\x0cR\x12internalStateChunk2\xcb\n\n\x0bSLAMService\x12\x95\x01\n\x0bGetPosition\x12(.viam.service.slam.v1.GetPositionRequest\x1a).viam.service.slam.v1.GetPositionResponse"1\x82\xd3\xe4\x93\x02+\x12)/viam/api/v1/service/slam/{name}/position\x12\x84\x01\n\x06GetMap\x12#.viam.service.slam.v1.GetMapRequest\x1a$.viam.service.slam.v1.GetMapResponse"/\x88\x02\x01\x82\xd3\xe4\x93\x02&\x12$/viam/api/v1/service/slam/{name}/map\x12\xa2\x01\n\x0eGetPositionNew\x12+.viam.service.slam.v1.GetPositionNewRequest\x1a,.viam.service.slam.v1.GetPositionNewResponse"5\x82\xd3\xe4\x93\x02/\x12-/viam/api/v1/service/slam/{name}/position_new\x12\xae\x01\n\x10GetPointCloudMap\x12-.viam.service.slam.v1.GetPointCloudMapRequest\x1a..viam.service.slam.v1.GetPointCloudMapResponse";\x88\x02\x01\x82\xd3\xe4\x93\x022\x120/viam/api/v1/service/slam/{name}/point_cloud_map\x12\xad\x01\n\x10GetInternalState\x12-.viam.service.slam.v1.GetInternalStateRequest\x1a..viam.service.slam.v1.GetInternalStateResponse":\x88\x02\x01\x82\xd3\xe4\x93\x021\x12//viam/api/v1/service/slam/{name}/internal_state\x12\xc6\x01\n\x16GetPointCloudMapStream\x123.viam.service.slam.v1.GetPointCloudMapStreamRequest\x1a4.viam.service.slam.v1.GetPointCloudMapStreamResponse"?\x82\xd3\xe4\x93\x029\x127/viam/api/v1/service/slam/{name}/point_cloud_map_stream0\x01\x12\xc5\x01\n\x16GetInternalStateStream\x123.viam.service.slam.v1.GetInternalStateStreamRequest\x1a4.viam.service.slam.v1.GetInternalStateStreamResponse">\x82\xd3\xe4\x93\x028\x126/viam/api/v1/service/slam/{name}/internal_state_stream0\x01\x12\x85\x01\n\tDoCommand\x12 .viam.common.v1.DoCommandRequest\x1a!.viam.common.v1.DoCommandResponse"3\x82\xd3\xe4\x93\x02-"+/viam/api/v1/service/slam/{name}/do_commandB;\n\x18com.viam.service.slam.v1Z\x1fgo.viam.com/api/service/slam/v1b\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'service.slam.v1.slam_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n\x18com.viam.service.slam.v1Z\x1fgo.viam.com/api/service/slam/v1'
    _GETPOSITIONREQUEST._options = None
    _GETPOSITIONREQUEST._serialized_options = b'\x18\x01'
    _GETPOSITIONRESPONSE._options = None
    _GETPOSITIONRESPONSE._serialized_options = b'\x18\x01'
    _GETMAPREQUEST._options = None
    _GETMAPREQUEST._serialized_options = b'\x18\x01'
    _GETMAPRESPONSE._options = None
    _GETMAPRESPONSE._serialized_options = b'\x18\x01'
    _GETPOINTCLOUDMAPREQUEST._options = None
    _GETPOINTCLOUDMAPREQUEST._serialized_options = b'\x18\x01'
    _GETPOINTCLOUDMAPRESPONSE._options = None
    _GETPOINTCLOUDMAPRESPONSE._serialized_options = b'\x18\x01'
    _GETINTERNALSTATEREQUEST._options = None
    _GETINTERNALSTATEREQUEST._serialized_options = b'\x18\x01'
    _GETINTERNALSTATERESPONSE._options = None
    _GETINTERNALSTATERESPONSE._serialized_options = b'\x18\x01'
    _SLAMSERVICE.methods_by_name['GetPosition']._options = None
    _SLAMSERVICE.methods_by_name['GetPosition']._serialized_options = b'\x82\xd3\xe4\x93\x02+\x12)/viam/api/v1/service/slam/{name}/position'
    _SLAMSERVICE.methods_by_name['GetMap']._options = None
    _SLAMSERVICE.methods_by_name['GetMap']._serialized_options = b'\x88\x02\x01\x82\xd3\xe4\x93\x02&\x12$/viam/api/v1/service/slam/{name}/map'
    _SLAMSERVICE.methods_by_name['GetPositionNew']._options = None
    _SLAMSERVICE.methods_by_name['GetPositionNew']._serialized_options = b'\x82\xd3\xe4\x93\x02/\x12-/viam/api/v1/service/slam/{name}/position_new'
    _SLAMSERVICE.methods_by_name['GetPointCloudMap']._options = None
    _SLAMSERVICE.methods_by_name['GetPointCloudMap']._serialized_options = b'\x88\x02\x01\x82\xd3\xe4\x93\x022\x120/viam/api/v1/service/slam/{name}/point_cloud_map'
    _SLAMSERVICE.methods_by_name['GetInternalState']._options = None
    _SLAMSERVICE.methods_by_name['GetInternalState']._serialized_options = b'\x88\x02\x01\x82\xd3\xe4\x93\x021\x12//viam/api/v1/service/slam/{name}/internal_state'
    _SLAMSERVICE.methods_by_name['GetPointCloudMapStream']._options = None
    _SLAMSERVICE.methods_by_name['GetPointCloudMapStream']._serialized_options = b'\x82\xd3\xe4\x93\x029\x127/viam/api/v1/service/slam/{name}/point_cloud_map_stream'
    _SLAMSERVICE.methods_by_name['GetInternalStateStream']._options = None
    _SLAMSERVICE.methods_by_name['GetInternalStateStream']._serialized_options = b'\x82\xd3\xe4\x93\x028\x126/viam/api/v1/service/slam/{name}/internal_state_stream'
    _SLAMSERVICE.methods_by_name['DoCommand']._options = None
    _SLAMSERVICE.methods_by_name['DoCommand']._serialized_options = b'\x82\xd3\xe4\x93\x02-"+/viam/api/v1/service/slam/{name}/do_command'
    _GETPOSITIONREQUEST._serialized_start = 136
    _GETPOSITIONREQUEST._serialized_end = 227
    _GETPOSITIONRESPONSE._serialized_start = 229
    _GETPOSITIONRESPONSE._serialized_end = 350
    _GETMAPREQUEST._serialized_start = 353
    _GETMAPREQUEST._serialized_end = 606
    _GETMAPRESPONSE._serialized_start = 609
    _GETMAPRESPONSE._serialized_end = 758
    _GETPOSITIONNEWREQUEST._serialized_start = 760
    _GETPOSITIONNEWREQUEST._serialized_end = 803
    _GETPOSITIONNEWRESPONSE._serialized_start = 806
    _GETPOSITIONNEWRESPONSE._serialized_end = 968
    _GETPOINTCLOUDMAPREQUEST._serialized_start = 970
    _GETPOINTCLOUDMAPREQUEST._serialized_end = 1019
    _GETPOINTCLOUDMAPRESPONSE._serialized_start = 1021
    _GETPOINTCLOUDMAPRESPONSE._serialized_end = 1091
    _GETINTERNALSTATEREQUEST._serialized_start = 1093
    _GETINTERNALSTATEREQUEST._serialized_end = 1142
    _GETINTERNALSTATERESPONSE._serialized_start = 1144
    _GETINTERNALSTATERESPONSE._serialized_end = 1213
    _GETPOINTCLOUDMAPSTREAMREQUEST._serialized_start = 1215
    _GETPOINTCLOUDMAPSTREAMREQUEST._serialized_end = 1266
    _GETPOINTCLOUDMAPSTREAMRESPONSE._serialized_start = 1268
    _GETPOINTCLOUDMAPSTREAMRESPONSE._serialized_end = 1351
    _GETINTERNALSTATESTREAMREQUEST._serialized_start = 1353
    _GETINTERNALSTATESTREAMREQUEST._serialized_end = 1404
    _GETINTERNALSTATESTREAMRESPONSE._serialized_start = 1406
    _GETINTERNALSTATESTREAMRESPONSE._serialized_end = 1488
    _SLAMSERVICE._serialized_start = 1491
    _SLAMSERVICE._serialized_end = 2846