"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from ....tagger.v1 import tagger_pb2 as tagger_dot_v1_dot_tagger__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18app/model/v1/model.proto\x12\x11viam.app.model.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x16tagger/v1/tagger.proto"\x1e\n\x08FileData\x12\x12\n\x04data\x18\x01 \x01(\x0cR\x04data"\x81\x01\n\x04File\x120\n\x04name\x18\x01 \x01(\tB\x1c\x9a\x84\x9e\x03\x17bson:"name" json:"name"R\x04name\x12G\n\nsize_bytes\x18\x02 \x01(\x03B(\x9a\x84\x9e\x03#bson:"size_bytes" json:"size_bytes"R\tsizeBytes"\xa4\x01\n\x0eUploadMetadata\x12\x15\n\x06org_id\x18\x01 \x01(\tR\x05orgId\x12\x1d\n\nmodel_name\x18\x02 \x01(\tR\tmodelName\x12-\n\x12associated_dataset\x18\x03 \x01(\tR\x11associatedDataset\x12-\n\x05files\x18\x04 \x03(\x0b2\x17.viam.app.model.v1.FileR\x05files"\xa5\x01\n\rUploadRequest\x12?\n\x08metadata\x18\x01 \x01(\x0b2!.viam.app.model.v1.UploadMetadataH\x00R\x08metadata\x12B\n\rfile_contents\x18\x02 \x01(\x0b2\x1b.viam.app.model.v1.FileDataH\x00R\x0cfileContentsB\x0f\n\rupload_packet"E\n\rDeleteRequest\x12\x15\n\x06org_id\x18\x01 \x01(\tR\x05orgId\x12\x1d\n\nmodel_name\x18\x02 \x01(\tR\tmodelName"E\n\rDeployRequest\x12\x15\n\x06org_id\x18\x01 \x01(\tR\x05orgId\x12\x1d\n\nmodel_name\x18\x02 \x01(\tR\tmodelName"\xa8\x01\n\x05Model\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x1d\n\nsize_bytes\x18\x02 \x01(\x03R\tsizeBytes\x12-\n\x05files\x18\x03 \x03(\x0b2\x17.viam.app.model.v1.FileR\x05files\x12=\n\x0ctime_created\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampR\x0btimeCreated"$\n\x0bInfoRequest\x12\x15\n\x06org_id\x18\x01 \x01(\tR\x05orgId">\n\x0cInfoResponse\x12.\n\x05model\x18\x01 \x03(\x0b2\x18.viam.app.model.v1.ModelR\x05model"]\n\x0eUploadResponse\x12\x18\n\x07message\x18\x01 \x01(\tR\x07message\x121\n\x06status\x18\x02 \x01(\x0e2\x19.viam.app.model.v1.StatusR\x06status"]\n\x0eDeleteResponse\x12\x18\n\x07message\x18\x01 \x01(\tR\x07message\x121\n\x06status\x18\x02 \x01(\x0e2\x19.viam.app.model.v1.StatusR\x06status"]\n\x0eDeployResponse\x12\x18\n\x07message\x18\x01 \x01(\tR\x07message\x121\n\x06status\x18\x02 \x01(\x0e2\x19.viam.app.model.v1.StatusR\x06status"\xb6\x04\n\x0bSyncedModel\x127\n\x06org_id\x18\x01 \x01(\tB \x9a\x84\x9e\x03\x1bbson:"org_id" json:"org_id"R\x05orgId\x12G\n\nmodel_name\x18\x02 \x01(\tB(\x9a\x84\x9e\x03#bson:"model_name" json:"model_name"R\tmodelName\x12g\n\x12associated_dataset\x18\x03 \x01(\tB8\x9a\x84\x9e\x033bson:"associated_dataset" json:"associated_dataset"R\x11associatedDataset\x12M\n\x05files\x18\x04 \x03(\x0b2\x17.viam.app.model.v1.FileB\x1e\x9a\x84\x9e\x03\x19bson:"files" json:"files"R\x05files\x12G\n\nsize_bytes\x18\x05 \x01(\x03B(\x9a\x84\x9e\x03#bson:"size_bytes" json:"size_bytes"R\tsizeBytes\x12C\n\tblob_path\x18\x06 \x01(\tB&\x9a\x84\x9e\x03!bson:"blob_path" json:"blob_path"R\x08blobPath\x12_\n\tsync_time\x18\x07 \x01(\x0b2\x1a.google.protobuf.TimestampB&\x9a\x84\x9e\x03!bson:"sync_time" json:"sync_time"R\x08syncTime*+\n\x06Status\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x08\n\x04FAIL\x10\x01\x12\x06\n\x02OK\x10\x022\xac\x03\n\x0cModelService\x12i\n\x06Upload\x12 .viam.app.model.v1.UploadRequest\x1a!.viam.app.model.v1.UploadResponse"\x18\x82\xd3\xe4\x93\x02\x12"\x10/model/v1/upload(\x01\x12g\n\x06Delete\x12 .viam.app.model.v1.DeleteRequest\x1a!.viam.app.model.v1.DeleteResponse"\x18\x82\xd3\xe4\x93\x02\x12*\x10/model/v1/delete\x12g\n\x06Deploy\x12 .viam.app.model.v1.DeployRequest\x1a!.viam.app.model.v1.DeployResponse"\x18\x82\xd3\xe4\x93\x02\x12"\x10/model/v1/deploy\x12_\n\x04Info\x12\x1e.viam.app.model.v1.InfoRequest\x1a\x1f.viam.app.model.v1.InfoResponse"\x16\x82\xd3\xe4\x93\x02\x10\x12\x0e/model/v1/infoB\x1eZ\x1cgo.viam.com/api/app/model/v1b\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'app.model.v1.model_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z\x1cgo.viam.com/api/app/model/v1'
    _FILE.fields_by_name['name']._options = None
    _FILE.fields_by_name['name']._serialized_options = b'\x9a\x84\x9e\x03\x17bson:"name" json:"name"'
    _FILE.fields_by_name['size_bytes']._options = None
    _FILE.fields_by_name['size_bytes']._serialized_options = b'\x9a\x84\x9e\x03#bson:"size_bytes" json:"size_bytes"'
    _SYNCEDMODEL.fields_by_name['org_id']._options = None
    _SYNCEDMODEL.fields_by_name['org_id']._serialized_options = b'\x9a\x84\x9e\x03\x1bbson:"org_id" json:"org_id"'
    _SYNCEDMODEL.fields_by_name['model_name']._options = None
    _SYNCEDMODEL.fields_by_name['model_name']._serialized_options = b'\x9a\x84\x9e\x03#bson:"model_name" json:"model_name"'
    _SYNCEDMODEL.fields_by_name['associated_dataset']._options = None
    _SYNCEDMODEL.fields_by_name['associated_dataset']._serialized_options = b'\x9a\x84\x9e\x033bson:"associated_dataset" json:"associated_dataset"'
    _SYNCEDMODEL.fields_by_name['files']._options = None
    _SYNCEDMODEL.fields_by_name['files']._serialized_options = b'\x9a\x84\x9e\x03\x19bson:"files" json:"files"'
    _SYNCEDMODEL.fields_by_name['size_bytes']._options = None
    _SYNCEDMODEL.fields_by_name['size_bytes']._serialized_options = b'\x9a\x84\x9e\x03#bson:"size_bytes" json:"size_bytes"'
    _SYNCEDMODEL.fields_by_name['blob_path']._options = None
    _SYNCEDMODEL.fields_by_name['blob_path']._serialized_options = b'\x9a\x84\x9e\x03!bson:"blob_path" json:"blob_path"'
    _SYNCEDMODEL.fields_by_name['sync_time']._options = None
    _SYNCEDMODEL.fields_by_name['sync_time']._serialized_options = b'\x9a\x84\x9e\x03!bson:"sync_time" json:"sync_time"'
    _MODELSERVICE.methods_by_name['Upload']._options = None
    _MODELSERVICE.methods_by_name['Upload']._serialized_options = b'\x82\xd3\xe4\x93\x02\x12"\x10/model/v1/upload'
    _MODELSERVICE.methods_by_name['Delete']._options = None
    _MODELSERVICE.methods_by_name['Delete']._serialized_options = b'\x82\xd3\xe4\x93\x02\x12*\x10/model/v1/delete'
    _MODELSERVICE.methods_by_name['Deploy']._options = None
    _MODELSERVICE.methods_by_name['Deploy']._serialized_options = b'\x82\xd3\xe4\x93\x02\x12"\x10/model/v1/deploy'
    _MODELSERVICE.methods_by_name['Info']._options = None
    _MODELSERVICE.methods_by_name['Info']._serialized_options = b'\x82\xd3\xe4\x93\x02\x10\x12\x0e/model/v1/info'
    _STATUS._serialized_start = 1902
    _STATUS._serialized_end = 1945
    _FILEDATA._serialized_start = 134
    _FILEDATA._serialized_end = 164
    _FILE._serialized_start = 167
    _FILE._serialized_end = 296
    _UPLOADMETADATA._serialized_start = 299
    _UPLOADMETADATA._serialized_end = 463
    _UPLOADREQUEST._serialized_start = 466
    _UPLOADREQUEST._serialized_end = 631
    _DELETEREQUEST._serialized_start = 633
    _DELETEREQUEST._serialized_end = 702
    _DEPLOYREQUEST._serialized_start = 704
    _DEPLOYREQUEST._serialized_end = 773
    _MODEL._serialized_start = 776
    _MODEL._serialized_end = 944
    _INFOREQUEST._serialized_start = 946
    _INFOREQUEST._serialized_end = 982
    _INFORESPONSE._serialized_start = 984
    _INFORESPONSE._serialized_end = 1046
    _UPLOADRESPONSE._serialized_start = 1048
    _UPLOADRESPONSE._serialized_end = 1141
    _DELETERESPONSE._serialized_start = 1143
    _DELETERESPONSE._serialized_end = 1236
    _DEPLOYRESPONSE._serialized_start = 1238
    _DEPLOYRESPONSE._serialized_end = 1331
    _SYNCEDMODEL._serialized_start = 1334
    _SYNCEDMODEL._serialized_end = 1900
    _MODELSERVICE._serialized_start = 1948
    _MODELSERVICE._serialized_end = 2376