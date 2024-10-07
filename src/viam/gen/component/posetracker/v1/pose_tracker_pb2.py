"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 2, '', 'component/posetracker/v1/pose_tracker.proto')
_sym_db = _symbol_database.Default()
from ....common.v1 import common_pb2 as common_dot_v1_dot_common__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+component/posetracker/v1/pose_tracker.proto\x12\x1dviam.component.posetracker.v1\x1a\x16common/v1/common.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1cgoogle/protobuf/struct.proto"s\n\x0fGetPosesRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x1d\n\nbody_names\x18\x02 \x03(\tR\tbodyNames\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"\xcc\x01\n\x10GetPosesResponse\x12]\n\nbody_poses\x18\x01 \x03(\x0b2>.viam.component.posetracker.v1.GetPosesResponse.BodyPosesEntryR\tbodyPoses\x1aY\n\x0eBodyPosesEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x121\n\x05value\x18\x02 \x01(\x0b2\x1b.viam.common.v1.PoseInFrameR\x05value:\x028\x012\xec\x03\n\x12PoseTrackerService\x12\xa5\x01\n\x08GetPoses\x12..viam.component.posetracker.v1.GetPosesRequest\x1a/.viam.component.posetracker.v1.GetPosesResponse"8\x82\xd3\xe4\x93\x022\x120/viam/api/v1/component/pose_tracker/{name}/poses\x12\x8f\x01\n\tDoCommand\x12 .viam.common.v1.DoCommandRequest\x1a!.viam.common.v1.DoCommandResponse"=\x82\xd3\xe4\x93\x027"5/viam/api/v1/component/pose_tracker/{name}/do_command\x12\x9b\x01\n\rGetGeometries\x12$.viam.common.v1.GetGeometriesRequest\x1a%.viam.common.v1.GetGeometriesResponse"=\x82\xd3\xe4\x93\x027\x125/viam/api/v1/component/pose_tracker/{name}/geometriesB5\n\x15com.viam.component.v1Z\x1cgo.viam.com/api/component/v1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'component.posetracker.v1.pose_tracker_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x15com.viam.component.v1Z\x1cgo.viam.com/api/component/v1'
    _globals['_GETPOSESRESPONSE_BODYPOSESENTRY']._loaded_options = None
    _globals['_GETPOSESRESPONSE_BODYPOSESENTRY']._serialized_options = b'8\x01'
    _globals['_POSETRACKERSERVICE'].methods_by_name['GetPoses']._loaded_options = None
    _globals['_POSETRACKERSERVICE'].methods_by_name['GetPoses']._serialized_options = b'\x82\xd3\xe4\x93\x022\x120/viam/api/v1/component/pose_tracker/{name}/poses'
    _globals['_POSETRACKERSERVICE'].methods_by_name['DoCommand']._loaded_options = None
    _globals['_POSETRACKERSERVICE'].methods_by_name['DoCommand']._serialized_options = b'\x82\xd3\xe4\x93\x027"5/viam/api/v1/component/pose_tracker/{name}/do_command'
    _globals['_POSETRACKERSERVICE'].methods_by_name['GetGeometries']._loaded_options = None
    _globals['_POSETRACKERSERVICE'].methods_by_name['GetGeometries']._serialized_options = b'\x82\xd3\xe4\x93\x027\x125/viam/api/v1/component/pose_tracker/{name}/geometries'
    _globals['_GETPOSESREQUEST']._serialized_start = 162
    _globals['_GETPOSESREQUEST']._serialized_end = 277
    _globals['_GETPOSESRESPONSE']._serialized_start = 280
    _globals['_GETPOSESRESPONSE']._serialized_end = 484
    _globals['_GETPOSESRESPONSE_BODYPOSESENTRY']._serialized_start = 395
    _globals['_GETPOSESRESPONSE_BODYPOSESENTRY']._serialized_end = 484
    _globals['_POSETRACKERSERVICE']._serialized_start = 487
    _globals['_POSETRACKERSERVICE']._serialized_end = 979