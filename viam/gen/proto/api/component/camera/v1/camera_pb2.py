"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import httpbody_pb2 as google_dot_api_dot_httpbody__pb2
from ......proto.api.common.v1 import common_pb2 as proto_dot_api_dot_common_dot_v1_dot_common__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*proto/api/component/camera/v1/camera.proto\x12\x1dproto.api.component.camera.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x19google/api/httpbody.proto\x1a proto/api/common/v1/common.proto"B\n\x0fGetFrameRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x1b\n\tmime_type\x18\x02 \x01(\tR\x08mimeType"}\n\x10GetFrameResponse\x12\x1b\n\tmime_type\x18\x01 \x01(\tR\x08mimeType\x12\x14\n\x05frame\x18\x02 \x01(\x0cR\x05frame\x12\x19\n\x08width_px\x18\x03 \x01(\x03R\x07widthPx\x12\x1b\n\theight_px\x18\x04 \x01(\x03R\x08heightPx"E\n\x12RenderFrameRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x1b\n\tmime_type\x18\x02 \x01(\tR\x08mimeType"G\n\x14GetPointCloudRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x1b\n\tmime_type\x18\x02 \x01(\tR\x08mimeType"J\n\x15GetPointCloudResponse\x12\x1b\n\tmime_type\x18\x01 \x01(\tR\x08mimeType\x12\x14\n\x05frame\x18\x02 \x01(\x0cR\x05frame2\xed\x03\n\rCameraService\x12\x9a\x01\n\x08GetFrame\x12..proto.api.component.camera.v1.GetFrameRequest\x1a/.proto.api.component.camera.v1.GetFrameResponse"-\x82\xd3\xe4\x93\x02\'\x12%/api/v1/component/camera/{name}/frame\x12\x8c\x01\n\x0bRenderFrame\x121.proto.api.component.camera.v1.RenderFrameRequest\x1a\x14.google.api.HttpBody"4\x82\xd3\xe4\x93\x02.\x12,/api/v1/component/camera/{name}/render_frame\x12\xaf\x01\n\rGetPointCloud\x123.proto.api.component.camera.v1.GetPointCloudRequest\x1a4.proto.api.component.camera.v1.GetPointCloudResponse"3\x82\xd3\xe4\x93\x02-\x12+/api/v1/component/camera/{name}/point_cloudB[\n*com.viam.rdk.proto.api.component.camera.v1Z-go.viam.com/rdk/proto/api/component/camera/v1b\x06proto3')
_GETFRAMEREQUEST = DESCRIPTOR.message_types_by_name['GetFrameRequest']
_GETFRAMERESPONSE = DESCRIPTOR.message_types_by_name['GetFrameResponse']
_RENDERFRAMEREQUEST = DESCRIPTOR.message_types_by_name['RenderFrameRequest']
_GETPOINTCLOUDREQUEST = DESCRIPTOR.message_types_by_name['GetPointCloudRequest']
_GETPOINTCLOUDRESPONSE = DESCRIPTOR.message_types_by_name['GetPointCloudResponse']
GetFrameRequest = _reflection.GeneratedProtocolMessageType('GetFrameRequest', (_message.Message,), {'DESCRIPTOR': _GETFRAMEREQUEST, '__module__': 'proto.api.component.camera.v1.camera_pb2'})
_sym_db.RegisterMessage(GetFrameRequest)
GetFrameResponse = _reflection.GeneratedProtocolMessageType('GetFrameResponse', (_message.Message,), {'DESCRIPTOR': _GETFRAMERESPONSE, '__module__': 'proto.api.component.camera.v1.camera_pb2'})
_sym_db.RegisterMessage(GetFrameResponse)
RenderFrameRequest = _reflection.GeneratedProtocolMessageType('RenderFrameRequest', (_message.Message,), {'DESCRIPTOR': _RENDERFRAMEREQUEST, '__module__': 'proto.api.component.camera.v1.camera_pb2'})
_sym_db.RegisterMessage(RenderFrameRequest)
GetPointCloudRequest = _reflection.GeneratedProtocolMessageType('GetPointCloudRequest', (_message.Message,), {'DESCRIPTOR': _GETPOINTCLOUDREQUEST, '__module__': 'proto.api.component.camera.v1.camera_pb2'})
_sym_db.RegisterMessage(GetPointCloudRequest)
GetPointCloudResponse = _reflection.GeneratedProtocolMessageType('GetPointCloudResponse', (_message.Message,), {'DESCRIPTOR': _GETPOINTCLOUDRESPONSE, '__module__': 'proto.api.component.camera.v1.camera_pb2'})
_sym_db.RegisterMessage(GetPointCloudResponse)
_CAMERASERVICE = DESCRIPTOR.services_by_name['CameraService']
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n*com.viam.rdk.proto.api.component.camera.v1Z-go.viam.com/rdk/proto/api/component/camera/v1'
    _CAMERASERVICE.methods_by_name['GetFrame']._options = None
    _CAMERASERVICE.methods_by_name['GetFrame']._serialized_options = b"\x82\xd3\xe4\x93\x02'\x12%/api/v1/component/camera/{name}/frame"
    _CAMERASERVICE.methods_by_name['RenderFrame']._options = None
    _CAMERASERVICE.methods_by_name['RenderFrame']._serialized_options = b'\x82\xd3\xe4\x93\x02.\x12,/api/v1/component/camera/{name}/render_frame'
    _CAMERASERVICE.methods_by_name['GetPointCloud']._options = None
    _CAMERASERVICE.methods_by_name['GetPointCloud']._serialized_options = b'\x82\xd3\xe4\x93\x02-\x12+/api/v1/component/camera/{name}/point_cloud'
    _GETFRAMEREQUEST._serialized_start = 168
    _GETFRAMEREQUEST._serialized_end = 234
    _GETFRAMERESPONSE._serialized_start = 236
    _GETFRAMERESPONSE._serialized_end = 361
    _RENDERFRAMEREQUEST._serialized_start = 363
    _RENDERFRAMEREQUEST._serialized_end = 432
    _GETPOINTCLOUDREQUEST._serialized_start = 434
    _GETPOINTCLOUDREQUEST._serialized_end = 505
    _GETPOINTCLOUDRESPONSE._serialized_start = 507
    _GETPOINTCLOUDRESPONSE._serialized_end = 581
    _CAMERASERVICE._serialized_start = 584
    _CAMERASERVICE._serialized_end = 1077