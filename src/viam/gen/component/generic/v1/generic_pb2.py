"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 2, '', 'component/generic/v1/generic.proto')
_sym_db = _symbol_database.Default()
from ....common.v1 import common_pb2 as common_dot_v1_dot_common__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n"component/generic/v1/generic.proto\x12\x19viam.component.generic.v1\x1a\x16common/v1/common.proto\x1a\x1cgoogle/api/annotations.proto2\xb6\x02\n\x0eGenericService\x12\x8a\x01\n\tDoCommand\x12 .viam.common.v1.DoCommandRequest\x1a!.viam.common.v1.DoCommandResponse"8\x82\xd3\xe4\x93\x022"0/viam/api/v1/component/generic/{name}/do_command\x12\x96\x01\n\rGetGeometries\x12$.viam.common.v1.GetGeometriesRequest\x1a%.viam.common.v1.GetGeometriesResponse"8\x82\xd3\xe4\x93\x022\x120/viam/api/v1/component/generic/{name}/geometriesBE\n\x1dcom.viam.component.generic.v1Z$go.viam.com/api/component/generic/v1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'component.generic.v1.generic_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1dcom.viam.component.generic.v1Z$go.viam.com/api/component/generic/v1'
    _globals['_GENERICSERVICE'].methods_by_name['DoCommand']._loaded_options = None
    _globals['_GENERICSERVICE'].methods_by_name['DoCommand']._serialized_options = b'\x82\xd3\xe4\x93\x022"0/viam/api/v1/component/generic/{name}/do_command'
    _globals['_GENERICSERVICE'].methods_by_name['GetGeometries']._loaded_options = None
    _globals['_GENERICSERVICE'].methods_by_name['GetGeometries']._serialized_options = b'\x82\xd3\xe4\x93\x022\x120/viam/api/v1/component/generic/{name}/geometries'
    _globals['_GENERICSERVICE']._serialized_start = 120
    _globals['_GENERICSERVICE']._serialized_end = 430