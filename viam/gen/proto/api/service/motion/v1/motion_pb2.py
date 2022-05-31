"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......proto.api.common.v1 import common_pb2 as proto_dot_api_dot_common_dot_v1_dot_common__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(proto/api/service/motion/v1/motion.proto\x12\x1bproto.api.service.motion.v1\x1a\x1cgoogle/api/annotations.proto\x1a proto/api/common/v1/common.proto"\xf2\x01\n\x0bMoveRequest\x12B\n\x0bdestination\x18\x01 \x01(\x0b2 .proto.api.common.v1.PoseInFrameR\x0bdestination\x12H\n\x0ecomponent_name\x18\x02 \x01(\x0b2!.proto.api.common.v1.ResourceNameR\rcomponentName\x12E\n\x0bworld_state\x18\x03 \x01(\x0b2\x1f.proto.api.common.v1.WorldStateH\x00R\nworldState\x88\x01\x01B\x0e\n\x0c_world_state"(\n\x0cMoveResponse\x12\x18\n\x07success\x18\x01 \x01(\x08R\x07success"\xe0\x01\n\x0eGetPoseRequest\x12H\n\x0ecomponent_name\x18\x01 \x01(\x0b2!.proto.api.common.v1.ResourceNameR\rcomponentName\x12+\n\x11destination_frame\x18\x02 \x01(\tR\x10destinationFrame\x12W\n\x17supplemental_transforms\x18\x03 \x03(\x0b2\x1e.proto.api.common.v1.TransformR\x16supplementalTransforms"G\n\x0fGetPoseResponse\x124\n\x04pose\x18\x01 \x01(\x0b2 .proto.api.common.v1.PoseInFrameR\x04pose2\xa8\x02\n\rMotionService\x12\x85\x01\n\x04Move\x12(.proto.api.service.motion.v1.MoveRequest\x1a).proto.api.service.motion.v1.MoveResponse"(\x82\xd3\xe4\x93\x02"" /viam/api/v1/service/motion/move\x12\x8e\x01\n\x07GetPose\x12+.proto.api.service.motion.v1.GetPoseRequest\x1a,.proto.api.service.motion.v1.GetPoseResponse"(\x82\xd3\xe4\x93\x02"\x12 /viam/api/v1/service/motion/poseBW\n(com.viam.rdk.proto.api.service.motion.v1Z+go.viam.com/rdk/proto/api/service/motion/v1b\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'proto.api.service.motion.v1.motion_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n(com.viam.rdk.proto.api.service.motion.v1Z+go.viam.com/rdk/proto/api/service/motion/v1'
    _MOTIONSERVICE.methods_by_name['Move']._options = None
    _MOTIONSERVICE.methods_by_name['Move']._serialized_options = b'\x82\xd3\xe4\x93\x02"" /viam/api/v1/service/motion/move'
    _MOTIONSERVICE.methods_by_name['GetPose']._options = None
    _MOTIONSERVICE.methods_by_name['GetPose']._serialized_options = b'\x82\xd3\xe4\x93\x02"\x12 /viam/api/v1/service/motion/pose'
    _MOVEREQUEST._serialized_start = 138
    _MOVEREQUEST._serialized_end = 380
    _MOVERESPONSE._serialized_start = 382
    _MOVERESPONSE._serialized_end = 422
    _GETPOSEREQUEST._serialized_start = 425
    _GETPOSEREQUEST._serialized_end = 649
    _GETPOSERESPONSE._serialized_start = 651
    _GETPOSERESPONSE._serialized_end = 722
    _MOTIONSERVICE._serialized_start = 725
    _MOTIONSERVICE._serialized_end = 1021