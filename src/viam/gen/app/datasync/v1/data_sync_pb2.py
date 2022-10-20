"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from ....tagger.v1 import tagger_pb2 as tagger_dot_v1_dot_tagger__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1fapp/datasync/v1/data_sync.proto\x12\x14viam.app.datasync.v1\x1a\x19google/protobuf/any.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x16tagger/v1/tagger.proto"\x94\x01\n\x0eSensorMetadata\x12A\n\x0etime_requested\x18\x01 \x01(\x0b2\x1a.google.protobuf.TimestampR\rtimeRequested\x12?\n\rtime_received\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampR\x0ctimeReceived"\xa3\x01\n\nSensorData\x12@\n\x08metadata\x18\x01 \x01(\x0b2$.viam.app.datasync.v1.SensorMetadataR\x08metadata\x121\n\x06struct\x18\x02 \x01(\x0b2\x17.google.protobuf.StructH\x00R\x06struct\x12\x18\n\x06binary\x18\x03 \x01(\x0cH\x00R\x06binaryB\x06\n\x04data"\x1e\n\x08FileData\x12\x12\n\x04data\x18\x01 \x01(\x0cR\x04data"\xb0\x04\n\x0eUploadMetadata\x12\x17\n\x07part_id\x18\x01 \x01(\tR\x06partId\x12%\n\x0ecomponent_type\x18\x02 \x01(\tR\rcomponentType\x12%\n\x0ecomponent_name\x18\x03 \x01(\tR\rcomponentName\x12\'\n\x0fcomponent_model\x18\x04 \x01(\tR\x0ecomponentModel\x12\x1f\n\x0bmethod_name\x18\x05 \x01(\tR\nmethodName\x122\n\x04type\x18\x06 \x01(\x0e2\x1e.viam.app.datasync.v1.DataTypeR\x04type\x12\x1b\n\tfile_name\x18\x07 \x01(\tR\x08fileName\x12g\n\x11method_parameters\x18\x08 \x03(\x0b2:.viam.app.datasync.v1.UploadMetadata.MethodParametersEntryR\x10methodParameters\x12%\n\x0efile_extension\x18\t \x01(\tR\rfileExtension\x12\x12\n\x04tags\x18\n \x03(\tR\x04tags\x12\x1d\n\nsession_id\x18\x0b \x01(\tR\tsessionId\x1aY\n\x15MethodParametersEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12*\n\x05value\x18\x02 \x01(\x0b2\x14.google.protobuf.AnyR\x05value:\x028\x01"\xf8\x01\n\rUploadRequest\x12B\n\x08metadata\x18\x01 \x01(\x0b2$.viam.app.datasync.v1.UploadMetadataH\x00R\x08metadata\x12K\n\x0fsensor_contents\x18\x02 \x01(\x0b2 .viam.app.datasync.v1.SensorDataH\x00R\x0esensorContents\x12E\n\rfile_contents\x18\x03 \x01(\x0b2\x1e.viam.app.datasync.v1.FileDataH\x00R\x0cfileContentsB\x0f\n\rupload_packet";\n\x0eUploadResponse\x12)\n\x10requests_written\x18\x01 \x01(\x05R\x0frequestsWritten"q\n\x0fCaptureInterval\x120\n\x05start\x18\x01 \x01(\x0b2\x1a.google.protobuf.TimestampR\x05start\x12,\n\x03end\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampR\x03end"\x84\x04\n\x13DataCaptureMetadata\x12%\n\x0ecomponent_type\x18\x01 \x01(\tR\rcomponentType\x12%\n\x0ecomponent_name\x18\x02 \x01(\tR\rcomponentName\x12\'\n\x0fcomponent_model\x18\x03 \x01(\tR\x0ecomponentModel\x12\x1f\n\x0bmethod_name\x18\x04 \x01(\tR\nmethodName\x122\n\x04type\x18\x05 \x01(\x0e2\x1e.viam.app.datasync.v1.DataTypeR\x04type\x12l\n\x11method_parameters\x18\x06 \x03(\x0b2?.viam.app.datasync.v1.DataCaptureMetadata.MethodParametersEntryR\x10methodParameters\x12%\n\x0efile_extension\x18\x07 \x01(\tR\rfileExtension\x12\x12\n\x04tags\x18\x08 \x03(\tR\x04tags\x12\x1d\n\nsession_id\x18\t \x01(\tR\tsessionId\x1aY\n\x15MethodParametersEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12*\n\x05value\x18\x02 \x01(\x0b2\x14.google.protobuf.AnyR\x05value:\x028\x01"\x9a\x0c\n\x0eTabularCapture\x12g\n\x08interval\x18\x01 \x01(\x0b2%.viam.app.datasync.v1.CaptureIntervalB$\x9a\x84\x9e\x03\x1fbson:"interval" json:"interval"R\x08interval\x127\n\x06org_id\x18\x02 \x01(\tB \x9a\x84\x9e\x03\x1bbson:"org_id" json:"org_id"R\x05orgId\x12?\n\x08robot_id\x18\x03 \x01(\tB$\x9a\x84\x9e\x03\x1fbson:"robot_id" json:"robot_id"R\x07robotId\x12;\n\x07part_id\x18\x04 \x01(\tB"\x9a\x84\x9e\x03\x1dbson:"part_id" json:"part_id"R\x06partId\x12K\n\x0blocation_id\x18\x05 \x01(\tB*\x9a\x84\x9e\x03%bson:"location_id" json:"location_id"R\nlocationId\x12W\n\x0ecomponent_name\x18\x06 \x01(\tB0\x9a\x84\x9e\x03+bson:"component_name" json:"component_name"R\rcomponentName\x12W\n\x0ecomponent_type\x18\x07 \x01(\tB0\x9a\x84\x9e\x03+bson:"component_type" json:"component_type"R\rcomponentType\x12[\n\x0fcomponent_model\x18\x08 \x01(\tB2\x9a\x84\x9e\x03-bson:"component_model" json:"component_model"R\x0ecomponentModel\x12K\n\x0bmethod_name\x18\t \x01(\tB*\x9a\x84\x9e\x03%bson:"method_name" json:"method_name"R\nmethodName\x12C\n\tblob_path\x18\n \x01(\tB&\x9a\x84\x9e\x03!bson:"blob_path" json:"blob_path"R\x08blobPath\x12O\n\x0ccolumn_names\x18\x0b \x03(\tB,\x9a\x84\x9e\x03\'bson:"column_names" json:"column_names"R\x0bcolumnNames\x12\x9f\x01\n\x11method_parameters\x18\x0c \x03(\x0b2:.viam.app.datasync.v1.TabularCapture.MethodParametersEntryB6\x9a\x84\x9e\x031bson:"method_parameters" json:"method_parameters"R\x10methodParameters\x12;\n\x07file_id\x18\r \x01(\tB"\x9a\x84\x9e\x03\x1dbson:"file_id" json:"file_id"R\x06fileId\x120\n\x04tags\x18\x0e \x03(\tB\x1c\x9a\x84\x9e\x03\x17bson:"tags" json:"tags"R\x04tags\x12S\n\rmessage_count\x18\x0f \x01(\x05B.\x9a\x84\x9e\x03)bson:"message_count" json:"message_count"R\x0cmessageCount\x12Z\n\x0ffile_size_bytes\x18\x10 \x01(\x03B2\x9a\x84\x9e\x03-bson:"file_size_bytes" json:"file_size_bytes"R\rfileSizeBytes\x12G\n\nsession_id\x18\x11 \x01(\tB(\x9a\x84\x9e\x03#bson:"session_id" json:"session_id"R\tsessionId\x12C\n\tmime_type\x18\x12 \x01(\tB&\x9a\x84\x9e\x03!bson:"mime_type" json:"mime_type"R\x08mimeType\x1aY\n\x15MethodParametersEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12*\n\x05value\x18\x02 \x01(\x0b2\x14.google.protobuf.AnyR\x05value:\x028\x01"\xf8\x0b\n\rBinaryCapture\x12g\n\x08interval\x18\x01 \x01(\x0b2%.viam.app.datasync.v1.CaptureIntervalB$\x9a\x84\x9e\x03\x1fbson:"interval" json:"interval"R\x08interval\x127\n\x06org_id\x18\x02 \x01(\tB \x9a\x84\x9e\x03\x1bbson:"org_id" json:"org_id"R\x05orgId\x12?\n\x08robot_id\x18\x03 \x01(\tB$\x9a\x84\x9e\x03\x1fbson:"robot_id" json:"robot_id"R\x07robotId\x12;\n\x07part_id\x18\x04 \x01(\tB"\x9a\x84\x9e\x03\x1dbson:"part_id" json:"part_id"R\x06partId\x12K\n\x0blocation_id\x18\x05 \x01(\tB*\x9a\x84\x9e\x03%bson:"location_id" json:"location_id"R\nlocationId\x12W\n\x0ecomponent_name\x18\x06 \x01(\tB0\x9a\x84\x9e\x03+bson:"component_name" json:"component_name"R\rcomponentName\x12W\n\x0ecomponent_type\x18\x07 \x01(\tB0\x9a\x84\x9e\x03+bson:"component_type" json:"component_type"R\rcomponentType\x12[\n\x0fcomponent_model\x18\x08 \x01(\tB2\x9a\x84\x9e\x03-bson:"component_model" json:"component_model"R\x0ecomponentModel\x12K\n\x0bmethod_name\x18\t \x01(\tB*\x9a\x84\x9e\x03%bson:"method_name" json:"method_name"R\nmethodName\x12C\n\tblob_path\x18\n \x01(\tB&\x9a\x84\x9e\x03!bson:"blob_path" json:"blob_path"R\x08blobPath\x12\x9e\x01\n\x11method_parameters\x18\x0b \x03(\x0b29.viam.app.datasync.v1.BinaryCapture.MethodParametersEntryB6\x9a\x84\x9e\x031bson:"method_parameters" json:"method_parameters"R\x10methodParameters\x12;\n\x07file_id\x18\x0c \x01(\tB"\x9a\x84\x9e\x03\x1dbson:"file_id" json:"file_id"R\x06fileId\x120\n\x04tags\x18\r \x03(\tB\x1c\x9a\x84\x9e\x03\x17bson:"tags" json:"tags"R\x04tags\x12Z\n\x0ffile_size_bytes\x18\x0e \x01(\x03B2\x9a\x84\x9e\x03-bson:"file_size_bytes" json:"file_size_bytes"R\rfileSizeBytes\x12G\n\nsession_id\x18\x0f \x01(\tB(\x9a\x84\x9e\x03#bson:"session_id" json:"session_id"R\tsessionId\x12C\n\tmime_type\x18\x10 \x01(\tB&\x9a\x84\x9e\x03!bson:"mime_type" json:"mime_type"R\x08mimeType\x12C\n\tfile_name\x18\x11 \x01(\tB&\x9a\x84\x9e\x03!bson:"file_name" json:"file_name"R\x08fileName\x12?\n\x08file_ext\x18\x12 \x01(\tB$\x9a\x84\x9e\x03\x1fbson:"file_ext" json:"file_ext"R\x07fileExt\x1aY\n\x15MethodParametersEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12*\n\x05value\x18\x02 \x01(\x0b2\x14.google.protobuf.AnyR\x05value:\x028\x01*t\n\x08DataType\x12\x19\n\x15DATA_TYPE_UNSPECIFIED\x10\x00\x12\x1b\n\x17DATA_TYPE_BINARY_SENSOR\x10\x01\x12\x1c\n\x18DATA_TYPE_TABULAR_SENSOR\x10\x02\x12\x12\n\x0eDATA_TYPE_FILE\x10\x032j\n\x0fDataSyncService\x12W\n\x06Upload\x12#.viam.app.datasync.v1.UploadRequest\x1a$.viam.app.datasync.v1.UploadResponse(\x010\x01B!Z\x1fgo.viam.com/api/app/datasync/v1b\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'app.datasync.v1.data_sync_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z\x1fgo.viam.com/api/app/datasync/v1'
    _UPLOADMETADATA_METHODPARAMETERSENTRY._options = None
    _UPLOADMETADATA_METHODPARAMETERSENTRY._serialized_options = b'8\x01'
    _DATACAPTUREMETADATA_METHODPARAMETERSENTRY._options = None
    _DATACAPTUREMETADATA_METHODPARAMETERSENTRY._serialized_options = b'8\x01'
    _TABULARCAPTURE_METHODPARAMETERSENTRY._options = None
    _TABULARCAPTURE_METHODPARAMETERSENTRY._serialized_options = b'8\x01'
    _TABULARCAPTURE.fields_by_name['interval']._options = None
    _TABULARCAPTURE.fields_by_name['interval']._serialized_options = b'\x9a\x84\x9e\x03\x1fbson:"interval" json:"interval"'
    _TABULARCAPTURE.fields_by_name['org_id']._options = None
    _TABULARCAPTURE.fields_by_name['org_id']._serialized_options = b'\x9a\x84\x9e\x03\x1bbson:"org_id" json:"org_id"'
    _TABULARCAPTURE.fields_by_name['robot_id']._options = None
    _TABULARCAPTURE.fields_by_name['robot_id']._serialized_options = b'\x9a\x84\x9e\x03\x1fbson:"robot_id" json:"robot_id"'
    _TABULARCAPTURE.fields_by_name['part_id']._options = None
    _TABULARCAPTURE.fields_by_name['part_id']._serialized_options = b'\x9a\x84\x9e\x03\x1dbson:"part_id" json:"part_id"'
    _TABULARCAPTURE.fields_by_name['location_id']._options = None
    _TABULARCAPTURE.fields_by_name['location_id']._serialized_options = b'\x9a\x84\x9e\x03%bson:"location_id" json:"location_id"'
    _TABULARCAPTURE.fields_by_name['component_name']._options = None
    _TABULARCAPTURE.fields_by_name['component_name']._serialized_options = b'\x9a\x84\x9e\x03+bson:"component_name" json:"component_name"'
    _TABULARCAPTURE.fields_by_name['component_type']._options = None
    _TABULARCAPTURE.fields_by_name['component_type']._serialized_options = b'\x9a\x84\x9e\x03+bson:"component_type" json:"component_type"'
    _TABULARCAPTURE.fields_by_name['component_model']._options = None
    _TABULARCAPTURE.fields_by_name['component_model']._serialized_options = b'\x9a\x84\x9e\x03-bson:"component_model" json:"component_model"'
    _TABULARCAPTURE.fields_by_name['method_name']._options = None
    _TABULARCAPTURE.fields_by_name['method_name']._serialized_options = b'\x9a\x84\x9e\x03%bson:"method_name" json:"method_name"'
    _TABULARCAPTURE.fields_by_name['blob_path']._options = None
    _TABULARCAPTURE.fields_by_name['blob_path']._serialized_options = b'\x9a\x84\x9e\x03!bson:"blob_path" json:"blob_path"'
    _TABULARCAPTURE.fields_by_name['column_names']._options = None
    _TABULARCAPTURE.fields_by_name['column_names']._serialized_options = b'\x9a\x84\x9e\x03\'bson:"column_names" json:"column_names"'
    _TABULARCAPTURE.fields_by_name['method_parameters']._options = None
    _TABULARCAPTURE.fields_by_name['method_parameters']._serialized_options = b'\x9a\x84\x9e\x031bson:"method_parameters" json:"method_parameters"'
    _TABULARCAPTURE.fields_by_name['file_id']._options = None
    _TABULARCAPTURE.fields_by_name['file_id']._serialized_options = b'\x9a\x84\x9e\x03\x1dbson:"file_id" json:"file_id"'
    _TABULARCAPTURE.fields_by_name['tags']._options = None
    _TABULARCAPTURE.fields_by_name['tags']._serialized_options = b'\x9a\x84\x9e\x03\x17bson:"tags" json:"tags"'
    _TABULARCAPTURE.fields_by_name['message_count']._options = None
    _TABULARCAPTURE.fields_by_name['message_count']._serialized_options = b'\x9a\x84\x9e\x03)bson:"message_count" json:"message_count"'
    _TABULARCAPTURE.fields_by_name['file_size_bytes']._options = None
    _TABULARCAPTURE.fields_by_name['file_size_bytes']._serialized_options = b'\x9a\x84\x9e\x03-bson:"file_size_bytes" json:"file_size_bytes"'
    _TABULARCAPTURE.fields_by_name['session_id']._options = None
    _TABULARCAPTURE.fields_by_name['session_id']._serialized_options = b'\x9a\x84\x9e\x03#bson:"session_id" json:"session_id"'
    _TABULARCAPTURE.fields_by_name['mime_type']._options = None
    _TABULARCAPTURE.fields_by_name['mime_type']._serialized_options = b'\x9a\x84\x9e\x03!bson:"mime_type" json:"mime_type"'
    _BINARYCAPTURE_METHODPARAMETERSENTRY._options = None
    _BINARYCAPTURE_METHODPARAMETERSENTRY._serialized_options = b'8\x01'
    _BINARYCAPTURE.fields_by_name['interval']._options = None
    _BINARYCAPTURE.fields_by_name['interval']._serialized_options = b'\x9a\x84\x9e\x03\x1fbson:"interval" json:"interval"'
    _BINARYCAPTURE.fields_by_name['org_id']._options = None
    _BINARYCAPTURE.fields_by_name['org_id']._serialized_options = b'\x9a\x84\x9e\x03\x1bbson:"org_id" json:"org_id"'
    _BINARYCAPTURE.fields_by_name['robot_id']._options = None
    _BINARYCAPTURE.fields_by_name['robot_id']._serialized_options = b'\x9a\x84\x9e\x03\x1fbson:"robot_id" json:"robot_id"'
    _BINARYCAPTURE.fields_by_name['part_id']._options = None
    _BINARYCAPTURE.fields_by_name['part_id']._serialized_options = b'\x9a\x84\x9e\x03\x1dbson:"part_id" json:"part_id"'
    _BINARYCAPTURE.fields_by_name['location_id']._options = None
    _BINARYCAPTURE.fields_by_name['location_id']._serialized_options = b'\x9a\x84\x9e\x03%bson:"location_id" json:"location_id"'
    _BINARYCAPTURE.fields_by_name['component_name']._options = None
    _BINARYCAPTURE.fields_by_name['component_name']._serialized_options = b'\x9a\x84\x9e\x03+bson:"component_name" json:"component_name"'
    _BINARYCAPTURE.fields_by_name['component_type']._options = None
    _BINARYCAPTURE.fields_by_name['component_type']._serialized_options = b'\x9a\x84\x9e\x03+bson:"component_type" json:"component_type"'
    _BINARYCAPTURE.fields_by_name['component_model']._options = None
    _BINARYCAPTURE.fields_by_name['component_model']._serialized_options = b'\x9a\x84\x9e\x03-bson:"component_model" json:"component_model"'
    _BINARYCAPTURE.fields_by_name['method_name']._options = None
    _BINARYCAPTURE.fields_by_name['method_name']._serialized_options = b'\x9a\x84\x9e\x03%bson:"method_name" json:"method_name"'
    _BINARYCAPTURE.fields_by_name['blob_path']._options = None
    _BINARYCAPTURE.fields_by_name['blob_path']._serialized_options = b'\x9a\x84\x9e\x03!bson:"blob_path" json:"blob_path"'
    _BINARYCAPTURE.fields_by_name['method_parameters']._options = None
    _BINARYCAPTURE.fields_by_name['method_parameters']._serialized_options = b'\x9a\x84\x9e\x031bson:"method_parameters" json:"method_parameters"'
    _BINARYCAPTURE.fields_by_name['file_id']._options = None
    _BINARYCAPTURE.fields_by_name['file_id']._serialized_options = b'\x9a\x84\x9e\x03\x1dbson:"file_id" json:"file_id"'
    _BINARYCAPTURE.fields_by_name['tags']._options = None
    _BINARYCAPTURE.fields_by_name['tags']._serialized_options = b'\x9a\x84\x9e\x03\x17bson:"tags" json:"tags"'
    _BINARYCAPTURE.fields_by_name['file_size_bytes']._options = None
    _BINARYCAPTURE.fields_by_name['file_size_bytes']._serialized_options = b'\x9a\x84\x9e\x03-bson:"file_size_bytes" json:"file_size_bytes"'
    _BINARYCAPTURE.fields_by_name['session_id']._options = None
    _BINARYCAPTURE.fields_by_name['session_id']._serialized_options = b'\x9a\x84\x9e\x03#bson:"session_id" json:"session_id"'
    _BINARYCAPTURE.fields_by_name['mime_type']._options = None
    _BINARYCAPTURE.fields_by_name['mime_type']._serialized_options = b'\x9a\x84\x9e\x03!bson:"mime_type" json:"mime_type"'
    _BINARYCAPTURE.fields_by_name['file_name']._options = None
    _BINARYCAPTURE.fields_by_name['file_name']._serialized_options = b'\x9a\x84\x9e\x03!bson:"file_name" json:"file_name"'
    _BINARYCAPTURE.fields_by_name['file_ext']._options = None
    _BINARYCAPTURE.fields_by_name['file_ext']._serialized_options = b'\x9a\x84\x9e\x03\x1fbson:"file_ext" json:"file_ext"'
    _DATATYPE._serialized_start = 5125
    _DATATYPE._serialized_end = 5241
    _SENSORMETADATA._serialized_start = 172
    _SENSORMETADATA._serialized_end = 320
    _SENSORDATA._serialized_start = 323
    _SENSORDATA._serialized_end = 486
    _FILEDATA._serialized_start = 488
    _FILEDATA._serialized_end = 518
    _UPLOADMETADATA._serialized_start = 521
    _UPLOADMETADATA._serialized_end = 1081
    _UPLOADMETADATA_METHODPARAMETERSENTRY._serialized_start = 992
    _UPLOADMETADATA_METHODPARAMETERSENTRY._serialized_end = 1081
    _UPLOADREQUEST._serialized_start = 1084
    _UPLOADREQUEST._serialized_end = 1332
    _UPLOADRESPONSE._serialized_start = 1334
    _UPLOADRESPONSE._serialized_end = 1393
    _CAPTUREINTERVAL._serialized_start = 1395
    _CAPTUREINTERVAL._serialized_end = 1508
    _DATACAPTUREMETADATA._serialized_start = 1511
    _DATACAPTUREMETADATA._serialized_end = 2027
    _DATACAPTUREMETADATA_METHODPARAMETERSENTRY._serialized_start = 992
    _DATACAPTUREMETADATA_METHODPARAMETERSENTRY._serialized_end = 1081
    _TABULARCAPTURE._serialized_start = 2030
    _TABULARCAPTURE._serialized_end = 3592
    _TABULARCAPTURE_METHODPARAMETERSENTRY._serialized_start = 992
    _TABULARCAPTURE_METHODPARAMETERSENTRY._serialized_end = 1081
    _BINARYCAPTURE._serialized_start = 3595
    _BINARYCAPTURE._serialized_end = 5123
    _BINARYCAPTURE_METHODPARAMETERSENTRY._serialized_start = 992
    _BINARYCAPTURE_METHODPARAMETERSENTRY._serialized_end = 1081
    _DATASYNCSERVICE._serialized_start = 5243
    _DATASYNCSERVICE._serialized_end = 5349