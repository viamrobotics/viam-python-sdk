"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1eproto/rpc/webrtc/v1/grpc.proto\x12\x13proto.rpc.webrtc.v1\x1a\x1egoogle/protobuf/duration.proto\x1a\x17google/rpc/status.proto"5\n\rPacketMessage\x12\x12\n\x04data\x18\x01 \x01(\x0cR\x04data\x12\x10\n\x03eom\x18\x02 \x01(\x08R\x03eom"\x18\n\x06Stream\x12\x0e\n\x02id\x18\x01 \x01(\x04R\x02id"\xe9\x01\n\x07Request\x123\n\x06stream\x18\x01 \x01(\x0b2\x1b.proto.rpc.webrtc.v1.StreamR\x06stream\x12?\n\x07headers\x18\x02 \x01(\x0b2#.proto.rpc.webrtc.v1.RequestHeadersH\x00R\x07headers\x12?\n\x07message\x18\x03 \x01(\x0b2#.proto.rpc.webrtc.v1.RequestMessageH\x00R\x07message\x12\x1f\n\nrst_stream\x18\x04 \x01(\x08H\x00R\trstStreamB\x06\n\x04type"\x98\x01\n\x0eRequestHeaders\x12\x16\n\x06method\x18\x01 \x01(\tR\x06method\x129\n\x08metadata\x18\x02 \x01(\x0b2\x1d.proto.rpc.webrtc.v1.MetadataR\x08metadata\x123\n\x07timeout\x18\x03 \x01(\x0b2\x19.google.protobuf.DurationR\x07timeout"\x8e\x01\n\x0eRequestMessage\x12\x1f\n\x0bhas_message\x18\x01 \x01(\x08R\nhasMessage\x12I\n\x0epacket_message\x18\x02 \x01(\x0b2".proto.rpc.webrtc.v1.PacketMessageR\rpacketMessage\x12\x10\n\x03eos\x18\x03 \x01(\x08R\x03eos"\x90\x02\n\x08Response\x123\n\x06stream\x18\x01 \x01(\x0b2\x1b.proto.rpc.webrtc.v1.StreamR\x06stream\x12@\n\x07headers\x18\x02 \x01(\x0b2$.proto.rpc.webrtc.v1.ResponseHeadersH\x00R\x07headers\x12@\n\x07message\x18\x03 \x01(\x0b2$.proto.rpc.webrtc.v1.ResponseMessageH\x00R\x07message\x12C\n\x08trailers\x18\x04 \x01(\x0b2%.proto.rpc.webrtc.v1.ResponseTrailersH\x00R\x08trailersB\x06\n\x04type"L\n\x0fResponseHeaders\x129\n\x08metadata\x18\x01 \x01(\x0b2\x1d.proto.rpc.webrtc.v1.MetadataR\x08metadata"\\\n\x0fResponseMessage\x12I\n\x0epacket_message\x18\x01 \x01(\x0b2".proto.rpc.webrtc.v1.PacketMessageR\rpacketMessage"y\n\x10ResponseTrailers\x12*\n\x06status\x18\x01 \x01(\x0b2\x12.google.rpc.StatusR\x06status\x129\n\x08metadata\x18\x02 \x01(\x0b2\x1d.proto.rpc.webrtc.v1.MetadataR\x08metadata"!\n\x07Strings\x12\x16\n\x06values\x18\x01 \x03(\tR\x06values"\x96\x01\n\x08Metadata\x125\n\x02md\x18\x01 \x03(\x0b2%.proto.rpc.webrtc.v1.Metadata.MdEntryR\x02md\x1aS\n\x07MdEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x122\n\x05value\x18\x02 \x01(\x0b2\x1c.proto.rpc.webrtc.v1.StringsR\x05value:\x028\x01B\'Z%go.viam.com/utils/proto/rpc/webrtc/v1b\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'proto.rpc.webrtc.v1.grpc_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z%go.viam.com/utils/proto/rpc/webrtc/v1'
    _METADATA_MDENTRY._options = None
    _METADATA_MDENTRY._serialized_options = b'8\x01'
    _PACKETMESSAGE._serialized_start = 112
    _PACKETMESSAGE._serialized_end = 165
    _STREAM._serialized_start = 167
    _STREAM._serialized_end = 191
    _REQUEST._serialized_start = 194
    _REQUEST._serialized_end = 427
    _REQUESTHEADERS._serialized_start = 430
    _REQUESTHEADERS._serialized_end = 582
    _REQUESTMESSAGE._serialized_start = 585
    _REQUESTMESSAGE._serialized_end = 727
    _RESPONSE._serialized_start = 730
    _RESPONSE._serialized_end = 1002
    _RESPONSEHEADERS._serialized_start = 1004
    _RESPONSEHEADERS._serialized_end = 1080
    _RESPONSEMESSAGE._serialized_start = 1082
    _RESPONSEMESSAGE._serialized_end = 1174
    _RESPONSETRAILERS._serialized_start = 1176
    _RESPONSETRAILERS._serialized_end = 1297
    _STRINGS._serialized_start = 1299
    _STRINGS._serialized_end = 1332
    _METADATA._serialized_start = 1335
    _METADATA._serialized_end = 1485
    _METADATA_MDENTRY._serialized_start = 1402
    _METADATA_MDENTRY._serialized_end = 1485