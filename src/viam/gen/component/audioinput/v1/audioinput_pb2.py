"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....common.v1 import common_pb2 as common_dot_v1_dot_common__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import httpbody_pb2 as google_dot_api_dot_httpbody__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(component/audioinput/v1/audioinput.proto\x12\x1cviam.component.audioinput.v1\x1a\x16common/v1/common.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x19google/api/httpbody.proto\x1a\x1egoogle/protobuf/duration.proto"Z\n\rRecordRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x125\n\x08duration\x18\x02 \x01(\x0b2\x19.google.protobuf.DurationR\x08duration"\xa2\x01\n\x0eAudioChunkInfo\x12O\n\rsample_format\x18\x01 \x01(\x0e2*.viam.component.audioinput.v1.SampleFormatR\x0csampleFormat\x12\x1a\n\x08channels\x18\x02 \x01(\rR\x08channels\x12#\n\rsampling_rate\x18\x03 \x01(\x03R\x0csamplingRate"8\n\nAudioChunk\x12\x12\n\x04data\x18\x01 \x01(\x0cR\x04data\x12\x16\n\x06length\x18\x02 \x01(\rR\x06length"t\n\rChunksRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12O\n\rsample_format\x18\x02 \x01(\x0e2*.viam.component.audioinput.v1.SampleFormatR\x0csampleFormat"\x9e\x01\n\x0eChunksResponse\x12B\n\x04info\x18\x01 \x01(\x0b2,.viam.component.audioinput.v1.AudioChunkInfoH\x00R\x04info\x12@\n\x05chunk\x18\x02 \x01(\x0b2(.viam.component.audioinput.v1.AudioChunkH\x00R\x05chunkB\x06\n\x04type"\'\n\x11PropertiesRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name"\x96\x02\n\x12PropertiesResponse\x12#\n\rchannel_count\x18\x01 \x01(\rR\x0cchannelCount\x123\n\x07latency\x18\x02 \x01(\x0b2\x19.google.protobuf.DurationR\x07latency\x12\x1f\n\x0bsample_rate\x18\x03 \x01(\rR\nsampleRate\x12\x1f\n\x0bsample_size\x18\x04 \x01(\rR\nsampleSize\x12"\n\ris_big_endian\x18\x05 \x01(\x08R\x0bisBigEndian\x12\x19\n\x08is_float\x18\x06 \x01(\x08R\x07isFloat\x12%\n\x0eis_interleaved\x18\x07 \x01(\x08R\risInterleaved*y\n\x0cSampleFormat\x12\x1d\n\x19SAMPLE_FORMAT_UNSPECIFIED\x10\x00\x12#\n\x1fSAMPLE_FORMAT_INT16_INTERLEAVED\x10\x01\x12%\n!SAMPLE_FORMAT_FLOAT32_INTERLEAVED\x10\x022\xdc\x05\n\x11AudioInputService\x12e\n\x06Chunks\x12+.viam.component.audioinput.v1.ChunksRequest\x1a,.viam.component.audioinput.v1.ChunksResponse0\x01\x12\xac\x01\n\nProperties\x12/.viam.component.audioinput.v1.PropertiesRequest\x1a0.viam.component.audioinput.v1.PropertiesResponse";\x82\xd3\xe4\x93\x025\x123/viam/api/v1/component/audioinput/{name}/properties\x12\x84\x01\n\x06Record\x12+.viam.component.audioinput.v1.RecordRequest\x1a\x14.google.api.HttpBody"7\x82\xd3\xe4\x93\x021\x12//viam/api/v1/component/audioinput/{name}/record\x12\x8d\x01\n\tDoCommand\x12 .viam.common.v1.DoCommandRequest\x1a!.viam.common.v1.DoCommandResponse";\x82\xd3\xe4\x93\x025"3/viam/api/v1/component/audioinput/{name}/do_command\x12\x99\x01\n\rGetGeometries\x12$.viam.common.v1.GetGeometriesRequest\x1a%.viam.common.v1.GetGeometriesResponse";\x82\xd3\xe4\x93\x025\x123/viam/api/v1/component/audioinput/{name}/geometriesBK\n com.viam.component.audioinput.v1Z\'go.viam.com/api/component/audioinput/v1b\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'component.audioinput.v1.audioinput_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b"\n com.viam.component.audioinput.v1Z'go.viam.com/api/component/audioinput/v1"
    _AUDIOINPUTSERVICE.methods_by_name['Properties']._options = None
    _AUDIOINPUTSERVICE.methods_by_name['Properties']._serialized_options = b'\x82\xd3\xe4\x93\x025\x123/viam/api/v1/component/audioinput/{name}/properties'
    _AUDIOINPUTSERVICE.methods_by_name['Record']._options = None
    _AUDIOINPUTSERVICE.methods_by_name['Record']._serialized_options = b'\x82\xd3\xe4\x93\x021\x12//viam/api/v1/component/audioinput/{name}/record'
    _AUDIOINPUTSERVICE.methods_by_name['DoCommand']._options = None
    _AUDIOINPUTSERVICE.methods_by_name['DoCommand']._serialized_options = b'\x82\xd3\xe4\x93\x025"3/viam/api/v1/component/audioinput/{name}/do_command'
    _AUDIOINPUTSERVICE.methods_by_name['GetGeometries']._options = None
    _AUDIOINPUTSERVICE.methods_by_name['GetGeometries']._serialized_options = b'\x82\xd3\xe4\x93\x025\x123/viam/api/v1/component/audioinput/{name}/geometries'
    _SAMPLEFORMAT._serialized_start = 1103
    _SAMPLEFORMAT._serialized_end = 1224
    _RECORDREQUEST._serialized_start = 187
    _RECORDREQUEST._serialized_end = 277
    _AUDIOCHUNKINFO._serialized_start = 280
    _AUDIOCHUNKINFO._serialized_end = 442
    _AUDIOCHUNK._serialized_start = 444
    _AUDIOCHUNK._serialized_end = 500
    _CHUNKSREQUEST._serialized_start = 502
    _CHUNKSREQUEST._serialized_end = 618
    _CHUNKSRESPONSE._serialized_start = 621
    _CHUNKSRESPONSE._serialized_end = 779
    _PROPERTIESREQUEST._serialized_start = 781
    _PROPERTIESREQUEST._serialized_end = 820
    _PROPERTIESRESPONSE._serialized_start = 823
    _PROPERTIESRESPONSE._serialized_end = 1101
    _AUDIOINPUTSERVICE._serialized_start = 1227
    _AUDIOINPUTSERVICE._serialized_end = 1959