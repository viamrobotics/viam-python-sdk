# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/api/component/v1/camera.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import httpbody_pb2 as google_dot_api_dot_httpbody__pb2
from proto.api.common.v1 import common_pb2 as proto_dot_api_dot_common_dot_v1_dot_common__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#proto/api/component/v1/camera.proto\x12\x16proto.api.component.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x19google/api/httpbody.proto\x1a proto/api/common/v1/common.proto\"O\n\x1c\x43\x61meraServiceGetFrameRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x1b\n\tmime_type\x18\x02 \x01(\tR\x08mimeType\"\x8a\x01\n\x1d\x43\x61meraServiceGetFrameResponse\x12\x1b\n\tmime_type\x18\x01 \x01(\tR\x08mimeType\x12\x14\n\x05\x66rame\x18\x02 \x01(\x0cR\x05\x66rame\x12\x19\n\x08width_px\x18\x03 \x01(\x03R\x07widthPx\x12\x1b\n\theight_px\x18\x04 \x01(\x03R\x08heightPx\"R\n\x1f\x43\x61meraServiceRenderFrameRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x1b\n\tmime_type\x18\x02 \x01(\tR\x08mimeType\"T\n!CameraServiceGetPointCloudRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x1b\n\tmime_type\x18\x02 \x01(\tR\x08mimeType\"W\n\"CameraServiceGetPointCloudResponse\x12\x1b\n\tmime_type\x18\x01 \x01(\tR\x08mimeType\x12\x14\n\x05\x66rame\x18\x02 \x01(\x0cR\x05\x66rame\"\xef\x01\n(CameraServiceGetObjectPointCloudsRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x1b\n\tmime_type\x18\x02 \x01(\tR\x08mimeType\x12-\n\x13min_points_in_plane\x18\x03 \x01(\x03R\x10minPointsInPlane\x12\x31\n\x15min_points_in_segment\x18\x04 \x01(\x03R\x12minPointsInSegment\x12\x30\n\x14\x63lustering_radius_mm\x18\x05 \x01(\x01R\x12\x63lusteringRadiusMm\"\x8c\x01\n)CameraServiceGetObjectPointCloudsResponse\x12\x1b\n\tmime_type\x18\x01 \x01(\tR\x08mimeType\x12\x42\n\x07objects\x18\x02 \x03(\x0b\x32(.proto.api.component.v1.PointCloudObjectR\x07objects\"\xc4\x01\n\x10PointCloudObject\x12\x14\n\x05\x66rame\x18\x01 \x01(\x0cR\x05\x66rame\x12P\n\x15\x63\x65nter_coordinates_mm\x18\x02 \x01(\x0b\x32\x1c.proto.api.common.v1.Vector3R\x13\x63\x65nterCoordinatesMm\x12H\n\x0f\x62ounding_box_mm\x18\x03 \x01(\x0b\x32 .proto.api.common.v1.BoxGeometryR\rboundingBoxMm2\xe6\x05\n\rCameraService\x12\xa6\x01\n\x08GetFrame\x12\x34.proto.api.component.v1.CameraServiceGetFrameRequest\x1a\x35.proto.api.component.v1.CameraServiceGetFrameResponse\"-\x82\xd3\xe4\x93\x02\'\x12%/api/v1/component/camera/{name}/frame\x12\x92\x01\n\x0bRenderFrame\x12\x37.proto.api.component.v1.CameraServiceRenderFrameRequest\x1a\x14.google.api.HttpBody\"4\x82\xd3\xe4\x93\x02.\x12,/api/v1/component/camera/{name}/render_frame\x12\xbb\x01\n\rGetPointCloud\x12\x39.proto.api.component.v1.CameraServiceGetPointCloudRequest\x1a:.proto.api.component.v1.CameraServiceGetPointCloudResponse\"3\x82\xd3\xe4\x93\x02-\x12+/api/v1/component/camera/{name}/point_cloud\x12\xd8\x01\n\x14GetObjectPointClouds\x12@.proto.api.component.v1.CameraServiceGetObjectPointCloudsRequest\x1a\x41.proto.api.component.v1.CameraServiceGetObjectPointCloudsResponse\";\x82\xd3\xe4\x93\x02\x35\x12\x33/api/v1/component/camera/{name}/object_point_cloudsBM\n#com.viam.rdk.proto.api.component.v1Z&go.viam.com/rdk/proto/api/component/v1b\x06proto3')



