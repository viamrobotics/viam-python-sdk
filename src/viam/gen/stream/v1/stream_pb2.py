"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16stream/v1/stream.proto\x12\x0fproto.stream.v1"\x14\n\x12ListStreamsRequest"+\n\x13ListStreamsResponse\x12\x14\n\x05names\x18\x01 \x03(\tR\x05names"&\n\x10AddStreamRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name"\x13\n\x11AddStreamResponse")\n\x13RemoveStreamRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name"\x16\n\x14RemoveStreamResponse":\n\nResolution\x12\x14\n\x05width\x18\x01 \x01(\x05R\x05width\x12\x16\n\x06height\x18\x02 \x01(\x05R\x06height"-\n\x17GetStreamOptionsRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name"Y\n\x18GetStreamOptionsResponse\x12=\n\x0bresolutions\x18\x01 \x03(\x0b2\x1b.proto.stream.v1.ResolutionR\x0bresolutions"j\n\x17SetStreamOptionsRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12;\n\nresolution\x18\x02 \x01(\x0b2\x1b.proto.stream.v1.ResolutionR\nresolution"\x1a\n\x18SetStreamOptionsResponse2\xec\x03\n\rStreamService\x12X\n\x0bListStreams\x12#.proto.stream.v1.ListStreamsRequest\x1a$.proto.stream.v1.ListStreamsResponse\x12R\n\tAddStream\x12!.proto.stream.v1.AddStreamRequest\x1a".proto.stream.v1.AddStreamResponse\x12g\n\x10GetStreamOptions\x12(.proto.stream.v1.GetStreamOptionsRequest\x1a).proto.stream.v1.GetStreamOptionsResponse\x12g\n\x10SetStreamOptions\x12(.proto.stream.v1.SetStreamOptionsRequest\x1a).proto.stream.v1.SetStreamOptionsResponse\x12[\n\x0cRemoveStream\x12$.proto.stream.v1.RemoveStreamRequest\x1a%.proto.stream.v1.RemoveStreamResponseB.Z,github.com/edaniels/gostream/proto/stream/v1b\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'stream.v1.stream_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z,github.com/edaniels/gostream/proto/stream/v1'
    _LISTSTREAMSREQUEST._serialized_start = 43
    _LISTSTREAMSREQUEST._serialized_end = 63
    _LISTSTREAMSRESPONSE._serialized_start = 65
    _LISTSTREAMSRESPONSE._serialized_end = 108
    _ADDSTREAMREQUEST._serialized_start = 110
    _ADDSTREAMREQUEST._serialized_end = 148
    _ADDSTREAMRESPONSE._serialized_start = 150
    _ADDSTREAMRESPONSE._serialized_end = 169
    _REMOVESTREAMREQUEST._serialized_start = 171
    _REMOVESTREAMREQUEST._serialized_end = 212
    _REMOVESTREAMRESPONSE._serialized_start = 214
    _REMOVESTREAMRESPONSE._serialized_end = 236
    _RESOLUTION._serialized_start = 238
    _RESOLUTION._serialized_end = 296
    _GETSTREAMOPTIONSREQUEST._serialized_start = 298
    _GETSTREAMOPTIONSREQUEST._serialized_end = 343
    _GETSTREAMOPTIONSRESPONSE._serialized_start = 345
    _GETSTREAMOPTIONSRESPONSE._serialized_end = 434
    _SETSTREAMOPTIONSREQUEST._serialized_start = 436
    _SETSTREAMOPTIONSREQUEST._serialized_end = 542
    _SETSTREAMOPTIONSRESPONSE._serialized_start = 544
    _SETSTREAMOPTIONSRESPONSE._serialized_end = 570
    _STREAMSERVICE._serialized_start = 573
    _STREAMSERVICE._serialized_end = 1065