"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1fapp/datasync/v1/data_sync.proto\x12\x14viam.app.datasync.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x19google/protobuf/any.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xa7\x01\n\x18DataCaptureUploadRequest\x12@\n\x08metadata\x18\x01 \x01(\x0b2$.viam.app.datasync.v1.UploadMetadataR\x08metadata\x12I\n\x0fsensor_contents\x18\x02 \x03(\x0b2 .viam.app.datasync.v1.SensorDataR\x0esensorContents"4\n\x19DataCaptureUploadResponse\x12\x17\n\x07file_id\x18\x01 \x01(\tR\x06fileId"\xaf\x01\n\x11FileUploadRequest\x12B\n\x08metadata\x18\x01 \x01(\x0b2$.viam.app.datasync.v1.UploadMetadataH\x00R\x08metadata\x12E\n\rfile_contents\x18\x02 \x01(\x0b2\x1e.viam.app.datasync.v1.FileDataH\x00R\x0cfileContentsB\x0f\n\rupload_packet"-\n\x12FileUploadResponse\x12\x17\n\x07file_id\x18\x01 \x01(\tR\x06fileId"\x99\x01\n!StreamingDataCaptureUploadRequest\x12M\n\x08metadata\x18\x01 \x01(\x0b2/.viam.app.datasync.v1.DataCaptureUploadMetadataH\x00R\x08metadata\x12\x14\n\x04data\x18\x02 \x01(\x0cH\x00R\x04dataB\x0f\n\rupload_packet"=\n"StreamingDataCaptureUploadResponse\x12\x17\n\x07file_id\x18\x01 \x01(\tR\x06fileId"\x94\x01\n\x0eSensorMetadata\x12A\n\x0etime_requested\x18\x01 \x01(\x0b2\x1a.google.protobuf.TimestampR\rtimeRequested\x12?\n\rtime_received\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampR\x0ctimeReceived"\xa3\x01\n\nSensorData\x12@\n\x08metadata\x18\x01 \x01(\x0b2$.viam.app.datasync.v1.SensorMetadataR\x08metadata\x121\n\x06struct\x18\x02 \x01(\x0b2\x17.google.protobuf.StructH\x00R\x06struct\x12\x18\n\x06binary\x18\x03 \x01(\x0cH\x00R\x06binaryB\x06\n\x04data"\x1e\n\x08FileData\x12\x12\n\x04data\x18\x01 \x01(\x0cR\x04data"\x91\x04\n\x0eUploadMetadata\x12\x17\n\x07part_id\x18\x01 \x01(\tR\x06partId\x12%\n\x0ecomponent_type\x18\x02 \x01(\tR\rcomponentType\x12%\n\x0ecomponent_name\x18\x03 \x01(\tR\rcomponentName\x12\x1f\n\x0bmethod_name\x18\x05 \x01(\tR\nmethodName\x122\n\x04type\x18\x06 \x01(\x0e2\x1e.viam.app.datasync.v1.DataTypeR\x04type\x12\x1b\n\tfile_name\x18\x07 \x01(\tR\x08fileName\x12g\n\x11method_parameters\x18\x08 \x03(\x0b2:.viam.app.datasync.v1.UploadMetadata.MethodParametersEntryR\x10methodParameters\x12%\n\x0efile_extension\x18\t \x01(\tR\rfileExtension\x12\x12\n\x04tags\x18\n \x03(\tR\x04tags\x1aY\n\x15MethodParametersEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12*\n\x05value\x18\x02 \x01(\x0b2\x14.google.protobuf.AnyR\x05value:\x028\x01J\x04\x08\x04\x10\x05J\x04\x08\x0b\x10\x0cR\x0fcomponent_modelR\nsession_id"q\n\x0fCaptureInterval\x120\n\x05start\x18\x01 \x01(\x0b2\x1a.google.protobuf.TimestampR\x05start\x12,\n\x03end\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampR\x03end"\xe5\x03\n\x13DataCaptureMetadata\x12%\n\x0ecomponent_type\x18\x01 \x01(\tR\rcomponentType\x12%\n\x0ecomponent_name\x18\x02 \x01(\tR\rcomponentName\x12\x1f\n\x0bmethod_name\x18\x04 \x01(\tR\nmethodName\x122\n\x04type\x18\x05 \x01(\x0e2\x1e.viam.app.datasync.v1.DataTypeR\x04type\x12l\n\x11method_parameters\x18\x06 \x03(\x0b2?.viam.app.datasync.v1.DataCaptureMetadata.MethodParametersEntryR\x10methodParameters\x12%\n\x0efile_extension\x18\x07 \x01(\tR\rfileExtension\x12\x12\n\x04tags\x18\x08 \x03(\tR\x04tags\x1aY\n\x15MethodParametersEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12*\n\x05value\x18\x02 \x01(\x0b2\x14.google.protobuf.AnyR\x05value:\x028\x01J\x04\x08\x03\x10\x04J\x04\x08\t\x10\nR\x0fcomponent_modelR\nsession_id"\xb9\x01\n\x19DataCaptureUploadMetadata\x12M\n\x0fupload_metadata\x18\x01 \x01(\x0b2$.viam.app.datasync.v1.UploadMetadataR\x0euploadMetadata\x12M\n\x0fsensor_metadata\x18\x02 \x01(\x0b2$.viam.app.datasync.v1.SensorMetadataR\x0esensorMetadata*t\n\x08DataType\x12\x19\n\x15DATA_TYPE_UNSPECIFIED\x10\x00\x12\x1b\n\x17DATA_TYPE_BINARY_SENSOR\x10\x01\x12\x1c\n\x18DATA_TYPE_TABULAR_SENSOR\x10\x02\x12\x12\n\x0eDATA_TYPE_FILE\x10\x032\x80\x04\n\x0fDataSyncService\x12\x9e\x01\n\x11DataCaptureUpload\x12..viam.app.datasync.v1.DataCaptureUploadRequest\x1a/.viam.app.datasync.v1.DataCaptureUploadResponse"(\x82\xd3\xe4\x93\x02"" /datasync/v1/data_capture_upload\x12\x83\x01\n\nFileUpload\x12\'.viam.app.datasync.v1.FileUploadRequest\x1a(.viam.app.datasync.v1.FileUploadResponse" \x82\xd3\xe4\x93\x02\x1a"\x18/datasync/v1/file_upload(\x01\x12\xc5\x01\n\x1aStreamingDataCaptureUpload\x127.viam.app.datasync.v1.StreamingDataCaptureUploadRequest\x1a8.viam.app.datasync.v1.StreamingDataCaptureUploadResponse"2\x82\xd3\xe4\x93\x02,"*/datasync/v1/streaming_data_capture_upload(\x01B!Z\x1fgo.viam.com/api/app/datasync/v1b\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'app.datasync.v1.data_sync_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z\x1fgo.viam.com/api/app/datasync/v1'
    _UPLOADMETADATA_METHODPARAMETERSENTRY._options = None
    _UPLOADMETADATA_METHODPARAMETERSENTRY._serialized_options = b'8\x01'
    _DATACAPTUREMETADATA_METHODPARAMETERSENTRY._options = None
    _DATACAPTUREMETADATA_METHODPARAMETERSENTRY._serialized_options = b'8\x01'
    _DATASYNCSERVICE.methods_by_name['DataCaptureUpload']._options = None
    _DATASYNCSERVICE.methods_by_name['DataCaptureUpload']._serialized_options = b'\x82\xd3\xe4\x93\x02"" /datasync/v1/data_capture_upload'
    _DATASYNCSERVICE.methods_by_name['FileUpload']._options = None
    _DATASYNCSERVICE.methods_by_name['FileUpload']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1a"\x18/datasync/v1/file_upload'
    _DATASYNCSERVICE.methods_by_name['StreamingDataCaptureUpload']._options = None
    _DATASYNCSERVICE.methods_by_name['StreamingDataCaptureUpload']._serialized_options = b'\x82\xd3\xe4\x93\x02,"*/datasync/v1/streaming_data_capture_upload'
    _DATATYPE._serialized_start = 2517
    _DATATYPE._serialized_end = 2633
    _DATACAPTUREUPLOADREQUEST._serialized_start = 178
    _DATACAPTUREUPLOADREQUEST._serialized_end = 345
    _DATACAPTUREUPLOADRESPONSE._serialized_start = 347
    _DATACAPTUREUPLOADRESPONSE._serialized_end = 399
    _FILEUPLOADREQUEST._serialized_start = 402
    _FILEUPLOADREQUEST._serialized_end = 577
    _FILEUPLOADRESPONSE._serialized_start = 579
    _FILEUPLOADRESPONSE._serialized_end = 624
    _STREAMINGDATACAPTUREUPLOADREQUEST._serialized_start = 627
    _STREAMINGDATACAPTUREUPLOADREQUEST._serialized_end = 780
    _STREAMINGDATACAPTUREUPLOADRESPONSE._serialized_start = 782
    _STREAMINGDATACAPTUREUPLOADRESPONSE._serialized_end = 843
    _SENSORMETADATA._serialized_start = 846
    _SENSORMETADATA._serialized_end = 994
    _SENSORDATA._serialized_start = 997
    _SENSORDATA._serialized_end = 1160
    _FILEDATA._serialized_start = 1162
    _FILEDATA._serialized_end = 1192
    _UPLOADMETADATA._serialized_start = 1195
    _UPLOADMETADATA._serialized_end = 1724
    _UPLOADMETADATA_METHODPARAMETERSENTRY._serialized_start = 1594
    _UPLOADMETADATA_METHODPARAMETERSENTRY._serialized_end = 1683
    _CAPTUREINTERVAL._serialized_start = 1726
    _CAPTUREINTERVAL._serialized_end = 1839
    _DATACAPTUREMETADATA._serialized_start = 1842
    _DATACAPTUREMETADATA._serialized_end = 2327
    _DATACAPTUREMETADATA_METHODPARAMETERSENTRY._serialized_start = 1594
    _DATACAPTUREMETADATA_METHODPARAMETERSENTRY._serialized_end = 1683
    _DATACAPTUREUPLOADMETADATA._serialized_start = 2330
    _DATACAPTUREUPLOADMETADATA._serialized_end = 2515
    _DATASYNCSERVICE._serialized_start = 2636
    _DATASYNCSERVICE._serialized_end = 3148