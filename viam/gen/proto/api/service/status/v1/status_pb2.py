"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......proto.api.common.v1 import common_pb2 as proto_dot_api_dot_common_dot_v1_dot_common__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(proto/api/service/status/v1/status.proto\x12\x1bproto.api.service.status.v1\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1cgoogle/api/annotations.proto\x1a proto/api/common/v1/common.proto"p\n\x06Status\x125\n\x04name\x18\x01 \x01(\x0b2!.proto.api.common.v1.ResourceNameR\x04name\x12/\n\x06status\x18\x02 \x01(\x0b2\x17.google.protobuf.StructR\x06status"\\\n\x10GetStatusRequest\x12H\n\x0eresource_names\x18\x01 \x03(\x0b2!.proto.api.common.v1.ResourceNameR\rresourceNames"P\n\x11GetStatusResponse\x12;\n\x06status\x18\x01 \x03(\x0b2#.proto.api.service.status.v1.StatusR\x06status"\x90\x01\n\x13StreamStatusRequest\x12H\n\x0eresource_names\x18\x01 \x03(\x0b2!.proto.api.common.v1.ResourceNameR\rresourceNames\x12/\n\x05every\x18\x02 \x01(\x0b2\x19.google.protobuf.DurationR\x05every"S\n\x14StreamStatusResponse\x12;\n\x06status\x18\x01 \x03(\x0b2#.proto.api.service.status.v1.StatusR\x06status2\xc5\x02\n\rStatusService\x12\x8f\x01\n\tGetStatus\x12-.proto.api.service.status.v1.GetStatusRequest\x1a..proto.api.service.status.v1.GetStatusResponse"#\x82\xd3\xe4\x93\x02\x1d\x12\x1b/viam/api/v1/service/status\x12\xa1\x01\n\x0cStreamStatus\x120.proto.api.service.status.v1.StreamStatusRequest\x1a1.proto.api.service.status.v1.StreamStatusResponse"*\x82\xd3\xe4\x93\x02$\x12"/viam/api/v1/service/status/stream0\x01BW\n(com.viam.rdk.proto.api.service.status.v1Z+go.viam.com/rdk/proto/api/service/status/v1b\x06proto3')
_STATUS = DESCRIPTOR.message_types_by_name['Status']
_GETSTATUSREQUEST = DESCRIPTOR.message_types_by_name['GetStatusRequest']
_GETSTATUSRESPONSE = DESCRIPTOR.message_types_by_name['GetStatusResponse']
_STREAMSTATUSREQUEST = DESCRIPTOR.message_types_by_name['StreamStatusRequest']
_STREAMSTATUSRESPONSE = DESCRIPTOR.message_types_by_name['StreamStatusResponse']
Status = _reflection.GeneratedProtocolMessageType('Status', (_message.Message,), {'DESCRIPTOR': _STATUS, '__module__': 'proto.api.service.status.v1.status_pb2'})
_sym_db.RegisterMessage(Status)
GetStatusRequest = _reflection.GeneratedProtocolMessageType('GetStatusRequest', (_message.Message,), {'DESCRIPTOR': _GETSTATUSREQUEST, '__module__': 'proto.api.service.status.v1.status_pb2'})
_sym_db.RegisterMessage(GetStatusRequest)
GetStatusResponse = _reflection.GeneratedProtocolMessageType('GetStatusResponse', (_message.Message,), {'DESCRIPTOR': _GETSTATUSRESPONSE, '__module__': 'proto.api.service.status.v1.status_pb2'})
_sym_db.RegisterMessage(GetStatusResponse)
StreamStatusRequest = _reflection.GeneratedProtocolMessageType('StreamStatusRequest', (_message.Message,), {'DESCRIPTOR': _STREAMSTATUSREQUEST, '__module__': 'proto.api.service.status.v1.status_pb2', '__doc__': 'Attributes:\n      every:\n          how often to send a new status.\n  '})
_sym_db.RegisterMessage(StreamStatusRequest)
StreamStatusResponse = _reflection.GeneratedProtocolMessageType('StreamStatusResponse', (_message.Message,), {'DESCRIPTOR': _STREAMSTATUSRESPONSE, '__module__': 'proto.api.service.status.v1.status_pb2'})
_sym_db.RegisterMessage(StreamStatusResponse)
_STATUSSERVICE = DESCRIPTOR.services_by_name['StatusService']
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n(com.viam.rdk.proto.api.service.status.v1Z+go.viam.com/rdk/proto/api/service/status/v1'
    _STATUSSERVICE.methods_by_name['GetStatus']._options = None
    _STATUSSERVICE.methods_by_name['GetStatus']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1d\x12\x1b/viam/api/v1/service/status'
    _STATUSSERVICE.methods_by_name['StreamStatus']._options = None
    _STATUSSERVICE.methods_by_name['StreamStatus']._serialized_options = b'\x82\xd3\xe4\x93\x02$\x12"/viam/api/v1/service/status/stream'
    _STATUS._serialized_start = 199
    _STATUS._serialized_end = 311
    _GETSTATUSREQUEST._serialized_start = 313
    _GETSTATUSREQUEST._serialized_end = 405
    _GETSTATUSRESPONSE._serialized_start = 407
    _GETSTATUSRESPONSE._serialized_end = 487
    _STREAMSTATUSREQUEST._serialized_start = 490
    _STREAMSTATUSREQUEST._serialized_end = 634
    _STREAMSTATUSRESPONSE._serialized_start = 636
    _STREAMSTATUSRESPONSE._serialized_end = 719
    _STATUSSERVICE._serialized_start = 722
    _STATUSSERVICE._serialized_end = 1047