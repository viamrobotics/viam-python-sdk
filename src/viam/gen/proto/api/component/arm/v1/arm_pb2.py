"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from ......proto.api.common.v1 import common_pb2 as proto_dot_api_dot_common_dot_v1_dot_common__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$proto/api/component/arm/v1/arm.proto\x12\x1aproto.api.component.arm.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a proto/api/common/v1/common.proto"Z\n\x15GetEndPositionRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"G\n\x16GetEndPositionResponse\x12-\n\x04pose\x18\x01 \x01(\x0b2\x19.proto.api.common.v1.PoseR\x04pose"(\n\x0eJointPositions\x12\x16\n\x06values\x18\x01 \x03(\x01R\x06values"]\n\x18GetJointPositionsRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"e\n\x19GetJointPositionsResponse\x12H\n\tpositions\x18\x01 \x01(\x0b2*.proto.api.component.arm.v1.JointPositionsR\tpositions"\xdc\x01\n\x15MoveToPositionRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12)\n\x02to\x18\x02 \x01(\x0b2\x19.proto.api.common.v1.PoseR\x02to\x12E\n\x0bworld_state\x18\x03 \x01(\x0b2\x1f.proto.api.common.v1.WorldStateH\x00R\nworldState\x88\x01\x01\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extraB\x0e\n\x0c_world_state"\x18\n\x16MoveToPositionResponse"\xaa\x01\n\x1bMoveToJointPositionsRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12H\n\tpositions\x18\x02 \x01(\x0b2*.proto.api.component.arm.v1.JointPositionsR\tpositions\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"\x1e\n\x1cMoveToJointPositionsResponse"P\n\x0bStopRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"\x0e\n\x0cStopResponse"\xb8\x01\n\x06Status\x12<\n\x0cend_position\x18\x01 \x01(\x0b2\x19.proto.api.common.v1.PoseR\x0bendPosition\x12S\n\x0fjoint_positions\x18\x02 \x01(\x0b2*.proto.api.component.arm.v1.JointPositionsR\x0ejointPositions\x12\x1b\n\tis_moving\x18\x03 \x01(\x08R\x08isMoving2\xf9\x06\n\nArmService\x12\xab\x01\n\x0eGetEndPosition\x121.proto.api.component.arm.v1.GetEndPositionRequest\x1a2.proto.api.component.arm.v1.GetEndPositionResponse"2\x82\xd3\xe4\x93\x02,\x12*/viam/api/v1/component/arm/{name}/position\x12\xab\x01\n\x0eMoveToPosition\x121.proto.api.component.arm.v1.MoveToPositionRequest\x1a2.proto.api.component.arm.v1.MoveToPositionResponse"2\x82\xd3\xe4\x93\x02,\x1a*/viam/api/v1/component/arm/{name}/position\x12\xbb\x01\n\x11GetJointPositions\x124.proto.api.component.arm.v1.GetJointPositionsRequest\x1a5.proto.api.component.arm.v1.GetJointPositionsResponse"9\x82\xd3\xe4\x93\x023\x121/viam/api/v1/component/arm/{name}/joint_positions\x12\xc4\x01\n\x14MoveToJointPositions\x127.proto.api.component.arm.v1.MoveToJointPositionsRequest\x1a8.proto.api.component.arm.v1.MoveToJointPositionsResponse"9\x82\xd3\xe4\x93\x023\x1a1/viam/api/v1/component/arm/{name}/joint_positions\x12\x89\x01\n\x04Stop\x12\'.proto.api.component.arm.v1.StopRequest\x1a(.proto.api.component.arm.v1.StopResponse".\x82\xd3\xe4\x93\x02("&/viam/api/v1/component/arm/{name}/stopBU\n\'com.viam.rdk.proto.api.component.arm.v1Z*go.viam.com/rdk/proto/api/component/arm/v1b\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'proto.api.component.arm.v1.arm_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b"\n'com.viam.rdk.proto.api.component.arm.v1Z*go.viam.com/rdk/proto/api/component/arm/v1"
    _ARMSERVICE.methods_by_name['GetEndPosition']._options = None
    _ARMSERVICE.methods_by_name['GetEndPosition']._serialized_options = b'\x82\xd3\xe4\x93\x02,\x12*/viam/api/v1/component/arm/{name}/position'
    _ARMSERVICE.methods_by_name['MoveToPosition']._options = None
    _ARMSERVICE.methods_by_name['MoveToPosition']._serialized_options = b'\x82\xd3\xe4\x93\x02,\x1a*/viam/api/v1/component/arm/{name}/position'
    _ARMSERVICE.methods_by_name['GetJointPositions']._options = None
    _ARMSERVICE.methods_by_name['GetJointPositions']._serialized_options = b'\x82\xd3\xe4\x93\x023\x121/viam/api/v1/component/arm/{name}/joint_positions'
    _ARMSERVICE.methods_by_name['MoveToJointPositions']._options = None
    _ARMSERVICE.methods_by_name['MoveToJointPositions']._serialized_options = b'\x82\xd3\xe4\x93\x023\x1a1/viam/api/v1/component/arm/{name}/joint_positions'
    _ARMSERVICE.methods_by_name['Stop']._options = None
    _ARMSERVICE.methods_by_name['Stop']._serialized_options = b'\x82\xd3\xe4\x93\x02("&/viam/api/v1/component/arm/{name}/stop'
    _GETENDPOSITIONREQUEST._serialized_start = 162
    _GETENDPOSITIONREQUEST._serialized_end = 252
    _GETENDPOSITIONRESPONSE._serialized_start = 254
    _GETENDPOSITIONRESPONSE._serialized_end = 325
    _JOINTPOSITIONS._serialized_start = 327
    _JOINTPOSITIONS._serialized_end = 367
    _GETJOINTPOSITIONSREQUEST._serialized_start = 369
    _GETJOINTPOSITIONSREQUEST._serialized_end = 462
    _GETJOINTPOSITIONSRESPONSE._serialized_start = 464
    _GETJOINTPOSITIONSRESPONSE._serialized_end = 565
    _MOVETOPOSITIONREQUEST._serialized_start = 568
    _MOVETOPOSITIONREQUEST._serialized_end = 788
    _MOVETOPOSITIONRESPONSE._serialized_start = 790
    _MOVETOPOSITIONRESPONSE._serialized_end = 814
    _MOVETOJOINTPOSITIONSREQUEST._serialized_start = 817
    _MOVETOJOINTPOSITIONSREQUEST._serialized_end = 987
    _MOVETOJOINTPOSITIONSRESPONSE._serialized_start = 989
    _MOVETOJOINTPOSITIONSRESPONSE._serialized_end = 1019
    _STOPREQUEST._serialized_start = 1021
    _STOPREQUEST._serialized_end = 1101
    _STOPRESPONSE._serialized_start = 1103
    _STOPRESPONSE._serialized_end = 1117
    _STATUS._serialized_start = 1120
    _STATUS._serialized_end = 1304
    _ARMSERVICE._serialized_start = 1307
    _ARMSERVICE._serialized_end = 2196