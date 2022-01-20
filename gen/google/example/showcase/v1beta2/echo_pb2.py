# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/example/showcase/v1beta2/echo.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import client_pb2 as google_dot_api_dot_client__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*google/example/showcase/v1beta2/echo.proto\x12\x1fgoogle.example.showcase.v1beta2\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a#google/longrunning/operations.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x17google/rpc/status.proto\"\xa8\x01\n\x0b\x45\x63hoRequest\x12\x1a\n\x07\x63ontent\x18\x01 \x01(\tH\x00R\x07\x63ontent\x12*\n\x05\x65rror\x18\x02 \x01(\x0b\x32\x12.google.rpc.StatusH\x00R\x05\x65rror\x12\x45\n\x08severity\x18\x03 \x01(\x0e\x32).google.example.showcase.v1beta2.SeverityR\x08severityB\n\n\x08response\"o\n\x0c\x45\x63hoResponse\x12\x18\n\x07\x63ontent\x18\x01 \x01(\tR\x07\x63ontent\x12\x45\n\x08severity\x18\x02 \x01(\x0e\x32).google.example.showcase.v1beta2.SeverityR\x08severity\"S\n\rExpandRequest\x12\x18\n\x07\x63ontent\x18\x01 \x01(\tR\x07\x63ontent\x12(\n\x05\x65rror\x18\x02 \x01(\x0b\x32\x12.google.rpc.StatusR\x05\x65rror\"p\n\x12PagedExpandRequest\x12\x1e\n\x07\x63ontent\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02R\x07\x63ontent\x12\x1b\n\tpage_size\x18\x02 \x01(\x05R\x08pageSize\x12\x1d\n\npage_token\x18\x03 \x01(\tR\tpageToken\"\x8a\x01\n\x13PagedExpandResponse\x12K\n\tresponses\x18\x01 \x03(\x0b\x32-.google.example.showcase.v1beta2.EchoResponseR\tresponses\x12&\n\x0fnext_page_token\x18\x02 \x01(\tR\rnextPageToken\"\xff\x01\n\x0bWaitRequest\x12\x37\n\x08\x65nd_time\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.TimestampH\x00R\x07\x65ndTime\x12-\n\x03ttl\x18\x04 \x01(\x0b\x32\x19.google.protobuf.DurationH\x00R\x03ttl\x12*\n\x05\x65rror\x18\x02 \x01(\x0b\x32\x12.google.rpc.StatusH\x01R\x05\x65rror\x12I\n\x07success\x18\x03 \x01(\x0b\x32-.google.example.showcase.v1beta2.WaitResponseH\x01R\x07successB\x05\n\x03\x65ndB\n\n\x08response\"(\n\x0cWaitResponse\x12\x18\n\x07\x63ontent\x18\x01 \x01(\tR\x07\x63ontent\"\xd4\x01\n\x0c\x42lockRequest\x12@\n\x0eresponse_delay\x18\x01 \x01(\x0b\x32\x19.google.protobuf.DurationR\rresponseDelay\x12*\n\x05\x65rror\x18\x02 \x01(\x0b\x32\x12.google.rpc.StatusH\x00R\x05\x65rror\x12J\n\x07success\x18\x03 \x01(\x0b\x32..google.example.showcase.v1beta2.BlockResponseH\x00R\x07successB\n\n\x08response\")\n\rBlockResponse\x12\x18\n\x07\x63ontent\x18\x01 \x01(\tR\x07\x63ontent*D\n\x08Severity\x12\x0f\n\x0bUNNECESSARY\x10\x00\x12\r\n\tNECESSARY\x10\x01\x12\n\n\x06URGENT\x10\x02\x12\x0c\n\x08\x43RITICAL\x10\x03\x32\xfa\x07\n\x04\x45\x63ho\x12\x82\x01\n\x04\x45\x63ho\x12,.google.example.showcase.v1beta2.EchoRequest\x1a-.google.example.showcase.v1beta2.EchoResponse\"\x1d\x82\xd3\xe4\x93\x02\x17\"\x12/v1beta2/echo:echo:\x01*\x12\x9a\x01\n\x06\x45xpand\x12..google.example.showcase.v1beta2.ExpandRequest\x1a-.google.example.showcase.v1beta2.EchoResponse\"/\xda\x41\rcontent,error\x82\xd3\xe4\x93\x02\x19\"\x14/v1beta2/echo:expand:\x01*0\x01\x12\x8a\x01\n\x07\x43ollect\x12,.google.example.showcase.v1beta2.EchoRequest\x1a-.google.example.showcase.v1beta2.EchoResponse\" \x82\xd3\xe4\x93\x02\x1a\"\x15/v1beta2/echo:collect:\x01*(\x01\x12i\n\x04\x43hat\x12,.google.example.showcase.v1beta2.EchoRequest\x1a-.google.example.showcase.v1beta2.EchoResponse\"\x00(\x01\x30\x01\x12\x9e\x01\n\x0bPagedExpand\x12\x33.google.example.showcase.v1beta2.PagedExpandRequest\x1a\x34.google.example.showcase.v1beta2.PagedExpandResponse\"$\x82\xd3\xe4\x93\x02\x1e\"\x19/v1beta2/echo:pagedExpand:\x01*\x12\x91\x01\n\x04Wait\x12,.google.example.showcase.v1beta2.WaitRequest\x1a\x1d.google.longrunning.Operation\"<\xca\x41\x1c\n\x0cWaitResponse\x12\x0cWaitMetadata\x82\xd3\xe4\x93\x02\x17\"\x12/v1beta2/echo:wait:\x01*\x12\x86\x01\n\x05\x42lock\x12-.google.example.showcase.v1beta2.BlockRequest\x1a..google.example.showcase.v1beta2.BlockResponse\"\x1e\x82\xd3\xe4\x93\x02\x18\"\x13/v1beta2/echo:block:\x01*\x1a\x1a\xca\x41\x17showcase.googleapis.comB\x8e\x01\n#com.google.example.showcase.v1beta2B\tEchoProtoP\x01Z4github.com/googleapis/gapic-showcase/server/genproto\xea\x02#Google::Example::Showcase::V1bBeta2b\x06proto3')

