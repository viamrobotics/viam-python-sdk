"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 2, '', 'app/datasync/v1/data_sync.proto')
_sym_db = _symbol_database.Default()
from ....app.data.v1 import data_pb2 as app_dot_data_dot_v1_dot_data__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1fapp/datasync/v1/data_sync.proto\x12\x14viam.app.datasync.v1\x1a\x16app/data/v1/data.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x19google/protobuf/any.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xa7\x01\n\x18DataCaptureUploadRequest\x12@\n\x08metadata\x18\x01 \x01(\x0b2$.viam.app.datasync.v1.UploadMetadataR\x08metadata\x12I\n\x0fsensor_contents\x18\x02 \x03(\x0b2 .viam.app.datasync.v1.SensorDataR\x0esensorContents"Z\n\x19DataCaptureUploadResponse\x12\x17\n\x07file_id\x18\x01 \x01(\tR\x06fileId\x12$\n\x0ebinary_data_id\x18\x02 \x01(\tR\x0cbinaryDataId"\xaf\x01\n\x11FileUploadRequest\x12B\n\x08metadata\x18\x01 \x01(\x0b2$.viam.app.datasync.v1.UploadMetadataH\x00R\x08metadata\x12E\n\rfile_contents\x18\x02 \x01(\x0b2\x1e.viam.app.datasync.v1.FileDataH\x00R\x0cfileContentsB\x0f\n\rupload_packet"W\n\x12FileUploadResponse\x12\x1b\n\x07file_id\x18\x01 \x01(\tB\x02\x18\x01R\x06fileId\x12$\n\x0ebinary_data_id\x18\x02 \x01(\tR\x0cbinaryDataId"\x99\x01\n!StreamingDataCaptureUploadRequest\x12M\n\x08metadata\x18\x01 \x01(\x0b2/.viam.app.datasync.v1.DataCaptureUploadMetadataH\x00R\x08metadata\x12\x14\n\x04data\x18\x02 \x01(\x0cH\x00R\x04dataB\x0f\n\rupload_packet"g\n"StreamingDataCaptureUploadResponse\x12\x1b\n\x07file_id\x18\x01 \x01(\tB\x02\x18\x01R\x06fileId\x12$\n\x0ebinary_data_id\x18\x02 \x01(\tR\x0cbinaryDataId"\x92\x02\n\x0eSensorMetadata\x12A\n\x0etime_requested\x18\x01 \x01(\x0b2\x1a.google.protobuf.TimestampR\rtimeRequested\x12?\n\rtime_received\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampR\x0ctimeReceived\x12;\n\tmime_type\x18\x03 \x01(\x0e2\x1e.viam.app.datasync.v1.MimeTypeR\x08mimeType\x12?\n\x0bannotations\x18\x04 \x01(\x0b2\x1d.viam.app.data.v1.AnnotationsR\x0bannotations"\xa3\x01\n\nSensorData\x12@\n\x08metadata\x18\x01 \x01(\x0b2$.viam.app.datasync.v1.SensorMetadataR\x08metadata\x121\n\x06struct\x18\x02 \x01(\x0b2\x17.google.protobuf.StructH\x00R\x06struct\x12\x18\n\x06binary\x18\x03 \x01(\x0cH\x00R\x06binaryB\x06\n\x04data"\x1e\n\x08FileData\x12\x12\n\x04data\x18\x01 \x01(\x0cR\x04data"\x91\x04\n\x0eUploadMetadata\x12\x17\n\x07part_id\x18\x01 \x01(\tR\x06partId\x12%\n\x0ecomponent_type\x18\x02 \x01(\tR\rcomponentType\x12%\n\x0ecomponent_name\x18\x03 \x01(\tR\rcomponentName\x12\x1f\n\x0bmethod_name\x18\x05 \x01(\tR\nmethodName\x122\n\x04type\x18\x06 \x01(\x0e2\x1e.viam.app.datasync.v1.DataTypeR\x04type\x12\x1b\n\tfile_name\x18\x07 \x01(\tR\x08fileName\x12g\n\x11method_parameters\x18\x08 \x03(\x0b2:.viam.app.datasync.v1.UploadMetadata.MethodParametersEntryR\x10methodParameters\x12%\n\x0efile_extension\x18\t \x01(\tR\rfileExtension\x12\x12\n\x04tags\x18\n \x03(\tR\x04tags\x1aY\n\x15MethodParametersEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12*\n\x05value\x18\x02 \x01(\x0b2\x14.google.protobuf.AnyR\x05value:\x028\x01J\x04\x08\x04\x10\x05J\x04\x08\x0b\x10\x0cR\x0fcomponent_modelR\nsession_id"q\n\x0fCaptureInterval\x120\n\x05start\x18\x01 \x01(\x0b2\x1a.google.protobuf.TimestampR\x05start\x12,\n\x03end\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampR\x03end"\xe5\x03\n\x13DataCaptureMetadata\x12%\n\x0ecomponent_type\x18\x01 \x01(\tR\rcomponentType\x12%\n\x0ecomponent_name\x18\x02 \x01(\tR\rcomponentName\x12\x1f\n\x0bmethod_name\x18\x04 \x01(\tR\nmethodName\x122\n\x04type\x18\x05 \x01(\x0e2\x1e.viam.app.datasync.v1.DataTypeR\x04type\x12l\n\x11method_parameters\x18\x06 \x03(\x0b2?.viam.app.datasync.v1.DataCaptureMetadata.MethodParametersEntryR\x10methodParameters\x12%\n\x0efile_extension\x18\x07 \x01(\tR\rfileExtension\x12\x12\n\x04tags\x18\x08 \x03(\tR\x04tags\x1aY\n\x15MethodParametersEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12*\n\x05value\x18\x02 \x01(\x0b2\x14.google.protobuf.AnyR\x05value:\x028\x01J\x04\x08\x03\x10\x04J\x04\x08\t\x10\nR\x0fcomponent_modelR\nsession_id"\xb9\x01\n\x19DataCaptureUploadMetadata\x12M\n\x0fupload_metadata\x18\x01 \x01(\x0b2$.viam.app.datasync.v1.UploadMetadataR\x0euploadMetadata\x12M\n\x0fsensor_metadata\x18\x02 \x01(\x0b2$.viam.app.datasync.v1.SensorMetadataR\x0esensorMetadata*w\n\x08MimeType\x12\x19\n\x15MIME_TYPE_UNSPECIFIED\x10\x00\x12\x18\n\x14MIME_TYPE_IMAGE_JPEG\x10\x01\x12\x17\n\x13MIME_TYPE_IMAGE_PNG\x10\x02\x12\x1d\n\x19MIME_TYPE_APPLICATION_PCD\x10\x03*t\n\x08DataType\x12\x19\n\x15DATA_TYPE_UNSPECIFIED\x10\x00\x12\x1b\n\x17DATA_TYPE_BINARY_SENSOR\x10\x01\x12\x1c\n\x18DATA_TYPE_TABULAR_SENSOR\x10\x02\x12\x12\n\x0eDATA_TYPE_FILE\x10\x032\x80\x04\n\x0fDataSyncService\x12\x9e\x01\n\x11DataCaptureUpload\x12..viam.app.datasync.v1.DataCaptureUploadRequest\x1a/.viam.app.datasync.v1.DataCaptureUploadResponse"(\x82\xd3\xe4\x93\x02"" /datasync/v1/data_capture_upload\x12\x83\x01\n\nFileUpload\x12\'.viam.app.datasync.v1.FileUploadRequest\x1a(.viam.app.datasync.v1.FileUploadResponse" \x82\xd3\xe4\x93\x02\x1a"\x18/datasync/v1/file_upload(\x01\x12\xc5\x01\n\x1aStreamingDataCaptureUpload\x127.viam.app.datasync.v1.StreamingDataCaptureUploadRequest\x1a8.viam.app.datasync.v1.StreamingDataCaptureUploadResponse"2\x82\xd3\xe4\x93\x02,"*/datasync/v1/streaming_data_capture_upload(\x01B!Z\x1fgo.viam.com/api/app/datasync/v1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'app.datasync.v1.data_sync_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z\x1fgo.viam.com/api/app/datasync/v1'
    _globals['_FILEUPLOADRESPONSE'].fields_by_name['file_id']._loaded_options = None
    _globals['_FILEUPLOADRESPONSE'].fields_by_name['file_id']._serialized_options = b'\x18\x01'
    _globals['_STREAMINGDATACAPTUREUPLOADRESPONSE'].fields_by_name['file_id']._loaded_options = None
    _globals['_STREAMINGDATACAPTUREUPLOADRESPONSE'].fields_by_name['file_id']._serialized_options = b'\x18\x01'
    _globals['_UPLOADMETADATA_METHODPARAMETERSENTRY']._loaded_options = None
    _globals['_UPLOADMETADATA_METHODPARAMETERSENTRY']._serialized_options = b'8\x01'
    _globals['_DATACAPTUREMETADATA_METHODPARAMETERSENTRY']._loaded_options = None
    _globals['_DATACAPTUREMETADATA_METHODPARAMETERSENTRY']._serialized_options = b'8\x01'
    _globals['_DATASYNCSERVICE'].methods_by_name['DataCaptureUpload']._loaded_options = None
    _globals['_DATASYNCSERVICE'].methods_by_name['DataCaptureUpload']._serialized_options = b'\x82\xd3\xe4\x93\x02"" /datasync/v1/data_capture_upload'
    _globals['_DATASYNCSERVICE'].methods_by_name['FileUpload']._loaded_options = None
    _globals['_DATASYNCSERVICE'].methods_by_name['FileUpload']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1a"\x18/datasync/v1/file_upload'
    _globals['_DATASYNCSERVICE'].methods_by_name['StreamingDataCaptureUpload']._loaded_options = None
    _globals['_DATASYNCSERVICE'].methods_by_name['StreamingDataCaptureUpload']._serialized_options = b'\x82\xd3\xe4\x93\x02,"*/datasync/v1/streaming_data_capture_upload'
    _globals['_MIMETYPE']._serialized_start = 2789
    _globals['_MIMETYPE']._serialized_end = 2908
    _globals['_DATATYPE']._serialized_start = 2910
    _globals['_DATATYPE']._serialized_end = 3026
    _globals['_DATACAPTUREUPLOADREQUEST']._serialized_start = 202
    _globals['_DATACAPTUREUPLOADREQUEST']._serialized_end = 369
    _globals['_DATACAPTUREUPLOADRESPONSE']._serialized_start = 371
    _globals['_DATACAPTUREUPLOADRESPONSE']._serialized_end = 461
    _globals['_FILEUPLOADREQUEST']._serialized_start = 464
    _globals['_FILEUPLOADREQUEST']._serialized_end = 639
    _globals['_FILEUPLOADRESPONSE']._serialized_start = 641
    _globals['_FILEUPLOADRESPONSE']._serialized_end = 728
    _globals['_STREAMINGDATACAPTUREUPLOADREQUEST']._serialized_start = 731
    _globals['_STREAMINGDATACAPTUREUPLOADREQUEST']._serialized_end = 884
    _globals['_STREAMINGDATACAPTUREUPLOADRESPONSE']._serialized_start = 886
    _globals['_STREAMINGDATACAPTUREUPLOADRESPONSE']._serialized_end = 989
    _globals['_SENSORMETADATA']._serialized_start = 992
    _globals['_SENSORMETADATA']._serialized_end = 1266
    _globals['_SENSORDATA']._serialized_start = 1269
    _globals['_SENSORDATA']._serialized_end = 1432
    _globals['_FILEDATA']._serialized_start = 1434
    _globals['_FILEDATA']._serialized_end = 1464
    _globals['_UPLOADMETADATA']._serialized_start = 1467
    _globals['_UPLOADMETADATA']._serialized_end = 1996
    _globals['_UPLOADMETADATA_METHODPARAMETERSENTRY']._serialized_start = 1866
    _globals['_UPLOADMETADATA_METHODPARAMETERSENTRY']._serialized_end = 1955
    _globals['_CAPTUREINTERVAL']._serialized_start = 1998
    _globals['_CAPTUREINTERVAL']._serialized_end = 2111
    _globals['_DATACAPTUREMETADATA']._serialized_start = 2114
    _globals['_DATACAPTUREMETADATA']._serialized_end = 2599
    _globals['_DATACAPTUREMETADATA_METHODPARAMETERSENTRY']._serialized_start = 1866
    _globals['_DATACAPTUREMETADATA_METHODPARAMETERSENTRY']._serialized_end = 1955
    _globals['_DATACAPTUREUPLOADMETADATA']._serialized_start = 2602
    _globals['_DATACAPTUREUPLOADMETADATA']._serialized_end = 2787
    _globals['_DATASYNCSERVICE']._serialized_start = 3029
    _globals['_DATASYNCSERVICE']._serialized_end = 3541