"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1eproto/rpc/webrtc/v1/grpc.proto\x12\x13proto.rpc.webrtc.v1\x1a\x1egoogle/protobuf/duration.proto\x1a\x17google/rpc/status.proto"5\n\rPacketMessage\x12\x12\n\x04data\x18\x01 \x01(\x0cR\x04data\x12\x10\n\x03eom\x18\x02 \x01(\x08R\x03eom"\x18\n\x06Stream\x12\x0e\n\x02id\x18\x01 \x01(\x04R\x02id"\xc8\x01\n\x07Request\x123\n\x06stream\x18\x01 \x01(\x0b2\x1b.proto.rpc.webrtc.v1.StreamR\x06stream\x12?\n\x07headers\x18\x02 \x01(\x0b2#.proto.rpc.webrtc.v1.RequestHeadersH\x00R\x07headers\x12?\n\x07message\x18\x03 \x01(\x0b2#.proto.rpc.webrtc.v1.RequestMessageH\x00R\x07messageB\x06\n\x04type"\x98\x01\n\x0eRequestHeaders\x12\x16\n\x06method\x18\x01 \x01(\tR\x06method\x129\n\x08metadata\x18\x02 \x01(\x0b2\x1d.proto.rpc.webrtc.v1.MetadataR\x08metadata\x123\n\x07timeout\x18\x03 \x01(\x0b2\x19.google.protobuf.DurationR\x07timeout"\x8e\x01\n\x0eRequestMessage\x12\x1f\n\x0bhas_message\x18\x01 \x01(\x08R\nhasMessage\x12I\n\x0epacket_message\x18\x02 \x01(\x0b2".proto.rpc.webrtc.v1.PacketMessageR\rpacketMessage\x12\x10\n\x03eos\x18\x03 \x01(\x08R\x03eos"\x90\x02\n\x08Response\x123\n\x06stream\x18\x01 \x01(\x0b2\x1b.proto.rpc.webrtc.v1.StreamR\x06stream\x12@\n\x07headers\x18\x02 \x01(\x0b2$.proto.rpc.webrtc.v1.ResponseHeadersH\x00R\x07headers\x12@\n\x07message\x18\x03 \x01(\x0b2$.proto.rpc.webrtc.v1.ResponseMessageH\x00R\x07message\x12C\n\x08trailers\x18\x04 \x01(\x0b2%.proto.rpc.webrtc.v1.ResponseTrailersH\x00R\x08trailersB\x06\n\x04type"L\n\x0fResponseHeaders\x129\n\x08metadata\x18\x01 \x01(\x0b2\x1d.proto.rpc.webrtc.v1.MetadataR\x08metadata"\\\n\x0fResponseMessage\x12I\n\x0epacket_message\x18\x01 \x01(\x0b2".proto.rpc.webrtc.v1.PacketMessageR\rpacketMessage"y\n\x10ResponseTrailers\x12*\n\x06status\x18\x01 \x01(\x0b2\x12.google.rpc.StatusR\x06status\x129\n\x08metadata\x18\x02 \x01(\x0b2\x1d.proto.rpc.webrtc.v1.MetadataR\x08metadata"!\n\x07Strings\x12\x16\n\x06values\x18\x01 \x03(\tR\x06values"\x96\x01\n\x08Metadata\x125\n\x02md\x18\x01 \x03(\x0b2%.proto.rpc.webrtc.v1.Metadata.MdEntryR\x02md\x1aS\n\x07MdEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x122\n\x05value\x18\x02 \x01(\x0b2\x1c.proto.rpc.webrtc.v1.StringsR\x05value:\x028\x01B\'Z%go.viam.com/utils/proto/rpc/webrtc/v1b\x06proto3')
_PACKETMESSAGE = DESCRIPTOR.message_types_by_name['PacketMessage']
_STREAM = DESCRIPTOR.message_types_by_name['Stream']
_REQUEST = DESCRIPTOR.message_types_by_name['Request']
_REQUESTHEADERS = DESCRIPTOR.message_types_by_name['RequestHeaders']
_REQUESTMESSAGE = DESCRIPTOR.message_types_by_name['RequestMessage']
_RESPONSE = DESCRIPTOR.message_types_by_name['Response']
_RESPONSEHEADERS = DESCRIPTOR.message_types_by_name['ResponseHeaders']
_RESPONSEMESSAGE = DESCRIPTOR.message_types_by_name['ResponseMessage']
_RESPONSETRAILERS = DESCRIPTOR.message_types_by_name['ResponseTrailers']
_STRINGS = DESCRIPTOR.message_types_by_name['Strings']
_METADATA = DESCRIPTOR.message_types_by_name['Metadata']
_METADATA_MDENTRY = _METADATA.nested_types_by_name['MdEntry']
PacketMessage = _reflection.GeneratedProtocolMessageType('PacketMessage', (_message.Message,), {'DESCRIPTOR': _PACKETMESSAGE, '__module__': 'proto.rpc.webrtc.v1.grpc_pb2', '__doc__': 'A PacketMessage is used to packetize large messages (> 64KiB) to be\n  able to safely transmit over WebRTC data channels.'})
_sym_db.RegisterMessage(PacketMessage)
Stream = _reflection.GeneratedProtocolMessageType('Stream', (_message.Message,), {'DESCRIPTOR': _STREAM, '__module__': 'proto.rpc.webrtc.v1.grpc_pb2', '__doc__': 'A Stream represents an instance of a gRPC stream between a client and\n  a server.'})
_sym_db.RegisterMessage(Stream)
Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), {'DESCRIPTOR': _REQUEST, '__module__': 'proto.rpc.webrtc.v1.grpc_pb2', '__doc__': 'A Request is a frame coming from a client. It is always associated\n  with a stream where the client assigns the stream identifier. Servers\n  will drop frames where the stream identifier has no association (if a\n  non-header frames are sent).'})
_sym_db.RegisterMessage(Request)
RequestHeaders = _reflection.GeneratedProtocolMessageType('RequestHeaders', (_message.Message,), {'DESCRIPTOR': _REQUESTHEADERS, '__module__': 'proto.rpc.webrtc.v1.grpc_pb2', '__doc__': 'RequestHeaders describe the unary or streaming call to make.'})
_sym_db.RegisterMessage(RequestHeaders)
RequestMessage = _reflection.GeneratedProtocolMessageType('RequestMessage', (_message.Message,), {'DESCRIPTOR': _REQUESTMESSAGE, '__module__': 'proto.rpc.webrtc.v1.grpc_pb2', '__doc__': 'A RequestMessage contains individual gRPC messages and a potential\n  end-of-stream (EOS) marker.'})
_sym_db.RegisterMessage(RequestMessage)
Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), {'DESCRIPTOR': _RESPONSE, '__module__': 'proto.rpc.webrtc.v1.grpc_pb2', '__doc__': 'A Response is a frame coming from a server. It is always associated\n  with a stream where the client assigns the stream identifier. Clients\n  will drop frames where the stream identifier has no association.'})
_sym_db.RegisterMessage(Response)
ResponseHeaders = _reflection.GeneratedProtocolMessageType('ResponseHeaders', (_message.Message,), {'DESCRIPTOR': _RESPONSEHEADERS, '__module__': 'proto.rpc.webrtc.v1.grpc_pb2', '__doc__': 'ResponseHeaders contain custom metadata that are sent to the client\n  before any message or trailers (unless only trailers are sent).'})
_sym_db.RegisterMessage(ResponseHeaders)
ResponseMessage = _reflection.GeneratedProtocolMessageType('ResponseMessage', (_message.Message,), {'DESCRIPTOR': _RESPONSEMESSAGE, '__module__': 'proto.rpc.webrtc.v1.grpc_pb2', '__doc__': 'ResponseMessage contains the data of a response to a call.'})
_sym_db.RegisterMessage(ResponseMessage)
ResponseTrailers = _reflection.GeneratedProtocolMessageType('ResponseTrailers', (_message.Message,), {'DESCRIPTOR': _RESPONSETRAILERS, '__module__': 'proto.rpc.webrtc.v1.grpc_pb2', '__doc__': 'ResponseTrailers contain the status of a response and any custom\n  metadata.'})
_sym_db.RegisterMessage(ResponseTrailers)
Strings = _reflection.GeneratedProtocolMessageType('Strings', (_message.Message,), {'DESCRIPTOR': _STRINGS, '__module__': 'proto.rpc.webrtc.v1.grpc_pb2', '__doc__': 'Strings are a series of values.'})
_sym_db.RegisterMessage(Strings)
Metadata = _reflection.GeneratedProtocolMessageType('Metadata', (_message.Message,), {'MdEntry': _reflection.GeneratedProtocolMessageType('MdEntry', (_message.Message,), {'DESCRIPTOR': _METADATA_MDENTRY, '__module__': 'proto.rpc.webrtc.v1.grpc_pb2'}), 'DESCRIPTOR': _METADATA, '__module__': 'proto.rpc.webrtc.v1.grpc_pb2', '__doc__': 'Metadata is for custom key values provided by a client or server\n  during a stream.'})
_sym_db.RegisterMessage(Metadata)
_sym_db.RegisterMessage(Metadata.MdEntry)
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
    _REQUEST._serialized_end = 394
    _REQUESTHEADERS._serialized_start = 397
    _REQUESTHEADERS._serialized_end = 549
    _REQUESTMESSAGE._serialized_start = 552
    _REQUESTMESSAGE._serialized_end = 694
    _RESPONSE._serialized_start = 697
    _RESPONSE._serialized_end = 969
    _RESPONSEHEADERS._serialized_start = 971
    _RESPONSEHEADERS._serialized_end = 1047
    _RESPONSEMESSAGE._serialized_start = 1049
    _RESPONSEMESSAGE._serialized_end = 1141
    _RESPONSETRAILERS._serialized_start = 1143
    _RESPONSETRAILERS._serialized_end = 1264
    _STRINGS._serialized_start = 1266
    _STRINGS._serialized_end = 1299
    _METADATA._serialized_start = 1302
    _METADATA._serialized_end = 1452
    _METADATA_MDENTRY._serialized_start = 1369
    _METADATA_MDENTRY._serialized_end = 1452