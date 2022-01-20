# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/example/showcase/v1beta1/sequence.proto
"""Generated protocol buffer code."""
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
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.google/example/showcase/v1beta1/sequence.proto\x12\x1fgoogle.example.showcase.v1beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x17google/rpc/status.proto\"\x9c\x02\n\x08Sequence\x12\x18\n\x04name\x18\x01 \x01(\tB\x04\xe2\x41\x01\x03R\x04name\x12P\n\tresponses\x18\x02 \x03(\x0b\x32\x32.google.example.showcase.v1beta1.Sequence.ResponseR\tresponses\x1ag\n\x08Response\x12*\n\x06status\x18\x01 \x01(\x0b\x32\x12.google.rpc.StatusR\x06status\x12/\n\x05\x64\x65lay\x18\x02 \x01(\x0b\x32\x19.google.protobuf.DurationR\x05\x64\x65lay:;\xea\x41\x38\n showcase.googleapis.com/Sequence\x12\x14sequences/{sequence}\"\xf8\x03\n\x0eSequenceReport\x12\x18\n\x04name\x18\x01 \x01(\tB\x04\xe2\x41\x01\x03R\x04name\x12S\n\x08\x61ttempts\x18\x02 \x03(\x0b\x32\x37.google.example.showcase.v1beta1.SequenceReport.AttemptR\x08\x61ttempts\x1a\xa4\x02\n\x07\x41ttempt\x12%\n\x0e\x61ttempt_number\x18\x01 \x01(\x05R\rattemptNumber\x12\x45\n\x10\x61ttempt_deadline\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x0f\x61ttemptDeadline\x12?\n\rresponse_time\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x0cresponseTime\x12>\n\rattempt_delay\x18\x04 \x01(\x0b\x32\x19.google.protobuf.DurationR\x0c\x61ttemptDelay\x12*\n\x06status\x18\x05 \x01(\x0b\x32\x12.google.rpc.StatusR\x06status:P\xea\x41M\n&showcase.googleapis.com/SequenceReport\x12#sequences/{sequence}/sequenceReport\"^\n\x15\x43reateSequenceRequest\x12\x45\n\x08sequence\x18\x01 \x01(\x0b\x32).google.example.showcase.v1beta1.SequenceR\x08sequence\"W\n\x16\x41ttemptSequenceRequest\x12=\n\x04name\x18\x01 \x01(\tB)\xe2\x41\x01\x02\xfa\x41\"\n showcase.googleapis.com/SequenceR\x04name\"_\n\x18GetSequenceReportRequest\x12\x43\n\x04name\x18\x01 \x01(\tB/\xe2\x41\x01\x02\xfa\x41(\n&showcase.googleapis.com/SequenceReportR\x04name2\xa5\x04\n\x0fSequenceService\x12\xa4\x01\n\x0e\x43reateSequence\x12\x36.google.example.showcase.v1beta1.CreateSequenceRequest\x1a).google.example.showcase.v1beta1.Sequence\"/\xda\x41\x08sequence\x82\xd3\xe4\x93\x02\x1e\"\x12/v1beta1/sequences:\x08sequence\x12\xba\x01\n\x11GetSequenceReport\x12\x39.google.example.showcase.v1beta1.GetSequenceReportRequest\x1a/.google.example.showcase.v1beta1.SequenceReport\"9\xda\x41\x04name\x82\xd3\xe4\x93\x02,\x12*/v1beta1/{name=sequences/*/sequenceReport}\x12\x91\x01\n\x0f\x41ttemptSequence\x12\x37.google.example.showcase.v1beta1.AttemptSequenceRequest\x1a\x16.google.protobuf.Empty\"-\xda\x41\x04name\x82\xd3\xe4\x93\x02 \"\x1b/v1beta1/{name=sequences/*}:\x01*\x1a\x1a\xca\x41\x17showcase.googleapis.comB\x88\x01\n#com.google.example.showcase.v1beta1B\rSequenceProtoP\x01Z4github.com/googleapis/gapic-showcase/server/genproto\xea\x02\x19Google::Showcase::V1Beta1b\x06proto3')



_SEQUENCE = DESCRIPTOR.message_types_by_name['Sequence']
_SEQUENCE_RESPONSE = _SEQUENCE.nested_types_by_name['Response']
_SEQUENCEREPORT = DESCRIPTOR.message_types_by_name['SequenceReport']
_SEQUENCEREPORT_ATTEMPT = _SEQUENCEREPORT.nested_types_by_name['Attempt']
_CREATESEQUENCEREQUEST = DESCRIPTOR.message_types_by_name['CreateSequenceRequest']
_ATTEMPTSEQUENCEREQUEST = DESCRIPTOR.message_types_by_name['AttemptSequenceRequest']
_GETSEQUENCEREPORTREQUEST = DESCRIPTOR.message_types_by_name['GetSequenceReportRequest']
Sequence = _reflection.GeneratedProtocolMessageType('Sequence', (_message.Message,), {

  'Response' : _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), {
    'DESCRIPTOR' : _SEQUENCE_RESPONSE,
    '__module__' : 'google.example.showcase.v1beta1.sequence_pb2'
    # @@protoc_insertion_point(class_scope:google.example.showcase.v1beta1.Sequence.Response)
    })
  ,
  'DESCRIPTOR' : _SEQUENCE,
  '__module__' : 'google.example.showcase.v1beta1.sequence_pb2'
  # @@protoc_insertion_point(class_scope:google.example.showcase.v1beta1.Sequence)
  })
_sym_db.RegisterMessage(Sequence)
_sym_db.RegisterMessage(Sequence.Response)