_SEVERITY = DESCRIPTOR.enum_types_by_name['Severity']
Severity = enum_type_wrapper.EnumTypeWrapper(_SEVERITY)
UNNECESSARY = 0
NECESSARY = 1
URGENT = 2
CRITICAL = 3


_ECHOREQUEST = DESCRIPTOR.message_types_by_name['EchoRequest']
_ECHORESPONSE = DESCRIPTOR.message_types_by_name['EchoResponse']
_EXPANDREQUEST = DESCRIPTOR.message_types_by_name['ExpandRequest']
_PAGEDEXPANDREQUEST = DESCRIPTOR.message_types_by_name['PagedExpandRequest']
_PAGEDEXPANDRESPONSE = DESCRIPTOR.message_types_by_name['PagedExpandResponse']
_WAITREQUEST = DESCRIPTOR.message_types_by_name['WaitRequest']
_WAITRESPONSE = DESCRIPTOR.message_types_by_name['WaitResponse']
_BLOCKREQUEST = DESCRIPTOR.message_types_by_name['BlockRequest']
_BLOCKRESPONSE = DESCRIPTOR.message_types_by_name['BlockResponse']
EchoRequest = _reflection.GeneratedProtocolMessageType('EchoRequest', (_message.Message,), {
  'DESCRIPTOR' : _ECHOREQUEST,
  '__module__' : 'google.example.showcase.v1beta2.echo_pb2'
  # @@protoc_insertion_point(class_scope:google.example.showcase.v1beta2.EchoRequest)
  })
_sym_db.RegisterMessage(EchoRequest)

EchoResponse = _reflection.GeneratedProtocolMessageType('EchoResponse', (_message.Message,), {
  'DESCRIPTOR' : _ECHORESPONSE,
  '__module__' : 'google.example.showcase.v1beta2.echo_pb2'
  # @@protoc_insertion_point(class_scope:google.example.showcase.v1beta2.EchoResponse)
  })
_sym_db.RegisterMessage(EchoResponse)

ExpandRequest = _reflection.GeneratedProtocolMessageType('ExpandRequest', (_message.Message,), {
  'DESCRIPTOR' : _EXPANDREQUEST,
  '__module__' : 'google.example.showcase.v1beta2.echo_pb2'
  # @@protoc_insertion_point(class_scope:google.example.showcase.v1beta2.ExpandRequest)
  })
_sym_db.RegisterMessage(ExpandRequest)

PagedExpandRequest = _reflection.GeneratedProtocolMessageType('PagedExpandRequest', (_message.Message,), {
  'DESCRIPTOR' : _PAGEDEXPANDREQUEST,
  '__module__' : 'google.example.showcase.v1beta2.echo_pb2'
  # @@protoc_insertion_point(class_scope:google.example.showcase.v1beta2.PagedExpandRequest)
  })
_sym_db.RegisterMessage(PagedExpandRequest)

PagedExpandResponse = _reflection.GeneratedProtocolMessageType('PagedExpandResponse', (_message.Message,), {
  'DESCRIPTOR' : _PAGEDEXPANDRESPONSE,
  '__module__' : 'google.example.showcase.v1beta2.echo_pb2'
  # @@protoc_insertion_point(class_scope:google.example.showcase.v1beta2.PagedExpandResponse)
  })
_sym_db.RegisterMessage(PagedExpandResponse)

