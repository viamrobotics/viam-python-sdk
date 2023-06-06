"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....common.v1 import common_pb2 as common_dot_v1_dot_common__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1acomponent/arm/v1/arm.proto\x12\x15viam.component.arm.v1\x1a\x16common/v1/common.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1cgoogle/protobuf/struct.proto"Z\n\x15GetEndPositionRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"B\n\x16GetEndPositionResponse\x12(\n\x04pose\x18\x01 \x01(\x0b2\x14.viam.common.v1.PoseR\x04pose"(\n\x0eJointPositions\x12\x16\n\x06values\x18\x01 \x03(\x01R\x06values"]\n\x18GetJointPositionsRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"`\n\x19GetJointPositionsResponse\x12C\n\tpositions\x18\x01 \x01(\x0b2%.viam.component.arm.v1.JointPositionsR\tpositions"\x80\x01\n\x15MoveToPositionRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12$\n\x02to\x18\x02 \x01(\x0b2\x14.viam.common.v1.PoseR\x02to\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"\x18\n\x16MoveToPositionResponse"\xa5\x01\n\x1bMoveToJointPositionsRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12C\n\tpositions\x18\x02 \x01(\x0b2%.viam.component.arm.v1.JointPositionsR\tpositions\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"\x1e\n\x1cMoveToJointPositionsResponse"P\n\x0bStopRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"\x0e\n\x0cStopResponse"\xae\x01\n\x06Status\x127\n\x0cend_position\x18\x01 \x01(\x0b2\x14.viam.common.v1.PoseR\x0bendPosition\x12N\n\x0fjoint_positions\x18\x02 \x01(\x0b2%.viam.component.arm.v1.JointPositionsR\x0ejointPositions\x12\x1b\n\tis_moving\x18\x03 \x01(\x08R\x08isMoving"%\n\x0fIsMovingRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name"/\n\x10IsMovingResponse\x12\x1b\n\tis_moving\x18\x01 \x01(\x08R\x08isMoving2\x94\x0b\n\nArmService\x12\xa1\x01\n\x0eGetEndPosition\x12,.viam.component.arm.v1.GetEndPositionRequest\x1a-.viam.component.arm.v1.GetEndPositionResponse"2\x82\xd3\xe4\x93\x02,\x12*/viam/api/v1/component/arm/{name}/position\x12\xa5\x01\n\x0eMoveToPosition\x12,.viam.component.arm.v1.MoveToPositionRequest\x1a-.viam.component.arm.v1.MoveToPositionResponse"6\xa0\x92)\x01\x82\xd3\xe4\x93\x02,\x1a*/viam/api/v1/component/arm/{name}/position\x12\xb1\x01\n\x11GetJointPositions\x12/.viam.component.arm.v1.GetJointPositionsRequest\x1a0.viam.component.arm.v1.GetJointPositionsResponse"9\x82\xd3\xe4\x93\x023\x121/viam/api/v1/component/arm/{name}/joint_positions\x12\xbe\x01\n\x14MoveToJointPositions\x122.viam.component.arm.v1.MoveToJointPositionsRequest\x1a3.viam.component.arm.v1.MoveToJointPositionsResponse"=\xa0\x92)\x01\x82\xd3\xe4\x93\x023\x1a1/viam/api/v1/component/arm/{name}/joint_positions\x12\x7f\n\x04Stop\x12".viam.component.arm.v1.StopRequest\x1a#.viam.component.arm.v1.StopResponse".\x82\xd3\xe4\x93\x02("&/viam/api/v1/component/arm/{name}/stop\x12\x90\x01\n\x08IsMoving\x12&.viam.component.arm.v1.IsMovingRequest\x1a\'.viam.component.arm.v1.IsMovingResponse"3\x82\xd3\xe4\x93\x02-\x12+/viam/api/v1/component/arm/{name}/is_moving\x12\x86\x01\n\tDoCommand\x12 .viam.common.v1.DoCommandRequest\x1a!.viam.common.v1.DoCommandResponse"4\x82\xd3\xe4\x93\x02.",/viam/api/v1/component/arm/{name}/do_command\x12\x92\x01\n\rGetKinematics\x12$.viam.common.v1.GetKinematicsRequest\x1a%.viam.common.v1.GetKinematicsResponse"4\x82\xd3\xe4\x93\x02.\x12,/viam/api/v1/component/arm/{name}/kinematics\x12\x92\x01\n\rGetGeometries\x12$.viam.common.v1.GetGeometriesRequest\x1a%.viam.common.v1.GetGeometriesResponse"4\x82\xd3\xe4\x93\x02.\x12,/viam/api/v1/component/arm/{name}/geometriesB=\n\x19com.viam.component.arm.v1Z go.viam.com/api/component/arm/v1b\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'component.arm.v1.arm_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n\x19com.viam.component.arm.v1Z go.viam.com/api/component/arm/v1'
    _ARMSERVICE.methods_by_name['GetEndPosition']._options = None
    _ARMSERVICE.methods_by_name['GetEndPosition']._serialized_options = b'\x82\xd3\xe4\x93\x02,\x12*/viam/api/v1/component/arm/{name}/position'
    _ARMSERVICE.methods_by_name['MoveToPosition']._options = None
    _ARMSERVICE.methods_by_name['MoveToPosition']._serialized_options = b'\xa0\x92)\x01\x82\xd3\xe4\x93\x02,\x1a*/viam/api/v1/component/arm/{name}/position'
    _ARMSERVICE.methods_by_name['GetJointPositions']._options = None
    _ARMSERVICE.methods_by_name['GetJointPositions']._serialized_options = b'\x82\xd3\xe4\x93\x023\x121/viam/api/v1/component/arm/{name}/joint_positions'
    _ARMSERVICE.methods_by_name['MoveToJointPositions']._options = None
    _ARMSERVICE.methods_by_name['MoveToJointPositions']._serialized_options = b'\xa0\x92)\x01\x82\xd3\xe4\x93\x023\x1a1/viam/api/v1/component/arm/{name}/joint_positions'
    _ARMSERVICE.methods_by_name['Stop']._options = None
    _ARMSERVICE.methods_by_name['Stop']._serialized_options = b'\x82\xd3\xe4\x93\x02("&/viam/api/v1/component/arm/{name}/stop'
    _ARMSERVICE.methods_by_name['IsMoving']._options = None
    _ARMSERVICE.methods_by_name['IsMoving']._serialized_options = b'\x82\xd3\xe4\x93\x02-\x12+/viam/api/v1/component/arm/{name}/is_moving'
    _ARMSERVICE.methods_by_name['DoCommand']._options = None
    _ARMSERVICE.methods_by_name['DoCommand']._serialized_options = b'\x82\xd3\xe4\x93\x02.",/viam/api/v1/component/arm/{name}/do_command'
    _ARMSERVICE.methods_by_name['GetKinematics']._options = None
    _ARMSERVICE.methods_by_name['GetKinematics']._serialized_options = b'\x82\xd3\xe4\x93\x02.\x12,/viam/api/v1/component/arm/{name}/kinematics'
    _ARMSERVICE.methods_by_name['GetGeometries']._options = None
    _ARMSERVICE.methods_by_name['GetGeometries']._serialized_options = b'\x82\xd3\xe4\x93\x02.\x12,/viam/api/v1/component/arm/{name}/geometries'
    _GETENDPOSITIONREQUEST._serialized_start = 137
    _GETENDPOSITIONREQUEST._serialized_end = 227
    _GETENDPOSITIONRESPONSE._serialized_start = 229
    _GETENDPOSITIONRESPONSE._serialized_end = 295
    _JOINTPOSITIONS._serialized_start = 297
    _JOINTPOSITIONS._serialized_end = 337
    _GETJOINTPOSITIONSREQUEST._serialized_start = 339
    _GETJOINTPOSITIONSREQUEST._serialized_end = 432
    _GETJOINTPOSITIONSRESPONSE._serialized_start = 434
    _GETJOINTPOSITIONSRESPONSE._serialized_end = 530
    _MOVETOPOSITIONREQUEST._serialized_start = 533
    _MOVETOPOSITIONREQUEST._serialized_end = 661
    _MOVETOPOSITIONRESPONSE._serialized_start = 663
    _MOVETOPOSITIONRESPONSE._serialized_end = 687
    _MOVETOJOINTPOSITIONSREQUEST._serialized_start = 690
    _MOVETOJOINTPOSITIONSREQUEST._serialized_end = 855
    _MOVETOJOINTPOSITIONSRESPONSE._serialized_start = 857
    _MOVETOJOINTPOSITIONSRESPONSE._serialized_end = 887
    _STOPREQUEST._serialized_start = 889
    _STOPREQUEST._serialized_end = 969
    _STOPRESPONSE._serialized_start = 971
    _STOPRESPONSE._serialized_end = 985
    _STATUS._serialized_start = 988
    _STATUS._serialized_end = 1162
    _ISMOVINGREQUEST._serialized_start = 1164
    _ISMOVINGREQUEST._serialized_end = 1201
    _ISMOVINGRESPONSE._serialized_start = 1203
    _ISMOVINGRESPONSE._serialized_end = 1250
    _ARMSERVICE._serialized_start = 1253
    _ARMSERVICE._serialized_end = 2681