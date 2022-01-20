# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v7/services/third_party_app_analytics_link_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.googleads.v7.resources import third_party_app_analytics_link_pb2 as google_dot_ads_dot_googleads_dot_v7_dot_resources_dot_third__party__app__analytics__link__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.api import client_pb2 as google_dot_api_dot_client__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nMgoogle/ads/googleads/v7/services/third_party_app_analytics_link_service.proto\x12 google.ads.googleads.v7.services\x1a\x46google/ads/googleads/v7/resources/third_party_app_analytics_link.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x19google/api/resource.proto\x1a\x17google/api/client.proto\"\x85\x01\n$GetThirdPartyAppAnalyticsLinkRequest\x12]\n\rresource_name\x18\x01 \x01(\tB8\xfa\x41\x35\n3googleads.googleapis.com/ThirdPartyAppAnalyticsLinkR\x0cresourceName\"\x81\x01\n RegenerateShareableLinkIdRequest\x12]\n\rresource_name\x18\x01 \x01(\tB8\xfa\x41\x35\n3googleads.googleapis.com/ThirdPartyAppAnalyticsLinkR\x0cresourceName\"#\n!RegenerateShareableLinkIdResponse2\xe5\x04\n!ThirdPartyAppAnalyticsLinkService\x12\xed\x01\n\x1dGetThirdPartyAppAnalyticsLink\x12\x46.google.ads.googleads.v7.services.GetThirdPartyAppAnalyticsLinkRequest\x1a=.google.ads.googleads.v7.resources.ThirdPartyAppAnalyticsLink\"E\x82\xd3\xe4\x93\x02?\x12=/v7/{resource_name=customers/*/thirdPartyAppAnalyticsLinks/*}\x12\x88\x02\n\x19RegenerateShareableLinkId\x12\x42.google.ads.googleads.v7.services.RegenerateShareableLinkIdRequest\x1a\x43.google.ads.googleads.v7.services.RegenerateShareableLinkIdResponse\"b\x82\xd3\xe4\x93\x02\\\"W/v7/{resource_name=customers/*/thirdPartyAppAnalyticsLinks/*}:regenerateShareableLinkId:\x01*\x1a\x45\xca\x41\x18googleads.googleapis.com\xd2\x41\'https://www.googleapis.com/auth/adwordsB\x8d\x02\n$com.google.ads.googleads.v7.servicesB&ThirdPartyAppAnalyticsLinkServiceProtoP\x01ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v7/services;services\xa2\x02\x03GAA\xaa\x02 Google.Ads.GoogleAds.V7.Services\xca\x02 Google\\Ads\\GoogleAds\\V7\\Services\xea\x02$Google::Ads::GoogleAds::V7::Servicesb\x06proto3')



_GETTHIRDPARTYAPPANALYTICSLINKREQUEST = DESCRIPTOR.message_types_by_name['GetThirdPartyAppAnalyticsLinkRequest']
_REGENERATESHAREABLELINKIDREQUEST = DESCRIPTOR.message_types_by_name['RegenerateShareableLinkIdRequest']
_REGENERATESHAREABLELINKIDRESPONSE = DESCRIPTOR.message_types_by_name['RegenerateShareableLinkIdResponse']
GetThirdPartyAppAnalyticsLinkRequest = _reflection.GeneratedProtocolMessageType('GetThirdPartyAppAnalyticsLinkRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETTHIRDPARTYAPPANALYTICSLINKREQUEST,
  '__module__' : 'google.ads.googleads.v7.services.third_party_app_analytics_link_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v7.services.GetThirdPartyAppAnalyticsLinkRequest)
  })
_sym_db.RegisterMessage(GetThirdPartyAppAnalyticsLinkRequest)

