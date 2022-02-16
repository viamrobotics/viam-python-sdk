"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....proto.api.common.v1 import common_pb2 as proto_dot_api_dot_common_dot_v1_dot_common__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'proto/api/service/v1/frame_system.proto\x12\x14proto.api.service.v1\x1a\x1cgoogle/api/annotations.proto\x1a proto/api/common/v1/common.proto"f\n\x1dFrameSystemServiceFrameConfig\x12\x16\n\x06parent\x18\x01 \x01(\tR\x06parent\x12-\n\x04pose\x18\x02 \x01(\x0b2\x19.proto.api.common.v1.PoseR\x04pose"\xa5\x01\n\x18FrameSystemServiceConfig\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12V\n\x0cframe_config\x18\x02 \x01(\x0b23.proto.api.service.v1.FrameSystemServiceFrameConfigR\x0bframeConfig\x12\x1d\n\nmodel_json\x18\x03 \x01(\x0cR\tmodelJson"!\n\x1fFrameSystemServiceConfigRequest"\x84\x01\n FrameSystemServiceConfigResponse\x12`\n\x14frame_system_configs\x18\x01 \x03(\x0b2..proto.api.service.v1.FrameSystemServiceConfigR\x12frameSystemConfigs2\xbb\x01\n\x12FrameSystemService\x12\xa4\x01\n\x06Config\x125.proto.api.service.v1.FrameSystemServiceConfigRequest\x1a6.proto.api.service.v1.FrameSystemServiceConfigResponse"+\x82\xd3\xe4\x93\x02%\x12#/api/v1/service/frame_system/configBI\n!com.viam.rdk.proto.api.service.v1Z$go.viam.com/rdk/proto/api/service/v1b\x06proto3')
_FRAMESYSTEMSERVICEFRAMECONFIG = DESCRIPTOR.message_types_by_name['FrameSystemServiceFrameConfig']
_FRAMESYSTEMSERVICECONFIG = DESCRIPTOR.message_types_by_name['FrameSystemServiceConfig']
_FRAMESYSTEMSERVICECONFIGREQUEST = DESCRIPTOR.message_types_by_name['FrameSystemServiceConfigRequest']
_FRAMESYSTEMSERVICECONFIGRESPONSE = DESCRIPTOR.message_types_by_name['FrameSystemServiceConfigResponse']
FrameSystemServiceFrameConfig = _reflection.GeneratedProtocolMessageType('FrameSystemServiceFrameConfig', (_message.Message,), {'DESCRIPTOR': _FRAMESYSTEMSERVICEFRAMECONFIG, '__module__': 'proto.api.service.v1.frame_system_pb2'})
_sym_db.RegisterMessage(FrameSystemServiceFrameConfig)
FrameSystemServiceConfig = _reflection.GeneratedProtocolMessageType('FrameSystemServiceConfig', (_message.Message,), {'DESCRIPTOR': _FRAMESYSTEMSERVICECONFIG, '__module__': 'proto.api.service.v1.frame_system_pb2'})
_sym_db.RegisterMessage(FrameSystemServiceConfig)
FrameSystemServiceConfigRequest = _reflection.GeneratedProtocolMessageType('FrameSystemServiceConfigRequest', (_message.Message,), {'DESCRIPTOR': _FRAMESYSTEMSERVICECONFIGREQUEST, '__module__': 'proto.api.service.v1.frame_system_pb2'})
_sym_db.RegisterMessage(FrameSystemServiceConfigRequest)
FrameSystemServiceConfigResponse = _reflection.GeneratedProtocolMessageType('FrameSystemServiceConfigResponse', (_message.Message,), {'DESCRIPTOR': _FRAMESYSTEMSERVICECONFIGRESPONSE, '__module__': 'proto.api.service.v1.frame_system_pb2'})
_sym_db.RegisterMessage(FrameSystemServiceConfigResponse)
_FRAMESYSTEMSERVICE = DESCRIPTOR.services_by_name['FrameSystemService']
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n!com.viam.rdk.proto.api.service.v1Z$go.viam.com/rdk/proto/api/service/v1'
    _FRAMESYSTEMSERVICE.methods_by_name['Config']._options = None
    _FRAMESYSTEMSERVICE.methods_by_name['Config']._serialized_options = b'\x82\xd3\xe4\x93\x02%\x12#/api/v1/service/frame_system/config'
    _FRAMESYSTEMSERVICEFRAMECONFIG._serialized_start = 129
    _FRAMESYSTEMSERVICEFRAMECONFIG._serialized_end = 231
    _FRAMESYSTEMSERVICECONFIG._serialized_start = 234
    _FRAMESYSTEMSERVICECONFIG._serialized_end = 399
    _FRAMESYSTEMSERVICECONFIGREQUEST._serialized_start = 401
    _FRAMESYSTEMSERVICECONFIGREQUEST._serialized_end = 434
    _FRAMESYSTEMSERVICECONFIGRESPONSE._serialized_start = 437
    _FRAMESYSTEMSERVICECONFIGRESPONSE._serialized_end = 569
    _FRAMESYSTEMSERVICE._serialized_start = 572
    _FRAMESYSTEMSERVICE._serialized_end = 759