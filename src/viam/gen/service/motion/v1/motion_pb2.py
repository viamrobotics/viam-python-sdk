"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....common.v1 import common_pb2 as common_dot_v1_dot_common__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1eservice/motion/v1/motion.proto\x12\x16viam.service.motion.v1\x1a\x16common/v1/common.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1cgoogle/protobuf/struct.proto"\xe7\x03\n\x0bMoveRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12=\n\x0bdestination\x18\x02 \x01(\x0b2\x1b.viam.common.v1.PoseInFrameR\x0bdestination\x12C\n\x0ecomponent_name\x18\x03 \x01(\x0b2\x1c.viam.common.v1.ResourceNameR\rcomponentName\x12@\n\x0bworld_state\x18\x04 \x01(\x0b2\x1a.viam.common.v1.WorldStateH\x00R\nworldState\x88\x01\x01\x12J\n\x0bconstraints\x18\x05 \x01(\x0b2#.viam.service.motion.v1.ConstraintsH\x01R\x0bconstraints\x88\x01\x01\x12M\n\x11slam_service_name\x18\x06 \x01(\x0b2\x1c.viam.common.v1.ResourceNameH\x02R\x0fslamServiceName\x88\x01\x01\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extraB\x0e\n\x0c_world_stateB\x0e\n\x0c_constraintsB\x14\n\x12_slam_service_name"(\n\x0cMoveResponse\x12\x18\n\x07success\x18\x01 \x01(\x08R\x07success"\xb5\x02\n\x1aMoveSingleComponentRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12=\n\x0bdestination\x18\x02 \x01(\x0b2\x1b.viam.common.v1.PoseInFrameR\x0bdestination\x12C\n\x0ecomponent_name\x18\x03 \x01(\x0b2\x1c.viam.common.v1.ResourceNameR\rcomponentName\x12@\n\x0bworld_state\x18\x04 \x01(\x0b2\x1a.viam.common.v1.WorldStateH\x00R\nworldState\x88\x01\x01\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extraB\x0e\n\x0c_world_state"7\n\x1bMoveSingleComponentResponse\x12\x18\n\x07success\x18\x01 \x01(\x08R\x07success"\x99\x02\n\x0eGetPoseRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12C\n\x0ecomponent_name\x18\x02 \x01(\x0b2\x1c.viam.common.v1.ResourceNameR\rcomponentName\x12+\n\x11destination_frame\x18\x03 \x01(\tR\x10destinationFrame\x12R\n\x17supplemental_transforms\x18\x04 \x03(\x0b2\x19.viam.common.v1.TransformR\x16supplementalTransforms\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"B\n\x0fGetPoseResponse\x12/\n\x04pose\x18\x01 \x01(\x0b2\x1b.viam.common.v1.PoseInFrameR\x04pose"\xb3\x02\n\x0bConstraints\x12U\n\x11linear_constraint\x18\x01 \x03(\x0b2(.viam.service.motion.v1.LinearConstraintR\x10linearConstraint\x12d\n\x16orientation_constraint\x18\x02 \x03(\x0b2-.viam.service.motion.v1.OrientationConstraintR\x15orientationConstraint\x12g\n\x17collision_specification\x18\x03 \x03(\x0b2..viam.service.motion.v1.CollisionSpecificationR\x16collisionSpecification"\xbb\x01\n\x10LinearConstraint\x12/\n\x11line_tolerance_mm\x18\x01 \x01(\x02H\x00R\x0flineToleranceMm\x88\x01\x01\x12A\n\x1aorientation_tolerance_degs\x18\x02 \x01(\x02H\x01R\x18orientationToleranceDegs\x88\x01\x01B\x14\n\x12_line_tolerance_mmB\x1d\n\x1b_orientation_tolerance_degs"y\n\x15OrientationConstraint\x12A\n\x1aorientation_tolerance_degs\x18\x01 \x01(\x02H\x00R\x18orientationToleranceDegs\x88\x01\x01B\x1d\n\x1b_orientation_tolerance_degs"\xc1\x01\n\x16CollisionSpecification\x12]\n\x06allows\x18\x01 \x03(\x0b2E.viam.service.motion.v1.CollisionSpecification.AllowedFrameCollisionsR\x06allows\x1aH\n\x16AllowedFrameCollisions\x12\x16\n\x06frame1\x18\x01 \x01(\tR\x06frame1\x12\x16\n\x06frame2\x18\x02 \x01(\tR\x06frame22\xef\x04\n\rMotionService\x12\x82\x01\n\x04Move\x12#.viam.service.motion.v1.MoveRequest\x1a$.viam.service.motion.v1.MoveResponse"/\x82\xd3\xe4\x93\x02)"\'/viam/api/v1/service/motion/{name}/move\x12\xc0\x01\n\x13MoveSingleComponent\x122.viam.service.motion.v1.MoveSingleComponentRequest\x1a3.viam.service.motion.v1.MoveSingleComponentResponse"@\x82\xd3\xe4\x93\x02:"8/viam/api/v1/service/motion/{name}/move_single_component\x12\x8b\x01\n\x07GetPose\x12&.viam.service.motion.v1.GetPoseRequest\x1a\'.viam.service.motion.v1.GetPoseResponse"/\x82\xd3\xe4\x93\x02)\x12\'/viam/api/v1/service/motion/{name}/pose\x12\x87\x01\n\tDoCommand\x12 .viam.common.v1.DoCommandRequest\x1a!.viam.common.v1.DoCommandResponse"5\x82\xd3\xe4\x93\x02/"-/viam/api/v1/service/motion/{name}/do_commandB?\n\x1acom.viam.service.motion.v1Z!go.viam.com/api/service/motion/v1b\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'service.motion.v1.motion_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n\x1acom.viam.service.motion.v1Z!go.viam.com/api/service/motion/v1'
    _MOTIONSERVICE.methods_by_name['Move']._options = None
    _MOTIONSERVICE.methods_by_name['Move']._serialized_options = b'\x82\xd3\xe4\x93\x02)"\'/viam/api/v1/service/motion/{name}/move'
    _MOTIONSERVICE.methods_by_name['MoveSingleComponent']._options = None
    _MOTIONSERVICE.methods_by_name['MoveSingleComponent']._serialized_options = b'\x82\xd3\xe4\x93\x02:"8/viam/api/v1/service/motion/{name}/move_single_component'
    _MOTIONSERVICE.methods_by_name['GetPose']._options = None
    _MOTIONSERVICE.methods_by_name['GetPose']._serialized_options = b"\x82\xd3\xe4\x93\x02)\x12'/viam/api/v1/service/motion/{name}/pose"
    _MOTIONSERVICE.methods_by_name['DoCommand']._options = None
    _MOTIONSERVICE.methods_by_name['DoCommand']._serialized_options = b'\x82\xd3\xe4\x93\x02/"-/viam/api/v1/service/motion/{name}/do_command'
    _MOVEREQUEST._serialized_start = 143
    _MOVEREQUEST._serialized_end = 630
    _MOVERESPONSE._serialized_start = 632
    _MOVERESPONSE._serialized_end = 672
    _MOVESINGLECOMPONENTREQUEST._serialized_start = 675
    _MOVESINGLECOMPONENTREQUEST._serialized_end = 984
    _MOVESINGLECOMPONENTRESPONSE._serialized_start = 986
    _MOVESINGLECOMPONENTRESPONSE._serialized_end = 1041
    _GETPOSEREQUEST._serialized_start = 1044
    _GETPOSEREQUEST._serialized_end = 1325
    _GETPOSERESPONSE._serialized_start = 1327
    _GETPOSERESPONSE._serialized_end = 1393
    _CONSTRAINTS._serialized_start = 1396
    _CONSTRAINTS._serialized_end = 1703
    _LINEARCONSTRAINT._serialized_start = 1706
    _LINEARCONSTRAINT._serialized_end = 1893
    _ORIENTATIONCONSTRAINT._serialized_start = 1895
    _ORIENTATIONCONSTRAINT._serialized_end = 2016
    _COLLISIONSPECIFICATION._serialized_start = 2019
    _COLLISIONSPECIFICATION._serialized_end = 2212
    _COLLISIONSPECIFICATION_ALLOWEDFRAMECOLLISIONS._serialized_start = 2140
    _COLLISIONSPECIFICATION_ALLOWEDFRAMECOLLISIONS._serialized_end = 2212
    _MOTIONSERVICE._serialized_start = 2215
    _MOTIONSERVICE._serialized_end = 2838