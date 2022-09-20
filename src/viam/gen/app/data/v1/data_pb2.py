"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16app/data/v1/data.proto\x12\x10viam.app.data.v1\x1a\x1fgoogle/protobuf/timestamp.proto"\xbc\x01\n\x0cQueryRequest\x123\n\x07filters\x18\x01 \x01(\x0b2\x19.viam.app.data.v1.FiltersR\x07filters\x12.\n\x04type\x18\x02 \x01(\x0e2\x1a.viam.app.data.v1.DataTypeR\x04type\x12\x12\n\x04skip\x18\x03 \x01(\x05R\x04skip\x12\x14\n\x05limit\x18\x04 \x01(\x05R\x05limit\x12\x1d\n\ncount_only\x18\x05 \x01(\x08R\tcountOnly"\x93\x03\n\x07Filters\x12%\n\x0ecomponent_name\x18\x01 \x01(\tR\rcomponentName\x12%\n\x0ecomponent_type\x18\x02 \x01(\tR\rcomponentType\x12\'\n\x0fcomponent_model\x18\x03 \x01(\tR\x0ecomponentModel\x12\x16\n\x06method\x18\x04 \x01(\tR\x06method\x12\x12\n\x04tags\x18\x05 \x03(\tR\x04tags\x12\x1d\n\nrobot_name\x18\x06 \x01(\tR\trobotName\x12\x19\n\x08robot_id\x18\x07 \x01(\tR\x07robotId\x12\x1b\n\tpart_name\x18\x08 \x01(\tR\x08partName\x12\x17\n\x07part_id\x18\t \x01(\tR\x06partId\x12\x1f\n\x0blocation_id\x18\n \x01(\tR\nlocationId\x12\x15\n\x06org_id\x18\x0b \x01(\tR\x05orgId\x12=\n\x08interval\x18\x0c \x01(\x0b2!.viam.app.data.v1.CaptureIntervalR\x08interval"q\n\x0fCaptureInterval\x120\n\x05start\x18\x01 \x01(\x0b2\x1a.google.protobuf.TimestampR\x05start\x12,\n\x03end\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampR\x03end"\xa1\x02\n\rQueryResponse\x12;\n\x07tabular\x18\x01 \x03(\x0b2!.viam.app.data.v1.TabularMetadataR\x07tabular\x128\n\x06binary\x18\x02 \x03(\x0b2 .viam.app.data.v1.BinaryMetadataR\x06binary\x122\n\x04file\x18\x03 \x03(\x0b2\x1e.viam.app.data.v1.FileMetadataR\x04file\x12#\n\rtabular_count\x18\x04 \x01(\x05R\x0ctabularCount\x12!\n\x0cbinary_count\x18\x05 \x01(\x05R\x0bbinaryCount\x12\x1d\n\nfile_count\x18\x06 \x01(\x05R\tfileCount"\xbe\x03\n\x0fTabularMetadata\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x1d\n\nrobot_name\x18\x02 \x01(\tR\trobotName\x12\x19\n\x08robot_id\x18\x03 \x01(\tR\x07robotId\x12\x1b\n\tpart_name\x18\x04 \x01(\tR\x08partName\x12\x17\n\x07part_id\x18\x05 \x01(\tR\x06partId\x12%\n\x0ecomponent_name\x18\x06 \x01(\tR\rcomponentName\x12%\n\x0ecomponent_type\x18\x07 \x01(\tR\rcomponentType\x12\'\n\x0fcomponent_model\x18\x08 \x01(\tR\x0ecomponentModel\x12\x16\n\x06method\x18\t \x01(\tR\x06method\x12\x12\n\x04tags\x18\n \x03(\tR\x04tags\x12=\n\x08interval\x18\x0b \x01(\x0b2!.viam.app.data.v1.CaptureIntervalR\x08interval\x12&\n\x0ffile_size_bytes\x18\x0c \x01(\x05R\rfileSizeBytes\x12!\n\x0cnum_readings\x18\r \x01(\x05R\x0bnumReadings"\xb3\x03\n\x0eBinaryMetadata\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x1d\n\nrobot_name\x18\x02 \x01(\tR\trobotName\x12\x19\n\x08robot_id\x18\x03 \x01(\tR\x07robotId\x12\x1b\n\tpart_name\x18\x04 \x01(\tR\x08partName\x12\x17\n\x07part_id\x18\x05 \x01(\tR\x06partId\x12%\n\x0ecomponent_name\x18\x06 \x01(\tR\rcomponentName\x12%\n\x0ecomponent_type\x18\x07 \x01(\tR\rcomponentType\x12\'\n\x0fcomponent_model\x18\x08 \x01(\tR\x0ecomponentModel\x12\x16\n\x06method\x18\t \x01(\tR\x06method\x12\x12\n\x04tags\x18\n \x03(\tR\x04tags\x12=\n\x08interval\x18\x0b \x01(\x0b2!.viam.app.data.v1.CaptureIntervalR\x08interval\x12&\n\x0ffile_size_bytes\x18\x0c \x01(\x05R\rfileSizeBytes\x12\x17\n\x07file_id\x18\r \x01(\tR\x06fileId"\x88\x02\n\x0cFileMetadata\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x1d\n\nrobot_name\x18\x02 \x01(\tR\trobotName\x12\x19\n\x08robot_id\x18\x03 \x01(\tR\x07robotId\x12\x1b\n\tpart_name\x18\x04 \x01(\tR\x08partName\x12\x17\n\x07part_id\x18\x05 \x01(\tR\x06partId\x127\n\tsync_time\x18\x06 \x01(\x0b2\x1a.google.protobuf.TimestampR\x08syncTime\x12&\n\x0ffile_size_bytes\x18\x07 \x01(\x05R\rfileSizeBytes\x12\x17\n\x07file_id\x18\x08 \x01(\tR\x06fileId*t\n\x08DataType\x12\x19\n\x15DATA_TYPE_UNSPECIFIED\x10\x00\x12\x1b\n\x17DATA_TYPE_BINARY_SENSOR\x10\x01\x12\x1c\n\x18DATA_TYPE_TABULAR_SENSOR\x10\x02\x12\x12\n\x0eDATA_TYPE_FILE\x10\x032W\n\x0bDataService\x12H\n\x05Query\x12\x1e.viam.app.data.v1.QueryRequest\x1a\x1f.viam.app.data.v1.QueryResponseB\x1dZ\x1bgo.viam.com/api/app/data/v1b\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'app.data.v1.data_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z\x1bgo.viam.com/api/app/data/v1'
    _DATATYPE._serialized_start = 2235
    _DATATYPE._serialized_end = 2351
    _QUERYREQUEST._serialized_start = 78
    _QUERYREQUEST._serialized_end = 266
    _FILTERS._serialized_start = 269
    _FILTERS._serialized_end = 672
    _CAPTUREINTERVAL._serialized_start = 674
    _CAPTUREINTERVAL._serialized_end = 787
    _QUERYRESPONSE._serialized_start = 790
    _QUERYRESPONSE._serialized_end = 1079
    _TABULARMETADATA._serialized_start = 1082
    _TABULARMETADATA._serialized_end = 1528
    _BINARYMETADATA._serialized_start = 1531
    _BINARYMETADATA._serialized_end = 1966
    _FILEMETADATA._serialized_start = 1969
    _FILEMETADATA._serialized_end = 2233
    _DATASERVICE._serialized_start = 2353
    _DATASERVICE._serialized_end = 2440