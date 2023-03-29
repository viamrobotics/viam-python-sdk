"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....common.v1 import common_pb2 as common_dot_v1_dot_common__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1aservice/slam/v1/slam.proto\x12\x14viam.service.slam.v1\x1a\x16common/v1/common.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1cgoogle/protobuf/struct.proto"(\n\x12GetPositionRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name"\x9f\x01\n\x13GetPositionResponse\x12(\n\x04pose\x18\x01 \x01(\x0b2\x14.viam.common.v1.PoseR\x04pose\x12/\n\x13component_reference\x18\x02 \x01(\tR\x12componentReference\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"-\n\x17GetPointCloudMapRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name"M\n\x18GetPointCloudMapResponse\x121\n\x15point_cloud_pcd_chunk\x18\x01 \x01(\x0cR\x12pointCloudPcdChunk"-\n\x17GetInternalStateRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name"L\n\x18GetInternalStateResponse\x120\n\x14internal_state_chunk\x18\x01 \x01(\x0cR\x12internalStateChunk"/\n\x15GetPositionNewRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name:\x02\x18\x01"\xa6\x01\n\x16GetPositionNewResponse\x12(\n\x04pose\x18\x01 \x01(\x0b2\x14.viam.common.v1.PoseR\x04pose\x12/\n\x13component_reference\x18\x02 \x01(\tR\x12componentReference\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra:\x02\x18\x01"7\n\x1dGetPointCloudMapStreamRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name:\x02\x18\x01"W\n\x1eGetPointCloudMapStreamResponse\x121\n\x15point_cloud_pcd_chunk\x18\x01 \x01(\x0cR\x12pointCloudPcdChunk:\x02\x18\x01"7\n\x1dGetInternalStateStreamRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name:\x02\x18\x01"V\n\x1eGetInternalStateStreamResponse\x120\n\x14internal_state_chunk\x18\x01 \x01(\x0cR\x12internalStateChunk:\x02\x18\x012\xcb\t\n\x0bSLAMService\x12\x95\x01\n\x0bGetPosition\x12(.viam.service.slam.v1.GetPositionRequest\x1a).viam.service.slam.v1.GetPositionResponse"1\x82\xd3\xe4\x93\x02+\x12)/viam/api/v1/service/slam/{name}/position\x12\xad\x01\n\x10GetPointCloudMap\x12-.viam.service.slam.v1.GetPointCloudMapRequest\x1a..viam.service.slam.v1.GetPointCloudMapResponse"8\x82\xd3\xe4\x93\x022\x120/viam/api/v1/service/slam/{name}/point_cloud_map0\x01\x12\xac\x01\n\x10GetInternalState\x12-.viam.service.slam.v1.GetInternalStateRequest\x1a..viam.service.slam.v1.GetInternalStateResponse"7\x82\xd3\xe4\x93\x021\x12//viam/api/v1/service/slam/{name}/internal_state0\x01\x12\xa5\x01\n\x0eGetPositionNew\x12+.viam.service.slam.v1.GetPositionNewRequest\x1a,.viam.service.slam.v1.GetPositionNewResponse"8\x88\x02\x01\x82\xd3\xe4\x93\x02/\x12-/viam/api/v1/service/slam/{name}/position_new\x12\xc9\x01\n\x16GetPointCloudMapStream\x123.viam.service.slam.v1.GetPointCloudMapStreamRequest\x1a4.viam.service.slam.v1.GetPointCloudMapStreamResponse"B\x88\x02\x01\x82\xd3\xe4\x93\x029\x127/viam/api/v1/service/slam/{name}/point_cloud_map_stream0\x01\x12\xc8\x01\n\x16GetInternalStateStream\x123.viam.service.slam.v1.GetInternalStateStreamRequest\x1a4.viam.service.slam.v1.GetInternalStateStreamResponse"A\x88\x02\x01\x82\xd3\xe4\x93\x028\x126/viam/api/v1/service/slam/{name}/internal_state_stream0\x01\x12\x85\x01\n\tDoCommand\x12 .viam.common.v1.DoCommandRequest\x1a!.viam.common.v1.DoCommandResponse"3\x82\xd3\xe4\x93\x02-"+/viam/api/v1/service/slam/{name}/do_commandB;\n\x18com.viam.service.slam.v1Z\x1fgo.viam.com/api/service/slam/v1b\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'service.slam.v1.slam_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n\x18com.viam.service.slam.v1Z\x1fgo.viam.com/api/service/slam/v1'
    _GETPOSITIONNEWREQUEST._options = None
    _GETPOSITIONNEWREQUEST._serialized_options = b'\x18\x01'
    _GETPOSITIONNEWRESPONSE._options = None
    _GETPOSITIONNEWRESPONSE._serialized_options = b'\x18\x01'
    _GETPOINTCLOUDMAPSTREAMREQUEST._options = None
    _GETPOINTCLOUDMAPSTREAMREQUEST._serialized_options = b'\x18\x01'
    _GETPOINTCLOUDMAPSTREAMRESPONSE._options = None
    _GETPOINTCLOUDMAPSTREAMRESPONSE._serialized_options = b'\x18\x01'
    _GETINTERNALSTATESTREAMREQUEST._options = None
    _GETINTERNALSTATESTREAMREQUEST._serialized_options = b'\x18\x01'
    _GETINTERNALSTATESTREAMRESPONSE._options = None
    _GETINTERNALSTATESTREAMRESPONSE._serialized_options = b'\x18\x01'
    _SLAMSERVICE.methods_by_name['GetPosition']._options = None
    _SLAMSERVICE.methods_by_name['GetPosition']._serialized_options = b'\x82\xd3\xe4\x93\x02+\x12)/viam/api/v1/service/slam/{name}/position'
    _SLAMSERVICE.methods_by_name['GetPointCloudMap']._options = None
    _SLAMSERVICE.methods_by_name['GetPointCloudMap']._serialized_options = b'\x82\xd3\xe4\x93\x022\x120/viam/api/v1/service/slam/{name}/point_cloud_map'
    _SLAMSERVICE.methods_by_name['GetInternalState']._options = None
    _SLAMSERVICE.methods_by_name['GetInternalState']._serialized_options = b'\x82\xd3\xe4\x93\x021\x12//viam/api/v1/service/slam/{name}/internal_state'
    _SLAMSERVICE.methods_by_name['GetPositionNew']._options = None
    _SLAMSERVICE.methods_by_name['GetPositionNew']._serialized_options = b'\x88\x02\x01\x82\xd3\xe4\x93\x02/\x12-/viam/api/v1/service/slam/{name}/position_new'
    _SLAMSERVICE.methods_by_name['GetPointCloudMapStream']._options = None
    _SLAMSERVICE.methods_by_name['GetPointCloudMapStream']._serialized_options = b'\x88\x02\x01\x82\xd3\xe4\x93\x029\x127/viam/api/v1/service/slam/{name}/point_cloud_map_stream'
    _SLAMSERVICE.methods_by_name['GetInternalStateStream']._options = None
    _SLAMSERVICE.methods_by_name['GetInternalStateStream']._serialized_options = b'\x88\x02\x01\x82\xd3\xe4\x93\x028\x126/viam/api/v1/service/slam/{name}/internal_state_stream'
    _SLAMSERVICE.methods_by_name['DoCommand']._options = None
    _SLAMSERVICE.methods_by_name['DoCommand']._serialized_options = b'\x82\xd3\xe4\x93\x02-"+/viam/api/v1/service/slam/{name}/do_command'
    _GETPOSITIONREQUEST._serialized_start = 136
    _GETPOSITIONREQUEST._serialized_end = 176
    _GETPOSITIONRESPONSE._serialized_start = 179
    _GETPOSITIONRESPONSE._serialized_end = 338
    _GETPOINTCLOUDMAPREQUEST._serialized_start = 340
    _GETPOINTCLOUDMAPREQUEST._serialized_end = 385
    _GETPOINTCLOUDMAPRESPONSE._serialized_start = 387
    _GETPOINTCLOUDMAPRESPONSE._serialized_end = 464
    _GETINTERNALSTATEREQUEST._serialized_start = 466
    _GETINTERNALSTATEREQUEST._serialized_end = 511
    _GETINTERNALSTATERESPONSE._serialized_start = 513
    _GETINTERNALSTATERESPONSE._serialized_end = 589
    _GETPOSITIONNEWREQUEST._serialized_start = 591
    _GETPOSITIONNEWREQUEST._serialized_end = 638
    _GETPOSITIONNEWRESPONSE._serialized_start = 641
    _GETPOSITIONNEWRESPONSE._serialized_end = 807
    _GETPOINTCLOUDMAPSTREAMREQUEST._serialized_start = 809
    _GETPOINTCLOUDMAPSTREAMREQUEST._serialized_end = 864
    _GETPOINTCLOUDMAPSTREAMRESPONSE._serialized_start = 866
    _GETPOINTCLOUDMAPSTREAMRESPONSE._serialized_end = 953
    _GETINTERNALSTATESTREAMREQUEST._serialized_start = 955
    _GETINTERNALSTATESTREAMREQUEST._serialized_end = 1010
    _GETINTERNALSTATESTREAMRESPONSE._serialized_start = 1012
    _GETINTERNALSTATESTREAMRESPONSE._serialized_end = 1098
    _SLAMSERVICE._serialized_start = 1101
    _SLAMSERVICE._serialized_end = 2328