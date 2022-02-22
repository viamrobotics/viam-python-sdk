"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......proto.api.common.v1 import common_pb2 as proto_dot_api_dot_common_dot_v1_dot_common__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nAproto/api/service/objectsegmentation/v1/object_segmentation.proto\x12\'proto.api.service.objectsegmentation.v1\x1a\x1cgoogle/api/annotations.proto\x1a proto/api/common/v1/common.proto"\xe2\x01\n\x1bGetObjectPointCloudsRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x1b\n\tmime_type\x18\x02 \x01(\tR\x08mimeType\x12-\n\x13min_points_in_plane\x18\x03 \x01(\x03R\x10minPointsInPlane\x121\n\x15min_points_in_segment\x18\x04 \x01(\x03R\x12minPointsInSegment\x120\n\x14clustering_radius_mm\x18\x05 \x01(\x01R\x12clusteringRadiusMm"\x90\x01\n\x1cGetObjectPointCloudsResponse\x12\x1b\n\tmime_type\x18\x01 \x01(\tR\x08mimeType\x12S\n\x07objects\x18\x02 \x03(\x0b29.proto.api.service.objectsegmentation.v1.PointCloudObjectR\x07objects"\xc9\x01\n\x10PointCloudObject\x12\x14\n\x05frame\x18\x01 \x01(\x0cR\x05frame\x12P\n\x15center_coordinates_mm\x18\x02 \x01(\x0b2\x1c.proto.api.common.v1.Vector3R\x13centerCoordinatesMm\x12M\n\x0fbounding_box_mm\x18\x03 \x01(\x0b2%.proto.api.common.v1.RectangularPrismR\rboundingBoxMm2\x82\x02\n\x19ObjectSegmentationService\x12\xe4\x01\n\x14GetObjectPointClouds\x12D.proto.api.service.objectsegmentation.v1.GetObjectPointCloudsRequest\x1aE.proto.api.service.objectsegmentation.v1.GetObjectPointCloudsResponse"?\x82\xd3\xe4\x93\x029\x127/api/v1/service/object_segmentation/object_point_cloudsBI\n!com.viam.rdk.proto.api.service.v1Z$go.viam.com/rdk/proto/api/service/v1b\x06proto3')
_GETOBJECTPOINTCLOUDSREQUEST = DESCRIPTOR.message_types_by_name['GetObjectPointCloudsRequest']
_GETOBJECTPOINTCLOUDSRESPONSE = DESCRIPTOR.message_types_by_name['GetObjectPointCloudsResponse']
_POINTCLOUDOBJECT = DESCRIPTOR.message_types_by_name['PointCloudObject']
GetObjectPointCloudsRequest = _reflection.GeneratedProtocolMessageType('GetObjectPointCloudsRequest', (_message.Message,), {'DESCRIPTOR': _GETOBJECTPOINTCLOUDSREQUEST, '__module__': 'proto.api.service.objectsegmentation.v1.object_segmentation_pb2'})
_sym_db.RegisterMessage(GetObjectPointCloudsRequest)
GetObjectPointCloudsResponse = _reflection.GeneratedProtocolMessageType('GetObjectPointCloudsResponse', (_message.Message,), {'DESCRIPTOR': _GETOBJECTPOINTCLOUDSRESPONSE, '__module__': 'proto.api.service.objectsegmentation.v1.object_segmentation_pb2'})
_sym_db.RegisterMessage(GetObjectPointCloudsResponse)
PointCloudObject = _reflection.GeneratedProtocolMessageType('PointCloudObject', (_message.Message,), {'DESCRIPTOR': _POINTCLOUDOBJECT, '__module__': 'proto.api.service.objectsegmentation.v1.object_segmentation_pb2'})
_sym_db.RegisterMessage(PointCloudObject)
_OBJECTSEGMENTATIONSERVICE = DESCRIPTOR.services_by_name['ObjectSegmentationService']
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n!com.viam.rdk.proto.api.service.v1Z$go.viam.com/rdk/proto/api/service/v1'
    _OBJECTSEGMENTATIONSERVICE.methods_by_name['GetObjectPointClouds']._options = None
    _OBJECTSEGMENTATIONSERVICE.methods_by_name['GetObjectPointClouds']._serialized_options = b'\x82\xd3\xe4\x93\x029\x127/api/v1/service/object_segmentation/object_point_clouds'
    _GETOBJECTPOINTCLOUDSREQUEST._serialized_start = 175
    _GETOBJECTPOINTCLOUDSREQUEST._serialized_end = 401
    _GETOBJECTPOINTCLOUDSRESPONSE._serialized_start = 404
    _GETOBJECTPOINTCLOUDSRESPONSE._serialized_end = 548
    _POINTCLOUDOBJECT._serialized_start = 551
    _POINTCLOUDOBJECT._serialized_end = 752
    _OBJECTSEGMENTATIONSERVICE._serialized_start = 755
    _OBJECTSEGMENTATIONSERVICE._serialized_end = 1013