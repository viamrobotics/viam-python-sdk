# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v9/resources/account_link.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.googleads.v9.enums import account_link_status_pb2 as google_dot_ads_dot_googleads_dot_v9_dot_enums_dot_account__link__status__pb2
from google.ads.googleads.v9.enums import linked_account_type_pb2 as google_dot_ads_dot_googleads_dot_v9_dot_enums_dot_linked__account__type__pb2
from google.ads.googleads.v9.enums import mobile_app_vendor_pb2 as google_dot_ads_dot_googleads_dot_v9_dot_enums_dot_mobile__app__vendor__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n4google/ads/googleads/v9/resources/account_link.proto\x12!google.ads.googleads.v9.resources\x1a\x37google/ads/googleads/v9/enums/account_link_status.proto\x1a\x37google/ads/googleads/v9/enums/linked_account_type.proto\x1a\x35google/ads/googleads/v9/enums/mobile_app_vendor.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1cgoogle/api/annotations.proto\"\xb8\x06\n\x0b\x41\x63\x63ountLink\x12R\n\rresource_name\x18\x01 \x01(\tB-\xe2\x41\x01\x05\xfa\x41&\n$googleads.googleapis.com/AccountLinkR\x0cresourceName\x12\x31\n\x0f\x61\x63\x63ount_link_id\x18\x08 \x01(\x03\x42\x04\xe2\x41\x01\x03H\x01R\raccountLinkId\x88\x01\x01\x12^\n\x06status\x18\x03 \x01(\x0e\x32\x46.google.ads.googleads.v9.enums.AccountLinkStatusEnum.AccountLinkStatusR\x06status\x12`\n\x04type\x18\x04 \x01(\x0e\x32\x46.google.ads.googleads.v9.enums.LinkedAccountTypeEnum.LinkedAccountTypeB\x04\xe2\x41\x01\x03R\x04type\x12\x8a\x01\n\x19third_party_app_analytics\x18\x05 \x01(\x0b\x32G.google.ads.googleads.v9.resources.ThirdPartyAppAnalyticsLinkIdentifierB\x04\xe2\x41\x01\x05H\x00R\x16thirdPartyAppAnalytics\x12g\n\x0c\x64\x61ta_partner\x18\x06 \x01(\x0b\x32<.google.ads.googleads.v9.resources.DataPartnerLinkIdentifierB\x04\xe2\x41\x01\x03H\x00R\x0b\x64\x61taPartner\x12\x61\n\ngoogle_ads\x18\x07 \x01(\x0b\x32:.google.ads.googleads.v9.resources.GoogleAdsLinkIdentifierB\x04\xe2\x41\x01\x03H\x00R\tgoogleAds:a\xea\x41^\n$googleads.googleapis.com/AccountLink\x12\x36\x63ustomers/{customer_id}/accountLinks/{account_link_id}B\x10\n\x0elinked_accountB\x12\n\x10_account_link_id\"\xa0\x02\n$ThirdPartyAppAnalyticsLinkIdentifier\x12\x44\n\x19\x61pp_analytics_provider_id\x18\x04 \x01(\x03\x42\x04\xe2\x41\x01\x05H\x00R\x16\x61ppAnalyticsProviderId\x88\x01\x01\x12 \n\x06\x61pp_id\x18\x05 \x01(\tB\x04\xe2\x41\x01\x05H\x01R\x05\x61ppId\x88\x01\x01\x12g\n\napp_vendor\x18\x03 \x01(\x0e\x32\x42.google.ads.googleads.v9.enums.MobileAppVendorEnum.MobileAppVendorB\x04\xe2\x41\x01\x05R\tappVendorB\x1c\n\x1a_app_analytics_provider_idB\t\n\x07_app_id\"b\n\x19\x44\x61taPartnerLinkIdentifier\x12\x31\n\x0f\x64\x61ta_partner_id\x18\x01 \x01(\x03\x42\x04\xe2\x41\x01\x05H\x00R\rdataPartnerId\x88\x01\x01\x42\x12\n\x10_data_partner_id\"s\n\x17GoogleAdsLinkIdentifier\x12K\n\x08\x63ustomer\x18\x03 \x01(\tB*\xe2\x41\x01\x05\xfa\x41#\n!googleads.googleapis.com/CustomerH\x00R\x08\x63ustomer\x88\x01\x01\x42\x0b\n\t_customerB\xfd\x01\n%com.google.ads.googleads.v9.resourcesB\x10\x41\x63\x63ountLinkProtoP\x01ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v9/resources;resources\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V9.Resources\xca\x02!Google\\Ads\\GoogleAds\\V9\\Resources\xea\x02%Google::Ads::GoogleAds::V9::Resourcesb\x06proto3')



_ACCOUNTLINK = DESCRIPTOR.message_types_by_name['AccountLink']
_THIRDPARTYAPPANALYTICSLINKIDENTIFIER = DESCRIPTOR.message_types_by_name['ThirdPartyAppAnalyticsLinkIdentifier']
_DATAPARTNERLINKIDENTIFIER = DESCRIPTOR.message_types_by_name['DataPartnerLinkIdentifier']
_GOOGLEADSLINKIDENTIFIER = DESCRIPTOR.message_types_by_name['GoogleAdsLinkIdentifier']
AccountLink = _reflection.GeneratedProtocolMessageType('AccountLink', (_message.Message,), {
  'DESCRIPTOR' : _ACCOUNTLINK,
  '__module__' : 'google.ads.googleads.v9.resources.account_link_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v9.resources.AccountLink)
  })
