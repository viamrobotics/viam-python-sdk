"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from ......proto.api.common.v1 import common_pb2 as proto_dot_api_dot_common_dot_v1_dot_common__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n;proto/api/service/objectdetection/v1/object_detection.proto\x12$proto.api.service.objectdetection.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a proto/api/common/v1/common.proto"\x16\n\x14DetectorNamesRequest">\n\x15DetectorNamesResponse\x12%\n\x0edetector_names\x18\x01 \x03(\tR\rdetectorNames"\xb3\x01\n\x12AddDetectorRequest\x12#\n\rdetector_name\x18\x01 \x01(\tR\x0cdetectorName\x12.\n\x13detector_model_type\x18\x02 \x01(\tR\x11detectorModelType\x12H\n\x13detector_parameters\x18\x03 \x01(\x0b2\x17.google.protobuf.StructR\x12detectorParameters"/\n\x13AddDetectorResponse\x12\x18\n\x07success\x18\x01 \x01(\x08R\x07success"U\n\rDetectRequest\x12\x1f\n\x0bcamera_name\x18\x01 \x01(\tR\ncameraName\x12#\n\rdetector_name\x18\x02 \x01(\tR\x0cdetectorName"a\n\x0eDetectResponse\x12O\n\ndetections\x18\x01 \x03(\x0b2/.proto.api.service.objectdetection.v1.DetectionR\ndetections"\x9e\x01\n\tDetection\x12\x13\n\x05x_min\x18\x01 \x01(\x03R\x04xMin\x12\x13\n\x05y_min\x18\x02 \x01(\x03R\x04yMin\x12\x13\n\x05x_max\x18\x03 \x01(\x03R\x04xMax\x12\x13\n\x05y_max\x18\x04 \x01(\x03R\x04yMax\x12\x1e\n\nconfidence\x18\x05 \x01(\x01R\nconfidence\x12\x1d\n\nclass_name\x18\x06 \x01(\tR\tclassName2\xce\x04\n\x16ObjectDetectionService\x12\xc6\x01\n\rDetectorNames\x12:.proto.api.service.objectdetection.v1.DetectorNamesRequest\x1a;.proto.api.service.objectdetection.v1.DetectorNamesResponse"<\x82\xd3\xe4\x93\x026\x124/viam/api/v1/service/object_detection/detector_names\x12\xbe\x01\n\x0bAddDetector\x128.proto.api.service.objectdetection.v1.AddDetectorRequest\x1a9.proto.api.service.objectdetection.v1.AddDetectorResponse":\x82\xd3\xe4\x93\x024"2/viam/api/v1/service/object_detection/add_detector\x12\xa9\x01\n\x06Detect\x123.proto.api.service.objectdetection.v1.DetectRequest\x1a4.proto.api.service.objectdetection.v1.DetectResponse"4\x82\xd3\xe4\x93\x02.",/viam/api/v1/service/object_detection/detectBi\n1com.viam.rdk.proto.api.service.objectdetection.v1Z4go.viam.com/rdk/proto/api/service/objectdetection/v1b\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'proto.api.service.objectdetection.v1.object_detection_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n1com.viam.rdk.proto.api.service.objectdetection.v1Z4go.viam.com/rdk/proto/api/service/objectdetection/v1'
    _OBJECTDETECTIONSERVICE.methods_by_name['DetectorNames']._options = None
    _OBJECTDETECTIONSERVICE.methods_by_name['DetectorNames']._serialized_options = b'\x82\xd3\xe4\x93\x026\x124/viam/api/v1/service/object_detection/detector_names'
    _OBJECTDETECTIONSERVICE.methods_by_name['AddDetector']._options = None
    _OBJECTDETECTIONSERVICE.methods_by_name['AddDetector']._serialized_options = b'\x82\xd3\xe4\x93\x024"2/viam/api/v1/service/object_detection/add_detector'
    _OBJECTDETECTIONSERVICE.methods_by_name['Detect']._options = None
    _OBJECTDETECTIONSERVICE.methods_by_name['Detect']._serialized_options = b'\x82\xd3\xe4\x93\x02.",/viam/api/v1/service/object_detection/detect'
    _DETECTORNAMESREQUEST._serialized_start = 195
    _DETECTORNAMESREQUEST._serialized_end = 217
    _DETECTORNAMESRESPONSE._serialized_start = 219
    _DETECTORNAMESRESPONSE._serialized_end = 281
    _ADDDETECTORREQUEST._serialized_start = 284
    _ADDDETECTORREQUEST._serialized_end = 463
    _ADDDETECTORRESPONSE._serialized_start = 465
    _ADDDETECTORRESPONSE._serialized_end = 512
    _DETECTREQUEST._serialized_start = 514
    _DETECTREQUEST._serialized_end = 599
    _DETECTRESPONSE._serialized_start = 601
    _DETECTRESPONSE._serialized_end = 698
    _DETECTION._serialized_start = 701
    _DETECTION._serialized_end = 859
    _OBJECTDETECTIONSERVICE._serialized_start = 862
    _OBJECTDETECTIONSERVICE._serialized_end = 1452