# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/dialogflow/v2beta1/conversation.proto
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
from google.cloud.dialogflow.v2beta1 import audio_config_pb2 as google_dot_cloud_dot_dialogflow_dot_v2beta1_dot_audio__config__pb2
from google.cloud.dialogflow.v2beta1 import conversation_profile_pb2 as google_dot_cloud_dot_dialogflow_dot_v2beta1_dot_conversation__profile__pb2
from google.cloud.dialogflow.v2beta1 import gcs_pb2 as google_dot_cloud_dot_dialogflow_dot_v2beta1_dot_gcs__pb2
from google.cloud.dialogflow.v2beta1 import participant_pb2 as google_dot_cloud_dot_dialogflow_dot_v2beta1_dot_participant__pb2
from google.cloud.dialogflow.v2beta1 import session_pb2 as google_dot_cloud_dot_dialogflow_dot_v2beta1_dot_session__pb2
from google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2google/cloud/dialogflow/v2beta1/conversation.proto\x12\x1fgoogle.cloud.dialogflow.v2beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x32google/cloud/dialogflow/v2beta1/audio_config.proto\x1a:google/cloud/dialogflow/v2beta1/conversation_profile.proto\x1a)google/cloud/dialogflow/v2beta1/gcs.proto\x1a\x31google/cloud/dialogflow/v2beta1/participant.proto\x1a-google/cloud/dialogflow/v2beta1/session.proto\x1a#google/longrunning/operations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x17google/rpc/status.proto\"\xb4\x07\n\x0c\x43onversation\x12\x18\n\x04name\x18\x01 \x01(\tB\x04\xe2\x41\x01\x03R\x04name\x12k\n\x0flifecycle_state\x18\x02 \x01(\x0e\x32<.google.cloud.dialogflow.v2beta1.Conversation.LifecycleStateB\x04\xe2\x41\x01\x03R\x0elifecycleState\x12i\n\x14\x63onversation_profile\x18\x03 \x01(\tB6\xe2\x41\x01\x02\xfa\x41/\n-dialogflow.googleapis.com/ConversationProfileR\x13\x63onversationProfile\x12\x61\n\x0cphone_number\x18\x04 \x01(\x0b\x32\x38.google.cloud.dialogflow.v2beta1.ConversationPhoneNumberB\x04\xe2\x41\x01\x03R\x0bphoneNumber\x12n\n\x12\x63onversation_stage\x18\x07 \x01(\x0e\x32?.google.cloud.dialogflow.v2beta1.Conversation.ConversationStageR\x11\x63onversationStage\x12?\n\nstart_time\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x04\xe2\x41\x01\x03R\tstartTime\x12;\n\x08\x65nd_time\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x04\xe2\x41\x01\x03R\x07\x65ndTime\"Q\n\x0eLifecycleState\x12\x1f\n\x1bLIFECYCLE_STATE_UNSPECIFIED\x10\x00\x12\x0f\n\x0bIN_PROGRESS\x10\x01\x12\r\n\tCOMPLETED\x10\x02\"h\n\x11\x43onversationStage\x12\"\n\x1e\x43ONVERSATION_STAGE_UNSPECIFIED\x10\x00\x12\x17\n\x13VIRTUAL_AGENT_STAGE\x10\x01\x12\x16\n\x12HUMAN_ASSIST_STAGE\x10\x02:\xa3\x01\xea\x41\x9f\x01\n&dialogflow.googleapis.com/Conversation\x12/projects/{project}/conversations/{conversation}\x12\x44projects/{project}/locations/{location}/conversations/{conversation}\"B\n\x17\x43onversationPhoneNumber\x12\'\n\x0cphone_number\x18\x03 \x01(\tB\x04\xe2\x41\x01\x03R\x0bphoneNumber\"\xec\x01\n\x19\x43reateConversationRequest\x12G\n\x06parent\x18\x01 \x01(\tB/\xe2\x41\x01\x02\xfa\x41(\x12&dialogflow.googleapis.com/ConversationR\x06parent\x12W\n\x0c\x63onversation\x18\x02 \x01(\x0b\x32-.google.cloud.dialogflow.v2beta1.ConversationB\x04\xe2\x41\x01\x02R\x0c\x63onversation\x12-\n\x0f\x63onversation_id\x18\x03 \x01(\tB\x04\xe2\x41\x01\x01R\x0e\x63onversationId\"\xb7\x01\n\x18ListConversationsRequest\x12G\n\x06parent\x18\x01 \x01(\tB/\xe2\x41\x01\x02\xfa\x41(\x12&dialogflow.googleapis.com/ConversationR\x06parent\x12\x1b\n\tpage_size\x18\x02 \x01(\x05R\x08pageSize\x12\x1d\n\npage_token\x18\x03 \x01(\tR\tpageToken\x12\x16\n\x06\x66ilter\x18\x04 \x01(\tR\x06\x66ilter\"\x98\x01\n\x19ListConversationsResponse\x12S\n\rconversations\x18\x01 \x03(\x0b\x32-.google.cloud.dialogflow.v2beta1.ConversationR\rconversations\x12&\n\x0fnext_page_token\x18\x02 \x01(\tR\rnextPageToken\"]\n\x16GetConversationRequest\x12\x43\n\x04name\x18\x01 \x01(\tB/\xe2\x41\x01\x02\xfa\x41(\n&dialogflow.googleapis.com/ConversationR\x04name\"b\n\x1b\x43ompleteConversationRequest\x12\x43\n\x04name\x18\x01 \x01(\tB/\xe2\x41\x01\x02\xfa\x41(\n&dialogflow.googleapis.com/ConversationR\x04name\"\xa9\x01\n\x14\x43reateMessageRequest\x12G\n\x06parent\x18\x01 \x01(\tB/\xe2\x41\x01\x02\xfa\x41(\n&dialogflow.googleapis.com/ConversationR\x06parent\x12H\n\x07message\x18\x02 \x01(\x0b\x32(.google.cloud.dialogflow.v2beta1.MessageB\x04\xe2\x41\x01\x02R\x07message\"\xbe\x01\n\x1a\x42\x61tchCreateMessagesRequest\x12G\n\x06parent\x18\x01 \x01(\tB/\xe2\x41\x01\x02\xfa\x41(\n&dialogflow.googleapis.com/ConversationR\x06parent\x12W\n\x08requests\x18\x02 \x03(\x0b\x32\x35.google.cloud.dialogflow.v2beta1.CreateMessageRequestB\x04\xe2\x41\x01\x02R\x08requests\"c\n\x1b\x42\x61tchCreateMessagesResponse\x12\x44\n\x08messages\x18\x01 \x03(\x0b\x32(.google.cloud.dialogflow.v2beta1.MessageR\x08messages\"\xad\x01\n\x13ListMessagesRequest\x12\x42\n\x06parent\x18\x01 \x01(\tB*\xe2\x41\x01\x02\xfa\x41#\x12!dialogflow.googleapis.com/MessageR\x06parent\x12\x16\n\x06\x66ilter\x18\x04 \x01(\tR\x06\x66ilter\x12\x1b\n\tpage_size\x18\x02 \x01(\x05R\x08pageSize\x12\x1d\n\npage_token\x18\x03 \x01(\tR\tpageToken\"\x84\x01\n\x14ListMessagesResponse\x12\x44\n\x08messages\x18\x01 \x03(\x0b\x32(.google.cloud.dialogflow.v2beta1.MessageR\x08messages\x12&\n\x0fnext_page_token\x18\x02 \x01(\tR\rnextPageToken2\x82\x0e\n\rConversations\x12\xa1\x02\n\x12\x43reateConversation\x12:.google.cloud.dialogflow.v2beta1.CreateConversationRequest\x1a-.google.cloud.dialogflow.v2beta1.Conversation\"\x9f\x01\xda\x41\x13parent,conversation\x82\xd3\xe4\x93\x02\x82\x01\"*/v2beta1/{parent=projects/*}/conversations:\x0c\x63onversationZF\"6/v2beta1/{parent=projects/*/locations/*}/conversations:\x0c\x63onversation\x12\x81\x02\n\x11ListConversations\x12\x39.google.cloud.dialogflow.v2beta1.ListConversationsRequest\x1a:.google.cloud.dialogflow.v2beta1.ListConversationsResponse\"u\xda\x41\x06parent\x82\xd3\xe4\x93\x02\x66\x12*/v2beta1/{parent=projects/*}/conversationsZ8\x12\x36/v2beta1/{parent=projects/*/locations/*}/conversations\x12\xee\x01\n\x0fGetConversation\x12\x37.google.cloud.dialogflow.v2beta1.GetConversationRequest\x1a-.google.cloud.dialogflow.v2beta1.Conversation\"s\xda\x41\x04name\x82\xd3\xe4\x93\x02\x66\x12*/v2beta1/{name=projects/*/conversations/*}Z8\x12\x36/v2beta1/{name=projects/*/locations/*/conversations/*}\x12\x91\x02\n\x14\x43ompleteConversation\x12<.google.cloud.dialogflow.v2beta1.CompleteConversationRequest\x1a-.google.cloud.dialogflow.v2beta1.Conversation\"\x8b\x01\xda\x41\x04name\x82\xd3\xe4\x93\x02~\"3/v2beta1/{name=projects/*/conversations/*}:complete:\x01*ZD\"?/v2beta1/{name=projects/*/locations/*/conversations/*}:complete:\x01*\x12\xbd\x02\n\x13\x42\x61tchCreateMessages\x12;.google.cloud.dialogflow.v2beta1.BatchCreateMessagesRequest\x1a<.google.cloud.dialogflow.v2beta1.BatchCreateMessagesResponse\"\xaa\x01\xda\x41\x06parent\x82\xd3\xe4\x93\x02\x9a\x01\"A/v2beta1/{parent=projects/*/conversations/*}/messages:batchCreate:\x01*ZR\"M/v2beta1/{parent=projects/*/locations/*/conversations/*}/messages:batchCreate:\x01*\x12\x89\x02\n\x0cListMessages\x12\x34.google.cloud.dialogflow.v2beta1.ListMessagesRequest\x1a\x35.google.cloud.dialogflow.v2beta1.ListMessagesResponse\"\x8b\x01\xda\x41\x06parent\x82\xd3\xe4\x93\x02|\x12\x35/v2beta1/{parent=projects/*/conversations/*}/messagesZC\x12\x41/v2beta1/{parent=projects/*/locations/*/conversations/*}/messages\x1ax\xca\x41\x19\x64ialogflow.googleapis.com\xd2\x41Yhttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/dialogflowB\xaf\x01\n#com.google.cloud.dialogflow.v2beta1B\x11\x43onversationProtoP\x01ZIgoogle.golang.org/genproto/googleapis/cloud/dialogflow/v2beta1;dialogflow\xf8\x01\x01\xa2\x02\x02\x44\x46\xaa\x02\x1fGoogle.Cloud.Dialogflow.V2beta1b\x06proto3')



