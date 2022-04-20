"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......proto.api.common.v1 import common_pb2 as proto_dot_api_dot_common_dot_v1_dot_common__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n5proto/api/component/posetracker/v1/pose_tracker.proto\x12"proto.api.component.posetracker.v1\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1cgoogle/api/annotations.proto\x1a proto/api/common/v1/common.proto"D\n\x0fGetPosesRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x1d\n\nbody_names\x18\x02 \x03(\tR\tbodyNames"\xd6\x01\n\x10GetPosesResponse\x12b\n\nbody_poses\x18\x01 \x03(\x0b2C.proto.api.component.posetracker.v1.GetPosesResponse.BodyPosesEntryR\tbodyPoses\x1a^\n\x0eBodyPosesEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x126\n\x05value\x18\x02 \x01(\x0b2 .proto.api.common.v1.PoseInFrameR\x05value:\x028\x012\xc6\x01\n\x12PoseTrackerService\x12\xaf\x01\n\x08GetPoses\x123.proto.api.component.posetracker.v1.GetPosesRequest\x1a4.proto.api.component.posetracker.v1.GetPosesResponse"8\x82\xd3\xe4\x93\x022\x120/viam/api/v1/component/pose_tracker/{name}/posesBM\n#com.viam.rdk.proto.api.component.v1Z&go.viam.com/rdk/proto/api/component/v1b\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'proto.api.component.posetracker.v1.pose_tracker_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n#com.viam.rdk.proto.api.component.v1Z&go.viam.com/rdk/proto/api/component/v1'
    _GETPOSESRESPONSE_BODYPOSESENTRY._options = None
    _GETPOSESRESPONSE_BODYPOSESENTRY._serialized_options = b'8\x01'
    _POSETRACKERSERVICE.methods_by_name['GetPoses']._options = None
    _POSETRACKERSERVICE.methods_by_name['GetPoses']._serialized_options = b'\x82\xd3\xe4\x93\x022\x120/viam/api/v1/component/pose_tracker/{name}/poses'
    _GETPOSESREQUEST._serialized_start = 187
    _GETPOSESREQUEST._serialized_end = 255
    _GETPOSESRESPONSE._serialized_start = 258
    _GETPOSESRESPONSE._serialized_end = 472
    _GETPOSESRESPONSE_BODYPOSESENTRY._serialized_start = 378
    _GETPOSESRESPONSE_BODYPOSESENTRY._serialized_end = 472
    _POSETRACKERSERVICE._serialized_start = 475
    _POSETRACKERSERVICE._serialized_end = 673