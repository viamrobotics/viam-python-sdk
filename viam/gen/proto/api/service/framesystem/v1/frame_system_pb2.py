"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......proto.api.common.v1 import common_pb2 as proto_dot_api_dot_common_dot_v1_dot_common__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3proto/api/service/framesystem/v1/frame_system.proto\x12 proto.api.service.framesystem.v1\x1a\x1cgoogle/api/annotations.proto\x1a proto/api/common/v1/common.proto"T\n\x0bFrameConfig\x12\x16\n\x06parent\x18\x01 \x01(\tR\x06parent\x12-\n\x04pose\x18\x02 \x01(\x0b2\x19.proto.api.common.v1.PoseR\x04pose"\x8d\x01\n\x06Config\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12P\n\x0cframe_config\x18\x02 \x01(\x0b2-.proto.api.service.framesystem.v1.FrameConfigR\x0bframeConfig\x12\x1d\n\nmodel_json\x18\x03 \x01(\x0cR\tmodelJson"\x0f\n\rConfigRequest"l\n\x0eConfigResponse\x12Z\n\x14frame_system_configs\x18\x01 \x03(\x0b2(.proto.api.service.framesystem.v1.ConfigR\x12frameSystemConfigs2\xaf\x01\n\x12FrameSystemService\x12\x98\x01\n\x06Config\x12/.proto.api.service.framesystem.v1.ConfigRequest\x1a0.proto.api.service.framesystem.v1.ConfigResponse"+\x82\xd3\xe4\x93\x02%\x12#/api/v1/service/frame_system/configBI\n!com.viam.rdk.proto.api.service.v1Z$go.viam.com/rdk/proto/api/service/v1b\x06proto3')
_FRAMECONFIG = DESCRIPTOR.message_types_by_name['FrameConfig']
_CONFIG = DESCRIPTOR.message_types_by_name['Config']
_CONFIGREQUEST = DESCRIPTOR.message_types_by_name['ConfigRequest']
_CONFIGRESPONSE = DESCRIPTOR.message_types_by_name['ConfigResponse']
FrameConfig = _reflection.GeneratedProtocolMessageType('FrameConfig', (_message.Message,), {'DESCRIPTOR': _FRAMECONFIG, '__module__': 'proto.api.service.framesystem.v1.frame_system_pb2'})
_sym_db.RegisterMessage(FrameConfig)
Config = _reflection.GeneratedProtocolMessageType('Config', (_message.Message,), {'DESCRIPTOR': _CONFIG, '__module__': 'proto.api.service.framesystem.v1.frame_system_pb2'})
_sym_db.RegisterMessage(Config)
ConfigRequest = _reflection.GeneratedProtocolMessageType('ConfigRequest', (_message.Message,), {'DESCRIPTOR': _CONFIGREQUEST, '__module__': 'proto.api.service.framesystem.v1.frame_system_pb2'})
_sym_db.RegisterMessage(ConfigRequest)
ConfigResponse = _reflection.GeneratedProtocolMessageType('ConfigResponse', (_message.Message,), {'DESCRIPTOR': _CONFIGRESPONSE, '__module__': 'proto.api.service.framesystem.v1.frame_system_pb2'})
_sym_db.RegisterMessage(ConfigResponse)
_FRAMESYSTEMSERVICE = DESCRIPTOR.services_by_name['FrameSystemService']
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n!com.viam.rdk.proto.api.service.v1Z$go.viam.com/rdk/proto/api/service/v1'
    _FRAMESYSTEMSERVICE.methods_by_name['Config']._options = None
    _FRAMESYSTEMSERVICE.methods_by_name['Config']._serialized_options = b'\x82\xd3\xe4\x93\x02%\x12#/api/v1/service/frame_system/config'
    _FRAMECONFIG._serialized_start = 153
    _FRAMECONFIG._serialized_end = 237
    _CONFIG._serialized_start = 240
    _CONFIG._serialized_end = 381
    _CONFIGREQUEST._serialized_start = 383
    _CONFIGREQUEST._serialized_end = 398
    _CONFIGRESPONSE._serialized_start = 400
    _CONFIGRESPONSE._serialized_end = 508
    _FRAMESYSTEMSERVICE._serialized_start = 511
    _FRAMESYSTEMSERVICE._serialized_end = 686