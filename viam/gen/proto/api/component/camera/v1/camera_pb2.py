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
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*proto/api/component/camera/v1/camera.proto\x12\x1dproto.api.component.camera.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x19google/api/httpbody.proto\x1a proto/api/common/v1/common.proto"B\n\x0fGetFrameRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x1b\n\tmime_type\x18\x02 \x01(\tR\x08mimeType"}\n\x10GetFrameResponse\x12\x1b\n\tmime_type\x18\x01 \x01(\tR\x08mimeType\x12\x14\n\x05image\x18\x02 \x01(\x0cR\x05image\x12\x19\n\x08width_px\x18\x03 \x01(\x03R\x07widthPx\x12\x1b\n\theight_px\x18\x04 \x01(\x03R\x08heightPx"E\n\x12RenderFrameRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x1b\n\tmime_type\x18\x02 \x01(\tR\x08mimeType"G\n\x14GetPointCloudRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x1b\n\tmime_type\x18\x02 \x01(\tR\x08mimeType"U\n\x15GetPointCloudResponse\x12\x1b\n\tmime_type\x18\x01 \x01(\tR\x08mimeType\x12\x1f\n\x0bpoint_cloud\x18\x02 \x01(\x0cR\npointCloud"J\n\x07Webcams\x12?\n\x07webcams\x18\x01 \x03(\x0b2%.proto.api.component.camera.v1.WebcamR\x07webcams"\x7f\n\x06Webcam\x12\x14\n\x05label\x18\x01 \x01(\tR\x05label\x12\x16\n\x06status\x18\x02 \x01(\tR\x06status\x12G\n\nproperties\x18\x03 \x03(\x0b2\'.proto.api.component.camera.v1.PropertyR\nproperties"F\n\x08Property\x12:\n\x05video\x18\x01 \x01(\x0b2$.proto.api.component.camera.v1.VideoR\x05video"X\n\x05Video\x12\x14\n\x05width\x18\x01 \x01(\x05R\x05width\x12\x16\n\x06height\x18\x02 \x01(\x05R\x06height\x12!\n\x0cframe_format\x18\x03 \x01(\tR\x0bframeFormat2\xfc\x03\n\rCameraService\x12\x9f\x01\n\x08GetFrame\x12..proto.api.component.camera.v1.GetFrameRequest\x1a/.proto.api.component.camera.v1.GetFrameResponse"2\x82\xd3\xe4\x93\x02,\x12*/viam/api/v1/component/camera/{name}/frame\x12\x91\x01\n\x0bRenderFrame\x121.proto.api.component.camera.v1.RenderFrameRequest\x1a\x14.google.api.HttpBody"9\x82\xd3\xe4\x93\x023\x121/viam/api/v1/component/camera/{name}/render_frame\x12\xb4\x01\n\rGetPointCloud\x123.proto.api.component.camera.v1.GetPointCloudRequest\x1a4.proto.api.component.camera.v1.GetPointCloudResponse"8\x82\xd3\xe4\x93\x022\x120/viam/api/v1/component/camera/{name}/point_cloudB[\n*com.viam.rdk.proto.api.component.camera.v1Z-go.viam.com/rdk/proto/api/component/camera/v1b\x06proto3')
_GETFRAMEREQUEST = DESCRIPTOR.message_types_by_name['GetFrameRequest']
_GETFRAMERESPONSE = DESCRIPTOR.message_types_by_name['GetFrameResponse']
_RENDERFRAMEREQUEST = DESCRIPTOR.message_types_by_name['RenderFrameRequest']
_GETPOINTCLOUDREQUEST = DESCRIPTOR.message_types_by_name['GetPointCloudRequest']
_GETPOINTCLOUDRESPONSE = DESCRIPTOR.message_types_by_name['GetPointCloudResponse']
_WEBCAMS = DESCRIPTOR.message_types_by_name['Webcams']
_WEBCAM = DESCRIPTOR.message_types_by_name['Webcam']
_PROPERTY = DESCRIPTOR.message_types_by_name['Property']
_VIDEO = DESCRIPTOR.message_types_by_name['Video']
GetFrameRequest = _reflection.GeneratedProtocolMessageType('GetFrameRequest', (_message.Message,), {'DESCRIPTOR': _GETFRAMEREQUEST, '__module__': 'proto.api.component.camera.v1.camera_pb2', '__doc__': 'Attributes:\n      name:\n          Name of a camera\n      mime_type:\n          Requested MIME type of response\n  '})
_sym_db.RegisterMessage(GetFrameRequest)
GetFrameResponse = _reflection.GeneratedProtocolMessageType('GetFrameResponse', (_message.Message,), {'DESCRIPTOR': _GETFRAMERESPONSE, '__module__': 'proto.api.component.camera.v1.camera_pb2', '__doc__': 'Attributes:\n      mime_type:\n          Actual MIME type of response\n      image:\n          Frame in bytes\n      width_px:\n          Width of frame in px\n      height_px:\n          Height of frame in px\n  '})
_sym_db.RegisterMessage(GetFrameResponse)
RenderFrameRequest = _reflection.GeneratedProtocolMessageType('RenderFrameRequest', (_message.Message,), {'DESCRIPTOR': _RENDERFRAMEREQUEST, '__module__': 'proto.api.component.camera.v1.camera_pb2', '__doc__': 'Attributes:\n      name:\n          Name of a camera\n      mime_type:\n          Requested MIME type of response\n  '})
_sym_db.RegisterMessage(RenderFrameRequest)
GetPointCloudRequest = _reflection.GeneratedProtocolMessageType('GetPointCloudRequest', (_message.Message,), {'DESCRIPTOR': _GETPOINTCLOUDREQUEST, '__module__': 'proto.api.component.camera.v1.camera_pb2', '__doc__': 'Attributes:\n      name:\n          Name of a camera\n      mime_type:\n          Requested MIME type of response\n  '})
_sym_db.RegisterMessage(GetPointCloudRequest)
GetPointCloudResponse = _reflection.GeneratedProtocolMessageType('GetPointCloudResponse', (_message.Message,), {'DESCRIPTOR': _GETPOINTCLOUDRESPONSE, '__module__': 'proto.api.component.camera.v1.camera_pb2', '__doc__': 'Attributes:\n      mime_type:\n          Actual MIME type of response\n      point_cloud:\n          Frame in bytes\n  '})
_sym_db.RegisterMessage(GetPointCloudResponse)
Webcams = _reflection.GeneratedProtocolMessageType('Webcams', (_message.Message,), {'DESCRIPTOR': _WEBCAMS, '__module__': 'proto.api.component.camera.v1.camera_pb2'})
_sym_db.RegisterMessage(Webcams)
Webcam = _reflection.GeneratedProtocolMessageType('Webcam', (_message.Message,), {'DESCRIPTOR': _WEBCAM, '__module__': 'proto.api.component.camera.v1.camera_pb2', '__doc__': 'Attributes:\n      label:\n          Camera driver label\n      status:\n          Camera driver status\n      properties:\n          Camera properties\n  '})
_sym_db.RegisterMessage(Webcam)
Property = _reflection.GeneratedProtocolMessageType('Property', (_message.Message,), {'DESCRIPTOR': _PROPERTY, '__module__': 'proto.api.component.camera.v1.camera_pb2', '__doc__': 'Attributes:\n      video:\n          Camera video properties\n  '})
_sym_db.RegisterMessage(Property)
Video = _reflection.GeneratedProtocolMessageType('Video', (_message.Message,), {'DESCRIPTOR': _VIDEO, '__module__': 'proto.api.component.camera.v1.camera_pb2', '__doc__': 'Attributes:\n      width:\n          Video resolution width\n      height:\n          Video resolution height\n      frame_format:\n          Video frame format\n  '})
_sym_db.RegisterMessage(Video)
_CAMERASERVICE = DESCRIPTOR.services_by_name['CameraService']
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n*com.viam.rdk.proto.api.component.camera.v1Z-go.viam.com/rdk/proto/api/component/camera/v1'
    _CAMERASERVICE.methods_by_name['GetFrame']._options = None
    _CAMERASERVICE.methods_by_name['GetFrame']._serialized_options = b'\x82\xd3\xe4\x93\x02,\x12*/viam/api/v1/component/camera/{name}/frame'
    _CAMERASERVICE.methods_by_name['RenderFrame']._options = None
    _CAMERASERVICE.methods_by_name['RenderFrame']._serialized_options = b'\x82\xd3\xe4\x93\x023\x121/viam/api/v1/component/camera/{name}/render_frame'
    _CAMERASERVICE.methods_by_name['GetPointCloud']._options = None
    _CAMERASERVICE.methods_by_name['GetPointCloud']._serialized_options = b'\x82\xd3\xe4\x93\x022\x120/viam/api/v1/component/camera/{name}/point_cloud'
    _GETFRAMEREQUEST._serialized_start = 168
    _GETFRAMEREQUEST._serialized_end = 234
    _GETFRAMERESPONSE._serialized_start = 236
    _GETFRAMERESPONSE._serialized_end = 361
    _RENDERFRAMEREQUEST._serialized_start = 363
    _RENDERFRAMEREQUEST._serialized_end = 432
    _GETPOINTCLOUDREQUEST._serialized_start = 434
    _GETPOINTCLOUDREQUEST._serialized_end = 505
    _GETPOINTCLOUDRESPONSE._serialized_start = 507
    _GETPOINTCLOUDRESPONSE._serialized_end = 592
    _WEBCAMS._serialized_start = 594
    _WEBCAMS._serialized_end = 668
    _WEBCAM._serialized_start = 670
    _WEBCAM._serialized_end = 797
    _PROPERTY._serialized_start = 799
    _PROPERTY._serialized_end = 869
    _VIDEO._serialized_start = 871
    _VIDEO._serialized_end = 959
    _CAMERASERVICE._serialized_start = 962
    _CAMERASERVICE._serialized_end = 1470