_sym_db.RegisterMessage(AccountLink)

ThirdPartyAppAnalyticsLinkIdentifier = _reflection.GeneratedProtocolMessageType('ThirdPartyAppAnalyticsLinkIdentifier', (_message.Message,), {
  'DESCRIPTOR' : _THIRDPARTYAPPANALYTICSLINKIDENTIFIER,
  '__module__' : 'google.ads.googleads.v9.resources.account_link_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v9.resources.ThirdPartyAppAnalyticsLinkIdentifier)
  })
_sym_db.RegisterMessage(ThirdPartyAppAnalyticsLinkIdentifier)

DataPartnerLinkIdentifier = _reflection.GeneratedProtocolMessageType('DataPartnerLinkIdentifier', (_message.Message,), {
  'DESCRIPTOR' : _DATAPARTNERLINKIDENTIFIER,
  '__module__' : 'google.ads.googleads.v9.resources.account_link_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v9.resources.DataPartnerLinkIdentifier)
  })
_sym_db.RegisterMessage(DataPartnerLinkIdentifier)

GoogleAdsLinkIdentifier = _reflection.GeneratedProtocolMessageType('GoogleAdsLinkIdentifier', (_message.Message,), {
  'DESCRIPTOR' : _GOOGLEADSLINKIDENTIFIER,
  '__module__' : 'google.ads.googleads.v9.resources.account_link_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v9.resources.GoogleAdsLinkIdentifier)
  })
_sym_db.RegisterMessage(GoogleAdsLinkIdentifier)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n%com.google.ads.googleads.v9.resourcesB\020AccountLinkProtoP\001ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v9/resources;resources\242\002\003GAA\252\002!Google.Ads.GoogleAds.V9.Resources\312\002!Google\\Ads\\GoogleAds\\V9\\Resources\352\002%Google::Ads::GoogleAds::V9::Resources'
  _ACCOUNTLINK.fields_by_name['resource_name']._options = None
  _ACCOUNTLINK.fields_by_name['resource_name']._serialized_options = b'\342A\001\005\372A&\n$googleads.googleapis.com/AccountLink'
  _ACCOUNTLINK.fields_by_name['account_link_id']._options = None
  _ACCOUNTLINK.fields_by_name['account_link_id']._serialized_options = b'\342A\001\003'
  _ACCOUNTLINK.fields_by_name['type']._options = None
  _ACCOUNTLINK.fields_by_name['type']._serialized_options = b'\342A\001\003'
  _ACCOUNTLINK.fields_by_name['third_party_app_analytics']._options = None
  _ACCOUNTLINK.fields_by_name['third_party_app_analytics']._serialized_options = b'\342A\001\005'
  _ACCOUNTLINK.fields_by_name['data_partner']._options = None
  _ACCOUNTLINK.fields_by_name['data_partner']._serialized_options = b'\342A\001\003'
  _ACCOUNTLINK.fields_by_name['google_ads']._options = None
  _ACCOUNTLINK.fields_by_name['google_ads']._serialized_options = b'\342A\001\003'
  _ACCOUNTLINK._options = None
  _ACCOUNTLINK._serialized_options = b'\352A^\n$googleads.googleapis.com/AccountLink\0226customers/{customer_id}/accountLinks/{account_link_id}'
  _THIRDPARTYAPPANALYTICSLINKIDENTIFIER.fields_by_name['app_analytics_provider_id']._options = None
  _THIRDPARTYAPPANALYTICSLINKIDENTIFIER.fields_by_name['app_analytics_provider_id']._serialized_options = b'\342A\001\005'
  _THIRDPARTYAPPANALYTICSLINKIDENTIFIER.fields_by_name['app_id']._options = None
  _THIRDPARTYAPPANALYTICSLINKIDENTIFIER.fields_by_name['app_id']._serialized_options = b'\342A\001\005'
  _THIRDPARTYAPPANALYTICSLINKIDENTIFIER.fields_by_name['app_vendor']._options = None
  _THIRDPARTYAPPANALYTICSLINKIDENTIFIER.fields_by_name['app_vendor']._serialized_options = b'\342A\001\005'
  _DATAPARTNERLINKIDENTIFIER.fields_by_name['data_partner_id']._options = None
  _DATAPARTNERLINKIDENTIFIER.fields_by_name['data_partner_id']._serialized_options = b'\342A\001\005'
  _GOOGLEADSLINKIDENTIFIER.fields_by_name['customer']._options = None
  _GOOGLEADSLINKIDENTIFIER.fields_by_name['customer']._serialized_options = b'\342A\001\005\372A#\n!googleads.googleapis.com/Customer'
  _ACCOUNTLINK._serialized_start=351
  _ACCOUNTLINK._serialized_end=1175
  _THIRDPARTYAPPANALYTICSLINKIDENTIFIER._serialized_start=1178
  _THIRDPARTYAPPANALYTICSLINKIDENTIFIER._serialized_end=1466
  _DATAPARTNERLINKIDENTIFIER._serialized_start=1468
  _DATAPARTNERLINKIDENTIFIER._serialized_end=1566
  _GOOGLEADSLINKIDENTIFIER._serialized_start=1568
  _GOOGLEADSLINKIDENTIFIER._serialized_end=1683
# @@protoc_insertion_point(module_scope)
