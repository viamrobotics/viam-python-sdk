"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....common.v1 import common_pb2 as common_dot_v1_dot_common__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1eservice/motion/v1/motion.proto\x12\x16viam.service.motion.v1\x1a\x16common/v1/common.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1cgoogle/protobuf/struct.proto"\xa6\x02\n\x0bMoveRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12=\n\x0bdestination\x18\x02 \x01(\x0b2\x1b.viam.common.v1.PoseInFrameR\x0bdestination\x12C\n\x0ecomponent_name\x18\x03 \x01(\x0b2\x1c.viam.common.v1.ResourceNameR\rcomponentName\x12@\n\x0bworld_state\x18\x04 \x01(\x0b2\x1a.viam.common.v1.WorldStateH\x00R\nworldState\x88\x01\x01\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extraB\x0e\n\x0c_world_state"(\n\x0cMoveResponse\x12\x18\n\x07success\x18\x01 \x01(\x08R\x07success"\xb5\x02\n\x1aMoveSingleComponentRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12=\n\x0bdestination\x18\x02 \x01(\x0b2\x1b.viam.common.v1.PoseInFrameR\x0bdestination\x12C\n\x0ecomponent_name\x18\x03 \x01(\x0b2\x1c.viam.common.v1.ResourceNameR\rcomponentName\x12@\n\x0bworld_state\x18\x04 \x01(\x0b2\x1a.viam.common.v1.WorldStateH\x00R\nworldState\x88\x01\x01\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extraB\x0e\n\x0c_world_state"7\n\x1bMoveSingleComponentResponse\x12\x18\n\x07success\x18\x01 \x01(\x08R\x07success"\x99\x02\n\x0eGetPoseRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12C\n\x0ecomponent_name\x18\x02 \x01(\x0b2\x1c.viam.common.v1.ResourceNameR\rcomponentName\x12+\n\x11destination_frame\x18\x03 \x01(\tR\x10destinationFrame\x12R\n\x17supplemental_transforms\x18\x04 \x03(\x0b2\x19.viam.common.v1.TransformR\x16supplementalTransforms\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"B\n\x0fGetPoseResponse\x12/\n\x04pose\x18\x01 \x01(\x0b2\x1b.viam.common.v1.PoseInFrameR\x04pose2\xdc\x03\n\rMotionService\x12\x82\x01\n\x04Move\x12#.viam.service.motion.v1.MoveRequest\x1a$.viam.service.motion.v1.MoveResponse"/\x82\xd3\xe4\x93\x02)"\'/viam/api/v1/service/motion/{name}/move\x12\xb7\x01\n\x13MoveSingleComponent\x122.viam.service.motion.v1.MoveSingleComponentRequest\x1a3.viam.service.motion.v1.MoveSingleComponentResponse"7\x82\xd3\xe4\x93\x021"//viam/api/v1/service/motion/movesinglecomponent\x12\x8b\x01\n\x07GetPose\x12&.viam.service.motion.v1.GetPoseRequest\x1a\'.viam.service.motion.v1.GetPoseResponse"/\x82\xd3\xe4\x93\x02)\x12\'/viam/api/v1/service/motion/{name}/poseB?\n\x1acom.viam.service.motion.v1Z!go.viam.com/api/service/motion/v1b\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'service.motion.v1.motion_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n\x1acom.viam.service.motion.v1Z!go.viam.com/api/service/motion/v1'
    _MOTIONSERVICE.methods_by_name['Move']._options = None
    _MOTIONSERVICE.methods_by_name['Move']._serialized_options = b'\x82\xd3\xe4\x93\x02)"\'/viam/api/v1/service/motion/{name}/move'
    _MOTIONSERVICE.methods_by_name['MoveSingleComponent']._options = None
    _MOTIONSERVICE.methods_by_name['MoveSingleComponent']._serialized_options = b'\x82\xd3\xe4\x93\x021"//viam/api/v1/service/motion/movesinglecomponent'
    _MOTIONSERVICE.methods_by_name['GetPose']._options = None
    _MOTIONSERVICE.methods_by_name['GetPose']._serialized_options = b"\x82\xd3\xe4\x93\x02)\x12'/viam/api/v1/service/motion/{name}/pose"
    _MOVEREQUEST._serialized_start = 143
    _MOVEREQUEST._serialized_end = 437
    _MOVERESPONSE._serialized_start = 439
    _MOVERESPONSE._serialized_end = 479
    _MOVESINGLECOMPONENTREQUEST._serialized_start = 482
    _MOVESINGLECOMPONENTREQUEST._serialized_end = 791
    _MOVESINGLECOMPONENTRESPONSE._serialized_start = 793
    _MOVESINGLECOMPONENTRESPONSE._serialized_end = 848
    _GETPOSEREQUEST._serialized_start = 851
    _GETPOSEREQUEST._serialized_end = 1132
    _GETPOSERESPONSE._serialized_start = 1134
    _GETPOSERESPONSE._serialized_end = 1200
    _MOTIONSERVICE._serialized_start = 1203
    _MOTIONSERVICE._serialized_end = 1679