"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....common.v1 import common_pb2 as common_dot_v1_dot_common__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$component/testecho/v1/testecho.proto\x12\x1aviam.component.testecho.v1\x1a\x16common/v1/common.proto";\n\x0bEchoRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x18\n\x07message\x18\x02 \x01(\tR\x07message"(\n\x0cEchoResponse\x12\x18\n\x07message\x18\x01 \x01(\tR\x07message"C\n\x13EchoMultipleRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x18\n\x07message\x18\x02 \x01(\tR\x07message"0\n\x14EchoMultipleResponse\x12\x18\n\x07message\x18\x01 \x01(\tR\x07message"?\n\x0fEchoBiDiRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x18\n\x07message\x18\x02 \x01(\tR\x07message",\n\x10EchoBiDiResponse\x12\x18\n\x07message\x18\x01 \x01(\tR\x07message"!\n\x0bStopRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name"\x0e\n\x0cStopResponse2\xb3\x03\n\x0fTestEchoService\x12[\n\x04Echo\x12\'.viam.component.testecho.v1.EchoRequest\x1a(.viam.component.testecho.v1.EchoResponse"\x00\x12y\n\x0cEchoMultiple\x12/.viam.component.testecho.v1.EchoMultipleRequest\x1a0.viam.component.testecho.v1.EchoMultipleResponse"\x04\xa0\x92)\x010\x01\x12k\n\x08EchoBiDi\x12+.viam.component.testecho.v1.EchoBiDiRequest\x1a,.viam.component.testecho.v1.EchoBiDiResponse"\x00(\x010\x01\x12[\n\x04Stop\x12\'.viam.component.testecho.v1.StopRequest\x1a(.viam.component.testecho.v1.StopResponse"\x00BG\n\x1ecom.viam.component.testecho.v1Z%go.viam.com/api/component/testecho/v1b\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'component.testecho.v1.testecho_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n\x1ecom.viam.component.testecho.v1Z%go.viam.com/api/component/testecho/v1'
    _TESTECHOSERVICE.methods_by_name['EchoMultiple']._options = None
    _TESTECHOSERVICE.methods_by_name['EchoMultiple']._serialized_options = b'\xa0\x92)\x01'
    _ECHOREQUEST._serialized_start = 92
    _ECHOREQUEST._serialized_end = 151
    _ECHORESPONSE._serialized_start = 153
    _ECHORESPONSE._serialized_end = 193
    _ECHOMULTIPLEREQUEST._serialized_start = 195
    _ECHOMULTIPLEREQUEST._serialized_end = 262
    _ECHOMULTIPLERESPONSE._serialized_start = 264
    _ECHOMULTIPLERESPONSE._serialized_end = 312
    _ECHOBIDIREQUEST._serialized_start = 314
    _ECHOBIDIREQUEST._serialized_end = 377
    _ECHOBIDIRESPONSE._serialized_start = 379
    _ECHOBIDIRESPONSE._serialized_end = 423
    _STOPREQUEST._serialized_start = 425
    _STOPREQUEST._serialized_end = 458
    _STOPRESPONSE._serialized_start = 460
    _STOPRESPONSE._serialized_end = 474
    _TESTECHOSERVICE._serialized_start = 477
    _TESTECHOSERVICE._serialized_end = 912