_CAMERASERVICEGETFRAMEREQUEST = DESCRIPTOR.message_types_by_name['CameraServiceGetFrameRequest']
_CAMERASERVICEGETFRAMERESPONSE = DESCRIPTOR.message_types_by_name['CameraServiceGetFrameResponse']
_CAMERASERVICERENDERFRAMEREQUEST = DESCRIPTOR.message_types_by_name['CameraServiceRenderFrameRequest']
_CAMERASERVICEGETPOINTCLOUDREQUEST = DESCRIPTOR.message_types_by_name['CameraServiceGetPointCloudRequest']
_CAMERASERVICEGETPOINTCLOUDRESPONSE = DESCRIPTOR.message_types_by_name['CameraServiceGetPointCloudResponse']
_CAMERASERVICEGETOBJECTPOINTCLOUDSREQUEST = DESCRIPTOR.message_types_by_name['CameraServiceGetObjectPointCloudsRequest']
_CAMERASERVICEGETOBJECTPOINTCLOUDSRESPONSE = DESCRIPTOR.message_types_by_name['CameraServiceGetObjectPointCloudsResponse']
_POINTCLOUDOBJECT = DESCRIPTOR.message_types_by_name['PointCloudObject']
CameraServiceGetFrameRequest = _reflection.GeneratedProtocolMessageType('CameraServiceGetFrameRequest', (_message.Message,), {
  'DESCRIPTOR' : _CAMERASERVICEGETFRAMEREQUEST,
  '__module__' : 'proto.api.component.v1.camera_pb2'
  # @@protoc_insertion_point(class_scope:proto.api.component.v1.CameraServiceGetFrameRequest)
  })
_sym_db.RegisterMessage(CameraServiceGetFrameRequest)

CameraServiceGetFrameResponse = _reflection.GeneratedProtocolMessageType('CameraServiceGetFrameResponse', (_message.Message,), {
  'DESCRIPTOR' : _CAMERASERVICEGETFRAMERESPONSE,
  '__module__' : 'proto.api.component.v1.camera_pb2'
  # @@protoc_insertion_point(class_scope:proto.api.component.v1.CameraServiceGetFrameResponse)
  })
_sym_db.RegisterMessage(CameraServiceGetFrameResponse)

CameraServiceRenderFrameRequest = _reflection.GeneratedProtocolMessageType('CameraServiceRenderFrameRequest', (_message.Message,), {
  'DESCRIPTOR' : _CAMERASERVICERENDERFRAMEREQUEST,
  '__module__' : 'proto.api.component.v1.camera_pb2'
  # @@protoc_insertion_point(class_scope:proto.api.component.v1.CameraServiceRenderFrameRequest)
  })
_sym_db.RegisterMessage(CameraServiceRenderFrameRequest)

CameraServiceGetPointCloudRequest = _reflection.GeneratedProtocolMessageType('CameraServiceGetPointCloudRequest', (_message.Message,), {
  'DESCRIPTOR' : _CAMERASERVICEGETPOINTCLOUDREQUEST,
  '__module__' : 'proto.api.component.v1.camera_pb2'
  # @@protoc_insertion_point(class_scope:proto.api.component.v1.CameraServiceGetPointCloudRequest)
  })
_sym_db.RegisterMessage(CameraServiceGetPointCloudRequest)

CameraServiceGetPointCloudResponse = _reflection.GeneratedProtocolMessageType('CameraServiceGetPointCloudResponse', (_message.Message,), {
  'DESCRIPTOR' : _CAMERASERVICEGETPOINTCLOUDRESPONSE,
  '__module__' : 'proto.api.component.v1.camera_pb2'
  # @@protoc_insertion_point(class_scope:proto.api.component.v1.CameraServiceGetPointCloudResponse)
  })
_sym_db.RegisterMessage(CameraServiceGetPointCloudResponse)

