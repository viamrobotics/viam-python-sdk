"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16app/data/v1/data.proto\x12\x10viam.app.data.v1\x1a\x19google/protobuf/any.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto"i\n\x0bDataRequest\x120\n\x06filter\x18\x01 \x01(\x0b2\x18.viam.app.data.v1.FilterR\x06filter\x12\x12\n\x04skip\x18\x02 \x01(\x03R\x04skip\x12\x14\n\x05limit\x18\x03 \x01(\x03R\x05limit"\xb1\x03\n\x06Filter\x12%\n\x0ecomponent_name\x18\x01 \x01(\tR\rcomponentName\x12%\n\x0ecomponent_type\x18\x02 \x01(\tR\rcomponentType\x12\'\n\x0fcomponent_model\x18\x03 \x01(\tR\x0ecomponentModel\x12\x16\n\x06method\x18\x04 \x01(\tR\x06method\x12\x12\n\x04tags\x18\x05 \x03(\tR\x04tags\x12\x1d\n\nrobot_name\x18\x06 \x01(\tR\trobotName\x12\x19\n\x08robot_id\x18\x07 \x01(\tR\x07robotId\x12\x1b\n\tpart_name\x18\x08 \x01(\tR\x08partName\x12\x17\n\x07part_id\x18\t \x01(\tR\x06partId\x12\x1f\n\x0blocation_id\x18\n \x01(\tR\nlocationId\x12\x17\n\x07org_ids\x18\x0b \x03(\tR\x06orgIds\x12\x1b\n\tmime_type\x18\x0c \x03(\tR\x08mimeType\x12=\n\x08interval\x18\r \x01(\x0b2!.viam.app.data.v1.CaptureIntervalR\x08interval"\xc3\x04\n\x0fCaptureMetadata\x12\x15\n\x06org_id\x18\x01 \x01(\tR\x05orgId\x12\x1f\n\x0blocation_id\x18\x02 \x01(\tR\nlocationId\x12\x1d\n\nrobot_name\x18\x03 \x01(\tR\trobotName\x12\x19\n\x08robot_id\x18\x04 \x01(\tR\x07robotId\x12\x1b\n\tpart_name\x18\x05 \x01(\tR\x08partName\x12\x17\n\x07part_id\x18\x06 \x01(\tR\x06partId\x12%\n\x0ecomponent_type\x18\x07 \x01(\tR\rcomponentType\x12\'\n\x0fcomponent_model\x18\x08 \x01(\tR\x0ecomponentModel\x12%\n\x0ecomponent_name\x18\t \x01(\tR\rcomponentName\x12\x1f\n\x0bmethod_name\x18\n \x01(\tR\nmethodName\x12d\n\x11method_parameters\x18\x0b \x03(\x0b27.viam.app.data.v1.CaptureMetadata.MethodParametersEntryR\x10methodParameters\x12\x12\n\x04tags\x18\x0c \x03(\tR\x04tags\x12\x1b\n\tmime_type\x18\r \x01(\tR\x08mimeType\x1aY\n\x15MethodParametersEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12*\n\x05value\x18\x02 \x01(\x0b2\x14.google.protobuf.AnyR\x05value:\x028\x01"q\n\x0fCaptureInterval\x120\n\x05start\x18\x01 \x01(\x0b2\x1a.google.protobuf.TimestampR\x05start\x12,\n\x03end\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampR\x03end"}\n\x1aTabularDataByFilterRequest\x12@\n\x0cdata_request\x18\x01 \x01(\x0b2\x1d.viam.app.data.v1.DataRequestR\x0bdataRequest\x12\x1d\n\ncount_only\x18\x02 \x01(\x08R\tcountOnly"\xa5\x01\n\x1bTabularDataByFilterResponse\x12=\n\x08metadata\x18\x01 \x03(\x0b2!.viam.app.data.v1.CaptureMetadataR\x08metadata\x121\n\x04data\x18\x02 \x03(\x0b2\x1d.viam.app.data.v1.TabularDataR\x04data\x12\x14\n\x05count\x18\x03 \x01(\x03R\x05count"\xe5\x01\n\x0bTabularData\x12+\n\x04data\x18\x01 \x01(\x0b2\x17.google.protobuf.StructR\x04data\x12%\n\x0emetadata_index\x18\x02 \x01(\x05R\rmetadataIndex\x12A\n\x0etime_requested\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampR\rtimeRequested\x12?\n\rtime_received\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampR\x0ctimeReceived"b\n\nBinaryData\x12\x16\n\x06binary\x18\x01 \x01(\x0cR\x06binary\x12<\n\x08metadata\x18\x02 \x01(\x0b2 .viam.app.data.v1.BinaryMetadataR\x08metadata"\xa3\x01\n\x19BinaryDataByFilterRequest\x12@\n\x0cdata_request\x18\x01 \x01(\x0b2\x1d.viam.app.data.v1.DataRequestR\x0bdataRequest\x12%\n\x0einclude_binary\x18\x02 \x01(\x08R\rincludeBinary\x12\x1d\n\ncount_only\x18\x03 \x01(\x08R\tcountOnly"d\n\x1aBinaryDataByFilterResponse\x120\n\x04data\x18\x01 \x03(\x0b2\x1c.viam.app.data.v1.BinaryDataR\x04data\x12\x14\n\x05count\x18\x02 \x01(\x03R\x05count"Z\n\x16BinaryDataByIDsRequest\x12\x19\n\x08file_ids\x18\x01 \x03(\tR\x07fileIds\x12%\n\x0einclude_binary\x18\x02 \x01(\x08R\rincludeBinary"a\n\x17BinaryDataByIDsResponse\x120\n\x04data\x18\x01 \x03(\x0b2\x1c.viam.app.data.v1.BinaryDataR\x04data\x12\x14\n\x05count\x18\x02 \x01(\x03R\x05count"\xbc\x02\n\x0eBinaryMetadata\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12L\n\x10capture_metadata\x18\x02 \x01(\x0b2!.viam.app.data.v1.CaptureMetadataR\x0fcaptureMetadata\x12A\n\x0etime_requested\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampR\rtimeRequested\x12?\n\rtime_received\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampR\x0ctimeReceived\x12\x1b\n\tfile_name\x18\x05 \x01(\tR\x08fileName\x12\x19\n\x08file_ext\x18\x06 \x01(\tR\x07fileExt\x12\x10\n\x03uri\x18\x07 \x01(\tR\x03uri2\xda\x02\n\x0bDataService\x12r\n\x13TabularDataByFilter\x12,.viam.app.data.v1.TabularDataByFilterRequest\x1a-.viam.app.data.v1.TabularDataByFilterResponse\x12o\n\x12BinaryDataByFilter\x12+.viam.app.data.v1.BinaryDataByFilterRequest\x1a,.viam.app.data.v1.BinaryDataByFilterResponse\x12f\n\x0fBinaryDataByIDs\x12(.viam.app.data.v1.BinaryDataByIDsRequest\x1a).viam.app.data.v1.BinaryDataByIDsResponseB\x1dZ\x1bgo.viam.com/api/app/data/v1b\x06proto3')
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
    _FILTER._serialized_end = 675
    _CAPTUREMETADATA._serialized_start = 678
    _CAPTUREMETADATA._serialized_end = 1257
    _CAPTUREMETADATA_METHODPARAMETERSENTRY._serialized_start = 1168
    _CAPTUREMETADATA_METHODPARAMETERSENTRY._serialized_end = 1257
    _CAPTUREINTERVAL._serialized_start = 1259
    _CAPTUREINTERVAL._serialized_end = 1372
    _TABULARDATABYFILTERREQUEST._serialized_start = 1374
    _TABULARDATABYFILTERREQUEST._serialized_end = 1499
    _TABULARDATABYFILTERRESPONSE._serialized_start = 1502
    _TABULARDATABYFILTERRESPONSE._serialized_end = 1667
    _TABULARDATA._serialized_start = 1670
    _TABULARDATA._serialized_end = 1899
    _BINARYDATA._serialized_start = 1901
    _BINARYDATA._serialized_end = 1999
    _BINARYDATABYFILTERREQUEST._serialized_start = 2002
    _BINARYDATABYFILTERREQUEST._serialized_end = 2165
    _BINARYDATABYFILTERRESPONSE._serialized_start = 2167
    _BINARYDATABYFILTERRESPONSE._serialized_end = 2267
    _BINARYDATABYIDSREQUEST._serialized_start = 2269
    _BINARYDATABYIDSREQUEST._serialized_end = 2359
    _BINARYDATABYIDSRESPONSE._serialized_start = 2361
    _BINARYDATABYIDSRESPONSE._serialized_end = 2458
    _BINARYMETADATA._serialized_start = 2461
    _BINARYMETADATA._serialized_end = 2777
    _DATASERVICE._serialized_start = 2780
    _DATASERVICE._serialized_end = 3126