RegenerateShareableLinkIdRequest = _reflection.GeneratedProtocolMessageType('RegenerateShareableLinkIdRequest', (_message.Message,), {
  'DESCRIPTOR' : _REGENERATESHAREABLELINKIDREQUEST,
  '__module__' : 'google.ads.googleads.v7.services.third_party_app_analytics_link_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v7.services.RegenerateShareableLinkIdRequest)
  })
_sym_db.RegisterMessage(RegenerateShareableLinkIdRequest)

RegenerateShareableLinkIdResponse = _reflection.GeneratedProtocolMessageType('RegenerateShareableLinkIdResponse', (_message.Message,), {
  'DESCRIPTOR' : _REGENERATESHAREABLELINKIDRESPONSE,
  '__module__' : 'google.ads.googleads.v7.services.third_party_app_analytics_link_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v7.services.RegenerateShareableLinkIdResponse)
  })
_sym_db.RegisterMessage(RegenerateShareableLinkIdResponse)

_THIRDPARTYAPPANALYTICSLINKSERVICE = DESCRIPTOR.services_by_name['ThirdPartyAppAnalyticsLinkService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n$com.google.ads.googleads.v7.servicesB&ThirdPartyAppAnalyticsLinkServiceProtoP\001ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v7/services;services\242\002\003GAA\252\002 Google.Ads.GoogleAds.V7.Services\312\002 Google\\Ads\\GoogleAds\\V7\\Services\352\002$Google::Ads::GoogleAds::V7::Services'
  _GETTHIRDPARTYAPPANALYTICSLINKREQUEST.fields_by_name['resource_name']._options = None
  _GETTHIRDPARTYAPPANALYTICSLINKREQUEST.fields_by_name['resource_name']._serialized_options = b'\372A5\n3googleads.googleapis.com/ThirdPartyAppAnalyticsLink'
  _REGENERATESHAREABLELINKIDREQUEST.fields_by_name['resource_name']._options = None
  _REGENERATESHAREABLELINKIDREQUEST.fields_by_name['resource_name']._serialized_options = b'\372A5\n3googleads.googleapis.com/ThirdPartyAppAnalyticsLink'
  _THIRDPARTYAPPANALYTICSLINKSERVICE._options = None
  _THIRDPARTYAPPANALYTICSLINKSERVICE._serialized_options = b'\312A\030googleads.googleapis.com\322A\'https://www.googleapis.com/auth/adwords'
  _THIRDPARTYAPPANALYTICSLINKSERVICE.methods_by_name['GetThirdPartyAppAnalyticsLink']._options = None
  _THIRDPARTYAPPANALYTICSLINKSERVICE.methods_by_name['GetThirdPartyAppAnalyticsLink']._serialized_options = b'\202\323\344\223\002?\022=/v7/{resource_name=customers/*/thirdPartyAppAnalyticsLinks/*}'
  _THIRDPARTYAPPANALYTICSLINKSERVICE.methods_by_name['RegenerateShareableLinkId']._options = None
  _THIRDPARTYAPPANALYTICSLINKSERVICE.methods_by_name['RegenerateShareableLinkId']._serialized_options = b'\202\323\344\223\002\\\"W/v7/{resource_name=customers/*/thirdPartyAppAnalyticsLinks/*}:regenerateShareableLinkId:\001*'
  _GETTHIRDPARTYAPPANALYTICSLINKREQUEST._serialized_start=270
  _GETTHIRDPARTYAPPANALYTICSLINKREQUEST._serialized_end=403
  _REGENERATESHAREABLELINKIDREQUEST._serialized_start=406
  _REGENERATESHAREABLELINKIDREQUEST._serialized_end=535
  _REGENERATESHAREABLELINKIDRESPONSE._serialized_start=537
  _REGENERATESHAREABLELINKIDRESPONSE._serialized_end=572
  _THIRDPARTYAPPANALYTICSLINKSERVICE._serialized_start=575
  _THIRDPARTYAPPANALYTICSLINKSERVICE._serialized_end=1188
# @@protoc_insertion_point(module_scope)
