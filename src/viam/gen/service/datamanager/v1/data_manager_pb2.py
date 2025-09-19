"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 2, '', 'service/datamanager/v1/data_manager.proto')
_sym_db = _symbol_database.Default()
from ....app.datasync.v1 import data_sync_pb2 as app_dot_datasync_dot_v1_dot_data__sync__pb2
from ....common.v1 import common_pb2 as common_dot_v1_dot_common__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)service/datamanager/v1/data_manager.proto\x12\x1bviam.service.datamanager.v1\x1a\x1fapp/datasync/v1/data_sync.proto\x1a\x16common/v1/common.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1cgoogle/protobuf/struct.proto"P\n\x0bSyncRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"\x0e\n\x0cSyncResponse"\xf9\x01\n!UploadBinaryDataToDatasetsRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x1f\n\x0bbinary_data\x18\x02 \x01(\x0cR\nbinaryData\x12\x12\n\x04tags\x18\x03 \x03(\tR\x04tags\x12\x1f\n\x0bdataset_ids\x18\x04 \x03(\tR\ndatasetIds\x12;\n\tmime_type\x18\x05 \x01(\x0e2\x1e.viam.app.datasync.v1.MimeTypeR\x08mimeType\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"$\n"UploadBinaryDataToDatasetsResponse2\xab\x04\n\x12DataManagerService\x12\x95\x01\n\x04Sync\x12(.viam.service.datamanager.v1.SyncRequest\x1a).viam.service.datamanager.v1.SyncResponse"8\x82\xd3\xe4\x93\x022"0/viam/api/v1/service/datamanager/{name}/datasync\x12\x8c\x01\n\tDoCommand\x12 .viam.common.v1.DoCommandRequest\x1a!.viam.common.v1.DoCommandResponse":\x82\xd3\xe4\x93\x024"2/viam/api/v1/service/datamanager/{name}/do_command\x12\xed\x01\n\x1aUploadBinaryDataToDatasets\x12>.viam.service.datamanager.v1.UploadBinaryDataToDatasetsRequest\x1a?.viam.service.datamanager.v1.UploadBinaryDataToDatasetsResponse"N\x82\xd3\xe4\x93\x02H"F/viam/api/v1/service/datamanager/{name}/upload_binary_data_to_datasetsBI\n\x1fcom.viam.service.datamanager.v1Z&go.viam.com/api/service/datamanager/v1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'service.datamanager.v1.data_manager_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1fcom.viam.service.datamanager.v1Z&go.viam.com/api/service/datamanager/v1'
    _globals['_DATAMANAGERSERVICE'].methods_by_name['Sync']._loaded_options = None
    _globals['_DATAMANAGERSERVICE'].methods_by_name['Sync']._serialized_options = b'\x82\xd3\xe4\x93\x022"0/viam/api/v1/service/datamanager/{name}/datasync'
    _globals['_DATAMANAGERSERVICE'].methods_by_name['DoCommand']._loaded_options = None
    _globals['_DATAMANAGERSERVICE'].methods_by_name['DoCommand']._serialized_options = b'\x82\xd3\xe4\x93\x024"2/viam/api/v1/service/datamanager/{name}/do_command'
    _globals['_DATAMANAGERSERVICE'].methods_by_name['UploadBinaryDataToDatasets']._loaded_options = None
    _globals['_DATAMANAGERSERVICE'].methods_by_name['UploadBinaryDataToDatasets']._serialized_options = b'\x82\xd3\xe4\x93\x02H"F/viam/api/v1/service/datamanager/{name}/upload_binary_data_to_datasets'
    _globals['_SYNCREQUEST']._serialized_start = 191
    _globals['_SYNCREQUEST']._serialized_end = 271
    _globals['_SYNCRESPONSE']._serialized_start = 273
    _globals['_SYNCRESPONSE']._serialized_end = 287
    _globals['_UPLOADBINARYDATATODATASETSREQUEST']._serialized_start = 290
    _globals['_UPLOADBINARYDATATODATASETSREQUEST']._serialized_end = 539
    _globals['_UPLOADBINARYDATATODATASETSRESPONSE']._serialized_start = 541
    _globals['_UPLOADBINARYDATATODATASETSRESPONSE']._serialized_end = 577
    _globals['_DATAMANAGERSERVICE']._serialized_start = 580
    _globals['_DATAMANAGERSERVICE']._serialized_end = 1135