_CONVERSATION = DESCRIPTOR.message_types_by_name['Conversation']
_CONVERSATIONPHONENUMBER = DESCRIPTOR.message_types_by_name['ConversationPhoneNumber']
_CREATECONVERSATIONREQUEST = DESCRIPTOR.message_types_by_name['CreateConversationRequest']
_LISTCONVERSATIONSREQUEST = DESCRIPTOR.message_types_by_name['ListConversationsRequest']
_LISTCONVERSATIONSRESPONSE = DESCRIPTOR.message_types_by_name['ListConversationsResponse']
_GETCONVERSATIONREQUEST = DESCRIPTOR.message_types_by_name['GetConversationRequest']
_COMPLETECONVERSATIONREQUEST = DESCRIPTOR.message_types_by_name['CompleteConversationRequest']
_CREATEMESSAGEREQUEST = DESCRIPTOR.message_types_by_name['CreateMessageRequest']
_BATCHCREATEMESSAGESREQUEST = DESCRIPTOR.message_types_by_name['BatchCreateMessagesRequest']
_BATCHCREATEMESSAGESRESPONSE = DESCRIPTOR.message_types_by_name['BatchCreateMessagesResponse']
_LISTMESSAGESREQUEST = DESCRIPTOR.message_types_by_name['ListMessagesRequest']
_LISTMESSAGESRESPONSE = DESCRIPTOR.message_types_by_name['ListMessagesResponse']
_CONVERSATION_LIFECYCLESTATE = _CONVERSATION.enum_types_by_name['LifecycleState']
_CONVERSATION_CONVERSATIONSTAGE = _CONVERSATION.enum_types_by_name['ConversationStage']
Conversation = _reflection.GeneratedProtocolMessageType('Conversation', (_message.Message,), {
  'DESCRIPTOR' : _CONVERSATION,
  '__module__' : 'google.cloud.dialogflow.v2beta1.conversation_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.dialogflow.v2beta1.Conversation)
  })
