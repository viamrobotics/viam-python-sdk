"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from ......proto.api.common.v1 import common_pb2 as proto_dot_api_dot_common_dot_v1_dot_common__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(proto/api/service/vision/v1/vision.proto\x12\x1bproto.api.service.vision.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a proto/api/common/v1/common.proto"S\n\x1eGetModelParameterSchemaRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x1d\n\nmodel_type\x18\x02 \x01(\tR\tmodelType"W\n\x1fGetModelParameterSchemaResponse\x124\n\x16model_parameter_schema\x18\x01 \x01(\x0cR\x14modelParameterSchema"-\n\x17GetDetectorNamesRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name"A\n\x18GetDetectorNamesResponse\x12%\n\x0edetector_names\x18\x01 \x03(\tR\rdetectorNames"\xc7\x01\n\x12AddDetectorRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12#\n\rdetector_name\x18\x02 \x01(\tR\x0cdetectorName\x12.\n\x13detector_model_type\x18\x03 \x01(\tR\x11detectorModelType\x12H\n\x13detector_parameters\x18\x04 \x01(\x0b2\x17.google.protobuf.StructR\x12detectorParameters"\x15\n\x13AddDetectorResponse"P\n\x15RemoveDetectorRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12#\n\rdetector_name\x18\x02 \x01(\tR\x0cdetectorName"\x18\n\x16RemoveDetectorResponse"\xb0\x01\n\x14GetDetectionsRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x14\n\x05image\x18\x02 \x01(\x0cR\x05image\x12\x14\n\x05width\x18\x03 \x01(\x03R\x05width\x12\x16\n\x06height\x18\x04 \x01(\x03R\x06height\x12\x1b\n\tmime_type\x18\x05 \x01(\tR\x08mimeType\x12#\n\rdetector_name\x18\x06 \x01(\tR\x0cdetectorName"_\n\x15GetDetectionsResponse\x12F\n\ndetections\x18\x01 \x03(\x0b2&.proto.api.service.vision.v1.DetectionR\ndetections"z\n\x1eGetDetectionsFromCameraRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x1f\n\x0bcamera_name\x18\x02 \x01(\tR\ncameraName\x12#\n\rdetector_name\x18\x03 \x01(\tR\x0cdetectorName"i\n\x1fGetDetectionsFromCameraResponse\x12F\n\ndetections\x18\x01 \x03(\x0b2&.proto.api.service.vision.v1.DetectionR\ndetections"\xda\x01\n\tDetection\x12\x18\n\x05x_min\x18\x01 \x01(\x03H\x00R\x04xMin\x88\x01\x01\x12\x18\n\x05y_min\x18\x02 \x01(\x03H\x01R\x04yMin\x88\x01\x01\x12\x18\n\x05x_max\x18\x03 \x01(\x03H\x02R\x04xMax\x88\x01\x01\x12\x18\n\x05y_max\x18\x04 \x01(\x03H\x03R\x04yMax\x88\x01\x01\x12\x1e\n\nconfidence\x18\x05 \x01(\x01R\nconfidence\x12\x1d\n\nclass_name\x18\x06 \x01(\tR\tclassNameB\x08\n\x06_x_minB\x08\n\x06_y_minB\x08\n\x06_x_maxB\x08\n\x06_y_max"/\n\x19GetClassifierNamesRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name"G\n\x1aGetClassifierNamesResponse\x12)\n\x10classifier_names\x18\x01 \x03(\tR\x0fclassifierNames"\xd5\x01\n\x14AddClassifierRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\'\n\x0fclassifier_name\x18\x02 \x01(\tR\x0eclassifierName\x122\n\x15classifier_model_type\x18\x03 \x01(\tR\x13classifierModelType\x12L\n\x15classifier_parameters\x18\x04 \x01(\x0b2\x17.google.protobuf.StructR\x14classifierParameters"\x17\n\x15AddClassifierResponse"V\n\x17RemoveClassifierRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\'\n\x0fclassifier_name\x18\x02 \x01(\tR\x0eclassifierName"\x1a\n\x18RemoveClassifierResponse"\xc7\x01\n\x19GetClassificationsRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x14\n\x05image\x18\x02 \x01(\x0cR\x05image\x12\x14\n\x05width\x18\x03 \x01(\x05R\x05width\x12\x16\n\x06height\x18\x04 \x01(\x05R\x06height\x12\x1b\n\tmime_type\x18\x05 \x01(\tR\x08mimeType\x12\'\n\x0fclassifier_name\x18\x06 \x01(\tR\x0eclassifierName\x12\x0c\n\x01n\x18\x07 \x01(\x05R\x01n"s\n\x1aGetClassificationsResponse\x12U\n\x0fclassifications\x18\x01 \x03(\x0b2+.proto.api.service.vision.v1.ClassificationR\x0fclassifications"\x91\x01\n#GetClassificationsFromCameraRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x1f\n\x0bcamera_name\x18\x02 \x01(\tR\ncameraName\x12\'\n\x0fclassifier_name\x18\x03 \x01(\tR\x0eclassifierName\x12\x0c\n\x01n\x18\x04 \x01(\x05R\x01n"}\n$GetClassificationsFromCameraResponse\x12U\n\x0fclassifications\x18\x01 \x03(\x0b2+.proto.api.service.vision.v1.ClassificationR\x0fclassifications"O\n\x0eClassification\x12\x1d\n\nclass_name\x18\x01 \x01(\tR\tclassName\x12\x1e\n\nconfidence\x18\x02 \x01(\x01R\nconfidence".\n\x18GetSegmenterNamesRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name"D\n\x19GetSegmenterNamesResponse\x12\'\n\x0fsegmenter_names\x18\x01 \x03(\tR\x0esegmenterNames"\xce\x01\n\x13AddSegmenterRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12%\n\x0esegmenter_name\x18\x02 \x01(\tR\rsegmenterName\x120\n\x14segmenter_model_type\x18\x03 \x01(\tR\x12segmenterModelType\x12J\n\x14segmenter_parameters\x18\x04 \x01(\x0b2\x17.google.protobuf.StructR\x13segmenterParameters"\x16\n\x14AddSegmenterResponse"S\n\x16RemoveSegmenterRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12%\n\x0esegmenter_name\x18\x02 \x01(\tR\rsegmenterName"\x19\n\x17RemoveSegmenterResponse"\x96\x01\n\x1bGetObjectPointCloudsRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x1f\n\x0bcamera_name\x18\x02 \x01(\tR\ncameraName\x12%\n\x0esegmenter_name\x18\x03 \x01(\tR\rsegmenterName\x12\x1b\n\tmime_type\x18\x04 \x01(\tR\x08mimeType"|\n\x1cGetObjectPointCloudsResponse\x12\x1b\n\tmime_type\x18\x01 \x01(\tR\x08mimeType\x12?\n\x07objects\x18\x02 \x03(\x0b2%.proto.api.common.v1.PointCloudObjectR\x07objects2\xf0\x16\n\rVisionService\x12\xd7\x01\n\x17GetModelParameterSchema\x12;.proto.api.service.vision.v1.GetModelParameterSchemaRequest\x1a<.proto.api.service.vision.v1.GetModelParameterSchemaResponse"A\x82\xd3\xe4\x93\x02;\x129/viam/api/v1/service/vision/{name}/model_parameter_schema\x12\xba\x01\n\x10GetDetectorNames\x124.proto.api.service.vision.v1.GetDetectorNamesRequest\x1a5.proto.api.service.vision.v1.GetDetectorNamesResponse"9\x82\xd3\xe4\x93\x023\x121/viam/api/v1/service/vision/{name}/detector_names\x12\xa9\x01\n\x0bAddDetector\x12/.proto.api.service.vision.v1.AddDetectorRequest\x1a0.proto.api.service.vision.v1.AddDetectorResponse"7\x82\xd3\xe4\x93\x021"//viam/api/v1/service/vision/{name}/add_detector\x12\xb5\x01\n\x0eRemoveDetector\x122.proto.api.service.vision.v1.RemoveDetectorRequest\x1a3.proto.api.service.vision.v1.RemoveDetectorResponse":\x82\xd3\xe4\x93\x024"2/viam/api/v1/service/vision/{name}/remove_detector\x12\xd2\x01\n\x17GetDetectionsFromCamera\x12;.proto.api.service.vision.v1.GetDetectionsFromCameraRequest\x1a<.proto.api.service.vision.v1.GetDetectionsFromCameraResponse"<\x82\xd3\xe4\x93\x026"4/viam/api/v1/service/vision/{name}/camera_detections\x12\xad\x01\n\rGetDetections\x121.proto.api.service.vision.v1.GetDetectionsRequest\x1a2.proto.api.service.vision.v1.GetDetectionsResponse"5\x82\xd3\xe4\x93\x02/"-/viam/api/v1/service/vision/{name}/detections\x12\xc2\x01\n\x12GetClassifierNames\x126.proto.api.service.vision.v1.GetClassifierNamesRequest\x1a7.proto.api.service.vision.v1.GetClassifierNamesResponse";\x82\xd3\xe4\x93\x025\x123/viam/api/v1/service/vision/{name}/classifier_names\x12\xb1\x01\n\rAddClassifier\x121.proto.api.service.vision.v1.AddClassifierRequest\x1a2.proto.api.service.vision.v1.AddClassifierResponse"9\x82\xd3\xe4\x93\x023"1/viam/api/v1/service/vision/{name}/add_classifier\x12\xbd\x01\n\x10RemoveClassifier\x124.proto.api.service.vision.v1.RemoveClassifierRequest\x1a5.proto.api.service.vision.v1.RemoveClassifierResponse"<\x82\xd3\xe4\x93\x026"4/viam/api/v1/service/vision/{name}/remove_classifier\x12\xe6\x01\n\x1cGetClassificationsFromCamera\x12@.proto.api.service.vision.v1.GetClassificationsFromCameraRequest\x1aA.proto.api.service.vision.v1.GetClassificationsFromCameraResponse"A\x82\xd3\xe4\x93\x02;"9/viam/api/v1/service/vision/{name}/camera_classifications\x12\xc1\x01\n\x12GetClassifications\x126.proto.api.service.vision.v1.GetClassificationsRequest\x1a7.proto.api.service.vision.v1.GetClassificationsResponse":\x82\xd3\xe4\x93\x024"2/viam/api/v1/service/vision/{name}/classifications\x12\xbe\x01\n\x11GetSegmenterNames\x125.proto.api.service.vision.v1.GetSegmenterNamesRequest\x1a6.proto.api.service.vision.v1.GetSegmenterNamesResponse":\x82\xd3\xe4\x93\x024\x122/viam/api/v1/service/vision/{name}/segmenter_names\x12\xad\x01\n\x0cAddSegmenter\x120.proto.api.service.vision.v1.AddSegmenterRequest\x1a1.proto.api.service.vision.v1.AddSegmenterResponse"8\x82\xd3\xe4\x93\x022"0/viam/api/v1/service/vision/{name}/add_segmenter\x12\xb9\x01\n\x0fRemoveSegmenter\x123.proto.api.service.vision.v1.RemoveSegmenterRequest\x1a4.proto.api.service.vision.v1.RemoveSegmenterResponse";\x82\xd3\xe4\x93\x025"3/viam/api/v1/service/vision/{name}/remove_segmenter\x12\xcb\x01\n\x14GetObjectPointClouds\x128.proto.api.service.vision.v1.GetObjectPointCloudsRequest\x1a9.proto.api.service.vision.v1.GetObjectPointCloudsResponse">\x82\xd3\xe4\x93\x028"6/viam/api/v1/service/vision/{name}/object_point_cloudsBW\n(com.viam.rdk.proto.api.service.vision.v1Z+go.viam.com/rdk/proto/api/service/vision/v1b\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'proto.api.service.vision.v1.vision_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n(com.viam.rdk.proto.api.service.vision.v1Z+go.viam.com/rdk/proto/api/service/vision/v1'
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
    _GETMODELPARAMETERSCHEMAREQUEST._serialized_start = 167
    _GETMODELPARAMETERSCHEMAREQUEST._serialized_end = 250
    _GETMODELPARAMETERSCHEMARESPONSE._serialized_start = 252
    _GETMODELPARAMETERSCHEMARESPONSE._serialized_end = 339
    _GETDETECTORNAMESREQUEST._serialized_start = 341
    _GETDETECTORNAMESREQUEST._serialized_end = 386
    _GETDETECTORNAMESRESPONSE._serialized_start = 388
    _GETDETECTORNAMESRESPONSE._serialized_end = 453
    _ADDDETECTORREQUEST._serialized_start = 456
    _ADDDETECTORREQUEST._serialized_end = 655
    _ADDDETECTORRESPONSE._serialized_start = 657
    _ADDDETECTORRESPONSE._serialized_end = 678
    _REMOVEDETECTORREQUEST._serialized_start = 680
    _REMOVEDETECTORREQUEST._serialized_end = 760
    _REMOVEDETECTORRESPONSE._serialized_start = 762
    _REMOVEDETECTORRESPONSE._serialized_end = 786
    _GETDETECTIONSREQUEST._serialized_start = 789
    _GETDETECTIONSREQUEST._serialized_end = 965
    _GETDETECTIONSRESPONSE._serialized_start = 967
    _GETDETECTIONSRESPONSE._serialized_end = 1062
    _GETDETECTIONSFROMCAMERAREQUEST._serialized_start = 1064
    _GETDETECTIONSFROMCAMERAREQUEST._serialized_end = 1186
    _GETDETECTIONSFROMCAMERARESPONSE._serialized_start = 1188
    _GETDETECTIONSFROMCAMERARESPONSE._serialized_end = 1293
    _DETECTION._serialized_start = 1296
    _DETECTION._serialized_end = 1514
    _GETCLASSIFIERNAMESREQUEST._serialized_start = 1516
    _GETCLASSIFIERNAMESREQUEST._serialized_end = 1563
    _GETCLASSIFIERNAMESRESPONSE._serialized_start = 1565
    _GETCLASSIFIERNAMESRESPONSE._serialized_end = 1636
    _ADDCLASSIFIERREQUEST._serialized_start = 1639
    _ADDCLASSIFIERREQUEST._serialized_end = 1852
    _ADDCLASSIFIERRESPONSE._serialized_start = 1854
    _ADDCLASSIFIERRESPONSE._serialized_end = 1877
    _REMOVECLASSIFIERREQUEST._serialized_start = 1879
    _REMOVECLASSIFIERREQUEST._serialized_end = 1965
    _REMOVECLASSIFIERRESPONSE._serialized_start = 1967
    _REMOVECLASSIFIERRESPONSE._serialized_end = 1993
    _GETCLASSIFICATIONSREQUEST._serialized_start = 1996
    _GETCLASSIFICATIONSREQUEST._serialized_end = 2195
    _GETCLASSIFICATIONSRESPONSE._serialized_start = 2197
    _GETCLASSIFICATIONSRESPONSE._serialized_end = 2312
    _GETCLASSIFICATIONSFROMCAMERAREQUEST._serialized_start = 2315
    _GETCLASSIFICATIONSFROMCAMERAREQUEST._serialized_end = 2460
    _GETCLASSIFICATIONSFROMCAMERARESPONSE._serialized_start = 2462
    _GETCLASSIFICATIONSFROMCAMERARESPONSE._serialized_end = 2587
    _CLASSIFICATION._serialized_start = 2589
    _CLASSIFICATION._serialized_end = 2668
    _GETSEGMENTERNAMESREQUEST._serialized_start = 2670
    _GETSEGMENTERNAMESREQUEST._serialized_end = 2716
    _GETSEGMENTERNAMESRESPONSE._serialized_start = 2718
    _GETSEGMENTERNAMESRESPONSE._serialized_end = 2786
    _ADDSEGMENTERREQUEST._serialized_start = 2789
    _ADDSEGMENTERREQUEST._serialized_end = 2995
    _ADDSEGMENTERRESPONSE._serialized_start = 2997
    _ADDSEGMENTERRESPONSE._serialized_end = 3019
    _REMOVESEGMENTERREQUEST._serialized_start = 3021
    _REMOVESEGMENTERREQUEST._serialized_end = 3104
    _REMOVESEGMENTERRESPONSE._serialized_start = 3106
    _REMOVESEGMENTERRESPONSE._serialized_end = 3131
    _GETOBJECTPOINTCLOUDSREQUEST._serialized_start = 3134
    _GETOBJECTPOINTCLOUDSREQUEST._serialized_end = 3284
    _GETOBJECTPOINTCLOUDSRESPONSE._serialized_start = 3286
    _GETOBJECTPOINTCLOUDSRESPONSE._serialized_end = 3410
    _VISIONSERVICE._serialized_start = 3413
    _VISIONSERVICE._serialized_end = 6341