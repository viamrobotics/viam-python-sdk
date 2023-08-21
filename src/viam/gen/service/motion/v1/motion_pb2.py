"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....common.v1 import common_pb2 as common_dot_v1_dot_common__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1eservice/motion/v1/motion.proto\x12\x16viam.service.motion.v1\x1a\x16common/v1/common.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1cgoogle/protobuf/struct.proto"\x82\x03\n\x0bMoveRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12=\n\x0bdestination\x18\x02 \x01(\x0b2\x1b.viam.common.v1.PoseInFrameR\x0bdestination\x12C\n\x0ecomponent_name\x18\x03 \x01(\x0b2\x1c.viam.common.v1.ResourceNameR\rcomponentName\x12@\n\x0bworld_state\x18\x04 \x01(\x0b2\x1a.viam.common.v1.WorldStateH\x00R\nworldState\x88\x01\x01\x12J\n\x0bconstraints\x18\x05 \x01(\x0b2#.viam.service.motion.v1.ConstraintsH\x01R\x0bconstraints\x88\x01\x01\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extraB\x0e\n\x0c_world_stateB\x0e\n\x0c_constraints"(\n\x0cMoveResponse\x12\x18\n\x07success\x18\x01 \x01(\x08R\x07success"\x9c\x02\n\x10MoveOnMapRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x126\n\x0bdestination\x18\x02 \x01(\x0b2\x14.viam.common.v1.PoseR\x0bdestination\x12C\n\x0ecomponent_name\x18\x03 \x01(\x0b2\x1c.viam.common.v1.ResourceNameR\rcomponentName\x12H\n\x11slam_service_name\x18\x04 \x01(\x0b2\x1c.viam.common.v1.ResourceNameR\x0fslamServiceName\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"-\n\x11MoveOnMapResponse\x12\x18\n\x07success\x18\x01 \x01(\x08R\x07success"\x86\x04\n\x13MotionConfiguration\x12E\n\x0fvision_services\x18\x01 \x03(\x0b2\x1c.viam.common.v1.ResourceNameR\x0evisionServices\x12F\n\x1dposition_polling_frequency_hz\x18\x02 \x01(\x01H\x00R\x1apositionPollingFrequencyHz\x88\x01\x01\x12F\n\x1dobstacle_polling_frequency_hz\x18\x03 \x01(\x01H\x01R\x1aobstaclePollingFrequencyHz\x88\x01\x01\x12-\n\x10plan_deviation_m\x18\x04 \x01(\x01H\x02R\x0eplanDeviationM\x88\x01\x01\x12,\n\x10linear_m_per_sec\x18\x05 \x01(\x01H\x03R\rlinearMPerSec\x88\x01\x01\x124\n\x14angular_degs_per_sec\x18\x06 \x01(\x01H\x04R\x11angularDegsPerSec\x88\x01\x01B \n\x1e_position_polling_frequency_hzB \n\x1e_obstacle_polling_frequency_hzB\x13\n\x11_plan_deviation_mB\x13\n\x11_linear_m_per_secB\x17\n\x15_angular_degs_per_sec"\x8c\x04\n\x12MoveOnGlobeRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12:\n\x0bdestination\x18\x02 \x01(\x0b2\x18.viam.common.v1.GeoPointR\x0bdestination\x12\x1d\n\x07heading\x18\x03 \x01(\x01H\x00R\x07heading\x88\x01\x01\x12C\n\x0ecomponent_name\x18\x04 \x01(\x0b2\x1c.viam.common.v1.ResourceNameR\rcomponentName\x12N\n\x14movement_sensor_name\x18\x05 \x01(\x0b2\x1c.viam.common.v1.ResourceNameR\x12movementSensorName\x129\n\tobstacles\x18\x06 \x03(\x0b2\x1b.viam.common.v1.GeoObstacleR\tobstacles\x12c\n\x14motion_configuration\x18\x07 \x01(\x0b2+.viam.service.motion.v1.MotionConfigurationH\x01R\x13motionConfiguration\x88\x01\x01\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extraB\n\n\x08_headingB\x17\n\x15_motion_configuration"/\n\x13MoveOnGlobeResponse\x12\x18\n\x07success\x18\x01 \x01(\x08R\x07success"\x99\x02\n\x0eGetPoseRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12C\n\x0ecomponent_name\x18\x02 \x01(\x0b2\x1c.viam.common.v1.ResourceNameR\rcomponentName\x12+\n\x11destination_frame\x18\x03 \x01(\tR\x10destinationFrame\x12R\n\x17supplemental_transforms\x18\x04 \x03(\x0b2\x19.viam.common.v1.TransformR\x16supplementalTransforms\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"B\n\x0fGetPoseResponse\x12/\n\x04pose\x18\x01 \x01(\x0b2\x1b.viam.common.v1.PoseInFrameR\x04pose"\xb3\x02\n\x0bConstraints\x12U\n\x11linear_constraint\x18\x01 \x03(\x0b2(.viam.service.motion.v1.LinearConstraintR\x10linearConstraint\x12d\n\x16orientation_constraint\x18\x02 \x03(\x0b2-.viam.service.motion.v1.OrientationConstraintR\x15orientationConstraint\x12g\n\x17collision_specification\x18\x03 \x03(\x0b2..viam.service.motion.v1.CollisionSpecificationR\x16collisionSpecification"\xbb\x01\n\x10LinearConstraint\x12/\n\x11line_tolerance_mm\x18\x01 \x01(\x02H\x00R\x0flineToleranceMm\x88\x01\x01\x12A\n\x1aorientation_tolerance_degs\x18\x02 \x01(\x02H\x01R\x18orientationToleranceDegs\x88\x01\x01B\x14\n\x12_line_tolerance_mmB\x1d\n\x1b_orientation_tolerance_degs"y\n\x15OrientationConstraint\x12A\n\x1aorientation_tolerance_degs\x18\x01 \x01(\x02H\x00R\x18orientationToleranceDegs\x88\x01\x01B\x1d\n\x1b_orientation_tolerance_degs"\xc1\x01\n\x16CollisionSpecification\x12]\n\x06allows\x18\x01 \x03(\x0b2E.viam.service.motion.v1.CollisionSpecification.AllowedFrameCollisionsR\x06allows\x1aH\n\x16AllowedFrameCollisions\x12\x16\n\x06frame1\x18\x01 \x01(\tR\x06frame1\x12\x16\n\x06frame2\x18\x02 \x01(\tR\x06frame22\xea\x05\n\rMotionService\x12\x82\x01\n\x04Move\x12#.viam.service.motion.v1.MoveRequest\x1a$.viam.service.motion.v1.MoveResponse"/\x82\xd3\xe4\x93\x02)"\'/viam/api/v1/service/motion/{name}/move\x12\x98\x01\n\tMoveOnMap\x12(.viam.service.motion.v1.MoveOnMapRequest\x1a).viam.service.motion.v1.MoveOnMapResponse"6\x82\xd3\xe4\x93\x020"./viam/api/v1/service/motion/{name}/move_on_map\x12\xa0\x01\n\x0bMoveOnGlobe\x12*.viam.service.motion.v1.MoveOnGlobeRequest\x1a+.viam.service.motion.v1.MoveOnGlobeResponse"8\x82\xd3\xe4\x93\x022"0/viam/api/v1/service/motion/{name}/move_on_globe\x12\x8b\x01\n\x07GetPose\x12&.viam.service.motion.v1.GetPoseRequest\x1a\'.viam.service.motion.v1.GetPoseResponse"/\x82\xd3\xe4\x93\x02)\x12\'/viam/api/v1/service/motion/{name}/pose\x12\x87\x01\n\tDoCommand\x12 .viam.common.v1.DoCommandRequest\x1a!.viam.common.v1.DoCommandResponse"5\x82\xd3\xe4\x93\x02/"-/viam/api/v1/service/motion/{name}/do_commandB?\n\x1acom.viam.service.motion.v1Z!go.viam.com/api/service/motion/v1b\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'service.motion.v1.motion_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n\x1acom.viam.service.motion.v1Z!go.viam.com/api/service/motion/v1'
    _MOTIONSERVICE.methods_by_name['Move']._options = None
    _MOTIONSERVICE.methods_by_name['Move']._serialized_options = b'\x82\xd3\xe4\x93\x02)"\'/viam/api/v1/service/motion/{name}/move'
    _MOTIONSERVICE.methods_by_name['MoveOnMap']._options = None
    _MOTIONSERVICE.methods_by_name['MoveOnMap']._serialized_options = b'\x82\xd3\xe4\x93\x020"./viam/api/v1/service/motion/{name}/move_on_map'
    _MOTIONSERVICE.methods_by_name['MoveOnGlobe']._options = None
    _MOTIONSERVICE.methods_by_name['MoveOnGlobe']._serialized_options = b'\x82\xd3\xe4\x93\x022"0/viam/api/v1/service/motion/{name}/move_on_globe'
    _MOTIONSERVICE.methods_by_name['GetPose']._options = None
    _MOTIONSERVICE.methods_by_name['GetPose']._serialized_options = b"\x82\xd3\xe4\x93\x02)\x12'/viam/api/v1/service/motion/{name}/pose"
    _MOTIONSERVICE.methods_by_name['DoCommand']._options = None
    _MOTIONSERVICE.methods_by_name['DoCommand']._serialized_options = b'\x82\xd3\xe4\x93\x02/"-/viam/api/v1/service/motion/{name}/do_command'
    _MOVEREQUEST._serialized_start = 143
    _MOVEREQUEST._serialized_end = 529
    _MOVERESPONSE._serialized_start = 531
    _MOVERESPONSE._serialized_end = 571
    _MOVEONMAPREQUEST._serialized_start = 574
    _MOVEONMAPREQUEST._serialized_end = 858
    _MOVEONMAPRESPONSE._serialized_start = 860
    _MOVEONMAPRESPONSE._serialized_end = 905
    _MOTIONCONFIGURATION._serialized_start = 908
    _MOTIONCONFIGURATION._serialized_end = 1426
    _MOVEONGLOBEREQUEST._serialized_start = 1429
    _MOVEONGLOBEREQUEST._serialized_end = 1953
    _MOVEONGLOBERESPONSE._serialized_start = 1955
    _MOVEONGLOBERESPONSE._serialized_end = 2002
    _GETPOSEREQUEST._serialized_start = 2005
    _GETPOSEREQUEST._serialized_end = 2286
    _GETPOSERESPONSE._serialized_start = 2288
    _GETPOSERESPONSE._serialized_end = 2354
    _CONSTRAINTS._serialized_start = 2357
    _CONSTRAINTS._serialized_end = 2664
    _LINEARCONSTRAINT._serialized_start = 2667
    _LINEARCONSTRAINT._serialized_end = 2854
    _ORIENTATIONCONSTRAINT._serialized_start = 2856
    _ORIENTATIONCONSTRAINT._serialized_end = 2977
    _COLLISIONSPECIFICATION._serialized_start = 2980
    _COLLISIONSPECIFICATION._serialized_end = 3173
    _COLLISIONSPECIFICATION_ALLOWEDFRAMECOLLISIONS._serialized_start = 3101
    _COLLISIONSPECIFICATION_ALLOWEDFRAMECOLLISIONS._serialized_end = 3173
    _MOTIONSERVICE._serialized_start = 3176
    _MOTIONSERVICE._serialized_end = 3922