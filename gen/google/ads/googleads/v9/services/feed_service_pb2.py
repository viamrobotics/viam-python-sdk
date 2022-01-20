# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v9/services/feed_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.googleads.v9.enums import response_content_type_pb2 as google_dot_ads_dot_googleads_dot_v9_dot_enums_dot_response__content__type__pb2
from google.ads.googleads.v9.resources import feed_pb2 as google_dot_ads_dot_googleads_dot_v9_dot_resources_dot_feed__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import client_pb2 as google_dot_api_dot_client__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3google/ads/googleads/v9/services/feed_service.proto\x12 google.ads.googleads.v9.services\x1a\x39google/ads/googleads/v9/enums/response_content_type.proto\x1a,google/ads/googleads/v9/resources/feed.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a google/protobuf/field_mask.proto\x1a\x17google/rpc/status.proto\"]\n\x0eGetFeedRequest\x12K\n\rresource_name\x18\x01 \x01(\tB&\xe2\x41\x01\x02\xfa\x41\x1f\n\x1dgoogleads.googleapis.com/FeedR\x0cresourceName\"\xe0\x02\n\x12MutateFeedsRequest\x12%\n\x0b\x63ustomer_id\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02R\ncustomerId\x12U\n\noperations\x18\x02 \x03(\x0b\x32/.google.ads.googleads.v9.services.FeedOperationB\x04\xe2\x41\x01\x02R\noperations\x12\'\n\x0fpartial_failure\x18\x03 \x01(\x08R\x0epartialFailure\x12#\n\rvalidate_only\x18\x04 \x01(\x08R\x0cvalidateOnly\x12~\n\x15response_content_type\x18\x05 \x01(\x0e\x32J.google.ads.googleads.v9.enums.ResponseContentTypeEnum.ResponseContentTypeR\x13responseContentType\"\xf9\x01\n\rFeedOperation\x12;\n\x0bupdate_mask\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\nupdateMask\x12\x41\n\x06\x63reate\x18\x01 \x01(\x0b\x32\'.google.ads.googleads.v9.resources.FeedH\x00R\x06\x63reate\x12\x41\n\x06update\x18\x02 \x01(\x0b\x32\'.google.ads.googleads.v9.resources.FeedH\x00R\x06update\x12\x18\n\x06remove\x18\x03 \x01(\tH\x00R\x06removeB\x0b\n\toperation\"\xab\x01\n\x13MutateFeedsResponse\x12\x46\n\x15partial_failure_error\x18\x03 \x01(\x0b\x32\x12.google.rpc.StatusR\x13partialFailureError\x12L\n\x07results\x18\x02 \x03(\x0b\x32\x32.google.ads.googleads.v9.services.MutateFeedResultR\x07results\"t\n\x10MutateFeedResult\x12#\n\rresource_name\x18\x01 \x01(\tR\x0cresourceName\x12;\n\x04\x66\x65\x65\x64\x18\x02 \x01(\x0b\x32\'.google.ads.googleads.v9.resources.FeedR\x04\x66\x65\x65\x64\x32\xc9\x03\n\x0b\x46\x65\x65\x64Service\x12\xa5\x01\n\x07GetFeed\x12\x30.google.ads.googleads.v9.services.GetFeedRequest\x1a\'.google.ads.googleads.v9.resources.Feed\"?\xda\x41\rresource_name\x82\xd3\xe4\x93\x02)\x12\'/v9/{resource_name=customers/*/feeds/*}\x12\xca\x01\n\x0bMutateFeeds\x12\x34.google.ads.googleads.v9.services.MutateFeedsRequest\x1a\x35.google.ads.googleads.v9.services.MutateFeedsResponse\"N\xda\x41\x16\x63ustomer_id,operations\x82\xd3\xe4\x93\x02/\"*/v9/customers/{customer_id=*}/feeds:mutate:\x01*\x1a\x45\xca\x41\x18googleads.googleapis.com\xd2\x41\'https://www.googleapis.com/auth/adwordsB\xf7\x01\n$com.google.ads.googleads.v9.servicesB\x10\x46\x65\x65\x64ServiceProtoP\x01ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v9/services;services\xa2\x02\x03GAA\xaa\x02 Google.Ads.GoogleAds.V9.Services\xca\x02 Google\\Ads\\GoogleAds\\V9\\Services\xea\x02$Google::Ads::GoogleAds::V9::Servicesb\x06proto3')



