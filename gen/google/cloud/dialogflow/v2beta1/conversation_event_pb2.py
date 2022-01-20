# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/dialogflow/v2beta1/conversation_event.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.cloud.dialogflow.v2beta1 import participant_pb2 as google_dot_cloud_dot_dialogflow_dot_v2beta1_dot_participant__pb2
from google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n8google/cloud/dialogflow/v2beta1/conversation_event.proto\x12\x1fgoogle.cloud.dialogflow.v2beta1\x1a\x31google/cloud/dialogflow/v2beta1/participant.proto\x1a\x17google/rpc/status.proto\x1a\x1cgoogle/api/annotations.proto\"\x9f\x03\n\x11\x43onversationEvent\x12\"\n\x0c\x63onversation\x18\x01 \x01(\tR\x0c\x63onversation\x12K\n\x04type\x18\x02 \x01(\x0e\x32\x37.google.cloud.dialogflow.v2beta1.ConversationEvent.TypeR\x04type\x12\x35\n\x0c\x65rror_status\x18\x03 \x01(\x0b\x32\x12.google.rpc.StatusR\x0b\x65rrorStatus\x12Z\n\x13new_message_payload\x18\x04 \x01(\x0b\x32(.google.cloud.dialogflow.v2beta1.MessageH\x00R\x11newMessagePayload\"{\n\x04Type\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\x18\n\x14\x43ONVERSATION_STARTED\x10\x01\x12\x19\n\x15\x43ONVERSATION_FINISHED\x10\x02\x12\x0f\n\x0bNEW_MESSAGE\x10\x05\x12\x17\n\x13UNRECOVERABLE_ERROR\x10\x04\x42\t\n\x07payloadB\xb4\x01\n#com.google.cloud.dialogflow.v2beta1B\x16\x43onversationEventProtoP\x01ZIgoogle.golang.org/genproto/googleapis/cloud/dialogflow/v2beta1;dialogflow\xf8\x01\x01\xa2\x02\x02\x44\x46\xaa\x02\x1fGoogle.Cloud.Dialogflow.V2beta1b\x06proto3')



_CONVERSATIONEVENT = DESCRIPTOR.message_types_by_name['ConversationEvent']
_CONVERSATIONEVENT_TYPE = _CONVERSATIONEVENT.enum_types_by_name['Type']
ConversationEvent = _reflection.GeneratedProtocolMessageType('ConversationEvent', (_message.Message,), {
  'DESCRIPTOR' : _CONVERSATIONEVENT,
  '__module__' : 'google.cloud.dialogflow.v2beta1.conversation_event_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.dialogflow.v2beta1.ConversationEvent)
  })
_sym_db.RegisterMessage(ConversationEvent)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n#com.google.cloud.dialogflow.v2beta1B\026ConversationEventProtoP\001ZIgoogle.golang.org/genproto/googleapis/cloud/dialogflow/v2beta1;dialogflow\370\001\001\242\002\002DF\252\002\037Google.Cloud.Dialogflow.V2beta1'
  _CONVERSATIONEVENT._serialized_start=200
  _CONVERSATIONEVENT._serialized_end=615
  _CONVERSATIONEVENT_TYPE._serialized_start=481
  _CONVERSATIONEVENT_TYPE._serialized_end=604
# @@protoc_insertion_point(module_scope)