_sym_db.RegisterMessage(Conversation)

ConversationPhoneNumber = _reflection.GeneratedProtocolMessageType('ConversationPhoneNumber', (_message.Message,), {
  'DESCRIPTOR' : _CONVERSATIONPHONENUMBER,
  '__module__' : 'google.cloud.dialogflow.v2beta1.conversation_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.dialogflow.v2beta1.ConversationPhoneNumber)
  })
_sym_db.RegisterMessage(ConversationPhoneNumber)

CreateConversationRequest = _reflection.GeneratedProtocolMessageType('CreateConversationRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATECONVERSATIONREQUEST,
  '__module__' : 'google.cloud.dialogflow.v2beta1.conversation_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.dialogflow.v2beta1.CreateConversationRequest)
  })
_sym_db.RegisterMessage(CreateConversationRequest)

ListConversationsRequest = _reflection.GeneratedProtocolMessageType('ListConversationsRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTCONVERSATIONSREQUEST,
  '__module__' : 'google.cloud.dialogflow.v2beta1.conversation_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.dialogflow.v2beta1.ListConversationsRequest)
  })
_sym_db.RegisterMessage(ListConversationsRequest)

ListConversationsResponse = _reflection.GeneratedProtocolMessageType('ListConversationsResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTCONVERSATIONSRESPONSE,
  '__module__' : 'google.cloud.dialogflow.v2beta1.conversation_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.dialogflow.v2beta1.ListConversationsResponse)
  })
