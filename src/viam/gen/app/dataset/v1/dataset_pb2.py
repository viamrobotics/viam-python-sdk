"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 2, '', 'app/dataset/v1/dataset.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1capp/dataset/v1/dataset.proto\x12\x13viam.app.dataset.v1\x1a\x1fgoogle/protobuf/timestamp.proto"\x95\x01\n\x07Dataset\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12\'\n\x0forganization_id\x18\x03 \x01(\tR\x0eorganizationId\x12=\n\x0ctime_created\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampR\x0btimeCreated"S\n\x14CreateDatasetRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\'\n\x0forganization_id\x18\x02 \x01(\tR\x0eorganizationId"\'\n\x15CreateDatasetResponse\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id"&\n\x14DeleteDatasetRequest\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id"\x17\n\x15DeleteDatasetResponse":\n\x14RenameDatasetRequest\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name"\x17\n\x15RenameDatasetResponse"N\n#ListDatasetsByOrganizationIDRequest\x12\'\n\x0forganization_id\x18\x01 \x01(\tR\x0eorganizationId"`\n$ListDatasetsByOrganizationIDResponse\x128\n\x08datasets\x18\x01 \x03(\x0b2\x1c.viam.app.dataset.v1.DatasetR\x08datasets",\n\x18ListDatasetsByIDsRequest\x12\x10\n\x03ids\x18\x01 \x03(\tR\x03ids"U\n\x19ListDatasetsByIDsResponse\x128\n\x08datasets\x18\x01 \x03(\x0b2\x1c.viam.app.dataset.v1.DatasetR\x08datasets2\xd2\x04\n\x0eDatasetService\x12f\n\rCreateDataset\x12).viam.app.dataset.v1.CreateDatasetRequest\x1a*.viam.app.dataset.v1.CreateDatasetResponse\x12f\n\rDeleteDataset\x12).viam.app.dataset.v1.DeleteDatasetRequest\x1a*.viam.app.dataset.v1.DeleteDatasetResponse\x12f\n\rRenameDataset\x12).viam.app.dataset.v1.RenameDatasetRequest\x1a*.viam.app.dataset.v1.RenameDatasetResponse\x12\x93\x01\n\x1cListDatasetsByOrganizationID\x128.viam.app.dataset.v1.ListDatasetsByOrganizationIDRequest\x1a9.viam.app.dataset.v1.ListDatasetsByOrganizationIDResponse\x12r\n\x11ListDatasetsByIDs\x12-.viam.app.dataset.v1.ListDatasetsByIDsRequest\x1a..viam.app.dataset.v1.ListDatasetsByIDsResponseB Z\x1ego.viam.com/api/app/dataset/v1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'app.dataset.v1.dataset_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z\x1ego.viam.com/api/app/dataset/v1'
    _globals['_DATASET']._serialized_start = 87
    _globals['_DATASET']._serialized_end = 236
    _globals['_CREATEDATASETREQUEST']._serialized_start = 238
    _globals['_CREATEDATASETREQUEST']._serialized_end = 321
    _globals['_CREATEDATASETRESPONSE']._serialized_start = 323
    _globals['_CREATEDATASETRESPONSE']._serialized_end = 362
    _globals['_DELETEDATASETREQUEST']._serialized_start = 364
    _globals['_DELETEDATASETREQUEST']._serialized_end = 402
    _globals['_DELETEDATASETRESPONSE']._serialized_start = 404
    _globals['_DELETEDATASETRESPONSE']._serialized_end = 427
    _globals['_RENAMEDATASETREQUEST']._serialized_start = 429
    _globals['_RENAMEDATASETREQUEST']._serialized_end = 487
    _globals['_RENAMEDATASETRESPONSE']._serialized_start = 489
    _globals['_RENAMEDATASETRESPONSE']._serialized_end = 512
    _globals['_LISTDATASETSBYORGANIZATIONIDREQUEST']._serialized_start = 514
    _globals['_LISTDATASETSBYORGANIZATIONIDREQUEST']._serialized_end = 592
    _globals['_LISTDATASETSBYORGANIZATIONIDRESPONSE']._serialized_start = 594
    _globals['_LISTDATASETSBYORGANIZATIONIDRESPONSE']._serialized_end = 690
    _globals['_LISTDATASETSBYIDSREQUEST']._serialized_start = 692
    _globals['_LISTDATASETSBYIDSREQUEST']._serialized_end = 736
    _globals['_LISTDATASETSBYIDSRESPONSE']._serialized_start = 738
    _globals['_LISTDATASETSBYIDSRESPONSE']._serialized_end = 823
    _globals['_DATASETSERVICE']._serialized_start = 826
    _globals['_DATASETSERVICE']._serialized_end = 1420