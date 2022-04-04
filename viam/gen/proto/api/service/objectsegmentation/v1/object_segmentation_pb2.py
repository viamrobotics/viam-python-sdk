"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from ......proto.api.common.v1 import common_pb2 as proto_dot_api_dot_common_dot_v1_dot_common__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nAproto/api/service/objectsegmentation/v1/object_segmentation.proto\x12\'proto.api.service.objectsegmentation.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a proto/api/common/v1/common.proto"\xbb\x01\n\x1bGetObjectPointCloudsRequest\x12\x1f\n\x0bcamera_name\x18\x01 \x01(\tR\ncameraName\x12%\n\x0esegmenter_name\x18\x02 \x01(\tR\rsegmenterName\x12\x1b\n\tmime_type\x18\x03 \x01(\tR\x08mimeType\x127\n\nparameters\x18\x04 \x01(\x0b2\x17.google.protobuf.StructR\nparameters"|\n\x1cGetObjectPointCloudsResponse\x12\x1b\n\tmime_type\x18\x01 \x01(\tR\x08mimeType\x12?\n\x07objects\x18\x02 \x03(\x0b2%.proto.api.common.v1.PointCloudObjectR\x07objects"F\n\x1dGetSegmenterParametersRequest\x12%\n\x0esegmenter_name\x18\x01 \x01(\tR\rsegmenterName"8\n\x0eTypedParameter\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x12\n\x04type\x18\x02 \x01(\tR\x04type"y\n\x1eGetSegmenterParametersResponse\x12W\n\nparameters\x18\x01 \x03(\x0b27.proto.api.service.objectsegmentation.v1.TypedParameterR\nparameters"\x16\n\x14GetSegmentersRequest"7\n\x15GetSegmentersResponse\x12\x1e\n\nsegmenters\x18\x01 \x03(\tR\nsegmenters2\xc8\x05\n\x19ObjectSegmentationService\x12\xe9\x01\n\x14GetObjectPointClouds\x12D.proto.api.service.objectsegmentation.v1.GetObjectPointCloudsRequest\x1aE.proto.api.service.objectsegmentation.v1.GetObjectPointCloudsResponse"D\x82\xd3\xe4\x93\x02>\x12</viam/api/v1/service/object_segmentation/object_point_clouds\x12\xf0\x01\n\x16GetSegmenterParameters\x12F.proto.api.service.objectsegmentation.v1.GetSegmenterParametersRequest\x1aG.proto.api.service.objectsegmentation.v1.GetSegmenterParametersResponse"E\x82\xd3\xe4\x93\x02?\x12=/viam/api/v1/service/object_segmentation/segmenter_parameters\x12\xcb\x01\n\rGetSegmenters\x12=.proto.api.service.objectsegmentation.v1.GetSegmentersRequest\x1a>.proto.api.service.objectsegmentation.v1.GetSegmentersResponse";\x82\xd3\xe4\x93\x025\x123/viam/api/v1/service/object_segmentation/segmentersBo\n4com.viam.rdk.proto.api.service.objectsegmentation.v1Z7go.viam.com/rdk/proto/api/service/objectsegmentation/v1b\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'proto.api.service.objectsegmentation.v1.object_segmentation_pb2', globals())
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