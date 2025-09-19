"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 2, '', 'service/worldstatestore/v1/world_state_store.proto')
_sym_db = _symbol_database.Default()
from ....common.v1 import common_pb2 as common_dot_v1_dot_common__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2service/worldstatestore/v1/world_state_store.proto\x12\x1fviam.service.worldstatestore.v1\x1a\x16common/v1/common.proto\x1a\x1cgoogle/api/annotations.proto\x1a google/protobuf/field_mask.proto\x1a\x1cgoogle/protobuf/struct.proto"U\n\x10ListUUIDsRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra")\n\x11ListUUIDsResponse\x12\x14\n\x05uuids\x18\x01 \x03(\x0cR\x05uuids"l\n\x13GetTransformRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x12\n\x04uuid\x18\x02 \x01(\x0cR\x04uuid\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"O\n\x14GetTransformResponse\x127\n\ttransform\x18\x02 \x01(\x0b2\x19.viam.common.v1.TransformR\ttransform"b\n\x1dStreamTransformChangesRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"\xf3\x01\n\x1eStreamTransformChangesResponse\x12U\n\x0bchange_type\x18\x01 \x01(\x0e24.viam.service.worldstatestore.v1.TransformChangeTypeR\nchangeType\x127\n\ttransform\x18\x02 \x01(\x0b2\x19.viam.common.v1.TransformR\ttransform\x12A\n\x0eupdated_fields\x18\x03 \x01(\x0b2\x1a.google.protobuf.FieldMaskR\rupdatedFields*\xa3\x01\n\x13TransformChangeType\x12%\n!TRANSFORM_CHANGE_TYPE_UNSPECIFIED\x10\x00\x12\x1f\n\x1bTRANSFORM_CHANGE_TYPE_ADDED\x10\x01\x12!\n\x1dTRANSFORM_CHANGE_TYPE_REMOVED\x10\x02\x12!\n\x1dTRANSFORM_CHANGE_TYPE_UPDATED\x10\x032\x8c\x05\n\x16WorldStateStoreService\x12t\n\tListUUIDs\x121.viam.service.worldstatestore.v1.ListUUIDsRequest\x1a2.viam.service.worldstatestore.v1.ListUUIDsResponse"\x00\x12}\n\x0cGetTransform\x124.viam.service.worldstatestore.v1.GetTransformRequest\x1a5.viam.service.worldstatestore.v1.GetTransformResponse"\x00\x12\xe9\x01\n\x16StreamTransformChanges\x12>.viam.service.worldstatestore.v1.StreamTransformChangesRequest\x1a?.viam.service.worldstatestore.v1.StreamTransformChangesResponse"L\x82\xd3\xe4\x93\x02F\x12D/viam/api/v1/service/worldstatestore/{name}/stream_transform_changes0\x01\x12\x90\x01\n\tDoCommand\x12 .viam.common.v1.DoCommandRequest\x1a!.viam.common.v1.DoCommandResponse">\x82\xd3\xe4\x93\x028"6/viam/api/v1/service/worldstatestore/{name}/do_commandBQ\n#com.viam.service.worldstatestore.v1Z*go.viam.com/api/service/worldstatestore/v1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'service.worldstatestore.v1.world_state_store_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.viam.service.worldstatestore.v1Z*go.viam.com/api/service/worldstatestore/v1'
    _globals['_WORLDSTATESTORESERVICE'].methods_by_name['StreamTransformChanges']._loaded_options = None
    _globals['_WORLDSTATESTORESERVICE'].methods_by_name['StreamTransformChanges']._serialized_options = b'\x82\xd3\xe4\x93\x02F\x12D/viam/api/v1/service/worldstatestore/{name}/stream_transform_changes'
    _globals['_WORLDSTATESTORESERVICE'].methods_by_name['DoCommand']._loaded_options = None
    _globals['_WORLDSTATESTORESERVICE'].methods_by_name['DoCommand']._serialized_options = b'\x82\xd3\xe4\x93\x028"6/viam/api/v1/service/worldstatestore/{name}/do_command'
    _globals['_TRANSFORMCHANGETYPE']._serialized_start = 873
    _globals['_TRANSFORMCHANGETYPE']._serialized_end = 1036
    _globals['_LISTUUIDSREQUEST']._serialized_start = 205
    _globals['_LISTUUIDSREQUEST']._serialized_end = 290
    _globals['_LISTUUIDSRESPONSE']._serialized_start = 292
    _globals['_LISTUUIDSRESPONSE']._serialized_end = 333
    _globals['_GETTRANSFORMREQUEST']._serialized_start = 335
    _globals['_GETTRANSFORMREQUEST']._serialized_end = 443
    _globals['_GETTRANSFORMRESPONSE']._serialized_start = 445
    _globals['_GETTRANSFORMRESPONSE']._serialized_end = 524
    _globals['_STREAMTRANSFORMCHANGESREQUEST']._serialized_start = 526
    _globals['_STREAMTRANSFORMCHANGESREQUEST']._serialized_end = 624
    _globals['_STREAMTRANSFORMCHANGESRESPONSE']._serialized_start = 627
    _globals['_STREAMTRANSFORMCHANGESRESPONSE']._serialized_end = 870
    _globals['_WORLDSTATESTORESERVICE']._serialized_start = 1039
    _globals['_WORLDSTATESTORESERVICE']._serialized_end = 1691