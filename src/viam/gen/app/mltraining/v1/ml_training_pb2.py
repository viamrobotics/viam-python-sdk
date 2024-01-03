"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
from ....tagger.v1 import tagger_pb2 as tagger_dot_v1_dot_tagger__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#app/mltraining/v1/ml_training.proto\x12\x16viam.app.mltraining.v1\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x17google/rpc/status.proto\x1a\x16tagger/v1/tagger.proto"\x8a\x04\n\x18SubmitTrainingJobRequest\x12G\n\ndataset_id\x18\x07 \x01(\tB(\x9a\x84\x9e\x03#bson:"dataset_id" json:"dataset_id"R\tdatasetId\x12[\n\x0forganization_id\x18\x02 \x01(\tB2\x9a\x84\x9e\x03-bson:"organization_id" json:"organization_id"R\x0eorganizationId\x12G\n\nmodel_name\x18\x03 \x01(\tB(\x9a\x84\x9e\x03#bson:"model_name" json:"model_name"R\tmodelName\x12S\n\rmodel_version\x18\x04 \x01(\tB.\x9a\x84\x9e\x03)bson:"model_version" json:"model_version"R\x0cmodelVersion\x12j\n\nmodel_type\x18\x05 \x01(\x0e2!.viam.app.mltraining.v1.ModelTypeB(\x9a\x84\x9e\x03#bson:"model_type" json:"model_type"R\tmodelType\x120\n\x04tags\x18\x06 \x03(\tB\x1c\x9a\x84\x9e\x03\x17bson:"tags" json:"tags"R\x04tagsJ\x04\x08\x01\x10\x02R\x06filter"+\n\x19SubmitTrainingJobResponse\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id"\'\n\x15GetTrainingJobRequest\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id"a\n\x16GetTrainingJobResponse\x12G\n\x08metadata\x18\x01 \x01(\x0b2+.viam.app.mltraining.v1.TrainingJobMetadataR\x08metadata"\x82\x01\n\x17ListTrainingJobsRequest\x12\'\n\x0forganization_id\x18\x01 \x01(\tR\x0eorganizationId\x12>\n\x06status\x18\x02 \x01(\x0e2&.viam.app.mltraining.v1.TrainingStatusR\x06status"[\n\x18ListTrainingJobsResponse\x12?\n\x04jobs\x18\x01 \x03(\x0b2+.viam.app.mltraining.v1.TrainingJobMetadataR\x04jobs"\xb7\x07\n\x13TrainingJobMetadata\x12n\n\x07request\x18\x01 \x01(\x0b20.viam.app.mltraining.v1.SubmitTrainingJobRequestB"\x9a\x84\x9e\x03\x1dbson:"request" json:"request"R\x07request\x12`\n\x06status\x18\x02 \x01(\x0e2&.viam.app.mltraining.v1.TrainingStatusB \x9a\x84\x9e\x03\x1bbson:"status" json:"status"R\x06status\x12c\n\ncreated_on\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB(\x9a\x84\x9e\x03#bson:"created_on" json:"created_on"R\tcreatedOn\x12o\n\rlast_modified\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampB.\x9a\x84\x9e\x03)bson:"last_modified" json:"last_modified"R\x0clastModified\x12Z\n\x0fsynced_model_id\x18\x05 \x01(\tB2\x9a\x84\x9e\x03-bson:"synced_model_id" json:"synced_model_id"R\rsyncedModelId\x123\n\x02id\x18\x07 \x01(\tB#\x9a\x84\x9e\x03\x1ebson:"_id" json:"id,omitempty"R\x02id\x12c\n\x0cerror_status\x18\x08 \x01(\x0b2\x12.google.rpc.StatusB,\x9a\x84\x9e\x03\'bson:"error_status" json:"error_status"R\x0berrorStatus\x12{\n\x10training_started\x18\t \x01(\x0b2\x1a.google.protobuf.TimestampB4\x9a\x84\x9e\x03/bson:"training_started" json:"training_started"R\x0ftrainingStarted\x12s\n\x0etraining_ended\x18\n \x01(\x0b2\x1a.google.protobuf.TimestampB0\x9a\x84\x9e\x03+bson:"training_ended" json:"training_ended"R\rtrainingEndedJ\x04\x08\x06\x10\x07R\nuser_email"*\n\x18CancelTrainingJobRequest\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id"\x1b\n\x19CancelTrainingJobResponse"3\n!DeleteCompletedTrainingJobRequest\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id"$\n"DeleteCompletedTrainingJobResponse*\x9f\x01\n\tModelType\x12\x1a\n\x16MODEL_TYPE_UNSPECIFIED\x10\x00\x12*\n&MODEL_TYPE_SINGLE_LABEL_CLASSIFICATION\x10\x01\x12)\n%MODEL_TYPE_MULTI_LABEL_CLASSIFICATION\x10\x02\x12\x1f\n\x1bMODEL_TYPE_OBJECT_DETECTION\x10\x03*\xe7\x01\n\x0eTrainingStatus\x12\x1f\n\x1bTRAINING_STATUS_UNSPECIFIED\x10\x00\x12\x1b\n\x17TRAINING_STATUS_PENDING\x10\x01\x12\x1f\n\x1bTRAINING_STATUS_IN_PROGRESS\x10\x02\x12\x1d\n\x19TRAINING_STATUS_COMPLETED\x10\x03\x12\x1a\n\x16TRAINING_STATUS_FAILED\x10\x04\x12\x1c\n\x18TRAINING_STATUS_CANCELED\x10\x05\x12\x1d\n\x19TRAINING_STATUS_CANCELING\x10\x062\x85\x05\n\x11MLTrainingService\x12x\n\x11SubmitTrainingJob\x120.viam.app.mltraining.v1.SubmitTrainingJobRequest\x1a1.viam.app.mltraining.v1.SubmitTrainingJobResponse\x12o\n\x0eGetTrainingJob\x12-.viam.app.mltraining.v1.GetTrainingJobRequest\x1a..viam.app.mltraining.v1.GetTrainingJobResponse\x12u\n\x10ListTrainingJobs\x12/.viam.app.mltraining.v1.ListTrainingJobsRequest\x1a0.viam.app.mltraining.v1.ListTrainingJobsResponse\x12x\n\x11CancelTrainingJob\x120.viam.app.mltraining.v1.CancelTrainingJobRequest\x1a1.viam.app.mltraining.v1.CancelTrainingJobResponse\x12\x93\x01\n\x1aDeleteCompletedTrainingJob\x129.viam.app.mltraining.v1.DeleteCompletedTrainingJobRequest\x1a:.viam.app.mltraining.v1.DeleteCompletedTrainingJobResponseB#Z!go.viam.com/api/app/mltraining/v1b\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'app.mltraining.v1.ml_training_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z!go.viam.com/api/app/mltraining/v1'
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
    _TRAININGJOBMETADATA.fields_by_name['training_started']._options = None
    _TRAININGJOBMETADATA.fields_by_name['training_started']._serialized_options = b'\x9a\x84\x9e\x03/bson:"training_started" json:"training_started"'
    _TRAININGJOBMETADATA.fields_by_name['training_ended']._options = None
    _TRAININGJOBMETADATA.fields_by_name['training_ended']._serialized_options = b'\x9a\x84\x9e\x03+bson:"training_ended" json:"training_ended"'
    _MODELTYPE._serialized_start = 2200
    _MODELTYPE._serialized_end = 2359
    _TRAININGSTATUS._serialized_start = 2362
    _TRAININGSTATUS._serialized_end = 2593
    _SUBMITTRAININGJOBREQUEST._serialized_start = 146
    _SUBMITTRAININGJOBREQUEST._serialized_end = 668
    _SUBMITTRAININGJOBRESPONSE._serialized_start = 670
    _SUBMITTRAININGJOBRESPONSE._serialized_end = 713
    _GETTRAININGJOBREQUEST._serialized_start = 715
    _GETTRAININGJOBREQUEST._serialized_end = 754
    _GETTRAININGJOBRESPONSE._serialized_start = 756
    _GETTRAININGJOBRESPONSE._serialized_end = 853
    _LISTTRAININGJOBSREQUEST._serialized_start = 856
    _LISTTRAININGJOBSREQUEST._serialized_end = 986
    _LISTTRAININGJOBSRESPONSE._serialized_start = 988
    _LISTTRAININGJOBSRESPONSE._serialized_end = 1079
    _TRAININGJOBMETADATA._serialized_start = 1082
    _TRAININGJOBMETADATA._serialized_end = 2033
    _CANCELTRAININGJOBREQUEST._serialized_start = 2035
    _CANCELTRAININGJOBREQUEST._serialized_end = 2077
    _CANCELTRAININGJOBRESPONSE._serialized_start = 2079
    _CANCELTRAININGJOBRESPONSE._serialized_end = 2106
    _DELETECOMPLETEDTRAININGJOBREQUEST._serialized_start = 2108
    _DELETECOMPLETEDTRAININGJOBREQUEST._serialized_end = 2159
    _DELETECOMPLETEDTRAININGJOBRESPONSE._serialized_start = 2161
    _DELETECOMPLETEDTRAININGJOBRESPONSE._serialized_end = 2197
    _MLTRAININGSERVICE._serialized_start = 2596
    _MLTRAININGSERVICE._serialized_end = 3241