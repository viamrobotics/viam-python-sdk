"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....common.v1 import common_pb2 as common_dot_v1_dot_common__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import httpbody_pb2 as google_dot_api_dot_httpbody__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n component/camera/v1/camera.proto\x12\x18viam.component.camera.v1\x1a\x16common/v1/common.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x19google/api/httpbody.proto"B\n\x0fGetImageRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x1b\n\tmime_type\x18\x02 \x01(\tR\x08mimeType"E\n\x10GetImageResponse\x12\x1b\n\tmime_type\x18\x01 \x01(\tR\x08mimeType\x12\x14\n\x05image\x18\x02 \x01(\x0cR\x05image"E\n\x12RenderFrameRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x1b\n\tmime_type\x18\x02 \x01(\tR\x08mimeType"G\n\x14GetPointCloudRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x1b\n\tmime_type\x18\x02 \x01(\tR\x08mimeType"U\n\x15GetPointCloudResponse\x12\x1b\n\tmime_type\x18\x01 \x01(\tR\x08mimeType\x12\x1f\n\x0bpoint_cloud\x18\x02 \x01(\x0cR\npointCloud"*\n\x14GetPropertiesRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name"\x81\x02\n\x15GetPropertiesResponse\x12!\n\x0csupports_pcd\x18\x01 \x01(\x08R\x0bsupportsPcd\x12`\n\x14intrinsic_parameters\x18\x02 \x01(\x0b2-.viam.component.camera.v1.IntrinsicParametersR\x13intrinsicParameters\x12c\n\x15distortion_parameters\x18\x03 \x01(\x0b2..viam.component.camera.v1.DistortionParametersR\x14distortionParameters"E\n\x07Webcams\x12:\n\x07webcams\x18\x01 \x03(\x0b2 .viam.component.camera.v1.WebcamR\x07webcams"\x9e\x01\n\x06Webcam\x12\x14\n\x05label\x18\x01 \x01(\tR\x05label\x12\x16\n\x06status\x18\x02 \x01(\tR\x06status\x12B\n\nproperties\x18\x03 \x03(\x0b2".viam.component.camera.v1.PropertyR\nproperties\x12\x12\n\x04name\x18\x04 \x01(\tR\x04name\x12\x0e\n\x02id\x18\x05 \x01(\tR\x02id"e\n\x08Property\x12\x19\n\x08width_px\x18\x01 \x01(\x05R\x07widthPx\x12\x1b\n\theight_px\x18\x02 \x01(\x05R\x08heightPx\x12!\n\x0cframe_format\x18\x03 \x01(\tR\x0bframeFormat"\xc9\x01\n\x13IntrinsicParameters\x12\x19\n\x08width_px\x18\x01 \x01(\rR\x07widthPx\x12\x1b\n\theight_px\x18\x02 \x01(\rR\x08heightPx\x12\x1c\n\nfocal_x_px\x18\x03 \x01(\x01R\x08focalXPx\x12\x1c\n\nfocal_y_px\x18\x04 \x01(\x01R\x08focalYPx\x12\x1e\n\x0bcenter_x_px\x18\x05 \x01(\x01R\tcenterXPx\x12\x1e\n\x0bcenter_y_px\x18\x06 \x01(\x01R\tcenterYPx"L\n\x14DistortionParameters\x12\x14\n\x05model\x18\x01 \x01(\tR\x05model\x12\x1e\n\nparameters\x18\x02 \x03(\x01R\nparameters2\x9b\x06\n\rCameraService\x12\x95\x01\n\x08GetImage\x12).viam.component.camera.v1.GetImageRequest\x1a*.viam.component.camera.v1.GetImageResponse"2\x82\xd3\xe4\x93\x02,\x12*/viam/api/v1/component/camera/{name}/image\x12\x8c\x01\n\x0bRenderFrame\x12,.viam.component.camera.v1.RenderFrameRequest\x1a\x14.google.api.HttpBody"9\x82\xd3\xe4\x93\x023\x121/viam/api/v1/component/camera/{name}/render_frame\x12\xaa\x01\n\rGetPointCloud\x12..viam.component.camera.v1.GetPointCloudRequest\x1a/.viam.component.camera.v1.GetPointCloudResponse"8\x82\xd3\xe4\x93\x022\x120/viam/api/v1/component/camera/{name}/point_cloud\x12\xa9\x01\n\rGetProperties\x12..viam.component.camera.v1.GetPropertiesRequest\x1a/.viam.component.camera.v1.GetPropertiesResponse"7\x82\xd3\xe4\x93\x021\x12//viam/api/v1/component/camera/{name}/properties\x12\x89\x01\n\tDoCommand\x12 .viam.common.v1.DoCommandRequest\x1a!.viam.common.v1.DoCommandResponse"7\x82\xd3\xe4\x93\x021"//viam/api/v1/component/camera/{name}/do_commandBC\n\x1ccom.viam.component.camera.v1Z#go.viam.com/api/component/camera/v1b\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'component.camera.v1.camera_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n\x1ccom.viam.component.camera.v1Z#go.viam.com/api/component/camera/v1'
    _CAMERASERVICE.methods_by_name['GetImage']._options = None
    _CAMERASERVICE.methods_by_name['GetImage']._serialized_options = b'\x82\xd3\xe4\x93\x02,\x12*/viam/api/v1/component/camera/{name}/image'
    _CAMERASERVICE.methods_by_name['RenderFrame']._options = None
    _CAMERASERVICE.methods_by_name['RenderFrame']._serialized_options = b'\x82\xd3\xe4\x93\x023\x121/viam/api/v1/component/camera/{name}/render_frame'
    _CAMERASERVICE.methods_by_name['GetPointCloud']._options = None
    _CAMERASERVICE.methods_by_name['GetPointCloud']._serialized_options = b'\x82\xd3\xe4\x93\x022\x120/viam/api/v1/component/camera/{name}/point_cloud'
    _CAMERASERVICE.methods_by_name['GetProperties']._options = None
    _CAMERASERVICE.methods_by_name['GetProperties']._serialized_options = b'\x82\xd3\xe4\x93\x021\x12//viam/api/v1/component/camera/{name}/properties'
    _CAMERASERVICE.methods_by_name['DoCommand']._options = None
    _CAMERASERVICE.methods_by_name['DoCommand']._serialized_options = b'\x82\xd3\xe4\x93\x021"//viam/api/v1/component/camera/{name}/do_command'
    _GETIMAGEREQUEST._serialized_start = 143
    _GETIMAGEREQUEST._serialized_end = 209
    _GETIMAGERESPONSE._serialized_start = 211
    _GETIMAGERESPONSE._serialized_end = 280
    _RENDERFRAMEREQUEST._serialized_start = 282
    _RENDERFRAMEREQUEST._serialized_end = 351
    _GETPOINTCLOUDREQUEST._serialized_start = 353
    _GETPOINTCLOUDREQUEST._serialized_end = 424
    _GETPOINTCLOUDRESPONSE._serialized_start = 426
    _GETPOINTCLOUDRESPONSE._serialized_end = 511
    _GETPROPERTIESREQUEST._serialized_start = 513
    _GETPROPERTIESREQUEST._serialized_end = 555
    _GETPROPERTIESRESPONSE._serialized_start = 558
    _GETPROPERTIESRESPONSE._serialized_end = 815
    _WEBCAMS._serialized_start = 817
    _WEBCAMS._serialized_end = 886
    _WEBCAM._serialized_start = 889
    _WEBCAM._serialized_end = 1047
    _PROPERTY._serialized_start = 1049
    _PROPERTY._serialized_end = 1150
    _INTRINSICPARAMETERS._serialized_start = 1153
    _INTRINSICPARAMETERS._serialized_end = 1354
    _DISTORTIONPARAMETERS._serialized_start = 1356
    _DISTORTIONPARAMETERS._serialized_end = 1432
    _CAMERASERVICE._serialized_start = 1435
    _CAMERASERVICE._serialized_end = 2230