CameraServiceGetObjectPointCloudsRequest = _reflection.GeneratedProtocolMessageType('CameraServiceGetObjectPointCloudsRequest', (_message.Message,), {
  'DESCRIPTOR' : _CAMERASERVICEGETOBJECTPOINTCLOUDSREQUEST,
  '__module__' : 'proto.api.component.v1.camera_pb2'
  # @@protoc_insertion_point(class_scope:proto.api.component.v1.CameraServiceGetObjectPointCloudsRequest)
  })
_sym_db.RegisterMessage(CameraServiceGetObjectPointCloudsRequest)

CameraServiceGetObjectPointCloudsResponse = _reflection.GeneratedProtocolMessageType('CameraServiceGetObjectPointCloudsResponse', (_message.Message,), {
  'DESCRIPTOR' : _CAMERASERVICEGETOBJECTPOINTCLOUDSRESPONSE,
  '__module__' : 'proto.api.component.v1.camera_pb2'
  # @@protoc_insertion_point(class_scope:proto.api.component.v1.CameraServiceGetObjectPointCloudsResponse)
  })
_sym_db.RegisterMessage(CameraServiceGetObjectPointCloudsResponse)

PointCloudObject = _reflection.GeneratedProtocolMessageType('PointCloudObject', (_message.Message,), {
  'DESCRIPTOR' : _POINTCLOUDOBJECT,
  '__module__' : 'proto.api.component.v1.camera_pb2'
  # @@protoc_insertion_point(class_scope:proto.api.component.v1.PointCloudObject)
  })
_sym_db.RegisterMessage(PointCloudObject)

_CAMERASERVICE = DESCRIPTOR.services_by_name['CameraService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n#com.viam.rdk.proto.api.component.v1Z&go.viam.com/rdk/proto/api/component/v1'
  _CAMERASERVICE.methods_by_name['GetFrame']._options = None
  _CAMERASERVICE.methods_by_name['GetFrame']._serialized_options = b'\202\323\344\223\002\'\022%/api/v1/component/camera/{name}/frame'
  _CAMERASERVICE.methods_by_name['RenderFrame']._options = None
  _CAMERASERVICE.methods_by_name['RenderFrame']._serialized_options = b'\202\323\344\223\002.\022,/api/v1/component/camera/{name}/render_frame'
  _CAMERASERVICE.methods_by_name['GetPointCloud']._options = None
  _CAMERASERVICE.methods_by_name['GetPointCloud']._serialized_options = b'\202\323\344\223\002-\022+/api/v1/component/camera/{name}/point_cloud'
  _CAMERASERVICE.methods_by_name['GetObjectPointClouds']._options = None
  _CAMERASERVICE.methods_by_name['GetObjectPointClouds']._serialized_options = b'\202\323\344\223\0025\0223/api/v1/component/camera/{name}/object_point_clouds'
  _CAMERASERVICEGETFRAMEREQUEST._serialized_start=154
  _CAMERASERVICEGETFRAMEREQUEST._serialized_end=233
  _CAMERASERVICEGETFRAMERESPONSE._serialized_start=236
  _CAMERASERVICEGETFRAMERESPONSE._serialized_end=374
  _CAMERASERVICERENDERFRAMEREQUEST._serialized_start=376
  _CAMERASERVICERENDERFRAMEREQUEST._serialized_end=458
  _CAMERASERVICEGETPOINTCLOUDREQUEST._serialized_start=460
  _CAMERASERVICEGETPOINTCLOUDREQUEST._serialized_end=544
  _CAMERASERVICEGETPOINTCLOUDRESPONSE._serialized_start=546
  _CAMERASERVICEGETPOINTCLOUDRESPONSE._serialized_end=633
  _CAMERASERVICEGETOBJECTPOINTCLOUDSREQUEST._serialized_start=636
  _CAMERASERVICEGETOBJECTPOINTCLOUDSREQUEST._serialized_end=875
  _CAMERASERVICEGETOBJECTPOINTCLOUDSRESPONSE._serialized_start=878
  _CAMERASERVICEGETOBJECTPOINTCLOUDSRESPONSE._serialized_end=1018
  _POINTCLOUDOBJECT._serialized_start=1021
  _POINTCLOUDOBJECT._serialized_end=1217
  _CAMERASERVICE._serialized_start=1220
  _CAMERASERVICE._serialized_end=1962
# @@protoc_insertion_point(module_scope)
