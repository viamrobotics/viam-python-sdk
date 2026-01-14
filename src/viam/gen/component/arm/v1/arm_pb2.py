"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 2, '', 'component/arm/v1/arm.proto')
_sym_db = _symbol_database.Default()
from ....common.v1 import common_pb2 as common_dot_v1_dot_common__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1acomponent/arm/v1/arm.proto\x12\x15viam.component.arm.v1\x1a\x16common/v1/common.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto"Z\n\x15GetEndPositionRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"B\n\x16GetEndPositionResponse\x12(\n\x04pose\x18\x01 \x01(\x0b2\x14.viam.common.v1.PoseR\x04pose"(\n\x0eJointPositions\x12\x16\n\x06values\x18\x01 \x03(\x01R\x06values"]\n\x18GetJointPositionsRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"`\n\x19GetJointPositionsResponse\x12C\n\tpositions\x18\x01 \x01(\x0b2%.viam.component.arm.v1.JointPositionsR\tpositions"\x7f\n\x1bStreamJointPositionsRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x15\n\x03fps\x18\x02 \x01(\x05H\x00R\x03fps\x88\x01\x01\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extraB\x06\n\x04_fps"\xb9\x01\n\x1cStreamJointPositionsResponse\x12C\n\tpositions\x18\x01 \x01(\x0b2%.viam.component.arm.v1.JointPositionsR\tpositions\x128\n\ttimestamp\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampR\ttimestamp\x12\x1a\n\x08sequence\x18\x03 \x01(\x05R\x08sequence"\x80\x01\n\x15MoveToPositionRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12$\n\x02to\x18\x02 \x01(\x0b2\x14.viam.common.v1.PoseR\x02to\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"\x18\n\x16MoveToPositionResponse"\xa5\x01\n\x1bMoveToJointPositionsRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12C\n\tpositions\x18\x02 \x01(\x0b2%.viam.component.arm.v1.JointPositionsR\tpositions\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"\x1e\n\x1cMoveToJointPositionsResponse"\xf9\x01\n MoveThroughJointPositionsRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12C\n\tpositions\x18\x02 \x03(\x0b2%.viam.component.arm.v1.JointPositionsR\tpositions\x12A\n\x07options\x18\x03 \x01(\x0b2".viam.component.arm.v1.MoveOptionsH\x00R\x07options\x88\x01\x01\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extraB\n\n\x08_options"#\n!MoveThroughJointPositionsResponse"P\n\x0bStopRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"\x0e\n\x0cStopResponse"\xae\x01\n\x06Status\x127\n\x0cend_position\x18\x01 \x01(\x0b2\x14.viam.common.v1.PoseR\x0bendPosition\x12N\n\x0fjoint_positions\x18\x02 \x01(\x0b2%.viam.component.arm.v1.JointPositionsR\x0ejointPositions\x12\x1b\n\tis_moving\x18\x03 \x01(\x08R\x08isMoving"%\n\x0fIsMovingRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name"/\n\x10IsMovingResponse\x12\x1b\n\tis_moving\x18\x01 \x01(\x08R\x08isMoving"\xac\x01\n\x0bMoveOptions\x123\n\x14max_vel_degs_per_sec\x18\x01 \x01(\x01H\x00R\x10maxVelDegsPerSec\x88\x01\x01\x125\n\x15max_acc_degs_per_sec2\x18\x02 \x01(\x01H\x01R\x11maxAccDegsPerSec2\x88\x01\x01B\x17\n\x15_max_vel_degs_per_secB\x18\n\x16_max_acc_degs_per_sec22\xc5\x0f\n\nArmService\x12\xa1\x01\n\x0eGetEndPosition\x12,.viam.component.arm.v1.GetEndPositionRequest\x1a-.viam.component.arm.v1.GetEndPositionResponse"2\x82\xd3\xe4\x93\x02,\x12*/viam/api/v1/component/arm/{name}/position\x12\xa5\x01\n\x0eMoveToPosition\x12,.viam.component.arm.v1.MoveToPositionRequest\x1a-.viam.component.arm.v1.MoveToPositionResponse"6\xa0\x92)\x01\x82\xd3\xe4\x93\x02,\x1a*/viam/api/v1/component/arm/{name}/position\x12\xb1\x01\n\x11GetJointPositions\x12/.viam.component.arm.v1.GetJointPositionsRequest\x1a0.viam.component.arm.v1.GetJointPositionsResponse"9\x82\xd3\xe4\x93\x023\x121/viam/api/v1/component/arm/{name}/joint_positions\x12\xc3\x01\n\x14StreamJointPositions\x122.viam.component.arm.v1.StreamJointPositionsRequest\x1a3.viam.component.arm.v1.StreamJointPositionsResponse"@\x82\xd3\xe4\x93\x02:\x128/viam/api/v1/component/arm/{name}/stream_joint_positions0\x01\x12\xbe\x01\n\x14MoveToJointPositions\x122.viam.component.arm.v1.MoveToJointPositionsRequest\x1a3.viam.component.arm.v1.MoveToJointPositionsResponse"=\xa0\x92)\x01\x82\xd3\xe4\x93\x023\x1a1/viam/api/v1/component/arm/{name}/joint_positions\x12\xda\x01\n\x19MoveThroughJointPositions\x127.viam.component.arm.v1.MoveThroughJointPositionsRequest\x1a8.viam.component.arm.v1.MoveThroughJointPositionsResponse"J\xa0\x92)\x01\x82\xd3\xe4\x93\x02@">/viam/api/v1/component/arm/{name}/move_through_joint_positions\x12\x7f\n\x04Stop\x12".viam.component.arm.v1.StopRequest\x1a#.viam.component.arm.v1.StopResponse".\x82\xd3\xe4\x93\x02("&/viam/api/v1/component/arm/{name}/stop\x12\x90\x01\n\x08IsMoving\x12&.viam.component.arm.v1.IsMovingRequest\x1a\'.viam.component.arm.v1.IsMovingResponse"3\x82\xd3\xe4\x93\x02-\x12+/viam/api/v1/component/arm/{name}/is_moving\x12\x86\x01\n\tDoCommand\x12 .viam.common.v1.DoCommandRequest\x1a!.viam.common.v1.DoCommandResponse"4\x82\xd3\xe4\x93\x02.",/viam/api/v1/component/arm/{name}/do_command\x12\x92\x01\n\rGetKinematics\x12$.viam.common.v1.GetKinematicsRequest\x1a%.viam.common.v1.GetKinematicsResponse"4\x82\xd3\xe4\x93\x02.\x12,/viam/api/v1/component/arm/{name}/kinematics\x12\x92\x01\n\rGetGeometries\x12$.viam.common.v1.GetGeometriesRequest\x1a%.viam.common.v1.GetGeometriesResponse"4\x82\xd3\xe4\x93\x02.\x12,/viam/api/v1/component/arm/{name}/geometries\x12\x8b\x01\n\x0bGet3DModels\x12".viam.common.v1.Get3DModelsRequest\x1a#.viam.common.v1.Get3DModelsResponse"3\x82\xd3\xe4\x93\x02-\x12+/viam/api/v1/component/arm/{name}/3d_modelsB=\n\x19com.viam.component.arm.v1Z go.viam.com/api/component/arm/v1b\x06proto3')
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
    _globals['_ARMSERVICE'].methods_by_name['StreamJointPositions']._loaded_options = None
    _globals['_ARMSERVICE'].methods_by_name['StreamJointPositions']._serialized_options = b'\x82\xd3\xe4\x93\x02:\x128/viam/api/v1/component/arm/{name}/stream_joint_positions'
    _globals['_ARMSERVICE'].methods_by_name['MoveToJointPositions']._loaded_options = None
    _globals['_ARMSERVICE'].methods_by_name['MoveToJointPositions']._serialized_options = b'\xa0\x92)\x01\x82\xd3\xe4\x93\x023\x1a1/viam/api/v1/component/arm/{name}/joint_positions'
    _globals['_ARMSERVICE'].methods_by_name['MoveThroughJointPositions']._loaded_options = None
    _globals['_ARMSERVICE'].methods_by_name['MoveThroughJointPositions']._serialized_options = b'\xa0\x92)\x01\x82\xd3\xe4\x93\x02@">/viam/api/v1/component/arm/{name}/move_through_joint_positions'
    _globals['_ARMSERVICE'].methods_by_name['Stop']._loaded_options = None
    _globals['_ARMSERVICE'].methods_by_name['Stop']._serialized_options = b'\x82\xd3\xe4\x93\x02("&/viam/api/v1/component/arm/{name}/stop'
    _globals['_ARMSERVICE'].methods_by_name['IsMoving']._loaded_options = None
    _globals['_ARMSERVICE'].methods_by_name['IsMoving']._serialized_options = b'\x82\xd3\xe4\x93\x02-\x12+/viam/api/v1/component/arm/{name}/is_moving'
    _globals['_ARMSERVICE'].methods_by_name['DoCommand']._loaded_options = None
    _globals['_ARMSERVICE'].methods_by_name['DoCommand']._serialized_options = b'\x82\xd3\xe4\x93\x02.",/viam/api/v1/component/arm/{name}/do_command'
    _globals['_ARMSERVICE'].methods_by_name['GetKinematics']._loaded_options = None
    _globals['_ARMSERVICE'].methods_by_name['GetKinematics']._serialized_options = b'\x82\xd3\xe4\x93\x02.\x12,/viam/api/v1/component/arm/{name}/kinematics'
    _globals['_ARMSERVICE'].methods_by_name['GetGeometries']._loaded_options = None
    _globals['_ARMSERVICE'].methods_by_name['GetGeometries']._serialized_options = b'\x82\xd3\xe4\x93\x02.\x12,/viam/api/v1/component/arm/{name}/geometries'
    _globals['_ARMSERVICE'].methods_by_name['Get3DModels']._loaded_options = None
    _globals['_ARMSERVICE'].methods_by_name['Get3DModels']._serialized_options = b'\x82\xd3\xe4\x93\x02-\x12+/viam/api/v1/component/arm/{name}/3d_models'
    _globals['_GETENDPOSITIONREQUEST']._serialized_start = 170
    _globals['_GETENDPOSITIONREQUEST']._serialized_end = 260
    _globals['_GETENDPOSITIONRESPONSE']._serialized_start = 262
    _globals['_GETENDPOSITIONRESPONSE']._serialized_end = 328
    _globals['_JOINTPOSITIONS']._serialized_start = 330
    _globals['_JOINTPOSITIONS']._serialized_end = 370
    _globals['_GETJOINTPOSITIONSREQUEST']._serialized_start = 372
    _globals['_GETJOINTPOSITIONSREQUEST']._serialized_end = 465
    _globals['_GETJOINTPOSITIONSRESPONSE']._serialized_start = 467
    _globals['_GETJOINTPOSITIONSRESPONSE']._serialized_end = 563
    _globals['_STREAMJOINTPOSITIONSREQUEST']._serialized_start = 565
    _globals['_STREAMJOINTPOSITIONSREQUEST']._serialized_end = 692
    _globals['_STREAMJOINTPOSITIONSRESPONSE']._serialized_start = 695
    _globals['_STREAMJOINTPOSITIONSRESPONSE']._serialized_end = 880
    _globals['_MOVETOPOSITIONREQUEST']._serialized_start = 883
    _globals['_MOVETOPOSITIONREQUEST']._serialized_end = 1011
    _globals['_MOVETOPOSITIONRESPONSE']._serialized_start = 1013
    _globals['_MOVETOPOSITIONRESPONSE']._serialized_end = 1037
    _globals['_MOVETOJOINTPOSITIONSREQUEST']._serialized_start = 1040
    _globals['_MOVETOJOINTPOSITIONSREQUEST']._serialized_end = 1205
    _globals['_MOVETOJOINTPOSITIONSRESPONSE']._serialized_start = 1207
    _globals['_MOVETOJOINTPOSITIONSRESPONSE']._serialized_end = 1237
    _globals['_MOVETHROUGHJOINTPOSITIONSREQUEST']._serialized_start = 1240
    _globals['_MOVETHROUGHJOINTPOSITIONSREQUEST']._serialized_end = 1489
    _globals['_MOVETHROUGHJOINTPOSITIONSRESPONSE']._serialized_start = 1491
    _globals['_MOVETHROUGHJOINTPOSITIONSRESPONSE']._serialized_end = 1526
    _globals['_STOPREQUEST']._serialized_start = 1528
    _globals['_STOPREQUEST']._serialized_end = 1608
    _globals['_STOPRESPONSE']._serialized_start = 1610
    _globals['_STOPRESPONSE']._serialized_end = 1624
    _globals['_STATUS']._serialized_start = 1627
    _globals['_STATUS']._serialized_end = 1801
    _globals['_ISMOVINGREQUEST']._serialized_start = 1803
    _globals['_ISMOVINGREQUEST']._serialized_end = 1840
    _globals['_ISMOVINGRESPONSE']._serialized_start = 1842
    _globals['_ISMOVINGRESPONSE']._serialized_end = 1889
    _globals['_MOVEOPTIONS']._serialized_start = 1892
    _globals['_MOVEOPTIONS']._serialized_end = 2064
    _globals['_ARMSERVICE']._serialized_start = 2067
    _globals['_ARMSERVICE']._serialized_end = 4056
