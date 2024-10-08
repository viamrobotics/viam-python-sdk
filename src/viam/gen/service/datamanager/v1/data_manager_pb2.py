"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....common.v1 import common_pb2 as common_dot_v1_dot_common__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)service/datamanager/v1/data_manager.proto\x12\x1bviam.service.datamanager.v1\x1a\x16common/v1/common.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1cgoogle/protobuf/struct.proto"P\n\x0bSyncRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"\x0e\n\x0cSyncResponse2\xbb\x02\n\x12DataManagerService\x12\x95\x01\n\x04Sync\x12(.viam.service.datamanager.v1.SyncRequest\x1a).viam.service.datamanager.v1.SyncResponse"8\x82\xd3\xe4\x93\x022"0/viam/api/v1/service/datamanager/{name}/datasync\x12\x8c\x01\n\tDoCommand\x12 .viam.common.v1.DoCommandRequest\x1a!.viam.common.v1.DoCommandResponse":\x82\xd3\xe4\x93\x024"2/viam/api/v1/service/datamanager/{name}/do_commandBI\n\x1fcom.viam.service.datamanager.v1Z&go.viam.com/api/service/datamanager/v1b\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'service.datamanager.v1.data_manager_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n\x1fcom.viam.service.datamanager.v1Z&go.viam.com/api/service/datamanager/v1'
    _DATAMANAGERSERVICE.methods_by_name['Sync']._options = None
    _DATAMANAGERSERVICE.methods_by_name['Sync']._serialized_options = b'\x82\xd3\xe4\x93\x022"0/viam/api/v1/service/datamanager/{name}/datasync'
    _DATAMANAGERSERVICE.methods_by_name['DoCommand']._options = None
    _DATAMANAGERSERVICE.methods_by_name['DoCommand']._serialized_options = b'\x82\xd3\xe4\x93\x024"2/viam/api/v1/service/datamanager/{name}/do_command'
    _SYNCREQUEST._serialized_start = 158
    _SYNCREQUEST._serialized_end = 238
    _SYNCRESPONSE._serialized_start = 240
    _SYNCRESPONSE._serialized_end = 254
    _DATAMANAGERSERVICE._serialized_start = 257
    _DATAMANAGERSERVICE._serialized_end = 572