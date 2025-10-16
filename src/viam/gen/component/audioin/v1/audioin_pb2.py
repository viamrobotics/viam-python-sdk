"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 2, '', 'component/audioin/v1/audioin.proto')
_sym_db = _symbol_database.Default()
from ....common.v1 import common_pb2 as common_dot_v1_dot_common__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n"component/audioin/v1/audioin.proto\x12\x19viam.component.audioin.v1\x1a\x16common/v1/common.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1cgoogle/protobuf/struct.proto"\xfa\x01\n\x0fGetAudioRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12)\n\x10duration_seconds\x18\x02 \x01(\x02R\x0fdurationSeconds\x12\x14\n\x05codec\x18\x03 \x01(\tR\x05codec\x12\x1d\n\nrequest_id\x18\x04 \x01(\tR\trequestId\x12D\n\x1eprevious_timestamp_nanoseconds\x18\x05 \x01(\x03R\x1cpreviousTimestampNanoseconds\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"n\n\x10GetAudioResponse\x12;\n\x05audio\x18\x01 \x01(\x0b2%.viam.component.audioin.v1.AudioChunkR\x05audio\x12\x1d\n\nrequest_id\x18\x02 \x01(\tR\trequestId"\xfd\x01\n\nAudioChunk\x12\x1d\n\naudio_data\x18\x01 \x01(\x0cR\taudioData\x128\n\naudio_info\x18\x02 \x01(\x0b2\x19.viam.common.v1.AudioInfoR\taudioInfo\x12>\n\x1bstart_timestamp_nanoseconds\x18\x03 \x01(\x03R\x19startTimestampNanoseconds\x12:\n\x19end_timestamp_nanoseconds\x18\x04 \x01(\x03R\x17endTimestampNanoseconds\x12\x1a\n\x08sequence\x18\x05 \x01(\x05R\x08sequence2\xee\x04\n\x0eAudioInService\x12\x9e\x01\n\x08GetAudio\x12*.viam.component.audioin.v1.GetAudioRequest\x1a+.viam.component.audioin.v1.GetAudioResponse"7\x82\xd3\xe4\x93\x021\x12//viam/api/v1/component/audioin/{name}/get_audio0\x01\x12\x96\x01\n\rGetProperties\x12$.viam.common.v1.GetPropertiesRequest\x1a%.viam.common.v1.GetPropertiesResponse"8\x82\xd3\xe4\x93\x022\x120/viam/api/v1/component/audioin/{name}/properties\x12\x88\x01\n\tDoCommand\x12 .viam.common.v1.DoCommandRequest\x1a!.viam.common.v1.DoCommandResponse"6\x82\xd3\xe4\x93\x020"./viam/api/v1/service/audioin/{name}/do_command\x12\x96\x01\n\rGetGeometries\x12$.viam.common.v1.GetGeometriesRequest\x1a%.viam.common.v1.GetGeometriesResponse"8\x82\xd3\xe4\x93\x022\x120/viam/api/v1/component/audioin/{name}/geometriesBE\n\x1dcom.viam.component.audioin.v1Z$go.viam.com/api/component/audioin/v1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'component.audioin.v1.audioin_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1dcom.viam.component.audioin.v1Z$go.viam.com/api/component/audioin/v1'
    _globals['_AUDIOINSERVICE'].methods_by_name['GetAudio']._loaded_options = None
    _globals['_AUDIOINSERVICE'].methods_by_name['GetAudio']._serialized_options = b'\x82\xd3\xe4\x93\x021\x12//viam/api/v1/component/audioin/{name}/get_audio'
    _globals['_AUDIOINSERVICE'].methods_by_name['GetProperties']._loaded_options = None
    _globals['_AUDIOINSERVICE'].methods_by_name['GetProperties']._serialized_options = b'\x82\xd3\xe4\x93\x022\x120/viam/api/v1/component/audioin/{name}/properties'
    _globals['_AUDIOINSERVICE'].methods_by_name['DoCommand']._loaded_options = None
    _globals['_AUDIOINSERVICE'].methods_by_name['DoCommand']._serialized_options = b'\x82\xd3\xe4\x93\x020"./viam/api/v1/service/audioin/{name}/do_command'
    _globals['_AUDIOINSERVICE'].methods_by_name['GetGeometries']._loaded_options = None
    _globals['_AUDIOINSERVICE'].methods_by_name['GetGeometries']._serialized_options = b'\x82\xd3\xe4\x93\x022\x120/viam/api/v1/component/audioin/{name}/geometries'
    _globals['_GETAUDIOREQUEST']._serialized_start = 150
    _globals['_GETAUDIOREQUEST']._serialized_end = 400
    _globals['_GETAUDIORESPONSE']._serialized_start = 402
    _globals['_GETAUDIORESPONSE']._serialized_end = 512
    _globals['_AUDIOCHUNK']._serialized_start = 515
    _globals['_AUDIOCHUNK']._serialized_end = 768
    _globals['_AUDIOINSERVICE']._serialized_start = 771
    _globals['_AUDIOINSERVICE']._serialized_end = 1393