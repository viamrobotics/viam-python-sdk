"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 2, '', 'component/audioout/v1/audioout.proto')
_sym_db = _symbol_database.Default()
from ....common.v1 import common_pb2 as common_dot_v1_dot_common__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$component/audioout/v1/audioout.proto\x12\x1aviam.component.audioout.v1\x1a\x16common/v1/common.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1cgoogle/protobuf/struct.proto"\xa9\x01\n\x0bPlayRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x1d\n\naudio_data\x18\x02 \x01(\x0cR\taudioData\x128\n\naudio_info\x18\x03 \x01(\x0b2\x19.viam.common.v1.AudioInfoR\taudioInfo\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"\x0e\n\x0cPlayResponse2\xe2\x04\n\x0fAudioOutService\x12\x8e\x01\n\x04Play\x12\'.viam.component.audioout.v1.PlayRequest\x1a(.viam.component.audioout.v1.PlayResponse"3\x82\xd3\xe4\x93\x02-"+/viam/api/v1/component/audioout/{name}/play\x12\x97\x01\n\rGetProperties\x12$.viam.common.v1.GetPropertiesRequest\x1a%.viam.common.v1.GetPropertiesResponse"9\x82\xd3\xe4\x93\x023\x121/viam/api/v1/component/audioout/{name}/properties\x12\x89\x01\n\tDoCommand\x12 .viam.common.v1.DoCommandRequest\x1a!.viam.common.v1.DoCommandResponse"7\x82\xd3\xe4\x93\x021"//viam/api/v1/service/audioout/{name}/do_command\x12\x97\x01\n\rGetGeometries\x12$.viam.common.v1.GetGeometriesRequest\x1a%.viam.common.v1.GetGeometriesResponse"9\x82\xd3\xe4\x93\x023\x121/viam/api/v1/component/audioout/{name}/geometriesBG\n\x1ecom.viam.component.audioout.v1Z%go.viam.com/api/component/audioout/v1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'component.audioout.v1.audioout_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ecom.viam.component.audioout.v1Z%go.viam.com/api/component/audioout/v1'
    _globals['_AUDIOOUTSERVICE'].methods_by_name['Play']._loaded_options = None
    _globals['_AUDIOOUTSERVICE'].methods_by_name['Play']._serialized_options = b'\x82\xd3\xe4\x93\x02-"+/viam/api/v1/component/audioout/{name}/play'
    _globals['_AUDIOOUTSERVICE'].methods_by_name['GetProperties']._loaded_options = None
    _globals['_AUDIOOUTSERVICE'].methods_by_name['GetProperties']._serialized_options = b'\x82\xd3\xe4\x93\x023\x121/viam/api/v1/component/audioout/{name}/properties'
    _globals['_AUDIOOUTSERVICE'].methods_by_name['DoCommand']._loaded_options = None
    _globals['_AUDIOOUTSERVICE'].methods_by_name['DoCommand']._serialized_options = b'\x82\xd3\xe4\x93\x021"//viam/api/v1/service/audioout/{name}/do_command'
    _globals['_AUDIOOUTSERVICE'].methods_by_name['GetGeometries']._loaded_options = None
    _globals['_AUDIOOUTSERVICE'].methods_by_name['GetGeometries']._serialized_options = b'\x82\xd3\xe4\x93\x023\x121/viam/api/v1/component/audioout/{name}/geometries'
    _globals['_PLAYREQUEST']._serialized_start = 153
    _globals['_PLAYREQUEST']._serialized_end = 322
    _globals['_PLAYRESPONSE']._serialized_start = 324
    _globals['_PLAYRESPONSE']._serialized_end = 338
    _globals['_AUDIOOUTSERVICE']._serialized_start = 341
    _globals['_AUDIOOUTSERVICE']._serialized_end = 951