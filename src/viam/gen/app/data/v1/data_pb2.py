"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16app/data/v1/data.proto\x12\x10viam.app.data.v1\x1a\x19google/protobuf/any.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto"i\n\x0bDataRequest\x120\n\x06filter\x18\x01 \x01(\x0b2\x18.viam.app.data.v1.FilterR\x06filter\x12\x12\n\x04skip\x18\x02 \x01(\x05R\x04skip\x12\x14\n\x05limit\x18\x03 \x01(\x05R\x05limit"\xaf\x03\n\x06Filter\x12%\n\x0ecomponent_name\x18\x01 \x01(\tR\rcomponentName\x12%\n\x0ecomponent_type\x18\x02 \x01(\tR\rcomponentType\x12\'\n\x0fcomponent_model\x18\x03 \x01(\tR\x0ecomponentModel\x12\x16\n\x06method\x18\x04 \x01(\tR\x06method\x12\x12\n\x04tags\x18\x05 \x03(\tR\x04tags\x12\x1d\n\nrobot_name\x18\x06 \x01(\tR\trobotName\x12\x19\n\x08robot_id\x18\x07 \x01(\tR\x07robotId\x12\x1b\n\tpart_name\x18\x08 \x01(\tR\x08partName\x12\x17\n\x07part_id\x18\t \x01(\tR\x06partId\x12\x1f\n\x0blocation_id\x18\n \x01(\tR\nlocationId\x12\x15\n\x06org_id\x18\x0b \x01(\tR\x05orgId\x12\x1b\n\tmime_type\x18\x0c \x03(\tR\x08mimeType\x12=\n\x08interval\x18\r \x01(\x0b2!.viam.app.data.v1.CaptureIntervalR\x08interval"\xac\x04\n\x0fCaptureMetadata\x12\x1f\n\x0blocation_id\x18\x01 \x01(\tR\nlocationId\x12\x1d\n\nrobot_name\x18\x02 \x01(\tR\trobotName\x12\x19\n\x08robot_id\x18\x03 \x01(\tR\x07robotId\x12\x1b\n\tpart_name\x18\x04 \x01(\tR\x08partName\x12\x17\n\x07part_id\x18\x05 \x01(\tR\x06partId\x12%\n\x0ecomponent_type\x18\x06 \x01(\tR\rcomponentType\x12\'\n\x0fcomponent_model\x18\x07 \x01(\tR\x0ecomponentModel\x12%\n\x0ecomponent_name\x18\x08 \x01(\tR\rcomponentName\x12\x1f\n\x0bmethod_name\x18\t \x01(\tR\nmethodName\x12d\n\x11method_parameters\x18\n \x03(\x0b27.viam.app.data.v1.CaptureMetadata.MethodParametersEntryR\x10methodParameters\x12\x12\n\x04tags\x18\x0b \x03(\tR\x04tags\x12\x1b\n\tmime_type\x18\x0c \x01(\tR\x08mimeType\x1aY\n\x15MethodParametersEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12*\n\x05value\x18\x02 \x01(\x0b2\x14.google.protobuf.AnyR\x05value:\x028\x01"q\n\x0fCaptureInterval\x120\n\x05start\x18\x01 \x01(\x0b2\x1a.google.protobuf.TimestampR\x05start\x12,\n\x03end\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampR\x03end"}\n\x1aTabularDataByFilterRequest\x12@\n\x0cdata_request\x18\x01 \x01(\x0b2\x1d.viam.app.data.v1.DataRequestR\x0bdataRequest\x12\x1d\n\ncount_only\x18\x02 \x01(\x08R\tcountOnly"\xa5\x01\n\x1bTabularDataByFilterResponse\x12=\n\x08metadata\x18\x01 \x03(\x0b2!.viam.app.data.v1.CaptureMetadataR\x08metadata\x121\n\x04data\x18\x02 \x03(\x0b2\x1d.viam.app.data.v1.TabularDataR\x04data\x12\x14\n\x05count\x18\x03 \x01(\x03R\x05count"\xe5\x01\n\x0bTabularData\x12+\n\x04data\x18\x01 \x01(\x0b2\x17.google.protobuf.StructR\x04data\x12%\n\x0emetadata_index\x18\x02 \x01(\x05R\rmetadataIndex\x12A\n\x0etime_requested\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampR\rtimeRequested\x12?\n\rtime_received\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampR\x0ctimeReceived"\xf1\x01\n\nBinaryData\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x10\n\x03uri\x18\x02 \x01(\tR\x03uri\x12\x16\n\x06binary\x18\x03 \x01(\x0cR\x06binary\x12%\n\x0emetadata_index\x18\x04 \x01(\x05R\rmetadataIndex\x12A\n\x0etime_requested\x18\x05 \x01(\x0b2\x1a.google.protobuf.TimestampR\rtimeRequested\x12?\n\rtime_received\x18\x06 \x01(\x0b2\x1a.google.protobuf.TimestampR\x0ctimeReceived"\xa3\x01\n\x19BinaryDataByFilterRequest\x12@\n\x0cdata_request\x18\x01 \x01(\x0b2\x1d.viam.app.data.v1.DataRequestR\x0bdataRequest\x12%\n\x0einclude_binary\x18\x02 \x01(\x08R\rincludeBinary\x12\x1d\n\ncount_only\x18\x03 \x01(\x08R\tcountOnly"\xa3\x01\n\x1aBinaryDataByFilterResponse\x12=\n\x08metadata\x18\x01 \x03(\x0b2!.viam.app.data.v1.CaptureMetadataR\x08metadata\x120\n\x04data\x18\x02 \x03(\x0b2\x1c.viam.app.data.v1.BinaryDataR\x04data\x12\x14\n\x05count\x18\x03 \x01(\x03R\x05count"Z\n\x16BinaryDataByIDsRequest\x12\x19\n\x08file_ids\x18\x01 \x03(\tR\x07fileIds\x12%\n\x0einclude_binary\x18\x02 \x01(\x08R\rincludeBinary"\xa0\x01\n\x17BinaryDataByIDsResponse\x12=\n\x08metadata\x18\x01 \x03(\x0b2!.viam.app.data.v1.CaptureMetadataR\x08metadata\x120\n\x04data\x18\x02 \x03(\x0b2\x1c.viam.app.data.v1.BinaryDataR\x04data\x12\x14\n\x05count\x18\x03 \x01(\x03R\x05count2\xda\x02\n\x0bDataService\x12r\n\x13TabularDataByFilter\x12,.viam.app.data.v1.TabularDataByFilterRequest\x1a-.viam.app.data.v1.TabularDataByFilterResponse\x12o\n\x12BinaryDataByFilter\x12+.viam.app.data.v1.BinaryDataByFilterRequest\x1a,.viam.app.data.v1.BinaryDataByFilterResponse\x12f\n\x0fBinaryDataByIDs\x12(.viam.app.data.v1.BinaryDataByIDsRequest\x1a).viam.app.data.v1.BinaryDataByIDsResponseB\x1dZ\x1bgo.viam.com/api/app/data/v1b\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'app.data.v1.data_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z\x1bgo.viam.com/api/app/data/v1'
    _CAPTUREMETADATA_METHODPARAMETERSENTRY._options = None
    _CAPTUREMETADATA_METHODPARAMETERSENTRY._serialized_options = b'8\x01'
    _DATAREQUEST._serialized_start = 134
    _DATAREQUEST._serialized_end = 239
    _FILTER._serialized_start = 242
    _FILTER._serialized_end = 673
    _CAPTUREMETADATA._serialized_start = 676
    _CAPTUREMETADATA._serialized_end = 1232
    _CAPTUREMETADATA_METHODPARAMETERSENTRY._serialized_start = 1143
    _CAPTUREMETADATA_METHODPARAMETERSENTRY._serialized_end = 1232
    _CAPTUREINTERVAL._serialized_start = 1234
    _CAPTUREINTERVAL._serialized_end = 1347
    _TABULARDATABYFILTERREQUEST._serialized_start = 1349
    _TABULARDATABYFILTERREQUEST._serialized_end = 1474
    _TABULARDATABYFILTERRESPONSE._serialized_start = 1477
    _TABULARDATABYFILTERRESPONSE._serialized_end = 1642
    _TABULARDATA._serialized_start = 1645
    _TABULARDATA._serialized_end = 1874
    _BINARYDATA._serialized_start = 1877
    _BINARYDATA._serialized_end = 2118
    _BINARYDATABYFILTERREQUEST._serialized_start = 2121
    _BINARYDATABYFILTERREQUEST._serialized_end = 2284
    _BINARYDATABYFILTERRESPONSE._serialized_start = 2287
    _BINARYDATABYFILTERRESPONSE._serialized_end = 2450
    _BINARYDATABYIDSREQUEST._serialized_start = 2452
    _BINARYDATABYIDSREQUEST._serialized_end = 2542
    _BINARYDATABYIDSRESPONSE._serialized_start = 2545
    _BINARYDATABYIDSRESPONSE._serialized_end = 2705
    _DATASERVICE._serialized_start = 2708
    _DATASERVICE._serialized_end = 3054