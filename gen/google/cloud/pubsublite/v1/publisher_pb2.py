# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/pubsublite/v1/publisher.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.cloud.pubsublite.v1 import common_pb2 as google_dot_cloud_dot_pubsublite_dot_v1_dot_common__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import client_pb2 as google_dot_api_dot_client__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*google/cloud/pubsublite/v1/publisher.proto\x12\x1agoogle.cloud.pubsublite.v1\x1a\'google/cloud/pubsublite/v1/common.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\"K\n\x15InitialPublishRequest\x12\x14\n\x05topic\x18\x01 \x01(\tR\x05topic\x12\x1c\n\tpartition\x18\x02 \x01(\x03R\tpartition\"\x18\n\x16InitialPublishResponse\"^\n\x15MessagePublishRequest\x12\x45\n\x08messages\x18\x01 \x03(\x0b\x32).google.cloud.pubsublite.v1.PubSubMessageR\x08messages\"_\n\x16MessagePublishResponse\x12\x45\n\x0cstart_cursor\x18\x01 \x01(\x0b\x32\".google.cloud.pubsublite.v1.CursorR\x0bstartCursor\"\xeb\x01\n\x0ePublishRequest\x12\\\n\x0finitial_request\x18\x01 \x01(\x0b\x32\x31.google.cloud.pubsublite.v1.InitialPublishRequestH\x00R\x0einitialRequest\x12k\n\x17message_publish_request\x18\x02 \x01(\x0b\x32\x31.google.cloud.pubsublite.v1.MessagePublishRequestH\x00R\x15messagePublishRequestB\x0e\n\x0crequest_type\"\xe4\x01\n\x0fPublishResponse\x12_\n\x10initial_response\x18\x01 \x01(\x0b\x32\x32.google.cloud.pubsublite.v1.InitialPublishResponseH\x00R\x0finitialResponse\x12_\n\x10message_response\x18\x02 \x01(\x0b\x32\x32.google.cloud.pubsublite.v1.MessagePublishResponseH\x00R\x0fmessageResponseB\x0f\n\rresponse_type2\xcb\x01\n\x10PublisherService\x12h\n\x07Publish\x12*.google.cloud.pubsublite.v1.PublishRequest\x1a+.google.cloud.pubsublite.v1.PublishResponse\"\x00(\x01\x30\x01\x1aM\xca\x41\x19pubsublite.googleapis.com\xd2\x41.https://www.googleapis.com/auth/cloud-platformB\xd8\x01\n!com.google.cloud.pubsublite.protoB\x0ePublisherProtoP\x01ZDgoogle.golang.org/genproto/googleapis/cloud/pubsublite/v1;pubsublite\xf8\x01\x01\xaa\x02\x1aGoogle.Cloud.PubSubLite.V1\xca\x02\x1aGoogle\\Cloud\\PubSubLite\\V1\xea\x02\x1dGoogle::Cloud::PubSubLite::V1b\x06proto3')



_INITIALPUBLISHREQUEST = DESCRIPTOR.message_types_by_name['InitialPublishRequest']
_INITIALPUBLISHRESPONSE = DESCRIPTOR.message_types_by_name['InitialPublishResponse']
_MESSAGEPUBLISHREQUEST = DESCRIPTOR.message_types_by_name['MessagePublishRequest']
_MESSAGEPUBLISHRESPONSE = DESCRIPTOR.message_types_by_name['MessagePublishResponse']
_PUBLISHREQUEST = DESCRIPTOR.message_types_by_name['PublishRequest']
_PUBLISHRESPONSE = DESCRIPTOR.message_types_by_name['PublishResponse']
InitialPublishRequest = _reflection.GeneratedProtocolMessageType('InitialPublishRequest', (_message.Message,), {
  'DESCRIPTOR' : _INITIALPUBLISHREQUEST,
  '__module__' : 'google.cloud.pubsublite.v1.publisher_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.pubsublite.v1.InitialPublishRequest)
  })
_sym_db.RegisterMessage(InitialPublishRequest)

InitialPublishResponse = _reflection.GeneratedProtocolMessageType('InitialPublishResponse', (_message.Message,), {
  'DESCRIPTOR' : _INITIALPUBLISHRESPONSE,
  '__module__' : 'google.cloud.pubsublite.v1.publisher_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.pubsublite.v1.InitialPublishResponse)
  })
_sym_db.RegisterMessage(InitialPublishResponse)

MessagePublishRequest = _reflection.GeneratedProtocolMessageType('MessagePublishRequest', (_message.Message,), {
  'DESCRIPTOR' : _MESSAGEPUBLISHREQUEST,
  '__module__' : 'google.cloud.pubsublite.v1.publisher_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.pubsublite.v1.MessagePublishRequest)
  })
_sym_db.RegisterMessage(MessagePublishRequest)

MessagePublishResponse = _reflection.GeneratedProtocolMessageType('MessagePublishResponse', (_message.Message,), {
  'DESCRIPTOR' : _MESSAGEPUBLISHRESPONSE,
  '__module__' : 'google.cloud.pubsublite.v1.publisher_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.pubsublite.v1.MessagePublishResponse)
  })
_sym_db.RegisterMessage(MessagePublishResponse)

PublishRequest = _reflection.GeneratedProtocolMessageType('PublishRequest', (_message.Message,), {
  'DESCRIPTOR' : _PUBLISHREQUEST,
  '__module__' : 'google.cloud.pubsublite.v1.publisher_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.pubsublite.v1.PublishRequest)
  })
_sym_db.RegisterMessage(PublishRequest)

PublishResponse = _reflection.GeneratedProtocolMessageType('PublishResponse', (_message.Message,), {
  'DESCRIPTOR' : _PUBLISHRESPONSE,
  '__module__' : 'google.cloud.pubsublite.v1.publisher_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.pubsublite.v1.PublishResponse)
  })
_sym_db.RegisterMessage(PublishResponse)

_PUBLISHERSERVICE = DESCRIPTOR.services_by_name['PublisherService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n!com.google.cloud.pubsublite.protoB\016PublisherProtoP\001ZDgoogle.golang.org/genproto/googleapis/cloud/pubsublite/v1;pubsublite\370\001\001\252\002\032Google.Cloud.PubSubLite.V1\312\002\032Google\\Cloud\\PubSubLite\\V1\352\002\035Google::Cloud::PubSubLite::V1'
  _PUBLISHERSERVICE._options = None
  _PUBLISHERSERVICE._serialized_options = b'\312A\031pubsublite.googleapis.com\322A.https://www.googleapis.com/auth/cloud-platform'
  _INITIALPUBLISHREQUEST._serialized_start=170
  _INITIALPUBLISHREQUEST._serialized_end=245
  _INITIALPUBLISHRESPONSE._serialized_start=247
  _INITIALPUBLISHRESPONSE._serialized_end=271
  _MESSAGEPUBLISHREQUEST._serialized_start=273
  _MESSAGEPUBLISHREQUEST._serialized_end=367
  _MESSAGEPUBLISHRESPONSE._serialized_start=369
  _MESSAGEPUBLISHRESPONSE._serialized_end=464
  _PUBLISHREQUEST._serialized_start=467
  _PUBLISHREQUEST._serialized_end=702
  _PUBLISHRESPONSE._serialized_start=705
  _PUBLISHRESPONSE._serialized_end=933
  _PUBLISHERSERVICE._serialized_start=936
  _PUBLISHERSERVICE._serialized_end=1139
# @@protoc_insertion_point(module_scope)
