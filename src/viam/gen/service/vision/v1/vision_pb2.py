"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....common.v1 import common_pb2 as common_dot_v1_dot_common__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1eservice/vision/v1/vision.proto\x12\x16viam.service.vision.v1\x1a\x16common/v1/common.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1cgoogle/protobuf/struct.proto"\xba\x01\n\x14GetDetectionsRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x14\n\x05image\x18\x02 \x01(\x0cR\x05image\x12\x14\n\x05width\x18\x03 \x01(\x03R\x05width\x12\x16\n\x06height\x18\x04 \x01(\x03R\x06height\x12\x1b\n\tmime_type\x18\x05 \x01(\tR\x08mimeType\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"Z\n\x15GetDetectionsResponse\x12A\n\ndetections\x18\x01 \x03(\x0b2!.viam.service.vision.v1.DetectionR\ndetections"\x84\x01\n\x1eGetDetectionsFromCameraRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x1f\n\x0bcamera_name\x18\x02 \x01(\tR\ncameraName\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"d\n\x1fGetDetectionsFromCameraResponse\x12A\n\ndetections\x18\x01 \x03(\x0b2!.viam.service.vision.v1.DetectionR\ndetections"\xda\x01\n\tDetection\x12\x18\n\x05x_min\x18\x01 \x01(\x03H\x00R\x04xMin\x88\x01\x01\x12\x18\n\x05y_min\x18\x02 \x01(\x03H\x01R\x04yMin\x88\x01\x01\x12\x18\n\x05x_max\x18\x03 \x01(\x03H\x02R\x04xMax\x88\x01\x01\x12\x18\n\x05y_max\x18\x04 \x01(\x03H\x03R\x04yMax\x88\x01\x01\x12\x1e\n\nconfidence\x18\x05 \x01(\x01R\nconfidence\x12\x1d\n\nclass_name\x18\x06 \x01(\tR\tclassNameB\x08\n\x06_x_minB\x08\n\x06_y_minB\x08\n\x06_x_maxB\x08\n\x06_y_max"\xcd\x01\n\x19GetClassificationsRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x14\n\x05image\x18\x02 \x01(\x0cR\x05image\x12\x14\n\x05width\x18\x03 \x01(\x05R\x05width\x12\x16\n\x06height\x18\x04 \x01(\x05R\x06height\x12\x1b\n\tmime_type\x18\x05 \x01(\tR\x08mimeType\x12\x0c\n\x01n\x18\x06 \x01(\x05R\x01n\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"n\n\x1aGetClassificationsResponse\x12P\n\x0fclassifications\x18\x01 \x03(\x0b2&.viam.service.vision.v1.ClassificationR\x0fclassifications"\x97\x01\n#GetClassificationsFromCameraRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x1f\n\x0bcamera_name\x18\x02 \x01(\tR\ncameraName\x12\x0c\n\x01n\x18\x03 \x01(\x05R\x01n\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"x\n$GetClassificationsFromCameraResponse\x12P\n\x0fclassifications\x18\x01 \x03(\x0b2&.viam.service.vision.v1.ClassificationR\x0fclassifications"O\n\x0eClassification\x12\x1d\n\nclass_name\x18\x01 \x01(\tR\tclassName\x12\x1e\n\nconfidence\x18\x02 \x01(\x01R\nconfidence"\x9e\x01\n\x1bGetObjectPointCloudsRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x1f\n\x0bcamera_name\x18\x02 \x01(\tR\ncameraName\x12\x1b\n\tmime_type\x18\x03 \x01(\tR\x08mimeType\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"w\n\x1cGetObjectPointCloudsResponse\x12\x1b\n\tmime_type\x18\x01 \x01(\tR\x08mimeType\x12:\n\x07objects\x18\x02 \x03(\x0b2 .viam.common.v1.PointCloudObjectR\x07objects2\xe7\x08\n\rVisionService\x12\xc8\x01\n\x17GetDetectionsFromCamera\x126.viam.service.vision.v1.GetDetectionsFromCameraRequest\x1a7.viam.service.vision.v1.GetDetectionsFromCameraResponse"<\x82\xd3\xe4\x93\x026"4/viam/api/v1/service/vision/{name}/camera_detections\x12\xa3\x01\n\rGetDetections\x12,.viam.service.vision.v1.GetDetectionsRequest\x1a-.viam.service.vision.v1.GetDetectionsResponse"5\x82\xd3\xe4\x93\x02/"-/viam/api/v1/service/vision/{name}/detections\x12\xdc\x01\n\x1cGetClassificationsFromCamera\x12;.viam.service.vision.v1.GetClassificationsFromCameraRequest\x1a<.viam.service.vision.v1.GetClassificationsFromCameraResponse"A\x82\xd3\xe4\x93\x02;"9/viam/api/v1/service/vision/{name}/camera_classifications\x12\xb7\x01\n\x12GetClassifications\x121.viam.service.vision.v1.GetClassificationsRequest\x1a2.viam.service.vision.v1.GetClassificationsResponse":\x82\xd3\xe4\x93\x024"2/viam/api/v1/service/vision/{name}/classifications\x12\xc1\x01\n\x14GetObjectPointClouds\x123.viam.service.vision.v1.GetObjectPointCloudsRequest\x1a4.viam.service.vision.v1.GetObjectPointCloudsResponse">\x82\xd3\xe4\x93\x028"6/viam/api/v1/service/vision/{name}/object_point_clouds\x12\x87\x01\n\tDoCommand\x12 .viam.common.v1.DoCommandRequest\x1a!.viam.common.v1.DoCommandResponse"5\x82\xd3\xe4\x93\x02/"-/viam/api/v1/service/vision/{name}/do_commandB?\n\x1acom.viam.service.vision.v1Z!go.viam.com/api/service/vision/v1b\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'service.vision.v1.vision_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n\x1acom.viam.service.vision.v1Z!go.viam.com/api/service/vision/v1'
    _VISIONSERVICE.methods_by_name['GetDetectionsFromCamera']._options = None
    _VISIONSERVICE.methods_by_name['GetDetectionsFromCamera']._serialized_options = b'\x82\xd3\xe4\x93\x026"4/viam/api/v1/service/vision/{name}/camera_detections'
    _VISIONSERVICE.methods_by_name['GetDetections']._options = None
    _VISIONSERVICE.methods_by_name['GetDetections']._serialized_options = b'\x82\xd3\xe4\x93\x02/"-/viam/api/v1/service/vision/{name}/detections'
    _VISIONSERVICE.methods_by_name['GetClassificationsFromCamera']._options = None
    _VISIONSERVICE.methods_by_name['GetClassificationsFromCamera']._serialized_options = b'\x82\xd3\xe4\x93\x02;"9/viam/api/v1/service/vision/{name}/camera_classifications'
    _VISIONSERVICE.methods_by_name['GetClassifications']._options = None
    _VISIONSERVICE.methods_by_name['GetClassifications']._serialized_options = b'\x82\xd3\xe4\x93\x024"2/viam/api/v1/service/vision/{name}/classifications'
    _VISIONSERVICE.methods_by_name['GetObjectPointClouds']._options = None
    _VISIONSERVICE.methods_by_name['GetObjectPointClouds']._serialized_options = b'\x82\xd3\xe4\x93\x028"6/viam/api/v1/service/vision/{name}/object_point_clouds'
    _VISIONSERVICE.methods_by_name['DoCommand']._options = None
    _VISIONSERVICE.methods_by_name['DoCommand']._serialized_options = b'\x82\xd3\xe4\x93\x02/"-/viam/api/v1/service/vision/{name}/do_command'
    _GETDETECTIONSREQUEST._serialized_start = 143
    _GETDETECTIONSREQUEST._serialized_end = 329
    _GETDETECTIONSRESPONSE._serialized_start = 331
    _GETDETECTIONSRESPONSE._serialized_end = 421
    _GETDETECTIONSFROMCAMERAREQUEST._serialized_start = 424
    _GETDETECTIONSFROMCAMERAREQUEST._serialized_end = 556
    _GETDETECTIONSFROMCAMERARESPONSE._serialized_start = 558
    _GETDETECTIONSFROMCAMERARESPONSE._serialized_end = 658
    _DETECTION._serialized_start = 661
    _DETECTION._serialized_end = 879
    _GETCLASSIFICATIONSREQUEST._serialized_start = 882
    _GETCLASSIFICATIONSREQUEST._serialized_end = 1087
    _GETCLASSIFICATIONSRESPONSE._serialized_start = 1089
    _GETCLASSIFICATIONSRESPONSE._serialized_end = 1199
    _GETCLASSIFICATIONSFROMCAMERAREQUEST._serialized_start = 1202
    _GETCLASSIFICATIONSFROMCAMERAREQUEST._serialized_end = 1353
    _GETCLASSIFICATIONSFROMCAMERARESPONSE._serialized_start = 1355
    _GETCLASSIFICATIONSFROMCAMERARESPONSE._serialized_end = 1475
    _CLASSIFICATION._serialized_start = 1477
    _CLASSIFICATION._serialized_end = 1556
    _GETOBJECTPOINTCLOUDSREQUEST._serialized_start = 1559
    _GETOBJECTPOINTCLOUDSREQUEST._serialized_end = 1717
    _GETOBJECTPOINTCLOUDSRESPONSE._serialized_start = 1719
    _GETOBJECTPOINTCLOUDSRESPONSE._serialized_end = 1838
    _VISIONSERVICE._serialized_start = 1841
    _VISIONSERVICE._serialized_end = 2968