_sym_db.RegisterMessage(ListConversationsResponse)

GetConversationRequest = _reflection.GeneratedProtocolMessageType('GetConversationRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETCONVERSATIONREQUEST,
  '__module__' : 'google.cloud.dialogflow.v2beta1.conversation_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.dialogflow.v2beta1.GetConversationRequest)
  })
_sym_db.RegisterMessage(GetConversationRequest)

CompleteConversationRequest = _reflection.GeneratedProtocolMessageType('CompleteConversationRequest', (_message.Message,), {
  'DESCRIPTOR' : _COMPLETECONVERSATIONREQUEST,
  '__module__' : 'google.cloud.dialogflow.v2beta1.conversation_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.dialogflow.v2beta1.CompleteConversationRequest)
  })
_sym_db.RegisterMessage(CompleteConversationRequest)

CreateMessageRequest = _reflection.GeneratedProtocolMessageType('CreateMessageRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEMESSAGEREQUEST,
  '__module__' : 'google.cloud.dialogflow.v2beta1.conversation_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.dialogflow.v2beta1.CreateMessageRequest)
  })
_sym_db.RegisterMessage(CreateMessageRequest)

BatchCreateMessagesRequest = _reflection.GeneratedProtocolMessageType('BatchCreateMessagesRequest', (_message.Message,), {
  'DESCRIPTOR' : _BATCHCREATEMESSAGESREQUEST,
  '__module__' : 'google.cloud.dialogflow.v2beta1.conversation_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.dialogflow.v2beta1.BatchCreateMessagesRequest)
  })
_sym_db.RegisterMessage(BatchCreateMessagesRequest)

BatchCreateMessagesResponse = _reflection.GeneratedProtocolMessageType('BatchCreateMessagesResponse', (_message.Message,), {
  'DESCRIPTOR' : _BATCHCREATEMESSAGESRESPONSE,
  '__module__' : 'google.cloud.dialogflow.v2beta1.conversation_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.dialogflow.v2beta1.BatchCreateMessagesResponse)
  })
_sym_db.RegisterMessage(BatchCreateMessagesResponse)

ListMessagesRequest = _reflection.GeneratedProtocolMessageType('ListMessagesRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTMESSAGESREQUEST,
  '__module__' : 'google.cloud.dialogflow.v2beta1.conversation_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.dialogflow.v2beta1.ListMessagesRequest)
  })
_sym_db.RegisterMessage(ListMessagesRequest)

ListMessagesResponse = _reflection.GeneratedProtocolMessageType('ListMessagesResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTMESSAGESRESPONSE,
  '__module__' : 'google.cloud.dialogflow.v2beta1.conversation_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.dialogflow.v2beta1.ListMessagesResponse)
  })
_sym_db.RegisterMessage(ListMessagesResponse)

