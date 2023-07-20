"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n5proto/rpc/examples/echoresource/v1/echoresource.proto\x12"proto.rpc.examples.echoresource.v1"C\n\x13EchoResourceRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x18\n\x07message\x18\x02 \x01(\tR\x07message"0\n\x14EchoResourceResponse\x12\x18\n\x07message\x18\x01 \x01(\tR\x07message"K\n\x1bEchoResourceMultipleRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x18\n\x07message\x18\x02 \x01(\tR\x07message"8\n\x1cEchoResourceMultipleResponse\x12\x18\n\x07message\x18\x01 \x01(\tR\x07message"G\n\x17EchoResourceBiDiRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x18\n\x07message\x18\x02 \x01(\tR\x07message"4\n\x18EchoResourceBiDiResponse\x12\x18\n\x07message\x18\x01 \x01(\tR\x07message2\xd1\x03\n\x13EchoResourceService\x12\x83\x01\n\x0cEchoResource\x127.proto.rpc.examples.echoresource.v1.EchoResourceRequest\x1a8.proto.rpc.examples.echoresource.v1.EchoResourceResponse"\x00\x12\x9d\x01\n\x14EchoResourceMultiple\x12?.proto.rpc.examples.echoresource.v1.EchoResourceMultipleRequest\x1a@.proto.rpc.examples.echoresource.v1.EchoResourceMultipleResponse"\x000\x01\x12\x93\x01\n\x10EchoResourceBiDi\x12;.proto.rpc.examples.echoresource.v1.EchoResourceBiDiRequest\x1a<.proto.rpc.examples.echoresource.v1.EchoResourceBiDiResponse"\x00(\x010\x01B6Z4go.viam.com/utils/proto/rpc/examples/echoresource/v1b\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'proto.rpc.examples.echoresource.v1.echoresource_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z4go.viam.com/utils/proto/rpc/examples/echoresource/v1'
    _ECHORESOURCEREQUEST._serialized_start = 93
    _ECHORESOURCEREQUEST._serialized_end = 160
    _ECHORESOURCERESPONSE._serialized_start = 162
    _ECHORESOURCERESPONSE._serialized_end = 210
    _ECHORESOURCEMULTIPLEREQUEST._serialized_start = 212
    _ECHORESOURCEMULTIPLEREQUEST._serialized_end = 287
    _ECHORESOURCEMULTIPLERESPONSE._serialized_start = 289
    _ECHORESOURCEMULTIPLERESPONSE._serialized_end = 345
    _ECHORESOURCEBIDIREQUEST._serialized_start = 347
    _ECHORESOURCEBIDIREQUEST._serialized_end = 418
    _ECHORESOURCEBIDIRESPONSE._serialized_start = 420
    _ECHORESOURCEBIDIRESPONSE._serialized_end = 472
    _ECHORESOURCESERVICE._serialized_start = 475
    _ECHORESOURCESERVICE._serialized_end = 940