"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import httpbody_pb2 as google_dot_api_dot_httpbody__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(component/audioinput/v1/audioinput.proto\x12\x1cviam.component.audioinput.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x19google/api/httpbody.proto\x1a\x1egoogle/protobuf/duration.proto"Z\n\rRecordRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x125\n\x08duration\x18\x02 \x01(\x0b2\x19.google.protobuf.DurationR\x08duration"\xa2\x01\n\x0eAudioChunkInfo\x12O\n\rsample_format\x18\x01 \x01(\x0e2*.viam.component.audioinput.v1.SampleFormatR\x0csampleFormat\x12\x1a\n\x08channels\x18\x02 \x01(\rR\x08channels\x12#\n\rsampling_rate\x18\x03 \x01(\x03R\x0csamplingRate"8\n\nAudioChunk\x12\x12\n\x04data\x18\x01 \x01(\x0cR\x04data\x12\x16\n\x06length\x18\x02 \x01(\rR\x06length"t\n\rChunksRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12O\n\rsample_format\x18\x02 \x01(\x0e2*.viam.component.audioinput.v1.SampleFormatR\x0csampleFormat"\x9e\x01\n\x0eChunksResponse\x12B\n\x04info\x18\x01 \x01(\x0b2,.viam.component.audioinput.v1.AudioChunkInfoH\x00R\x04info\x12@\n\x05chunk\x18\x02 \x01(\x0b2(.viam.component.audioinput.v1.AudioChunkH\x00R\x05chunkB\x06\n\x04type"\'\n\x11PropertiesRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name"\x96\x02\n\x12PropertiesResponse\x12#\n\rchannel_count\x18\x01 \x01(\rR\x0cchannelCount\x123\n\x07latency\x18\x02 \x01(\x0b2\x19.google.protobuf.DurationR\x07latency\x12\x1f\n\x0bsample_rate\x18\x03 \x01(\rR\nsampleRate\x12\x1f\n\x0bsample_size\x18\x04 \x01(\rR\nsampleSize\x12"\n\ris_big_endian\x18\x05 \x01(\x08R\x0bisBigEndian\x12\x19\n\x08is_float\x18\x06 \x01(\x08R\x07isFloat\x12%\n\x0eis_interleaved\x18\x07 \x01(\x08R\risInterleaved*y\n\x0cSampleFormat\x12\x1d\n\x19SAMPLE_FORMAT_UNSPECIFIED\x10\x00\x12#\n\x1fSAMPLE_FORMAT_INT16_INTERLEAVED\x10\x01\x12%\n!SAMPLE_FORMAT_FLOAT32_INTERLEAVED\x10\x022\xb0\x03\n\x11AudioInputService\x12e\n\x06Chunks\x12+.viam.component.audioinput.v1.ChunksRequest\x1a,.viam.component.audioinput.v1.ChunksResponse0\x01\x12\xac\x01\n\nProperties\x12/.viam.component.audioinput.v1.PropertiesRequest\x1a0.viam.component.audioinput.v1.PropertiesResponse";\x82\xd3\xe4\x93\x025\x123/viam/api/v1/component/audioinput/{name}/properties\x12\x84\x01\n\x06Record\x12+.viam.component.audioinput.v1.RecordRequest\x1a\x14.google.api.HttpBody"7\x82\xd3\xe4\x93\x021\x12//viam/api/v1/component/audioinput/{name}/recordBK\n com.viam.component.audioinput.v1Z\'go.viam.com/api/component/audioinput/v1b\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'component.audioinput.v1.audioinput_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b"\n com.viam.component.audioinput.v1Z'go.viam.com/api/component/audioinput/v1"
    _AUDIOINPUTSERVICE.methods_by_name['Properties']._options = None
    _AUDIOINPUTSERVICE.methods_by_name['Properties']._serialized_options = b'\x82\xd3\xe4\x93\x025\x123/viam/api/v1/component/audioinput/{name}/properties'
    _AUDIOINPUTSERVICE.methods_by_name['Record']._options = None
    _AUDIOINPUTSERVICE.methods_by_name['Record']._serialized_options = b'\x82\xd3\xe4\x93\x021\x12//viam/api/v1/component/audioinput/{name}/record'
    _SAMPLEFORMAT._serialized_start = 1079
    _SAMPLEFORMAT._serialized_end = 1200
    _RECORDREQUEST._serialized_start = 163
    _RECORDREQUEST._serialized_end = 253
    _AUDIOCHUNKINFO._serialized_start = 256
    _AUDIOCHUNKINFO._serialized_end = 418
    _AUDIOCHUNK._serialized_start = 420
    _AUDIOCHUNK._serialized_end = 476
    _CHUNKSREQUEST._serialized_start = 478
    _CHUNKSREQUEST._serialized_end = 594
    _CHUNKSRESPONSE._serialized_start = 597
    _CHUNKSRESPONSE._serialized_end = 755
    _PROPERTIESREQUEST._serialized_start = 757
    _PROPERTIESREQUEST._serialized_end = 796
    _PROPERTIESRESPONSE._serialized_start = 799
    _PROPERTIESRESPONSE._serialized_end = 1077
    _AUDIOINPUTSERVICE._serialized_start = 1203
    _AUDIOINPUTSERVICE._serialized_end = 1635