_GETFEEDREQUEST = DESCRIPTOR.message_types_by_name['GetFeedRequest']
_MUTATEFEEDSREQUEST = DESCRIPTOR.message_types_by_name['MutateFeedsRequest']
_FEEDOPERATION = DESCRIPTOR.message_types_by_name['FeedOperation']
_MUTATEFEEDSRESPONSE = DESCRIPTOR.message_types_by_name['MutateFeedsResponse']
_MUTATEFEEDRESULT = DESCRIPTOR.message_types_by_name['MutateFeedResult']
GetFeedRequest = _reflection.GeneratedProtocolMessageType('GetFeedRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETFEEDREQUEST,
  '__module__' : 'google.ads.googleads.v9.services.feed_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v9.services.GetFeedRequest)
  })
_sym_db.RegisterMessage(GetFeedRequest)

MutateFeedsRequest = _reflection.GeneratedProtocolMessageType('MutateFeedsRequest', (_message.Message,), {
  'DESCRIPTOR' : _MUTATEFEEDSREQUEST,
  '__module__' : 'google.ads.googleads.v9.services.feed_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v9.services.MutateFeedsRequest)
  })
_sym_db.RegisterMessage(MutateFeedsRequest)

FeedOperation = _reflection.GeneratedProtocolMessageType('FeedOperation', (_message.Message,), {
  'DESCRIPTOR' : _FEEDOPERATION,
  '__module__' : 'google.ads.googleads.v9.services.feed_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v9.services.FeedOperation)
  })
_sym_db.RegisterMessage(FeedOperation)

MutateFeedsResponse = _reflection.GeneratedProtocolMessageType('MutateFeedsResponse', (_message.Message,), {
  'DESCRIPTOR' : _MUTATEFEEDSRESPONSE,
  '__module__' : 'google.ads.googleads.v9.services.feed_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v9.services.MutateFeedsResponse)
  })
_sym_db.RegisterMessage(MutateFeedsResponse)

MutateFeedResult = _reflection.GeneratedProtocolMessageType('MutateFeedResult', (_message.Message,), {
  'DESCRIPTOR' : _MUTATEFEEDRESULT,
  '__module__' : 'google.ads.googleads.v9.services.feed_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v9.services.MutateFeedResult)
  })
_sym_db.RegisterMessage(MutateFeedResult)

_FEEDSERVICE = DESCRIPTOR.services_by_name['FeedService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n$com.google.ads.googleads.v9.servicesB\020FeedServiceProtoP\001ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v9/services;services\242\002\003GAA\252\002 Google.Ads.GoogleAds.V9.Services\312\002 Google\\Ads\\GoogleAds\\V9\\Services\352\002$Google::Ads::GoogleAds::V9::Services'
  _GETFEEDREQUEST.fields_by_name['resource_name']._options = None
  _GETFEEDREQUEST.fields_by_name['resource_name']._serialized_options = b'\342A\001\002\372A\037\n\035googleads.googleapis.com/Feed'
  _MUTATEFEEDSREQUEST.fields_by_name['customer_id']._options = None
  _MUTATEFEEDSREQUEST.fields_by_name['customer_id']._serialized_options = b'\342A\001\002'
  _MUTATEFEEDSREQUEST.fields_by_name['operations']._options = None
  _MUTATEFEEDSREQUEST.fields_by_name['operations']._serialized_options = b'\342A\001\002'
  _FEEDSERVICE._options = None
  _FEEDSERVICE._serialized_options = b'\312A\030googleads.googleapis.com\322A\'https://www.googleapis.com/auth/adwords'
  _FEEDSERVICE.methods_by_name['GetFeed']._options = None
  _FEEDSERVICE.methods_by_name['GetFeed']._serialized_options = b'\332A\rresource_name\202\323\344\223\002)\022\'/v9/{resource_name=customers/*/feeds/*}'
  _FEEDSERVICE.methods_by_name['MutateFeeds']._options = None
  _FEEDSERVICE.methods_by_name['MutateFeeds']._serialized_options = b'\332A\026customer_id,operations\202\323\344\223\002/\"*/v9/customers/{customer_id=*}/feeds:mutate:\001*'
  _GETFEEDREQUEST._serialized_start=368
  _GETFEEDREQUEST._serialized_end=461
  _MUTATEFEEDSREQUEST._serialized_start=464
  _MUTATEFEEDSREQUEST._serialized_end=816
  _FEEDOPERATION._serialized_start=819
  _FEEDOPERATION._serialized_end=1068
  _MUTATEFEEDSRESPONSE._serialized_start=1071
  _MUTATEFEEDSRESPONSE._serialized_end=1242
  _MUTATEFEEDRESULT._serialized_start=1244
  _MUTATEFEEDRESULT._serialized_end=1360
  _FEEDSERVICE._serialized_start=1363
  _FEEDSERVICE._serialized_end=1820
# @@protoc_insertion_point(module_scope)
