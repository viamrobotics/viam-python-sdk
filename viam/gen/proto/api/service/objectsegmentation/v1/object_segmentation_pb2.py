"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from ......proto.api.common.v1 import common_pb2 as proto_dot_api_dot_common_dot_v1_dot_common__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nAproto/api/service/objectsegmentation/v1/object_segmentation.proto\x12\'proto.api.service.objectsegmentation.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a proto/api/common/v1/common.proto"\xbb\x01\n\x1bGetObjectPointCloudsRequest\x12\x1f\n\x0bcamera_name\x18\x01 \x01(\tR\ncameraName\x12%\n\x0esegmenter_name\x18\x02 \x01(\tR\rsegmenterName\x12\x1b\n\tmime_type\x18\x03 \x01(\tR\x08mimeType\x127\n\nparameters\x18\x04 \x01(\x0b2\x17.google.protobuf.StructR\nparameters"|\n\x1cGetObjectPointCloudsResponse\x12\x1b\n\tmime_type\x18\x01 \x01(\tR\x08mimeType\x12?\n\x07objects\x18\x02 \x03(\x0b2%.proto.api.common.v1.PointCloudObjectR\x07objects"F\n\x1dGetSegmenterParametersRequest\x12%\n\x0esegmenter_name\x18\x01 \x01(\tR\rsegmenterName"8\n\x0eTypedParameter\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x12\n\x04type\x18\x02 \x01(\tR\x04type"y\n\x1eGetSegmenterParametersResponse\x12W\n\nparameters\x18\x01 \x03(\x0b27.proto.api.service.objectsegmentation.v1.TypedParameterR\nparameters"\x16\n\x14GetSegmentersRequest"7\n\x15GetSegmentersResponse\x12\x1e\n\nsegmenters\x18\x01 \x03(\tR\nsegmenters2\xc8\x05\n\x19ObjectSegmentationService\x12\xe9\x01\n\x14GetObjectPointClouds\x12D.proto.api.service.objectsegmentation.v1.GetObjectPointCloudsRequest\x1aE.proto.api.service.objectsegmentation.v1.GetObjectPointCloudsResponse"D\x82\xd3\xe4\x93\x02>\x12</viam/api/v1/service/object_segmentation/object_point_clouds\x12\xf0\x01\n\x16GetSegmenterParameters\x12F.proto.api.service.objectsegmentation.v1.GetSegmenterParametersRequest\x1aG.proto.api.service.objectsegmentation.v1.GetSegmenterParametersResponse"E\x82\xd3\xe4\x93\x02?\x12=/viam/api/v1/service/object_segmentation/segmenter_parameters\x12\xcb\x01\n\rGetSegmenters\x12=.proto.api.service.objectsegmentation.v1.GetSegmentersRequest\x1a>.proto.api.service.objectsegmentation.v1.GetSegmentersResponse";\x82\xd3\xe4\x93\x025\x123/viam/api/v1/service/object_segmentation/segmentersBo\n4com.viam.rdk.proto.api.service.objectsegmentation.v1Z7go.viam.com/rdk/proto/api/service/objectsegmentation/v1b\x06proto3')
_GETOBJECTPOINTCLOUDSREQUEST = DESCRIPTOR.message_types_by_name['GetObjectPointCloudsRequest']
_GETOBJECTPOINTCLOUDSRESPONSE = DESCRIPTOR.message_types_by_name['GetObjectPointCloudsResponse']
_GETSEGMENTERPARAMETERSREQUEST = DESCRIPTOR.message_types_by_name['GetSegmenterParametersRequest']
_TYPEDPARAMETER = DESCRIPTOR.message_types_by_name['TypedParameter']
_GETSEGMENTERPARAMETERSRESPONSE = DESCRIPTOR.message_types_by_name['GetSegmenterParametersResponse']
_GETSEGMENTERSREQUEST = DESCRIPTOR.message_types_by_name['GetSegmentersRequest']
_GETSEGMENTERSRESPONSE = DESCRIPTOR.message_types_by_name['GetSegmentersResponse']
GetObjectPointCloudsRequest = _reflection.GeneratedProtocolMessageType('GetObjectPointCloudsRequest', (_message.Message,), {'DESCRIPTOR': _GETOBJECTPOINTCLOUDSREQUEST, '__module__': 'proto.api.service.objectsegmentation.v1.object_segmentation_pb2', '__doc__': 'Attributes:\n      camera_name:\n          Name of a camera\n      segmenter_name:\n          Name of the segmentation algorithm\n      mime_type:\n          Requested MIME type of response\n      parameters:\n          parameters for the chosen segmenter\n  '})
_sym_db.RegisterMessage(GetObjectPointCloudsRequest)
GetObjectPointCloudsResponse = _reflection.GeneratedProtocolMessageType('GetObjectPointCloudsResponse', (_message.Message,), {'DESCRIPTOR': _GETOBJECTPOINTCLOUDSRESPONSE, '__module__': 'proto.api.service.objectsegmentation.v1.object_segmentation_pb2', '__doc__': 'Attributes:\n      mime_type:\n          Actual MIME type of response\n      objects:\n          List of objects in the scene\n  '})
_sym_db.RegisterMessage(GetObjectPointCloudsResponse)
GetSegmenterParametersRequest = _reflection.GeneratedProtocolMessageType('GetSegmenterParametersRequest', (_message.Message,), {'DESCRIPTOR': _GETSEGMENTERPARAMETERSREQUEST, '__module__': 'proto.api.service.objectsegmentation.v1.object_segmentation_pb2', '__doc__': 'Attributes:\n      segmenter_name:\n          Name of the segmentation algo\n  '})
_sym_db.RegisterMessage(GetSegmenterParametersRequest)
TypedParameter = _reflection.GeneratedProtocolMessageType('TypedParameter', (_message.Message,), {'DESCRIPTOR': _TYPEDPARAMETER, '__module__': 'proto.api.service.objectsegmentation.v1.object_segmentation_pb2'})
_sym_db.RegisterMessage(TypedParameter)
GetSegmenterParametersResponse = _reflection.GeneratedProtocolMessageType('GetSegmenterParametersResponse', (_message.Message,), {'DESCRIPTOR': _GETSEGMENTERPARAMETERSRESPONSE, '__module__': 'proto.api.service.objectsegmentation.v1.object_segmentation_pb2', '__doc__': 'Attributes:\n      parameters:\n          parameter names of the segmenter in the request\n  '})
_sym_db.RegisterMessage(GetSegmenterParametersResponse)
GetSegmentersRequest = _reflection.GeneratedProtocolMessageType('GetSegmentersRequest', (_message.Message,), {'DESCRIPTOR': _GETSEGMENTERSREQUEST, '__module__': 'proto.api.service.objectsegmentation.v1.object_segmentation_pb2'})
_sym_db.RegisterMessage(GetSegmentersRequest)
GetSegmentersResponse = _reflection.GeneratedProtocolMessageType('GetSegmentersResponse', (_message.Message,), {'DESCRIPTOR': _GETSEGMENTERSRESPONSE, '__module__': 'proto.api.service.objectsegmentation.v1.object_segmentation_pb2', '__doc__': 'Attributes:\n      segmenters:\n          segmenters in the registry\n  '})
_sym_db.RegisterMessage(GetSegmentersResponse)
_OBJECTSEGMENTATIONSERVICE = DESCRIPTOR.services_by_name['ObjectSegmentationService']
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n4com.viam.rdk.proto.api.service.objectsegmentation.v1Z7go.viam.com/rdk/proto/api/service/objectsegmentation/v1'
    _OBJECTSEGMENTATIONSERVICE.methods_by_name['GetObjectPointClouds']._options = None
    _OBJECTSEGMENTATIONSERVICE.methods_by_name['GetObjectPointClouds']._serialized_options = b'\x82\xd3\xe4\x93\x02>\x12</viam/api/v1/service/object_segmentation/object_point_clouds'
    _OBJECTSEGMENTATIONSERVICE.methods_by_name['GetSegmenterParameters']._options = None
    _OBJECTSEGMENTATIONSERVICE.methods_by_name['GetSegmenterParameters']._serialized_options = b'\x82\xd3\xe4\x93\x02?\x12=/viam/api/v1/service/object_segmentation/segmenter_parameters'
    _OBJECTSEGMENTATIONSERVICE.methods_by_name['GetSegmenters']._options = None
    _OBJECTSEGMENTATIONSERVICE.methods_by_name['GetSegmenters']._serialized_options = b'\x82\xd3\xe4\x93\x025\x123/viam/api/v1/service/object_segmentation/segmenters'
    _GETOBJECTPOINTCLOUDSREQUEST._serialized_start = 205
    _GETOBJECTPOINTCLOUDSREQUEST._serialized_end = 392
    _GETOBJECTPOINTCLOUDSRESPONSE._serialized_start = 394
    _GETOBJECTPOINTCLOUDSRESPONSE._serialized_end = 518
    _GETSEGMENTERPARAMETERSREQUEST._serialized_start = 520
    _GETSEGMENTERPARAMETERSREQUEST._serialized_end = 590
    _TYPEDPARAMETER._serialized_start = 592
    _TYPEDPARAMETER._serialized_end = 648
    _GETSEGMENTERPARAMETERSRESPONSE._serialized_start = 650
    _GETSEGMENTERPARAMETERSRESPONSE._serialized_end = 771
    _GETSEGMENTERSREQUEST._serialized_start = 773
    _GETSEGMENTERSREQUEST._serialized_end = 795
    _GETSEGMENTERSRESPONSE._serialized_start = 797
    _GETSEGMENTERSRESPONSE._serialized_end = 852
    _OBJECTSEGMENTATIONSERVICE._serialized_start = 855
    _OBJECTSEGMENTATIONSERVICE._serialized_end = 1567