"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18app/model/v1/model.proto\x12\x11viam.app.model.v1\x1a\x1fgoogle/protobuf/timestamp.proto"\x1e\n\x08FileData\x12\x12\n\x04data\x18\x01 \x01(\x0cR\x04data"u\n\x0eUploadMetadata\x12\x15\n\x06org_id\x18\x01 \x01(\tR\x05orgId\x12\x1d\n\nmodel_name\x18\x02 \x01(\tR\tmodelName\x12-\n\x12associated_dataset\x18\x03 \x01(\tR\x11associatedDataset"\xa5\x01\n\rUploadRequest\x12?\n\x08metadata\x18\x01 \x01(\x0b2!.viam.app.model.v1.UploadMetadataH\x00R\x08metadata\x12B\n\rfile_contents\x18\x02 \x01(\x0b2\x1b.viam.app.model.v1.FileDataH\x00R\x0cfileContentsB\x0f\n\rupload_packet"F\n\x0eDeleteMetadata\x12\x15\n\x06org_id\x18\x01 \x01(\tR\x05orgId\x12\x1d\n\nmodel_name\x18\x02 \x01(\tR\tmodelName"N\n\rDeleteRequest\x12=\n\x08metadata\x18\x01 \x01(\x0b2!.viam.app.model.v1.DeleteMetadataR\x08metadata"/\n\x0eDeployMetadata\x12\x1d\n\nmodel_name\x18\x01 \x01(\tR\tmodelName"N\n\rDeployRequest\x12=\n\x08metadata\x18\x01 \x01(\x0b2!.viam.app.model.v1.DeployMetadataR\x08metadata"]\n\x0eUploadResponse\x12\x18\n\x07message\x18\x01 \x01(\tR\x07message\x121\n\x06status\x18\x02 \x01(\x0e2\x19.viam.app.model.v1.StatusR\x06status"]\n\x0eDeleteResponse\x12\x18\n\x07message\x18\x01 \x01(\tR\x07message\x121\n\x06status\x18\x02 \x01(\x0e2\x19.viam.app.model.v1.StatusR\x06status"]\n\x0eDeployResponse\x12\x18\n\x07message\x18\x01 \x01(\tR\x07message\x121\n\x06status\x18\x02 \x01(\x0e2\x19.viam.app.model.v1.StatusR\x06status"\xc8\x01\n\x0bSyncedModel\x12\x15\n\x06org_id\x18\x01 \x01(\tR\x05orgId\x12\x1d\n\nmodel_name\x18\x02 \x01(\tR\tmodelName\x12-\n\x12associated_dataset\x18\x03 \x01(\tR\x11associatedDataset\x12\x1b\n\tblob_path\x18\x04 \x01(\tR\x08blobPath\x127\n\tsync_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.TimestampR\x08syncTime*+\n\x06Status\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x08\n\x04FAIL\x10\x01\x12\x06\n\x02OK\x10\x022\xfd\x01\n\x0cModelService\x12O\n\x06Upload\x12 .viam.app.model.v1.UploadRequest\x1a!.viam.app.model.v1.UploadResponse(\x01\x12M\n\x06Delete\x12 .viam.app.model.v1.DeleteRequest\x1a!.viam.app.model.v1.DeleteResponse\x12M\n\x06Deploy\x12 .viam.app.model.v1.DeployRequest\x1a!.viam.app.model.v1.DeployResponseB\x1eZ\x1cgo.viam.com/api/app/model/v1b\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'app.model.v1.model_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z\x1cgo.viam.com/api/app/model/v1'
    _STATUS._serialized_start = 1168
    _STATUS._serialized_end = 1211
    _FILEDATA._serialized_start = 80
    _FILEDATA._serialized_end = 110
    _UPLOADMETADATA._serialized_start = 112
    _UPLOADMETADATA._serialized_end = 229
    _UPLOADREQUEST._serialized_start = 232
    _UPLOADREQUEST._serialized_end = 397
    _DELETEMETADATA._serialized_start = 399
    _DELETEMETADATA._serialized_end = 469
    _DELETEREQUEST._serialized_start = 471
    _DELETEREQUEST._serialized_end = 549
    _DEPLOYMETADATA._serialized_start = 551
    _DEPLOYMETADATA._serialized_end = 598
    _DEPLOYREQUEST._serialized_start = 600
    _DEPLOYREQUEST._serialized_end = 678
    _UPLOADRESPONSE._serialized_start = 680
    _UPLOADRESPONSE._serialized_end = 773
    _DELETERESPONSE._serialized_start = 775
    _DELETERESPONSE._serialized_end = 868
    _DEPLOYRESPONSE._serialized_start = 870
    _DEPLOYRESPONSE._serialized_end = 963
    _SYNCEDMODEL._serialized_start = 966
    _SYNCEDMODEL._serialized_end = 1166
    _MODELSERVICE._serialized_start = 1214
    _MODELSERVICE._serialized_end = 1467