_CONVERSATIONS = DESCRIPTOR.services_by_name['Conversations']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n#com.google.cloud.dialogflow.v2beta1B\021ConversationProtoP\001ZIgoogle.golang.org/genproto/googleapis/cloud/dialogflow/v2beta1;dialogflow\370\001\001\242\002\002DF\252\002\037Google.Cloud.Dialogflow.V2beta1'
  _CONVERSATION.fields_by_name['name']._options = None
  _CONVERSATION.fields_by_name['name']._serialized_options = b'\342A\001\003'
  _CONVERSATION.fields_by_name['lifecycle_state']._options = None
  _CONVERSATION.fields_by_name['lifecycle_state']._serialized_options = b'\342A\001\003'
  _CONVERSATION.fields_by_name['conversation_profile']._options = None
  _CONVERSATION.fields_by_name['conversation_profile']._serialized_options = b'\342A\001\002\372A/\n-dialogflow.googleapis.com/ConversationProfile'
  _CONVERSATION.fields_by_name['phone_number']._options = None
  _CONVERSATION.fields_by_name['phone_number']._serialized_options = b'\342A\001\003'
  _CONVERSATION.fields_by_name['start_time']._options = None
  _CONVERSATION.fields_by_name['start_time']._serialized_options = b'\342A\001\003'
  _CONVERSATION.fields_by_name['end_time']._options = None
  _CONVERSATION.fields_by_name['end_time']._serialized_options = b'\342A\001\003'
  _CONVERSATION._options = None
  _CONVERSATION._serialized_options = b'\352A\237\001\n&dialogflow.googleapis.com/Conversation\022/projects/{project}/conversations/{conversation}\022Dprojects/{project}/locations/{location}/conversations/{conversation}'
  _CONVERSATIONPHONENUMBER.fields_by_name['phone_number']._options = None
  _CONVERSATIONPHONENUMBER.fields_by_name['phone_number']._serialized_options = b'\342A\001\003'
  _CREATECONVERSATIONREQUEST.fields_by_name['parent']._options = None
  _CREATECONVERSATIONREQUEST.fields_by_name['parent']._serialized_options = b'\342A\001\002\372A(\022&dialogflow.googleapis.com/Conversation'
  _CREATECONVERSATIONREQUEST.fields_by_name['conversation']._options = None
  _CREATECONVERSATIONREQUEST.fields_by_name['conversation']._serialized_options = b'\342A\001\002'
  _CREATECONVERSATIONREQUEST.fields_by_name['conversation_id']._options = None
  _CREATECONVERSATIONREQUEST.fields_by_name['conversation_id']._serialized_options = b'\342A\001\001'
  _LISTCONVERSATIONSREQUEST.fields_by_name['parent']._options = None
  _LISTCONVERSATIONSREQUEST.fields_by_name['parent']._serialized_options = b'\342A\001\002\372A(\022&dialogflow.googleapis.com/Conversation'
  _GETCONVERSATIONREQUEST.fields_by_name['name']._options = None
  _GETCONVERSATIONREQUEST.fields_by_name['name']._serialized_options = b'\342A\001\002\372A(\n&dialogflow.googleapis.com/Conversation'
  _COMPLETECONVERSATIONREQUEST.fields_by_name['name']._options = None
  _COMPLETECONVERSATIONREQUEST.fields_by_name['name']._serialized_options = b'\342A\001\002\372A(\n&dialogflow.googleapis.com/Conversation'
  _CREATEMESSAGEREQUEST.fields_by_name['parent']._options = None
  _CREATEMESSAGEREQUEST.fields_by_name['parent']._serialized_options = b'\342A\001\002\372A(\n&dialogflow.googleapis.com/Conversation'
  _CREATEMESSAGEREQUEST.fields_by_name['message']._options = None
  _CREATEMESSAGEREQUEST.fields_by_name['message']._serialized_options = b'\342A\001\002'
  _BATCHCREATEMESSAGESREQUEST.fields_by_name['parent']._options = None
  _BATCHCREATEMESSAGESREQUEST.fields_by_name['parent']._serialized_options = b'\342A\001\002\372A(\n&dialogflow.googleapis.com/Conversation'
  _BATCHCREATEMESSAGESREQUEST.fields_by_name['requests']._options = None
  _BATCHCREATEMESSAGESREQUEST.fields_by_name['requests']._serialized_options = b'\342A\001\002'
  _LISTMESSAGESREQUEST.fields_by_name['parent']._options = None
  _LISTMESSAGESREQUEST.fields_by_name['parent']._serialized_options = b'\342A\001\002\372A#\022!dialogflow.googleapis.com/Message'
  _CONVERSATIONS._options = None
  _CONVERSATIONS._serialized_options = b'\312A\031dialogflow.googleapis.com\322AYhttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/dialogflow'
  _CONVERSATIONS.methods_by_name['CreateConversation']._options = None
  _CONVERSATIONS.methods_by_name['CreateConversation']._serialized_options = b'\332A\023parent,conversation\202\323\344\223\002\202\001\"*/v2beta1/{parent=projects/*}/conversations:\014conversationZF\"6/v2beta1/{parent=projects/*/locations/*}/conversations:\014conversation'
  _CONVERSATIONS.methods_by_name['ListConversations']._options = None
  _CONVERSATIONS.methods_by_name['ListConversations']._serialized_options = b'\332A\006parent\202\323\344\223\002f\022*/v2beta1/{parent=projects/*}/conversationsZ8\0226/v2beta1/{parent=projects/*/locations/*}/conversations'
  _CONVERSATIONS.methods_by_name['GetConversation']._options = None
  _CONVERSATIONS.methods_by_name['GetConversation']._serialized_options = b'\332A\004name\202\323\344\223\002f\022*/v2beta1/{name=projects/*/conversations/*}Z8\0226/v2beta1/{name=projects/*/locations/*/conversations/*}'
  _CONVERSATIONS.methods_by_name['CompleteConversation']._options = None
  _CONVERSATIONS.methods_by_name['CompleteConversation']._serialized_options = b'\332A\004name\202\323\344\223\002~\"3/v2beta1/{name=projects/*/conversations/*}:complete:\001*ZD\"?/v2beta1/{name=projects/*/locations/*/conversations/*}:complete:\001*'
  _CONVERSATIONS.methods_by_name['BatchCreateMessages']._options = None
  _CONVERSATIONS.methods_by_name['BatchCreateMessages']._serialized_options = b'\332A\006parent\202\323\344\223\002\232\001\"A/v2beta1/{parent=projects/*/conversations/*}/messages:batchCreate:\001*ZR\"M/v2beta1/{parent=projects/*/locations/*/conversations/*}/messages:batchCreate:\001*'
  _CONVERSATIONS.methods_by_name['ListMessages']._options = None
  _CONVERSATIONS.methods_by_name['ListMessages']._serialized_options = b'\332A\006parent\202\323\344\223\002|\0225/v2beta1/{parent=projects/*/conversations/*}/messagesZC\022A/v2beta1/{parent=projects/*/locations/*/conversations/*}/messages'
  _CONVERSATION._serialized_start=614
  _CONVERSATION._serialized_end=1562
  _CONVERSATION_LIFECYCLESTATE._serialized_start=1209
  _CONVERSATION_LIFECYCLESTATE._serialized_end=1290
  _CONVERSATION_CONVERSATIONSTAGE._serialized_start=1292
  _CONVERSATION_CONVERSATIONSTAGE._serialized_end=1396
  _CONVERSATIONPHONENUMBER._serialized_start=1564
  _CONVERSATIONPHONENUMBER._serialized_end=1630
  _CREATECONVERSATIONREQUEST._serialized_start=1633
  _CREATECONVERSATIONREQUEST._serialized_end=1869
  _LISTCONVERSATIONSREQUEST._serialized_start=1872
  _LISTCONVERSATIONSREQUEST._serialized_end=2055
  _LISTCONVERSATIONSRESPONSE._serialized_start=2058
  _LISTCONVERSATIONSRESPONSE._serialized_end=2210
  _GETCONVERSATIONREQUEST._serialized_start=2212
  _GETCONVERSATIONREQUEST._serialized_end=2305
  _COMPLETECONVERSATIONREQUEST._serialized_start=2307
  _COMPLETECONVERSATIONREQUEST._serialized_end=2405
  _CREATEMESSAGEREQUEST._serialized_start=2408
  _CREATEMESSAGEREQUEST._serialized_end=2577
  _BATCHCREATEMESSAGESREQUEST._serialized_start=2580
  _BATCHCREATEMESSAGESREQUEST._serialized_end=2770
  _BATCHCREATEMESSAGESRESPONSE._serialized_start=2772
  _BATCHCREATEMESSAGESRESPONSE._serialized_end=2871
  _LISTMESSAGESREQUEST._serialized_start=2874
  _LISTMESSAGESREQUEST._serialized_end=3047
  _LISTMESSAGESRESPONSE._serialized_start=3050
  _LISTMESSAGESRESPONSE._serialized_end=3182
  _CONVERSATIONS._serialized_start=3185
  _CONVERSATIONS._serialized_end=4979
# @@protoc_insertion_point(module_scope)
