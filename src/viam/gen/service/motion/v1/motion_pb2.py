"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....common.v1 import common_pb2 as common_dot_v1_dot_common__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1eservice/motion/v1/motion.proto\x12\x16viam.service.motion.v1\x1a\x16common/v1/common.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\x82\x03\n\x0bMoveRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12=\n\x0bdestination\x18\x02 \x01(\x0b2\x1b.viam.common.v1.PoseInFrameR\x0bdestination\x12C\n\x0ecomponent_name\x18\x03 \x01(\x0b2\x1c.viam.common.v1.ResourceNameR\rcomponentName\x12@\n\x0bworld_state\x18\x04 \x01(\x0b2\x1a.viam.common.v1.WorldStateH\x00R\nworldState\x88\x01\x01\x12J\n\x0bconstraints\x18\x05 \x01(\x0b2#.viam.service.motion.v1.ConstraintsH\x01R\x0bconstraints\x88\x01\x01\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extraB\x0e\n\x0c_world_stateB\x0e\n\x0c_constraints"(\n\x0cMoveResponse\x12\x18\n\x07success\x18\x01 \x01(\x08R\x07success"\xd2\x03\n\x10MoveOnMapRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x126\n\x0bdestination\x18\x02 \x01(\x0b2\x14.viam.common.v1.PoseR\x0bdestination\x12C\n\x0ecomponent_name\x18\x03 \x01(\x0b2\x1c.viam.common.v1.ResourceNameR\rcomponentName\x12H\n\x11slam_service_name\x18\x04 \x01(\x0b2\x1c.viam.common.v1.ResourceNameR\x0fslamServiceName\x12c\n\x14motion_configuration\x18\x05 \x01(\x0b2+.viam.service.motion.v1.MotionConfigurationH\x00R\x13motionConfiguration\x88\x01\x01\x126\n\tobstacles\x18\x06 \x03(\x0b2\x18.viam.common.v1.GeometryR\tobstacles\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extraB\x17\n\x15_motion_configuration"6\n\x11MoveOnMapResponse\x12!\n\x0cexecution_id\x18\x01 \x01(\tR\x0bexecutionId"\x8d\x01\n\x10ObstacleDetector\x12C\n\x0evision_service\x18\x01 \x01(\x0b2\x1c.viam.common.v1.ResourceNameR\rvisionService\x124\n\x06camera\x18\x02 \x01(\x0b2\x1c.viam.common.v1.ResourceNameR\x06camera"\x98\x04\n\x13MotionConfiguration\x12W\n\x12obstacle_detectors\x18\x01 \x03(\x0b2(.viam.service.motion.v1.ObstacleDetectorR\x11obstacleDetectors\x12F\n\x1dposition_polling_frequency_hz\x18\x02 \x01(\x01H\x00R\x1apositionPollingFrequencyHz\x88\x01\x01\x12F\n\x1dobstacle_polling_frequency_hz\x18\x03 \x01(\x01H\x01R\x1aobstaclePollingFrequencyHz\x88\x01\x01\x12-\n\x10plan_deviation_m\x18\x04 \x01(\x01H\x02R\x0eplanDeviationM\x88\x01\x01\x12,\n\x10linear_m_per_sec\x18\x05 \x01(\x01H\x03R\rlinearMPerSec\x88\x01\x01\x124\n\x14angular_degs_per_sec\x18\x06 \x01(\x01H\x04R\x11angularDegsPerSec\x88\x01\x01B \n\x1e_position_polling_frequency_hzB \n\x1e_obstacle_polling_frequency_hzB\x13\n\x11_plan_deviation_mB\x13\n\x11_linear_m_per_secB\x17\n\x15_angular_degs_per_sec"\xd4\x04\n\x12MoveOnGlobeRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12:\n\x0bdestination\x18\x02 \x01(\x0b2\x18.viam.common.v1.GeoPointR\x0bdestination\x12\x1d\n\x07heading\x18\x03 \x01(\x01H\x00R\x07heading\x88\x01\x01\x12C\n\x0ecomponent_name\x18\x04 \x01(\x0b2\x1c.viam.common.v1.ResourceNameR\rcomponentName\x12N\n\x14movement_sensor_name\x18\x05 \x01(\x0b2\x1c.viam.common.v1.ResourceNameR\x12movementSensorName\x129\n\tobstacles\x18\x06 \x03(\x0b2\x1b.viam.common.v1.GeoGeometryR\tobstacles\x12c\n\x14motion_configuration\x18\x07 \x01(\x0b2+.viam.service.motion.v1.MotionConfigurationH\x01R\x13motionConfiguration\x88\x01\x01\x12F\n\x10bounding_regions\x18\x08 \x03(\x0b2\x1b.viam.common.v1.GeoGeometryR\x0fboundingRegions\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extraB\n\n\x08_headingB\x17\n\x15_motion_configuration"8\n\x13MoveOnGlobeResponse\x12!\n\x0cexecution_id\x18\x01 \x01(\tR\x0bexecutionId"\x99\x02\n\x0eGetPoseRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12C\n\x0ecomponent_name\x18\x02 \x01(\x0b2\x1c.viam.common.v1.ResourceNameR\rcomponentName\x12+\n\x11destination_frame\x18\x03 \x01(\tR\x10destinationFrame\x12R\n\x17supplemental_transforms\x18\x04 \x03(\x0b2\x19.viam.common.v1.TransformR\x16supplementalTransforms\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"B\n\x0fGetPoseResponse\x12/\n\x04pose\x18\x01 \x01(\x0b2\x1b.viam.common.v1.PoseInFrameR\x04pose"\x99\x01\n\x0fStopPlanRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12C\n\x0ecomponent_name\x18\x02 \x01(\x0b2\x1c.viam.common.v1.ResourceNameR\rcomponentName\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"\x12\n\x10StopPlanResponse"\x88\x01\n\x17ListPlanStatusesRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12*\n\x11only_active_plans\x18\x02 \x01(\x08R\x0fonlyActivePlans\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"y\n\x18ListPlanStatusesResponse\x12]\n\x16plan_statuses_with_ids\x18\x01 \x03(\x0b2(.viam.service.motion.v1.PlanStatusWithIDR\x13planStatusesWithIds"\xf7\x01\n\x0eGetPlanRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12C\n\x0ecomponent_name\x18\x02 \x01(\x0b2\x1c.viam.common.v1.ResourceNameR\rcomponentName\x12$\n\x0elast_plan_only\x18\x03 \x01(\x08R\x0clastPlanOnly\x12&\n\x0cexecution_id\x18\x04 \x01(\tH\x00R\x0bexecutionId\x88\x01\x01\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extraB\x0f\n\r_execution_id"\xc1\x01\n\x0fGetPlanResponse\x12_\n\x18current_plan_with_status\x18\x01 \x01(\x0b2&.viam.service.motion.v1.PlanWithStatusR\x15currentPlanWithStatus\x12M\n\x0ereplan_history\x18\x02 \x03(\x0b2&.viam.service.motion.v1.PlanWithStatusR\rreplanHistory"\xb3\x02\n\x0bConstraints\x12U\n\x11linear_constraint\x18\x01 \x03(\x0b2(.viam.service.motion.v1.LinearConstraintR\x10linearConstraint\x12d\n\x16orientation_constraint\x18\x02 \x03(\x0b2-.viam.service.motion.v1.OrientationConstraintR\x15orientationConstraint\x12g\n\x17collision_specification\x18\x03 \x03(\x0b2..viam.service.motion.v1.CollisionSpecificationR\x16collisionSpecification"\xbb\x01\n\x10LinearConstraint\x12/\n\x11line_tolerance_mm\x18\x01 \x01(\x02H\x00R\x0flineToleranceMm\x88\x01\x01\x12A\n\x1aorientation_tolerance_degs\x18\x02 \x01(\x02H\x01R\x18orientationToleranceDegs\x88\x01\x01B\x14\n\x12_line_tolerance_mmB\x1d\n\x1b_orientation_tolerance_degs"y\n\x15OrientationConstraint\x12A\n\x1aorientation_tolerance_degs\x18\x01 \x01(\x02H\x00R\x18orientationToleranceDegs\x88\x01\x01B\x1d\n\x1b_orientation_tolerance_degs"\xc1\x01\n\x16CollisionSpecification\x12]\n\x06allows\x18\x01 \x03(\x0b2E.viam.service.motion.v1.CollisionSpecification.AllowedFrameCollisionsR\x06allows\x1aH\n\x16AllowedFrameCollisions\x12\x16\n\x06frame1\x18\x01 \x01(\tR\x06frame1\x12\x16\n\x06frame2\x18\x02 \x01(\tR\x06frame2"\xc9\x01\n\x0ePlanWithStatus\x120\n\x04plan\x18\x01 \x01(\x0b2\x1c.viam.service.motion.v1.PlanR\x04plan\x12:\n\x06status\x18\x02 \x01(\x0b2".viam.service.motion.v1.PlanStatusR\x06status\x12I\n\x0estatus_history\x18\x03 \x03(\x0b2".viam.service.motion.v1.PlanStatusR\rstatusHistory"\xcf\x01\n\x10PlanStatusWithID\x12\x17\n\x07plan_id\x18\x01 \x01(\tR\x06planId\x12C\n\x0ecomponent_name\x18\x02 \x01(\x0b2\x1c.viam.common.v1.ResourceNameR\rcomponentName\x12!\n\x0cexecution_id\x18\x03 \x01(\tR\x0bexecutionId\x12:\n\x06status\x18\x04 \x01(\x0b2".viam.service.motion.v1.PlanStatusR\x06status"\xa7\x01\n\nPlanStatus\x127\n\x05state\x18\x01 \x01(\x0e2!.viam.service.motion.v1.PlanStateR\x05state\x128\n\ttimestamp\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampR\ttimestamp\x12\x1b\n\x06reason\x18\x03 \x01(\tH\x00R\x06reason\x88\x01\x01B\t\n\x07_reason"\xb6\x01\n\x04Plan\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12C\n\x0ecomponent_name\x18\x02 \x01(\x0b2\x1c.viam.common.v1.ResourceNameR\rcomponentName\x12!\n\x0cexecution_id\x18\x03 \x01(\tR\x0bexecutionId\x126\n\x05steps\x18\x04 \x03(\x0b2 .viam.service.motion.v1.PlanStepR\x05steps"\xab\x01\n\x08PlanStep\x12>\n\x04step\x18\x01 \x03(\x0b2*.viam.service.motion.v1.PlanStep.StepEntryR\x04step\x1a_\n\tStepEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12<\n\x05value\x18\x02 \x01(\x0b2&.viam.service.motion.v1.ComponentStateR\x05value:\x028\x01":\n\x0eComponentState\x12(\n\x04pose\x18\x01 \x01(\x0b2\x14.viam.common.v1.PoseR\x04pose*\x8c\x01\n\tPlanState\x12\x1a\n\x16PLAN_STATE_UNSPECIFIED\x10\x00\x12\x1a\n\x16PLAN_STATE_IN_PROGRESS\x10\x01\x12\x16\n\x12PLAN_STATE_STOPPED\x10\x02\x12\x18\n\x14PLAN_STATE_SUCCEEDED\x10\x03\x12\x15\n\x11PLAN_STATE_FAILED\x10\x042\xc9\t\n\rMotionService\x12\x82\x01\n\x04Move\x12#.viam.service.motion.v1.MoveRequest\x1a$.viam.service.motion.v1.MoveResponse"/\x82\xd3\xe4\x93\x02)"\'/viam/api/v1/service/motion/{name}/move\x12\x98\x01\n\tMoveOnMap\x12(.viam.service.motion.v1.MoveOnMapRequest\x1a).viam.service.motion.v1.MoveOnMapResponse"6\x82\xd3\xe4\x93\x020"./viam/api/v1/service/motion/{name}/move_on_map\x12\xa0\x01\n\x0bMoveOnGlobe\x12*.viam.service.motion.v1.MoveOnGlobeRequest\x1a+.viam.service.motion.v1.MoveOnGlobeResponse"8\x82\xd3\xe4\x93\x022"0/viam/api/v1/service/motion/{name}/move_on_globe\x12\x8b\x01\n\x07GetPose\x12&.viam.service.motion.v1.GetPoseRequest\x1a\'.viam.service.motion.v1.GetPoseResponse"/\x82\xd3\xe4\x93\x02)\x12\'/viam/api/v1/service/motion/{name}/pose\x12\x93\x01\n\x08StopPlan\x12\'.viam.service.motion.v1.StopPlanRequest\x1a(.viam.service.motion.v1.StopPlanResponse"4\x82\xd3\xe4\x93\x02.\x1a,/viam/api/v1/service/motion/{name}/stop_plan\x12\xb4\x01\n\x10ListPlanStatuses\x12/.viam.service.motion.v1.ListPlanStatusesRequest\x1a0.viam.service.motion.v1.ListPlanStatusesResponse"=\x82\xd3\xe4\x93\x027\x125/viam/api/v1/service/motion/{name}/list_plan_statuses\x12\x8f\x01\n\x07GetPlan\x12&.viam.service.motion.v1.GetPlanRequest\x1a\'.viam.service.motion.v1.GetPlanResponse"3\x82\xd3\xe4\x93\x02-\x12+/viam/api/v1/service/motion/{name}/get_plan\x12\x87\x01\n\tDoCommand\x12 .viam.common.v1.DoCommandRequest\x1a!.viam.common.v1.DoCommandResponse"5\x82\xd3\xe4\x93\x02/"-/viam/api/v1/service/motion/{name}/do_commandB?\n\x1acom.viam.service.motion.v1Z!go.viam.com/api/service/motion/v1b\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'service.motion.v1.motion_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n\x1acom.viam.service.motion.v1Z!go.viam.com/api/service/motion/v1'
    _PLANSTEP_STEPENTRY._options = None
    _PLANSTEP_STEPENTRY._serialized_options = b'8\x01'
    _MOTIONSERVICE.methods_by_name['Move']._options = None
    _MOTIONSERVICE.methods_by_name['Move']._serialized_options = b'\x82\xd3\xe4\x93\x02)"\'/viam/api/v1/service/motion/{name}/move'
    _MOTIONSERVICE.methods_by_name['MoveOnMap']._options = None
    _MOTIONSERVICE.methods_by_name['MoveOnMap']._serialized_options = b'\x82\xd3\xe4\x93\x020"./viam/api/v1/service/motion/{name}/move_on_map'
    _MOTIONSERVICE.methods_by_name['MoveOnGlobe']._options = None
    _MOTIONSERVICE.methods_by_name['MoveOnGlobe']._serialized_options = b'\x82\xd3\xe4\x93\x022"0/viam/api/v1/service/motion/{name}/move_on_globe'
    _MOTIONSERVICE.methods_by_name['GetPose']._options = None
    _MOTIONSERVICE.methods_by_name['GetPose']._serialized_options = b"\x82\xd3\xe4\x93\x02)\x12'/viam/api/v1/service/motion/{name}/pose"
    _MOTIONSERVICE.methods_by_name['StopPlan']._options = None
    _MOTIONSERVICE.methods_by_name['StopPlan']._serialized_options = b'\x82\xd3\xe4\x93\x02.\x1a,/viam/api/v1/service/motion/{name}/stop_plan'
    _MOTIONSERVICE.methods_by_name['ListPlanStatuses']._options = None
    _MOTIONSERVICE.methods_by_name['ListPlanStatuses']._serialized_options = b'\x82\xd3\xe4\x93\x027\x125/viam/api/v1/service/motion/{name}/list_plan_statuses'
    _MOTIONSERVICE.methods_by_name['GetPlan']._options = None
    _MOTIONSERVICE.methods_by_name['GetPlan']._serialized_options = b'\x82\xd3\xe4\x93\x02-\x12+/viam/api/v1/service/motion/{name}/get_plan'
    _MOTIONSERVICE.methods_by_name['DoCommand']._options = None
    _MOTIONSERVICE.methods_by_name['DoCommand']._serialized_options = b'\x82\xd3\xe4\x93\x02/"-/viam/api/v1/service/motion/{name}/do_command'
    _PLANSTATE._serialized_start = 5530
    _PLANSTATE._serialized_end = 5670
    _MOVEREQUEST._serialized_start = 176
    _MOVEREQUEST._serialized_end = 562
    _MOVERESPONSE._serialized_start = 564
    _MOVERESPONSE._serialized_end = 604
    _MOVEONMAPREQUEST._serialized_start = 607
    _MOVEONMAPREQUEST._serialized_end = 1073
    _MOVEONMAPRESPONSE._serialized_start = 1075
    _MOVEONMAPRESPONSE._serialized_end = 1129
    _OBSTACLEDETECTOR._serialized_start = 1132
    _OBSTACLEDETECTOR._serialized_end = 1273
    _MOTIONCONFIGURATION._serialized_start = 1276
    _MOTIONCONFIGURATION._serialized_end = 1812
    _MOVEONGLOBEREQUEST._serialized_start = 1815
    _MOVEONGLOBEREQUEST._serialized_end = 2411
    _MOVEONGLOBERESPONSE._serialized_start = 2413
    _MOVEONGLOBERESPONSE._serialized_end = 2469
    _GETPOSEREQUEST._serialized_start = 2472
    _GETPOSEREQUEST._serialized_end = 2753
    _GETPOSERESPONSE._serialized_start = 2755
    _GETPOSERESPONSE._serialized_end = 2821
    _STOPPLANREQUEST._serialized_start = 2824
    _STOPPLANREQUEST._serialized_end = 2977
    _STOPPLANRESPONSE._serialized_start = 2979
    _STOPPLANRESPONSE._serialized_end = 2997
    _LISTPLANSTATUSESREQUEST._serialized_start = 3000
    _LISTPLANSTATUSESREQUEST._serialized_end = 3136
    _LISTPLANSTATUSESRESPONSE._serialized_start = 3138
    _LISTPLANSTATUSESRESPONSE._serialized_end = 3259
    _GETPLANREQUEST._serialized_start = 3262
    _GETPLANREQUEST._serialized_end = 3509
    _GETPLANRESPONSE._serialized_start = 3512
    _GETPLANRESPONSE._serialized_end = 3705
    _CONSTRAINTS._serialized_start = 3708
    _CONSTRAINTS._serialized_end = 4015
    _LINEARCONSTRAINT._serialized_start = 4018
    _LINEARCONSTRAINT._serialized_end = 4205
    _ORIENTATIONCONSTRAINT._serialized_start = 4207
    _ORIENTATIONCONSTRAINT._serialized_end = 4328
    _COLLISIONSPECIFICATION._serialized_start = 4331
    _COLLISIONSPECIFICATION._serialized_end = 4524
    _COLLISIONSPECIFICATION_ALLOWEDFRAMECOLLISIONS._serialized_start = 4452
    _COLLISIONSPECIFICATION_ALLOWEDFRAMECOLLISIONS._serialized_end = 4524
    _PLANWITHSTATUS._serialized_start = 4527
    _PLANWITHSTATUS._serialized_end = 4728
    _PLANSTATUSWITHID._serialized_start = 4731
    _PLANSTATUSWITHID._serialized_end = 4938
    _PLANSTATUS._serialized_start = 4941
    _PLANSTATUS._serialized_end = 5108
    _PLAN._serialized_start = 5111
    _PLAN._serialized_end = 5293
    _PLANSTEP._serialized_start = 5296
    _PLANSTEP._serialized_end = 5467
    _PLANSTEP_STEPENTRY._serialized_start = 5372
    _PLANSTEP_STEPENTRY._serialized_end = 5467
    _COMPONENTSTATE._serialized_start = 5469
    _COMPONENTSTATE._serialized_end = 5527
    _MOTIONSERVICE._serialized_start = 5673
    _MOTIONSERVICE._serialized_end = 6898