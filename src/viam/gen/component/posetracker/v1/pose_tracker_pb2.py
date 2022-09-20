"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....common.v1 import common_pb2 as common_dot_v1_dot_common__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+component/posetracker/v1/pose_tracker.proto\x12\x1dviam.component.posetracker.v1\x1a\x16common/v1/common.proto\x1a\x1cgoogle/api/annotations.proto"D\n\x0fGetPosesRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x1d\n\nbody_names\x18\x02 \x03(\tR\tbodyNames"\xcc\x01\n\x10GetPosesResponse\x12]\n\nbody_poses\x18\x01 \x03(\x0b2>.viam.component.posetracker.v1.GetPosesResponse.BodyPosesEntryR\tbodyPoses\x1aY\n\x0eBodyPosesEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x121\n\x05value\x18\x02 \x01(\x0b2\x1b.viam.common.v1.PoseInFrameR\x05value:\x028\x012\xbc\x01\n\x12PoseTrackerService\x12\xa5\x01\n\x08GetPoses\x12..viam.component.posetracker.v1.GetPosesRequest\x1a/.viam.component.posetracker.v1.GetPosesResponse"8\x82\xd3\xe4\x93\x022\x120/viam/api/v1/component/pose_tracker/{name}/posesB5\n\x15com.viam.component.v1Z\x1cgo.viam.com/api/component/v1b\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'component.posetracker.v1.pose_tracker_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n\x15com.viam.component.v1Z\x1cgo.viam.com/api/component/v1'
    _GETPOSESRESPONSE_BODYPOSESENTRY._options = None
    _GETPOSESRESPONSE_BODYPOSESENTRY._serialized_options = b'8\x01'
    _POSETRACKERSERVICE.methods_by_name['GetPoses']._options = None
    _POSETRACKERSERVICE.methods_by_name['GetPoses']._serialized_options = b'\x82\xd3\xe4\x93\x022\x120/viam/api/v1/component/pose_tracker/{name}/poses'
    _GETPOSESREQUEST._serialized_start = 132
    _GETPOSESREQUEST._serialized_end = 200
    _GETPOSESRESPONSE._serialized_start = 203
    _GETPOSESRESPONSE._serialized_end = 407
    _GETPOSESRESPONSE_BODYPOSESENTRY._serialized_start = 318
    _GETPOSESRESPONSE_BODYPOSESENTRY._serialized_end = 407
    _POSETRACKERSERVICE._serialized_start = 410
    _POSETRACKERSERVICE._serialized_end = 598