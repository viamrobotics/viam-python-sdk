"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....common.v1 import common_pb2 as common_dot_v1_dot_common__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1eservice/vision/v1/vision.proto\x12\x16viam.service.vision.v1\x1a\x16common/v1/common.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1cgoogle/protobuf/struct.proto"S\n\x1eGetModelParameterSchemaRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x1d\n\nmodel_type\x18\x02 \x01(\tR\tmodelType"W\n\x1fGetModelParameterSchemaResponse\x124\n\x16model_parameter_schema\x18\x01 \x01(\x0cR\x14modelParameterSchema"-\n\x17GetDetectorNamesRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name"A\n\x18GetDetectorNamesResponse\x12%\n\x0edetector_names\x18\x01 \x03(\tR\rdetectorNames"\xc7\x01\n\x12AddDetectorRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12#\n\rdetector_name\x18\x02 \x01(\tR\x0cdetectorName\x12.\n\x13detector_model_type\x18\x03 \x01(\tR\x11detectorModelType\x12H\n\x13detector_parameters\x18\x04 \x01(\x0b2\x17.google.protobuf.StructR\x12detectorParameters"\x15\n\x13AddDetectorResponse"P\n\x15RemoveDetectorRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12#\n\rdetector_name\x18\x02 \x01(\tR\x0cdetectorName"\x18\n\x16RemoveDetectorResponse"\xb0\x01\n\x14GetDetectionsRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x14\n\x05image\x18\x02 \x01(\x0cR\x05image\x12\x14\n\x05width\x18\x03 \x01(\x03R\x05width\x12\x16\n\x06height\x18\x04 \x01(\x03R\x06height\x12\x1b\n\tmime_type\x18\x05 \x01(\tR\x08mimeType\x12#\n\rdetector_name\x18\x06 \x01(\tR\x0cdetectorName"Z\n\x15GetDetectionsResponse\x12A\n\ndetections\x18\x01 \x03(\x0b2!.viam.service.vision.v1.DetectionR\ndetections"z\n\x1eGetDetectionsFromCameraRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x1f\n\x0bcamera_name\x18\x02 \x01(\tR\ncameraName\x12#\n\rdetector_name\x18\x03 \x01(\tR\x0cdetectorName"d\n\x1fGetDetectionsFromCameraResponse\x12A\n\ndetections\x18\x01 \x03(\x0b2!.viam.service.vision.v1.DetectionR\ndetections"\xda\x01\n\tDetection\x12\x18\n\x05x_min\x18\x01 \x01(\x03H\x00R\x04xMin\x88\x01\x01\x12\x18\n\x05y_min\x18\x02 \x01(\x03H\x01R\x04yMin\x88\x01\x01\x12\x18\n\x05x_max\x18\x03 \x01(\x03H\x02R\x04xMax\x88\x01\x01\x12\x18\n\x05y_max\x18\x04 \x01(\x03H\x03R\x04yMax\x88\x01\x01\x12\x1e\n\nconfidence\x18\x05 \x01(\x01R\nconfidence\x12\x1d\n\nclass_name\x18\x06 \x01(\tR\tclassNameB\x08\n\x06_x_minB\x08\n\x06_y_minB\x08\n\x06_x_maxB\x08\n\x06_y_max"/\n\x19GetClassifierNamesRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name"G\n\x1aGetClassifierNamesResponse\x12)\n\x10classifier_names\x18\x01 \x03(\tR\x0fclassifierNames"\xd5\x01\n\x14AddClassifierRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\'\n\x0fclassifier_name\x18\x02 \x01(\tR\x0eclassifierName\x122\n\x15classifier_model_type\x18\x03 \x01(\tR\x13classifierModelType\x12L\n\x15classifier_parameters\x18\x04 \x01(\x0b2\x17.google.protobuf.StructR\x14classifierParameters"\x17\n\x15AddClassifierResponse"V\n\x17RemoveClassifierRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\'\n\x0fclassifier_name\x18\x02 \x01(\tR\x0eclassifierName"\x1a\n\x18RemoveClassifierResponse"\xc7\x01\n\x19GetClassificationsRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x14\n\x05image\x18\x02 \x01(\x0cR\x05image\x12\x14\n\x05width\x18\x03 \x01(\x05R\x05width\x12\x16\n\x06height\x18\x04 \x01(\x05R\x06height\x12\x1b\n\tmime_type\x18\x05 \x01(\tR\x08mimeType\x12\'\n\x0fclassifier_name\x18\x06 \x01(\tR\x0eclassifierName\x12\x0c\n\x01n\x18\x07 \x01(\x05R\x01n"n\n\x1aGetClassificationsResponse\x12P\n\x0fclassifications\x18\x01 \x03(\x0b2&.viam.service.vision.v1.ClassificationR\x0fclassifications"\x91\x01\n#GetClassificationsFromCameraRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x1f\n\x0bcamera_name\x18\x02 \x01(\tR\ncameraName\x12\'\n\x0fclassifier_name\x18\x03 \x01(\tR\x0eclassifierName\x12\x0c\n\x01n\x18\x04 \x01(\x05R\x01n"x\n$GetClassificationsFromCameraResponse\x12P\n\x0fclassifications\x18\x01 \x03(\x0b2&.viam.service.vision.v1.ClassificationR\x0fclassifications"O\n\x0eClassification\x12\x1d\n\nclass_name\x18\x01 \x01(\tR\tclassName\x12\x1e\n\nconfidence\x18\x02 \x01(\x01R\nconfidence".\n\x18GetSegmenterNamesRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name"D\n\x19GetSegmenterNamesResponse\x12\'\n\x0fsegmenter_names\x18\x01 \x03(\tR\x0esegmenterNames"\xce\x01\n\x13AddSegmenterRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12%\n\x0esegmenter_name\x18\x02 \x01(\tR\rsegmenterName\x120\n\x14segmenter_model_type\x18\x03 \x01(\tR\x12segmenterModelType\x12J\n\x14segmenter_parameters\x18\x04 \x01(\x0b2\x17.google.protobuf.StructR\x13segmenterParameters"\x16\n\x14AddSegmenterResponse"S\n\x16RemoveSegmenterRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12%\n\x0esegmenter_name\x18\x02 \x01(\tR\rsegmenterName"\x19\n\x17RemoveSegmenterResponse"\x96\x01\n\x1bGetObjectPointCloudsRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x1f\n\x0bcamera_name\x18\x02 \x01(\tR\ncameraName\x12%\n\x0esegmenter_name\x18\x03 \x01(\tR\rsegmenterName\x12\x1b\n\tmime_type\x18\x04 \x01(\tR\x08mimeType"w\n\x1cGetObjectPointCloudsResponse\x12\x1b\n\tmime_type\x18\x01 \x01(\tR\x08mimeType\x12:\n\x07objects\x18\x02 \x03(\x0b2 .viam.common.v1.PointCloudObjectR\x07objects2\xda\x15\n\rVisionService\x12\xcd\x01\n\x17GetModelParameterSchema\x126.viam.service.vision.v1.GetModelParameterSchemaRequest\x1a7.viam.service.vision.v1.GetModelParameterSchemaResponse"A\x82\xd3\xe4\x93\x02;\x129/viam/api/v1/service/vision/{name}/model_parameter_schema\x12\xb0\x01\n\x10GetDetectorNames\x12/.viam.service.vision.v1.GetDetectorNamesRequest\x1a0.viam.service.vision.v1.GetDetectorNamesResponse"9\x82\xd3\xe4\x93\x023\x121/viam/api/v1/service/vision/{name}/detector_names\x12\x9f\x01\n\x0bAddDetector\x12*.viam.service.vision.v1.AddDetectorRequest\x1a+.viam.service.vision.v1.AddDetectorResponse"7\x82\xd3\xe4\x93\x021"//viam/api/v1/service/vision/{name}/add_detector\x12\xab\x01\n\x0eRemoveDetector\x12-.viam.service.vision.v1.RemoveDetectorRequest\x1a..viam.service.vision.v1.RemoveDetectorResponse":\x82\xd3\xe4\x93\x024"2/viam/api/v1/service/vision/{name}/remove_detector\x12\xc8\x01\n\x17GetDetectionsFromCamera\x126.viam.service.vision.v1.GetDetectionsFromCameraRequest\x1a7.viam.service.vision.v1.GetDetectionsFromCameraResponse"<\x82\xd3\xe4\x93\x026"4/viam/api/v1/service/vision/{name}/camera_detections\x12\xa3\x01\n\rGetDetections\x12,.viam.service.vision.v1.GetDetectionsRequest\x1a-.viam.service.vision.v1.GetDetectionsResponse"5\x82\xd3\xe4\x93\x02/"-/viam/api/v1/service/vision/{name}/detections\x12\xb8\x01\n\x12GetClassifierNames\x121.viam.service.vision.v1.GetClassifierNamesRequest\x1a2.viam.service.vision.v1.GetClassifierNamesResponse";\x82\xd3\xe4\x93\x025\x123/viam/api/v1/service/vision/{name}/classifier_names\x12\xa7\x01\n\rAddClassifier\x12,.viam.service.vision.v1.AddClassifierRequest\x1a-.viam.service.vision.v1.AddClassifierResponse"9\x82\xd3\xe4\x93\x023"1/viam/api/v1/service/vision/{name}/add_classifier\x12\xb3\x01\n\x10RemoveClassifier\x12/.viam.service.vision.v1.RemoveClassifierRequest\x1a0.viam.service.vision.v1.RemoveClassifierResponse"<\x82\xd3\xe4\x93\x026"4/viam/api/v1/service/vision/{name}/remove_classifier\x12\xdc\x01\n\x1cGetClassificationsFromCamera\x12;.viam.service.vision.v1.GetClassificationsFromCameraRequest\x1a<.viam.service.vision.v1.GetClassificationsFromCameraResponse"A\x82\xd3\xe4\x93\x02;"9/viam/api/v1/service/vision/{name}/camera_classifications\x12\xb7\x01\n\x12GetClassifications\x121.viam.service.vision.v1.GetClassificationsRequest\x1a2.viam.service.vision.v1.GetClassificationsResponse":\x82\xd3\xe4\x93\x024"2/viam/api/v1/service/vision/{name}/classifications\x12\xb4\x01\n\x11GetSegmenterNames\x120.viam.service.vision.v1.GetSegmenterNamesRequest\x1a1.viam.service.vision.v1.GetSegmenterNamesResponse":\x82\xd3\xe4\x93\x024\x122/viam/api/v1/service/vision/{name}/segmenter_names\x12\xa3\x01\n\x0cAddSegmenter\x12+.viam.service.vision.v1.AddSegmenterRequest\x1a,.viam.service.vision.v1.AddSegmenterResponse"8\x82\xd3\xe4\x93\x022"0/viam/api/v1/service/vision/{name}/add_segmenter\x12\xaf\x01\n\x0fRemoveSegmenter\x12..viam.service.vision.v1.RemoveSegmenterRequest\x1a/.viam.service.vision.v1.RemoveSegmenterResponse";\x82\xd3\xe4\x93\x025"3/viam/api/v1/service/vision/{name}/remove_segmenter\x12\xc1\x01\n\x14GetObjectPointClouds\x123.viam.service.vision.v1.GetObjectPointCloudsRequest\x1a4.viam.service.vision.v1.GetObjectPointCloudsResponse">\x82\xd3\xe4\x93\x028"6/viam/api/v1/service/vision/{name}/object_point_cloudsB?\n\x1acom.viam.service.vision.v1Z!go.viam.com/api/service/vision/v1b\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'service.vision.v1.vision_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n\x1acom.viam.service.vision.v1Z!go.viam.com/api/service/vision/v1'
    _VISIONSERVICE.methods_by_name['GetModelParameterSchema']._options = None
    _VISIONSERVICE.methods_by_name['GetModelParameterSchema']._serialized_options = b'\x82\xd3\xe4\x93\x02;\x129/viam/api/v1/service/vision/{name}/model_parameter_schema'
    _VISIONSERVICE.methods_by_name['GetDetectorNames']._options = None
    _VISIONSERVICE.methods_by_name['GetDetectorNames']._serialized_options = b'\x82\xd3\xe4\x93\x023\x121/viam/api/v1/service/vision/{name}/detector_names'
    _VISIONSERVICE.methods_by_name['AddDetector']._options = None
    _VISIONSERVICE.methods_by_name['AddDetector']._serialized_options = b'\x82\xd3\xe4\x93\x021"//viam/api/v1/service/vision/{name}/add_detector'
    _VISIONSERVICE.methods_by_name['RemoveDetector']._options = None
    _VISIONSERVICE.methods_by_name['RemoveDetector']._serialized_options = b'\x82\xd3\xe4\x93\x024"2/viam/api/v1/service/vision/{name}/remove_detector'
    _VISIONSERVICE.methods_by_name['GetDetectionsFromCamera']._options = None
    _VISIONSERVICE.methods_by_name['GetDetectionsFromCamera']._serialized_options = b'\x82\xd3\xe4\x93\x026"4/viam/api/v1/service/vision/{name}/camera_detections'
    _VISIONSERVICE.methods_by_name['GetDetections']._options = None
    _VISIONSERVICE.methods_by_name['GetDetections']._serialized_options = b'\x82\xd3\xe4\x93\x02/"-/viam/api/v1/service/vision/{name}/detections'
    _VISIONSERVICE.methods_by_name['GetClassifierNames']._options = None
    _VISIONSERVICE.methods_by_name['GetClassifierNames']._serialized_options = b'\x82\xd3\xe4\x93\x025\x123/viam/api/v1/service/vision/{name}/classifier_names'
    _VISIONSERVICE.methods_by_name['AddClassifier']._options = None
    _VISIONSERVICE.methods_by_name['AddClassifier']._serialized_options = b'\x82\xd3\xe4\x93\x023"1/viam/api/v1/service/vision/{name}/add_classifier'
    _VISIONSERVICE.methods_by_name['RemoveClassifier']._options = None
    _VISIONSERVICE.methods_by_name['RemoveClassifier']._serialized_options = b'\x82\xd3\xe4\x93\x026"4/viam/api/v1/service/vision/{name}/remove_classifier'
    _VISIONSERVICE.methods_by_name['GetClassificationsFromCamera']._options = None
    _VISIONSERVICE.methods_by_name['GetClassificationsFromCamera']._serialized_options = b'\x82\xd3\xe4\x93\x02;"9/viam/api/v1/service/vision/{name}/camera_classifications'
    _VISIONSERVICE.methods_by_name['GetClassifications']._options = None
    _VISIONSERVICE.methods_by_name['GetClassifications']._serialized_options = b'\x82\xd3\xe4\x93\x024"2/viam/api/v1/service/vision/{name}/classifications'
    _VISIONSERVICE.methods_by_name['GetSegmenterNames']._options = None
    _VISIONSERVICE.methods_by_name['GetSegmenterNames']._serialized_options = b'\x82\xd3\xe4\x93\x024\x122/viam/api/v1/service/vision/{name}/segmenter_names'
    _VISIONSERVICE.methods_by_name['AddSegmenter']._options = None
    _VISIONSERVICE.methods_by_name['AddSegmenter']._serialized_options = b'\x82\xd3\xe4\x93\x022"0/viam/api/v1/service/vision/{name}/add_segmenter'
    _VISIONSERVICE.methods_by_name['RemoveSegmenter']._options = None
    _VISIONSERVICE.methods_by_name['RemoveSegmenter']._serialized_options = b'\x82\xd3\xe4\x93\x025"3/viam/api/v1/service/vision/{name}/remove_segmenter'
    _VISIONSERVICE.methods_by_name['GetObjectPointClouds']._options = None
    _VISIONSERVICE.methods_by_name['GetObjectPointClouds']._serialized_options = b'\x82\xd3\xe4\x93\x028"6/viam/api/v1/service/vision/{name}/object_point_clouds'
    _GETMODELPARAMETERSCHEMAREQUEST._serialized_start = 142
    _GETMODELPARAMETERSCHEMAREQUEST._serialized_end = 225
    _GETMODELPARAMETERSCHEMARESPONSE._serialized_start = 227
    _GETMODELPARAMETERSCHEMARESPONSE._serialized_end = 314
    _GETDETECTORNAMESREQUEST._serialized_start = 316
    _GETDETECTORNAMESREQUEST._serialized_end = 361
    _GETDETECTORNAMESRESPONSE._serialized_start = 363
    _GETDETECTORNAMESRESPONSE._serialized_end = 428
    _ADDDETECTORREQUEST._serialized_start = 431
    _ADDDETECTORREQUEST._serialized_end = 630
    _ADDDETECTORRESPONSE._serialized_start = 632
    _ADDDETECTORRESPONSE._serialized_end = 653
    _REMOVEDETECTORREQUEST._serialized_start = 655
    _REMOVEDETECTORREQUEST._serialized_end = 735
    _REMOVEDETECTORRESPONSE._serialized_start = 737
    _REMOVEDETECTORRESPONSE._serialized_end = 761
    _GETDETECTIONSREQUEST._serialized_start = 764
    _GETDETECTIONSREQUEST._serialized_end = 940
    _GETDETECTIONSRESPONSE._serialized_start = 942
    _GETDETECTIONSRESPONSE._serialized_end = 1032
    _GETDETECTIONSFROMCAMERAREQUEST._serialized_start = 1034
    _GETDETECTIONSFROMCAMERAREQUEST._serialized_end = 1156
    _GETDETECTIONSFROMCAMERARESPONSE._serialized_start = 1158
    _GETDETECTIONSFROMCAMERARESPONSE._serialized_end = 1258
    _DETECTION._serialized_start = 1261
    _DETECTION._serialized_end = 1479
    _GETCLASSIFIERNAMESREQUEST._serialized_start = 1481
    _GETCLASSIFIERNAMESREQUEST._serialized_end = 1528
    _GETCLASSIFIERNAMESRESPONSE._serialized_start = 1530
    _GETCLASSIFIERNAMESRESPONSE._serialized_end = 1601
    _ADDCLASSIFIERREQUEST._serialized_start = 1604
    _ADDCLASSIFIERREQUEST._serialized_end = 1817
    _ADDCLASSIFIERRESPONSE._serialized_start = 1819
    _ADDCLASSIFIERRESPONSE._serialized_end = 1842
    _REMOVECLASSIFIERREQUEST._serialized_start = 1844
    _REMOVECLASSIFIERREQUEST._serialized_end = 1930
    _REMOVECLASSIFIERRESPONSE._serialized_start = 1932
    _REMOVECLASSIFIERRESPONSE._serialized_end = 1958
    _GETCLASSIFICATIONSREQUEST._serialized_start = 1961
    _GETCLASSIFICATIONSREQUEST._serialized_end = 2160
    _GETCLASSIFICATIONSRESPONSE._serialized_start = 2162
    _GETCLASSIFICATIONSRESPONSE._serialized_end = 2272
    _GETCLASSIFICATIONSFROMCAMERAREQUEST._serialized_start = 2275
    _GETCLASSIFICATIONSFROMCAMERAREQUEST._serialized_end = 2420
    _GETCLASSIFICATIONSFROMCAMERARESPONSE._serialized_start = 2422
    _GETCLASSIFICATIONSFROMCAMERARESPONSE._serialized_end = 2542
    _CLASSIFICATION._serialized_start = 2544
    _CLASSIFICATION._serialized_end = 2623
    _GETSEGMENTERNAMESREQUEST._serialized_start = 2625
    _GETSEGMENTERNAMESREQUEST._serialized_end = 2671
    _GETSEGMENTERNAMESRESPONSE._serialized_start = 2673
    _GETSEGMENTERNAMESRESPONSE._serialized_end = 2741
    _ADDSEGMENTERREQUEST._serialized_start = 2744
    _ADDSEGMENTERREQUEST._serialized_end = 2950
    _ADDSEGMENTERRESPONSE._serialized_start = 2952
    _ADDSEGMENTERRESPONSE._serialized_end = 2974
    _REMOVESEGMENTERREQUEST._serialized_start = 2976
    _REMOVESEGMENTERREQUEST._serialized_end = 3059
    _REMOVESEGMENTERRESPONSE._serialized_start = 3061
    _REMOVESEGMENTERRESPONSE._serialized_end = 3086
    _GETOBJECTPOINTCLOUDSREQUEST._serialized_start = 3089
    _GETOBJECTPOINTCLOUDSREQUEST._serialized_end = 3239
    _GETOBJECTPOINTCLOUDSRESPONSE._serialized_start = 3241
    _GETOBJECTPOINTCLOUDSRESPONSE._serialized_end = 3360
    _VISIONSERVICE._serialized_start = 3363
    _VISIONSERVICE._serialized_end = 6141