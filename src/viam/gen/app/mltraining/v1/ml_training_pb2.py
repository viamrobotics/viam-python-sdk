"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....app.data.v1 import data_pb2 as app_dot_data_dot_v1_dot_data__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
from ....tagger.v1 import tagger_pb2 as tagger_dot_v1_dot_tagger__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#app/mltraining/v1/ml_training.proto\x12\x16viam.app.mltraining.v1\x1a\x16app/data/v1/data.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x17google/rpc/status.proto\x1a\x16tagger/v1/tagger.proto"\xd0\x04\n\x18SubmitTrainingJobRequest\x12R\n\x06filter\x18\x01 \x01(\x0b2\x18.viam.app.data.v1.FilterB \x9a\x84\x9e\x03\x1bbson:"filter" json:"filter"R\x06filter\x12G\n\ndataset_id\x18\x07 \x01(\tB(\x9a\x84\x9e\x03#bson:"dataset_id" json:"dataset_id"R\tdatasetId\x12[\n\x0forganization_id\x18\x02 \x01(\tB2\x9a\x84\x9e\x03-bson:"organization_id" json:"organization_id"R\x0eorganizationId\x12G\n\nmodel_name\x18\x03 \x01(\tB(\x9a\x84\x9e\x03#bson:"model_name" json:"model_name"R\tmodelName\x12S\n\rmodel_version\x18\x04 \x01(\tB.\x9a\x84\x9e\x03)bson:"model_version" json:"model_version"R\x0cmodelVersion\x12j\n\nmodel_type\x18\x05 \x01(\x0e2!.viam.app.mltraining.v1.ModelTypeB(\x9a\x84\x9e\x03#bson:"model_type" json:"model_type"R\tmodelType\x120\n\x04tags\x18\x06 \x03(\tB\x1c\x9a\x84\x9e\x03\x17bson:"tags" json:"tags"R\x04tags"+\n\x19SubmitTrainingJobResponse\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id"\'\n\x15GetTrainingJobRequest\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id"a\n\x16GetTrainingJobResponse\x12G\n\x08metadata\x18\x01 \x01(\x0b2+.viam.app.mltraining.v1.TrainingJobMetadataR\x08metadata"\x82\x01\n\x17ListTrainingJobsRequest\x12\'\n\x0forganization_id\x18\x01 \x01(\tR\x0eorganizationId\x12>\n\x06status\x18\x02 \x01(\x0e2&.viam.app.mltraining.v1.TrainingStatusR\x06status"[\n\x18ListTrainingJobsResponse\x12?\n\x04jobs\x18\x01 \x03(\x0b2+.viam.app.mltraining.v1.TrainingJobMetadataR\x04jobs"\xc5\x05\n\x13TrainingJobMetadata\x12n\n\x07request\x18\x01 \x01(\x0b20.viam.app.mltraining.v1.SubmitTrainingJobRequestB"\x9a\x84\x9e\x03\x1dbson:"request" json:"request"R\x07request\x12`\n\x06status\x18\x02 \x01(\x0e2&.viam.app.mltraining.v1.TrainingStatusB \x9a\x84\x9e\x03\x1bbson:"status" json:"status"R\x06status\x12c\n\ncreated_on\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB(\x9a\x84\x9e\x03#bson:"created_on" json:"created_on"R\tcreatedOn\x12o\n\rlast_modified\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampB.\x9a\x84\x9e\x03)bson:"last_modified" json:"last_modified"R\x0clastModified\x12Z\n\x0fsynced_model_id\x18\x05 \x01(\tB2\x9a\x84\x9e\x03-bson:"synced_model_id" json:"synced_model_id"R\rsyncedModelId\x123\n\x02id\x18\x07 \x01(\tB#\x9a\x84\x9e\x03\x1ebson:"_id" json:"id,omitempty"R\x02id\x12c\n\x0cerror_status\x18\x08 \x01(\x0b2\x12.google.rpc.StatusB,\x9a\x84\x9e\x03\'bson:"error_status" json:"error_status"R\x0berrorStatusJ\x04\x08\x06\x10\x07R\nuser_email"*\n\x18CancelTrainingJobRequest\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id"\x1b\n\x19CancelTrainingJobResponse*\x9f\x01\n\tModelType\x12\x1a\n\x16MODEL_TYPE_UNSPECIFIED\x10\x00\x12*\n&MODEL_TYPE_SINGLE_LABEL_CLASSIFICATION\x10\x01\x12)\n%MODEL_TYPE_MULTI_LABEL_CLASSIFICATION\x10\x02\x12\x1f\n\x1bMODEL_TYPE_OBJECT_DETECTION\x10\x03*\xe7\x01\n\x0eTrainingStatus\x12\x1f\n\x1bTRAINING_STATUS_UNSPECIFIED\x10\x00\x12\x1b\n\x17TRAINING_STATUS_PENDING\x10\x01\x12\x1f\n\x1bTRAINING_STATUS_IN_PROGRESS\x10\x02\x12\x1d\n\x19TRAINING_STATUS_COMPLETED\x10\x03\x12\x1a\n\x16TRAINING_STATUS_FAILED\x10\x04\x12\x1c\n\x18TRAINING_STATUS_CANCELED\x10\x05\x12\x1d\n\x19TRAINING_STATUS_CANCELING\x10\x062\xef\x03\n\x11MLTrainingService\x12x\n\x11SubmitTrainingJob\x120.viam.app.mltraining.v1.SubmitTrainingJobRequest\x1a1.viam.app.mltraining.v1.SubmitTrainingJobResponse\x12o\n\x0eGetTrainingJob\x12-.viam.app.mltraining.v1.GetTrainingJobRequest\x1a..viam.app.mltraining.v1.GetTrainingJobResponse\x12u\n\x10ListTrainingJobs\x12/.viam.app.mltraining.v1.ListTrainingJobsRequest\x1a0.viam.app.mltraining.v1.ListTrainingJobsResponse\x12x\n\x11CancelTrainingJob\x120.viam.app.mltraining.v1.CancelTrainingJobRequest\x1a1.viam.app.mltraining.v1.CancelTrainingJobResponseB#Z!go.viam.com/api/app/mltraining/v1b\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'app.mltraining.v1.ml_training_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z!go.viam.com/api/app/mltraining/v1'
    _SUBMITTRAININGJOBREQUEST.fields_by_name['filter']._options = None
    _SUBMITTRAININGJOBREQUEST.fields_by_name['filter']._serialized_options = b'\x9a\x84\x9e\x03\x1bbson:"filter" json:"filter"'
    _SUBMITTRAININGJOBREQUEST.fields_by_name['dataset_id']._options = None
    _SUBMITTRAININGJOBREQUEST.fields_by_name['dataset_id']._serialized_options = b'\x9a\x84\x9e\x03#bson:"dataset_id" json:"dataset_id"'
    _SUBMITTRAININGJOBREQUEST.fields_by_name['organization_id']._options = None
    _SUBMITTRAININGJOBREQUEST.fields_by_name['organization_id']._serialized_options = b'\x9a\x84\x9e\x03-bson:"organization_id" json:"organization_id"'
    _SUBMITTRAININGJOBREQUEST.fields_by_name['model_name']._options = None
    _SUBMITTRAININGJOBREQUEST.fields_by_name['model_name']._serialized_options = b'\x9a\x84\x9e\x03#bson:"model_name" json:"model_name"'
    _SUBMITTRAININGJOBREQUEST.fields_by_name['model_version']._options = None
    _SUBMITTRAININGJOBREQUEST.fields_by_name['model_version']._serialized_options = b'\x9a\x84\x9e\x03)bson:"model_version" json:"model_version"'
    _SUBMITTRAININGJOBREQUEST.fields_by_name['model_type']._options = None
    _SUBMITTRAININGJOBREQUEST.fields_by_name['model_type']._serialized_options = b'\x9a\x84\x9e\x03#bson:"model_type" json:"model_type"'
    _SUBMITTRAININGJOBREQUEST.fields_by_name['tags']._options = None
    _SUBMITTRAININGJOBREQUEST.fields_by_name['tags']._serialized_options = b'\x9a\x84\x9e\x03\x17bson:"tags" json:"tags"'
    _TRAININGJOBMETADATA.fields_by_name['request']._options = None
    _TRAININGJOBMETADATA.fields_by_name['request']._serialized_options = b'\x9a\x84\x9e\x03\x1dbson:"request" json:"request"'
    _TRAININGJOBMETADATA.fields_by_name['status']._options = None
    _TRAININGJOBMETADATA.fields_by_name['status']._serialized_options = b'\x9a\x84\x9e\x03\x1bbson:"status" json:"status"'
    _TRAININGJOBMETADATA.fields_by_name['created_on']._options = None
    _TRAININGJOBMETADATA.fields_by_name['created_on']._serialized_options = b'\x9a\x84\x9e\x03#bson:"created_on" json:"created_on"'
    _TRAININGJOBMETADATA.fields_by_name['last_modified']._options = None
    _TRAININGJOBMETADATA.fields_by_name['last_modified']._serialized_options = b'\x9a\x84\x9e\x03)bson:"last_modified" json:"last_modified"'
    _TRAININGJOBMETADATA.fields_by_name['synced_model_id']._options = None
    _TRAININGJOBMETADATA.fields_by_name['synced_model_id']._serialized_options = b'\x9a\x84\x9e\x03-bson:"synced_model_id" json:"synced_model_id"'
    _TRAININGJOBMETADATA.fields_by_name['id']._options = None
    _TRAININGJOBMETADATA.fields_by_name['id']._serialized_options = b'\x9a\x84\x9e\x03\x1ebson:"_id" json:"id,omitempty"'
    _TRAININGJOBMETADATA.fields_by_name['error_status']._options = None
    _TRAININGJOBMETADATA.fields_by_name['error_status']._serialized_options = b'\x9a\x84\x9e\x03\'bson:"error_status" json:"error_status"'
    _MODELTYPE._serialized_start = 1961
    _MODELTYPE._serialized_end = 2120
    _TRAININGSTATUS._serialized_start = 2123
    _TRAININGSTATUS._serialized_end = 2354
    _SUBMITTRAININGJOBREQUEST._serialized_start = 170
    _SUBMITTRAININGJOBREQUEST._serialized_end = 762
    _SUBMITTRAININGJOBRESPONSE._serialized_start = 764
    _SUBMITTRAININGJOBRESPONSE._serialized_end = 807
    _GETTRAININGJOBREQUEST._serialized_start = 809
    _GETTRAININGJOBREQUEST._serialized_end = 848
    _GETTRAININGJOBRESPONSE._serialized_start = 850
    _GETTRAININGJOBRESPONSE._serialized_end = 947
    _LISTTRAININGJOBSREQUEST._serialized_start = 950
    _LISTTRAININGJOBSREQUEST._serialized_end = 1080
    _LISTTRAININGJOBSRESPONSE._serialized_start = 1082
    _LISTTRAININGJOBSRESPONSE._serialized_end = 1173
    _TRAININGJOBMETADATA._serialized_start = 1176
    _TRAININGJOBMETADATA._serialized_end = 1885
    _CANCELTRAININGJOBREQUEST._serialized_start = 1887
    _CANCELTRAININGJOBREQUEST._serialized_end = 1929
    _CANCELTRAININGJOBRESPONSE._serialized_start = 1931
    _CANCELTRAININGJOBRESPONSE._serialized_end = 1958
    _MLTRAININGSERVICE._serialized_start = 2357
    _MLTRAININGSERVICE._serialized_end = 2852