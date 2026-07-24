"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 6, 33, 5, '', 'component/arm/v1/arm.proto')
_sym_db = _symbol_database.Default()
from ....common.v1 import common_pb2 as common_dot_v1_dot_common__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1acomponent/arm/v1/arm.proto\x12\x15viam.component.arm.v1\x1a\x16common/v1/common.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1cgoogle/protobuf/struct.proto"Z\n\x15GetEndPositionRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"B\n\x16GetEndPositionResponse\x12(\n\x04pose\x18\x01 \x01(\x0b2\x14.viam.common.v1.PoseR\x04pose"(\n\x0eJointPositions\x12\x16\n\x06values\x18\x01 \x03(\x01R\x06values")\n\x0fJointVelocities\x12\x16\n\x06values\x18\x01 \x03(\x01R\x06values",\n\x12JointAccelerations\x12\x16\n\x06values\x18\x01 \x03(\x01R\x06values"]\n\x18GetJointPositionsRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"`\n\x19GetJointPositionsResponse\x12C\n\tpositions\x18\x01 \x01(\x0b2%.viam.component.arm.v1.JointPositionsR\tpositions"\x80\x01\n\x15MoveToPositionRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12$\n\x02to\x18\x02 \x01(\x0b2\x14.viam.common.v1.PoseR\x02to\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"\x18\n\x16MoveToPositionResponse"\xa5\x01\n\x1bMoveToJointPositionsRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12C\n\tpositions\x18\x02 \x01(\x0b2%.viam.component.arm.v1.JointPositionsR\tpositions\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"\x1e\n\x1cMoveToJointPositionsResponse"\xf9\x01\n MoveThroughJointPositionsRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12C\n\tpositions\x18\x02 \x03(\x0b2%.viam.component.arm.v1.JointPositionsR\tpositions\x12A\n\x07options\x18\x03 \x01(\x0b2".viam.component.arm.v1.MoveOptionsH\x00R\x07options\x88\x01\x01\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extraB\n\n\x08_options"#\n!MoveThroughJointPositionsResponse"\xc2\x03\n\x0fTrajectoryPoint\x12-\n\x04time\x18\x01 \x01(\x0b2\x19.google.protobuf.DurationR\x04time\x12C\n\tpositions\x18\x02 \x01(\x0b2%.viam.component.arm.v1.JointPositionsR\tpositions\x12b\n\x0bconstraints\x18\x03 \x01(\x0b2;.viam.component.arm.v1.TrajectoryPoint.KinematicConstraintsH\x00R\x0bconstraints\x88\x01\x01\x1a\xc6\x01\n\x14KinematicConstraints\x12F\n\nvelocities\x18\x01 \x01(\x0b2&.viam.component.arm.v1.JointVelocitiesR\nvelocities\x12T\n\raccelerations\x18\x02 \x01(\x0b2).viam.component.arm.v1.JointAccelerationsH\x00R\raccelerations\x88\x01\x01B\x10\n\x0e_accelerationsB\x0e\n\x0c_constraints"\x98\x03\n(MoveThroughJointPositionsStreamedRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12Z\n\x04init\x18\x02 \x01(\x0b2D.viam.component.arm.v1.MoveThroughJointPositionsStreamedRequest.InitH\x00R\x04init\x12g\n\x05batch\x18\x03 \x01(\x0b2O.viam.component.arm.v1.MoveThroughJointPositionsStreamedRequest.TrajectoryBatchH\x00R\x05batch\x1a5\n\x04Init\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra\x1aQ\n\x0fTrajectoryBatch\x12>\n\x06points\x18\x01 \x03(\x0b2&.viam.component.arm.v1.TrajectoryPointR\x06pointsB\t\n\x07message"\xd0\x01\n)MoveThroughJointPositionsStreamedResponse\x12]\n\x03ack\x18\x01 \x01(\x0b2I.viam.component.arm.v1.MoveThroughJointPositionsStreamedResponse.BatchAckH\x00R\x03ack\x1a9\n\x08BatchAck\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extraB\t\n\x07message"P\n\x0bStopRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"\x0e\n\x0cStopResponse"\xae\x01\n\x06Status\x127\n\x0cend_position\x18\x01 \x01(\x0b2\x14.viam.common.v1.PoseR\x0bendPosition\x12N\n\x0fjoint_positions\x18\x02 \x01(\x0b2%.viam.component.arm.v1.JointPositionsR\x0ejointPositions\x12\x1b\n\tis_moving\x18\x03 \x01(\x08R\x08isMoving"%\n\x0fIsMovingRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name"/\n\x10IsMovingResponse\x12\x1b\n\tis_moving\x18\x01 \x01(\x08R\x08isMoving"\xe3\x02\n\x0bMoveOptions\x123\n\x14max_vel_degs_per_sec\x18\x01 \x01(\x01H\x00R\x10maxVelDegsPerSec\x88\x01\x01\x125\n\x15max_acc_degs_per_sec2\x18\x02 \x01(\x01H\x01R\x11maxAccDegsPerSec2\x88\x01\x01\x12;\n\x1bmax_vel_degs_per_sec_joints\x18\x03 \x03(\x01R\x16maxVelDegsPerSecJoints\x12=\n\x1cmax_acc_degs_per_sec2_joints\x18\x04 \x03(\x01R\x17maxAccDegsPerSec2Joints\x12\'\n\rmax_tcp_speed\x18\x05 \x01(\x01H\x02R\x0bmaxTcpSpeed\x88\x01\x01B\x17\n\x15_max_vel_degs_per_secB\x18\n\x16_max_acc_degs_per_sec2B\x10\n\x0e_max_tcp_speed2\xbb\x10\n\nArmService\x12\xa1\x01\n\x0eGetEndPosition\x12,.viam.component.arm.v1.GetEndPositionRequest\x1a-.viam.component.arm.v1.GetEndPositionResponse"2\x82\xd3\xe4\x93\x02,\x12*/viam/api/v1/component/arm/{name}/position\x12\xa5\x01\n\x0eMoveToPosition\x12,.viam.component.arm.v1.MoveToPositionRequest\x1a-.viam.component.arm.v1.MoveToPositionResponse"6\xa0\x92)\x01\x82\xd3\xe4\x93\x02,\x1a*/viam/api/v1/component/arm/{name}/position\x12\xb1\x01\n\x11GetJointPositions\x12/.viam.component.arm.v1.GetJointPositionsRequest\x1a0.viam.component.arm.v1.GetJointPositionsResponse"9\x82\xd3\xe4\x93\x023\x121/viam/api/v1/component/arm/{name}/joint_positions\x12\xbe\x01\n\x14MoveToJointPositions\x122.viam.component.arm.v1.MoveToJointPositionsRequest\x1a3.viam.component.arm.v1.MoveToJointPositionsResponse"=\xa0\x92)\x01\x82\xd3\xe4\x93\x023\x1a1/viam/api/v1/component/arm/{name}/joint_positions\x12\xda\x01\n\x19MoveThroughJointPositions\x127.viam.component.arm.v1.MoveThroughJointPositionsRequest\x1a8.viam.component.arm.v1.MoveThroughJointPositionsResponse"J\xa0\x92)\x01\x82\xd3\xe4\x93\x02@">/viam/api/v1/component/arm/{name}/move_through_joint_positions\x12\xb0\x01\n!MoveThroughJointPositionsStreamed\x12?.viam.component.arm.v1.MoveThroughJointPositionsStreamedRequest\x1a@.viam.component.arm.v1.MoveThroughJointPositionsStreamedResponse"\x04\xa0\x92)\x01(\x010\x01\x12\x7f\n\x04Stop\x12".viam.component.arm.v1.StopRequest\x1a#.viam.component.arm.v1.StopResponse".\x82\xd3\xe4\x93\x02("&/viam/api/v1/component/arm/{name}/stop\x12\x90\x01\n\x08IsMoving\x12&.viam.component.arm.v1.IsMovingRequest\x1a\'.viam.component.arm.v1.IsMovingResponse"3\x82\xd3\xe4\x93\x02-\x12+/viam/api/v1/component/arm/{name}/is_moving\x12\x86\x01\n\tDoCommand\x12 .viam.common.v1.DoCommandRequest\x1a!.viam.common.v1.DoCommandResponse"4\x82\xd3\xe4\x93\x02.",/viam/api/v1/component/arm/{name}/do_command\x12\x86\x01\n\tGetStatus\x12 .viam.common.v1.GetStatusRequest\x1a!.viam.common.v1.GetStatusResponse"4\x82\xd3\xe4\x93\x02.\x12,/viam/api/v1/component/arm/{name}/get_status\x12\x92\x01\n\rGetKinematics\x12$.viam.common.v1.GetKinematicsRequest\x1a%.viam.common.v1.GetKinematicsResponse"4\x82\xd3\xe4\x93\x02.\x12,/viam/api/v1/component/arm/{name}/kinematics\x12\x92\x01\n\rGetGeometries\x12$.viam.common.v1.GetGeometriesRequest\x1a%.viam.common.v1.GetGeometriesResponse"4\x82\xd3\xe4\x93\x02.\x12,/viam/api/v1/component/arm/{name}/geometries\x12\x8b\x01\n\x0bGet3DModels\x12".viam.common.v1.Get3DModelsRequest\x1a#.viam.common.v1.Get3DModelsResponse"3\x82\xd3\xe4\x93\x02-\x12+/viam/api/v1/component/arm/{name}/3d_modelsB=\n\x19com.viam.component.arm.v1Z go.viam.com/api/component/arm/v1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'component.arm.v1.arm_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x19com.viam.component.arm.v1Z go.viam.com/api/component/arm/v1'
    _globals['_ARMSERVICE'].methods_by_name['GetEndPosition']._loaded_options = None
    _globals['_ARMSERVICE'].methods_by_name['GetEndPosition']._serialized_options = b'\x82\xd3\xe4\x93\x02,\x12*/viam/api/v1/component/arm/{name}/position'
    _globals['_ARMSERVICE'].methods_by_name['MoveToPosition']._loaded_options = None
    _globals['_ARMSERVICE'].methods_by_name['MoveToPosition']._serialized_options = b'\xa0\x92)\x01\x82\xd3\xe4\x93\x02,\x1a*/viam/api/v1/component/arm/{name}/position'
    _globals['_ARMSERVICE'].methods_by_name['GetJointPositions']._loaded_options = None
    _globals['_ARMSERVICE'].methods_by_name['GetJointPositions']._serialized_options = b'\x82\xd3\xe4\x93\x023\x121/viam/api/v1/component/arm/{name}/joint_positions'
    _globals['_ARMSERVICE'].methods_by_name['MoveToJointPositions']._loaded_options = None
    _globals['_ARMSERVICE'].methods_by_name['MoveToJointPositions']._serialized_options = b'\xa0\x92)\x01\x82\xd3\xe4\x93\x023\x1a1/viam/api/v1/component/arm/{name}/joint_positions'
    _globals['_ARMSERVICE'].methods_by_name['MoveThroughJointPositions']._loaded_options = None
    _globals['_ARMSERVICE'].methods_by_name['MoveThroughJointPositions']._serialized_options = b'\xa0\x92)\x01\x82\xd3\xe4\x93\x02@">/viam/api/v1/component/arm/{name}/move_through_joint_positions'
    _globals['_ARMSERVICE'].methods_by_name['MoveThroughJointPositionsStreamed']._loaded_options = None
    _globals['_ARMSERVICE'].methods_by_name['MoveThroughJointPositionsStreamed']._serialized_options = b'\xa0\x92)\x01'
    _globals['_ARMSERVICE'].methods_by_name['Stop']._loaded_options = None
    _globals['_ARMSERVICE'].methods_by_name['Stop']._serialized_options = b'\x82\xd3\xe4\x93\x02("&/viam/api/v1/component/arm/{name}/stop'
    _globals['_ARMSERVICE'].methods_by_name['IsMoving']._loaded_options = None
    _globals['_ARMSERVICE'].methods_by_name['IsMoving']._serialized_options = b'\x82\xd3\xe4\x93\x02-\x12+/viam/api/v1/component/arm/{name}/is_moving'
    _globals['_ARMSERVICE'].methods_by_name['DoCommand']._loaded_options = None
    _globals['_ARMSERVICE'].methods_by_name['DoCommand']._serialized_options = b'\x82\xd3\xe4\x93\x02.",/viam/api/v1/component/arm/{name}/do_command'
    _globals['_ARMSERVICE'].methods_by_name['GetStatus']._loaded_options = None
    _globals['_ARMSERVICE'].methods_by_name['GetStatus']._serialized_options = b'\x82\xd3\xe4\x93\x02.\x12,/viam/api/v1/component/arm/{name}/get_status'
    _globals['_ARMSERVICE'].methods_by_name['GetKinematics']._loaded_options = None
    _globals['_ARMSERVICE'].methods_by_name['GetKinematics']._serialized_options = b'\x82\xd3\xe4\x93\x02.\x12,/viam/api/v1/component/arm/{name}/kinematics'
    _globals['_ARMSERVICE'].methods_by_name['GetGeometries']._loaded_options = None
    _globals['_ARMSERVICE'].methods_by_name['GetGeometries']._serialized_options = b'\x82\xd3\xe4\x93\x02.\x12,/viam/api/v1/component/arm/{name}/geometries'
    _globals['_ARMSERVICE'].methods_by_name['Get3DModels']._loaded_options = None
    _globals['_ARMSERVICE'].methods_by_name['Get3DModels']._serialized_options = b'\x82\xd3\xe4\x93\x02-\x12+/viam/api/v1/component/arm/{name}/3d_models'
    _globals['_GETENDPOSITIONREQUEST']._serialized_start = 169
    _globals['_GETENDPOSITIONREQUEST']._serialized_end = 259
    _globals['_GETENDPOSITIONRESPONSE']._serialized_start = 261
    _globals['_GETENDPOSITIONRESPONSE']._serialized_end = 327
    _globals['_JOINTPOSITIONS']._serialized_start = 329
    _globals['_JOINTPOSITIONS']._serialized_end = 369
    _globals['_JOINTVELOCITIES']._serialized_start = 371
    _globals['_JOINTVELOCITIES']._serialized_end = 412
    _globals['_JOINTACCELERATIONS']._serialized_start = 414
    _globals['_JOINTACCELERATIONS']._serialized_end = 458
    _globals['_GETJOINTPOSITIONSREQUEST']._serialized_start = 460
    _globals['_GETJOINTPOSITIONSREQUEST']._serialized_end = 553
    _globals['_GETJOINTPOSITIONSRESPONSE']._serialized_start = 555
    _globals['_GETJOINTPOSITIONSRESPONSE']._serialized_end = 651
    _globals['_MOVETOPOSITIONREQUEST']._serialized_start = 654
    _globals['_MOVETOPOSITIONREQUEST']._serialized_end = 782
    _globals['_MOVETOPOSITIONRESPONSE']._serialized_start = 784
    _globals['_MOVETOPOSITIONRESPONSE']._serialized_end = 808
    _globals['_MOVETOJOINTPOSITIONSREQUEST']._serialized_start = 811
    _globals['_MOVETOJOINTPOSITIONSREQUEST']._serialized_end = 976
    _globals['_MOVETOJOINTPOSITIONSRESPONSE']._serialized_start = 978
    _globals['_MOVETOJOINTPOSITIONSRESPONSE']._serialized_end = 1008
    _globals['_MOVETHROUGHJOINTPOSITIONSREQUEST']._serialized_start = 1011
    _globals['_MOVETHROUGHJOINTPOSITIONSREQUEST']._serialized_end = 1260
    _globals['_MOVETHROUGHJOINTPOSITIONSRESPONSE']._serialized_start = 1262
    _globals['_MOVETHROUGHJOINTPOSITIONSRESPONSE']._serialized_end = 1297
    _globals['_TRAJECTORYPOINT']._serialized_start = 1300
    _globals['_TRAJECTORYPOINT']._serialized_end = 1750
    _globals['_TRAJECTORYPOINT_KINEMATICCONSTRAINTS']._serialized_start = 1536
    _globals['_TRAJECTORYPOINT_KINEMATICCONSTRAINTS']._serialized_end = 1734
    _globals['_MOVETHROUGHJOINTPOSITIONSSTREAMEDREQUEST']._serialized_start = 1753
    _globals['_MOVETHROUGHJOINTPOSITIONSSTREAMEDREQUEST']._serialized_end = 2161
    _globals['_MOVETHROUGHJOINTPOSITIONSSTREAMEDREQUEST_INIT']._serialized_start = 2014
    _globals['_MOVETHROUGHJOINTPOSITIONSSTREAMEDREQUEST_INIT']._serialized_end = 2067
    _globals['_MOVETHROUGHJOINTPOSITIONSSTREAMEDREQUEST_TRAJECTORYBATCH']._serialized_start = 2069
    _globals['_MOVETHROUGHJOINTPOSITIONSSTREAMEDREQUEST_TRAJECTORYBATCH']._serialized_end = 2150
    _globals['_MOVETHROUGHJOINTPOSITIONSSTREAMEDRESPONSE']._serialized_start = 2164
    _globals['_MOVETHROUGHJOINTPOSITIONSSTREAMEDRESPONSE']._serialized_end = 2372
    _globals['_MOVETHROUGHJOINTPOSITIONSSTREAMEDRESPONSE_BATCHACK']._serialized_start = 2304
    _globals['_MOVETHROUGHJOINTPOSITIONSSTREAMEDRESPONSE_BATCHACK']._serialized_end = 2361
    _globals['_STOPREQUEST']._serialized_start = 2374
    _globals['_STOPREQUEST']._serialized_end = 2454
    _globals['_STOPRESPONSE']._serialized_start = 2456
    _globals['_STOPRESPONSE']._serialized_end = 2470
    _globals['_STATUS']._serialized_start = 2473
    _globals['_STATUS']._serialized_end = 2647
    _globals['_ISMOVINGREQUEST']._serialized_start = 2649
    _globals['_ISMOVINGREQUEST']._serialized_end = 2686
    _globals['_ISMOVINGRESPONSE']._serialized_start = 2688
    _globals['_ISMOVINGRESPONSE']._serialized_end = 2735
    _globals['_MOVEOPTIONS']._serialized_start = 2738
    _globals['_MOVEOPTIONS']._serialized_end = 3093
    _globals['_ARMSERVICE']._serialized_start = 3096
    _globals['_ARMSERVICE']._serialized_end = 5203