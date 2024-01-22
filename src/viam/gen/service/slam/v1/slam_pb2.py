"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....common.v1 import common_pb2 as common_dot_v1_dot_common__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1aservice/slam/v1/slam.proto\x12\x14viam.service.slam.v1\x1a\x16common/v1/common.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1cgoogle/protobuf/struct.proto"(\n\x12GetPositionRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name"\x9f\x01\n\x13GetPositionResponse\x12(\n\x04pose\x18\x01 \x01(\x0b2\x14.viam.common.v1.PoseR\x04pose\x12/\n\x13component_reference\x18\x02 \x01(\tR\x12componentReference\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"-\n\x17GetPointCloudMapRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name"M\n\x18GetPointCloudMapResponse\x121\n\x15point_cloud_pcd_chunk\x18\x01 \x01(\x0cR\x12pointCloudPcdChunk"-\n\x17GetInternalStateRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name"L\n\x18GetInternalStateResponse\x120\n\x14internal_state_chunk\x18\x01 \x01(\x0cR\x12internalStateChunk"*\n\x14GetPropertiesRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name"|\n\x15GetPropertiesResponse\x12\x1d\n\ncloud_slam\x18\x01 \x01(\x08R\tcloudSlam\x12D\n\x0cmapping_mode\x18\x02 \x01(\x0e2!.viam.service.slam.v1.MappingModeR\x0bmappingMode*\x92\x01\n\x0bMappingMode\x12\x1c\n\x18MAPPING_MODE_UNSPECIFIED\x10\x00\x12\x1f\n\x1bMAPPING_MODE_CREATE_NEW_MAP\x10\x01\x12\x1e\n\x1aMAPPING_MODE_LOCALIZE_ONLY\x10\x02\x12$\n MAPPING_MODE_UPDATE_EXISTING_MAP\x10\x032\xac\x06\n\x0bSLAMService\x12\x95\x01\n\x0bGetPosition\x12(.viam.service.slam.v1.GetPositionRequest\x1a).viam.service.slam.v1.GetPositionResponse"1\x82\xd3\xe4\x93\x02+\x12)/viam/api/v1/service/slam/{name}/position\x12\xad\x01\n\x10GetPointCloudMap\x12-.viam.service.slam.v1.GetPointCloudMapRequest\x1a..viam.service.slam.v1.GetPointCloudMapResponse"8\x82\xd3\xe4\x93\x022\x120/viam/api/v1/service/slam/{name}/point_cloud_map0\x01\x12\xac\x01\n\x10GetInternalState\x12-.viam.service.slam.v1.GetInternalStateRequest\x1a..viam.service.slam.v1.GetInternalStateResponse"7\x82\xd3\xe4\x93\x021\x12//viam/api/v1/service/slam/{name}/internal_state0\x01\x12\x9d\x01\n\rGetProperties\x12*.viam.service.slam.v1.GetPropertiesRequest\x1a+.viam.service.slam.v1.GetPropertiesResponse"3\x82\xd3\xe4\x93\x02-\x12+/viam/api/v1/service/slam/{name}/properties\x12\x85\x01\n\tDoCommand\x12 .viam.common.v1.DoCommandRequest\x1a!.viam.common.v1.DoCommandResponse"3\x82\xd3\xe4\x93\x02-"+/viam/api/v1/service/slam/{name}/do_commandB;\n\x18com.viam.service.slam.v1Z\x1fgo.viam.com/api/service/slam/v1b\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'service.slam.v1.slam_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n\x18com.viam.service.slam.v1Z\x1fgo.viam.com/api/service/slam/v1'
    _SLAMSERVICE.methods_by_name['GetPosition']._options = None
    _SLAMSERVICE.methods_by_name['GetPosition']._serialized_options = b'\x82\xd3\xe4\x93\x02+\x12)/viam/api/v1/service/slam/{name}/position'
    _SLAMSERVICE.methods_by_name['GetPointCloudMap']._options = None
    _SLAMSERVICE.methods_by_name['GetPointCloudMap']._serialized_options = b'\x82\xd3\xe4\x93\x022\x120/viam/api/v1/service/slam/{name}/point_cloud_map'
    _SLAMSERVICE.methods_by_name['GetInternalState']._options = None
    _SLAMSERVICE.methods_by_name['GetInternalState']._serialized_options = b'\x82\xd3\xe4\x93\x021\x12//viam/api/v1/service/slam/{name}/internal_state'
    _SLAMSERVICE.methods_by_name['GetProperties']._options = None
    _SLAMSERVICE.methods_by_name['GetProperties']._serialized_options = b'\x82\xd3\xe4\x93\x02-\x12+/viam/api/v1/service/slam/{name}/properties'
    _SLAMSERVICE.methods_by_name['DoCommand']._options = None
    _SLAMSERVICE.methods_by_name['DoCommand']._serialized_options = b'\x82\xd3\xe4\x93\x02-"+/viam/api/v1/service/slam/{name}/do_command'
    _MAPPINGMODE._serialized_start = 762
    _MAPPINGMODE._serialized_end = 908
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
    _GETPROPERTIESREQUEST._serialized_start = 591
    _GETPROPERTIESREQUEST._serialized_end = 633
    _GETPROPERTIESRESPONSE._serialized_start = 635
    _GETPROPERTIESRESPONSE._serialized_end = 759
    _SLAMSERVICE._serialized_start = 911
    _SLAMSERVICE._serialized_end = 1723