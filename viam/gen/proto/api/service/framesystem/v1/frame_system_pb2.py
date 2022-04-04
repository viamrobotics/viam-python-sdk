"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......proto.api.common.v1 import common_pb2 as proto_dot_api_dot_common_dot_v1_dot_common__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3proto/api/service/framesystem/v1/frame_system.proto\x12 proto.api.service.framesystem.v1\x1a\x1cgoogle/api/annotations.proto\x1a proto/api/common/v1/common.proto"\x8e\x01\n\x06Config\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12Q\n\x14pose_in_parent_frame\x18\x02 \x01(\x0b2 .proto.api.common.v1.PoseInFrameR\x11poseInParentFrame\x12\x1d\n\nmodel_json\x18\x03 \x01(\x0cR\tmodelJson"\x0f\n\rConfigRequest"l\n\x0eConfigResponse\x12Z\n\x14frame_system_configs\x18\x01 \x03(\x0b2(.proto.api.service.framesystem.v1.ConfigR\x12frameSystemConfigs"r\n\x14TransformPoseRequest\x128\n\x06source\x18\x01 \x01(\x0b2 .proto.api.common.v1.PoseInFrameR\x06source\x12 \n\x0bdestination\x18\x02 \x01(\tR\x0bdestination"M\n\x15TransformPoseResponse\x124\n\x04pose\x18\x01 \x01(\x0b2 .proto.api.common.v1.PoseInFrameR\x04pose2\xf1\x02\n\x12FrameSystemService\x12\x9d\x01\n\x06Config\x12/.proto.api.service.framesystem.v1.ConfigRequest\x1a0.proto.api.service.framesystem.v1.ConfigResponse"0\x82\xd3\xe4\x93\x02*\x12(/viam/api/v1/service/frame_system/config\x12\xba\x01\n\rTransformPose\x126.proto.api.service.framesystem.v1.TransformPoseRequest\x1a7.proto.api.service.framesystem.v1.TransformPoseResponse"8\x82\xd3\xe4\x93\x022\x120/viam/api/v1/service/frame_system/transform_poseBa\n-com.viam.rdk.proto.api.service.framesystem.v1Z0go.viam.com/rdk/proto/api/service/framesystem/v1b\x06proto3')
_CONFIG = DESCRIPTOR.message_types_by_name['Config']
_CONFIGREQUEST = DESCRIPTOR.message_types_by_name['ConfigRequest']
_CONFIGRESPONSE = DESCRIPTOR.message_types_by_name['ConfigResponse']
_TRANSFORMPOSEREQUEST = DESCRIPTOR.message_types_by_name['TransformPoseRequest']
_TRANSFORMPOSERESPONSE = DESCRIPTOR.message_types_by_name['TransformPoseResponse']
Config = _reflection.GeneratedProtocolMessageType('Config', (_message.Message,), {'DESCRIPTOR': _CONFIG, '__module__': 'proto.api.service.framesystem.v1.frame_system_pb2'})
_sym_db.RegisterMessage(Config)
ConfigRequest = _reflection.GeneratedProtocolMessageType('ConfigRequest', (_message.Message,), {'DESCRIPTOR': _CONFIGREQUEST, '__module__': 'proto.api.service.framesystem.v1.frame_system_pb2'})
_sym_db.RegisterMessage(ConfigRequest)
ConfigResponse = _reflection.GeneratedProtocolMessageType('ConfigResponse', (_message.Message,), {'DESCRIPTOR': _CONFIGRESPONSE, '__module__': 'proto.api.service.framesystem.v1.frame_system_pb2'})
_sym_db.RegisterMessage(ConfigResponse)
TransformPoseRequest = _reflection.GeneratedProtocolMessageType('TransformPoseRequest', (_message.Message,), {'DESCRIPTOR': _TRANSFORMPOSEREQUEST, '__module__': 'proto.api.service.framesystem.v1.frame_system_pb2'})
_sym_db.RegisterMessage(TransformPoseRequest)
TransformPoseResponse = _reflection.GeneratedProtocolMessageType('TransformPoseResponse', (_message.Message,), {'DESCRIPTOR': _TRANSFORMPOSERESPONSE, '__module__': 'proto.api.service.framesystem.v1.frame_system_pb2'})
_sym_db.RegisterMessage(TransformPoseResponse)
_FRAMESYSTEMSERVICE = DESCRIPTOR.services_by_name['FrameSystemService']
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n-com.viam.rdk.proto.api.service.framesystem.v1Z0go.viam.com/rdk/proto/api/service/framesystem/v1'
    _FRAMESYSTEMSERVICE.methods_by_name['Config']._options = None
    _FRAMESYSTEMSERVICE.methods_by_name['Config']._serialized_options = b'\x82\xd3\xe4\x93\x02*\x12(/viam/api/v1/service/frame_system/config'
    _FRAMESYSTEMSERVICE.methods_by_name['TransformPose']._options = None
    _FRAMESYSTEMSERVICE.methods_by_name['TransformPose']._serialized_options = b'\x82\xd3\xe4\x93\x022\x120/viam/api/v1/service/frame_system/transform_pose'
    _CONFIG._serialized_start = 154
    _CONFIG._serialized_end = 296
    _CONFIGREQUEST._serialized_start = 298
    _CONFIGREQUEST._serialized_end = 313
    _CONFIGRESPONSE._serialized_start = 315
    _CONFIGRESPONSE._serialized_end = 423
    _TRANSFORMPOSEREQUEST._serialized_start = 425
    _TRANSFORMPOSEREQUEST._serialized_end = 539
    _TRANSFORMPOSERESPONSE._serialized_start = 541
    _TRANSFORMPOSERESPONSE._serialized_end = 618
    _FRAMESYSTEMSERVICE._serialized_start = 621
    _FRAMESYSTEMSERVICE._serialized_end = 990