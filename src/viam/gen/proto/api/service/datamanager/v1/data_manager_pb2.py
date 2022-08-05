"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3proto/api/service/datamanager/v1/data_manager.proto\x12 proto.api.service.datamanager.v1\x1a\x1cgoogle/api/annotations.proto"\r\n\x0bSyncRequest"\x0e\n\x0cSyncResponse2\xaf\x01\n\x12DataManagerService\x12\x98\x01\n\x04Sync\x12-.proto.api.service.datamanager.v1.SyncRequest\x1a..proto.api.service.datamanager.v1.SyncResponse"1\x82\xd3\xe4\x93\x02+")/viam/api/v1/service/datamanager/datasyncBa\n-com.viam.rdk.proto.api.service.datamanager.v1Z0go.viam.com/rdk/proto/api/service/datamanager/v1b\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'proto.api.service.datamanager.v1.data_manager_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n-com.viam.rdk.proto.api.service.datamanager.v1Z0go.viam.com/rdk/proto/api/service/datamanager/v1'
    _DATAMANAGERSERVICE.methods_by_name['Sync']._options = None
    _DATAMANAGERSERVICE.methods_by_name['Sync']._serialized_options = b'\x82\xd3\xe4\x93\x02+")/viam/api/v1/service/datamanager/datasync'
    _SYNCREQUEST._serialized_start = 119
    _SYNCREQUEST._serialized_end = 132
    _SYNCRESPONSE._serialized_start = 134
    _SYNCRESPONSE._serialized_end = 148
    _DATAMANAGERSERVICE._serialized_start = 151
    _DATAMANAGERSERVICE._serialized_end = 326