SequenceReport = _reflection.GeneratedProtocolMessageType('SequenceReport', (_message.Message,), {

  'Attempt' : _reflection.GeneratedProtocolMessageType('Attempt', (_message.Message,), {
    'DESCRIPTOR' : _SEQUENCEREPORT_ATTEMPT,
    '__module__' : 'google.example.showcase.v1beta1.sequence_pb2'
    # @@protoc_insertion_point(class_scope:google.example.showcase.v1beta1.SequenceReport.Attempt)
    })
  ,
  'DESCRIPTOR' : _SEQUENCEREPORT,
  '__module__' : 'google.example.showcase.v1beta1.sequence_pb2'
  # @@protoc_insertion_point(class_scope:google.example.showcase.v1beta1.SequenceReport)
  })
_sym_db.RegisterMessage(SequenceReport)
_sym_db.RegisterMessage(SequenceReport.Attempt)

CreateSequenceRequest = _reflection.GeneratedProtocolMessageType('CreateSequenceRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATESEQUENCEREQUEST,
  '__module__' : 'google.example.showcase.v1beta1.sequence_pb2'
  # @@protoc_insertion_point(class_scope:google.example.showcase.v1beta1.CreateSequenceRequest)
  })
_sym_db.RegisterMessage(CreateSequenceRequest)

AttemptSequenceRequest = _reflection.GeneratedProtocolMessageType('AttemptSequenceRequest', (_message.Message,), {
  'DESCRIPTOR' : _ATTEMPTSEQUENCEREQUEST,
  '__module__' : 'google.example.showcase.v1beta1.sequence_pb2'
  # @@protoc_insertion_point(class_scope:google.example.showcase.v1beta1.AttemptSequenceRequest)
  })
_sym_db.RegisterMessage(AttemptSequenceRequest)

GetSequenceReportRequest = _reflection.GeneratedProtocolMessageType('GetSequenceReportRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETSEQUENCEREPORTREQUEST,
  '__module__' : 'google.example.showcase.v1beta1.sequence_pb2'
  # @@protoc_insertion_point(class_scope:google.example.showcase.v1beta1.GetSequenceReportRequest)
  })
_sym_db.RegisterMessage(GetSequenceReportRequest)

_SEQUENCESERVICE = DESCRIPTOR.services_by_name['SequenceService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n#com.google.example.showcase.v1beta1B\rSequenceProtoP\001Z4github.com/googleapis/gapic-showcase/server/genproto\352\002\031Google::Showcase::V1Beta1'
  _SEQUENCE.fields_by_name['name']._options = None
  _SEQUENCE.fields_by_name['name']._serialized_options = b'\342A\001\003'
  _SEQUENCE._options = None
  _SEQUENCE._serialized_options = b'\352A8\n showcase.googleapis.com/Sequence\022\024sequences/{sequence}'
  _SEQUENCEREPORT.fields_by_name['name']._options = None
  _SEQUENCEREPORT.fields_by_name['name']._serialized_options = b'\342A\001\003'
  _SEQUENCEREPORT._options = None
  _SEQUENCEREPORT._serialized_options = b'\352AM\n&showcase.googleapis.com/SequenceReport\022#sequences/{sequence}/sequenceReport'
  _ATTEMPTSEQUENCEREQUEST.fields_by_name['name']._options = None
  _ATTEMPTSEQUENCEREQUEST.fields_by_name['name']._serialized_options = b'\342A\001\002\372A\"\n showcase.googleapis.com/Sequence'
  _GETSEQUENCEREPORTREQUEST.fields_by_name['name']._options = None
  _GETSEQUENCEREPORTREQUEST.fields_by_name['name']._serialized_options = b'\342A\001\002\372A(\n&showcase.googleapis.com/SequenceReport'
  _SEQUENCESERVICE._options = None
  _SEQUENCESERVICE._serialized_options = b'\312A\027showcase.googleapis.com'
  _SEQUENCESERVICE.methods_by_name['CreateSequence']._options = None
  _SEQUENCESERVICE.methods_by_name['CreateSequence']._serialized_options = b'\332A\010sequence\202\323\344\223\002\036\"\022/v1beta1/sequences:\010sequence'
  _SEQUENCESERVICE.methods_by_name['GetSequenceReport']._options = None
  _SEQUENCESERVICE.methods_by_name['GetSequenceReport']._serialized_options = b'\332A\004name\202\323\344\223\002,\022*/v1beta1/{name=sequences/*/sequenceReport}'
  _SEQUENCESERVICE.methods_by_name['AttemptSequence']._options = None
  _SEQUENCESERVICE.methods_by_name['AttemptSequence']._serialized_options = b'\332A\004name\202\323\344\223\002 \"\033/v1beta1/{name=sequences/*}:\001*'
  _SEQUENCE._serialized_start=318
  _SEQUENCE._serialized_end=602
  _SEQUENCE_RESPONSE._serialized_start=438
  _SEQUENCE_RESPONSE._serialized_end=541
  _SEQUENCEREPORT._serialized_start=605
  _SEQUENCEREPORT._serialized_end=1109
  _SEQUENCEREPORT_ATTEMPT._serialized_start=735
  _SEQUENCEREPORT_ATTEMPT._serialized_end=1027
  _CREATESEQUENCEREQUEST._serialized_start=1111
  _CREATESEQUENCEREQUEST._serialized_end=1205
  _ATTEMPTSEQUENCEREQUEST._serialized_start=1207
  _ATTEMPTSEQUENCEREQUEST._serialized_end=1294
  _GETSEQUENCEREPORTREQUEST._serialized_start=1296
  _GETSEQUENCEREPORTREQUEST._serialized_end=1391
  _SEQUENCESERVICE._serialized_start=1394
  _SEQUENCESERVICE._serialized_end=1943
# @@protoc_insertion_point(module_scope)
