"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16stream/v1/stream.proto\x12\x0fproto.stream.v1"\x14\n\x12ListStreamsRequest"+\n\x13ListStreamsResponse\x12\x14\n\x05names\x18\x01 \x03(\tR\x05names"&\n\x10AddStreamRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name"\x13\n\x11AddStreamResponse")\n\x13RemoveStreamRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name"\x16\n\x14RemoveStreamResponse2\x9a\x02\n\rStreamService\x12X\n\x0bListStreams\x12#.proto.stream.v1.ListStreamsRequest\x1a$.proto.stream.v1.ListStreamsResponse\x12R\n\tAddStream\x12!.proto.stream.v1.AddStreamRequest\x1a".proto.stream.v1.AddStreamResponse\x12[\n\x0cRemoveStream\x12$.proto.stream.v1.RemoveStreamRequest\x1a%.proto.stream.v1.RemoveStreamResponseB.Z,github.com/edaniels/gostream/proto/stream/v1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'stream.v1.stream_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z,github.com/edaniels/gostream/proto/stream/v1'
    _globals['_LISTSTREAMSREQUEST']._serialized_start = 43
    _globals['_LISTSTREAMSREQUEST']._serialized_end = 63
    _globals['_LISTSTREAMSRESPONSE']._serialized_start = 65
    _globals['_LISTSTREAMSRESPONSE']._serialized_end = 108
    _globals['_ADDSTREAMREQUEST']._serialized_start = 110
    _globals['_ADDSTREAMREQUEST']._serialized_end = 148
    _globals['_ADDSTREAMRESPONSE']._serialized_start = 150
    _globals['_ADDSTREAMRESPONSE']._serialized_end = 169
    _globals['_REMOVESTREAMREQUEST']._serialized_start = 171
    _globals['_REMOVESTREAMREQUEST']._serialized_end = 212
    _globals['_REMOVESTREAMRESPONSE']._serialized_start = 214
    _globals['_REMOVESTREAMRESPONSE']._serialized_end = 236
    _globals['_STREAMSERVICE']._serialized_start = 239
    _globals['_STREAMSERVICE']._serialized_end = 521