"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......proto.api.common.v1 import common_pb2 as proto_dot_api_dot_common_dot_v1_dot_common__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nAproto/api/service/objectmanipulation/v1/object_manipulation.proto\x12\'proto.api.service.objectmanipulation.v1\x1a\x1cgoogle/api/annotations.proto\x1a proto/api/common/v1/common.proto"\xc3\x01\n\rDoGrabRequest\x128\n\x06target\x18\x01 \x01(\x0b2 .proto.api.common.v1.PoseInFrameR\x06target\x12!\n\x0cgripper_name\x18\x02 \x01(\tR\x0bgripperName\x12E\n\x0bworld_state\x18\x03 \x01(\x0b2\x1f.proto.api.common.v1.WorldStateH\x00R\nworldState\x88\x01\x01B\x0e\n\x0c_world_state"*\n\x0eDoGrabResponse\x12\x18\n\x07success\x18\x01 \x01(\x08R\x07success"\x87\x01\n\x0eGetPoseRequest\x12H\n\x0ecomponent_name\x18\x01 \x01(\x0b2!.proto.api.common.v1.ResourceNameR\rcomponentName\x12+\n\x11destination_frame\x18\x02 \x01(\tR\x10destinationFrame"G\n\x0fGetPoseResponse\x124\n\x04pose\x18\x01 \x01(\x0b2 .proto.api.common.v1.PoseInFrameR\x04pose2\x87\x03\n\x19ObjectManipulationService\x12\xb3\x01\n\x06DoGrab\x126.proto.api.service.objectmanipulation.v1.DoGrabRequest\x1a7.proto.api.service.objectmanipulation.v1.DoGrabResponse"8\x82\xd3\xe4\x93\x022"0/viam/api/v1/service/object_manipulation/do_grab\x12\xb3\x01\n\x07GetPose\x127.proto.api.service.objectmanipulation.v1.GetPoseRequest\x1a8.proto.api.service.objectmanipulation.v1.GetPoseResponse"5\x82\xd3\xe4\x93\x02/\x12-/viam/api/v1/service/object_manipulation/poseBo\n4com.viam.rdk.proto.api.service.objectmanipulation.v1Z7go.viam.com/rdk/proto/api/service/objectmanipulation/v1b\x06proto3')
_DOGRABREQUEST = DESCRIPTOR.message_types_by_name['DoGrabRequest']
_DOGRABRESPONSE = DESCRIPTOR.message_types_by_name['DoGrabResponse']
_GETPOSEREQUEST = DESCRIPTOR.message_types_by_name['GetPoseRequest']
_GETPOSERESPONSE = DESCRIPTOR.message_types_by_name['GetPoseResponse']
DoGrabRequest = _reflection.GeneratedProtocolMessageType('DoGrabRequest', (_message.Message,), {'DESCRIPTOR': _DOGRABREQUEST, '__module__': 'proto.api.service.objectmanipulation.v1.object_manipulation_pb2'})
_sym_db.RegisterMessage(DoGrabRequest)
DoGrabResponse = _reflection.GeneratedProtocolMessageType('DoGrabResponse', (_message.Message,), {'DESCRIPTOR': _DOGRABRESPONSE, '__module__': 'proto.api.service.objectmanipulation.v1.object_manipulation_pb2'})
_sym_db.RegisterMessage(DoGrabResponse)
GetPoseRequest = _reflection.GeneratedProtocolMessageType('GetPoseRequest', (_message.Message,), {'DESCRIPTOR': _GETPOSEREQUEST, '__module__': 'proto.api.service.objectmanipulation.v1.object_manipulation_pb2'})
_sym_db.RegisterMessage(GetPoseRequest)
GetPoseResponse = _reflection.GeneratedProtocolMessageType('GetPoseResponse', (_message.Message,), {'DESCRIPTOR': _GETPOSERESPONSE, '__module__': 'proto.api.service.objectmanipulation.v1.object_manipulation_pb2'})
_sym_db.RegisterMessage(GetPoseResponse)
_OBJECTMANIPULATIONSERVICE = DESCRIPTOR.services_by_name['ObjectManipulationService']
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n4com.viam.rdk.proto.api.service.objectmanipulation.v1Z7go.viam.com/rdk/proto/api/service/objectmanipulation/v1'
    _OBJECTMANIPULATIONSERVICE.methods_by_name['DoGrab']._options = None
    _OBJECTMANIPULATIONSERVICE.methods_by_name['DoGrab']._serialized_options = b'\x82\xd3\xe4\x93\x022"0/viam/api/v1/service/object_manipulation/do_grab'
    _OBJECTMANIPULATIONSERVICE.methods_by_name['GetPose']._options = None
    _OBJECTMANIPULATIONSERVICE.methods_by_name['GetPose']._serialized_options = b'\x82\xd3\xe4\x93\x02/\x12-/viam/api/v1/service/object_manipulation/pose'
    _DOGRABREQUEST._serialized_start = 175
    _DOGRABREQUEST._serialized_end = 370
    _DOGRABRESPONSE._serialized_start = 372
    _DOGRABRESPONSE._serialized_end = 414
    _GETPOSEREQUEST._serialized_start = 417
    _GETPOSEREQUEST._serialized_end = 552
    _GETPOSERESPONSE._serialized_start = 554
    _GETPOSERESPONSE._serialized_end = 625
    _OBJECTMANIPULATIONSERVICE._serialized_start = 628
    _OBJECTMANIPULATIONSERVICE._serialized_end = 1019