WaitRequest = _reflection.GeneratedProtocolMessageType('WaitRequest', (_message.Message,), {
  'DESCRIPTOR' : _WAITREQUEST,
  '__module__' : 'google.example.showcase.v1beta2.echo_pb2'
  # @@protoc_insertion_point(class_scope:google.example.showcase.v1beta2.WaitRequest)
  })
_sym_db.RegisterMessage(WaitRequest)

WaitResponse = _reflection.GeneratedProtocolMessageType('WaitResponse', (_message.Message,), {
  'DESCRIPTOR' : _WAITRESPONSE,
  '__module__' : 'google.example.showcase.v1beta2.echo_pb2'
  # @@protoc_insertion_point(class_scope:google.example.showcase.v1beta2.WaitResponse)
  })
_sym_db.RegisterMessage(WaitResponse)

BlockRequest = _reflection.GeneratedProtocolMessageType('BlockRequest', (_message.Message,), {
  'DESCRIPTOR' : _BLOCKREQUEST,
  '__module__' : 'google.example.showcase.v1beta2.echo_pb2'
  # @@protoc_insertion_point(class_scope:google.example.showcase.v1beta2.BlockRequest)
  })
_sym_db.RegisterMessage(BlockRequest)

BlockResponse = _reflection.GeneratedProtocolMessageType('BlockResponse', (_message.Message,), {
  'DESCRIPTOR' : _BLOCKRESPONSE,
  '__module__' : 'google.example.showcase.v1beta2.echo_pb2'
  # @@protoc_insertion_point(class_scope:google.example.showcase.v1beta2.BlockResponse)
  })
_sym_db.RegisterMessage(BlockResponse)

_ECHO = DESCRIPTOR.services_by_name['Echo']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n#com.google.example.showcase.v1beta2B\tEchoProtoP\001Z4github.com/googleapis/gapic-showcase/server/genproto\352\002#Google::Example::Showcase::V1bBeta2'
  _PAGEDEXPANDREQUEST.fields_by_name['content']._options = None
  _PAGEDEXPANDREQUEST.fields_by_name['content']._serialized_options = b'\342A\001\002'
  _ECHO._options = None
  _ECHO._serialized_options = b'\312A\027showcase.googleapis.com'
  _ECHO.methods_by_name['Echo']._options = None
  _ECHO.methods_by_name['Echo']._serialized_options = b'\202\323\344\223\002\027\"\022/v1beta2/echo:echo:\001*'
  _ECHO.methods_by_name['Expand']._options = None
  _ECHO.methods_by_name['Expand']._serialized_options = b'\332A\rcontent,error\202\323\344\223\002\031\"\024/v1beta2/echo:expand:\001*'
  _ECHO.methods_by_name['Collect']._options = None
  _ECHO.methods_by_name['Collect']._serialized_options = b'\202\323\344\223\002\032\"\025/v1beta2/echo:collect:\001*'
  _ECHO.methods_by_name['PagedExpand']._options = None
  _ECHO.methods_by_name['PagedExpand']._serialized_options = b'\202\323\344\223\002\036\"\031/v1beta2/echo:pagedExpand:\001*'
  _ECHO.methods_by_name['Wait']._options = None
  _ECHO.methods_by_name['Wait']._serialized_options = b'\312A\034\n\014WaitResponse\022\014WaitMetadata\202\323\344\223\002\027\"\022/v1beta2/echo:wait:\001*'
  _ECHO.methods_by_name['Block']._options = None
  _ECHO.methods_by_name['Block']._serialized_options = b'\202\323\344\223\002\030\"\023/v1beta2/echo:block:\001*'
  _SEVERITY._serialized_start=1476
  _SEVERITY._serialized_end=1544
  _ECHOREQUEST._serialized_start=295
  _ECHOREQUEST._serialized_end=463
  _ECHORESPONSE._serialized_start=465
  _ECHORESPONSE._serialized_end=576
  _EXPANDREQUEST._serialized_start=578
  _EXPANDREQUEST._serialized_end=661
  _PAGEDEXPANDREQUEST._serialized_start=663
  _PAGEDEXPANDREQUEST._serialized_end=775
  _PAGEDEXPANDRESPONSE._serialized_start=778
  _PAGEDEXPANDRESPONSE._serialized_end=916
  _WAITREQUEST._serialized_start=919
  _WAITREQUEST._serialized_end=1174
  _WAITRESPONSE._serialized_start=1176
  _WAITRESPONSE._serialized_end=1216
  _BLOCKREQUEST._serialized_start=1219
  _BLOCKREQUEST._serialized_end=1431
  _BLOCKRESPONSE._serialized_start=1433
  _BLOCKRESPONSE._serialized_end=1474
  _ECHO._serialized_start=1547
  _ECHO._serialized_end=2565
# @@protoc_insertion_point(module_scope)
