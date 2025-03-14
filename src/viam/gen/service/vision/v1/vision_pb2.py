"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 2, '', 'service/vision/v1/vision.proto')
_sym_db = _symbol_database.Default()
from ....common.v1 import common_pb2 as common_dot_v1_dot_common__pb2
from ....component.camera.v1 import camera_pb2 as component_dot_camera_dot_v1_dot_camera__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1eservice/vision/v1/vision.proto\x12\x16viam.service.vision.v1\x1a\x16common/v1/common.proto\x1a component/camera/v1/camera.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1cgoogle/protobuf/struct.proto"\xba\x01\n\x14GetDetectionsRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x14\n\x05image\x18\x02 \x01(\x0cR\x05image\x12\x14\n\x05width\x18\x03 \x01(\x03R\x05width\x12\x16\n\x06height\x18\x04 \x01(\x03R\x06height\x12\x1b\n\tmime_type\x18\x05 \x01(\tR\x08mimeType\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"Z\n\x15GetDetectionsResponse\x12A\n\ndetections\x18\x01 \x03(\x0b2!.viam.service.vision.v1.DetectionR\ndetections"\x84\x01\n\x1eGetDetectionsFromCameraRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x1f\n\x0bcamera_name\x18\x02 \x01(\tR\ncameraName\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"d\n\x1fGetDetectionsFromCameraResponse\x12A\n\ndetections\x18\x01 \x03(\x0b2!.viam.service.vision.v1.DetectionR\ndetections"\xea\x03\n\tDetection\x12\x18\n\x05x_min\x18\x01 \x01(\x03H\x00R\x04xMin\x88\x01\x01\x12\x18\n\x05y_min\x18\x02 \x01(\x03H\x01R\x04yMin\x88\x01\x01\x12\x18\n\x05x_max\x18\x03 \x01(\x03H\x02R\x04xMax\x88\x01\x01\x12\x18\n\x05y_max\x18\x04 \x01(\x03H\x03R\x04yMax\x88\x01\x01\x12\x1e\n\nconfidence\x18\x05 \x01(\x01R\nconfidence\x12\x1d\n\nclass_name\x18\x06 \x01(\tR\tclassName\x12-\n\x10x_min_normalized\x18\x07 \x01(\x01H\x04R\x0exMinNormalized\x88\x01\x01\x12-\n\x10y_min_normalized\x18\x08 \x01(\x01H\x05R\x0eyMinNormalized\x88\x01\x01\x12-\n\x10x_max_normalized\x18\t \x01(\x01H\x06R\x0exMaxNormalized\x88\x01\x01\x12-\n\x10y_max_normalized\x18\n \x01(\x01H\x07R\x0eyMaxNormalized\x88\x01\x01B\x08\n\x06_x_minB\x08\n\x06_y_minB\x08\n\x06_x_maxB\x08\n\x06_y_maxB\x13\n\x11_x_min_normalizedB\x13\n\x11_y_min_normalizedB\x13\n\x11_x_max_normalizedB\x13\n\x11_y_max_normalized"\xcd\x01\n\x19GetClassificationsRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x14\n\x05image\x18\x02 \x01(\x0cR\x05image\x12\x14\n\x05width\x18\x03 \x01(\x05R\x05width\x12\x16\n\x06height\x18\x04 \x01(\x05R\x06height\x12\x1b\n\tmime_type\x18\x05 \x01(\tR\x08mimeType\x12\x0c\n\x01n\x18\x06 \x01(\x05R\x01n\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"n\n\x1aGetClassificationsResponse\x12P\n\x0fclassifications\x18\x01 \x03(\x0b2&.viam.service.vision.v1.ClassificationR\x0fclassifications"\x97\x01\n#GetClassificationsFromCameraRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x1f\n\x0bcamera_name\x18\x02 \x01(\tR\ncameraName\x12\x0c\n\x01n\x18\x03 \x01(\x05R\x01n\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"x\n$GetClassificationsFromCameraResponse\x12P\n\x0fclassifications\x18\x01 \x03(\x0b2&.viam.service.vision.v1.ClassificationR\x0fclassifications"O\n\x0eClassification\x12\x1d\n\nclass_name\x18\x01 \x01(\tR\tclassName\x12\x1e\n\nconfidence\x18\x02 \x01(\x01R\nconfidence"\x9e\x01\n\x1bGetObjectPointCloudsRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x1f\n\x0bcamera_name\x18\x02 \x01(\tR\ncameraName\x12\x1b\n\tmime_type\x18\x03 \x01(\tR\x08mimeType\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"w\n\x1cGetObjectPointCloudsResponse\x12\x1b\n\tmime_type\x18\x01 \x01(\tR\x08mimeType\x12:\n\x07objects\x18\x02 \x03(\x0b2 .viam.common.v1.PointCloudObjectR\x07objects"Y\n\x14GetPropertiesRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"\xc5\x02\n\x1bCaptureAllFromCameraRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x1f\n\x0bcamera_name\x18\x02 \x01(\tR\ncameraName\x12!\n\x0creturn_image\x18\x03 \x01(\x08R\x0breturnImage\x125\n\x16return_classifications\x18\x04 \x01(\x08R\x15returnClassifications\x12+\n\x11return_detections\x18\x05 \x01(\x08R\x10returnDetections\x12;\n\x1areturn_object_point_clouds\x18\x06 \x01(\x08R\x17returnObjectPointClouds\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"\xd5\x02\n\x1cCaptureAllFromCameraResponse\x125\n\x05image\x18\x01 \x01(\x0b2\x1f.viam.component.camera.v1.ImageR\x05image\x12A\n\ndetections\x18\x02 \x03(\x0b2!.viam.service.vision.v1.DetectionR\ndetections\x12P\n\x0fclassifications\x18\x03 \x03(\x0b2&.viam.service.vision.v1.ClassificationR\x0fclassifications\x12:\n\x07objects\x18\x04 \x03(\x0b2 .viam.common.v1.PointCloudObjectR\x07objects\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"\xca\x01\n\x15GetPropertiesResponse\x12;\n\x19classifications_supported\x18\x01 \x01(\x08R\x18classificationsSupported\x121\n\x14detections_supported\x18\x02 \x01(\x08R\x13detectionsSupported\x12A\n\x1dobject_point_clouds_supported\x18\x03 \x01(\x08R\x1aobjectPointCloudsSupported2\xcd\x0b\n\rVisionService\x12\xc8\x01\n\x17GetDetectionsFromCamera\x126.viam.service.vision.v1.GetDetectionsFromCameraRequest\x1a7.viam.service.vision.v1.GetDetectionsFromCameraResponse"<\x82\xd3\xe4\x93\x026"4/viam/api/v1/service/vision/{name}/camera_detections\x12\xa3\x01\n\rGetDetections\x12,.viam.service.vision.v1.GetDetectionsRequest\x1a-.viam.service.vision.v1.GetDetectionsResponse"5\x82\xd3\xe4\x93\x02/"-/viam/api/v1/service/vision/{name}/detections\x12\xdc\x01\n\x1cGetClassificationsFromCamera\x12;.viam.service.vision.v1.GetClassificationsFromCameraRequest\x1a<.viam.service.vision.v1.GetClassificationsFromCameraResponse"A\x82\xd3\xe4\x93\x02;"9/viam/api/v1/service/vision/{name}/camera_classifications\x12\xb7\x01\n\x12GetClassifications\x121.viam.service.vision.v1.GetClassificationsRequest\x1a2.viam.service.vision.v1.GetClassificationsResponse":\x82\xd3\xe4\x93\x024"2/viam/api/v1/service/vision/{name}/classifications\x12\xc1\x01\n\x14GetObjectPointClouds\x123.viam.service.vision.v1.GetObjectPointCloudsRequest\x1a4.viam.service.vision.v1.GetObjectPointCloudsResponse">\x82\xd3\xe4\x93\x028"6/viam/api/v1/service/vision/{name}/object_point_clouds\x12\xa7\x01\n\rGetProperties\x12,.viam.service.vision.v1.GetPropertiesRequest\x1a-.viam.service.vision.v1.GetPropertiesResponse"9\x82\xd3\xe4\x93\x023"1/viam/api/v1/service/vision/{name}/get_properties\x12\xb9\x01\n\x14CaptureAllFromCamera\x123.viam.service.vision.v1.CaptureAllFromCameraRequest\x1a4.viam.service.vision.v1.CaptureAllFromCameraResponse"6\x82\xd3\xe4\x93\x020"./viam/api/v1/service/vision/{name}/capture_all\x12\x87\x01\n\tDoCommand\x12 .viam.common.v1.DoCommandRequest\x1a!.viam.common.v1.DoCommandResponse"5\x82\xd3\xe4\x93\x02/"-/viam/api/v1/service/vision/{name}/do_commandB?\n\x1acom.viam.service.vision.v1Z!go.viam.com/api/service/vision/v1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'service.vision.v1.vision_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1acom.viam.service.vision.v1Z!go.viam.com/api/service/vision/v1'
    _globals['_VISIONSERVICE'].methods_by_name['GetDetectionsFromCamera']._loaded_options = None
    _globals['_VISIONSERVICE'].methods_by_name['GetDetectionsFromCamera']._serialized_options = b'\x82\xd3\xe4\x93\x026"4/viam/api/v1/service/vision/{name}/camera_detections'
    _globals['_VISIONSERVICE'].methods_by_name['GetDetections']._loaded_options = None
    _globals['_VISIONSERVICE'].methods_by_name['GetDetections']._serialized_options = b'\x82\xd3\xe4\x93\x02/"-/viam/api/v1/service/vision/{name}/detections'
    _globals['_VISIONSERVICE'].methods_by_name['GetClassificationsFromCamera']._loaded_options = None
    _globals['_VISIONSERVICE'].methods_by_name['GetClassificationsFromCamera']._serialized_options = b'\x82\xd3\xe4\x93\x02;"9/viam/api/v1/service/vision/{name}/camera_classifications'
    _globals['_VISIONSERVICE'].methods_by_name['GetClassifications']._loaded_options = None
    _globals['_VISIONSERVICE'].methods_by_name['GetClassifications']._serialized_options = b'\x82\xd3\xe4\x93\x024"2/viam/api/v1/service/vision/{name}/classifications'
    _globals['_VISIONSERVICE'].methods_by_name['GetObjectPointClouds']._loaded_options = None
    _globals['_VISIONSERVICE'].methods_by_name['GetObjectPointClouds']._serialized_options = b'\x82\xd3\xe4\x93\x028"6/viam/api/v1/service/vision/{name}/object_point_clouds'
    _globals['_VISIONSERVICE'].methods_by_name['GetProperties']._loaded_options = None
    _globals['_VISIONSERVICE'].methods_by_name['GetProperties']._serialized_options = b'\x82\xd3\xe4\x93\x023"1/viam/api/v1/service/vision/{name}/get_properties'
    _globals['_VISIONSERVICE'].methods_by_name['CaptureAllFromCamera']._loaded_options = None
    _globals['_VISIONSERVICE'].methods_by_name['CaptureAllFromCamera']._serialized_options = b'\x82\xd3\xe4\x93\x020"./viam/api/v1/service/vision/{name}/capture_all'
    _globals['_VISIONSERVICE'].methods_by_name['DoCommand']._loaded_options = None
    _globals['_VISIONSERVICE'].methods_by_name['DoCommand']._serialized_options = b'\x82\xd3\xe4\x93\x02/"-/viam/api/v1/service/vision/{name}/do_command'
    _globals['_GETDETECTIONSREQUEST']._serialized_start = 177
    _globals['_GETDETECTIONSREQUEST']._serialized_end = 363
    _globals['_GETDETECTIONSRESPONSE']._serialized_start = 365
    _globals['_GETDETECTIONSRESPONSE']._serialized_end = 455
    _globals['_GETDETECTIONSFROMCAMERAREQUEST']._serialized_start = 458
    _globals['_GETDETECTIONSFROMCAMERAREQUEST']._serialized_end = 590
    _globals['_GETDETECTIONSFROMCAMERARESPONSE']._serialized_start = 592
    _globals['_GETDETECTIONSFROMCAMERARESPONSE']._serialized_end = 692
    _globals['_DETECTION']._serialized_start = 695
    _globals['_DETECTION']._serialized_end = 1185
    _globals['_GETCLASSIFICATIONSREQUEST']._serialized_start = 1188
    _globals['_GETCLASSIFICATIONSREQUEST']._serialized_end = 1393
    _globals['_GETCLASSIFICATIONSRESPONSE']._serialized_start = 1395
    _globals['_GETCLASSIFICATIONSRESPONSE']._serialized_end = 1505
    _globals['_GETCLASSIFICATIONSFROMCAMERAREQUEST']._serialized_start = 1508
    _globals['_GETCLASSIFICATIONSFROMCAMERAREQUEST']._serialized_end = 1659
    _globals['_GETCLASSIFICATIONSFROMCAMERARESPONSE']._serialized_start = 1661
    _globals['_GETCLASSIFICATIONSFROMCAMERARESPONSE']._serialized_end = 1781
    _globals['_CLASSIFICATION']._serialized_start = 1783
    _globals['_CLASSIFICATION']._serialized_end = 1862
    _globals['_GETOBJECTPOINTCLOUDSREQUEST']._serialized_start = 1865
    _globals['_GETOBJECTPOINTCLOUDSREQUEST']._serialized_end = 2023
    _globals['_GETOBJECTPOINTCLOUDSRESPONSE']._serialized_start = 2025
    _globals['_GETOBJECTPOINTCLOUDSRESPONSE']._serialized_end = 2144
    _globals['_GETPROPERTIESREQUEST']._serialized_start = 2146
    _globals['_GETPROPERTIESREQUEST']._serialized_end = 2235
    _globals['_CAPTUREALLFROMCAMERAREQUEST']._serialized_start = 2238
    _globals['_CAPTUREALLFROMCAMERAREQUEST']._serialized_end = 2563
    _globals['_CAPTUREALLFROMCAMERARESPONSE']._serialized_start = 2566
    _globals['_CAPTUREALLFROMCAMERARESPONSE']._serialized_end = 2907
    _globals['_GETPROPERTIESRESPONSE']._serialized_start = 2910
    _globals['_GETPROPERTIESRESPONSE']._serialized_end = 3112
    _globals['_VISIONSERVICE']._serialized_start = 3115
    _globals['_VISIONSERVICE']._serialized_end = 4600